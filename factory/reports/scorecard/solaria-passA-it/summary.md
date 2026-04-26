# Solaria Pass A IT · Summary

**Run-ISO**: `20260426T1000Z` · **Subject**: `solaria-coaching`
**Goal of pass A** (verbatim from the user prompt): *"Upgrade Solaria so that the Italian version reads as a truly distinct, premium, elegant, modern, dynamic, professional template — not just a technically integrated third enrollee."*

---

## 1 · One-paragraph verdict

Solaria's Italian home now reads as a visibly distinct premium coaching template, not a recolored Pragma/Fiscus sibling. The largest single move was wiring the archetype's two unused image hooks — `partner.portrait` on home leadership cards and `post.thumb` on home case-preview rows — both for the first time on any corporate-suite template. Combined with a tightened hero (≤ 35 words), an editorial reportage credit overlay, a coaching-method-specific meta-strip, sponsor-coded trust band, and a home CTA differentiated from the contact form, the home now shows real coachee/coach faces above and below the KPI band where the pass-1 draft showed only typographic blocks. All 171 catalog tests stay green; `manage.py check` is clean (only the expected Pragma W001 grandfather warning); 0 console errors; AAA contrast on every body slot.

## 2 · What changed (Solaria-local, no archetype edits)

- **Files touched**: 1 — `apps/catalog/template_content_solaria.py`. No edits to the archetype skin folder, no edits to `apps/editor / apps/projects / apps/commerce`, no new archetypes.
- **Hard-constraint compliance**: all 10 hard constraints from the user prompt verified — IT-only, no multilingual rollout, no public flip, Pexels-only imagery, browser-live verification mandatory, Playwright MCP used, server URL/port reported, no apps/editor changes, no apps/projects changes, no apps/commerce changes, no new archetypes.

## 3 · Distinctness vs Pragma + Fiscus

Captured side-by-side at 1440 × 900 desktop:

| Dimension | Solaria (pass A) | Pragma | Fiscus |
|---|---|---|---|
| Hero photo | Two coachees in 1:1 conversation | Hands-on-flipchart boardroom | Fiscal-desk close-up with laptop + papers |
| Hero credit | Editorial reportage ("Sessione executive 1:1 / Solaria · Milano Isola") | Firm credit ("CdA Industriale Lombarda · 2025 / 2004") | Founder credit ("Dott. A. Ruffini / 2003") |
| Hero meta-strip | Coaching-method (Sessione 60' bisettimanale / Discovery call gratuita / Supervisione ICF-MCC) | Boardroom (Headquarters / 14 partner / 42 mandati) | Studio (Sede / Albo ODCEC 4 iscritti / 260 partite IVA) |
| Heading typography | **Fraunces** (humanist serif, warmer) | Merriweather (transitional serif) | IBM Plex Serif (contemporary) |
| Palette | Warm carbon `#2B2A28` + ocra `#C8621A` + earth brown `#8B5A2B` | Navy `#1E293B` + blue `#3B82F6` + emerald `#10B981` | Dark gray `#1F2937` + warm gold `#B58F4A` + blu-notte `#1C3D5A` |
| Sectors ribbon | "Profili dei coachee" (CEO neo-promossi · Direttori in transizione · Middle manager in crescita...) | "Settori di intervento" (Industria · Servizi finanziari · Energia...) | "Settori dei clienti" (Partite IVA · PMI manifattura · Studi professionali...) |
| Trust band | Sponsor-coded mandates (SCALE-UP FINTECH · SERIE B / FONDAZIONE EDUCATIVA / MEDICAL DEVICE MANUFACTURER) | Industry blurbs (GRUPPO INDUSTRIALE BRESCIANO · FONDO MEZZANINO ITALIA...) | Anonymized client classes (PARTITE IVA INDIVIDUALI · STUDI DI CONSULENZA...) |
| **Leadership cards** | **2 editorial portraits** (Pexels coach / coachee) | typographic-only | typographic-only |
| **Cases preview rows** | **3 editorial 80×60 thumbs** (notebook detail / warm office / man-with-notebook) | typographic-only | typographic-only |
| Final CTA copy | "È il momento giusto?" / "Venti minuti per capire se Solaria fa al caso tuo" | "Una conversazione preliminare" / "Trenta minuti, agenda ristretta, niente impegno" | "Primo appuntamento" / "Quarantacinque minuti, agenda aperta, nessun impegno" |
| Voice anchor | *"Il coaching non è terapia e non è consulenza"* | *"Dove si prendono le decisioni che contano"* | *"L'adempimento corretto, non la trovata"* |

## 4 · Honest residuals (still weak after pass A)

1. **Tier remains `draft`** — by binding (no public flip in this pass).
2. **EN / FR / ES / AR not authored** — pass A is IT-only by binding.
3. **About-page team strip stays typographic-only** — the archetype's `about.html` does not currently expose a `team[].portrait` hook (only `home.leadership[].portrait` does). Adding it would require an archetype edit, which pass A's "no archetype edits" constraint forbids. The portraits live in the imagery pool but cannot surface on `il-coach` without an archetype-level change.
4. **Inner pages /percorsi /casi /contatti still have no imagery hooks** at the archetype level — same chrome constraint. Pass A's image-rhythm gain is concentrated on the home page.
5. **Hero filter (grayscale 15% / contrast 1.04 / brightness 0.97)** is uniform across Pragma + Fiscus + Solaria at the archetype level — Solaria's warm carbon palette would benefit from a slightly warmer hero filter, but that is also an archetype-level CSS property out of scope.

These residuals are real, not paperwork. A future pass can address them once the archetype-edit constraint is relaxed.

## 5 · Server + access

- **URL**: `http://127.0.0.1:8731/`
- **Solaria home (staff preview)**: `http://127.0.0.1:8731/templates/business/solaria-coaching/preview/?preview=1`
- **Auth**: `solaria_qa_staff` / `solariapassA2026` (password reset to a known string for this session per pass-A staff-preview convention)
- **Server status**: running in background (Django autoreload enabled)

## 6 · Files written this pass

```
M  apps/catalog/template_content_solaria.py        (Pass A delta · ~120 LOC of edits + 6 _POOL_* constants)
A  factory/reports/solaria/solaria-passA-it-premium-distinctness.md  (side-by-side proof)
A  factory/reports/browser-verification/solaria-passA-it.md          (browser-walk narrative)
A  factory/reports/browser-verification/solaria-passA-it/20260426T1000Z/01-home-1440-passA.png
A  factory/reports/browser-verification/solaria-passA-it/20260426T1000Z/02-pragma-home-1440-baseline.png
A  factory/reports/browser-verification/solaria-passA-it/20260426T1000Z/03-fiscus-home-1440-baseline.png
A  factory/reports/browser-verification/solaria-passA-it/20260426T1000Z/04-il-coach-1440.png
A  factory/reports/browser-verification/solaria-passA-it/20260426T1000Z/05-percorsi-1440.png
A  factory/reports/browser-verification/solaria-passA-it/20260426T1000Z/06-casi-1440.png
A  factory/reports/browser-verification/solaria-passA-it/20260426T1000Z/07-contatti-1440.png
A  factory/reports/browser-verification/solaria-passA-it/20260426T1000Z/08-home-mobile-390.png
A  factory/reports/browser-verification/solaria-passA-it/20260426T1000Z/09-home-tablet-768.png
A  factory/reports/scorecard/solaria-passA-it/style-critic.md
A  factory/reports/scorecard/solaria-passA-it/contrast-accessibility.md
A  factory/reports/scorecard/solaria-passA-it/responsive-auditor.md
A  factory/reports/scorecard/solaria-passA-it/browser-verifier.md
A  factory/reports/scorecard/solaria-passA-it/scorecard.md
A  factory/reports/scorecard/solaria-passA-it/summary.md     (this file)
```

## 7 · Final answer to the user's questions

- **Files changed**: 1 (`apps/catalog/template_content_solaria.py`).
- **Server command used**: `python manage.py runserver 127.0.0.1:8731` (autoreload on).
- **URL/port left open**: `http://127.0.0.1:8731/` · Solaria home at `/templates/business/solaria-coaching/preview/?preview=1`.
- **Major visible improvements made**: (1) leadership now shows 2 real portraits via the unused archetype `partner.portrait` hook, (2) cases preview now shows 3 editorial 80×60 thumbnails via the unused `post.thumb` hook, (3) hero subhead trimmed from 39 → 26 words, (4) hero meta-strip rewritten with coaching-method anchors (60' bisettimanale / discovery call gratuita / ICF-MCC supervision), (5) hero credit reframed as editorial reportage, (6) sectors ribbon relabelled "Profili dei coachee" naming actual people not industries, (7) trust band rewritten as sponsor-coded mandates, (8) home final-CTA differentiated from contact-form CTA.
- **Remaining weak points**: still `tier=draft`, no EN/FR/ES/AR yet, about-page team cards typographic-only (no archetype hook), inner pages /percorsi /casi /contatti have no imagery surfaces.
- **Side-by-side distinctness verdict vs Pragma/Fiscus**: **clearly distinct** — different hero photo, different hero typography (Fraunces vs Merriweather vs IBM Plex Serif), different palette (warm carbon vs navy vs dark-gray-with-gold), different leadership treatment (portraits vs typographic-only), different cases treatment (thumbs vs typographic-only), different copy voice (coaching-method declarative vs board-advisory sober vs fiscal-precision institutional). All three captured side-by-side in `factory/reports/browser-verification/solaria-passA-it/20260426T1000Z/{01,02,03}-*-1440-*.png`.
- **Is Solaria IT now genuinely ready for human visual review?**: **Yes**, at `tier=draft` via staff preview. The user-visible product quality work is done; the public-flip + multilingual passes remain held for separate user-authorized increments.
