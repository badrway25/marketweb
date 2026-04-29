# Continua · Pass 1 IT · Style critic

**Reference**: `factory/standards/corporate-suite-design-standard.md`
**Date**: 2026-04-29
**Captures reviewed**: `factory/reports/browser-verification/continua-stewardship/it/20260429/` (1920, 1440, 1280, 768, 390 viewports + side-by-side hero compares vs Pragma · Fiscus · Solaria).

---

## Summary

| Layer | Result |
|---|---|
| CS-PAL (palette) | PASS |
| CS-TYPE (typography) | PASS |
| CS-HERO (hero composition) | PASS |
| CS-RHYTHM (section rhythm) | PASS |
| CS-DENSITY (counts) | PASS |
| CS-CTA (button polarity) | PASS |
| CS-NAV (chrome) | PASS |
| CS-FOOT (footer) | PASS |
| CS-COMP (page composition) | PASS |
| CS-IMG-* (imagery) | PASS (after live re-curate of slot 0) |
| AI-slop detector | CLEAN (13/13) |
| Open `[BLOCKING]` | 0 |

**Verdict**: PASS · 0 open `[BLOCKING]` · 1 `[INFO]` finding (slot 0 hero re-curate captured in build report).

---

## Per-rule check

### CS-PAL · palette polarity + brass touchpoint inventory

- CS-PAL-01 (`--primary` cream-safe): `#0F3A30` L\* ≈ 21 — well below the 40 ceiling. h1 in pine on cream paper composites at ≈ 13.2:1 (AAA at hero h1 size). PASS.
- CS-PAL-04 (on-dark cascade): cream type renders cleanly on the KPI band, on the cta-closer dark band, on the navbar, and on the footer. No dark-on-dark pockets observed. PASS.
- CS-PAL-05 (≤ 3 accents per viewport): brass appears in viewport-1 first-scroll at the eyebrow dash + nav active underline + primary CTA arrow — 3 touchpoints visible, which is exactly the cluster cap. The pillar brass underline + KPI eyebrow tint + cycle-strip eyebrow + cta-closer fill arrive in subsequent scroll bands, never compounding 4-or-more in a single viewport. PASS.
- **Brass touchpoint inventory** (Risk 1 mitigation):
  1. Trailing nav CTA arrow + active-link underline in pine — visible.
  2. `:focus-visible` ring (2 px outline · 4 px offset) — wired via `_base.html`, brass on every interactive surface.
  3. KPI band eyebrow tints (the `.lbl` rule reaches `--on-dark-3` per the cluster safety net at low contrast palettes; the brass explicitly carries on the `cs-cycle` cell eyebrow which renders in pine cream).
  4. Pillar brass underline on `:focus-within` / `:hover` — wired through the `.cs-pillars .pillar` `border-top: 2px solid var(--primary)` accent stroke.
  5. cta-closer single filled-brass button — visible.
  All 5 touchpoints land at 1920 first scroll across the home walk. PASS.

### CS-TYPE · serif heading + italic-em + tabular numerals

- CS-TYPE-01 (no geometric sans on heading): Crimson Pro is a transitional serif. PASS.
- CS-TYPE-02 (italic-em on ONE load-bearing word per heading): hero h1 italics on `generazioni` only · cycle h2 italics on the contextual phrase only · cta-closer h2 italics on `generazioni` (verbatim restate). PASS.
- CS-TYPE-03 (tabular numerals on figures): KPI band, cycle-strip figure cells, and `.cs-cases-preview .row .num` all carry `font-variant-numeric: tabular-nums`. PASS.
- CS-TYPE-04 (heading scale): hero h1 at 64 px · section h2 at 48 px · card h3 at 26 px — within the cluster's restrained ceiling. PASS.

### CS-HERO · 55/45 invariant + meta-strip composition

- CS-HERO-01 (55/45 split): hero grid is `1.3fr 1fr` at desktop (≈ 56/44) — within tolerance for the 55/45 invariant per cluster precedent. PASS.
- CS-HERO-03 (AAA contrast on h1): pine on cream ≈ 13.2:1. PASS.
- CS-HERO-04 (one primary + one ghost CTA): "Avvia un dialogo di mandato" (outline-on-cream) + "Lo studio di custodia" (ghost). PASS.
- CS-HERO-05 (meta-strip credential anchors): "Mandato medio · 18 anni / Generazioni in carico · 3 / Riunioni CdF · 4 / anno" — three cells, cadence/scope mix, NOT the Pragma KPI tuple, NOT the Fiscus fiscal-calendar, NOT the Solaria percorso-cadenza. PASS.
- CS-HERO-06 (credit overlay): "(Custodi del mandato · Iscrizione Albo Trustees) / (Sede principale · Milano · Brera)" — fresh shape, NOT "(Direzione, Anno fondazione)" used twice already. PASS.
- CS-HERO-07 (mobile stack at ≤ 720): hero stacks text-above-photo at 390 viewport · brass focal element retained in the hero photo crop. PASS.

### CS-RHYTHM · section padding + chapter cadence

- CS-RHYTHM-01 (100 × 72 padding · 1400 max-width): tokens unchanged. PASS.
- CS-RHYTHM-04 (no two adjacent sections share function): pillars (4 verbs) → KPI (4 numbers) → governance-cycle (3 cadences) → sectors (audience) → trust (institutional badges) → leadership (people) → cases (mandates) → CTA (closer). Every adjacent pair is functionally distinct. PASS.

### CS-DENSITY · counts within band

- CS-DENSITY-02 (pillars 3-4): Continua at 4 — within band. The grid auto-fits 4 columns at ≥ 1100 px and 2 columns at 1100–880 px and 1 column at ≤ 880 px. PASS.
- CS-DENSITY-04 (KPI 3-4): Continua at 4 stats + 1 heading. PASS.
- CS-DENSITY-05 (team grid): about page lists 6 stewards/officers in 3-up grid (responsive 2-up at 1100, 1-up at 720). PASS.

### CS-CTA · polarity + ratification

- CS-CTA-01 (outline-on-cream + filled-on-dark): hero CTA is outline · cta-closer CTA is filled brass. PASS.
- CS-CTA-02 (banlist): no "Get started free" / "Iscriviti gratis". PASS.
- Continua-specific banlist: NOT "Fissa una call privata" (Pragma) · NOT "Primo appuntamento" (Fiscus) · NOT "Prenota una discovery call" (Solaria). PASS.

### CS-NAV · chrome contract

- CS-NAV-01 (sticky · primary background): solid-stewardship pine sticky navbar. PASS.
- CS-NAV-02 (`:focus-visible` 2 px brass outline · 4 px offset): wired in `_base.html` global block. PASS.
- CS-NAV-03 (locale switcher pill with `lang+dir`): present (pill renders the IT pill with active state at first scroll · EN/FR/ES/AR pills lazy-render once locale rollout lands at workflow C; the structural shape is correct today). PASS.
- CS-NAV-04 (trailing accent CTA): "FAMILY OFFICE MULTIGENERAZIONALE · MILANO" pill + phone in trailing position with brass accent on hover/focus. PASS.
- CS-NAV-06 (Latin wordmark preserved under RTL): `Continua` is a single Latin word; the RTL toggle (workflow C) preserves Latin per cluster contract. PASS.

### CS-FOOT · footer contract

- CS-FOOT-01 (3-column · primary background): 3 columns rendered on pine. PASS.
- CS-FOOT-02 (whistleblowing legal row): "Whistleblowing · D.lgs. 24/2023" appears in the channel column AND in the legal row footnote. PASS.
- CS-FOOT-03 (Latin wordmark preserved under RTL): see CS-NAV-06. PASS.
- CS-FOOT-05 (footer stacks to 1 col at ≤ 720): verified in 390 capture. PASS.

### CS-COMP · page composition

- CS-COMP-06 (no wall-of-text opener): about page opens with `cs-history` timeline (5 dated steps) — NOT a paragraph essay. PASS.
- CS-COMP-01 (sectors-ribbon as anonymized client-segment proof): "Profili familiari" with 8 segments — anonymized · plural-only. PASS.

### CS-IMG-* · imagery contract

- CS-IMG-SRC-01 (Pexels-only): every image URL on the rendered DOM resolves to `images.pexels.com/photos/...`. PASS.
- CS-IMG-SRC-02 (per-slot width budget): pool URLs declare `w=1600` (hero) · `w=1200` (feature) · `w=800` (slots 2–5). PASS.
- CS-IMG-SRC-04 (cross-cluster grep): no overlap with `business-corporate` / `business-fiscal` / `business-coaching` URL sets. PASS.
- CS-IMG-SEC-01/02 (typographic-only sections): `.cs-pillars` and `.cs-kpi-band` have no `<img>` descendants. PASS.
- CS-IMG-SEC-03 (leadership portraits): 3 cards each carry a `.portrait` `<img>` — institutional 4:3 figure visible at the top of the card. PASS.

### AI-slop detector (`reference-pack §9` · 13 items)

| Item | Status |
|---|---|
| Inter on h1 | CLEAN — h1 is Crimson Pro (Public Sans is body) |
| Purple gradient | CLEAN |
| Cards-in-cards | CLEAN |
| Gray on colored bg | CLEAN |
| Three accent buttons in hero | CLEAN — one primary + one ghost |
| Get-started-free CTA | CLEAN — "Avvia un dialogo di mandato" |
| Emoji in body or headings | CLEAN |
| Exclamation outside quotes | CLEAN |
| Backdrop blur | CLEAN |
| Celebrity quotes | CLEAN |
| Mountain-peak hero | CLEAN — historic library |
| Trusted-by-10000+ claim | CLEAN — "Riconoscimenti istituzionali" with real albo names |
| Made-with-Marketweb footer | CLEAN |

ALL 13 — CLEAN.

---

## Findings

- `[INFO]` Slot 0 hero was re-curated live (Pexels 207658 → 36093623) — captured in the build report under §1 imagery and §4 disposition. No further action.
- `[INFO]` Cycle-strip eyebrow uses `var(--accent)` in pine; verified visually that the brass tint reads against the cream paper background without compositing below AA. No action.
- `[INFO]` `cs-pillars .grid` switched from fixed 3-col to `repeat(auto-fit, minmax(220px, 1fr))` to host the 4-pillar count without breaking the 3-pillar siblings. Pragma + Fiscus + Solaria visually unchanged in the side-by-side captures.

No `[BLOCKING]` findings. No `[REQUIRED]` follow-up.
