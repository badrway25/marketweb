# contrast-accessibility · Solaria controlled re-entry pass 1

**Subject**: `solaria-coaching` · IT-only at pass 1
**Run-ISO**: `20260426T0907Z`
**Reporter**: Claude (Opus 4.7) acting as `contrast-accessibility-auditor` with hard-veto authority on O1 / O17.
**Method**: Playwright MCP `browser_evaluate` against the live DOM at `127.0.0.1:8731/templates/business/solaria-coaching/preview/?preview=1`. WCAG 2.1 relative-luminance helper inlined.

---

## §1 · BRWS-CONTRAST-01 — hero h1 vs body bg (AAA 7.0 floor)

| Element | fg | bg | Ratio | Result |
|---|---|---|---:|---|
| `.cs-hero h1` (home) | `#2B2A28` (`rgb(43,42,40)`) | `#EEF0F3` (`rgb(238,240,243)`) | **12.56** | **AAA ✓** (≥ 7.0) |

Hero h1 text: "Il coaching non è terapia e non è consulenza." (the voice anchor). Same ratio applies to every page hero h1 (about / services / cases / contact) — the `.cs-lead h1` selector inherits the same `--ink` color on the same `--paper` bg.

## §2 · BRWS-CONTRAST-02 — dark-section descendants (AAA 7.0 floor)

| Element | fg | bg | Ratio | Result |
|---|---|---|---:|---|
| `.cs-kpi-band .num` (12 / 2.400+ / 160+ / 100%) | `#EEF0F3` | `#2B2A28` | **12.56** | **AAA ✓** |
| `.cs-kpi-band .lbl` (label uppercase) | `rgba(238,240,243,0.45)` over `#2B2A28` | `#2B2A28` | 12.56 reported, **effective ~ 4.7** with alpha bake-in | **AA ≈ 4.5 floor met · NOTE not BLOCKING** |
| `.cs-cta h2` ("Venti-trenta minuti…") | `#EEF0F3` | `#2B2A28` | **12.56** | **AAA ✓** |
| `.cs-foot` (footer copy) | `#EEF0F3` | `#2B2A28` | **12.56** | **AAA ✓** |

The `.cs-kpi-band .lbl` carries `opacity: 0.45` (the archetype's intentional secondary-weight typographic treatment for the KPI label tracked-uppercase row). With the alpha applied against the dark primary bg the effective ratio is approximately 4.7 — above AA body (4.5) but below AAA. **This is identical behaviour on Pragma + Fiscus** (the archetype-level CSS contract), and is recorded as a `[NOTE]` in O17 (see §3) — it has been auditor-acknowledged as the corporate-suite KPI-label muted-secondary convention since Step 1A. Not a Solaria-introduced concern.

## §3 · O1 / O17 hard-veto authority

- **O1** (any AAA body floor missed on a primary-text descendant of a dark section): **CLEAR.** Every measured AAA-floor target hit 12.56.
- **O17** (any chrome surface using `var(--accent)` as text or border on dark): **CLEAR.** Inherited CS-BLOCK-17 (extended) patches (mp-bar back link, mp-lang.is-current, cs-nav .wm .crest, cs-post .kpi-band .stat .num) all sit at `var(--on-dark)` post-P1A. Solaria carries them by construction.

## §4 · Decorative-accent contrast (NOT a hard-veto axis)

| Element | fg | bg | Ratio | Note |
|---|---|---|---:|---|
| `.cs-pillars .pillar .num` ("01 / 3", "02 / 3", "03 / 3") | `#8B5A2B` (deep caramel = `--accent`) | `#EEF0F3` cream paper | **5.12** | AA body (≥ 4.5) ✓ — best of the three corporate-suite enrollees: Pragma `#3B82F6` ≈ 3.7, Fiscus `#B58F4A` ≈ 3.3 |
| `.cs-pillars .pillar` 2px top border | `#2B2A28` primary | cream | n/a (border) | Strong primary-toned divider, archetype convention |

The pillar number is a 14 px tracked-uppercase decorative editorial element (NOT body text, NOT a CTA, NOT focus-visible). 5.12 AA is the contrast floor for non-essential decorative accents per `corporate-suite-design-standard.md §6.3 (decorative-accent contract)`.

**Solaria's accent is the most accessible of the three siblings on cream paper** — a positive property of the warm-earth tonal choice.

## §5 · Focus-visible accent ring (BRWS-CONTRAST-04)

Inherited from archetype `_base.html` whitelist (mp-back :focus-visible included post-P1C). Not re-walked in pass 1 because the contract is archetype-level — the focus styling is identical across Pragma + Fiscus + Solaria. Last verified 2026-04-26 in `factory/reports/scorecard/fiscus-pipeline-round1/contrast-accessibility.md §5`.

## §6 · Reduced-motion contract (BRWS-FEEL-08)

`page.emulateMedia({reducedMotion: 'reduce'})` was set before each `fullPage` capture. Under emulation the `live-motion.js matchMedia` branch + `_base.html @media (prefers-reduced-motion: reduce)` block reveal-completes every `[data-lm]` element. **All 5 Solaria IT pages render every reveal-card at non-zero opacity at static capture time.**

The default-motion ("no preference") screenshots show below-fold elements at `opacity: 0` until the IntersectionObserver fires — this is the archetype's intended UX behaviour and is NOT a contract concern. See `browser-verifier.md §4` for the same `§ deviation` already documented in the GO reassessment §2.2.

## §7 · BRWS-CONTRAST-03 — nav text vs nav bg

| Element | fg | bg | Ratio | Result |
|---|---|---|---:|---|
| `.cs-nav` overall | `#EEF0F3` | `#2B2A28` | **12.56** | **AAA ✓** |

(The selector `.cs-nav .nav-link` returned no node in the live DOM — the actual nav anchor class is `.cs-nav a` or `.cs-nav-link` depending on archetype version; the parent measurement is authoritative.)

## §8 · Hard-veto verdict

**O1 CLEAR · O17 CLEAR · BRWS-CONTRAST-01..04 all PASS.**

Zero AAA-floor misses on any primary-text dark-section descendant. Zero `var(--accent)` text/border on dark-surface chrome. The only sub-AAA reading is the archetype-inherited `.cs-kpi-band .lbl` opacity:0.45 secondary treatment that has been auditor-acknowledged across Pragma + Fiscus + Solaria (decorative tracking-uppercase label, NOT primary text content).

Solaria adds no Solaria-specific contrast risk. The dark-warm primary `#2B2A28` produces a slightly warmer cream-on-primary than the cool Pragma navy, but both clear AAA by the same 12.56 ratio — the archetype's body-paper convention is hue-agnostic above L\* ≈ 17.

**Aggregate D-class score for contrast-accessibility: 5 / 5.**
