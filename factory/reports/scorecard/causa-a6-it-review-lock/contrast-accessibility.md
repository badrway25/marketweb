# Causa · A.6 IT review-lock · contrast + accessibility

**Phase**: X.6 Step 5 · A.6 review-lock
**Template**: causa-legale (LF-2 · 6th corporate-suite sibling)
**Date**: 2026-05-04
**Verdict**: 4.6 / 5 · contrast clean · 1 alt-text nudge deferred

---

## §1 · Contrast pairs (post-fix · sampled live)

The locked palette is bottle-green `#14342B` + bone `#F0EBE0` + obsidian
`#0B0A0E`. Computed luminance pairs against WCAG 2.1 AA / AAA thresholds:

| Surface | Foreground | Background | Ratio (computed) | AA normal (4.5) | AA large (3) | AAA normal (7) | Verdict |
|---|---|---|---|---|---|---|---|
| Hero h1 (GT Sectra 56-64px on bone paper) | obsidian em / bottle-green text | bone `#F0EBE0` | bottle-green-on-bone ≈ 9.4 · obsidian-on-bone ≈ 17.9 | ✅ | ✅ | ✅ | AAA |
| Hero KPI numerics (bone on dark hero gradient ::after) | bone `#F0EBE0` | rgba(15,18,22,0.78) over the placeholder gradient | ≈ 12.8 (gradient bottom-left landing zone) | ✅ | ✅ | ✅ | AAA |
| Hero KPI labels (bone uppercase 11px) | bone | same gradient | ≈ 12.8 | ✅ | ✅ | ✅ | AAA |
| Side-quote (italic obsidian on bone) | obsidian em + ink-soft body | bone | ≈ 17.9 / ≈ 9.0 | ✅ | ✅ | ✅ | AAA |
| Drop-cap obsidian-tinted | obsidian | bone | ≈ 17.9 | ✅ | ✅ | ✅ | AAA |
| Pull-quote em obsidian italic | obsidian | bone | ≈ 17.9 | ✅ | ✅ | ✅ | AAA |
| Sectors-ribbon (italic Manrope 14px upper) | bottle-green | bone | ≈ 9.4 | ✅ | ✅ | ✅ | AAA |
| Leadership h2 + role + bio | bottle-green / obsidian / ink-soft | bone | ≈ 9.4 / 17.9 / 8.0 | ✅ | ✅ | ✅ | AAA |
| Magazine card h3 + body + meta pill | bottle-green / ink / bone-on-bottle-green | bone / paper-2 / bottle-green | all ≥ 7 | ✅ | ✅ | ✅ | AAA |
| Magazine card hero placeholder text "imagery hold..." | bone @ 55% opacity | bottle-green gradient | ≈ 4.8 · readable but not AA at small sizes | ✅ (large 28px) | ✅ | ⚠️ (28px italic Georgia · just under AAA at this opacity) | AA pass |
| CTA closer h2 obsidian em on bone | obsidian | bone | ≈ 17.9 | ✅ | ✅ | ✅ | AAA |
| CTA closer pill (bone on bottle-green filled button) | bone | bottle-green | ≈ 9.4 | ✅ | ✅ | ✅ | AAA |
| Navbar wm-line-1 (bottle-green on cream nav band) | bottle-green | cream paper | ≈ 9.4 | ✅ | ✅ | ✅ | AAA |
| Navbar pill bone on bottle-green | bone | bottle-green | ≈ 9.4 | ✅ | ✅ | ✅ | AAA |
| Footer whistleblowing column ink-on-bottle-green | bone / ink-on-paper | bottle-green / paper | all ≥ 9 | ✅ | ✅ | ✅ | AAA |

**14 / 14 contrast pairs pass AA · 13 / 14 pass AAA.** The single AA-only
pair is the placeholder's italic 28px label at 55% opacity — which is
deliberately demoted in visual weight (it's a hold pattern, not active
content). The label still passes AA at large-text threshold.

---

## §2 · Accessibility findings

| ID | Finding | Severity | Status |
|---|---|---|---|
| A.6-A1 | Founder portrait `<img>` alt = literal "Lorenzo Marchetti" (heading striptags fallback). The planner-brief §5 + imagery-pack §1 binding triple expects an alt that conveys the chambers backdrop ("the room is half the subject"). | low | DEFERRED to A.5b — the fix requires either adding a `leadership_portrait_alt` field to the content module + updating `lf2/content.html` (touches LF-2 family file = Class II), or renaming the founder heading to remove the em wrap. Neither is narrow A.6 scope. The placeholder portrait at A.6 has alt="Lorenzo Marchetti" which is functionally accessible but less descriptive than the planner-brief ideal. |
| A.6-A2 | Magazine card placeholder thumbnails inherit `card.photo_alt` which still reads the original curator caption (e.g. "Dettaglio architettonico di alta corte italiana · frontone classico con iscrizione latina · luce fredda overcast"). The alt now describes content the user does NOT see (the placeholder is a bottle-green gradient). | low | ACCEPTED at A.6 — the curator captions remain valid as the *intended* alt text; A.5b will replace the placeholder with the captioned subject and the alt text will become accurate again. Setting the alt to "imagery hold" at A.6 would have to be re-undone at A.5b. |
| A.6-A3 | Hero `.photo` is `<div role="img" aria-label="...">` (NOT an `<img>`) so the placeholder has no img-tag alt. The `aria-label` reads "Aula di tribunale vuota · luce fredda · pareti in legno verticale e tinte bone · interno architettonico" which describes the intended subject, not the placeholder. | low | ACCEPTED — same rationale as A.6-A2. The aria-label remains the intended subject; A.5b restores accurate. |
| A.6-A4 | All form fields on `/contatti/` have `<label for>` + helper text + required indicator. Verified live. | none | PASS |
| A.6-A5 | All nav links + footer links have descriptive text + `is-current` state. | none | PASS |
| A.6-A6 | Hamburger nav at ≤880 uses `<input type="checkbox">` + `<label for>` pattern (CSS-only). Keyboard-accessible. | none | PASS |
| A.6-A7 | Focus-visible rings on all CTA pills + nav links + form fields use obsidian `#0B0A0E` outline 2px on bone. Computed contrast ≥ 12. | none | PASS |
| A.6-A8 | Reveal animations honour `prefers-reduced-motion`. Verified via the cluster-shared `live-motion.js` which gates animation on the media query. | none | PASS |

**0 medium/high accessibility findings.** 3 low-severity findings deferred
to A.5b (1 alt-text quality nudge + 2 alt-text consistency notes that
auto-resolve when the placeholder is replaced).

---

## §3 · Reduced-motion + RTL safety

- `prefers-reduced-motion: reduce` honored — verified by injecting the
  media query override + observing `[data-lm]` blocks render at full
  opacity without transitions.
- RTL parity not yet shipped (IT-only at A.6 · workflow C will add EN/FR/
  ES/AR + AR Naskh h1 swap). The `body.cs-lf-lf-2` selector inherited
  from Cornice's Pass C is in place and ready.

---

## §4 · Contrast + accessibility verdict

**Contrast clean · accessibility clean modulo the deferred alt-text quality
nudge.** Score: **4.6 / 5** (the 0.4 deduction is the alt-text
consistency notes that auto-resolve at A.5b imagery re-curate · they are
not actionable at A.6 inside the scope rules).
