# Causa · A.6 IT review-lock · live browser verification

**Status**: PARTIAL — copy/chrome/typography/palette LOCKED · imagery HELD pending A.5b re-curate
**Date**: 2026-05-03
**Test client**: Playwright MCP (1440×900 lead · 880×900 tablet · 375×800 mobile) + Python urllib opener with Django session cookie (staff `causa_review_a6` · is_staff=True · is_superuser=True)
**Server**: `http://127.0.0.1:8052/` · port 8052 · running in background
**Captures**: `factory/reports/browser-verification/causa-a6-it-review-lock/captures/` (20 JPEGs)

---

## §1 · Route walk · staff `?preview=1` (must be 200) · post-fix

| # | Route | Status | Length | Title |
|---|---|---|---|---|
| 1 | `/templates/business/causa-legale/preview/` (home) | **200** | 104,466 | CAUSA — Studio |
| 2 | `/templates/business/causa-legale/preview/studio/` | **200** | 69,007 | CAUSA — Pubblicazioni |
| 3 | `/templates/business/causa-legale/preview/materie/` | **200** | 70,107 | CAUSA — Materie |
| 4 | `/templates/business/causa-legale/preview/contenzioso/` | **200** | 61,299 | CAUSA — Contenzioso |
| 5 | `/templates/business/causa-legale/preview/contatti/` | **200** | 70,709 | CAUSA — Contatti |
| 6 | `/preview/contenzioso/cass-ssuu-responsabilita-consulente-fiscale-2024/` | **200** | 64,011 | CAUSA — Contenzioso |
| 7 | `/preview/contenzioso/cass-civ-iii-anatocismo-bancario-2023/` | **200** | 63,330 | CAUSA — Contenzioso |
| 8 | `/preview/contenzioso/tar-lombardia-agcom-proporzionalita-2022/` | **200** | 63,395 | CAUSA — Contenzioso |
| 9 | `/preview/contenzioso/appello-milano-art-36bis-dpr-600-1973-2021/` | **200** | 63,260 | CAUSA — Contenzioso |

**9/9 staff-preview routes 200.** ✅ Home grew by ~4.5KB vs A.5 (104,466 vs
100,006) due to the placeholder data URL appearing 10 times in the rendered
HTML (each ~836 bytes inline).

---

## §2 · Anonymous draft-gate (must be 404)

| Route | Expected | Got | Verdict |
|---|---|---|---|
| `/templates/business/causa-legale/preview/` | 404 | 404 | ✅ |
| `/preview/contenzioso/cass-ssuu-...-2024/` | 404 | 404 | ✅ |
| `/templates/business/` (catalog · Causa MUST NOT appear) | 200 + Causa absent | 200 + `causa-legale` not in body | ✅ |
| `/` (homepage trust counter `templates_live`) | "24+" | "24+" preserved | ✅ |

**4/4 anonymous draft-gate checks pass.** ✅ Tier=draft preserved · catalog
count unchanged at 24 published_live · Causa NOT visible to public.

---

## §3 · Frozen sibling regression (post-fix · byte-equivalent vs A.5)

| Sibling | LF | Anonymous home | A.5 length | A.6 length | Verdict |
|---|---|---|---|---|---|
| Pragma | LF-1 | **200** | 87,112 | 87,112 | **NO REGRESSION** (byte-equivalent) |
| Cornice | LF-2 | **200** | 98,673 | 98,673 | **NO REGRESSION** (byte-equivalent) |
| Fiscus | LF-3 | **200** | 88,010 | 88,010 | **NO REGRESSION** (byte-equivalent) |
| Solaria | LF-4 | **200** | 88,449 | 88,449 | **NO REGRESSION** (byte-equivalent) |
| Continua | LF-5 | **200** | 94,640 | 94,640 | **NO REGRESSION** (byte-equivalent) |

**5/5 frozen siblings byte-equivalent before/after A.6 fix.** Cornice
control screenshot at `captures/20-cornice-1440-control.jpeg` confirms
Bologna golden-hour portico hero + Cormorant Garamond + filled rust pill
"APRI UN FASCICOLO PROGETTO" + KPI tuple `47 / 18 / 6` all intact.

---

## §4 · Per-Pexels-URL direct verification (the load-bearing A.6 test)

A.5 reported the Pexels CDN as "sandbox-blocked at this build" (Issue 3).
A.6's brief explicitly asked the reviewer to "distinguish clearly between
real product issue and tooling issue." A.6 navigated each Pexels URL
directly in the Playwright browser sandbox AND saved the rendered photo
to disk for evidence.

**Method**. For each Pexels ID in the curator pack
(`docs/content-factory/imagery/packs/business-litigation.md`), Playwright
navigated to `https://images.pexels.com/photos/<id>/pexels-photo-<id>.jpeg
?auto=compress&cs=tinysrgb&w=<width>` and a screenshot was saved at the
viewport. The screenshot contents were then compared to the curator's
binding caption and the planner-brief subject-class binding rules.

| Slot | Pexels ID | Page title (proves URL resolved) | Rendered content (capture) | Caption match | Capture file |
|---|---|---|---|---|---|
| 0 hero | 17109985 | `pexels-photo-17109985.jpeg (1600×1067)` | group portrait of casual youths · sepia/dark setting · "JEAN YLLANA" sign · multiple people | **NO MATCH** (curator: "empty courtroom interior · zero people") | `02-hero-pexels-direct.jpeg` |
| 11 hero backup | 15796091 | `pexels-photo-15796091.jpeg (1600×2000)` | single palm tree silhouetted against grey-blue sky | **NO MATCH** (curator: "empty European court chamber · light timber-and-bone interior") | `03-backup11-15796091.jpeg` |
| 12 hero backup | 8112167 | (page returns 404) | white page with text "404" in top-left | **404 · URL DOES NOT EXIST** | `04-backup12-8112167.jpeg` |
| 13 hero backup | 4427451 | `pexels-photo-4427451.jpeg (1600×2133)` | night cityscape · church/castle silhouette + medieval town wall | **NO MATCH** (curator: "empty courtroom interior with vertical timber columns") | `05-backup13-4427451.jpeg` |
| 14 hero backup PRE-CLEARED FALLBACK | 7841457 | `pexels-photo-7841457.jpeg (1600×1067)` | three-person consultation in warm wood-panelled office · burgundy leather chairs · mahogany desk · framed paintings | **NO MATCH** (curator: "Codex-spread on chambers desk wide-shot · zero people") + **WARM-MAHOGANY COLLISION** with R-CAU-2 (Continua adjacency) + 3 PEOPLE | `06-backup14-7841457.jpeg` |
| 2 founder portrait | 8101948 | `pexels-photo-8101948.jpeg (800×600)` | bowl of food (Mexican-style ceviche / shredded mixed dish) in terracotta dish on light wooden surface | **NO MATCH** (curator: "Senior man (60s · greying hair · horn-rimmed eyeglasses · charcoal-grey three-piece suit) seated at chambers desk") | `07-portrait-8101948.jpeg` |
| 7 case-card hero | 9489162 | `pexels-photo-9489162.jpeg (1200×1500)` | half-nude male model seated on white fabric backdrop · studio portrait | **NO MATCH** (curator: "Italian high-court exterior detail · classical pediment") | `08-case-9489162.jpeg` |
| 1 feature | 6077368 | `pexels-photo-6077368.jpeg (1200×801)` | residential bay-window living-room · cream couches with burgundy throw cushion · panoramic city view | **NO MATCH** (curator: "Open Italian law codex · single tome · zero hands") | `09-feature-6077368.jpeg` |

**Verdict: 8 / 8 sampled Pexels IDs return content categorically different
from curator captions.** This is not a sandbox CDN issue (the URLs resolve
and return 200 with photo content); it is a curator-layer issue (the IDs
were never real-Pexels assignments for the captioned subjects). The pack's
backup roster is also unusable (1/4 returns 404; 3/4 return wrong-subject
content).

**Reclassification of A.5 Issue 3**: from "sandbox-only · NOT FIXED" to
**REAL PRODUCT DEFECT · curator-hallucinated Pexels IDs · imagery pack
must be re-curated at A.5b**.

---

## §5 · Post-fix DOM probes on Causa home

Verified via Playwright `browser_evaluate` at `/preview/?preview=1` after the
F1 mitigation (10 photo URL constants → single `_IMAGERY_HOLD_PLACEHOLDER`
base64 SVG data URL).

| Probe | Expected | Got | Verdict |
|---|---|---|---|
| `document.title` | "CAUSA — Studio" | "CAUSA — Studio" | ✅ |
| `body.className` includes `cs-lf-lf-2` | true | `cs-lf-lf-2 lm-ready` | ✅ |
| `.cs-nav` has `cs-nav--lf2` | true | yes | ✅ |
| Hero h1 text (voice anchor) | verbatim 11-word IT sentence | exact match | ✅ |
| `.cs-hero .photo` background-image | data URL containing `image/svg+xml;base64` | `data:image/svg+xml;base64,PHN2ZyB4bWxucz0i...` (824 base64 chars) | ✅ (placeholder rendered) |
| Hero photo `aspect-ratio` | 24/11 | `24 / 11` | ✅ |
| KPI tuple cells (3) | 28 / 14 / 31 | exact match · `tabular-nums` applied | ✅ |
| Sectors-ribbon segments | 12 cells | 12 cells (penale tributario · civile contrattualistica · ... · ENCA mediation) | ✅ |
| Leadership single img.src | placeholder | `data:image/svg+xml;base64,...` | ✅ (placeholder rendered) |
| Leadership single img.alt | "Lorenzo Marchetti" | exact match | ✅ (functional but generic — F2 deferred to A.5b) |
| Leadership h2 text | "Lorenzo Marchetti" | exact match | ✅ (em on `Marchetti` preserved) |
| Leadership label | "STUDIO FOUNDER · AVVOCATO CASSAZIONISTA" | exact match | ✅ |
| Magazine cards | 4 (1 hero + 3 small) | 4 cards · `card--hero` + 3 × `card--small` | ✅ |
| Magazine card 1 (hero) h3 em | `incardinata` | `incardinata` | ✅ |
| CTA closer h2 (voice anchor recurrence 2/2) | verbatim sentence | exact match | ✅ |
| Footer whistleblowing column | present (D.lgs. 24/2023) | `cs-foot-col--whistleblowing` present + populated | ✅ |
| Navbar pill | "APRI UN PARERE PRELIMINARE" | exact match | ✅ |
| `--primary` CSS variable | `#14342B` | `#14342B` | ✅ |
| `--secondary` CSS variable | `#F0EBE0` | `#F0EBE0` | ✅ |
| `--accent` CSS variable | `#0B0A0E` | `#0B0A0E` | ✅ |
| `--heading` CSS variable | `'GT Sectra', Georgia, ...` | `'GT Sectra', Georgia, 'Times New Roman', serif` | ✅ |
| `--body` CSS variable | `'Manrope', system-ui, ...` | `'Manrope', system-ui, sans-serif` | ✅ |
| Document `scrollHeight` (1440 viewport) | ~9500px | 9555px | ✅ |
| Voice anchor verbatim count on home | 2 | 2 | ✅ |
| em-word count on home | 12 | 12 | ✅ |

**24 / 24 DOM probes PASS.** ✅ The placeholder mitigation preserves all
non-photographic surfaces. The imagery axis renders as a deliberate hold
pattern, not as a broken render.

---

## §6 · Per-page navbar pill audit (post-fix · all 9 pages)

The corporate-suite shared `_base.html:1241` defaults the trailing CTA pill
to `{{ page_data.primary_cta|default:"Apri un fascicolo" }}` (Cornice's
literal). Verified live on every page.

| Page | Expected | Got | Verdict |
|---|---|---|---|
| home | APRI UN PARERE PRELIMINARE | APRI UN PARERE PRELIMINARE | ✅ |
| studio (`/studio/`) | APRI UN PARERE PRELIMINARE | APRI UN PARERE PRELIMINARE | ✅ |
| materie (`/materie/`) | APRI UN PARERE PRELIMINARE | APRI UN PARERE PRELIMINARE | ✅ |
| contenzioso list (`/contenzioso/`) | APRI UN PARERE PRELIMINARE | APRI UN PARERE PRELIMINARE | ✅ |
| contatti (`/contatti/`) | APRI UN PARERE PRELIMINARE | APRI UN PARERE PRELIMINARE | ✅ |
| case-detail SS.UU. 2024 | APRI UN PARERE PRELIMINARE | APRI UN PARERE PRELIMINARE | ✅ |
| case-detail Cass. III 2023 | APRI UN PARERE PRELIMINARE | APRI UN PARERE PRELIMINARE | ✅ |
| case-detail TAR 2022 | APRI UN PARERE PRELIMINARE | APRI UN PARERE PRELIMINARE | ✅ |
| case-detail App. Milano 2021 | APRI UN PARERE PRELIMINARE | APRI UN PARERE PRELIMINARE | ✅ |

**9/9 pages render the Causa-specific CTA pill.** ✅ Zero Cornice-collision
surfaces. Priority surface 4 PASS.

---

## §7 · Voice anchor verbatim recurrence audit (CS-EXEC-01 · F2 · AC-15 · post-fix)

Per LF-2 family rule: voice anchor MUST appear verbatim on EXACTLY 2 home
surfaces (hero h1 + cs-cta-closer-cream h2).

```
Voice anchor: Ogni sentenza è un'<em>evidenza</em> incardinata, non un'opinione difesa.
```

Regex extraction count on rendered home: **2** ✅

Surface map (verified live · DOM-probe text exact-match):
1. **Hero h1** (cs-hero .below .left h1 · GT Sectra 56-64px) — italic em on `evidenza` · obsidian on bone paper.
2. **CTA closer h2** (cs-cta-cream centred · GT Sectra 40px) — italic em on `evidenza` · same ink, same paper, identical wording.

The 12-em audit on home (per copy-authoring §13):

| # | Surface | Em-word | Voice anchor surface? |
|---|---|---|---|
| 1 | Hero h1 | `evidenza` | **YES** · 1/2 |
| 2 | Hero side-quote | `incardina` | NO (verb-form derived from anchor) |
| 3 | Pull-quote 1 | `giurisdizione` | NO |
| 4 | Pull-quote 2 | `massima` | NO |
| 5 | Pull-quote 3 | `sostenuta` | NO |
| 6 | Sectors counter | `2008` | NO |
| 7 | Leadership h2 | `Marchetti` | NO (founder name em) |
| 8 | Card 1 hero h3 | `incardinata` | NO (anchor's past participle resonance) |
| 9 | Card 2 small h3 | `giurisprudenza` | NO |
| 10 | Card 3 small h3 | `principio` | NO |
| 11 | Card 4 small h3 | `controversia` | NO |
| 12 | CTA closer h2 | `evidenza` | **YES** · 2/2 (verbatim recurrence) |

**12/12 em-words distinct + forensic-publication-register.** ✅ Zero
`argomento · argomenta · geometria · lotto · minore` (Cornice's set). Zero
`generazioni · custodia` (Continua's set). Voice anchor preserved through
F1's photographic hold (the em pattern is copy-only · unaffected by imagery).

---

## §8 · LF-2 family signal verification (post-fix)

Per planner-brief §2.4 LF-2 family signature contract:

| Signature | DOM probe result | Verdict |
|---|---|---|
| Body class `cs-lf-lf-2` | present (`cs-lf-lf-2 lm-ready`) | ✅ |
| Cream-paper navbar `cs-nav--lf2` | present | ✅ |
| Split-line masthead `CAUSA / studio legale` | exact match (`wm-line-1` + `wm-line-2`) | ✅ |
| Filled trailing CTA pill (NOT phone-right) | filled-bottle-green pill "APRI UN PARERE PRELIMINARE" | ✅ |
| 5-link inline nav | STUDIO · MATERIE · PUBBLICAZIONI · CONTENZIOSO · CONTATTI | ✅ |
| Stacked-editorial hero | `.cs-hero .photo` (full-bleed top) + `.below` (8/4 split) | ✅ |
| KPI tuple in photo overlay | `.cs-hero .overlay .kpi-row` with 3 cells | ✅ (legible above placeholder) |
| Narrative essay drop-cap + 3 pull-quotes + side-rail | `.cs-narrative` + `.dropcap` + 3 `.pull-quote` + `.side-rail` 4 anchors | ✅ |
| 12-cell sectors-ribbon | `.cs-sectors-ribbon` 12 segs | ✅ |
| Single-portrait masthead L6 | `cs-leadership-single` 1 portrait | ✅ (placeholder · structure intact) |
| 3+1 magazine-grid L7 | 1 hero card + 3 small cards | ✅ (placeholders × 4 · structure intact) |
| Cream-hairline CTA closer (NOT dark) | `cs-cta-cream` background paper | ✅ |
| 4-col footer with whistleblowing column | `cs-foot-col--whistleblowing` populated | ✅ |

**13/13 LF-2 family signatures intact post-fix.** ✅

---

## §9 · Captures (20 JPEGs)

Files in `factory/reports/browser-verification/causa-a6-it-review-lock/captures/`:

### Pre-fix evidence — Pexels CDN direct probes

| # | File | Description |
|---|---|---|
| 01 | `01-home-1440-viewport.jpeg` | Causa home pre-fix · viewport 1440 · hero shows group portrait of casual youths (Pexels 17109985 wrong content) |
| 02 | `02-hero-pexels-direct.jpeg` | Direct navigation to Pexels 17109985 · confirms wrong content |
| 03 | `03-backup11-15796091.jpeg` | Direct navigation to backup 11 · single palm tree (NOT a court chamber) |
| 04 | `04-backup12-8112167.jpeg` | Direct navigation to backup 12 · 404 not found |
| 05 | `05-backup13-4427451.jpeg` | Direct navigation to backup 13 · night cityscape with church/castle (NOT a courtroom) |
| 06 | `06-backup14-7841457.jpeg` | Direct navigation to backup 14 (PRE-CLEARED FALLBACK) · 3-person warm-mahogany consultation (NOT a codex-spread · NOT zero-people) |
| 07 | `07-portrait-8101948.jpeg` | Direct navigation to founder portrait Pexels 8101948 · bowl of food (NOT a senior Cassazionista) |
| 08 | `08-case-9489162.jpeg` | Direct navigation to magazine-card-hero Pexels 9489162 · half-nude male model studio shot (NOT a high-court exterior) |
| 09 | `09-feature-6077368.jpeg` | Direct navigation to feature Pexels 6077368 · residential bay-window living-room (NOT an open codex on a chambers desk) |

### Post-fix verification — placeholder rendered

| # | File | Description |
|---|---|---|
| 10 | `10-home-1440-postfix-viewport.jpeg` | Causa home AFTER edit but BEFORE server reload (paper-only render with reveal blocks) |
| 11 | `11-home-1440-postfix-viewport.jpeg` | Causa home post-server-reload BEFORE base64 fix (Django auto-escape mangled the SVG · light gradient render) |
| 12 | `12-home-1440-postfix-viewport.jpeg` | Causa home post-base64-fix · viewport 1440 · placeholder bottle-green gradient with "imagery hold · A.5b re-curate pending" italic label · KPI tuple legible · LF-2 cream navbar + filled bottle-green CTA pill intact |
| 13 | `13-home-1440-postfix-fullpage.jpeg` | Causa home post-fix · fullpage 1440 · pre-reveal (some sections animate-in waiting on scroll) |
| 14 | `14-home-1440-postfix-revealed-fullpage.jpeg` | Causa home post-fix · fullpage 1440 · WITH reveal blocks forced active · ALL 6 sections visible (hero · narrative · sectors · leadership · cases magazine · cta closer · footer) |
| 15 | `15-studio-1440-fullpage.jpeg` | Studio (about · "Pubblicazioni") page · history strip + 4 values + 3-column team + sede + final CTA · navbar pill = APRI UN PARERE PRELIMINARE |
| 16 | `16-contenzioso-1440-fullpage.jpeg` | Contenzioso list page · 4 case rows (SS.UU. · Cass. III · TAR · App. Milano trib.) + final CTA · text-only · zero placeholder needed |
| 17 | `17-case-ssuu-1440-fullpage.jpeg` | Case-detail SS.UU. 2024 · breadcrumb + h1 + meta-strip + lead + 3 sections + KPI band on bottle-green + team strip + next-case · zero photo · clean render |
| 18 | `18-home-880-fullpage.jpeg` | Tablet 880 fullpage · 8/4 hero stacks · 12 sectors row reflow · cases card grid still visible · placeholder hero proportional |
| 19 | `19-home-375-fullpage.jpeg` | Mobile 375 fullpage · single column · all sections legible · footer 4-col reflows to stack · placeholder hero proportional |
| 20 | `20-cornice-1440-control.jpeg` | Cornice (frozen sibling) anonymous home · viewport 1440 · Bologna golden-hour portico hero intact · Cormorant Garamond + rust accent + filled rust pill "APRI UN FASCICOLO PROGETTO" + KPI 47/18/6 + Lo Studio nav · proves zero regression |

---

## §10 · Priority checks (per the task brief)

| Priority check | Status | Evidence |
|---|---|---|
| 1. Hero must read courtroom/interior-litigation, not library/editorial | ⚠️ HELD | Pre-fix: hero rendered group portrait of casual youths (Pexels 17109985 wrong content per capture 02) — FAIL. Post-fix: hero renders bottle-green placeholder with "imagery hold" label per capture 12 — neutral. A.5b must replace with verified empty-courtroom photo. |
| 2. Founder portrait must read chambers/environmental, not LinkedIn headshot | ⚠️ HELD | Pre-fix: portrait rendered bowl of food (Pexels 8101948 wrong content per capture 07) — FAIL. Post-fix: portrait renders bottle-green placeholder per capture 14 — neutral. A.5b must replace with verified senior Cassazionista in chambers photo. |
| 3. Voice anchor must read evidentiary-forensic, not editorial | ✅ PASS | "Ogni sentenza è un'<em>evidenza</em> incardinata, non un'opinione difesa." — em on `evidenza` · public-record-evidence sense · verbatim recurrence on hero h1 + cta-closer h2 (2/2) · 21 `evidenza` body hits + 21 `massima` + 11 `patrocinio` + 9 `incardinata` confirm forensic-publication register dense. Zero `argomento` (Cornice). Zero `generazioni` (Continua). |
| 4. Inner-page CTA pill must remain Causa-specific on every page | ✅ PASS | "APRI UN PARERE PRELIMINARE" on all 9 pages including 4 case-detail (verified live · §6 above). Zero Cornice `Apri un fascicolo` leak surfaces. |
| 5. Draft preview path must remain legitimate | ✅ PASS | Anonymous: 4/4 draft-gate checks 404. Staff `?preview=1`: 9/9 routes 200. DB `tier='draft'` confirmed. Trust counter `templates_live='24+'` preserved. Catalog listing does not include Causa. |
| 6. If the Pexels CDN issue was sandbox-only, distinguish clearly between real product issue and tooling issue | ✅ DISAMBIGUATED | A.5 reported "sandbox-blocked at this build · in the dev-server context any browser with normal Pexels reachability will load the photos". A.6 directly verified 8 Pexels URLs in the browser sandbox: 8/8 returned content (1 with 404 · 7 with WRONG content). The defect is **NOT** a sandbox CDN issue — it is a **REAL PRODUCT DEFECT** at the curator layer (Pexels IDs are curator-hallucinated · do not match captioned subjects · backup roster also unusable). Reclassified per causa-a6-it-review-lock.md §3 F4. |

**3/6 priority checks PASS.** **2/6 priority checks HELD pending A.5b imagery
re-curate.** **1/6 priority check DISAMBIGUATED (Pexels CDN issue is a real
product issue, not a tooling issue).**

---

## §11 · Distinctness verdict (1-second wordmark-stripped read · CS-TONE-05 · post-fix)

A reader stripping the wordmark from the home page sees: bottle-green
gradient hero placeholder with italic "imagery hold · A.5b re-curate
pending" label · KPI tuple "28 sentenze citate · 14 voci in massimario ·
31 anni di patrocinio" · "Aula di tribunale · interno · 2024" + "Foro di
Milano" credit overlay caption · h1 voice anchor "Ogni sentenza è un'
*evidenza* incardinata, non un'opinione difesa." in GT Sectra · sectors
ribbon listing 12 forensic materie · Lorenzo Marchetti masthead with 4
forensic credentials (placeholder portrait) · 4 magazine-grid cards citing
Cass. SS.UU. + Cass. civ. III + TAR Lombardia + Corte d'Appello Milano sez.
tributaria · "Apri un parere preliminare" CTA · forensic firm whistleblowing
channel · D.lgs. 24/2023 · art. 622 c.p.

**The 30-second read is unmistakably "evidence-led Cassazionista litigation
boutique with imagery hold pending re-curate."** Zero collapse against any
of the 5 live siblings — the placeholder pattern is hex-distinct from
Continua's pine, palette-distinct from Cornice's graphite/rust, layout-
distinct from Pragma/Fiscus/Solaria.

---

## §12 · Verdict

**A.6 review-lock PARTIAL.** Causa IT draft has copy/chrome/typography/
palette/responsive/voice anchor/em-word audit/navbar pill/draft preview
path/frozen sibling regression/test suite all LOCKED. Photographic surfaces
are HELD pending a Phase X.6 Step 5b imagery re-curate workstream.

**Causa IT is NOT YET LOCKED FOR USER VISUAL HANDSHAKE.** The placeholder
imagery makes the page reviewable for everything-except-imagery, but the
visual handshake itself requires real photos for the user to confirm the
litigation-boutique register reads as intended at the photographic axis.

**Workflow C (multilingual) and Workflow D (public flip) remain HELD.**
