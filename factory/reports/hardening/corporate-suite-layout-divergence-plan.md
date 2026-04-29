# Corporate-suite layout divergence — operational plan

**Status**: hardening plan v1 · **Date**: 2026-04-29 · **Branch**: `phase-x4b-corporate-suite-layout-divergence`
**Scope**: corporate-suite archetype only. No application code changed in this pass.
**Companions**: `corporate-suite-layout-variance-rules.md` (rule book) · `corporate-suite-layout-family-matrix.md` (slotting).
**Inputs read**: `design-orchestrator/references/internal-baselines/corporate-suite-{distinctness-matrix,reference-pack}.md` · `design-orchestrator/{DISTINCTNESS_RULES,NEXT_STEPS}.md` · `factory/standards/corporate-suite-{design-standard,blocking-rules}.md` · `factory/reports/{solaria,continua}/*` · `templates/live_templates/business/corporate-suite/{home,_base}.html`.

---

## 1 · Why current siblings still feel too similar

The four current corporate-suite siblings — Pragma (advisory), Fiscus (commercialista), Solaria (coaching), Continua (stewardship) — all pass the existing 5-axis distinctness matrix at 4–5 of 5 vs every neighbour, yet still read as variants of one master template. The reason is **structural**: the matrix scores **skin-level** axes (palette · imagery · voice · typography · "structural rhythm") but the load-bearing axis-5 ("structural rhythm") is currently scoped narrowly to *section count and dark-band placement* and is in practice a near-invariant across all four siblings.

Concretely:

- All four templates render the **same DOM shell** from a single shared file (`templates/live_templates/business/corporate-suite/home.html`, 687 lines). The section sequence is hardcoded:
  `cs-hero · cs-pillars · cs-kpi-band · {cs-cycle?} · cs-sectors · cs-trust · cs-leadership · cs-cases-preview · cs-cta`.
- The only structural variance currently expressible in the skin is **one optional `<section class="cs-cycle">` cell** gated on `if page_data.cycle_strip` (`home.html:578`). That is a single boolean, not a layout family.
- Hero is a hard cluster invariant: `display: grid; grid-template-columns: 1.3fr 1fr; min-height: 620px` (`home.html:11`). Every sibling renders serif-h1-LEFT + photo-RIGHT in the same proportions. CS-HERO-01 explicitly **blocks** any other hero shape.
- Navbar is identical across all four (`_base.html:1039–1061`): sticky, primary-background, wordmark-left + 5-link-row + phone-right. CS-NAV-01 blocks deviation.
- Footer is identical across all four (`_base.html:1065–1108`): three-column brand + sitemap + contact + offices, primary-background. CS-FOOT-01 fixes the columns.
- Cases preview is the same `list-row` shape (`home.html:658–671`) for every sibling.
- Leadership is a `repeat(auto-fit, minmax(280px, 1fr))` card grid in every sibling.

The "differentiation" the matrix scores happens **inside** the cells:
- Pragma's hero meta-strip carries `(HQ · Equipe · Mandati)`; Fiscus carries a fiscal-calendar tuple; Solaria carries a percorso-cadenza tuple; Continua carries a governance-cycle tuple. **All four use the same `<div class="meta-strip">` DOM** with different copy.
- The cycle-strip differentiator (Fiscus calendar / Solaria method-cadenza / Continua governance-cycle) is **the same `<section class="cs-cycle">` DOM** with different labels.
- Palette tokens (navy / gold / ocra / brass) drive `--primary` `--secondary` `--accent` — all CSS variables on the same DOM.

Net effect: the cluster scores well on every axis the matrix watches, but a wireframe outline of any two siblings overlays at >90% identical bounding boxes. Side-by-side captures look like four palette skins of one template, which is precisely what the user is reporting.

This is not a quality regression — every sibling shipped under a clean scorecard. It is a **gap in what the matrix measures**: layout grammar was never promoted to a first-class differentiation axis, so the system has been optimising the things it can see and ignoring the thing it can't.

---

## 2 · The shared structural traits causing sameness

Inventory of what is identical across Pragma/Fiscus/Solaria/Continua at the DOM/layout level. Each row is a sameness vector that must be addressed.

| # | Shared trait | Where it lives | What it forces |
|---|---|---|---|
| S1 | **One shared `home.html`** with hardcoded section order | `home.html:524–684` | All four siblings render the same `<section>` list in the same order. |
| S2 | **55/45 hero split serif-L + photo-R** as cluster invariant | `home.html:10–14` · CS-HERO-01 [BLOCKING] | No sibling can ship a stacked, side-rail, object-overlay, or type-only hero. |
| S3 | **Hero meta-strip is a horizontal `(label, value)` tuple** | `home.html:533–537` | Differentiation forced into copy of three flex-items, not into shape. |
| S4 | **Pillars are a 3-or-4 col `auto-fit` grid with numbered serif** | `home.html:106` · CS-DENSITY-02 | No vertical-stagger, side-quote, image-paired, or essay-replacement variant available. |
| S5 | **Dark KPI band always at section position 3** | CS-RHYTHM-02 / CS-RHYTHM-03 [REQUIRED] | KPI cannot promote into hero, demote to closer, or be replaced by a narrative band. |
| S6 | **Sectors ribbon + trust marquee always between KPI and leadership** | `home.html:599–625` | Two adjacent ribbon-shaped sections in a row — a structural fingerprint. |
| S7 | **Leadership block is always rendered** | `home.html:627–648` (no `{% if %}` gate) | Solaria ships an empty card grid even though it's a single-coach firm; the section can't be omitted. |
| S8 | **Cases preview is always `list-row` with thumb + arrow** | `home.html:650–672` | No grid, collage, timeline, or single-feature variant. |
| S9 | **CTA closer is always a dark band** at the bottom | `home.html:674–684` · CS-CTA-05 | Cream-on-cream hairline closer is not expressible. |
| S10 | **Sticky-top primary navbar with 5-link inline row + phone-right** | `_base.html:1039–1061` · CS-NAV-01 [BLOCKING] | Side-rail, drawer-only, split-wordmark, or condensed-minimal navs are blocked. |
| S11 | **Three-column footer: brand + sitemap + contact + offices** | `_base.html:1065–1108` · CS-FOOT-01 | 4-col with whistleblowing column, 2-col stacked, or single-row condensed footers are blocked. |
| S12 | **All four siblings use the same `<section class="cs-*">` class names** | universal | Style-critic side-by-side comparators see identical class lists. |

S1 is the root cause; S2–S11 are its emanations through the standards layer. Fixing S1 by introducing layout families is the lever.

---

## 3 · Layout dimensions that must become first-class differentiation axes

The current 5-axis matrix (voice · palette · imagery · typography · structural rhythm) collapses everything structural into axis 5, which is then enforced almost exclusively as "section count + dark-band placement." We expand axis 5 into **nine named layout dimensions**, and we lift them to first-class status alongside the existing four skin axes. Every dimension below is enforced at the DOM layer — different code paths, not different copy.

| # | Layout dimension | What is varied | Today's range | Target range |
|---|---|---|---|---|
| L1 | **Hero geometry** | The shape and split of the hero section | 1 shape (55/45 split serif-L + photo-R) | ≥4 shapes (split-55-45 · stacked-editorial · object-overlay · side-rail-photo · type-only) |
| L2 | **Section sequence** | The ordered list of `<section>` blocks on home | 1 fixed sequence | ≥4 sequences, one per layout family |
| L3 | **Mid-strip differentiator slot** | Which position carries the family's named cadence cell | Always slot 4 (between KPI and sectors), or absent | Slots 2 / 4 / 6, or absent — declared per family |
| L4 | **Pillars treatment** | The visual shape of the pillars/competence section | 1 shape (3–4 col `auto-fit` numbered grid) | ≥4 shapes (numbered-grid · vertical-stagger · 2×2-with-image · essay-with-anchors · side-quote-with-cards) |
| L5 | **KPI placement** | Where the dark-grounding figure-band sits | Always position 3 | {hero-overlay · band-at-3 · band-at-5 · band-at-closer · narrative-prose-replacement} |
| L6 | **Leadership presence** | Whether and how the people block renders | Always typographic-or-photo grid | {absent · typographic · photo-grid · single-portrait-feature · pillar-photo} |
| L7 | **Cases-preview shape** | The DOM shape of the cases preview list | Always `list-row` with thumb | {list-row · magazine-grid · timeline · collage-3+1 · single-feature + sub-list} |
| L8 | **Navbar geometry** | The chrome's structural placement | Always sticky-top primary-bg | {sticky-top · side-rail · drawer-only · split-wordmark-top · condensed-minimal-top} |
| L9 | **Footer structure** | Column count and content shape | Always 3-col brand+sitemap+contact+offices | {3-col · 4-col-with-whistleblowing · 2-col-stacked · full-bleed-crest · condensed-single-row} |

L1, L2, L7, L8 are the four highest-leverage dimensions — they change the wireframe outline. L3, L4, L5, L6, L9 amplify the diff but matter less if L1+L2+L7+L8 already differ.

These dimensions are codified as `CS-LAYOUT-*` rules in `corporate-suite-layout-variance-rules.md`.

---

## 4 · The four (+1) layout families

Each layout family is a **distinct DOM scaffold** that picks a value from each of the nine layout dimensions L1–L9. The rule is: **two siblings cannot share a layout family**. A new sibling without an open family slot must either claim a new family or wait.

> Full per-family slotting is in `corporate-suite-layout-family-matrix.md`. Summary here.

### LF-1 · Boardroom Vertical
Reference shape for **multi-partner advisory firms with NDA-anchored proof.** The "default" composition the cluster started from. Hero is the 55/45 serif-L + photo-R split; pillars are the numbered 3-up grid; KPI band is dark at position 3; leadership is the typographic 3-card row; cases are list-row; CTA is the dark band closer. Footer is 3-col.
- L1=split-55-45 · L2=A · L3=absent · L4=numbered-grid · L5=band-at-3 · L6=typographic · L7=list-row · L8=sticky-top · L9=3-col

### LF-2 · Editorial Spread
Reference shape for **portfolio-of-work-led firms** (architecture, evidence-led legal, independent directorships). Hero is **stacked**: full-bleed editorial photo TOP with credit overlay, serif h1 + side-quoted intro BELOW (8/4 col). Pillars are replaced by an **editorial narrative band** with pull quotes and an anchor-rail. KPI is **promoted into the hero credit overlay**, no dark band. Sectors is a sentence-ribbon. Leadership is a **single-portrait masthead**. Cases are a **magazine 3+1 grid**. CTA is a hairline-bordered cream band. Footer is 4-col.
- L1=stacked-editorial · L2=B · L3=absent · L4=essay-with-anchors · L5=hero-overlay · L6=single-portrait · L7=magazine-grid · L8=split-wordmark-top · L9=4-col-with-whistleblowing

### LF-3 · Compliance Calendar
Reference shape for **deadline-anchored regulated practices** (commercialista, revisione legale, OAM-supervised brokerage). Inherits LF-1's hero, pillars, KPI; **claims slot-4 for a calendar-cadence cell** (the single thing that makes Fiscus structurally distinct today). Leadership is typographic 4-card. Cases are list-row.
- L1=split-55-45 · L2=A+slot4 · L3=slot-4 · L4=numbered-grid · L5=band-at-3 · L6=typographic · L7=list-row · L8=sticky-top · L9=3-col

### LF-4 · Manifesto-First
Reference shape for **method-declared single-practitioner firms** (executive coach, fiduciary, public-trust independent director). **Manifesto block replaces pillars at position 2.** Three-step enumeration at position 3 (typographic with cadence anchor). Dark KPI band shifts to position 4. Method-cadenza-strip at position 5. **Leadership is omitted.** Cases at position 6. CTA dark closer.
- L1=split-55-45 · L2=C · L3=slot-5 · L4=manifesto-replacement · L5=band-at-5 · L6=absent · L7=list-row · L8=sticky-top · L9=3-col

### LF-5 · Stewardship Object-Hero
Reference shape for **custody / family-office / notarile / archive-led practices.** Hero is rebuilt as **object-overlay**: full-bleed object-led photo (no people) with TWO credit-block overlays + serif h1 overlaid lower-third (no 55/45 split). Pillars become a **4-pillar custodia matrix** (presidio/governance/successione/compliance). **Cycle-strip is promoted to position 2**, immediately after hero. Dark KPI band at position 4 (post-cycle). Sectors band carries an explicit **whistleblowing surface** (D.lgs. 24/2023). Leadership uses **pillar-photo** framing (3 cards, environmental portraits not portrait-headshot). Cases are a **timeline list** (year + mandate + horizon). CTA is a tinted-cream hairline band. Footer is 4-col with whistleblowing column.
- L1=object-overlay · L2=D · L3=slot-2 · L4=2x2-with-image · L5=band-at-4 · L6=pillar-photo · L7=timeline · L8=condensed-minimal-top · L9=4-col-with-whistleblowing

### LF-6 · Rail-Side Chrome (RESERVED)
Reserved for the 6th sibling onwards — kept on file so the matrix has a known next slot. **Vertical sidebar nav** replaces sticky-top. Hero shifts full-width-right with chrome on left. Magazine-style scroll cadence with pull-quotes. Footer is condensed single-row. Suitable for **magazine-edited boutique firms** (audit-led methodology, public-hearing law, conservation studios).
- L1=side-rail-photo · L2=E · L3=slot-6 · L4=side-quote-with-cards · L5=narrative-prose-replacement · L6=photo-grid · L7=collage-3+1 · L8=side-rail · L9=condensed-single-row

LF-1..LF-5 are the four required (+1) families. LF-6 is the deliberate next-slot to prevent the matrix from re-collapsing once siblings 5+ land.

---

## 5 · Where each current sibling should map

| Sibling | Current state | Should map to | Action required |
|---|---|---|---|
| **Pragma** | LF-1 (Boardroom Vertical) | LF-1 | None. Pragma is the reference shape; it stays. (Audit only — confirm no L4/L7 drift creeping in.) |
| **Fiscus** | LF-3 (Compliance Calendar) without explicit family declaration | LF-3 | Document the slot-4 calendar cell as the family's identity, not as a one-off. No DOM change. |
| **Solaria** | LF-4 (Manifesto-First) without explicit family declaration | LF-4 | Document the manifesto+omitted-leadership shape as LF-4. No DOM change. The current home is already structurally LF-4 in spirit; the family slot just names it. |
| **Continua** | **LF-3** today (DOM-identical to Fiscus, only the cycle-strip copy differs) | **LF-5** (Stewardship Object-Hero) | **Rebuild needed** — object-overlay hero · cycle promoted to slot-2 · 4-pillar matrix · timeline cases · 4-col footer with whistleblowing. This is the work that justifies the layout-family system. |

This mapping has two consequences:
1. Pragma + Fiscus + Solaria require **no source code changes** to fit the new system. They are retrospectively classified into LF-1/LF-3/LF-4 — the system describes the state we already shipped.
2. Continua **does not yet fit** any layout family that distinguishes it from Fiscus. It has been holding LF-3 with a different cycle-strip composition, which is an in-family variation, not a family-distinct sibling. That is the visible-design failure the user diagnosed. The fix is to migrate Continua to LF-5 in IT-only **before** running its multilingual pass.

---

## 6 · What future siblings must not repeat

The cluster's prohibition list grows monotonically. Items below extend the existing distinctness matrix bans (palette / imagery / hero-meta / etc.) with **layout-level** bans.

After Pragma, Fiscus, Solaria, Continua land in their target families, the next sibling MUST NOT:

- Pick **LF-1** unless explicitly demoted to a Pragma variant under DISTINCTNESS_RULES §5 option 3.
- Pick **LF-3** (Fiscus's slot-4 calendar shape) — taken.
- Pick **LF-4** (Solaria's manifesto-replacement) — taken.
- Pick **LF-5** (Continua's object-overlay) — taken.
- Re-render Pragma/Fiscus's `list-row` cases preview without compensating changes on hero geometry AND pillars treatment AND footer structure (≥3 of 4 macro dimensions must differ when one is reused).
- Use a 55/45 hero split AND a sticky-top primary navbar AND a 3-col footer AND a numbered-grid pillars AND a list-row cases simultaneously — that combination is reserved for LF-1.
- Insert a `<section class="cs-cycle">` mid-strip at slot-4 with three `(eyebrow, figure, context)` cells — Fiscus's exact shape.
- Render an **empty** leadership grid because the firm is single-practitioner — pick LF-4 (omits the section) or LF-2 (replaces it with a single-portrait masthead) or define a new family.
- Render a hero with people AND a leadership block with portraits AND a sectors marquee on the same home — Pragma's exact composition.
- Add a SECOND optional mid-strip cell to a layout family that already declared one — if a family wants two beats, it claims slots 2 AND 4 explicitly (LF-5 does this), it does not silently grow.

This list extends `corporate-suite-distinctness-matrix.md §1.8` (section rhythm) and `corporate-suite-reference-pack.md §1` ("don't clone") with layout-family bans.

---

## 7 · What may stay archetype-shared vs what must vary

The cluster's identity (institutional-advisory · serif heading + sans body · cream paper · Pexels imagery · 5-locale voice anchor · ≤3 accent hits per viewport · AAA contrast on h1) is a **brand contract**, not a layout. Layout families inherit the brand contract; they vary only on the nine layout dimensions L1–L9.

### Stays archetype-shared (CS-* invariants — never vary by family)

- Typography family — serif heading + sans body (CS-TYPE-01 BLOCKING).
- Italic-`<em>` emphasis on h1 + h2, no bold/no uppercase (CS-TYPE-02 BLOCKING).
- Eyebrow letter-spacing 0.22em uppercase, body 0 (CS-TYPE-05).
- Cream paper baseline (`--paper`/`--paper-2`) on every non-dark surface.
- Accent budget ≤3 hits per viewport (CS-PAL-05).
- AAA h1 contrast on cream (CS-HERO-03 / CS-BLOCK-01 BLOCKING).
- Dark-section descendant contrast ≥ AA + distance ≥120 (CS-PAL-04 / CS-BLOCK-17 BLOCKING).
- Locale switcher pill with `lang` + `dir` per link (CS-NAV-03).
- Voice anchor verbatim across 5 locales (CS-EXEC-01 / F2 BLOCKING).
- Pexels-only imagery, zero URL overlap across siblings (CS-IMG-SRC-01 / CS-IMG-SRC-04 BLOCKING).
- `:focus-visible` gold ring, 2px outline + 4px offset (CS-NAV-02 / E1).
- Reduced-motion honoured on every animated path.
- Section wrapper rhythm `padding: 100px 72px; max-width: 1400px` (CS-RHYTHM-01 BLOCKING).
- Editor click-to-edit affordances guarded by `body.mw-is-editor-preview` (CS-MARKET-01).
- Whistleblowing legal-row entry where D.lgs. 24/2023 applies.
- ≤720px responsive collapse (hero stacks · nav becomes hamburger drawer · footer collapses).

### Must vary by layout family (CS-LAYOUT-* — different per family)

- L1 hero geometry · L2 section sequence · L3 mid-strip slot · L4 pillars treatment · L5 KPI placement · L6 leadership presence · L7 cases-preview shape · L8 navbar geometry · L9 footer structure.

A layout family is the operational mechanism that says: **the brand contract is shared, the body shape is not.**

---

## 8 · How browser review verifies layout distinctness, not just styling distinctness

The current browser-rubric (`factory/standards/corporate-suite-browser-rubric.md`) walks every sibling against a **9-dimension scorecard** that is mostly content/imagery/contrast/locale. Layout overlap can score 5/5 today because no rubric line specifically asks "does the wireframe outline differ?". The rubric needs three new gates.

### B-LAYOUT-1 · Wireframe overlay compare (BLOCKING)
On every new sibling walk, capture a **layout-only outline** of `home.html` at 1920px viewport: each `<section>` rendered as a coloured rectangle with section-name + bounding box, no copy/photos/colour. Overlay against the wireframe of every existing sibling.
- **Pass**: ≥30% of bounding-box surface area differs vs the closest sibling.
- **Fail**: ≥90% identical bounding boxes (current Continua-vs-Fiscus state).

### B-LAYOUT-2 · DOM-section list compare (BLOCKING)
Enumerate `document.querySelectorAll('section[class*="cs-"]')` on the home of every sibling. Two siblings cannot ship the same list of section class names in the same order.
- **Pass**: section list differs by ≥2 entries (insertions + deletions + re-orderings) vs every existing sibling.
- **Fail**: identical list (current Pragma/Fiscus/Solaria/Continua all share `cs-hero · cs-pillars · cs-kpi-band · cs-cycle? · cs-sectors · cs-trust · cs-leadership · cs-cases-preview · cs-cta`).

### B-LAYOUT-3 · Layout-dimension classification (REQUIRED)
At walk start, the verifier classifies the new sibling's home along all nine L1–L9 axes (using the value sets in `corporate-suite-layout-family-matrix.md`). A row is filed in the family matrix.
- **Pass**: classification matches the planner-declared layout family AND no two siblings share the full L1–L9 tuple AND the sibling differs from every existing sibling on ≥4 of 9 layout dimensions.
- **Fail**: classification drift from the declared family OR exact L1–L9 collision OR <4 layout dimensions differ.

### Side-by-side capture changes
The walk's `_compare-{sibling}-1920.png` artifact (already produced for Continua per `factory/reports/scorecard/continua-pass1-it/browser-verifier.md`) is split into two:
- `_compare-{sibling}-1920-skin.png` (current full render with palette, imagery, copy, colour) — the existing capture.
- `_compare-{sibling}-1920-wireframe.png` (new — layout-only outline as per B-LAYOUT-1).

Both must be filed in the evidence directory. The reviewer reads the wireframe pair first, then the skin pair.

---

## 9 · Why Continua multilingual must wait until this is settled

Continua passed Pass 1 (IT) and Pass 1.5 (review-lock) at draft tier. The `MEMORY.md` index points at the `phase_x4_continua_pass1_5_review_lock` checkpoint (`2026-04-29 GREEN`). The natural next pass is **multilingual rollout** — port IT to EN/FR/ES/AR + AR RTL — following the Solaria Pass B precedent.

It must wait for three reasons:

1. **Continua's current layout shape is going to change.** Continua holds LF-3 today (Fiscus's calendar shape with a governance-cycle cell substituted in). Once LF-5 (Stewardship Object-Hero) is built, Continua's hero geometry, pillars treatment, mid-strip slot, leadership framing, cases shape, and footer structure all change. Those are the surfaces where copy length, line breaks, italic-em positioning, and RTL mirroring decisions are made. Translating now means re-translating later.
2. **The italic-em emphasis is layout-sensitive.** `<em>` placement on the voice-anchor word is locked at IT-build time and the FR/ES/AR translator brief instructs which word carries the italic post-translation (CS-EXEC-01 / R7). If the LF-5 hero promotes the voice anchor to an overlaid h1 lower-third, the em-anchor word interacts with the photo's bright/dark zone — the translator brief becomes obsolete and must be re-issued per locale.
3. **Walk-budget arithmetic.** Each multilingual pass is 5 locales × ~7 cells = ~35 walk cells (per the Solaria Pass B precedent — 11 captures + 4 RTL passes + voice-anchor verification). Spending 35 walks on LF-3 Continua and another 35 on LF-5 Continua doubles the cost of one rollout. Building LF-5 first and walking once at LF-5 in IT, then porting once to 4 locales, costs ~42 walks total instead of ~70.

Multilingual is therefore deferred to a workflow C pass that runs **after** the Continua LF-5 rebuild closes IT-green at the new layout family. That is the only sequencing that does not waste prior translation work.

---

## 10 · Recommended next implementation order

Numbered, gated, and small enough that any step that fails halts the next. Each step has an explicit gate.

### Step 1 — Codify the layout-variance contract (this hardening pass)
- Land the three documents in `factory/reports/hardening/corporate-suite-layout-{divergence-plan, variance-rules, family-matrix}.md`.
- No source code change.
- **Gate**: user-review of the three documents. If approved, the rule IDs become referencable from the design-standard, brief schema, walk rubric.

### Step 2 — Backfill the layout-family classification for the four current siblings
- Update `corporate-suite-distinctness-matrix.md` to add a 13th dimension (Layout family) with the LF-1/LF-3/LF-4/LF-3 mapping for Pragma/Fiscus/Solaria/Continua.
- Update each existing sibling's docstring header (`page_data._meta` / module top comment) to declare its layout family.
- No DOM change — this is annotation only.
- **Gate**: 375/375 tests still green. Distinctness matrix shows 4 siblings × LF mapping.

### Step 3 — Rebuild Continua at LF-5 (Stewardship Object-Hero) in IT-only
- Source-code work: shared `home.html` gains layout-family branching, OR a per-template `home.html` override path is introduced for siblings that ship a non-LF-1 family. Likely shape: `templates/live_templates/business/corporate-suite/_layouts/{lf1,lf2,lf3,lf4,lf5}/home.html` with `_base.html` selecting via `template.layout_family`.
- Continua's `template_content_continua.py` adds the LF-5-specific page_data shape (object-hero credit pair, slot-2 cycle, 4-pillar matrix, timeline cases, 4-col footer).
- Imagery pack stays (already object-led from Pass 1).
- **Gate**: IT walk PASS at the new layout family. Wireframe overlay vs Pragma/Fiscus/Solaria shows ≥30% bounding-box variance on each pair. B-LAYOUT-1, B-LAYOUT-2, B-LAYOUT-3 all pass. Aggregate ≥4.50.

### Step 4 — Re-walk Continua IT at LF-5 with the new browser gates
- Apply B-LAYOUT-1, B-LAYOUT-2, B-LAYOUT-3 retroactively to Pragma, Fiscus, Solaria as well — confirm they pass when classified into LF-1/LF-3/LF-4.
- File `factory/reports/scorecard/continua-pass2-lf5/` with the new wireframe captures.
- **Gate**: All four siblings pass the layout-family classification check.

### Step 5 — Port Continua LF-5 to EN/FR/ES/AR + AR RTL (workflow C)
- This is the multilingual rollout that was deferred. Now safe to run, because the layout shape is settled.
- **Gate**: 5 locales × 7 cells walk-PASS · voice anchor verbatim · RTL mirror clean · public-flip user handshake.

### Step 6 — Build LF-2 (Editorial Spread) on the next corporate-suite enrollee
- Pick the 5th corporate-suite candidate that fits LF-2 — likely an architecture firm, an evidence-led legal practice, or an independent-director firm.
- Use this build to validate the variance system can land a fundamentally different layout (stacked hero, no dark KPI band, single-portrait leadership, magazine cases) without breaking cluster invariants.
- **Gate**: 5/5 distinctness vs Pragma/Fiscus/Solaria/Continua on the 13-dimension matrix. ≥4 of 9 layout dimensions differ vs every existing sibling.

### Step 7 — Audit Pragma/Fiscus/Solaria for in-family fit
- Run the layout-family classification against Pragma's home, Fiscus's home, Solaria's home. Confirm each fits its declared LF cleanly.
- If any drift surfaces (e.g., Solaria silently grew a leadership card), file a follow-up on that sibling.
- **Gate**: All four current siblings + the 5th LF-2 sibling fit their families with zero drift.

Steps 1–2 are this pass and the next. Steps 3–4 unblock multilingual Continua. Steps 5–7 are the multi-pass rollout that the rest of the workstream rests on.

---

## 11 · The clearest explanation of why current siblings still feel too similar

**The four siblings render the same DOM.** A single `templates/live_templates/business/corporate-suite/home.html` file (687 lines) drives every corporate-suite home, with a single optional `<section class="cs-cycle">` cell as the sole structural switch. Pragma, Fiscus, Solaria, and Continua differ only in the **content plugged into identical bounding boxes** — palette tokens, copy, imagery URLs, and the labels inside the meta-strip and cycle-strip. The 5-axis distinctness matrix scores 4–5 of 5 across every sibling-pair because it watches voice, palette, imagery, typography, and "structural rhythm" — but the structural-rhythm axis was scoped narrowly enough (section count, dark-band placement) that every sibling passes it by virtue of the shared shell. **Layout grammar was never promoted to a first-class differentiation axis.** When the user sees four siblings that "feel the same despite different palettes and copy," they are correctly reading that the wireframes overlay at >90% identical bounding boxes — which is exactly what shipping four palette/copy/imagery skins of one DOM produces. Differentiation has been optimised on the four axes the system can see, while the axis that produces the strongest "this is a different template" cue (DOM shape) is invariant.

---

## 12 · The five highest-priority structural changes

In descending order of how much wireframe-distinctness each one buys per unit of build cost.

1. **Promote layout family to a first-class differentiation axis** in `DISTINCTNESS_RULES.md` and the corporate-suite distinctness matrix. Add a 6th differentiation axis — "Layout family" — and require ≥4 of 9 layout dimensions to differ between any sibling pair. This is the meta-change that unlocks every other change below.
2. **Diversify hero geometry (L1)**. Stop treating the 55/45 split as a cluster invariant. Demote CS-HERO-01 from BLOCKING to "REQUIRED at family level — each layout family declares a hero geometry; the cluster does not pre-assign one." LF-1 keeps 55/45 split; LF-2 introduces stacked-editorial; LF-5 introduces object-overlay; LF-6 reserves side-rail. This single change alters the first-30-second read of a new sibling more than any other.
3. **Make the section sequence (L2) family-scoped, not archetype-scoped**. Demote CS-RHYTHM-02 from REQUIRED to "REQUIRED at family level." Each family declares its sequence in the family matrix; the home-shell becomes a router that picks the layout family's section list. This is the structural change that gives Solaria's manifesto-first composition a home and unlocks LF-2's editorial-spread rebuild.
4. **Promote the cases-preview shape (L7) to a 5-state property**. Today every sibling renders `list-row`. Add `magazine-grid` (LF-2), `timeline` (LF-5), `collage-3+1` (LF-6), `single-feature + sub-list` (reserved). Cases preview is one of the most-scrolled sections; varying its shape is a high-yield wireframe-difference move.
5. **Treat leadership presence (L6) as a 4-state property, not an always-rendered grid**. Today `cs-leadership` renders unconditionally; Solaria ships an empty card grid because its registry leadership list is empty. Make L6 a family choice: `{absent, typographic-grid, photo-grid, single-portrait-feature, pillar-photo}`. LF-4 omits it; LF-2 ships the single-portrait masthead; LF-5 ships pillar-photo. This change directly addresses the empty-leadership-block visual debt and creates a real distinctness lever.

A 6th candidate worth keeping on the list as the next priority after the top five lands: **navbar geometry diversification (L8)**, currently fixed to sticky-top by CS-NAV-01 BLOCKING. Demoting it to "REQUIRED at family level" unlocks LF-6's side-rail nav and is the single biggest above-the-fold differentiator available — but it carries a higher build cost (full responsive matrix re-walk per family) so it sits behind the layout-family scaffolding work in steps 1–5.

---

## 13 · Recommended next build order (one-line summary)

> **(1)** Land these 3 docs · **(2)** Backfill LF-1/LF-3/LF-4 mapping for Pragma/Fiscus/Solaria + LF-3-current/LF-5-target for Continua · **(3)** Rebuild Continua at LF-5 in IT-only · **(4)** Re-walk all four siblings under the new B-LAYOUT-1/2/3 gates · **(5)** Then port Continua LF-5 to EN/FR/ES/AR + AR RTL · **(6)** Build the 5th sibling at LF-2 to validate the system · **(7)** Audit Pragma/Fiscus/Solaria for in-family drift.

Multilingual Continua does NOT begin before Step 5. The rebuild precedes the rollout.
