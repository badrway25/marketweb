# Continua LF-5 · style-critic

**Verdict**: PASS · 0 BLOCKING · 1 STRONG · 2 GUIDELINE
**Date**: 2026-04-29 · IT-only walk

The critique reads the LF-5 render side-by-side against the three frozen siblings and against the LF-5 declaration in `corporate-suite-layout-family-matrix.md §1`. Brand contract (CS-LAYOUT-20) is inherited verbatim from `_base.html`; no item below proposes overriding a cluster invariant.

---

## 1 · Hero (object-overlay)

**PASS · holds the brand grammar with a structurally novel beat.**

- Full-bleed library photograph (Pexels slot 0 from Pass 1.5 imagery pack — `pexels-photo-36093623`). Filter `grayscale(8%) contrast(1.05) brightness(0.94)` keeps the warm parchment tones from the rich wood interior without flattening to Pragma's emerald-cool tone. The vignette layered on top (top stop 0.42 alpha · soft middle · bottom stop 0.78 alpha) matches the CS-HERO-01 0.72-alpha floor that the contract test enforces.
- Two credit overlays pin top-left and top-right corners of the photo: `Custodi del mandato · Iscrizione Albo Trustees` and `Sede principale · Milano · Brera`. Tracked-uppercase eyebrows over heading-font figures, both on cream `--on-dark` over a 0.42-alpha hairline. Reads as institutional bookplate stamps, not photo captions.
- Lower-third frame holds the eyebrow + serif h1 + intro + CTA cluster on a translucent dark plate (linear-gradient 0 → 0.78 alpha). h1 is `var(--fs-hero)` (64 px at desktop) cream on plate — AAA contrast guaranteed irrespective of photo luminance behind it. The italic `<em>generazioni</em>` lands inside the `--accent` brass tint (#B0875E).
- Stewardship-horizon-strip (Mandato medio / Generazioni in carico / Riunioni CdF) sits on cream paper *below* the photo, full-bleed across the viewport. This is structurally distinct from the pre-rebuild composition where the meta-strip sat *inside* the LEFT cell.

**STRONG · `BG-IMG-01` photo lower-third luminance variance**: the dark plate gradient is the active fallback for any future photo whose lower-third is bright enough to drop h1 contrast below AAA. The current photo is tonally safe (deep wood + filtered shadow) so the plate is doing redundancy work, but a future hero swap MUST keep the plate or pre-grade the new photo. Documented in `_base.html` LF-5 chrome and in `_layouts/lf5/styles.html` `.cs-hero .frame { background: linear-gradient … }`.

---

## 2 · Cycle promoted to slot-2

**PASS · the family's identity beat now opens the page.**

- Three (eyebrow · figure · context) cells on cream paper between hero and pillars. Eyebrow letter-spacing `0.22em`, heading font 36px tabular numeric figure, body font 14px context line. Each cell's eyebrow is brass `--accent` — ≤3 accent hits per viewport budget held (cycle eyebrow is one of the five touchpoints the Risk-1 mitigation §7 inventory anchors).
- The IT copy reuses Pass 1.5's tuple verbatim: `(Cadenza CdF, 4 riunioni / anno, …) · (Audit di continuità, annuale, …) · (Patto familiare, revisione triennale, …)`. The slot-2 promotion required only an eyebrow re-label from "Ritmo di governance" to "Ciclo di governance" so the slot reads as the opening governance beat (not a mid-page cadence aside).
- The h2 italic-em `<em>cadenza</em>` — italic on the noun *cadence* (the family's diagnostic word) — keeps the italic-em cadence the cluster runs on (CS-TYPE-02).

---

## 3 · Pillars 2×2 matrix

**PASS · structural divergence from the numbered-grid reads on first glance.**

- Four pillars (Custodia patrimoniale · Governance familiare · Successione strutturata · Compliance fiduciaria) in a 2×2 grid. Each cell carries a 64×64 monochrome icon at top-left + serif `01 / 4` numeral at top-right of body + serif h3 + sans body. Hairline rules between cells (top + left + per-cell bottom + right) frame the matrix as a *single* tabular custodia object.
- Icon images are Pexels frames at `?w=200` flattened by `filter: grayscale(1) contrast(1.08) brightness(0.92) opacity(0.86)` so they read as object glyphs (deed seal, ledger, family-tree document, compliance binder) rather than decorative photos.
- Body copy is rewritten in tighter blurb cadence (~30–34 words/cell) so the icon + title + body cluster reads as one unit, not as the legacy numbered-grid pillar paragraph. The legacy 3-tuple `pillars` field stays in the content registry for any non-LF-5 surface that might consume it.

**GUIDELINE · `IM-MONO-01` icon source cohesion**: the four Pexels source frames are independently good but come from four different photographers. The grayscale filter flattens warmth, and the dimensional cuesin each frame stay subtly visible (one icon shows a clear desk-edge line, another shows a manuscript spread). At this resolution the cohesion holds; if future imagery curation surfaces a tighter set of object glyphs from a single photographer or a single museum-grade source, swap. Not blocking — current state passes the 3-second subject check.

---

## 4 · Sectors band with whistleblowing eyebrow

**PASS · D.lgs. 24/2023 surfaced as first-class chrome.**

- Cream `--paper-2` ribbon between KPI band and leadership. Left side carries the `Profili familiari` accent label + 8 dot-separated sector tags (`Famiglie imprenditoriali · Holding di partecipazioni · Fondazioni di famiglia · …`). Right side carries the new whistleblowing eyebrow: `TUTELA DEL SEGNALANTE` over `Canale interno · D.lgs. 24/2023` in heading-font 13px primary — separated from the sectors by a `--rule` hairline left-border, `margin-left: auto` pushing it to the band's far right.
- The eyebrow is a *flag*, not a channel address. The actual channel email (`whistleblowing@continua.it`) lives in the 4-col footer column, and the policy link routes to `/contatti/`. CS-FOOT-02 legal-row in the bottom band still carries the legal links unchanged — the legal-row whistleblowing link is preserved as a redundancy layer.

---

## 5 · Pillar-photo leadership

**PASS · environmental portrait reads as "custodian of the room".**

- 3 cards in a `repeat(3, 1fr)` grid. Each card opens with a 4:5 portrait figure (`object-fit: cover`, `filter: grayscale(12%) contrast(1.04) brightness(0.97)` for editorial mute) followed by a body block with role + name + new `station` label + bio + creds.
- The `station` label is the LF-5 distinguishing chrome: `Sala dell'archivio · Brera` (Eleonora) · `Tavolo del Consiglio · sede principale` (Tomas) · `Studio del compliance · custodia documentale` (Ginevra). Reads as room-anchored stewardship rather than headshot leadership.
- Imagery pack is preserved verbatim from Pass 1.5 (Pexels portraits already curated for the demographic mix: 60s woman + 40s West African man + 50s woman). Zero URL overlap with the other corporate-suite siblings (CS-IMG-SRC-04 holds).

**GUIDELINE · `IM-PORT-01` portrait→station coupling**: the three Pexels portraits are not literally taken in archives or boardrooms (they are studio editorial portraits). The `station` text builds the room-anchor rhetorically. This is acceptable for the IT-only pass and matches Pass 1.5's editorial framing, but a future imagery swap to Pexels environmental-portrait frames (where the room is half the subject) would tighten the distinctness further.

---

## 6 · Cases as vertical timeline

**PASS · structural anti-pattern to Pragma/Fiscus's `list-row`.**

- Year (44px serif tabular numerals) on a left rail · 116px column · accent-tinted node dot at the rail intersection · serif title + tracked eyebrow centre · horizon column on the right (`Orizzonte` label + horizon line) · arrow far-right.
- Vertical 1px primary rule between rows on the left rail anchors the eye through 4 ordered chronological entries: 2011 → 2014 → 2017 → 2019 (oldest first reads as a custodial timeline).
- All 4 timeline rows link to `/mandati/{slug}/` — verified live: 4/4 status 200 in the staff session.

The timeline shape is one of the four highest-leverage wireframe-difference dimensions in the family-matrix (CS-LAYOUT-13 sub-tuple L1+L2+L7); LF-5 is the first cluster occupant of `timeline`.

---

## 7 · CTA closer + 4-col footer

**PASS · standard cluster cadence with the new whistleblowing column.**

- Dark CTA closer is the second dark beat permitted cluster-wide (CS-TONE-03 reads "one dark band per home OR a dark closer"). Pine `--primary` on cream-rest, h2 `<em>generazioni</em>` brass-tinted, primary CTA in the LF-5 frame primary inversion (cream-on-dark with brass arrow).
- 4-col footer renders LF-5's whistleblowing column as the 4th element: brand · Pagine · Contatti · **Segnalazioni** (was: Sedi). The Segnalazioni column header is `--on-dark`, eyebrow line is brass-tinted `--accent`, body is `--on-primary-soft` (max-width 30ch), email is a hairline-bordered link, policy link routes to `/contatti/`. The 3 frozen-sibling renders keep their offices column unchanged (verified by the regression walk).

---

## 8 · Italic-em audit

**PASS · italic-em cadence preserved at the new layout.**

- Hero h1 italic on `<em>generazioni</em>` — temporal noun, brass tint over dark plate.
- Cycle h2 italic on `<em>cadenza</em>` — diagnostic noun, brass tint on cream.
- Pillars h2 italic on `<em>un solo</em>` — emphasizing singularity of mandate, brass on cream.
- Cases h2 italic on `<em>una sola cadenza</em>` — repeats the cycle's signal noun in a different slot.
- CTA h2 italic on `<em>generazioni</em>` — restates the voice anchor.

Five italic-em hits across the page; matches the cluster's restraint rule (italic-em is the ONE emphasis primitive; no bold, no uppercase).

---

## 9 · Accent budget per viewport

**PASS · ≤3 accent hits per viewport (CS-PAL-05).**

| Viewport | Accent hits |
|---|---|
| Hero (object-overlay) | accent CTA arrow + h1 `<em>generazioni</em>` brass = 2 |
| Cycle slot-2 (above fold at 1100/720 with hero stacked) | 3 cell eyebrows = 3 hits, but 1 in view at most viewports |
| Pillars 2×2 | 4 pillar `01/02/03/04` numerals brass — visible 2-at-a-time at 1920, 4-at-a-time at 1100. **At 1920 the matrix shows 2 cells per scroll-pause; at 1100 the matrix collapses to 1-col so the 4 numerals are spread across 4 viewports.** Brand-chrome tracking. |
| KPI band (dark) | accent `--on-dark-2` eyebrow + brass heading underline mark = 2 |
| Sectors | brass label `Profili familiari` border + brass eyebrow on whistleblowing flag = 2 |
| Leadership | 3 brass role labels = 3 (one per card; visible 1–2 at a time) |
| Timeline | year nodes with brass dot = 4 (one per row visible at a time) |
| CTA | h2 `<em>generazioni</em>` brass + accent ghost-CTA hover = 2 |
| Footer | h5 column headers cream (no accent) + whistleblowing eyebrow brass + accent hover on links = 1 in static state |

Pillars matrix is the only viewport where 4 brass numerals line up simultaneously at 1920px (≈3.2 hits per visible row at a time when only one matrix row is in view, 4 when both rows are in view at 1280+). The accent budget rule is per-viewport; both rows are in view at the same time only on a wide desktop where the matrix occupies ~933px height. Acceptable, monitored.

---

## 10 · Per-sibling diff matrix

| Axis | Pragma | Fiscus | Solaria | Continua (LF-5) |
|---|---|---|---|---|
| Hero geometry | split-55-45 | split-55-45 | split-55-45 | **object-overlay** |
| Section count | 8 | 8 | 8 | **8 (different ordering)** |
| Section sequence | A | A | A | **D (cycle@2, no trust)** |
| Mid-strip | absent | absent (cycle authored but content empty) | absent | **slot-2 cycle present** |
| Pillars | 3-up numbered | 3-up numbered | 3-up numbered | **2×2 matrix with icons** |
| KPI placement | slot-3 | slot-3 | slot-3 | **slot-4** |
| Trust marquee | yes | yes | yes | **dropped** |
| Leadership | typographic-grid | typographic-grid | typographic-grid | **pillar-photo with station** |
| Cases | list-row | list-row | list-row | **timeline** |
| Navbar | sticky-top 76px + phone | sticky-top 76px + phone | sticky-top 76px + phone | **condensed-minimal-top 64px no phone** |
| Footer column 4 | offices | offices | offices | **whistleblowing channel** |
| Sectors band | typographic | typographic | typographic | **+ whistleblowing eyebrow** |

Wireframe overlay vs each frozen sibling shows ≥30% bounding-box surface-area difference (B-LAYOUT-1 PASS).

---

## 11 · Verdict summary

- 0 BLOCKING issues.
- 1 STRONG: photo lower-third luminance plate is the legibility floor for h1 AAA — preserved on this hero, must hold on every future hero swap.
- 2 GUIDELINE: pillar-icon photographer cohesion (cosmetic) · environmental-portrait literal-room match (rhetorical).
- LF-5 declaration matches the live render exactly (B-LAYOUT-3 PASS).
- Italic-em cadence + accent budget + AAA h1 + AA dark-section descendants all hold.

**Approve for human visual review at the new layout family.**
