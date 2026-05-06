# Causa · Workflow C multilingual rollout · IT + EN/FR/ES/AR

```yaml
report_type:        workflow-c-multilingual · 5-locale draft-reviewable
                    rollout on top of IT review-locked + slice-01 +
                    slice-02 + motion-profile-pass-1
template_slug:      causa-legale
archetype:          corporate-suite
sub_cluster:        studio-legale-cassazionista · evidence-led litigation boutique
layout_family:      LF-2 · Editorial Spread (2nd occupant after Cornice)
phase:              X.6 · Causa · workflow C multilingual
                    (post-A.6 review-lock · post-A.5b imagery re-curate ·
                    post-X.7d slice-01 · post-X.7d slice-02 · post-X.7b
                    motion-profile DNA pass 1)
date:               2026-05-06
agent:              workflow-c-multilingual-rollout (orchestrator-side
                    authoring · single-pass slice on top of the locked
                    IT draft)
trigger:            user authorisation to ship Causa from IT-only draft
                    to 5-locale draft-reviewable state, preserving the
                    anti-clone gains, the LF-2 second-occupant identity,
                    and the newly implemented motion_profile DNA
                    behaviour.
inputs_consumed:
  - factory/reports/causa/causa-planner-brief.md (binding · §11 voice
    anchor + §13 ban list)
  - factory/reports/causa/causa-a5-it-build.md
  - factory/reports/causa/causa-a6-it-review-lock.md
  - factory/reports/causa/causa-a5b-imagery-recurate.md
  - factory/reports/causa/causa-distinctness-proof.md
  - factory/reports/copy/causa-legale/voice-anchor-lock.md (§4.2
    cognate set · §5 ban list · §6 verbatim-in-translation contract)
  - factory/reports/copy/causa-legale/copy-authoring.md
  - factory/reports/copy/causa-legale/content-volume-check.md
  - factory/reports/hardening/anti-clone-2.0-rules.md (§3 within-
    family threshold · §4 critical-axis vetoes)
  - factory/reports/hardening/lf2-family-internal-variance-rules.md
    (§4 AC-V1 sub-variant adoption floor · §5 verbatim-in-translation
    propagation contract)
  - factory/reports/hardening/causa-retrofit-slice-01.md (R1 CTA + R4
    NAV-1 + R6 EVID-5)
  - factory/reports/hardening/causa-retrofit-slice-02.md (R2 EVID-3
    + R3 TIME-3)
  - factory/reports/hardening/motion-profile-implementation-pass1.md
    (g2-editorial-counter profile + 7-flag bundle)
  - factory/reports/hardening/motion-profile-dna-plan.md (paper
    contract)
  - factory/standards/corporate-suite-imagery-standard.md
  - design-orchestrator/references/internal-baselines/cornice-lf2-reference-pack.md
    (Pass C precedent · Naskh AR h1 swap chrome rule)
  - design-orchestrator/references/internal-baselines/corporate-suite-distinctness-matrix.md
  - apps/catalog/template_content_cornice_{en,fr,es,ar}.py (workflow-C
    shape precedent · same-keys / same-nesting / same-list-shapes
    contract)
  - apps/catalog/template_content_continua_{en,fr,es,ar}.py (LF-5 5-
    locale precedent · zero Naskh swap as control for LF-2 scoping)
status_tag:         WORKFLOW-C-MULTILINGUAL-GREEN-REVIEW-READY
verdict:            5-locale draft-reviewable. All 25 staff routes 200
                    (5 pages × 5 locales) + 20 case-detail routes 200
                    (4 posts × 5 locales) = **45/45 staff routes 200**.
                    Anonymous draft-gate intact (5/5 anon 404 on Causa
                    home + Causa absent from public catalog). 5/5
                    frozen siblings byte-equivalent on body data-attrs
                    + motion profile + voice-anchor cognate isolation.
                    546/546 Django tests OK · zero new failures · zero
                    regressions.
next_action:        Workflow D public flip remains explicitly HELD
                    pending user-handshake on the multilingual walk
                    (R-SOL-8 / CS-BLOCK-13). On user authorisation,
                    workflow D delivers a 7-line cascade per the
                    Cornice public-flip precedent (1 registry edit ·
                    `sync_template_tiers` · 7 explicit-literal test
                    bumps in `apps/catalog/tests.py` 24 → 25 / "24+"
                    → "25+").
```

This file is the binding workflow C narrative for Causa. It pairs with:
- `factory/reports/browser-verification/causa-workflowC-multilingual.md` —
  live walk evidence + anti-collision audit + Naskh-scoping verification +
  frozen-sibling regression.
- `factory/reports/scorecard/causa-workflowC-multilingual/summary.md` —
  scorecard panel mirroring the slice-01 / slice-02 format.

---

## §1 · Why this phase exists (the workflow C contract)

A.6 IT review-lock (`causa-a6-it-review-lock.md`) closed the IT draft as
**review-locked for COPY/CHROME/TYPOGRAPHY/PALETTE** but held imagery
pending A.5b re-curate. A.5b (`causa-a5b-imagery-recurate.md`) replaced
all 10 photo URL constants with verified Pexels URLs (St George's
Hall hero · senior-man-with-codex founder · Corte di Cassazione
facade lead card). Slice-01 (`causa-retrofit-slice-01.md`) cleared all
5 anti-clone-2.0 critical-axis vetoes (CTA · motion · imagery · voice
anchor · hero subject). Slice-02 (`causa-retrofit-slice-02.md`) raised
the Cornice ↔ Causa pair to **29/54** (or 30/54 with axis-18 promote)
and pushed AC-V1 sub-variant adoption to **5/9** (2× the ≥3 floor).
Motion-profile DNA pass 1 (`motion-profile-implementation-pass1.md`)
wired the 8th DNA axis as code-verifiable (g2-editorial-counter
profile · 5 flags firing on Causa) and added 2 paper-then-code gates
(card_lift_restrained + cinematic_fade) for future cluster intakes.

At that point the IT draft was anti-clone 2.0 COMPLIANT vs Cornice
**with margin**, the imagery was real, the chrome was hardened, and
the motion-profile axis was code-verifiable. Workflow C is the next
gate: take the locked IT draft to **5-locale draft-reviewable** state
on top of all of the above, preserving every gain.

The user brief for this phase enumerated seven strict do-NOTs:
1. NOT public-flip Causa.
2. NOT redesign the layout.
3. NOT widen into sibling 7.
4. NOT touch apps/editor / apps/projects / apps/commerce.
5. NOT regress Cornice or the frozen live siblings.
6. NOT silently flatten Causa into generic advisory tone.
7. NOT weaken the litigation/evidence-led register · NOT alter
   motion_profile semantics except where locale/RTL requires safe
   adaptation.

This file's contract is to evidence that all seven were respected.

---

## §2 · What workflow C ships

### §2.1 · Source-file delta

Six source files added or modified · zero deletions:

| file | nature | net lines |
|---|---|---|
| `apps/catalog/template_content_causa_en.py` | new locale tree (English · forensic-publication legal-press register) | +1147 |
| `apps/catalog/template_content_causa_fr.py` | new locale tree (French · Cassation / Dalloz / Gazette du Palais register) | +1238 |
| `apps/catalog/template_content_causa_es.py` | new locale tree (Spanish · La Ley / Aranzadi / Sala Civil TS register) | +1244 |
| `apps/catalog/template_content_causa_ar.py` | new locale tree (Arabic MSA · MENA legal-press register · LF-2-scoped Naskh h1 swap inherited from Cornice's Pass C chrome) | +1456 |
| `apps/catalog/template_content.py` | 4 new imports + locale dispatch map flipped from `{"it": ...}` to all 5 locales | +14 / −3 |
| `TEMPLATE_REGISTRY.json` | locale list `["it"]` → `["it","en","fr","es","ar"]` + tier_reason narrative extended | +5 / −1 |

**Zero edits** to: `apps/editor/` · `apps/projects/` · `apps/commerce/` ·
`apps/catalog/template_content_causa.py` (the IT module · sole source
of truth for shared Pexels URL constants imported by all 4 locales) ·
`apps/catalog/template_content_pragma.py / _cornice.py / _fiscus.py /
_solaria.py / _continua.py` (frozen-sibling content modules) · LF-1 /
LF-3 / LF-4 / LF-5 layout files · LF-2 layout files (`_layouts/lf2/
content.html` + `_layouts/lf2/styles.html`) · corporate-suite chrome
(`_base.html`) · `static/js/live-motion.js` · `static/css/live-motion.css` ·
`apps/catalog/views.py` · `apps/catalog/template_dna.py` ·
`apps/catalog/preview_imagery.py` · `apps/catalog/migrations/*` · any
non-Causa locale tree (Cornice / Continua / Solaria EN/FR/ES/AR
unchanged byte-by-byte).

### §2.2 · Tier · public catalog · DB row

`tier=draft` preserved through the full workflow. Public catalog count
unchanged at **24 published_live / 1 draft** (Causa). Anonymous home
of `causa-legale` returns 404; staff session with `?preview=1` returns
200 across all 5 locales × 5 pages + 4 posts. Public catalog listing
`/templates/business/` does NOT include `causa-legale` (verified).

### §2.3 · Locale switcher honesty (D-068)

`get_available_locales("causa-legale")` now returns
`["it", "en", "fr", "es", "ar"]` (was `["it"]` only). The locale
switcher in the corporate-suite chrome correctly exposes 4 alternate
locale pills on every Causa page (the current locale shows as active;
the 4 others as switchable). No silent fallback to IT for any locale
— every locale serves its own authored tree.

---

## §3 · Voice anchor preservation across 5 locales (verbatim-in-translation)

The load-bearing contract from `voice-anchor-lock.md §6` and
`planner-brief.md §11` binds every locale to the public-record-
evidence cognate set. Italic em moves with the noun root in every
locale; the 2-surface verbatim recurrence on home (hero h1 + cs-cta-
closer-cream h2) holds.

### §3.1 · The 5-locale cognate set (locked at workflow C)

| Locale | Anchor sentence (verbatim · em on the public-record-evidence noun) |
|---|---|
| **IT** | `Ogni sentenza è un'<em>evidenza</em> incardinata, non un'opinione difesa.` |
| **EN** | `Every ruling is <em>evidence</em> on the record — not an opinion defended.` |
| **FR** | `Chaque décision est une <em>preuve</em> versée au dossier — non une opinion défendue.` |
| **ES** | `Cada sentencia es una <em>evidencia</em> incardinada — no una opinión defendida.` |
| **AR** | `كلُّ حكمٍ <em>دليلٌ</em> مُثبَتٌ في السجل، لا رأيٌ يُدافَع عنه.` |

Each translation:
- Preserves the em-word on the noun root in the public-record-evidence
  sense (NOT proof-as-statistics · NOT testimony · NOT clue · NOT
  circumstantial-proof).
- Preserves the rhetorical contrast structure (`X is Y, not Z`).
- Preserves the verbatim-on-2-surfaces recurrence (the same translated
  sentence lands on hero h1 AND cs-cta-closer-cream h2).
- Reads as a method-statement in the locale's forensic-press register,
  not as a marketing-slogan.

### §3.2 · Side-quote verb-em (verb-form derived from the noun anchor)

Per `voice-anchor-lock §6.4`: the side-quote em-word is a verb-form
derived from the public-record-evidence anchor. The translator picks
per-locale within the verb-family bound to the noun anchor:

| Locale | Side-quote verb-em | Idiom |
|---|---|---|
| **IT** | `<em>incardina</em>` | `incardinare nel fascicolo processuale` (forensic-publication register) |
| **EN** | `<em>enters</em>` | `enters on the record` (UK barristers'-chambers idiom) |
| **FR** | `<em>verse</em>` | `verse au dossier` (canonical Cassation idiom) |
| **ES** | `<em>incardina</em>` | `incardinar en el expediente procesal` (Spanish forensic-press uses the same Latinate root) |
| **AR** | `<em>يُثبِت</em>` | `يُثبِت في ملفّ الدعوى` (MENA legal-press canonical verb derived from `دليل / إثبات`) |

In all 5 locales the anchor noun and the side-quote verb form a
**single rhetorical motif** ("the firm argues only what it places on
the record") — the verb echoes the noun's root and the visitor reads
the two surfaces as a single forensic-publication argument.

### §3.3 · Resonance on `incardinare` (motif of three em-surfaces)

Per `voice-anchor-lock §7.3`, the IT home carries a deliberate
forensic-publication motif: three em-words on `incardinare`/`incardina`/
`incardinata` across hero h1 + side-quote + magazine card 1's h3.
This triple resonance translates to each locale within the same root
family:

| Locale | Hero h1 (anchor noun) | Side-quote (verb-em) | Card 1 h3 (em payoff) |
|---|---|---|---|
| IT | `evidenza` (incardinata) | `incardina` | `incardinata` |
| EN | `evidence` (on the record) | `enters` | `grounded` |
| FR | `preuve` (versée au dossier) | `verse` | `versée` |
| ES | `evidencia` (incardinada) | `incardina` | `incardinada` |
| AR | `دليل` (مُثبَت في السجل) | `يُثبِت` | `مُثبَت` |

The motif holds in IT/ES/AR with **identical root** across all three
surfaces (incardina · incardina · يُثبِت/مُثبَت), and in EN/FR with
the same **semantic family** (record / dossier) carrying the
forensic-publication echo. CS-TYPE-02 single-em-per-heading rule is
respected in every locale (each surface has exactly one em).

### §3.4 · Anti-collision · Cornice-cognate ban (verified live)

The translator-binding contract per `voice-anchor-lock §5.5 +
planner-brief §13` rules out any rendering that would collapse Causa
onto Cornice's curatorial-thesis cognate set. Live walk verifies:

| Locale | Cornice cognate (BANNED) | Causa rendered body contains it? |
|---|---|---|
| IT | `<em>argomento</em>` | **False** ✓ |
| EN | `<em>argument</em>` | **False** ✓ |
| FR | `<em>argument</em>` | **False** ✓ |
| ES | `<em>argumento</em>` | **False** ✓ |
| AR | `<em>حُجَّة</em>` | **False** ✓ |

5/5 locales · zero Cornice-cognate leakage. Cornice's voice anchor
remains uniquely Cornice's; Causa's voice anchor remains uniquely
Causa's. A reader landing on Causa in any of 5 locales reads a
forensic-publication firm; a reader landing on Cornice reads an
architectural-press studio. The two firms are **categorically
disjoint at the anchor noun** in every locale.

### §3.5 · Evidence-led register preserved (NOT generic advisory tone)

The user brief explicitly forbade "silently flattening Causa into
generic advisory tone" or "weakening the litigation/evidence-led
register". Workflow C honours this in three layers:

1. **Vocabulary density**: Each locale ships ≥40 forensic-publication
   hits on the home (rulings · case-law · evidence on the record ·
   pleadings · briefs · Cassation · jurisdiction · case-law · etc.).
   The vocabulary survey:

   | Locale | Forensic vocabulary density (home body · indicative count) |
   |---|---|
   | IT | `evidenza` 21 · `massima` 21 · `patrocinio` 11 · `incardinata` 9 · `Cassazionista` 7+ |
   | EN | `evidence` 24+ · `ruling` 22+ · `cassation/Cassation` 12+ · `internal repertory` 10+ · `Cassazionista` 7 (Italian preserved) |
   | FR | `preuve` 22+ · `décision` 24+ · `Cassation` 12+ · `répertoire interne` 10+ · `Cassazionista` 7 (Italian preserved) |
   | ES | `evidencia` 22+ · `sentencia` 24+ · `Casación` 12+ · `repertorio interno` 10+ · `Cassazionista` 7 (Italian preserved) |
   | AR | `دليل` 18+ · `حكم` 22+ · `قاعدة` 10+ · `النقض` 12+ · `Cassazionista` 7 (Latin preserved) |

2. **Italian normative references preserved verbatim** in all 4
   non-IT locales: D.lgs. 24/2023 · D.lgs. 196/2003 · D.M. 55/2014 ·
   Codice Deontologico Forense · art. 622 c.p. · D.lgs. 28/2010 ·
   D.lgs. 74/2000 · D.lgs. 259/2003 · ENCA · CTU forense · Tribunale
   di Milano · Cassazione · TAR Lombardia · Corte d'Appello di Milano
   · Foro di Milano · Foro Italiano · Giurisprudenza Italiana · Albo
   Avvocati · Reg. UE 679/2016 / GDPR · Albo CTU forense Tribunale di
   Milano. Italian addresses (Via Borgonuovo 14 · 20121 Milano) and
   phone formats (`+39 02 7634 8210`) and Euro figures (`€ 50.000` ·
   `€ 5 M`) and Latin year numerals preserved. The legal credentials
   on the founder ("Cassazionista since 2003 · ENCA mediators · Albo
   CTU forense") read in every locale as a real Italian Cassationist
   firm — not as a generic legal practice in the locale's country.

3. **Sentence-identifier verbatim**: The 4 case-detail posts and the
   4 magazine-grid card EVID-3 citations preserve the Italian
   sentence-identifiers verbatim across all 5 locales: `Cass. SS.UU.
   n. 11237/2024` · `Cass. civ. sez. III n. 28914/2023` · `TAR
   Lombardia sez. III n. 814/2022` · `Corte d'Appello Milano sez.
   trib. n. 3187/2021`. Only the surrounding language (article-the-
   article, prepositions, paraphrase of the legal principle) is
   localised; the sentence identifiers themselves are identical across
   all 5 locales (verified live).

The result: a reader landing on Causa EN at the hero reads "Every
ruling is evidence on the record — not an opinion defended" with a
firm whose founder is a Cassazionista in Milan since 2003, whose lead
case is a Cass. SS.UU. ruling of April 2024, whose CTA reads "Submit
a preliminary opinion" in English-flavoured forensic English. The
same applies to FR / ES / AR with native-flavoured equivalents. **No
locale flattens Causa into "law firm" or "legal services"** — every
locale ships a litigation-evidence-led Cassationist boutique.

---

## §4 · LF-2 second-occupant identity preserved

### §4.1 · Cornice-vs-Causa anti-collapse separation across all 5 locales

Per the anti-clone 2.0 within-family threshold (≥27/54) and the
critical-axis vetoes, Cornice ↔ Causa pair must read as
**categorically different** at first scroll in every locale. Workflow
C verifies this on rendered home in every locale:

| Axis | Cornice (live) | Causa (5 locales) | Verdict |
|---|---|---|---|
| 12 voice anchor noun | `argomento / argument / argumento / حُجَّة` | `evidenza / evidence / preuve / evidencia / دليل` | **DISJOINT in 5 locales** ✓ |
| 13 CTA mental model | `Apri un fascicolo / Open a project dossier / Ouvrez un dossier / Abra un expediente / افتح كرّاس مشروع` | `Sottometti / Submit / Soumettez / Someta / قَدِّم` (verb-class explicitly disjoint per AC-V3) | **DISJOINT in 5 locales** ✓ |
| 2 hero subject | Bologna golden-hour portico exterior (architectural-press) | empty courtroom interior (litigation chamber) | **DISJOINT** (imagery URL constants explicitly different · neither URL appears in the other sibling) |
| 18 motion + page choreography | g2-editorial profile · 0 motion patterns firing · static throughout | g2-editorial-counter profile · **5 motion patterns firing** (KPI-2 + NAV-1 + EVID-5 + EVID-3 + TIME-3) | **DISJOINT at first scroll** ✓ |
| 17 imagery register | golden-hour-warm-stone (architectural press) · static credit-line | cool-courtroom-bone (litigation chamber) · EVID-5 hover-revealed provenance tooltip | **DISJOINT** ✓ |
| 7 KPI placement | static text tuple inside hero credit overlay | KPI-2 count-up animation on viewport entry | **DISJOINT** ✓ |
| 9 cases-preview | static magazine-grid · cards link out to detail | EVID-3 inline `<details>` citation-pop on each of 4 cards · forensic-publication-register massima snippets | **DISJOINT** ✓ |
| 10 navbar | static cream-paper nav · 84px throughout | NAV-1 sticky-condensed: 84px → 64px after 240px scroll · `is-shrunk` body class | **DISJOINT** ✓ |

8 of 18 axes are **categorically disjoint** in every locale. The
remaining 10 are family-shared (LF-2 inheritance) and thus
intentionally adjacent — they form the LF-2 family signature. Per
anti-clone 2.0 §3 the within-family threshold is ≥27/54: post-slice-
02 the pair scores **29/54** (or 30/54 with axis-18 promote on the
"5 patterns vs 0 = structurally separate" reading), which workflow C
preserves.

### §4.2 · AC-V1 sub-variant adoption preserved across locales

Per `lf2-family-internal-variance-rules.md §4 AC-V1`: a 2nd LF-2
occupant MUST adopt at least 3 within-cell sub-variant patterns
Cornice doesn't ship. Causa post-slice-02 ships 5 of 9 sub-variants
(KPI-2 + NAV-1 + EVID-5 + EVID-3 + TIME-3 · 2× the ≥3 floor).

Workflow C propagates the locale-parity contract: **all 5 sub-variants
fire on every Causa locale**. Verified live via body data-attributes:

| Locale | data-motion-profile | data-motion-kpi-animate | data-motion-nav-condense | data-motion-evid5 | data-motion-evid3 | data-motion-time3 |
|---|---|---|---|---|---|---|
| it | `g2-editorial-counter` | 1 | 1 | 1 | 1 | 1 |
| en | `g2-editorial-counter` | 1 | 1 | 1 | 1 | 1 |
| fr | `g2-editorial-counter` | 1 | 1 | 1 | 1 | 1 |
| es | `g2-editorial-counter` | 1 | 1 | 1 | 1 | 1 |
| ar | `g2-editorial-counter` | 1 | 1 | 1 | 1 | 1 |

5/5 locales identical motion-profile bundle. AC-V1 ≥3 floor cleared
in every locale with **2× margin**.

### §4.3 · The slice-01 / slice-02 retrofit copy translates verbatim

The retrofit copy surfaces (CTA verb · NAV-1 sticky-condensed · EVID-5
provenance tooltip · EVID-3 case-citation labels · TIME-3 chronotick
year-labels) propagate across all 5 locales. Live verification:

**EVID-3 case-citation-pop** (4 cards × 5 locales = 20 panels):

| Locale | Citation-toggle label | Card 1 em-target (forensic principle) |
|---|---|---|
| IT | `Vedi la massima n. 14` | `responsabilità` |
| EN | `View ruling no. 14` | `liability` |
| FR | `Voir la décision n° 14` | `responsabilité` |
| ES | `Ver la voz n.º 14` | `responsabilidad` |
| AR | `اقرأ القاعدة رقم 14` | `المسؤوليّة` |

20/20 EVID-3 panels render in every locale with locale-flavoured
forensic-press register on the body and the same Italian sentence-
identifier verbatim (Cass. SS.UU. n. 11237/2024 etc.).

**TIME-3 chronotick** (6 ticks × 5 locales = 30 milestone-cells):

| Year (Latin numeric · same in all locales) | IT | EN | FR | ES | AR |
|---|---|---|---|---|---|
| 1995 | Fondazione · Milano | Founding · Milan | Fondation · Milan | Fundación · Milán | التأسيس · Milano |
| 2003 | Abilitazione Cassazionista | Cassazionista qualification | Habilitation Cassazionista | Habilitación Cassazionista | تأهيل أمام محكمة النقض |
| 2008 | Prima massima in massimario | First ruling in the internal repertory | Première décision au répertoire interne | Primera voz en el repertorio interno | أوّل قاعدة في السجل الداخلي |
| 2014 | Prima rimessione SS.UU. | First SS.UU. referral | Première saisine SS.UU. | Primera remisión SS.UU. | أوّل إحالة إلى الدوائر المتّحدة |
| 2018 | Iscrizione Albo CTU forense | Albo CTU forense registration | Inscription Albo CTU forense | Inscripción Albo CTU forense | تسجيل خبير قضائي · Albo CTU forense |
| 2024 | Quattordicesima massima · SS.UU. | Fourteenth entry · SS.UU. | Quatorzième entrée · SS.UU. | Decimocuarta voz · SS.UU. | القاعدة الرابعة عشر · الدوائر المتّحدة |

30/30 chronotick milestone-cells render in every locale with Latin
numerics preserved + locale-flavoured labels. The 6-tick rail draws
the studio's chronology in the same forensic-publication register
across all 5 locales.

**EVID-5 provenance-tooltip**: the slug + Latin Pexels-ID + St.
George's Hall reference are preserved verbatim across all 5 locales;
only the introductory text translates ("photograph provenance" /
"Provenance de la photographie" / "Procedencia de la fotografía" /
"مصدر الصورة"). 5/5 locales render the EVID-5 reveal correctly.

**NAV-1 sticky-condensed**: behaviour is locale-agnostic (CSS-only
gate on body data-attribute). Verified live: 5/5 locales emit the
`data-motion-nav-condense="1"` body attribute and trigger the 84 →
64px shrink on scroll past 240px.

**KPI-2 count-up**: Latin numerals (`28 · 14 · 31`) preserved in all
5 locales; the labels translate ("Sentenze citate" / "Rulings cited"
/ "Décisions citées" / "Sentencias citadas" / "أحكام مُستشهَدٌ بها").
KPI-2 fires on viewport entry across 5 locales.

---

## §5 · AR RTL · Naskh h1 swap correctly scoped at LF-2

### §5.1 · The Naskh-vs-Kufi scoping contract (inherited from Cornice)

Per `cornice-lf2-reference-pack.md §AC-13`, the LF-2 editorial-
publication register favours Noto Naskh Arabic humanist forms over
the cluster-default Noto Kufi Arabic display register. The chrome
selector that scopes this swap is:

```css
html[dir="rtl"] body.cs-lf-lf-2 {
  --heading: 'Noto Naskh Arabic', '{{ theme.heading_font }}', Georgia, serif;
}
```

The selector sits in the corporate-suite `_base.html` chrome (line
~818) and was introduced verbatim by Cornice at Pass C. Workflow C for
Causa **inherits this selector verbatim** — the AR locale tree does
NOT modify the chrome rule. Live verification:

| Template | Layout family | AR body class | AR heading font (computed) |
|---|---|---|---|
| Pragma AR | LF-1 | `cs-lf-lf-1` | Noto Kufi Arabic (cluster default) |
| **Cornice AR** | **LF-2** | `cs-lf-lf-2` | **Noto Naskh Arabic** (Pass C scope) |
| Fiscus AR | LF-3 | `cs-lf-lf-3` | Noto Kufi Arabic (cluster default) |
| Solaria AR | LF-4 | `cs-lf-lf-4` | Noto Kufi Arabic (cluster default) |
| Continua AR | LF-5 | `cs-lf-lf-5` | Noto Kufi Arabic (cluster default) |
| **Causa AR** | **LF-2** | `cs-lf-lf-2` | **Noto Naskh Arabic** (Cornice precedent inherited) |

**Naskh swap fires on LF-2 only.** Causa AR (LF-2) gets Naskh; the
4 non-LF-2 frozen siblings (Pragma · Fiscus · Solaria · Continua) AR
locales remain on Noto Kufi (cluster default). Cornice AR (LF-2)
keeps its Pass-C Naskh swap. **Zero Naskh-or-Kufi leakage across LF
boundaries** (verified live).

### §5.2 · Voice anchor in Naskh register (forensic-publication match)

The AR voice anchor `كلُّ حكمٍ <em>دليلٌ</em> مُثبَتٌ في السجل، لا رأيٌ يُدافَع عنه.`
renders in Noto Naskh Arabic on hero h1 + cs-cta-closer-cream h2 — the
forensic-publication serif register that matches the editorial-
publication register Cornice established and Causa inherits. Body
copy continues in Amiri / Noto Naskh as appropriate to the cluster
(LF-2 family). The Latin wordmark `CAUSA / studio legale` is
preserved on the navbar masthead per CS-NAV-06; Latin numerals are
preserved on KPI tuple (`28 · 14 · 31`) and chronotick milestones
(`1995/2003/2008/2014/2018/2024`) and Pexels IDs (`33939830`) per
CS-FOOT-03 / planner-brief §11.

### §5.3 · RTL rendering (logical-property layer)

The corporate-suite chrome already supports `dir="rtl"` via the
`_base.html` logical-property layer (the same layer Cornice / Continua
/ Solaria use). The Causa AR locale tree relies on this layer
verbatim — no new RTL chrome rules introduced. Live verification:

- `<html lang="ar" dir="rtl">` correctly emitted on every AR page.
- The hero photo's KPI tuple credit-overlay reads right-to-left (the
  3-stat order shifts visually but reads logically as `28 · 14 · 31`
  in Latin numerals — preserved per CS-FOOT-03).
- The narrative essay's drop-cap renders correctly under RTL (the
  drop-cap glyph is Arabic `ا` instead of Latin `L` — ligated into
  the body copy per AR convention).
- The 12-cell sectors-ribbon reads right-to-left with Arabic typography.
- The 4-magazine-card grid reverses visually (card 1 lands on the
  right, cards 2-3-4 on the left/below) — same shape Cornice AR uses.
- The CTA pill (`قَدِّم رأياً تمهيدياً`) on the navbar trailing slot
  is right-aligned per RTL convention.

### §5.4 · AR-specific anti-collision (per voice-anchor-lock §5.5)

Per the AR ban list, Causa's `دليل` cognate must NOT collapse onto:

| Banned AR cognate | Reason | Causa AR contains it as em-target? |
|---|---|---|
| `حُجَّة` | Cornice's curatorial-thesis cognate (AC-3 ban) | **No** ✓ |
| `شهادة` | testimony register; not public-record-evidence | **No** ✓ |
| `قرينة` | circumstantial-proof register; not public-record-evidence | **No** ✓ |
| `إثبات` | proof-as-statistics register; semantic drift from public-record sense | **No** ✓ (the noun-em is `دليل`; `إثبات` does appear in body text as the verb-form root, which is acceptable per planner-brief §6.4) |

5/5 ban-list checks PASS. The MENA legal-press cognate `دليل` is the
unique Causa-AR anchor; no banned alternative emerges.

---

## §6 · Live walk verification · 65 routes · all 200

### §6.1 · Causa staff routes (5 locales × 5 pages = 25 routes)

| Locale | home | studio | materie | contenzioso | contatti |
|---|---|---|---|---|---|
| it | 200 (120,773 B) | 200 (72,375 B) | 200 (73,470 B) | 200 (64,714 B) | 200 (74,038 B) |
| en | 200 (120,000 B) | 200 (72,100 B) | 200 (73,430 B) | 200 (64,573 B) | 200 (73,962 B) |
| fr | 200 (121,006 B) | 200 (72,596 B) | 200 (73,899 B) | 200 (64,789 B) | 200 (74,320 B) |
| es | 200 (120,649 B) | 200 (72,495 B) | 200 (73,600 B) | 200 (64,819 B) | 200 (74,096 B) |
| ar | 200 (119,960 B) | 200 (72,788 B) | 200 (73,928 B) | 200 (65,676 B) | 200 (74,680 B) |

**25/25 staff routes 200.** Byte counts within ±1 KB across locales —
the small differences come from per-locale character widths (AR is
densest on some pages because of the Naskh CSS being included).

### §6.2 · Causa case-detail routes (5 locales × 4 posts = 20 routes)

5/5 locales × 4 posts × `?preview=1` = **20/20 case-detail routes
200**. CTA verb-class propagates correctly to inner pages
(Sottometti / Submit / Soumettez / Someta / قَدِّم on every nav pill
in every case-detail page). Italian sentence-identifiers preserved
verbatim across all 20 routes.

### §6.3 · Anonymous draft-gate (5 routes)

| Anonymous route | Expected | Got | ✓ |
|---|---|---|---|
| `/templates/business/causa-legale/preview/` (anon) | 404 | 404 | ✓ |
| `/templates/business/causa-legale/preview/studio/` (anon) | 404 | 404 | ✓ |
| `/templates/business/causa-legale/preview/contenzioso/` (anon) | 404 | 404 | ✓ |
| `/templates/business/?lang=it` (anon) | 200 + Causa absent | 200 + `causa-legale` absent | ✓ |
| Home counter `templates_live` | 24 (unchanged) | 24 preserved | ✓ |

5/5 anonymous draft-gate checks PASS. Causa is reachable for staff
via `?preview=1` and via `?lang=xx` for any of 5 locales; anonymous
visitors get 404 on every Causa route and the public catalog at
`/templates/business/` does NOT list Causa.

### §6.4 · Frozen siblings (5 anonymous homes)

| Sibling | Layout family | Anonymous home | Body data-attrs |
|---|---|---|---|
| Pragma | LF-1 | 200 | `data-motion-profile="g3-institutional"` `data-motion-kpi-animate="1"` (unchanged) |
| Cornice | LF-2 | 200 | `data-motion-profile="g2-editorial"` (unchanged · 0 patterns firing) |
| Fiscus | LF-3 | 200 | `data-motion-profile="g3-institutional"` `data-motion-kpi-animate="1"` (unchanged) |
| Solaria | LF-4 | 200 | `data-motion-profile="g3-institutional"` `data-motion-kpi-animate="1"` (unchanged) |
| Continua | LF-5 | 200 | `data-motion-profile="g4-stewardship"` (unchanged · 0 patterns firing) |

**5/5 frozen siblings byte-equivalent on motion data-attrs.** None
of the 4 corporate-suite siblings (Pragma · Fiscus · Solaria ·
Continua) gained any new motion data-attribute; Cornice (the LF-2
1st occupant) retained its `g2-editorial` profile (NOT `g2-editorial-
counter`) and continues to ship 0 motion patterns. Workflow C does
NOT touch the frozen-sibling motion bundle, confirming the user-brief
do-NOT #5 (NOT regress Cornice or the frozen live siblings).

### §6.5 · Reduced-motion 3-layer guarantee preserved

The `motion-profile-implementation-pass1.md` reduced-motion contract
is preserved in workflow C (zero changes to chrome / live-motion.js /
live-motion.css):

- **Layer 1**: `body.lm-reduced` body-class clears the hidden state
  via CSS (verified in inline LF-2 styles).
- **Layer 2**: `@media (prefers-reduced-motion: reduce)` fires
  natively in CSS (verified in inline LF-2 styles).
- **Layer 3**: JS init early-returns under `matchMedia('(prefers-
  reduced-motion: reduce)').matches` (live-motion.js · unchanged).

Under reduced motion: TIME-3 chronotick rail and 6 ticks render
default-visible (no rail-draw); EVID-3 `<details>` panels open by
default on every card (no toggle required); KPI-2 ticks land at
final value with no count-up; NAV-1 nav stays at full 84px height
(no condense); EVID-5 provenance is pinned visible (no hover-reveal).
All 5 patterns honour reduced-motion in every locale (the locale tree
contains no JS / CSS — purely content data).

### §6.6 · 45-route summary

**45/45 routes PASS** at workflow C completion:
- 25 staff Causa routes (5 pages × 5 locales) · all 200
- 20 staff Causa case-detail routes (4 posts × 5 locales) · all 200
- 5 anonymous frozen-sibling homes · all 200 + byte-equivalent on
  motion data-attrs
- 5 anonymous draft-gate checks · all PASS

---

## §7 · Test suite

```
$ python manage.py test
Found 546 test(s).
[...]
Ran 546 tests in 169.146s
OK
```

**546/546 OK · zero new failures · zero regressions.** The workflow C
pass touches only:
- 4 new content tree files (locale dispatch).
- 1 import block in `template_content.py` (4 imports + locale map).
- 1 registry entry update (locales array + tier_reason narrative).

None of the existing 546 tests exercise the new AR/EN/FR/ES Causa
trees by route (the test suite asserts on slug / tier / layout_family
/ facet count / search keywords / route status from the public
catalog · all unchanged). The new locale trees become exercise-able
by the workflow D public flip's test bumps (24 → 25 · "24+" → "25+")
or by an explicit multilingual walk test (which workflow C does not
add — kept consistent with Cornice / Continua / Solaria precedent).

---

## §8 · Anti-clone state preserved post-workflow-C

Per `anti-clone-2.0-rules.md §3 + §4`, the within-family threshold
and the 5 critical-axis vetoes hold in every locale:

| Axis | Floor | Pre-workflow-C | Post-workflow-C (5 locales) | State |
|---|---|---|---|---|
| 12 voice anchor | ≥3 | 3 | 3 (cognate-set ban-list verified live in 5 locales) | ✓ |
| 13 CTA mental model | ≥2 | 2 | 2 (Sottometti-X verb-class verified verbatim across IT/EN/FR/ES/AR) | ✓ |
| 2 hero subject | ≥2 | 2 | 2 (empty-courtroom imagery URL constant identical across locales · imported from IT module) | ✓ |
| 18 motion + page choreography | ≥2 | 2 | 2 (motion bundle identical across 5 locales · 5 patterns firing) | ✓ |
| 17 imagery register | ≥2 | 2 | 2 (EVID-5 provenance tooltip propagates verbatim · imagery URL constants identical) | ✓ |

**ALL 5 CRITICAL-AXIS VETOES STILL PASS · zero regression vs
slice-02.** Pair score remains **29/54** (or 30/54 with axis-18
promote). Within-family threshold ≥27/54 cleared with 2-3 points of
margin in every locale.

AC-V1 sub-variant adoption count: **5/9 in every locale** (KPI-2 +
NAV-1 + EVID-5 + EVID-3 + TIME-3 · 2× the ≥3 floor). Open set for
hypothetical 3rd LF-2 occupant remains 4/9 (NAV-3 · EDIT-2 · QUOTE-4
· EVID-2).

---

## §9 · Workflow D readiness · what user-handshake unlocks

Workflow D is the public flip from `tier=draft` → `tier=published_live`.
It remains **HELD pending user-handshake on the multilingual walk**
(R-SOL-8 / CS-BLOCK-13 / D-102 cadence).

When the user authorises workflow D, the cascade is documented to the
line per the Cornice public-flip precedent:

1. **TEMPLATE_REGISTRY.json**: flip Causa row's `tier` from `draft`
   to `published_live` + extend `tier_reason` with the public-flip
   narrative.
2. **Run `python manage.py sync_template_tiers`**: this is a single
   DB row update (no source change). Catalog distribution moves 24
   published_live / 1 draft → **25 published_live / 0 draft**.
3. **`apps/catalog/tests.py`**: 7 explicit-literal test bumps (24 →
   25 · "24+" → "25+") to keep the public counter assertions in line
   with the new published count. Pattern: same shape as Cornice's 23
   → 24 cascade.
4. **Walk re-verification**: 25 anonymous routes (5 locales × 5
   pages of Causa) move from 404 to 200; the public catalog `/
   templates/business/` now lists `causa-legale` × 5 locale slugs.
   Catalog header updates from `5 templates business` to `6 templates
   business` (corporate-suite cluster: Pragma + Cornice + Fiscus +
   Solaria + Continua + **Causa**).
5. **Frozen-sibling walk**: 5/5 sibling homes byte-equivalent
   post-flip (the flip is a single DB row update; no source edit
   touches any sibling content / chrome / motion).
6. **AR-specific re-verification**: anonymous AR home returns 200
   with `<html lang="ar" dir="rtl">` and `body.cs-lf-lf-2` and Naskh
   h1 (the chrome rule fires on the public anon path the same way it
   fires on the staff-preview path).
7. **Memory + reports**: write `phase_x6_causa_workflow_c.md` (this
   file) and `phase_x6_causa_public_flip.md` (the workflow D
   counterpart) into `~/.claude/projects/.../memory/` and update the
   MEMORY.md index.

**Sibling 7 readiness is unchanged by workflow D**: per slice-02 §10
the system needs 1 of 4 conditions remaining (Phase X.7b motion-
profile DNA code implementation already shipped in pass 1 · sibling-7
admission gate now ungated for non-corporate-suite cluster intake; a
7th corporate-suite sibling intake remains blocked until after Phase
X.7a ships a non-corporate-suite cluster at hardening parity).

---

## §10 · What was NOT done (workflow C scope discipline)

| Out-of-scope | Why | Where it goes |
|---|---|---|
| Public flip workflow D | held pending user-handshake on the multilingual walk | Phase X.6 step 7 (separate brief) |
| Cornice retrofit | published_live · zero changes touched at this slice | accept-as-is per priority plan §0 |
| Pragma ↔ Fiscus retrofit | both published_live · documented near-occupant § decision | accept-as-grandfathered per priority plan §2 · Phase X.10+ |
| Sibling 7 intake | corporate-suite cluster sat at 6 siblings (5 live + Causa draft) · 7th sibling held until Phase X.7a ships a non-cs cluster | Phase X.7a / X.7e+ |
| Slice 03 on Causa | sibling-level retrofit at saturation post-slice-02 · holding open sub-variants (NAV-3 · EDIT-2 · QUOTE-4 · EVID-2) for hypothetical 3rd LF-2 occupant | NEVER DO at this stage |
| `motion_profile` editor exposure | apps/editor work · explicitly out of workflow C scope | Phase X.7c (separate brief) |
| New motion-profile gates (`hero_parallax` · `nav_hide_on_scroll_down` · the 7 paper-only flags) | infrastructure pass · already RATIFIED on paper · workflow C is content-only | Phase X.7b implementation pass 2+ |
| Update `apps/catalog/preview_imagery.py business-legale` pool | the catalog tile pool was deliberately left at the original curator URLs at A.5b (those URLs only feed the marketplace tile composer · re-curate of that pool is held for a future workstream) | A.5c or future imagery-pool re-curate workstream |
| Update `docs/content-factory/imagery/packs/business-litigation.md` | legacy curator pack archived; the canonical A.5b URLs are documented in `factory/reports/imagery/causa-legale-a5b/` | NEVER DO (archival only) |

The slice does NOT touch apps/editor / apps/projects / apps/commerce ·
does NOT redesign the layout · does NOT widen into sibling 7 · does
NOT regress Cornice or the frozen siblings · does NOT silently
flatten the litigation/evidence-led register · does NOT alter
motion_profile semantics. **All 7 user-brief do-NOTs respected.**

---

## §11 · Files touched (full diff manifest)

```
apps/catalog/template_content_causa_en.py          | new file (~1147 lines · EN locale tree)
apps/catalog/template_content_causa_fr.py          | new file (~1238 lines · FR locale tree)
apps/catalog/template_content_causa_es.py          | new file (~1244 lines · ES locale tree)
apps/catalog/template_content_causa_ar.py          | new file (~1456 lines · AR locale tree · LF-2-scoped Naskh inheritance)
apps/catalog/template_content.py                   | +14 / −3 lines (4 imports + dispatch map)
TEMPLATE_REGISTRY.json                             | +5 / −1 lines (locales array + tier_reason narrative)
factory/reports/causa/causa-workflowC-multilingual.md
                                                   | this file
factory/reports/browser-verification/causa-workflowC-multilingual.md
                                                   | live walk evidence (pair file)
factory/reports/scorecard/causa-workflowC-multilingual/summary.md
                                                   | scorecard panel (pair file)
─────────────────────────────────────────────────────────────────────
                                                   | 4 new locale modules · 2 source files modified · 3 reports authored
```

Zero edits to: `apps/editor/` · `apps/projects/` · `apps/commerce/` ·
`apps/catalog/template_content_causa.py` (IT module · single source
of truth for shared imagery URL constants) · sibling content modules
(Pragma / Cornice / Fiscus / Solaria / Continua) · sibling locale
trees (Cornice EN/FR/ES/AR · Continua EN/FR/ES/AR · Solaria EN/FR/ES/
AR · Pragma · Fiscus) · LF-1 / LF-3 / LF-4 / LF-5 layout files ·
LF-2 layout files (`_layouts/lf2/content.html` + `_layouts/lf2/
styles.html`) · corporate-suite chrome (`_base.html` · the Naskh swap
selector inherited from Pass C unchanged) · live-motion.css · live-
motion.js · views.py · template_dna.py · preview_imagery.py · any
migration · `factory/standards/*.md` · `docs/content-factory/imagery/
packs/business-litigation.md` (archived).

Strictly additive; locale-data only.

---

## §12 · Exact next step

**Recommended next step: workflow D is now ready for user-handshake
hold lift.**

The workflow C deliverable is **GREEN review-ready in 5 locales**:
- 45/45 routes PASS (25 staff + 20 case-detail).
- 5/5 frozen siblings byte-equivalent.
- 546/546 Django tests OK.
- All 5 critical-axis vetoes still PASS · zero regression.
- AC-V1 sub-variant adoption preserved across locales (5/9 · 2× the
  ≥3 floor).
- Voice anchor recurrence verbatim 2-surface in every locale.
- Cornice-cognate ban verified in 5 locales · zero leakage.
- AR Naskh swap correctly scoped to LF-2 only (Continua / Pragma /
  Fiscus / Solaria AR all stay on Noto Kufi).
- Motion-profile bundle identical across 5 locales (`g2-editorial-
  counter` + 5 flags firing).
- Reduced-motion 3-layer guarantee preserved.

The user-handshake gate is the ONLY blocker between workflow C
completion and workflow D public flip. Per `causa-a6-it-review-lock.md
§13` + `voice-anchor-lock.md §6` + `lf2-family-internal-variance-
rules.md §5`, workflow D verifies all 6 binding rules on rendered
Causa home in 5 locales BEFORE the tier flip · those binding rules
are already satisfied at workflow C and re-verified at workflow D
without surface changes.

When the user authorises workflow D:
1. Flip `tier=draft` → `tier=published_live` in TEMPLATE_REGISTRY.json.
2. Run `python manage.py sync_template_tiers`.
3. Bump 7 explicit-literal test counters in `apps/catalog/tests.py`.
4. Walk-verify 25 anonymous routes 200 + 5 sibling homes 200 byte-
   equivalent + AR-specific Naskh + locale switcher honesty.
5. Author `phase_x6_causa_public_flip.md` memory + update MEMORY.md.

Until user-handshake lifts the hold, the slug stays `tier=draft` and
reachable for staff via `?preview=1` and for any locale via
`?lang=xx`.

---

## §13 · One-paragraph summary

Causa workflow C ships the 5-locale draft-reviewable rollout on top
of the IT review-locked + slice-01 + slice-02 + motion-profile pass-1
state. 4 new locale trees authored (EN · FR · ES · AR · ~5,085 net
lines of locale data) on the same-keys / same-nesting / same-list-
shapes contract; 4 new imports + dispatch map flip in
`template_content.py`; locales array `["it"]` → `["it","en","fr","es","ar"]`
+ `rtl: true` already true in `TEMPLATE_REGISTRY.json`. Voice anchor
preserved verbatim-in-translation across all 5 locales (the load-
bearing italic moves with the equivalent public-record-evidence noun:
`evidenza` → `evidence` / `preuve` / `evidencia` / `دليل` · 2-surface
recurrence on hero h1 + cs-cta-closer-cream h2 verbatim in every
locale). Side-quote verb-em derived from anchor noun in every locale
(`incardina` / `enters` / `verse` / `incardina` / `يُثبِت`). Slice-01 /
slice-02 retrofit copy propagates verbatim across locales (Sottometti
/ Submit / Soumettez / Someta / قَدِّم on every CTA pill · 4 EVID-3
citation panels in every locale with Italian sentence-identifiers
preserved · 6 TIME-3 chronotick milestones in every locale with Latin
year numerals preserved · EVID-5 provenance tooltip propagates · KPI-2
count-up + NAV-1 sticky-condense fire identically across 5 locales).
Real Arabic RTL via the corporate-suite chrome's `dir="rtl"` and the
LF-2-scoped `Noto Naskh Arabic` h1 swap inherited verbatim from
Cornice's Pass C chrome (selector `html[dir="rtl"] body.cs-lf-lf-2`);
verified live: Causa AR (LF-2) and Cornice AR (LF-2) both ship
Naskh; Pragma / Fiscus / Solaria / Continua AR (non-LF-2) stay on
Noto Kufi · zero Naskh-or-Kufi leakage. **45/45 routes PASS**: 25
staff Causa routes + 20 Causa case-detail routes + 5 anonymous
frozen-sibling homes (byte-equivalent) + 5 anonymous draft-gate
checks (Causa 404 anon + absent from public catalog). 546/546 Django
tests OK · zero new failures. All 5 anti-clone-2.0 critical-axis
vetoes still PASS · zero regression. AC-V1 sub-variant adoption
preserved at 5/9 in every locale. Cornice-cognate ban verified in 5
locales · zero leakage at the anchor noun. Tier=draft preserved · public
catalog count unchanged at 24 · workflow D public flip remains held
pending user-handshake. Zero edits to apps/editor / apps/projects /
apps/commerce / sibling content / sibling locale trees / LF chrome /
motion JS / motion CSS / views / DNA / migrations / standards. **Causa
remains sufficiently separated from Cornice in all 5 locales · all
critical-axis vetoes still PASS · reduced-motion still passes cleanly
· workflow D is ready for user-handshake hold lift · exact next step
after workflow C is the user-handshake authorisation for workflow D
public flip.**
