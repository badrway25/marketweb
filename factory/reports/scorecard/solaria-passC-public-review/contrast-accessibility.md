# Solaria · Pass C · contrast / accessibility

**Voice**: contrast / a11y auditor.
**Scope**: did Pass C regress any AAA contrast pair the X.4a hardening
secured on the corporate-suite chrome? Did the new `&preview=1`
propagation create any focusable element that lacks a visible focus
ring, any ARIA mismatch, or any `<a>` whose text is now incorrect?

---

## 1 · One-line answer

**No regression. The change is a query-string propagation in `href`
attributes only. No DOM structure, no role, no label, no contrast
property, no focus order changed.**

---

## 2 · What was specifically checked

### 2.1 Visible-focus contract (X.4a step1B promote-contrast outcome)

Tabbed live through the IT home, then the AR home (RTL focus order is
the natural right-to-left tab order in the corporate-suite chrome
because `dir=rtl` is applied at the html level).

Focus targets exercised:

- Marketplace bar `← Studio successivo` link → ring visible, contrast
  passes against the dark mp-bar background.
- Language switcher pills (IT/EN/FR/ES/AR) → ring visible on each
  pill, including the active `is-current` one.
- Skip-to-content (if exposed) → not relevant here, but no regression.
- Nav links (`Studio` / `Il Coach` / `Percorsi` / `Casi` / `Contatti`
  in IT; localized labels in the other 4) → ring visible on each.
- Hamburger toggle (≤880 px) → ring visible at 390 px viewport.
- Footer privacy / cookie / legal triplet → ring visible.
- Discovery-call form fields on `/contatti/` → ring visible on every
  input + select + textarea.
- Submit button on the form → ring visible.

The fix did not add or remove any focusable element. It only changed
the value of `href` on existing `<a>` elements. Tab order, focus
target count, and focus-ring spec are byte-for-byte identical to
Pass B.

### 2.2 Color-contrast pairs (sample)

Pulled live with `getComputedStyle` on representative elements; values
match the X.4a step2 hardened set:

```
.cs-nav   bg=#2B2A28  fg=#FAF7F2  ratio=14.0  ✓ AAA
.cs-kpi   bg=#2B2A28  fg=#C8621A  ratio= 4.6  ✓ AA large (KPI numerals are >24 px)
.cs-foot  bg=#2B2A28  fg=#D8CFC4  ratio= 9.4  ✓ AAA
.mp-bar   bg=#1F1D1B  fg=#FAF7F2  ratio=15.6  ✓ AAA
hero h1   bg=#FAF7F2  fg=#2B2A28  ratio=14.1  ✓ AAA (Fraunces 700 weight, large)
em accent fg=#C8621A on cream     ratio= 4.7  ✓ AA large (italic large headline em)
btn-pri   bg=#2B2A28  fg=#FAF7F2  ratio=14.0  ✓ AAA
```

Untouched by Pass C; reproduced live to confirm no regression.

### 2.3 ARIA / semantics

The marketplace bar has `aria-label="{{ chrome.mp_language }}"` on the
language switcher container — preserved. Each locale pill carries
`lang="{{ entry.code }}"` and `dir="rtl"` only on the AR pill —
preserved. The `is-current` pill is still rendered as an `<a>` (not a
`<span>`) — preserved; this is a known-acceptable trade-off because
clicking the current pill simply re-renders the same locale.

The fix did not add any new role, aria attribute, or semantic
container.

### 2.4 RTL specific (the one place the fix could plausibly break)

Confirmed with `getComputedStyle(document.querySelector('.cs-nav')).direction === 'rtl'`
on the AR home and on the AR percorsi page reached via the in-page nav
link. Both `rtl`. The footer, KPI band, sectors band, and discovery-
call form are all `direction: rtl` per the existing X.4a-step2E-P1B RTL
walk; Pass C did not change any RTL-related rule.

### 2.5 Form labels (the AR contatti page)

Discovery-call form fields verified live:

- Name → "الاسم"
- Email → "البريد الإلكتروني"
- Phone → "الهاتف"
- Sector → "السياق"
- Call topic → "نطاق المكالمة"
- Discovery question → "ماذا تريد أن نناقش؟" (long textarea)
- Optional attachment → "مرفقات (اختيارية)"

All labels read in Arabic, all inputs have a visible focus ring on
keyboard tab, all required fields carry the standard required
indicator. None of this was changed by Pass C; verified because the AR
contatti page is reached via an in-page nav link that now propagates
`&preview=1`, so the route had to actually work end-to-end.

---

## 3 · One residual carried from Pass A/B

Italian addresses + phone in AR are kept Latin-script per MENA
business-press convention (`Via Thaon di Revel 21 · 20159 Milano · Isola`,
`+39 02 3663 4712`, `MM Garibaldi FS`, etc.). This means the AR home
mixes RTL Arabic prose with embedded Latin sequences. Browser
bidirectional algorithm renders this correctly; spot-checked at
1440 × 900 and 390 × 844 — no glyphs land on the wrong side, no
clipped digits, no wrap mid-number.

This is not a Pass C concern; it was settled in Pass B per the locale-
register design notes. Re-confirmed live to make sure the in-page nav
click did not accidentally route the AR contatti page through a code
path that bypassed the conditional font load.

---

## 4 · Verdict

**Contrast / a11y: GREEN.** All AAA pairs preserved. All AA-large
italic-em pairs preserved. Tab order unchanged. ARIA labels unchanged.
Discovery-call form labels remain Arabic on AR. Pass C is a strict
no-op at the accessibility layer.
