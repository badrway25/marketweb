# Solaria · Pass C · style critic

**Voice**: blunt design critic, anti-paperwork.
**Scope**: did Pass C regress any of the visual quality Pass A built and
Pass B carried? Is anything new visible enough to need re-evaluation?

---

## 1 · One-line answer

**No regression. No new visual surface. Pass C is invisible to the eye
but visible to the mouse.**

The single behavioural change — staff-preview flag propagation in
internal hrefs — does not alter a single rendered pixel. Every
component, every typeface, every palette token, every image, every
spacing decision Pass A and Pass B made survives intact. I am not going
to manufacture a new "10-row diff" for a pass that did not author
visual content; that would be exactly the meta-paperwork the
alignment-reset warned against.

---

## 2 · What I re-checked, briefly, in case I'm wrong

### 2.1 Voice anchor (the only typographic element that could regress)

Pulled live from each locale's running document:

```
IT  · Fraunces · "Il coaching non è terapia e non è consulenza."
EN  · Fraunces · "Coaching is not therapy, and not consultancy."
FR  · Fraunces · "Le coaching n'est ni une thérapie, ni du conseil."
ES  · Fraunces · "El coaching no es terapia, ni es consultoría."
AR  · Noto Kufi Arabic · "التدريب ليس علاجاً نفسياً، وليس استشارة."
```

Same as Pass B. Same italic em on "terapia / therapy / thérapie /
terapia / علاجاً نفسياً". Italic em survives the AR swap because the
locale tree still ships `<em>` markup; the AR font (Noto Kufi Arabic)
does not bleed into the Latin word "Solaria" or the Latin numerals in
the KPI band.

### 2.2 Palette

```
--primary    : #2B2A28  (warm dark carbon)
--secondary  : #C8621A  (warm earth ochre)
--accent     : #8B5A2B  (deep caramel)
```

Untouched by Pass C. `corporate_suite.E001` palette polarity gate
remains green. The build-time check has no Solaria-specific output —
silent good news.

### 2.3 Image rhythm on home (the Pass A distinctness move)

Below-the-fold home page on every locale still shows:

- 1 hero photo (coachee 1:1 conversation)
- 2 leadership portraits (Giulia Loreti, Martina Erriquez)
- 3 case-study row thumbnails

That is the same 5-photo home rhythm Pass A established. The sibling
templates (Pragma + Fiscus) still have only 1 hero each. The
distinctness vector Pass A built is not eroded.

### 2.4 RTL chrome

`<html dir="rtl">` on every AR page. `direction:rtl` computed on
`.cs-nav`. Hero photo flips to the visual left, headline column to the
right. Marketplace bar / language pills mirrored. Footer columns
mirrored. Numbering on percorsi cards reads `4/01` right-aligned.
Discovery-call form mirrored, fields read right-to-left, all field
labels Arabic.

This is unchanged from Pass B. I checked because internal hrefs now
carry `&preview=1` and I wanted to confirm no `?` / `&` separator goof
shipped in the Arabic page. It did not.

### 2.5 Hover / focus states (the easy place to break a fix like this)

Tabbed across the language switcher and the in-page nav. Focus rings
are the same teal-on-cream X.4a hardening installed on the corporate-
suite chrome. No focus ring was lost, no contrast pair was harmed.

---

## 3 · Things I did NOT review (and why)

I am not going to re-litigate the 10-row Pass A distinctness diff or
the 5-locale Pass B parity grid. Those pass docs exist at
`factory/reports/solaria/solaria-passA-it-premium-distinctness.md` and
`factory/reports/solaria/solaria-passB-multilingual.md`. Pass C did not
touch any of the surfaces those docs scored. Re-scoring them here would
be paperwork around invisible churn.

---

## 4 · The one thing I'd flag on the design layer (not a Pass C blocker)

Carried forward verbatim from Pass A's anti-claims §4: the corporate-
suite hero filter (`grayscale 15% / contrast 1.04 / brightness 0.97`)
slightly desaturates Solaria's warm carbon-and-ochre identity. A
warmer-skewed filter would suit Solaria better than Pragma + Fiscus,
but it would require an archetype-level branch on the filter rule and
is out of scope for any pass that respects the "no archetype edits"
constraint. Honest residual.

---

## 5 · Verdict

**Style: GREEN.** No regression. No drift. Solaria still looks like a
real premium coaching template, distinguishable in 10 seconds from its
two corporate-suite siblings, in 5 locales, on 1440 / 1024 / 390. Pass
C did its narrow job and stayed out of the design layer's way.
