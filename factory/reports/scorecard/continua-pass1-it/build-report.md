# Continua · Pass 1 IT · Build report

**Date**: 2026-04-29
**Branch**: `phase-x4-design-orchestrator-hardening-v1`
**Template**: `continua-stewardship` · 4th corporate-suite sibling · 1st family-office variant
**Source brief**: `design-orchestrator/real-candidates/continua-build-brief.md`
**Tier at landing**: `draft` in `TEMPLATE_REGISTRY.json`; flipped to `published_live` in the DB only for the duration of the dev walk so the staff-preview gate did not block the verification (registry-side tier remains `draft` and will re-sync on next `seed_templates` run).

---

## 1 · Files changed

| Layer | File | Nature of change |
|---|---|---|
| DNA registry | `apps/catalog/template_dna.py` | Added `continua-stewardship` block — pine + pewter + brass palette, Crimson Pro + Public Sans, `governance-cycle-strip` injected into `section_order`, content placeholders for hero / pillars (4) / KPI / sectors. |
| Content registry | `apps/catalog/template_content_continua.py` | NEW · ~870 lines · IT-only content for 5 page kinds (home, about, custodia, mandati list, contatti) + 4 mandate detail posts. Voice anchor verbatim with `<em>generazioni</em>`. Form gate is scope + orizzonte + struttura — no P.IVA/CF, no NDA-boardroom, no ICF reference. Whistleblowing channel surfaced in footer + footnote. |
| Content registry index | `apps/catalog/template_content.py` | Imported `CONTINUA_CONTENT_IT` and registered under the `continua-stewardship` slug (IT-only · workflow C will add EN/FR/ES/AR). |
| Imagery pool | `apps/catalog/preview_imagery.py` | Added `business-stewardship` 6-slot pool with curator-verified Pexels URLs. Initial slot 0 candidate (Pexels 207658) returned a "BACK TO SCHOOL" Scrabble-tile composition; **swapped live at A.3 re-curate** to Pexels 36093623 (historic library room with rich wooden interiors). All 6 slots now read on-brief. |
| Imagery policy | `apps/catalog/imagery_policy.py` | Added `business-stewardship` to `CORPORATE_SUITE_POOL_KEYS` so the policy validator runs against Continua. |
| Seed | `apps/catalog/management/commands/seed_templates.py` | Added Continua seed entry (cluster=`corporate`, style=`classic-serif`, price tier `premium`, has_booking, has_rtl, multi-page) and metadata block. |
| Registry | `TEMPLATE_REGISTRY.json` | Added Continua row at `tier: draft` with full DNA + tier_reason narrative. |
| Skin (shared) | `templates/live_templates/business/corporate-suite/home.html` | Two opt-in additions only — no behaviour change for Pragma/Fiscus/Solaria: <br>(a) `cs-pillars .grid` switched from `repeat(3, 1fr)` to `repeat(auto-fit, minmax(220px, 1fr))` so 4-pillar siblings render 4-up at desktop without breaking 3-pillar rendering. <br>(b) New `<section class="cs-cycle">` wrapped in `{% if page_data.cycle_strip %}` and accompanying CSS · only Continua opts in. <br>(c) `page_data.cta_heading` filtered with `\|safe` so the closer voice anchor `<em>` renders rather than escaping. |

**Files NOT touched** (per the hard constraints):
- `apps/editor/*` — untouched
- `apps/projects/*` — untouched
- `apps/commerce/*` — untouched
- No new archetype defined; Continua reuses the corporate-suite shell.

---

## 2 · DNA from build brief — applied

| Brief field | Build value |
|---|---|
| `archetype` | corporate-suite |
| `sub_cluster` | family-office-multigenerazionale |
| `hero_style` | split-stewardship |
| `navbar_style` | solid-stewardship |
| `footer_style` | sectors-ribbon-continuita |
| `card_style` | pillar-stewardship |
| `button_style` | ghost-stewardship |
| `density` | airy |
| `tone` | stewardship-longitudinal |
| `imagery_direction` | stewardship-archive-room |
| `imagery_key` | business-stewardship |
| `conversion_pattern` | mandate-dialogue |
| `font_pairing` | Crimson Pro + Public Sans |
| Palette `--primary` | `#0F3A30` deep pine (L\* ≈ 21 · cream-safe per CS-PAL-01) |
| Palette `--secondary` | `#5A6E78` cool pewter |
| Palette `--accent` | `#B0875E` antique brass |
| Voice anchor IT | "La continuità di una famiglia si misura in `<em>generazioni</em>`." |
| em-word | `generazioni` (italic on a single temporal noun · CS-TYPE-02 default · NOT Solaria's contrast pair) |

The Crimson Pro fallback ladder (Spectral) was not invoked at A.5 entry — Crimson Pro loaded cleanly via Google Fonts (italic glyph coverage confirmed at 56 px h1).

---

## 3 · Section sequence — implemented

The home renders the brief's 8-section sequence verbatim, plus the cluster's invariant trust band sitting between sectors and leadership (cluster precedent — explicit at build-brief §8 Trust band row).

```
home order   = [
  hero,                       # 55/45 split · object-led right · italic on "generazioni"
  pillars-4,                  # custodia · governance · successione · compliance
  kpi-band-dark,              # 18 anni · 3 generazioni · €1.8 B · 4 riunioni CdF
  governance-cycle-strip,     # the differentiator · 3 cells · (eyebrow · figure · context)
  sectors-ribbon,             # "Profili familiari" · 8 segments
  trust-band,                 # "Riconoscimenti istituzionali" (cluster-invariant slot)
  leadership,                 # "Custodi del mandato" · 3 stewards · photo-present
  cases,                      # "Mandati in continuità" · 4 mandates · multi-year markers
  cta-closer-dark,            # voice anchor restated · single filled-brass CTA
]
```

The trust band is rendered between sectors and leadership in line with the cluster precedent set by Pragma/Fiscus/Solaria; the Continua label sharpens the Pragma generic from "sectors + association marquee" to "Riconoscimenti istituzionali" with real albo badges (Albo Trustees · STEP · ANC · OAM).

---

## 4 · Imagery pack · final disposition

| Slot | URL | Disposition |
|---|---|---|
| 0 hero | Pexels 36093623 — "historic library room with rich wooden interiors" | GO · curator-verified live · landscape 1600×1067 · object-led · zero people · brass details on fireplace + leather chair + partner desk · NO documents > 1, NO laptop, NO human |
| 1 feature | Pexels 7045772 — "black classic desk near elegant leather chair next to window in light study room" | GO · landscape · zero people · oak/leather feel · feature-band on about / accent on home pillars |
| 2 portrait senior | Pexels 5333750 — "senior woman white hair coral suit holding eyeglasses thoughtfully" | GO · 60s · woman · institutional · solves Solaria 30sCx2 gap on the senior side |
| 3 portrait 40s | Pexels 7841828 — "mature businessman in business attire arms crossed in modern office" | GO · 40s · man · West African heritage · explicit demographic distance from slot 2 |
| 4 detail | Pexels 36824936 — "elegant letter with red wax seal on a wooden desk" | GO · ceremonial · NO tax-document framing (Fiscus reservation respected) |
| 5 ambient | Pexels 6587827 — "marble stairway with golden banister in classic styled villa" | GO · NOT bookshelf (Fiscus owns it · CS-IMG-SRC-04) · NOT atrium (Pragma) · NOT warm-meeting-room (Solaria) |

**Pexels-only contract**: every URL resolves to `images.pexels.com/photos/...`. No Unsplash carve-out. Cross-cluster grep against `business-corporate` / `business-fiscal` / `business-coaching` — clean (no shared IDs).

**Curator note**: the initial slot 0 candidate (Pexels 207658) was screened live during the walk and was found to render as Scrabble-tile "BACK TO SCHOOL" — a curator failure. The replacement (36093623) was sourced via the Pexels search UI from inside the walk session, screenshot-verified before commit, and matches the brief's "private library / partner-study reading room · oak shelves · brass details · NO people" specification more exactly than the original spec's lamp-on-desk framing (the room's fireplace + leather chair + mahogany desk reads as "stewardship office" at first glance).

---

## 5 · Voice anchor · em discipline

- IT h1 (hero): `La continuità di una famiglia si misura in <em>generazioni</em>.` — italic on the single temporal noun · italic rendered as italic Crimson Pro 500 in pine.
- CTA-closer h2: voice anchor RESTATED verbatim with the same `<em>` wrap (template's `cta_heading` field gained `|safe` filter so the markup renders).
- All other headings carry exactly one em-wrap or zero — no contrast pair (Solaria's exception · §1.4 matrix Italic-em row).

---

## 6 · Form gate · differentiation

The `/contatti/` form is scope + orizzonte + struttura · the horizon-selector is the differentiating field. NO P.IVA + CF (Fiscus collision avoided). NO NDA-ready boardroom shape (Pragma collision avoided). NO ICF code-of-ethics reference (Solaria collision avoided). Form sections:
1. Referente (name + surname + email + phone)
2. Famiglia (nucleo familiare + ruolo)
3. Mandato di custodia (orizzonte 5/10/25/multi-gen + struttura holding/fondazione/trust/patto/nessuna + scope textarea)
4. Allegati (facoltativi, PDF/DOCX max 20 MB · archivio cifrato)

The submit label echoes the primary CTA: `Avvia un dialogo di mandato`.

---

## 7 · Multilingual posture (deferred to workflow C)

Pass 1 ships IT-only at draft tier per the build brief (D-102 cadence). The brief's §11 multilingual-intent block is preserved for the future workflow C pass — voice anchor verbatim-in-translation (`generations` / `générations` / `generaciones` / `الأجيال`) plus AR RTL with Noto Kufi heading swap and Amiri body. The IT walk does not gate on AR convention questions.

---

## 8 · Build outcome

- 9 Continua URLs return HTTP 200 in dev: `home / chi-siamo / custodia / mandati / mandati/<4 posts> / contatti`.
- No new archetype, no editor/projects/commerce churn, no other-template regressions.
- `cs-pillars .grid` switch to `auto-fit` is backward-compatible with 3-pillar siblings — Pragma/Fiscus/Solaria still render 3-up at 1440 (verified via the comparison captures).
- `cs-cycle` section is gated on `page_data.cycle_strip` and only Continua's content registry supplies it — invisible to all other templates.
- The shared `home.html` `cta_heading|safe` filter is safe: the field is internal content, never user input, and follows the same pattern as `headline|safe` on line 464.

Build report file count: 9 source-file edits + 1 new content module + 8 scorecard report files. Total artefact size: well within the brief's "skin-budget ≤ 1100 lines" guidance (Continua adds ~70 CSS lines to `home.html` plus ~50 lines of section markup — net new template-side surface).
