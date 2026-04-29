# Corporate-suite layout-family assignment

**Status**: assignment v1 · **Date**: 2026-04-29
**Scope**: corporate-suite archetype only.
**Companion files**: `corporate-suite-distinctness-matrix.md` · `corporate-suite-reference-pack.md` · `factory/reports/hardening/corporate-suite-layout-{divergence-plan,variance-rules,family-matrix,family-backfill}.md`.

This is the orchestrator's single-page reference for *which sibling occupies which layout family*, and *what each sibling is locked to* until further notice. The factory hardening reports hold the full reasoning; this file is the short-form lookup.

---

## 1 · Sibling → family map

| Sibling | Slug | Family | L1–L9 tuple | Status |
|---|---|---|---|---|
| **Pragma** (advisory) | `pragma` | **LF-1 · Boardroom Vertical** | `split-55-45 · A · absent · numbered-grid · band-at-3 · typographic-grid · list-row · sticky-top · 3-col` | Active · reference shape · no migration |
| **Fiscus** (commercialista) | `fiscus` | **LF-3 · Compliance Calendar** | `split-55-45 · A+slot4 · slot-4 · numbered-grid · band-at-3 · typographic-grid · list-row · sticky-top · 3-col` | Active · slot-4 calendar IS the family · no migration |
| **Solaria** (executive coaching) | `solaria` | **LF-4 · Manifesto-First** | `split-55-45 · C · slot-5 · manifesto-replacement · band-at-5 · absent · list-row · sticky-top · 3-col` | Active · multilingual GREEN · public-flip held · no migration |
| **Continua** (stewardship) — **current** | `continua` | **LF-3** (in-family overlap with Fiscus) | `split-55-45 · A+slot4 · slot-4 · numbered-grid · band-at-3 · typographic-grid · list-row · sticky-top · 3-col` | **Superseded — pending migration to LF-5** |
| **Continua** (stewardship) — **target** | `continua` | **LF-5 · Stewardship Object-Hero** | `object-overlay · D · slot-2 · 2x2-with-image · band-at-4 · pillar-photo · timeline · condensed-minimal-top · 4-col-with-whistleblowing` | Target · IT-only rebuild · multilingual deferred |

Per `corporate-suite-layout-variance-rules.md` CS-LAYOUT-11: families are exclusive. After Continua → LF-5, four families are claimed (LF-1, LF-3, LF-4, LF-5). LF-2 is open for the 5th sibling. LF-6 is reserved.

---

## 2 · Why each sibling sits in its family

Plain operational reasoning — what about the firm makes the family the right fit.

### Pragma → LF-1
Multi-partner advisory firm. Partners + ODCEC credentials carry the proof. Numeric KPIs are the badge of seriousness. Institution itself is the value — no named cadence cell needed. This is exactly LF-1's reference profile, and Pragma's home is the literal shape LF-1 was defined from.

### Fiscus → LF-3
Commercialista presidio · revisione legale · OAM-supervised brokerage profile. The firm's value lives in deadlines (mese · scadenza · ambito calendar). The slot-4 cycle cell is **structurally** what makes this firm different from a general advisory — and that structural fact is precisely what LF-3 captures.

### Solaria → LF-4
Executive coaching · single-coach firm. The method-statement (manifesto + percorsi enumeration + method-cadenza) IS the proposition. There are no partners to display, so a leadership grid would be empty by construction — LF-4 declares L6=`absent` and turns the empty-grid debt into a designed feature. Solaria already shipped this shape; the family slot retroactively names it.

### Continua → LF-5 (target)
Stewardship · custody · family-office · notarile · archive-led continuity profile. The proof is the **object** — the seal, the codex, the ledger, the deed — and the cadence is **governance**, not deadline. LF-5's object-overlay hero, slot-2 governance-cycle, 4-pillar custodia matrix, pillar-photo leadership (environmental portraits in archive vault / partner desk / boardroom), and timeline cases all map to the firm's shape.

The reason Continua sits at LF-3 today is historical — the cluster only had a Fiscus-shaped shell available when Continua was first built, and the (presidio · figura · orizzonte) cycle was retro-fitted into the slot-4 calendar cell. The migration corrects that.

---

## 3 · Per-sibling freeze list

Until the Continua rebuild closes IT-green at LF-5, the following surfaces are frozen.

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
- Wireframe regression budget: **0 px** vs pre-rebuild capture.

### Fiscus (LF-3) — full freeze
- All LF-1 surfaces, plus:
- `cs-cycle` at slot-4 with three `(eyebrow=mese, figure=scadenza, context=ambito)` cells.
- 4-card typographic leadership (Fiscus's variant).
- Wireframe regression budget: **0 px**.

### Solaria (LF-4) — full freeze + state-lock
- `cs-manifesto` block at slot-2 (replaces pillars).
- `cs-percorsi` enumeration at slot-3.
- Dark KPI band at slot-4.
- `cs-cycle` at slot-5 with `(inizio · cadenza · fine)` method cells.
- Leadership section omitted (L6=`absent` is the family's choice; do not re-introduce).
- List-row cases at slot-6.
- Dark CTA closer at slot-7.
- 5-locale registry · `tier=draft` · public-flip held pending user authorization (R-SOL-8).
- `?preview=1` propagation across chrome (closed in `phase_x4_corporate_suite_case_parent_fix`).
- Wireframe regression budget: **0 px**.

### Continua (LF-3 today) — preserved until rebuild
- Existing IT-only render preserved as-is.
- Imagery pack preserved (object-led from Pass 1; carries forward into LF-5 unchanged).
- IT cycle copy preserved — text reused at slot-2 in LF-5.
- `tier=draft` · IT-only locale list.
- No edits to the shared `home.html` until rebuild starts (any edit cascades to Pragma · Fiscus · Solaria).

---

## 4 · Cluster invariants (inherited by every family)

Per CS-LAYOUT-20. These hold across LF-1, LF-3, LF-4, LF-5 — and across LF-2, LF-6, LF-{NEW} when they enroll. A family that proposes deviation triggers a § decision review.

- Serif heading + sans body family · italic-`<em>` emphasis · no bold · no uppercase headings.
- Cream paper baseline · accent budget ≤3 hits per viewport.
- h1 AAA contrast on cream · dark-section descendant contrast ≥ AA + ΔL ≥120.
- Pexels-only imagery · zero URL overlap across siblings · 3-second subject check.
- Locale-pill switcher · `lang` + `dir` per link · Latin wordmark + numerics in RTL · voice anchor verbatim across 5 locales.
- 100×72 section padding · max-width 1400px.
- Density ceilings (CS-DENSITY-01..07).
- One dark band per home (CS-TONE-03).
- Reduced-motion honoured.
- Editor click-to-edit isolated by `body.mw-is-editor-preview`.
- CTA contract — one primary per viewport, advisor-voice, real route hrefs.
- `:focus-visible` gold ring (2px outline + 4px offset).
- Whistleblowing legal-row entry where D.lgs. 24/2023 applies.
- ≤720px responsive collapse — hero stacks · nav becomes hamburger drawer · footer collapses.

---

## 5 · Sibling-pair distinctness scoring

Counting differences in L1–L9 tuple. CS-LAYOUT-12 requires ≥4 of 9 dimensions to differ between any two siblings.

| Pair | Today (Continua at LF-3) | After Continua → LF-5 |
|---|---|---|
| Pragma vs Fiscus | 2/9 (L2, L3) — passes barely | 2/9 (unchanged · audit deferred per plan §10 Step 7) |
| Pragma vs Solaria | 5/9 (L2, L3, L4, L5, L6) | 5/9 |
| Pragma vs Continua | **2/9 (L2, L3) — CS-LAYOUT-12 FAIL state** | **9/9 different** |
| Fiscus vs Solaria | 5/9 (L2, L3, L4, L5, L6) | 5/9 |
| Fiscus vs Continua | **0/9 — F-LAYOUT-01 FAIL state** | **8/9 (only L8 close — both sticky-top variants)** |
| Solaria vs Continua | 5/9 (L2, L3, L4, L5, L6) | 8/9 (L1, L2, L3, L4, L5, L6, L7, L9) |

The migration converts the two failing rows (Pragma↔Continua and Fiscus↔Continua) into wide-margin passes. The Pragma↔Fiscus 2/9 score remains and is queued for a separate audit pass — out of scope for the Continua rebuild.

---

## 6 · Open territory

After Continua → LF-5 lands, the cluster's remaining family slots:

| Family | Status | Next sibling profile |
|---|---|---|
| LF-2 · Editorial Spread | OPEN | Architecture studio · evidence-led legal · independent directorship · audit methodology · 5th sibling enrollment per divergence plan §10 Step 6 |
| LF-6 · Rail-Side Chrome | RESERVED | Magazine-edited boutique · public-hearing law · conservation studio · 6th–7th sibling |
| LF-{NEW} | OPEN | Any candidate that doesn't fit LF-1..LF-6; planner files an addendum to the family matrix declaring the new L1–L9 tuple before build |

LF-1, LF-3, LF-4, LF-5 are CLAIMED. Re-use is permitted only via DISTINCTNESS_RULES §5 option 3 (variant demotion) with explicit user approval.

---

## 7 · Authority and update protocol

- **This file is the orchestrator's reference**. The factory hardening report (`corporate-suite-family-backfill.md`) is the authoritative record of *why* assignments hold. The family matrix (`factory/reports/hardening/corporate-suite-layout-family-matrix.md`) is the source of truth for *what each family declares*.
- **Each new sibling adds a row to §1** at intake (declared) and at walk (rendered). Drift between declared and rendered = CS-LAYOUT-14 fail.
- **Migrations annotate, not overwrite**. Continua's LF-3 row stays as `Superseded` once the LF-5 row goes Active.
- **The freeze list in §3 is enforced by the rebuild session** — the rebuilder reads §3 before any code change and confirms the regression walks at the end.

---

## 8 · Pointer to the migration brief

Continua's LF-3 → LF-5 migration is the single open work item this assignment generates. The implementation-ready hand-off is:

> `design-orchestrator/references/internal-baselines/continua-lf5-migration-brief.md`

That brief is what the rebuild session reads first.
