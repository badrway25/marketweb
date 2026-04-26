# style-critic · Solaria controlled re-entry pass 1

**Subject**: `solaria-coaching` (corporate-suite, third enrollee · IT-only at pass 1)
**Run-ISO**: `20260426T0907Z`
**Reporter**: Claude (Opus 4.7) acting as `style-critic`.
**Standards consulted**: `corporate-suite-design-standard.md`, `corporate-suite-quality-scorecard.md`, `corporate-suite-blocking-rules.md`.

---

## D1 · Editorial typography (CS-TYPE-\*)

- **Font pairing**: Fraunces + Inter (humanist serif + neutral sans). Distinct from Pragma's Merriweather + Inter and Fiscus's IBM Plex Serif + IBM Plex Sans. **Three-template typographic differentiation honored.**
- **Hero h1 size at 1440 × 900**: 64 px (= `--fs-hero` archetype variable). Within CS-TYPE-04 ceiling (72 px max).
- **Hero h1 size at 390 × 844**: 32 px (verified live). CS-RESPONSIVE-03 floor (≥ 32 px @ 390) met exactly.
- **Letter-spacing on hero h1**: -0.022em — consistent with archetype contract (no display-headline overhang).

**Score: 5 / 5.** No deviations.

## D2 · Restraint over density (CS-DENS-\*)

- Hero left column has eyebrow + h1 + sub + 2 CTAs + meta-strip — the canonical archetype 5-anchor layout.
- Pillars: 3 numbered cards × 1 short blurb each — three-line scan-floor honored.
- KPI band: 4 stats (12 / 2.400+ / 160+ / 100%) — within the 4-stat ceiling.
- Sectors ribbon: 5 sector labels + marquee — typographic, no logo cliché.
- Trust band: 6 anonymized client-category labels (per ICF §2.4 confidentiality, NOT logo-as-image) — content choice doubles as ethical-anchor.

Solaria's content is, if anything, **less dense** than Pragma + Fiscus on home — appropriate for a coaching solo-practitioner's tone vs. Pragma's 14-partner board advisory voice. The "airy" density (declared in DNA) renders correctly in the live walk.

**Score: 5 / 5.**

## D3 · Color discipline / palette polarity (CS-PAL-\*)

- **Primary `#2B2A28`** = warm dark carbon · luminance 0.024 · contrast vs cream 12.56 AAA.
- **Secondary `#C8621A`** = warm-earth ocra (the brand's main accent — chrome + buttons + decorative number on cream).
- **Accent `#8B5A2B`** = deep caramel (quieter secondary).
- **Body bg**: `--paper` = `#EEF0F3` (skin default; Solaria does not override).
- **Dark-surface text**: `--on-dark` = `#EEF0F3` cream (post CS-BLOCK-17 (extended) inherited contract).

The dark-warm palette renders as warm-cream-dark editorial — distinct from Pragma's navy-emerald cool advisory and Fiscus's gold-navy institutional. **D-054 palette differentiation gate cleared 10 / 10 vs both siblings.**

CS-PAL-01 build-time gate: **passes** (`#2B2A28` luminance 0.024 ≤ 0.12 ceiling AND ratio 12.56 ≥ 7.0 floor).

**Score: 5 / 5.**

## D5 · CTA discipline (CS-CTA-\*)

- **Primary CTA**: "Prenota una discovery call" (outline-only on cream paper · CS-DECISION-WAIVER recorded in design standard §10).
- **Ghost CTA**: "Il metodo".
- **CS-CTA-01 touch-target floor at 390**: primary CTA `min-height: 44px · padding: 14px 22px` (verified via `@media (max-width: 720px)` rule in home.html:441-446). **PASS at 390.**
- **CS-CTA-04 footer real-route wiring**: 8 / 8 anchors live-verified non-`#` (browser-verifier §3 row CS-CTA-04).
- **CS-CTA-03 ghost = typographic-link standing waiver**: inherited from archetype.

**Score: 5 / 5.** The Solaria primary "Prenota una discovery call" inherits the §10 paper-surface outline-only WAIVER decided in P1D — explicitly permitted, NOT a placeholder reading.

## D6 · Imagery direction (CS-IMG-DIR-\*)

DNA `imagery_direction = "coaching-conversation"` resolves to `business-coaching` Pexels pool. Six slot-canonical URLs:

| Slot | Direction | URL stem |
|---:|---|---|
| 0 (hero) | 1:1 conversation in bright office | `7979456` |
| 1 (feature) | man writing in notebook during indoor discussion | `5756579` |
| 2 (portrait-coach) | woman with clipboard, minimalist indoor | `9064347` |
| 3 (portrait-coachee) | confident businesswoman, arms crossed | `12934369` |
| 4 (detail-notebook) | open notebook with pen on wooden desk | `34601` |
| 5 (ambient-warm-office) | warm home-office with plants | `31236101` |

The hero slot 0 (`7979456`) was sampled live: **renders correctly in the right-hand panel of `.cs-hero` at 1440 × 900** (verified via `getComputedStyle(.cs-hero .right).backgroundImage` regex match against `images.pexels.com`).

**No mountain-peak / motivational-quote / drawn-arrow cliché** (blueprint §8 + §13 guardrails). Imagery is institutional-warm, coaching-domain-appropriate, NOT therapy / NOT consulting / NOT guru.

**Score: 5 / 5.**

## D7 · Information structure (CS-STRUCT-\*)

- 5 pages: home · il-coach · percorsi · casi · contatti — corporate-suite skin page-kinds (no new kinds introduced).
- Section order on home: hero → pillars → kpi-band → sectors → trust → leadership → cases-preview → cta. **Identical to Fiscus** (Solaria reuses the same section_order in DNA).
- About page: hero → history (5-step method timeline) → values (4 principi non negoziabili) → team (4 cards: founder + associate + supervisor + back-office) → coordinates → cta.
- Services page: hero → services (4 percorsi cards) → process (4 steps on dark band) → cta.
- Cases list: hero → 3 anonymized case rows.
- Contact: hero → discovery-call form (4 numbered sections) + Milano coordinates side panel.

**No structural improvisation** vs Pragma + Fiscus. Solaria's content rhythm matches the archetype contract.

**Score: 5 / 5.**

## D8 · Voice anchors and editorial copy (CS-VOICE-\*)

- **Voice anchor**: "Il coaching non è terapia e non è consulenza." Verbatim in home h1, present in il-coach intro, recurring in cases-preview intro, anchoring contatti hero. **5 / 5 anchor placements honored** (BRWS-FEEL-05).
- **Method-declared**: GROW + Co-Active + Immunity to Change frameworks named explicitly in il-coach + percorsi.
- **Bounded path**: every percorso card declares duration + frequency + format. No "trasformazione in trenta giorni" promise.
- **ICF Code of Ethics §2.4 referenced** in trust-band copy + casi-list intro + contatti GDPR consent. Confidentiality is content-anchored, not just legal-footer-deferred.
- **Anti-pattern guardrails**: 0 grep hits across the entire DOM (build-report §5).

**Score: 5 / 5.**

## Style-critic verdict

**Aggregate: 5 / 5 across D1, D2, D3, D5, D6, D7, D8** (the 7 dimensions style-critic owns; D4 / D9 / D10 / D11 / D12 / D13 / D14 belong to other agents per scorecard §3).

Zero blocking-rule trips: CS-BLOCK-08 (display-headline cap) clear, CS-BLOCK-09 (cream-on-cream) clear, CS-BLOCK-10 (logo-as-cliché) clear, CS-BLOCK-16 (font-family fallback) clear, CS-BLOCK-17 (extended) (dark-on-dark inversion on chrome) clear by archetype inheritance.

Solaria reads warm-earth-coaching where Pragma reads navy-corporate and Fiscus reads gold-institutional. The three-template typographic + palette + voice differentiation is the strongest evidence yet that the corporate-suite archetype generalizes correctly beyond the original Pragma blueprint.
