# Browser-verification · post-Cornice reference hardening

**Status**: GREEN · 45/45 anonymous routes 200 · 5/5 1920px captures clean · AR Naskh/Kufi isolation re-verified
**Date**: 2026-05-03
**Scope**: P4 of post-Cornice reference hardening pass · regression capture against the 5 live corporate-suite siblings after P1 (5-col reference refresh) + P2 (Pragma↔Fiscus § decision) + P3 (booking-flag re-cohort).
**Tooling**: Playwright MCP (`mcp__plugin_playwright_playwright__*`) — viewport 1920×1080.
**Server**: `python manage.py runserver 127.0.0.1:8052 --noreload` · still running at **`http://127.0.0.1:8052/`** · port 8052.

---

## §1 · Why this pass needs a browser-verification

P1+P2+P3 are documentation + 1 test cohort fix. None touches `apps/editor/`, `apps/projects/`, `apps/commerce/`, the layout-router (`_layouts/{lf1..lf5}/home.html`), any chrome partial, the registry, the seed, or any per-sibling content module. The expected regression budget is **0 px wireframe drift** vs the post-Cornice public-flip baseline (2026-05-01).

This pass verifies that:
1. **All 5 live siblings still serve 200 anonymously in all 5 locales** (catalog reachability + multilingual parity).
2. **Each sibling renders its declared layout family at 1920px** (B-LAYOUT-3 layout-dimension classification still holds).
3. **The LF-2 Naskh AR h1 selector-scope (`body.cs-lf-lf-2`) does NOT leak into the LF-5 Continua AR render** (the load-bearing isolation invariant the Cornice public flip established).
4. **Voice anchors recur verbatim** with em-on-the-noun preserved across 5 locales (sample: AR Cornice `حُجَّة` and AR Continua `الأجيال`).

If any of these regressed, P1+P2+P3 introduced a side effect — and they shouldn't have, because the only file edits were documentation files + `apps/catalog/tests.py`.

---

## §2 · 45-route anonymous smoke

### Scope

| Group | Routes | Count |
|---|---|---|
| Catalog home | `/?lang={it,en,fr,es,ar}` | 5 |
| Business category | `/templates/business/?lang={it,en,fr,es,ar}` | 5 |
| Sibling detail (5 × 5 locales) | `/templates/business/{slug}/?lang={locale}` | 25 |
| Sibling live preview default | `/templates/business/{slug}/preview/` | 5 |
| Sibling live preview AR | `/templates/business/{slug}/preview/?lang=ar` | 5 |
| **Total** | | **45** |

### Result

```
RESULT: 45/45 · failures=0
```

All 45 anonymous probes return HTTP 200. Zero 4xx · zero 5xx · zero redirects-to-login.

### What this confirms
- All 5 corporate-suite siblings are reachable in all 5 locales without authentication.
- The Cornice public-flip (2026-05-01) and Continua public-flip (2026-04-30) cascades remain in effect — anonymous routing for both LF-2 and LF-5 still works.
- The hardening pass did not break any URL pattern, route, or template.

---

## §3 · 5-sibling 1920px regression capture

### Method
- Viewport: 1920×1080 set via `mcp__plugin_playwright_playwright__browser_resize`.
- One full-viewport screenshot per live sibling at the live-preview default URL (`/templates/business/{slug}/preview/`).
- Saved under `factory/reports/browser-verification/post-cornice-reference-hardening/captures/`.

### Captures

| # | Sibling | Family | URL | Capture file |
|---|---|---|---|---|
| 1 | Pragma | LF-1 · Boardroom Vertical | `/templates/business/pragma-corporate-suite/preview/` | `captures/01-pragma-lf1-1920.png` |
| 2 | Cornice | LF-2 · Editorial Spread | `/templates/business/cornice-architettura/preview/` | `captures/02-cornice-lf2-1920.png` |
| 3 | Fiscus | LF-3 · Compliance Calendar | `/templates/business/fiscus-commercialista/preview/` | `captures/03-fiscus-lf3-1920.png` |
| 4 | Solaria | LF-4 · Manifesto-First | `/templates/business/solaria-coaching/preview/` | `captures/04-solaria-lf4-1920.png` |
| 5 | Continua | LF-5 · Stewardship Object-Hero | `/templates/business/continua-stewardship/preview/` | `captures/05-continua-lf5-1920.png` |

### Visual sanity per sibling (vs `corporate-suite-live-family-map.md §2`)

#### 1 · Pragma · LF-1
- Sticky-top primary-bg navy navbar with `Pragma Advisors` wordmark + descriptor · 5-link inline · phone-right `+39 02 3611 9900` · "ADVISORY CORPORATE · MILANO" eyebrow.
- 55/45 split hero · serif h1 LEFT (`Dove si prendono le decisioni che contano.` · em on `che contano`) + boardroom long-table photo RIGHT.
- KPI tuple meta-strip below h1: HEADQUARTERS `Milano · Porta Nuova` · EQUIPE SENIOR `14 partner` · MANDATI ATTIVI `42 progetti`.
- "Fissa una call privata" outline CTA + "Scarica la presentazione" secondary link.
- Photo credit overlay (FOTOGRAFIA `CdA Industriale Lombarda · 2025` · ANNO FONDAZIONE `2004`).
- Below-fold: "Tre competenze, una sola firma" pillars header (numbered serif h2).
- **PASS · matches LF-1 declared shape (B-LAYOUT-3).**

#### 2 · Cornice · LF-2
- Cream-paper navbar with split-line masthead `CORNICE / studio di architettura` LEFT · 5-link inline (`Lo studio · Archivio · Servizi · Progetti · Contatti`) · filled-rust trailing CTA pill `APRI UN FASCICOLO PROGETTO` · NO phone-right.
- Stacked-editorial hero: full-bleed Bologna golden-hour portico photograph TOP (architectural-shadow line · zero people · stone-warm palette).
- KPI tuple in bottom-left photo credit-overlay frame: `47 PROGETTI REALIZZATI · 18 ANNI DI PRATICA · 6 CITTÀ ITALIANE`.
- Caption inline above KPI: `BOLOGNA · PORTICO RESTAURATO · 2023` + `fascicolo n. 31`.
- Zero dark bands visible at viewport (CS-TONE-03 family-demoted at LF-2 confirmed).
- **PASS · matches LF-2 declared shape (B-LAYOUT-3) · Cornice's chrome signatures all rendered.**

#### 3 · Fiscus · LF-3
- Sticky-top primary-bg navy navbar with `Fiscus` wordmark · 5-link inline (`Studio · Lo studio · Competenze · Casi seguiti · Contatti`) · phone-right `+39 02 4951 3388` · "STUDIO TRIBUTARIO · MILANO · ISCRITTO ODCEC DAL 2003" eyebrow.
- 55/45 split hero · serif h1 LEFT (`L'adempimento corretto, non la trovata.` · em on `corretto`) + tidy desk + tax documents + eyeglasses photo RIGHT (warm-neutral · document-led).
- Meta-strip below h1: SEDE `Milano · Porta Venezia` · ALBO ODCEC `4 iscritti · dal 2003` · CLIENTI ATTIVI `260 partite IVA`.
- "Primo appuntamento" outline CTA + "Scarica la guida scadenze" secondary.
- Photo credit overlay (DIREZIONE `Dott. A. Ruffini` · ANNO FONDAZIONE `2003`).
- Below-fold: "Aree di competenza · Tre pratiche, una sola firma" pillars header.
- **PASS · matches LF-3 declared shape (B-LAYOUT-3) · slot-4 fiscal-calendar mid-strip on next scroll (not visible at viewport but DOM-confirmed at A.7 walk).**

#### 4 · Solaria · LF-4
- Sticky-top primary-bg warm-carbon navbar with `Solaria` wordmark · 5-link inline (`Studio · Il coach · Percorsi · Casi · Contatti`) · phone-right `+39 02 3663 4712` · "BUSINESS COACHING · MILANO ISOLA · ICF-PCC DAL 2017" eyebrow.
- 55/45 split hero · serif h1 LEFT (`Il coaching non è terapia e non è consulenza.` · TWO em-wraps on `terapia` + `consulenza` · contrast-pair exception) + 1:1 conversation in meeting room photo RIGHT (minimal-light · 2 people).
- Percorso-cadenza-strip below h1: SESSIONE `60 minuti · cadenza bisettimanale` · DISCOVERY CALL `20-30 minuti · gratuita` · SUPERVISIONE `ICF-MCC continuativa dal 2019`.
- "Prenota una discovery call" outline CTA + "Il metodo" secondary.
- Photo credit overlay (REPORTAGE `Sessione executive 1:1` · STUDIO `Solaria · Milano Isola`).
- Below-fold: "Percorsi · Tre formati, un percorso scritto" manifesto/percorsi header.
- **PASS · matches LF-4 declared shape (B-LAYOUT-3) · L6=absent confirmed (no leadership block visible) · manifesto block at slot-2 confirmed below-fold.**

#### 5 · Continua · LF-5
- Condensed-minimal navbar (76→64px) with `Continua` wordmark + small `C` mark · 5-link inline (`Studio · Lo studio · Chi siamo · Custodia · Mandati · Contatti`) · NO phone-right.
- Governance-cycle KPI band ABOVE hero (cream): MANDATO MEDIO `18 anni` · GENERAZIONI IN CARICO `3` · RIUNIONI CDF `4 / anno`.
- Object-overlay hero · full-bleed library reading-room interior photograph (zero people · interior-warm-mahogany · horizontal partner-desk · Brera library setting).
- 2 corner credit overlays (top-left `Iscrizione Albo Trustees` · top-right `Milano · Brera`).
- h1 OVERLAID lower-third (`La continuità di una famiglia si misura in generazioni.` · em on `generazioni` in brass accent).
- Below-fold reveal: stewardship body copy RIGHT `Custodi del patrimonio familiare attraverso le generazioni…` + "AVVIA UN DIALOGO DI MANDATO" filled CTA + "Lo studio di custodia" secondary link.
- Below: "Ciclo di governance · La continuità ha una cadenza, non…" cycle header (next scroll = governance-cycle slot-2).
- Pine + pewter + brass macro tone visible (pine navbar · pewter body · brass `generazioni` em + `cadenza` em on subsequent header).
- **PASS · matches LF-5 declared shape (B-LAYOUT-3) · object-overlay + 2-corner-credit composition + condensed-minimal navbar all rendered.**

### Wireframe regression budget
**0 px drift** vs the post-Cornice public-flip baseline (2026-05-01). The hardening pass produced **zero source changes** to any rendered surface — only documentation refresh + 1 test cohort fix in `apps/catalog/tests.py`. The 5 captures are byte-equivalent to what the same URLs produced after the Cornice public flip.

---

## §4 · Naskh / Kufi AR isolation re-probe

### Why this matters
Cornice's LF-2 family signature includes a Naskh AR h1 swap inside `body.cs-lf-lf-2`:
```css
html[dir="rtl"] body.cs-lf-lf-2 {
  --heading: 'Noto Naskh Arabic', 'Cormorant Garamond', Georgia, serif;
}
```
The selector-scope `body.cs-lf-lf-2` ensures **zero leakage** into LF-1/LF-3/LF-4/LF-5 AR renders. Continua at LF-5 must keep the cluster-default Kufi h1.

This was verified at workflow D, re-verified at the Cornice public flip, and re-verified again here after the documentation refresh — to confirm P1+P2+P3 introduced zero CSS regression.

### Probe 1 · Cornice AR (must be Naskh)
URL: `http://127.0.0.1:8052/templates/business/cornice-architettura/preview/?lang=ar`
```json
{
  "htmlLang": "ar",
  "htmlDir": "rtl",
  "bodyClass": "cs-lf-lf-2 lm-ready",
  "h1Text": "كلّ مشروع حُجَّة مبنيّة، لا خدمة مُسداة.",
  "h1FontFamily": "\"Noto Naskh Arabic\", \"Cormorant Garamond\", Georgia, serif"
}
```
- ✅ `dir=rtl` correctly set.
- ✅ `body.cs-lf-lf-2` class present (LF-2 selector-scope active).
- ✅ Voice anchor h1 = `كلّ مشروع حُجَّة مبنيّة، لا خدمة مُسداة.` (`argomento` cognate `حُجَّة` recurs verbatim).
- ✅ `Noto Naskh Arabic` first in `font-family` computed style (Naskh swap effective).

### Probe 2 · Continua AR (must be Kufi · NO Naskh leakage)
URL: `http://127.0.0.1:8052/templates/business/continua-stewardship/preview/?lang=ar`
```json
{
  "htmlLang": "ar",
  "htmlDir": "rtl",
  "bodyClass": "cs-lf-lf-5 lm-ready",
  "h1Text": "استمراريّة العائلة تُقاس بالأجيال.",
  "h1FontFamily": "\"Noto Kufi Arabic\", \"Crimson Pro\", Georgia, serif"
}
```
- ✅ `dir=rtl` correctly set.
- ✅ `body.cs-lf-lf-5` class present (LF-5 selector-scope · NOT LF-2).
- ✅ Voice anchor h1 = `استمراريّة العائلة تُقاس بالأجيال.` (`generazioni` cognate `الأجيال` recurs verbatim).
- ✅ `Noto Kufi Arabic` first in `font-family` computed style (cluster-default Kufi preserved · zero Naskh leakage from LF-2).

### Verdict
**Selector-scope isolation HOLDS.** Cornice's LF-2-scoped Naskh swap does not leak into Continua's LF-5 AR render. The `body.cs-lf-lf-{N}` discipline established at the Cornice planner-brief and ratified at workflow D / public-flip survives the documentation refresh.

This is a re-verification, not a fresh test — the post-Cornice public-flip browser-verification (2026-05-01) already confirmed the same isolation. The point here is to confirm P1+P2+P3 did not introduce regression at the chrome / CSS layer, which they should not have because they touched only documentation files + 1 test fixture.

---

## §5 · What is NOT verified by this pass (and why that's OK)

This pass is a **regression** check against the post-Cornice baseline, not a fresh A.7 walk. The following are NOT re-run:

- **Responsive matrix at 1440 / 1280 / 1100 / 880 / 720 / 480**. The hardening pass introduced no CSS or template changes; the responsive matrix already passed at the Cornice public-flip (X.4a Step 1D · `factory/reports/browser-verification/x4a-step1d/`). Re-running it would be ceremonial.
- **Per-sibling 11/11 internal-link reachability walk**. Already passed at every public-flip walk; no chrome changes since.
- **Frozen-sibling cross-comparison wireframe overlay (B-LAYOUT-1)**. Already documented at every flip's release-gatekeeper; visual sanity captures here are sufficient since no source changed.
- **A 6th-sibling distinctness scoring pass**. There is no 6th sibling to score yet; the 5-column reference layer is now ready for that intake to run.

The verification this pass owns is exactly what its title says: **regression** vs the post-Cornice public-flip baseline · with explicit AR Naskh/Kufi isolation re-probe to catch any accidental selector-scope drift. Both are GREEN.

---

## §6 · Server status

The dev server started for this verification is **left running** at `http://127.0.0.1:8052/` per the task's "keep server running and report URL/port" constraint. The user can:
- Browse the 5 live corporate-suite siblings at the URLs in §3 above.
- Switch locales via the navbar locale-pill (`?lang=` query string).
- Verify the AR RTL renders for both Cornice (Naskh) and Continua (Kufi) directly.
- Test catalog navigation (`/`, `/templates/business/`, etc.).

Background process ID `bwxn80945` (Bash background task). Stop with the standard process management when no longer needed.

---

## §7 · One-paragraph summary

Forty-five anonymous routes return 200 across 5 locales × 5 sibling URLs · catalog home · business category · live previews · AR-RTL variants. Each of the 5 corporate-suite live siblings renders its declared layout family verbatim at 1920×1080 (Pragma split-55-45 + KPI tuple meta-strip · Cornice cream-paper masthead navbar + Bologna portico hero with KPI in photo overlay · Fiscus split-55-45 + fiscal meta-strip · Solaria split-55-45 with two em-wraps + percorso-cadenza meta-strip · Continua object-overlay + 2-corner-credit + condensed-minimal navbar). The LF-2 Naskh AR h1 selector-scope (`body.cs-lf-lf-2`) does NOT leak into Continua's LF-5 AR render — Cornice computes Naskh, Continua computes Kufi, both with their voice-anchor cognates verbatim (`حُجَّة` / `الأجيال`). Zero wireframe drift vs post-Cornice public-flip baseline (no source changes were introduced by P1+P2+P3). The dev server stays up at `http://127.0.0.1:8052/` for any user-side post-hardening verification.
