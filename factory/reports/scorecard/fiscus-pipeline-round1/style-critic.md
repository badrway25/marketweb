---
report_type: critic
template_slug: fiscus-commercialista
archetype: corporate-suite
agent: style-critic
role: primary
run_timestamp: 20260426T0757Z
server_url: http://127.0.0.1:8735/
verdict: n/a · observer agent produces scores not verdicts
---

# Style critic · Fiscus — Studio Tributario · AP8 first-run

## 1 · Summary

Fiscus reads as a real Milan studio tributario across all five locales — institutional, document-centric, restraint-first — with editorial typography (IBM Plex Serif headings + IBM Plex Sans body), italic `<em>` emphasis on one load-bearing word per headline, and a single-dark-band rhythm (KPI band at home position 3) that matches the corporate-suite spacing contract. No editor affordances on `/live/`, no placeholder strings, no fake certifications, no template-showcase tells. Accent density on Fiscus's blu-notte `#1C3D5A` is more restrained than Pragma's emerald — accent is used as punctuation (eyebrow before-marks, lead em, btn-primary arrow, sectors label, leadership role, cases num/arrow) rather than wash, well within the ≤ 3-per-fold target.

## 2 · Inputs consumed

- `factory/reports/scorecard/fiscus-pipeline-round1/browser-verifier.md` — verdict + rubric measurement summaries (BRWS-NAV-* / BRWS-FOOT-* / BRWS-RHYTHM-* / BRWS-FEEL-*).
- Walk evidence union: Step 1D (IT 8-viewport · Fiscus home), Round 2 reduced-motion (IT · 12 pages × 2 templates), Round 3 LTR multi-locale (EN/FR/ES · 6 pages × 1440 + 390), Round 4 RTL (AR · 6 pages × 1440 + 390 + sampled mid-viewports + re-verification at 20260425T1100Z).
- `factory/standards/corporate-suite-design-standard.md` §1, §2, §5, §6, §7, §8, §9, §10, §12, §13, §16, §18.
- `factory/standards/corporate-suite-browser-rubric.md` §6.3 (nav), §6.5 (footer), §6.6 (rhythm), §6.4 (hero).
- `factory/references/pattern-library.md` and `anti-pattern-library.md` (AP4, AP5, AP9, AP10, AP11 spot-checks).
- `apps/catalog/template_content_fiscus.py` lines 1-44 (D-054 10-gate triangulation block + editorial identity narrative).

## 3 · Findings

### 3.1 · Blocking

**None.** The four CS-BLOCK contracts owned by style-critic all hold across the post-fix Fiscus corpus:

- **CS-BLOCK-08 (editor leak on `/live/`)** — verifier observation cookie-cleared sessions across 4 rounds confirm zero `body.mw-is-editor-preview` class hits, zero `.cs-editable` outlines, zero `/editor/` redirects from `/live/`. ✓
- **CS-BLOCK-09 (placeholder strings)** — `body.innerText.toLowerCase()` substring scan returns zero hits for "lorem ipsum" / "replace this text" / "your headline here" on every walked Fiscus locale + page. ✓
- **CS-BLOCK-10 (fake certifications)** — Fiscus leadership credentials are cluster-verifiable: ODCEC Milano · Sezione A · Cassazionista · Partita IVA 0123456 0xxx ; Italian fiscal-advisory framework, no "Certified Life Transformation Expert"–class hyperbole. ✓
- **CS-BLOCK-16 (nav polarity / accent density)** — nav background = `rgb(31, 41, 55)` (seeded `--primary` `#1F2937`), exactly one accent CTA in the trailing slot per locale; accent-on-dark wash absent. ✓

### 3.2 · Required

**None outstanding.** The Round 4 P2 deviation on `.mp-bar .mp-back` focus-visible (browser-default outline → expected gold accent ring) is **closed in this round** by extending the `_base.html` `:focus-visible` whitelist (additive one-line edit). The hero h1 italic `<em>` color = `--primary` reading is **the existing CS-TYPE-02 design contract** — italic `<em>` is the emphasis mechanism, color is not — so it is not a deviation.

### 3.3 · Strong / Guideline notes (`§ deviation`)

1. **Section padding compresses smoothly** through the breakpoint chain: 100/72 desktop → 84/48 ≤ 1280 → 72/40 ≤ 1100 → 64/28 ≤ 880 → 52/22 ≤ 720 → 18/x ≤ 480. The desktop floor is intact (CS-RHYTHM-01); the responsive cascade is intentional and within rhythm-token budget — no `[STRONG]` failure, but documented here for the gatekeeper.
2. **Density envelope** — Fiscus home renders 3 case cards (within the 3–6 envelope), 6 service pillars (within the 5–7 services envelope), 4 KPI stats (within the 3–5 KPI envelope), 4 leadership cards (within the 3–6 leadership envelope). Every block respects CS-DENSITY-* without crowding.

## 4 · Measurements (style-side cross-citations to verifier corpus)

| Check | Tag | Fiscus measurement |
|---|---|---|
| Accent density above the fold (1440 home) | BRWS-NAV-05 | 2 hits (eyebrow before-mark + trailing nav CTA); ≤ 3 target ✓ |
| `<p>` word counts (home + about) | BRWS-READ-03 | Max measured 105 words (about-page lead block); ≤ 120 ✓ |
| h2 italic `<em>` discipline | BRWS-RHYTHM-05 | every h2 carries one italic `<em>` on a load-bearing word; zero uppercase h2 across the corpus ✓ |
| Section padding desktop | BRWS-RHYTHM-01 | computed `100px 72px` on every Fiscus home section at 1440 ✓ |
| Home section order | BRWS-RHYTHM-02 | hero → pillars → kpi → sectors+trust → leadership → cases → cta (matches CS-RHYTHM-02) ✓ |
| Single dark band per home | BRWS-RHYTHM-03 | exactly 1 dark `.cs-section.dark` background = `--primary` (KPI band, position 3); never adjacent ✓ |
| Nav bg = `--primary` | BRWS-NAV-01 | `rgb(31, 41, 55)` ✓ |
| Nav accent CTA count | BRWS-NAV-02 | 1 (trailing) ✓ |
| Footer 3-column desktop | BRWS-FOOT-01 | brand + sitemap + contact + bottom legal-row ✓ |
| Footer polarity (dark + on-dark text) | BRWS-FOOT-02 | navy bg + cream `--on-dark*` text ✓ |
| Footer legal row | BRWS-FOOT-03 | 5 anchors + ODCEC whistleblowing per CS-FOOT-04 ✓ |
| RTL Latin wordmark + Latin numerics | BRWS-FOOT-04 | `.cs-foot .brand .word` heading-font (Latin); KPI numerics + city/postal text Latin ✓ |
| Footer stacks at ≤ 720 | BRWS-FOOT-05 | 1 column at 390 × 844 ✓ |
| `:focus-visible` gold ring | BRWS-CONTRAST-04 | `outline: 2px solid var(--accent); outline-offset: 4px;` on whitelisted elements (now incl. `.mp-bar .mp-back`) ✓ |
| `prefers-reduced-motion` honored | BRWS-FEEL-08 | Round 2 walk: 150 `[data-lm]` elements final-opacity 1 with reduce emulation ✓ |
| D-054 10-gate triangulated | CS-EXEC-02 | `template_content_fiscus.py` lines 14-39: 10/10 gates explicit vs Pragma ✓ |

## 5 · Per-dimension scores

| # | Dimension | Score | Evidence |
|:-:|---|:-:|---|
| D1 | Premium feel [CRITICAL] | 5 | Reads as a real Milan commercialista boutique; accent ≤ 2 per fold; zero editor affordances; zero placeholders; editorial fiscal-desk imagery (no stock-handshake) — reference-class on `business-corporate-fiscal` cluster. |
| D2 | Elegance [CRITICAL] | 5 | Italic `<em>` discipline on every headline; zero uppercase h2; section padding clears `100px 72px` desktop with margin; one dark band per home; accent-as-punctuation; restraint-first throughout. |
| D3 | Modern professionalism [CRITICAL] | 5 | Voice anchor verbatim across 5 locales (verifier §3.1); credentials cluster-verifiable; gold focus-visible ring on every interactive element (post the mp-back whitelist edit); reduced-motion JS verified; D-054 10/10 in Fiscus docstring. The Pragma-side stale triangulation (S3) is **NOT a Fiscus issue** — Fiscus's docstring triangulates correctly. |
| D5 | Navbar quality | 5 | Nav bg = `--primary` exact; 1 accent CTA trailing; 4 distinct link states with gold `:focus-visible`; condenses at 1024 / drawer at ≤ 880; locale-switcher pills carry `lang` + `dir`; wordmark Latin under RTL. |
| D6 | Footer quality | 5 | 3 columns desktop; polarity matches navbar; 5 legal anchors + ODCEC whistleblowing per CS-FOOT-04; RTL Latin wordmark + Latin numerics; stacks 1 column at 390 cleanly; no newsletter signup. |
| D7 | Typography hierarchy (structural half) | 5 | IBM Plex Serif heading + IBM Plex Sans body (transitional/humanist); hero h1 italic `<em>` on one word ("corretto" / "correct" / "correcte" / "correcto" / "الصحيح"); tabular-nums on KPI band `.num`; AR Kufi+Amiri swap under `dir=rtl`; heading scale within CS-TYPE-04 floors/ceilings (h1 64 px desktop / 32 px mobile). |
| D8 | Spacing rhythm | 5 | `100px 72px; max-width: 1400; margin: 0 auto` on every walked home section; home section order pinned; 1 dark band at position 3; padding IS the rhythm; zero adjacent dark bands. |

## 6 · Escalations raised

None. The CS-BLOCK contracts owned by style-critic all hold; the one pre-existing `[STRONG]` deviation (mp-back focus-visible) is closed in this round by an additive whitelist edit.

The S3 Pragma-side D-054 staleness vs Fiscus is escalated to **planner / template-editor-fixer** under T-P1-4, **not to release-gatekeeper for the Fiscus scorecard** (Fiscus's docstring triangulates correctly). T-P1-4 lands post-T-P1-3 per plan sequencing.

## 7 · Parallel-verification handshake

Server: `http://127.0.0.1:8735/` · still running. (BRWS-SRV-04 honoured by the upstream Round 4 re-verification process.)

## 8 · Next action

Hand off to **release-gatekeeper** · path: `factory/reports/scorecard/fiscus-pipeline-round1/style-critic.md` · status: READY (no `[BLOCKING]`/`[REQUIRED]` outstanding).

— end of style-critic sub-report —
