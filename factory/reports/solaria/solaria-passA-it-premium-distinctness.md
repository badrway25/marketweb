# Solaria · Pass A IT premium-distinctness proof

**Phase**: X.4 Wave 2 Pilot #2 · Solaria — Business Coaching · **Pass**: A
**Date**: 2026-04-26 · **Run-ISO**: `20260426T1000Z`
**Branch**: `phase-x4-solaria-user-visible-passA`
**Author**: Claude (Opus 4.7)
**Audience**: project owner, reading honestly. Plain language, evidence-cited.

This document does ONE job: show, side by side, that Solaria's Italian home now reads as a different premium template from Pragma + Fiscus, not a recolored sibling. Captures sit at:
- `factory/reports/browser-verification/solaria-passA-it/20260426T1000Z/01-home-1440-passA.png` (Solaria post-pass-A)
- `factory/reports/browser-verification/solaria-passA-it/20260426T1000Z/02-pragma-home-1440-baseline.png`
- `factory/reports/browser-verification/solaria-passA-it/20260426T1000Z/03-fiscus-home-1440-baseline.png`

All three were captured at 1440 × 900, fullPage, on the same dev server (`127.0.0.1:8731`), in the same Chromium MCP context, in the same minute. Reveal-target opacity was forced to 1 for capture so the screenshots show what a visitor sees within ~200 ms of any scroll (the IntersectionObserver-driven reveal is a motion polish, not a content change — see `factory/reports/scorecard/solaria-passA-it/browser-verifier.md §6 deviation 3`).

---

## 1 · The 10-row diff that matters

| # | Surface (above-the-fold to footer) | Solaria pass A | Pragma | Fiscus |
|---|---|---|---|---|
| 1 | Heading typeface | **Fraunces** (humanist serif · warmer x-height · ink-black weight 700 · italic em on "terapia" + "consulenza") | Merriweather (transitional serif · narrow x-height · italic em on "che contano") | IBM Plex Serif (contemporary serif · italic em on "corretto") |
| 2 | Palette primary / accent | **Warm carbon `#2B2A28` + earth ocra `#C8621A`** (warmth-first axis) | Navy `#1E293B` + cool emerald `#10B981` (cool-tech axis) | Dark gray `#1F2937` + warm gold + blu-notte `#1C3D5A` (institutional axis) |
| 3 | Hero photo | Two coachees in 1:1 conversation, daylight office, 3/4 profile reportage | Hand on flipchart pinning post-it (boardroom workshop) | Tidy fiscal desk close-up: laptop + folders + glasses |
| 4 | Hero credit | **Reportage / Sessione executive 1:1 · Studio / Solaria · Milano Isola** (editorial documentation framing) | Fotografia / CdA Industriale Lombarda · 2025 + Anno fondazione / 2004 (firm + history credit) | Direzione / Dott. A. Ruffini + Anno fondazione / 2003 (founder + studio credit) |
| 5 | Hero meta-strip | **Sessione · 60 minuti · cadenza bisettimanale / Discovery call · 20-30 minuti · gratuita / Supervisione · ICF-MCC continuativa dal 2019** — names the unit of work (a sessione, a discovery call, the supervision arrangement) | Headquarters / Equipe senior / Mandati attivi — names the firm's footprint | Sede / Albo ODCEC / Clienti attivi — names the studio's licensure footprint |
| 6 | Pillars heading | "Tre formati, **un percorso scritto**" — names the contracted percorso (the unit of work in coaching) | "Tre competenze, una sola firma" | "Tre pratiche, una sola firma" |
| 7 | Sectors ribbon | **Profili dei coachee** · CEO neo-promossi · Direttori in transizione · Middle manager in crescita · Team post-riorganizzazione · Partner di studi (names the actual people in the room) | Settori di intervento · Industria · Servizi finanziari · Energia · Retail · Healthcare (names client industries) | Settori dei clienti · Partite IVA · PMI manifattura · Studi professionali · Wealth privato · Immobiliare (names client legal forms) |
| 8 | Trust band | **Aziende sponsor 2023 — 2025 · nomi oscurati per Codice ICF §2.4** · 6 sponsor-coded mandates (SCALE-UP FINTECH · SERIE B / FONDAZIONE EDUCATIVA / MEDICAL DEVICE MANUFACTURER...) | "Hanno scelto Pragma negli ultimi cinque anni" · 6 industry-blurb wordmarks (GRUPPO INDUSTRIALE BRESCIANO · FONDO MEZZANINO ITALIA...) | "Seguono con Fiscus la propria fiscalità" · 6 anonymized client classes (PARTITE IVA INDIVIDUALI · STUDI DI CONSULENZA...) |
| 9 | **Leadership cards (above the cases section)** | **2 editorial portraits** (4:3 figure crop · Pexels coach + coachee from `business-coaching` pool slot 2/3 · 800×1200 native · lazy-loaded) on top of the typographic block | typographic-only · 3 cards · no portraits | typographic-only · 3 cards · no portraits |
| 10 | **Cases preview rows (below the cases-section heading)** | **3 editorial 80×60 thumbnails** inside the row title (slot 4 detail-notebook / slot 5 ambient-warm-office / slot 1 feature-man-with-notebook · NEVER slot 0 per CS-IMG-SEC-05) | typographic-only · 3 rows · no thumbnails | typographic-only · 3 rows · no thumbnails |

Rows 9 and 10 are the largest single distinctness moves. Pragma and Fiscus both ship the corporate-suite chrome but leave the `partner.portrait` and `post.thumb` hooks unused; Solaria pass A is the **first** corporate-suite template to wire them. Visually this means Solaria has 5 coaching-pool images on the home page (1 hero + 2 portraits + 3 thumbs) where Pragma and Fiscus each have 1 image (just the hero). The home page is no longer "visually thin below the KPI band"; it has real faces and real editorial accents in the 1200 px below the dark band.

---

## 2 · Anti-claims · what is honestly NOT distinct

The user prompt asked for honesty about residuals. Here is the load-bearing list:

1. **The chrome (nav · footer · KPI band · sectors band · trust band · CTA band) is identical** between Solaria, Pragma and Fiscus by design. The corporate-suite archetype is the shared shell; differentiation comes from palette + typography + imagery + copy. Pass A respects this constraint — no archetype-folder edit was made. If you compare the *layout skeleton* of the three sites, it is the same skeleton. That is the design contract; D-054 differentiation is a content + palette + imagery vector, not a chrome vector.

2. **The about page (/il-coach) team strip is typographic-only on Solaria too.** The archetype's `about.html` does not currently expose a `team[].portrait` hook (only `home.leadership[].portrait` does). Solaria's `il-coach` team cards therefore stay typographic-only, even though the imagery pool would have additional photos available. This is a real residual that a future archetype-hardening pass could close — but pass A's "no archetype edits" constraint forbids it.

3. **The inner pages (/percorsi /casi /contatti) have no image surfaces.** Same archetype-level limitation. Pass A's image-rhythm gain is concentrated on the home page where the hooks exist.

4. **The hero filter is uniform across the three siblings** (`grayscale 15% / contrast 1.04 / brightness 0.97` — applied at the archetype level on `.cs-hero .right`). Solaria's warm carbon palette would benefit from a slightly warmer filter that doesn't desaturate, but that is an archetype-level CSS property and out of scope.

5. **Pragma still grandfathered on Unsplash** (the `corporate_suite.W001` warning surfaces on every `manage.py check`). Solaria is **not** grandfathered — Solaria's pool is 6/6 Pexels and the build-time `corporate_suite.E002 / E003` checks are silent on the Solaria slug.

6. **Pass A is IT-only**. EN / FR / ES / AR locale trees are not authored. The cross-locale BRWS-FEEL-05 voice-anchor verification is therefore not exercised this pass.

7. **Solaria stays at `tier=draft`**. A normal visitor going to `/templates/business/` does not see Solaria. A normal visitor opening the direct URL gets a 404. Only a logged-in staff user with `?preview=1` can see Solaria today. Pass A does not flip the tier; the public-flip cascade is held for a separate user-authorized pass.

These seven items are honest residuals, not paperwork. None of them blocks the pass A goal (make Solaria look like a real premium distinct template in IT before any multilingual or public rollout).

---

## 3 · Side-by-side reading guide

Open the three captures in three browser tabs:

- **Tab 1**: `01-home-1440-passA.png` (Solaria)
- **Tab 2**: `02-pragma-home-1440-baseline.png` (Pragma)
- **Tab 3**: `03-fiscus-home-1440-baseline.png` (Fiscus)

What you should see in 10 seconds:

- **Three different hero photos** — coachee conversation vs boardroom workshop vs fiscal desk close-up. Same archetype layout, three different worlds.
- **Three different palettes** — warm carbon-and-earth vs navy-and-emerald vs dark-gray-and-warm-gold. Hero eyebrow rule + accent-coloured italic em + arrow glyph all change colour family between the three.
- **Three different heading typefaces** — Fraunces's humanist warmth vs Merriweather's transitional restraint vs IBM Plex Serif's contemporary edge.
- **Solaria has visible faces** below the KPI band; Pragma and Fiscus do not.
- **Solaria has visible thumbs** in the cases section; Pragma and Fiscus do not.
- **Three different voice anchors** — "Il coaching non è terapia e non è consulenza" vs "Dove si prendono le decisioni che contano" vs "L'adempimento corretto, non la trovata".

If you cannot tell the three sites apart, the differentiation has failed. With pass A, you should be able to.

---

## 4 · How to verify yourself (5-minute walk)

```bash
# 1. From the marketweb project root, with the dev server running on 8731:
open http://127.0.0.1:8731/account/login/   # log in as solaria_qa_staff / solariapassA2026

# 2. Open Solaria home (staff preview):
open http://127.0.0.1:8731/templates/business/solaria-coaching/preview/?preview=1

# 3. Open Pragma + Fiscus side by side (no preview flag needed; both are tier=published_live):
open http://127.0.0.1:8731/templates/business/pragma-corporate-suite/preview/
open http://127.0.0.1:8731/templates/business/fiscus-commercialista/preview/

# 4. Compare row 9 (leadership) and row 10 (cases preview) between the three.
#    Solaria shows 2 portraits and 3 thumbs; the others show neither.
```

You will also see the 4 inner Solaria pages render in IT under the same staff preview:
- `/templates/business/solaria-coaching/preview/il-coach/?preview=1`
- `/templates/business/solaria-coaching/preview/percorsi/?preview=1`
- `/templates/business/solaria-coaching/preview/casi/?preview=1`
- `/templates/business/solaria-coaching/preview/contatti/?preview=1`

---

## 5 · Final verdict

**Solaria IT is now visibly distinct from Pragma and Fiscus and is genuinely ready for human visual review.** The home page no longer feels visually thin; the leadership and cases sections show real coaching-pool imagery; the meta-strip and trust band are coaching-coded rather than corporate-coded; the CTA is differentiated from the contact form. Inside the IT-only / no-public-flip / no-archetype-edits constraint set, this is the maximum quality lift available. The next levers are EN/FR/ES/AR authoring (Pass B) and the public-flip cascade (Pass C) per the alignment-reset §"What we should do next now" — both held for separate user-authorized increments.
