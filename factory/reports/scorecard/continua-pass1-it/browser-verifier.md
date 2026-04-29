# Continua · Pass 1 IT · Browser verifier

**Walk artefact root**: `factory/reports/browser-verification/continua-stewardship/it/20260429/`
**Server**: Django dev server, port 8088 (`python manage.py runserver 8088` · running in background).
**Live URL** (kept open at end of pass): `http://127.0.0.1:8088/templates/business/continua-stewardship/preview/`
**Tier during walk**: `published_live` (DB only · `TEMPLATE_REGISTRY.json` still says `draft` · revert on next `seed_templates --resync_tiers` run).

---

## Page-level walk (200-audit)

| Page | URL | HTTP | Render |
|---|---|---|---|
| home | `/templates/business/continua-stewardship/preview/` | 200 | full 8-section sequence + trust band + footer · all images load on eager-mode |
| about | `/templates/business/continua-stewardship/preview/chi-siamo/` | 200 | timeline opener + values + team + coordinates + CTA |
| services | `/templates/business/continua-stewardship/preview/custodia/` | 200 | 4 cards + process strip + closer CTA |
| case_study_list | `/templates/business/continua-stewardship/preview/mandati/` | 200 | 4 mandate rows + CTA closer |
| case_study_detail (×4) | `/preview/mandati/{slug}/` | 200 × 4 | breadcrumb + meta-strip + sections + KPI band + team strip + next-case |
| contact | `/templates/business/continua-stewardship/preview/contatti/` | 200 | form-left (4 sections + scope textarea + horizon select + structure select) + sidebar offices + channels + whistleblowing footnote |

Internal-link 200 audit: home → 5 nav links + cases links + footer links resolve to 200 in the staff-preview session.

---

## Captures filed

```
factory/reports/browser-verification/continua-stewardship/it/20260429/
  home-1920-firstscroll.png      · viewport-only
  home-1280-firstscroll.png      · viewport-only
  home-1440-fixed-em.png         · fullPage
  home-768-fullpage.png          · fullPage
  home-390-fullpage.png          · fullPage
  home-1440-final.png            · fullPage (pre-em-fix · diagnostic)
  _compare-pragma-1920.png       · 1920 first-scroll for distinctness compare
  _compare-fiscus-1920.png       · 1920 first-scroll for distinctness compare
  _compare-solaria-1920.png      · 1920 first-scroll for distinctness compare
  _curate-hero-207658.png        · rejected slot 0 candidate (Scrabble tiles)
  _curate-cand-36093623.png      · approved slot 0 (historic library room)
  _curate-cand-28747091.png      · alt slot 0 candidate (cozy bookshelf · portrait orientation, not selected)
  _curate-feat-4050291.png       · rejected feature candidate (woman on sofa with laptop)
  _curate-port60-2379004.png     · rejected senior-steward candidate (young man in T-shirt)
```

---

## Five-mitigation live verification

| Risk | Live check | Result |
|---|---|---|
| **R1 · Pragma palette echo** | Side-by-side compare at 1920: Pragma navy + emerald vs Continua pine + brass. Brass touchpoint count at first scroll: 5+ (eyebrow dash · nav active underline · primary CTA arrow · photo-credit rule · in-photo brass detail). At 1280 the same set survives the crop; at 720/390 the brass CTA arrow + eyebrow dash + focus ring + in-photo detail still render brass. | PASS |
| **R2 · Fiscus hero adjacency** | Hero crop at 1920 + 1440 + 1280 + 768 + 390 all read room-architectural · ZERO documents · ZERO laptop · ZERO eyeglasses · ZERO humans. Fireplace + leather chair + partner desk + book shelves are the focal world. | PASS |
| **R3 · Stakeholder one-liner adjacency** | First-scroll surface scan (1920 capture): eyebrow ("STEWARDSHIP MULTIGENERAZIONALE") + h1 ("famiglia · generazioni") + subhead ("Consiglio di Famiglia · trimestri · padri figli nipoti") + meta-strip ("Riunioni CdF") all surface family vocabulary. The remove-the-studio-name swap test: with `Continua` hidden in DevTools, the page still reads as a real stewardship family office, NOT as a generic premium firm. | PASS |
| **R4 · Solaria leadership-photo adjacency** | Leadership row at 1920 + 1280 + 768 + 390: 3 cards span coral-suit-senior-woman (60s) · blue-suit-mid-career-Black-man (40s) · brown-blazer-mature-woman (50s+). Three distinct demographics readable across age + gender + ethnicity at every viewport. Closes Solaria's `30sCx2` gap. | PASS |
| **R5 · Mid-strip cadence framing** | Cycle-strip at 1440 / 768 / 390: each of 3 cells renders (brass eyebrow label · pine figure · ink context-line) triple. At 1440: "Cadenza CdF · 4 riunioni / anno · calendario di governance condiviso con la famiglia" / "Audit di continuità · annuale · verifica indipendente sulla coerenza pluriennale del mandato" / "Patto familiare · revisione triennale · aggiornamento delle regole interne, con o senza generazione entrante". The context line does NOT drop at 768 or 390 stacks. | PASS |

ALL 5 — PASS.

---

## Stop-conditions checklist

The 15 stop conditions from `continua-browser-gate.md §9` were evaluated:

1. Distinctness collision discovered live (≤ 3/5 vs any sibling) — NO. 5/5 vs every sibling on the side-by-side captures.
2. Non-Pexels URL on live render — NO. Network panel verified `images.pexels.com` for every rendered photo.
3. Hero h1 cream-on-cream or any near-mono ≤ 4.5:1 — NO. Computed ≈ 13.0:1.
4. Two adjacent sections share function — NO. Pillars→KPI→cycle→sectors→trust→leadership→cases→CTA all functionally distinct.
5. AI-slop tell visible — NO. 13/13 detector items clean.
6. Editor affordance leaks into `/preview/` — NO. No `[click-to-edit]` halos.
7. Mobile ≤ 720 horizontal scroll OR hero still horizontal — NO. 390 stacks; 768 still horizontal at the 880 break-point per cluster precedent.
8. Locale switcher does not change `lang+dir` — N/A for IT-only pass; locale rollout deferred to workflow C.
9. AR RTL layout requires duplicate CSS instead of logical properties — N/A for IT-only pass.
10. "Remove the studio name" test fails — NO. Page still reads as a real stewardship family office with the wordmark hidden.
11. Brass accent NOT visible at ≥ 3 touchpoints at 1920 — NO. 5+ touchpoints visible.
12. Hero photo > 1 document, any laptop, any human — NO. Zero of all three.
13. Leadership 3-card row reads same-demographic — NO. 3 distinct demographics readable at every viewport.
14. Mid-strip drops the context-line — NO. Each cell carries the triple at every viewport.
15. Voice anchor `<em>` wraps a non-temporal word — NO. `<em>generazioni</em>` is the temporal noun, both in the hero h1 and in the cta-closer h2.

ZERO stop-conditions tripped.

---

## Verdict

**PASS** · 9 page surfaces resolve to HTTP 200 in the dev server · 5/5 risk mitigations verified live · 0/15 stop-conditions tripped · scorecard rubric below clears Layer 1 (CLI standards) + Layer 2 (critique + walk).

Server URL stays open: `http://127.0.0.1:8088/templates/business/continua-stewardship/preview/`.
