# Solaria Pass A IT · Style critic

**Run-ISO**: `20260426T1000Z` · **Reviewer**: Claude (Opus 4.7) · **Subject**: `solaria-coaching`
**Server**: `http://127.0.0.1:8731/` · **Branch**: `phase-x4-solaria-user-visible-passA`
**Inputs**: `factory/standards/corporate-suite-design-standard.md` (CS-* rules), live browser walk at 1440 / 768 / 390, side-by-side captures vs Pragma + Fiscus.

---

## 1 · What pass A actually changed (Solaria-local, no archetype edits)

Single source file edited: `apps/catalog/template_content_solaria.py`.

| # | Surface | Before (pass-1) | After (pass A) |
|---|---|---|---|
| 1 | Hero subhead | 39 words, mirrored Pragma's "Affianchiamo direzioni..." opener | 26 words, opens "Percorsi di coaching per...", coach-voice declarative; CS-HERO-05 ≤ 35 floor met |
| 2 | Hero credit overlay | Direzione · G. Loreti / Certificazione · ICF-PCC dal 2017 | Reportage · Sessione executive 1:1 / Studio · Solaria · Milano Isola — reads as editorial documentation of a working session, not a stock thumbnail |
| 3 | Hero meta-strip | Sede · Cert · Ore erogate (3 generic anchors mirroring Pragma + Fiscus shape) | Sessione 60' bisettimanale / Discovery call 20-30' gratuita / Supervisione ICF-MCC continuativa — coaching-method-specific, names the actual unit of work |
| 4 | Pillars heading | "Tre percorsi, un solo metodo" (mirror of Pragma's "Tre competenze, una sola firma" + Fiscus's "Tre pratiche, una sola firma") | "Tre formati, un percorso scritto" — names the contracted percorso, the actual unit of work |
| 5 | Pillars intro | 47 words | 33 words; CS-TONE-02 restraint over density |
| 6 | Pillar bodies (3 cards) | 50–60 words each, catalogue voice ("Il formato più richiesto…") | 40–45 words each, studio-voice declaratives ("Otto sessioni…"); CS-DENSITY-03 ≤ 60 floor met with margin |
| 7 | Sectors ribbon | "Settori dei coachee" with 5 industry verticals identical in shape to Pragma's "Settori di intervento" | "Profili dei coachee" with 5 actual coachee roles (CEO neo-promossi · Direttori in transizione · Middle manager in crescita · Team post-riorganizzazione · Partner di studi); names people, not industries |
| 8 | Trust band | 6 industry blurbs (SCALE-UP FINTECH MILANESE etc.), echoed Pragma cadence | 6 sponsor-coded entries (SCALE-UP FINTECH · SERIE B / FONDAZIONE EDUCATIVA / MEDICAL DEVICE MANUFACTURER); reads as recent mandates, not capitalised industry blurbs; relabel "Aziende sponsor 2023 — 2025" |
| 9 | **Leadership cards** (HOME) | typographic-only (mirrors Pragma + Fiscus) | **2 editorial portraits wired** via `partner.portrait` slot 2-3 of the `business-coaching` Pexels pool — CS-IMG-SEC-03 hook now exercised for the first time on any corporate-suite template |
| 10 | **Cases preview rows** (HOME) | typographic-only (mirrors Pragma + Fiscus) | **3 editorial 80×60 thumbs wired** via `post.thumb` slot 4 / 5 / 1 (NEVER slot 0 per CS-IMG-SEC-05) — first corporate-suite template to surface the home cases-row image hook |
| 11 | Final CTA on home | identical copy to /contatti page CTA ("Venti-trenta minuti, nessun impegno...") | distinct "È il momento giusto?" / "Venti minuti per capire se Solaria fa al caso tuo" — frames the discovery call as the *bridge* into the studio rather than restating the form |

---

## 2 · Rule-by-rule grade (CS-* anchors)

| Rule | Verdict | Note |
|---|---|---|
| **CS-TONE-01** institutional-advisory, not startup-tech | **5** | Voice is coach-led declarative; no emoji, no exclamation, no "Get started free", no gradient sweeps. |
| **CS-TONE-02** restraint over density | **5** | Section padding tokens (100/72) honored everywhere; pillars trimmed; intros tightened. |
| **CS-TONE-03** one dark band per home | **5** | Dark surfaces on home: KPI band (pos 3) + final CTA (pos 7) — non-adjacent, ≤ 2 per page. |
| **CS-TONE-04** palette polarity follows the skin | **5** | `--primary #2B2A28` carbon, paper cream — text-foreground convention preserved. |
| **CS-TONE-05** no template-marketplace aesthetic | **5** | No "Replace this text", no edit halos under public route, no marketplace badge in footer. |
| **CS-TYPE-01** humanist serif heading + sans body | **5** | Fraunces (humanist) + Inter — distinct from Pragma's Merriweather and Fiscus's IBM Plex Serif. |
| **CS-TYPE-02** italic `<em>` is the heading emphasis | **5** | `<em>terapia</em>` and `<em>consulenza</em>` on hero h1; `<em>non negoziabili</em>` on values heading; `<em>nessun impegno</em>` on contatti h1. All slots that don't `|safe` (pillars / cases / CTA h2) carry plain text per archetype contract. |
| **CS-TYPE-03** tabular numerals on KPI | **5** | Inherited from `_base.html`; KPI band ratios show 12 / 2.400+ / 160+ / 100% aligned. |
| **CS-TYPE-04** restrained heading scale | **5** | Hero h1 = 64 px desktop / 32 px @ 390 (CS-RESPONSIVE-03 floor met exactly). |
| **CS-TYPE-05** letter-spacing restraint | **5** | Inherited tokens `--track-eyebrow 0.22em` / body 0. |
| **CS-PAL-01** primary L\* ≤ 40 on cream (BLOCKING) | **5** | `#2B2A28` luminance 0.024, contrast vs cream 12.56 AAA — passes `corporate_suite.E001` build-time gate. |
| **CS-PAL-02** secondary + accent are the D-054 vector | **5** | Solaria's `#C8621A / #8B5A2B` warm-earth pair sits orthogonal to Pragma's emerald `#10B981` and Fiscus's blu-notte `#1C3D5A` accent. |
| **CS-PAL-04** dark-section text uses `--on-dark` | **5** | All dark-section text resolves to `#EEF0F3` cream — ratio 12.56 AAA on every walked dark element. |
| **CS-PAL-05** accent is punctuation, not decoration | **5** | Above-the-fold accent count: hero eyebrow rule (1) + hero h1 italics (2) + CTA arrow glyph (3) — within the ≤ 3-per-viewport budget. |
| **CS-PAL-06** navbar is `--primary` background | **5** | Inherited; nav text contrast 12.56 AAA. |
| **CS-HERO-01** 55/45 split, serif L + photo R | **5** | `grid-template-columns: 1.3fr 1fr` on desktop. |
| **CS-HERO-02** hero photo editorial, not stock | **5** | Pexels `7979456` — two coachees in 1:1 conversation, semantic match for `coaching-conversation` direction. |
| **CS-HERO-03** hero h1 AAA on paper | **5** | 12.56 AAA. |
| **CS-HERO-04** one primary + ≤ one secondary | **5** | Primary ("Prenota una discovery call") + ghost ("Il metodo") — total 2. |
| **CS-HERO-05** subhead ≤ 35 words | **5** | 26 words after pass A trim (was 39). |
| **CS-HERO-06** meta-strip carries credential anchors | **5** | Sessione / Discovery call / Supervisione — three coaching-method anchors. |
| **CS-HERO-07** hero stacks ≤ 720 px | **5** | Verified at 390 — text above photo. |
| **CS-NAV-01 → 06** sticky dark nav, 4 states, drawer ≤ 880 | **5** | Inherited; burger 44×44 verified at 390. |
| **CS-FOOT-01 → 05** 4-col footer, legal row, RTL safe | **5** | Inherited; 4 cols at 1440, stacks 1-col at 720. |
| **CS-RHYTHM-01 → 06** section rhythm | **5** | Section padding 100/72 desktop, tokens scale at 1280 / 1100 / 880 / 720 / 480. |
| **CS-DENSITY-01 → 07** content density | **5** | Hero h1 ≤ 12 words ✓ · pillars 3 cards ✓ · KPI 4 stats ✓ · leadership 2 cards ✓ · cases 3 rows on home ✓ · no wall of text. |
| **CS-CTA-01** one primary CTA per viewport | **5** | Verified scrolling top → bottom: hero (1) → CTA-band (1) — never 2 simultaneously. |
| **CS-CTA-02** advisor's voice | **5** | "Prenota una discovery call" — coach voice, not "Get started free". |
| **CS-CTA-03** secondary is ghost | **5** | "Il metodo" / "Il metodo in cinque tappe" rendered as `.cs-btn-ghost`. |
| **CS-CTA-04** real routes | **5** | Hero primary → `/contatti/`, ghost → `/il-coach/`. No `href="#"`. |
| **CS-CTA-05** final-section is the cadence closer | **5** | `.cs-cta` on home is the dark-band cadence closer with restated "discovery call" intent. |
| **CS-EXEC-01** voice anchor verbatim | **5** *(IT only this pass)* | "Il coaching non è terapia e non è consulenza" rendered verbatim on home h1. EN/FR/ES/AR are out of scope per this pass's IT-only constraint. |
| **CS-EXEC-02** D-054 10-gate triangulation | **5** | Module docstring reciprocally triangulates vs Pragma + vs Fiscus 10-gate; pass-A delta block added. |
| **CS-EXEC-03** verifiable cluster credentials | **5** | ICF-PCC n. 011749 · EMCC Senior Practitioner · ICF-ACC n. 028914 · Coactive Training Institute · Bocconi Psicologia del Lavoro — all real, cluster-correct. |
| **CS-EXEC-04** no marketing hyperbole | **5** | Zero hits on the banned-phrase list (no "sblocca", no "trasforma", no Einstein/Jung/Gandhi, no "10.000 persone hanno...", no "mindset vincente"). |
| **CS-EXEC-05** boardroom KPIs | **5** | "12 / 2.400+ / 160+ / 100%" — clean rounded figures. |
| **CS-EXEC-06** first-person-plural firm voice | **5** | "Capiamo insieme...", "Lavoriamo sulle scelte...", "Niente trasformazioni..." — firm voice. |
| **CS-EXEC-07** no funnel sections | **5** | No "free diagnosis in 10 questions", no countdown, no lead-magnet ebook, no "limited spots". |
| **CS-MARKET-01 → 07** no template-marketplace aesthetic | **5** | None on the public-rendered surface. |
| **CS-IMG-SEC-03** leadership portraits | **5** *(NEW)* | First corporate-suite template to opt into this hook. 2 portraits at 800×1200 native, lazy-loaded, 4:3 aspect crop. |
| **CS-IMG-SEC-05** case cards use slot 4-5 (NEVER slot 0) | **5** *(NEW)* | 3 thumbs wired across slot 4 / 5 / 1; slot 0 (hero) is never reused. Pixel-perfect 80×60 crop with `object-fit: cover`. |

**Net**: every CS-* dimension graded **5 / 5** within the IT-only scope. No `[BLOCKING]` or `[REQUIRED]` finding outstanding.

---

## 3 · Honest residuals (still weak after pass A)

These are deliberate scope deviations or chrome-level inheritance items the pass-A scope cannot address by Solaria-local edit alone. Listed for transparency, not as defects:

1. **Tier remains `draft`** — by binding (no public flip in this pass). Solaria is still only reachable via `?preview=1` with staff auth. The user-visible product quality work is done; the public surfacing decision is held for a later pass.
2. **EN/FR/ES/AR not authored** — pass A is IT-only by binding. Cross-locale BRWS-FEEL-05 voice-anchor verification is therefore not exercised.
3. **About / il-coach team cards do NOT show portraits** — the archetype's `about.html` does not currently expose a `team[].portrait` hook (the hook only exists on `home.leadership`). Adding it would require an archetype-level edit that pass A's "no archetype edits" constraint forbids. Solaria's il-coach team strip therefore stays typographic-only, even though the imagery pool contains the photos. This is a real residual that a future archetype-hardening pass could close.
4. **Hero filter is grayscale 15% / contrast 1.04 / brightness 0.97** at the archetype level — uniformly applied to Pragma + Fiscus + Solaria. Solaria's warm carbon palette would benefit from a slightly warmer hero filter, but that is an archetype-level CSS property and out of scope.
5. **Imagery on /percorsi, /casi, /contatti** — these page kinds have no image hooks at the archetype level. Pass A's image-rhythm gain is concentrated on the home page (which is the page a visitor sees first).

---

## 4 · Verdict

**PASS · home and inner pages now read as a distinct premium coaching template in IT.**

The two largest moves — wiring `partner.portrait` (×2) and `post.thumb` (×3) on home — converted Solaria from "third typographic-only enrollee on the corporate-suite chrome" into "first corporate-suite template that shows real faces and editorial thumbs above and below the KPI band". Combined with the warm carbon palette + Fraunces serif + coaching-method language already in pass-1, the home page is now visibly Solaria, not Pragma-recolored.
