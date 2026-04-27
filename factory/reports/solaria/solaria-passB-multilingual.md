# Solaria · Pass B multilingual completion

**Phase**: X.4 Wave 2 Pilot #2 · Solaria — Business Coaching · **Pass**: B
**Date**: 2026-04-26 · **Run-ISO**: `20260426T1500Z`
**Branch**: `phase-x4-solaria-passB-multilingual`
**Author**: Claude (Opus 4.7)
**Audience**: project owner, plain-language honest read of what changed and what was verified.

This document does ONE job: report, in plain language, that Solaria now ships
with the same five-locale coverage (IT/EN/FR/ES/AR + Arabic RTL) as every
previously-shipped corporate-suite sibling, and that the visible quality
established by Pass A in Italian survives intact in the four added locales.

Public flip remains **out of scope** — Solaria stays at `tier=draft`. Pass B
is multilingual completion only; Pass C is the public-flip cascade per the
alignment-reset §"What we should do next now".

---

## 1 · What changed

| Surface | Before Pass B (Pass A tip `2e583af`) | After Pass B |
|---|---|---|
| Locales authored | 1 (`it` only) | 5 (`it · en · fr · es · ar`) |
| Voice anchor in render | IT only | Verbatim-in-translation in all 5 locales |
| Language switcher pills | hidden (D-068 honesty: only IT authored) | 5 pills visible (IT/EN/FR/ES/AR) |
| Arabic RTL | not authored | `<html dir="rtl">` + Noto Kufi Arabic h1 + mirrored layout |
| Cross-locale parity vs Pragma + Fiscus | regression (-4 locales) | parity (5/5 like the other corporate-suite siblings) |
| `tier` | `draft` | `draft` (unchanged · Pass C territory) |
| Test suite | 546/546 | 546/546 (no test churn) |
| `manage.py check` | clean (1 pre-existing Pragma W001 warning) | clean (same warning · no new ones for Solaria) |

### Files added

```
apps/catalog/template_content_solaria_en.py    (English locale tree)
apps/catalog/template_content_solaria_fr.py    (French locale tree)
apps/catalog/template_content_solaria_es.py    (Spanish · peninsular)
apps/catalog/template_content_solaria_ar.py    (Arabic · MSA · RTL)
factory/reports/solaria/solaria-passB-multilingual.md           (this file)
factory/reports/browser-verification/solaria-passB-multilingual.md
factory/reports/browser-verification/solaria-passB-multilingual/20260426T1500Z/*.png
factory/reports/scorecard/solaria-passB-multilingual/*.md       (8-file packet)
```

### Files modified

```
apps/catalog/template_content.py
  · imports added for the 4 new locale modules
  · TEMPLATE_CONTENT["solaria-coaching"] entry expanded from {"it"} to all 5 locales
  · pre-existing Pass-A docstring kept verbatim
```

No other source files changed. No `apps/editor`, `apps/projects`, or
`apps/commerce` edits. No archetype edits. No new archetypes. No
`TEMPLATE_REGISTRY.json` change. No DNA / preview-imagery / seed-templates
edits — Pass A already wired all of those.

---

## 2 · The voice anchor in 5 locales

The Solaria voice anchor is the load-bearing identity sentence
(CS-EXEC-01 / CS-BLOCK-11 · F2). It is preserved verbatim-in-translation
across all 5 locale trees:

| Locale | Anchor render (h1 hero · headline) |
|---|---|
| **IT** | "Il coaching non è *terapia* e non è *consulenza*." |
| **EN** | "Coaching is not *therapy*, and not *consultancy*." |
| **FR** | "Le coaching n'est ni une *thérapie*, ni du *conseil*." |
| **ES** | "El coaching no es *terapia*, ni es *consultoría*." |
| **AR** | "التدريب ليس *علاجاً نفسياً*، وليس *استشارة*." |

The full anchor — including the second + third sentences ("we don't say what
to do…", "a path has a declared beginning and a declared end…", "more
autonomous, not more dependent") — is preserved across the 5 locales in the
`il-coach` § principles section. Italian is the authoritative source; the
four other locales are translations of the same canonical sentence, not
paraphrases.

---

## 3 · Voice register decisions per locale

The four added locales each carry a register chosen to match the cluster
blueprint (coaching · adult-to-adult · ICF-aligned) and the existing
corporate-suite siblings already shipped:

| Locale | Register | Reference voices |
|---|---|---|
| EN | warm-professional, Anglo-business, declarative | HBR coaching column, Forbes coaching, Coaching at Work magazine |
| FR | vouvoiement throughout, calm-direct, no personal-development jargon | HBR France coaching, Les Echos Executives, Coaching Magazine France |
| ES | usted/ustedes, peninsular, sober | HBR en español, Cinco Días Directivos, Capital Humano |
| AR | formal MSA / الفصحى, adult-to-adult, no funnel-pattern | Asharq al-Awsat business pages, HBR Arabia coaching column |

Each locale carries **the same 5-page tree** (home, il-coach, percorsi, casi,
contatti) with the **same shape** — the dict keys, list lengths, posts list
length, form fields list, leadership credentials lists are identical to the
IT module. Only the *values* change. This is the same shape-parity contract
every other corporate-suite sibling ships under (CS-EXEC-01 · F2).

### Italian anchors preserved across locales

The four added locales preserve the Italian normative references that the IT
tree treats as anchors of the firm's identity:

- **Italian addresses** (`Via Thaon di Revel 21 · 20159 Milano · Isola`) —
  kept in Latin script for postal correctness.
- **Italian phone format** (`+39 02 3663 4712`) — the firm has one office.
- **Italian Euro figures and years** (`2014`, `2.400+ ore`) — kept as
  boardroom figures with locale-specific number separators (`,` vs `.`
  per locale, `2 400+` in FR).
- **ICF / EMCC / ACC / PCC / MCC** — kept verbatim as international
  credentials. NOT translated.
- **Codice Deontologico ICF §2.4** — translated to "ICF Code of Ethics
  §2.4" / "Code Déontologique ICF §2.4" / "Código Deontológico ICF §2.4" /
  "ميثاق ICF الأخلاقي §2.4" — section number kept as-is.
- **Reg. UE 679/2016** — translated to "EU Reg. 679/2016 (GDPR)" /
  "Règl. UE 679/2016 (RGPD)" / "Regl. UE 679/2016 (RGPD)" /
  "اللائحة الأوروبية 679/2016 (GDPR)".
- **Latin-script proper nouns** — Solaria, Giulia Loreti, Martina
  Erriquez, Donatella Rinaldi, Elena Mannucci, Università Bocconi,
  Università Cattolica, Coach Training Institute, Co-Active, GROW,
  Immunity to Change, Kegan & Lahey, Brescia, Milano, Trento, ODCEC,
  Series B, Cassazionista, NDA, LinkedIn — preserved per MENA
  business-press convention in the AR tree, kept Latin in EN/FR/ES too.

Anti-pattern guardrails (blueprint §13) cleared in every locale —
"Unlock your potential" / "Sblocca il tuo potenziale" /
"Libérez votre potentiel" / "Desbloquea tu potencial" /
"أطلِق العنان لإمكاناتك" — none appear in any rendered page. Same
clearance for "Game-changing", "Mindset vincente",
"Best version of yourself", and the Einstein/Jung/Gandhi/Steve Jobs
quote list.

---

## 4 · What was verified in the browser

Captures live at `factory/reports/browser-verification/solaria-passB-multilingual/20260426T1500Z/`:

| # | Capture | Verifies |
|---|---|---|
| 01 | `01-it-home-1440.png` | IT home, 1440×900, full page · voice anchor render baseline |
| 02 | `02-en-home-1440.png` | EN home, 1440×900, full page · voice-anchor-EN render |
| 03 | `03-fr-home-1440.png` | FR home, 1440×900, full page · voice-anchor-FR render |
| 04 | `04-es-home-1440.png` | ES home, 1440×900, full page · voice-anchor-ES render |
| 05 | `05-ar-home-1440.png` | AR home, 1440×900, full page · `dir="rtl"` + Noto Kufi h1 |
| 05b | `05b-ar-home-1440-images-loaded.png` | AR home with lazy-loaded portraits forced eager |
| 06 | `06-ar-percorsi-1440.png` | AR services page · 4 percorsi cards · numbering 4/01 right-aligned |
| 07 | `07-ar-contatti-1440.png` | AR contact page · discovery-call form · all field labels Arabic |
| 08 | `08-ar-home-390.png` | AR home, 390×844 mobile · hamburger present · zero overflow |
| 09 | `09-en-percorsi-1440.png` | EN services page · 4 percorsi cards · LTR mirror of AR |
| 10 | `10-fr-il-coach-1440.png` | FR about page · 5-step method timeline · 4-principle values |

### Browser-evaluated checkpoints (per locale)

```
IT  · dir=ltr · lang=it · h1="Il coaching non è terapia e non è consulenza."
                          fontFamily=Fraunces · overflowPx=0
EN  · dir=ltr · lang=en · h1="Coaching is not therapy, and not consultancy."
                          fontFamily=Fraunces · overflowPx=0
FR  · dir=ltr · lang=fr · h1="Le coaching n'est ni une thérapie, ni du conseil."
                          fontFamily=Fraunces · overflowPx=0
ES  · dir=ltr · lang=es · h1="El coaching no es terapia, ni es consultoría."
                          fontFamily=Fraunces · overflowPx=0
AR  · dir=rtl · lang=ar · h1="التدريب ليس علاجاً نفسياً، وليس استشارة."
                          fontFamily="Noto Kufi Arabic, Fraunces, Georgia, serif"
                          overflowPx=0 · navDir=rtl
```

### Language-switcher proof

The five-pill switcher now appears for Solaria (was hidden during Pass A
because only IT was authored — D-068 honesty rule):

```
[IT]  ←  current
[EN]  → /preview/?lang=en
[FR]  → /preview/?lang=fr
[ES]  → /preview/?lang=es
[AR]  → /preview/?lang=ar  · pill carries dir="rtl"
```

`get_available_locales("solaria-coaching")` now returns the full 5-tuple,
exactly like Pragma, Fiscus, Vertex, Cardio, Gusto, and every other
shipped corporate-suite + medical + restaurant + ecommerce sibling.

---

## 5 · Anti-claims · what is honestly NOT changed

These items from Pass A's anti-claim list still apply unchanged in Pass B:

1. **The chrome (nav · footer · KPI band · sectors band · trust band ·
   CTA band) is identical** between Solaria, Pragma and Fiscus by design.
   Pass B respected the no-archetype-edit constraint — corporate-suite
   skin files are untouched.

2. **The about page (`/il-coach`) team strip is typographic-only** in
   every locale — the archetype's `about.html` does not expose a
   `team[].portrait` hook; only `home.leadership[].portrait` does. This
   is a known archetype-level limitation and out of scope for Pass B.

3. **The inner pages (`/percorsi /casi /contatti`) have no image
   surfaces.** Same archetype-level limitation. Pass A's image-rhythm
   gain remains concentrated on the home page; the four added locales
   inherit that.

4. **The hero filter is uniform** across the three corporate-suite
   siblings (`grayscale 15% / contrast 1.04 / brightness 0.97`).
   Solaria's warm carbon palette would benefit from a slightly warmer
   filter, but that is an archetype-level CSS property and out of scope.

5. **Pragma still grandfathered on Unsplash** (the
   `corporate_suite.W001` warning surfaces on every `manage.py check`).
   Solaria stays Pexels-clean — the build-time
   `corporate_suite.E002 / E003` checks remain silent on the Solaria slug,
   and the locale-file `_POOL_*` constants are imported from the IT
   module so all 5 locales reference the same 6-URL Pexels pool.

6. **Pass B does NOT flip the tier.** Solaria stays `draft`. A normal
   visitor at `/templates/business/` does not see Solaria. A normal
   visitor opening the direct URL gets a 404. Only a logged-in staff
   user with `?preview=1` reaches it. The public catalog count remains
   21 / 22.

7. **Pass B does NOT extend imagery.** Same 6-URL Pexels pool from
   Pass A; same hero / portrait / thumb URLs in every locale. Adding
   locale-specific imagery is a future curator pass, out of scope here.

---

## 6 · Side-by-side reading guide for the user

Open these tabs in order — each pair illustrates the same surface in two
locales at the same viewport width:

- **Tab 1**: `01-it-home-1440.png` (Solaria IT home)
- **Tab 2**: `02-en-home-1440.png` (Solaria EN home)
- **Tab 3**: `05-ar-home-1440.png` (Solaria AR home · RTL)

What you should see in 10 seconds:

- **Same hero photo** in all 3 (the coachee-conversation Pexels frame).
- **Same warm-carbon + ochre palette**, same Fraunces type, same KPI
  values (12 / 2.400+ / 160+ / 100%) — the Solaria identity holds.
- **Three different headline renders**, all carrying the voice anchor
  verbatim-in-translation.
- **Tab 3 is mirrored**: navbar pills flow right-to-left, hero photo
  is on the left (vs right in IT/EN), credit overlay flips, switcher
  pills RTL, footer columns flow right-to-left.
- **No square-glyph fallback** in AR — the Arabic h1 renders in Noto
  Kufi Arabic (the corporate-suite RTL stack). No `□□□` boxes.
- **No layout overflow** at 1440 in any locale (overflowPx = 0).

If you cannot tell IT and EN apart from the screenshots — that is by
design. The hero photo, palette, type and chrome are intentionally the
same; what changes is the language. If you cannot tell IT and AR apart
— the layout flip should be unambiguous.

---

## 7 · Final verdict

**Solaria now matches the multilingual standard of every previously-good
corporate-suite sibling**: 5 authored locales, voice anchor preserved
verbatim-in-translation, real RTL for Arabic with Noto Kufi heading swap,
language switcher exposing all 5 pills honestly, no overflow at 1440 or
390, no banned phrases in any locale, all 546 tests still green, no new
`manage.py check` warnings.

The user-level multilingual goal from the alignment reset
(§5 "Is multilingual support actually implemented yet? — No.") is now
**met**. The only remaining gap from the same alignment reset is the
public-flip cascade (Pass C), which is held under separate user
authorization — Solaria stays at `tier=draft` until that pass.

Solaria is ready for human visual review of the four added locales and,
on user authorization, ready to enter the Pass C public-flip cascade
(tier draft → published_live · public-count 21 → 22 · 6-test cascade ·
homepage trust counter · discovery facets).
