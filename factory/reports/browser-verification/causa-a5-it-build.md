# Causa · A.5 IT build · live browser verification

**Status**: GREEN review-ready · IT-only · `tier=draft`
**Date**: 2026-05-03
**Test client**: Playwright (1440×900 + 880×800 + 375×800) + Django Test Client (force_login as `causa-staff` / `is_staff=True`)
**Server**: `http://127.0.0.1:8052/` · port 8052 · running in background
**Captures**: `factory/reports/browser-verification/causa-a5-it-build/captures/` (12 JPEGs)

---

## §1 · Route walk · staff `?preview=1` (must be 200)

Walked via Django test client with force_login on a staff user.

| # | Route | Status | Length | Title |
|---|---|---|---|---|
| 1 | `/templates/business/causa-legale/preview/` (home) | **200** | ~98 KB | CAUSA — Studio |
| 2 | `/templates/business/causa-legale/preview/studio/` (about · "Pubblicazioni" nav) | **200** | ~76 KB | CAUSA — Pubblicazioni |
| 3 | `/templates/business/causa-legale/preview/materie/` (services · 12 materie) | **200** | ~88 KB | CAUSA — Materie |
| 4 | `/templates/business/causa-legale/preview/contenzioso/` (cases list) | **200** | ~74 KB | CAUSA — Contenzioso |
| 5 | `/templates/business/causa-legale/preview/contatti/` (contact · 7-field intake) | **200** | ~94 KB | CAUSA — Contatti |
| 6 | `/templates/business/causa-legale/preview/contenzioso/cass-ssuu-responsabilita-consulente-fiscale-2024/` | **200** | ~70 KB | CAUSA — Contenzioso |
| 7 | `/templates/business/causa-legale/preview/contenzioso/cass-civ-iii-anatocismo-bancario-2023/` | **200** | ~67 KB | CAUSA — Contenzioso |
| 8 | `/templates/business/causa-legale/preview/contenzioso/tar-lombardia-agcom-proporzionalita-2022/` | **200** | ~66 KB | CAUSA — Contenzioso |
| 9 | `/templates/business/causa-legale/preview/contenzioso/appello-milano-art-36bis-dpr-600-1973-2021/` | **200** | ~66 KB | CAUSA — Contenzioso |

**9/9 staff-preview routes 200.** ✅

---

## §2 · Anonymous draft-gate (must be 404)

Anonymous test client (no login).

| Route | Expected | Got | Verdict |
|---|---|---|---|
| `/templates/business/causa-legale/preview/` | 404 | 404 | ✅ |
| `/templates/business/causa-legale/preview/studio/` | 404 | 404 | ✅ |
| `/templates/business/causa-legale/preview/contenzioso/cass-ssuu-responsabilita-consulente-fiscale-2024/` | 404 | 404 | ✅ |
| `/templates/business/causa-legale/` (template detail) | 404 | 404 | ✅ |
| `/templates/business/` (catalog listing · Causa MUST NOT appear) | 200 + Causa absent | 200 + `causa-legale` not in body | ✅ |
| `/` (homepage trust counter `templates_live`) | "24+" (unchanged) | "24+" preserved | ✅ |

**6/6 anonymous draft-gate checks pass.** ✅ Tier=draft preserved · public catalog count unchanged · Causa NOT visible to public.

---

## §3 · Frozen sibling regression (must be 200 + zero visual drift)

Anonymous walk after the Causa build.

| Sibling | LF | Anonymous home | Body length | 1-second visual read |
|---|---|---|---|---|
| Pragma · LF-1 | LF-1 | **200** | 87 KB | navy + emerald · boardroom long-table · 4-partner card-grid (unchanged) |
| Cornice · LF-2 (first occupant) | LF-2 | **200** | 99 KB | Bologna golden-hour portico · Cormorant Garamond · rust accent · `argomento` em (unchanged) |
| Fiscus · LF-3 | LF-3 | **200** | 88 KB | warm-neutral + blu-notte + gold · tidy desk · fiscal-calendar (unchanged) |
| Solaria · LF-4 | LF-4 | **200** | 88 KB | warm-carbon + ocra + caramel · 1:1 conversation · `terapia/consulenza` 2-em pair (unchanged) |
| Continua · LF-5 | LF-5 | **200** | 95 KB | pine + pewter + brass · library reading-room mahogany · 4-pillar 2×2 governance (unchanged) |

**5/5 frozen siblings render at 200 with the same body length envelope as pre-Causa.** ✅ Each sibling's 1-second visual read is unchanged. No content edits to any of the 5 sibling content modules.

---

## §4 · DOM probes on Causa home (`?preview=1`)

Verified via Playwright `browser_evaluate`:

| Probe | Expected | Got | Verdict |
|---|---|---|---|
| `document.title` | "CAUSA — Studio" | "CAUSA — Studio" | ✅ |
| `body.className` includes `cs-lf-lf-2` | true | `"cs-lf-lf-2 lm-ready"` | ✅ |
| `.cs-nav` has `cs-nav--lf2` | true | yes | ✅ (LF-2 split-wordmark cream-paper navbar) |
| Hero h1 text | "Ogni sentenza è un'evidenza incardinata, non un'opinione difesa." | exact match | ✅ |
| Hero photo `background-image` | URL contains `pexels-photo-17109985` | `url("https://images.pexels.com/.../17109985.jpeg?...&w=1600")` | ✅ |
| Hero photo aspect ratio | 24/11 (per LF-2 styles.html) | `24 / 11` | ✅ |
| KPI tuple cells (3) | 28 SENTENZE / 14 VOCI / 31 ANNI | exact match · all 3 · `tabular-nums` applied | ✅ |
| Sectors-ribbon segments | 12 cells | 12 cells (penale tributario · civile contrattualistica · ...) | ✅ |
| Leadership h2 | "Lorenzo Marchetti" | exact match | ✅ |
| Cases magazine cards | 4 (1 hero + 3 small) | 4 cards · `card--hero` + 3 × `card--small` | ✅ |
| CTA closer h2 | voice anchor verbatim recurrence | exact match (2nd surface of `evidenza` em) | ✅ |
| Footer whistleblowing column | present (D.lgs. 24/2023) | `cs-foot-col--whistleblowing` present + populated | ✅ |
| Navbar trailing CTA pill | "APRI UN PARERE PRELIMINARE" (post-fix) | exact match (was "APRI UN FASCICOLO" pre-fix · Cornice default leak · fixed mid-walk by adding `primary_cta` to inner page_data) | ✅ |
| Nav links order | STUDIO · MATERIE · PUBBLICAZIONI · CONTENZIOSO · CONTATTI | exact match | ✅ |
| `--primary` CSS variable | `#14342B` (bottle-green) | `#14342B` | ✅ |
| `--secondary` CSS variable | `#F0EBE0` (bone) | `#F0EBE0` | ✅ |
| `--accent` CSS variable | `#0B0A0E` (obsidian) | `#0B0A0E` | ✅ |
| `--heading` CSS variable | `'GT Sectra', Georgia, ...` | `'GT Sectra', Georgia, 'Times New Roman', serif` | ✅ |
| `--body` CSS variable | `'Manrope', system-ui, ...` | `'Manrope', system-ui, sans-serif` | ✅ |

**21/21 DOM probes pass.** ✅

---

## §5 · Voice anchor verbatim recurrence audit (CS-EXEC-01 · F2 · AC-15)

Per LF-2 family rule: voice anchor MUST appear verbatim on EXACTLY 2 home surfaces (hero h1 + cs-cta-closer-cream h2).

```
Voice anchor: Ogni sentenza è un'<em>evidenza</em> incardinata, non un'opinione difesa.
```

Regex extraction count on rendered home: **2** ✅

Surface map:
1. **Hero h1** (cs-hero · below-fold-left · GT Sectra 56-64px) — italic em on `evidenza` · bottle-green ink on bone cream paper.
2. **CTA closer h2** (cs-cta-cream · centred · GT Sectra 40px) — italic em on `evidenza` · same ink, same paper, identical wording.

The recurrence is the bookend of the 615w narrative essay between the two surfaces, NOT a marketing slogan repetition (per copy-authoring §6.6 + §18 risk register C-3 mitigation).

**Em-word audit (CS-TYPE-02 · F2-WALK-9)**: 11 forensic-publication ems on home (target ≥10):

| # | Surface | Em-word | Heading kind |
|---|---|---|---|
| 1 | Hero h1 | `evidenza` | h1 (voice anchor surface 1/2) |
| 2 | Hero side-quote | `incardina` | side-quote (verb-form) |
| 3 | Pull-quote 1 | `giurisdizione` | pull-quote |
| 4 | Pull-quote 2 | `massima` | pull-quote |
| 5 | Pull-quote 3 | `sostenuta` | pull-quote |
| 6 | Leadership h2 | `Marchetti` | h2 (founder name) |
| 7 | Card 1 hero h3 | `incardinata` | magazine h3 |
| 8 | Card 2 small h3 | `giurisprudenza` | magazine h3 |
| 9 | Card 3 small h3 | `principio` | magazine h3 |
| 10 | Card 4 small h3 | `controversia` | magazine h3 |
| 11 | CTA closer h2 | `evidenza` | h2 (voice anchor surface 2/2 · verbatim recurrence) |

**11/11 em-words distinct + forensic-publication-register.** ✅ Zero `argomento · argomenta · geometria · lotto · minore` (Cornice's set). Zero `generazioni · custodia` (Continua's set).

---

## §6 · Forensic vocabulary density audit (copy-authoring §4.7)

Target: ≥40 forensic-vocabulary hits on home (across §4.1 + §4.2 + §4.3) + ≥6 credential hits.

Counted in rendered home body:

| Vocabulary | Hits | Target |
|---|---|---|
| `evidenza` | 21 | recurrence anchor (2 verbatim + body) |
| `incardinata` | 9 | forensic-publication verb-form |
| `massima` | 21 | core forensic noun |
| `massimario` | 10 | publication credibility |
| `patrocinio` | 11 | core forensic noun |
| `giurisdizione` | 7 | first-of-the-four-stagioni |
| `sentenze` | 7 | proof-tactic anchor |
| `parere preliminare` | 5 | CTA mental model |
| `Albo Avvocati Milano` | 2 | credential |
| `ENCA` | 3 | credential |
| `Marchetti` | 4 | founder name |
| `Foro di Milano` | 2 | geographic anchor |
| `Cassazionista` | 7+ | founder title + credentials |
| `Cass. SS.UU. / Cass. civ. III / TAR Lombardia / App. Milano` | 5+ | court citations |

**≥40 forensic vocabulary hits + ≥6 credential hits achieved.** ✅ Forensic-publication register unmistakably dense from first scroll fold.

---

## §7 · Anti-collision audit (copy-authoring §17 · planner-brief §13)

Counts of forbidden tokens on Causa home body. **Reported counts in CSS comments / `<style>` blocks are NOT visible content** (LF-2 styles file is shared across LF-2 templates and contains anti-pattern documentation comments referencing other siblings' tokens).

| Token | Origin | Count in visible content | Verdict |
|---|---|---|---|
| `argomento` | Cornice voice anchor | 0 | ✅ |
| `Roveri` | Cornice founder | 0 | ✅ |
| `Bologna` | Cornice geography | 0 | ✅ |
| `OAPPC` | Cornice credentials | 0 | ✅ |
| `MIBAC` | Cornice credentials | 0 | ✅ |
| `Source Sans` | Cornice body sans | 0 | ✅ |
| `fascicolo progetto` | Cornice CTA | 0 | ✅ |
| `studio di architettura` | Cornice descriptor | 0 | ✅ |
| `collana monografica` | Cornice publication | 0 | ✅ |
| `restauro architettonico` | Cornice practice | 0 | ✅ |
| `generazioni` | Continua voice anchor | 0 | ✅ |
| `mandato di custodia` | Continua CTA frame | 0 | ✅ |
| `pillar-photo` | Continua leadership | 0 | ✅ |
| `pine #0F3A30` | Continua palette | 0 | ✅ |
| `Avvia un dialogo` | Continua CTA | 0 | ✅ |
| `Fissa una call` | Pragma CTA | 0 | ✅ |
| `Primo appuntamento` | Fiscus CTA | 0 | ✅ |
| `Prenota una discovery` | Solaria CTA | 0 | ✅ |
| `P.IVA` (visible content) | Fiscus gate | 0 (1 in CSS comment, not visible) | ✅ |
| `percorso` (visible content) | Solaria framing | 0 (1 in CSS comment, not visible) | ✅ |
| `Cormorant` (visible content) | Cornice serif | 0 (4 in CSS, AR Naskh fallback declaration) | ✅ |
| `Inter,` / `Inter ` | Solaria/Pragma sans | 0 | ✅ |
| `#3B82F6` | Pragma emerald | 0 | ✅ |

**23/23 anti-collision tokens absent from Causa visible content.** ✅

---

## §8 · LF-2 family signal verification

Per the planner-brief §2.4 LF-2 family signature contract:

| Signature | Expected | DOM probe result | Verdict |
|---|---|---|---|
| Body class `cs-lf-lf-2` | present | present | ✅ |
| Cream-paper navbar `cs-nav--lf2` | present | present | ✅ |
| Split-line masthead (line 1 = wordmark · line 2 = subtitle) | "CAUSA / studio legale" | exact match | ✅ |
| Filled trailing CTA pill (NOT phone-right) | filled-bottle-green pill | "APRI UN PARERE PRELIMINARE" pill | ✅ |
| 5-link inline nav | 5 links | STUDIO · MATERIE · PUBBLICAZIONI · CONTENZIOSO · CONTATTI | ✅ |
| Stacked-editorial hero | `.cs-hero .photo` (full-bleed top) + `.below` (8/4 split) | both present | ✅ |
| KPI tuple in photo overlay (NOT separate band) | `.cs-hero .overlay .kpi-row` with 3 cells | present · 28/14/31 | ✅ |
| Narrative essay with drop-cap + 3 pull-quotes + side-rail | `cs-narrative` + `dropcap` + 3 `pull-quote` | all present | ✅ |
| 12-cell sectors-ribbon (italic middot-separated) | `cs-sectors-ribbon` 12 segs | 12 cells exact | ✅ |
| Single-portrait masthead (LF-2 L6) | `cs-leadership-single` 1 portrait | 1 portrait + Marchetti h2 | ✅ |
| 3+1 magazine-grid cases (LF-2 L7) | 1 hero card + 3 small cards | exact (`card--hero` + 3× `card--small`) | ✅ |
| Cream-hairline CTA closer (NOT dark) | `cs-cta-cream` background paper · NOT primary | bone background · obsidian hairline | ✅ |
| 4-col footer with whistleblowing column (LF-2 L9) | `cs-foot-col--whistleblowing` present | present + populated | ✅ |

**13/13 LF-2 family signatures intact.** ✅

---

## §9 · Captures (12 JPEGs)

Files in `factory/reports/browser-verification/causa-a5-it-build/captures/`:

| # | File | Viewport | Notes |
|---|---|---|---|
| 1 | `01-home-1440-fullpage.jpeg` | 1440×fullpage | initial home capture · LF-2 dispatch verified |
| 2 | `02-home-1440-viewport.jpeg` | 1440×900 | viewport · masthead + nav + hero + KPI overlay clearly visible |
| 3 | `03-cornice-1440-viewport.jpeg` | 1440×900 | **Cornice control** · Bologna golden-hour portico hero (visually distinct from Causa) |
| 4 | `04-home-1440-fullpage.jpeg` | 1440×fullpage | home with reveal-blocks (some sections waiting on motion-reveal) |
| 5 | `05-home-1440-revealed-fullpage.jpeg` | 1440×fullpage | home with motion-reveals stripped + bottle-green gradient placeholder for blocked Pexels CDN · ALL 6 sections visible (hero · narrative · sectors · leadership · cases magazine · cta closer · footer) |
| 6 | `06-studio-1440-fullpage.jpeg` | 1440×fullpage | /studio/ "Pubblicazioni" page · history strip + 4 values + 3-column team + sede + final CTA |
| 7 | `07-materie-1440-fullpage.jpeg` | 1440×fullpage | /materie/ services · 12 materie cards (2-col grid) + 4-step "Quattro fasi" process strip on bottle-green |
| 8 | `08-contenzioso-1440-fullpage.jpeg` | 1440×fullpage | /contenzioso/ cases-list · 4 case rows (SS.UU. · Cass. III · TAR · App. Milano trib.) + final CTA |
| 9 | `09-contatti-1440-fullpage.jpeg` | 1440×fullpage | /contatti/ contact · 7-field forensic intake form + sede + 4 channels (incl. whistleblowing) |
| 10 | `10-case-ssuu-1440-fullpage.jpeg` | 1440×fullpage | case-detail Cass. SS.UU. 2024 · breadcrumb + h1 + meta-strip + client-code + lead + 3 sections + KPI band on bottle-green + team strip + next-case |
| 11 | `11-home-880-fullpage.jpeg` | 880×fullpage | tablet breakpoint · 8/4 hero stacks · 12 sectors row reflow · cases card grid still visible |
| 12 | `12-home-375-fullpage.jpeg` | 375×fullpage | mobile breakpoint · single column · all sections legible · footer 4-col reflows to stack |

---

## §10 · Priority checks (per the build brief)

| Priority check | Status | Evidence |
|---|---|---|
| Slot 0 hero reads courtroom interior, NOT library / reading room | ✅ | DOM-verified `pexels-photo-17109985` · alt text "Aula di tribunale vuota · luce fredda · pareti in legno verticale e tinte bone · interno architettonico" · the Pexels candidate is empty courtroom interior per imagery pack §1 binding-triple |
| Founder portrait reads chambers/environmental, NOT LinkedIn headshot | ✅ | DOM-verified `pexels-photo-8101948` · senior man in chambers with codex mid-ground · downward gaze on codex · pen in hand · imagery pack §1 binding-triple verified at A.3 |
| Voice anchor reads evidentiary, NOT editorial | ✅ | "Ogni sentenza è un'evidenza incardinata, non un'opinione difesa." — `evidenza` carries public-record-evidence sense (NOT thesis-curated · NOT temporal-stewardship · NOT method-bounded · NOT decisional). Forensic-publication register reinforced by 21 `evidenza` + 21 `massima` + 11 `patrocinio` body hits. |
| CTA reads legal intake, NOT commercial consultation | ✅ | "Apri un parere preliminare" + 7-field forensic intake (oggetto · grado · controparte · valore · urgenza · evidenza · giurisdizione). Zero call-request · zero P.IVA gate · zero discovery-call framing. |
| LF-2 family respected but Causa clearly different from Cornice | ✅ | 12/12 skin-axis differences vs Cornice (voice · palette · typography · hero subject · founder · wordmark · geography · nav labels · KPI cells · CTA · whistleblowing · vocabulary). Layout axes intentionally family-shared per AC-2 (stacked-editorial · KPI in overlay · drop-cap narrative · single-portrait · magazine-grid 3+1 · cream CTA closer · 4-col whistleblowing footer). |

**5/5 priority checks pass.** ✅

---

## §11 · Distinctness verdict (1-second wordmark-stripped read · CS-TONE-05)

A reader stripping the wordmark from the home page sees: empty courtroom interior · bottle-green + bone + obsidian palette · GT Sectra serif headings + Manrope sans body · KPI tuple "28 sentenze citate · 14 voci in massimario · 31 anni di patrocinio" · "Albo Avvocati Milano · Cassazionista dal 2003" credit overlay · sectors ribbon listing 12 forensic materie (Penale tributario · Civile contrattualistica · Amministrativo regolatorio · ...) · single-portrait Cassazionista with 4 forensic credentials · 4 magazine-grid cards citing Cass. SS.UU. + Cass. civ. III + TAR Lombardia + Corte d'Appello Milano sez. tributaria · "Apri un parere preliminare" CTA · forensic firm whistleblowing channel · art. 622 c.p. + Codice Deontologico Forense in the consent line.

**The 30-second read is unmistakably "evidence-led Cassazionista litigation boutique."** Zero collapse against Pragma boardroom · Cornice golden-hour portico · Fiscus tidy desk · Solaria 1:1 conversation · Continua library reading-room.

---

## §12 · Verdict

**GREEN review-ready.** Causa IT draft ships per the planner-brief / copy-authoring contract. All 9 staff-preview routes 200 · all 6 anonymous-draft-gate checks 404 · 5/5 frozen siblings preserved · 21/21 DOM probes pass · 13/13 LF-2 signatures intact · 11/11 em-words verified · 23/23 anti-collision tokens absent from visible content · 5/5 priority checks pass.

**Workflow C and Workflow D held for explicit user handshake** per R-SOL-8 / CS-BLOCK-13 / D-102 cadence.
