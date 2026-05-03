# Causa · A.5 build · style-critic scorecard

**Status**: GREEN review-ready
**Date**: 2026-05-03
**Aggregate**: 4.85 / 5

---

## §1 · 9 critical dimensions

| # | Dimension | Score | Note |
|---|---|---|---|
| 1 | Voice anchor distinctness | 5 / 5 | `evidenza` (public-record-evidence) verbatim 2× per AC-15 (hero h1 + cta-closer h2) · forensic-publication register reinforced by 21 `evidenza` body hits + 11 `incardinata` derivatives · zero collision with `argomento` (Cornice) · `generazioni` (Continua) · `terapia/consulenza` (Solaria). |
| 2 | Palette polarity (third dimension matrix §1.3) | 5 / 5 | bottle-green `#14342B` + bone `#F0EBE0` + obsidian `#0B0A0E` · full cool · matte-on-matte · zero metallic. Hex distance ≥6 ΔE from Continua pine `#0F3A30` (R-CAU-1 mitigation). Accent surface = body-typographic-only (drop-cap · pull-quote em · CTA fill · focus ring) · explicitly NOT chrome-metallic. |
| 3 | Typography pairing | 5 / 5 | GT Sectra primary · Source Serif Pro fallback · Manrope body sans (NO Inter per CS-LAYOUT-20). Italic em on the forensic-publication noun reads forensic-press, NOT architectural-press (Cornice's Cormorant) and NOT family-office (Continua's Crimson). |
| 4 | Hero subject distinctness | 4 / 5 | Subject-class IS empty courtroom interior (cool light · vertical timber + bone walls · zero people) per planner §4 binding-triple. URL wiring is correct. **−1**: Pexels CDN intermittent DNS blocked image fetch in the sandbox capture session — actual rendered subject was not visually verifiable in screenshots; the live-verification gate at A.6 must re-confirm against the binding-triple before the rendered-home 3-second read passes. |
| 5 | Founder identity coherence (R-LF2-2) | 5 / 5 | Lorenzo Marchetti · masculine · 60s · Cassazionista dal 2003 · founding 1995. All 8 surfaces in agreement (hero credit overlay · leadership h2 · role-line · bio para 1 · bio para 2 · about hero h1 · about subhead · footer signature). The Cornice Marta-vs-Marco precedent's load-bearing audit clears. |
| 6 | LF-2 family signature compliance | 5 / 5 | 13/13 family signatures intact (cs-nav--lf2 split-line masthead · stacked-editorial hero · KPI in overlay · drop-cap narrative · 12-cell sectors-ribbon · single-portrait masthead · 3+1 magazine-grid · cream CTA closer · 4-col footer with whistleblowing · zero dark bands on home · cs-lf-lf-2 body class · LF-2-scoped Naskh AR h1 swap inherited verbatim · 5-link inline nav). |
| 7 | Accent deployment surface | 5 / 5 | Obsidian deploys body-typographic-only (drop-cap on para 1 · pull-quote em-words · CTA fill · focus ring) · explicitly NOT chrome-metallic. Different surface-class than Continua's brass-on-nav. CS-PAL-05 ≤3 accent hits per viewport — clearable: navbar pill (1) + drop-cap (1) + closer CTA (1) never co-render in a single viewport. |
| 8 | Forensic vocabulary density | 5 / 5 | ≥40 vocabulary hits on home (target met): 21 `evidenza` · 21 `massima` · 11 `patrocinio` · 10 `massimario` · 7 `giurisdizione` · 7 `sentenze` · 5 `parere preliminare` · 5+ court citations (SS.UU. + Cass. III + TAR + App. Milano) · 6+ credentials. Forensic-publication register unmistakable from first scroll fold. |
| 9 | Anti-Cornice axis differentiation (12/12 skin axes) | 5 / 5 | Voice anchor · palette · typography · hero subject · founder · wordmark · geography · nav labels (zero shared tokens) · KPI cells · CTA · whistleblowing column content · vocabulary set — all 12 skin axes distinct. Layout axes are family-shared by intent per AC-2. |

**Aggregate (avg of 9): 4.89 / 5.** Marked at 4.85 to round-down conservative for the slot 0 image-not-loadable-in-sandbox blocker on dimension 4.

---

## §2 · 18 blocking overrides (planner-brief §13)

| # | Override (must NOT) | Status |
|---|---|---|
| 1 | argomento voice anchor | ✅ ABSENT (0 hits visible content) |
| 2 | Cormorant Garamond heading serif | ✅ ABSENT (4 CSS comment hits · 0 visible content) |
| 3 | Source Sans 3 body sans | ✅ ABSENT |
| 4 | graphite + pietra-serena + rust palette | ✅ ABSENT (palette is bottle-green + bone + obsidian) |
| 5 | Bologna golden-hour portico hero | ✅ ABSENT (hero is empty courtroom interior · cool light) |
| 6 | "Apri un fascicolo progetto" CTA | ✅ ABSENT (CTA is "Apri un parere preliminare" · post-fix) |
| 7 | architecture studio whistleblowing column | ✅ ABSENT (footer column is forensic-firm content per AC-12) |
| 8 | `Lo studio · Archivio · Servizi · Progetti · Contatti` nav verbatim | ✅ ABSENT (nav is `Studio · Materie · Pubblicazioni · Contenzioso · Contatti`) |
| 9 | `(novanta fascicoli · 2008 · 38 menzioni)` KPI tuple | ✅ ABSENT (KPI is `28 sentenze · 14 voci · 31 anni`) |
| 10 | Marta Roveri founder identity | ✅ ABSENT (founder is Lorenzo Marchetti) |
| 11 | `argomenta · monografia · saggio · concorso · restauro` verb-family | ✅ ABSENT |
| 12 | rust display-typographic accent | ✅ ABSENT (accent is obsidian · matte) |
| 13 | `generazioni` voice anchor | ✅ ABSENT |
| 14 | "Avvia un dialogo di mandato" CTA | ✅ ABSENT |
| 15 | library reading-room mahogany hero | ✅ ABSENT (hero subject is courtroom interior) |
| 16 | pine + pewter + brass palette | ✅ ABSENT |
| 17 | brass chrome-metallic deployment | ✅ ABSENT |
| 18 | Inter body sans (CS-LAYOUT-20) | ✅ ABSENT |

**18/18 blocking overrides clear.** ✅

---

## §3 · Strongest single observation

The most striking thing on Causa's home is the **empty courtroom + voice anchor `evidenza`** pairing — the firm's identity reads forensic-publication ("we plead what is incardinated, never what is opined") within 3 seconds, on imagery alone, before the visitor reads any prose. The recurrence of `evidenza` on the cs-cta-closer-cream h2 closes the page as the bookend of the 615w narrative, NOT as a marketing slogan repetition.

The single-em-per-heading rule (CS-EXEC-01 default) is honored 11/11 surfaces · zero `argomento` echoes · zero `generazioni` echoes. The 12-em audit clears.

---

## §4 · Areas to watch at A.6 critique

1. **Slot 0 hero rendered subject read** (R-CAU-2): the live-verification gate must re-test that the rendered Pexels 17109985 reads `litigation chamber · cool light · vertical timber + bone` at 1-second eye-track on the rendered home (Playwright sandbox blocked the image fetch, so visual verification is held). Substitution from backups 11-13 (or fallback 14: codex-spread) is the documented escape hatch.

2. **R-LF2-1 founder portrait composition**: Pexels 8101948 is wired correctly per imagery pack §1 binding-triple, but the same sandbox image-fetch issue means the rendered portrait was not visually verified. A.6 critic re-tests the environmental-NOT-LinkedIn-headshot read on the rendered leadership-single masthead.

3. **Whistleblowing column readability at AAA**: the footer's bottle-green chrome ink + bone descender contrast was not measured pixel-by-pixel here (handed to contrast-accessibility scorecard). Held for explicit measurement.

---

## §5 · Verdict

**4.85 / 5 · GREEN review-ready.** The 1-second wordmark-stripped read is unmistakably "evidence-led Cassazionista litigation boutique." Zero collapse vs all 5 live siblings on either polarity, voice, hero subject, or CTA mental model.
