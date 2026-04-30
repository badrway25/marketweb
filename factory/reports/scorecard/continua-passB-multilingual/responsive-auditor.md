# Responsive auditor · Continua Pass B Multilingual · 2026-04-30

## 1 · Scope

LF-5 ships a 5-breakpoint responsive matrix (1920 / 1440 / 1100 / 880 / 720 / 480) inherited from the LF-5 IT rebuild pass 2 (`continua-lf5-it-rebuild.md §7`). Pass B does not change the responsive matrix — the only chrome edit is the additive RTL letter-spacing reset. The audit therefore re-confirms that:

1. The IT-side responsive matrix still passes after the chrome edit (LTR-side regression check).
2. The Arabic responsive matrix passes at the most stress-point viewport (720 mobile RTL).
3. No locale introduces horizontal overflow at any audited viewport.

## 2 · Audited viewports

| Viewport | Locale | Verdict | Capture |
|---|---|---|---|
| 1440×900  | IT | PASS · LF-5 sequence + voice anchor + 5 italic-em + zero overflow | `it-1440-fullpage.png` |
| 1440×900  | EN | PASS · LF-5 sequence + voice anchor + 5 italic-em + zero overflow | `en-1440-fullpage.png` |
| 1440×900  | FR | PASS · LF-5 sequence + voice anchor + 5 italic-em + zero overflow | `fr-1440-fullpage.png` |
| 1440×900  | ES | PASS · LF-5 sequence + voice anchor + 5 italic-em + zero overflow | `es-1440-fullpage.png` |
| 1440×900  | AR | PASS · LF-5 sequence + voice anchor + 5 italic-em + zero overflow + RTL flip | `ar-1440-fullpage.png` |
| 720×1024  | AR | PASS · single-column collapse + RTL hamburger + zero overflow | `ar-720-fullpage.png` |
| 1440×900  | AR (contatti) | PASS · RTL form fields + sidebar offices + footer | `ar-1440-contatti.png` |

7 captures total · all PASS.

## 3 · LTR overflow probe (cross-locale)

For each LTR locale at 1440:

```
{ pageW: 1425, scrollW: 1425, horizontalOverflow: false }
```

For AR at 1440 and 720:

```
1440: { pageW: 1425, scrollW: 1425, horizontalOverflow: false }
 720: { pageW: 705,  scrollW: 705,  horizontalOverflow: false }
```

The 15px delta (1440 → 1425, 720 → 705) is the OS scrollbar gutter, not a content overflow. **Zero horizontal overflow on any locale at any audited viewport.**

## 4 · LF-5 responsive matrix re-validation (LTR side)

Per the LF-5 IT rebuild §7 Browser walk:
- ≤ 1280 hero meta-strip eases padding, frame columns 1.2/1
- ≤ 1100 frame stacks (anchor above body), pillars 1-col, cases-preview rail collapses
- ≤ 880 pillar matrix collapses to 1-col, cycle stacks, hero credit-row stacks vertically
- ≤ 720 hero shows photo + plate without side credits, KPI 2x2, leadership 1-col, timeline single-axis
- ≤ 480 minimum spacing, hero h1 ≥ 32 px floor, photo ratio 4:5

The Pass B chrome edit (CS-TYPE-05 RTL reset extended) is RTL-scoped only (`html[dir="rtl"]` selector), so the LTR responsive matrix is byte-equivalent before and after. Confirmed by re-rendering IT/EN/FR/ES at 1440 post-fix and observing no visual regression.

## 5 · AR responsive matrix at 720

The AR mobile capture (`ar-720-fullpage.png`) shows:

- Hamburger nav drawer engaged at ≤880 (cluster-default · CS-NAV-08)
- Hero photo at 4:5 aspect ratio with credit-row stacked vertically
- Hero h1 floor maintained at ≥ 32px (Noto Kufi Arabic at 32px+ holds legibility)
- Cycle section single-column, three cells stacked
- Pillars matrix collapsed to 1-col with each pillar's icon + title + body legible
- KPI band 2x2 grid with Latin numerals (18 / 3 / € 1.8 B / 4) preserved
- Sectors ribbon flowing right-to-left
- Leadership 3-card collapsed to 1-col
- Timeline single-axis with year + title + horizon stacked
- Dark CTA closer with em on `بالأجيال` visible
- Footer 4-col collapsed to single-col with whistleblowing column reachable

No content lost, no overflow, no clipping.

## 6 · AR contact form RTL flow

The AR contatti capture (`ar-1440-contatti.png`) shows:

- 9 form fields with Arabic labels right-aligned
- Helper text right-flowing under each field
- Form sections organized in 4 numbered blocks (المرجع · العائلة · تفويض الحفظ · مرفقات)
- Sidebar offices (Milano · Lugano · Luxembourg) flowing RTL with Latin city names + Arabic role tags
- Direct channels list with Arabic labels and Latin email/phone preserved
- Form submit button with arrow flipped (`←` instead of `→` per `_base.html` line 685)
- Whistleblowing channel surfaced as the third channel in the direct-channels list

No form field collision, no overlapping labels, no broken right-alignment.

## 7 · Verdict

Responsive auditor GREEN across all 5 locales at 1440 and on AR at 720 + AR-contatti. The Pass B chrome edit is byte-equivalent on the LTR side (RTL-scoped only). The Arabic responsive matrix collapses correctly at every audited viewport.
