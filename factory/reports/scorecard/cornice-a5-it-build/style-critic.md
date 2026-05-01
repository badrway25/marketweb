# Style-critic panel · Cornice A.5 IT build

```yaml
panel:           style-critic
template_slug:   cornice-architettura
phase:           X.5 · A.5 build
date:            2026-05-01
verdict:         PASS
score:           4.7/5
```

## LF-2 row verification (binding from `factory/reports/hardening/corporate-suite-layout-family-matrix.md §1`)

| Slot | Declared | Rendered | Status |
|---|---|---|---|
| L1 hero | stacked-editorial | full-bleed photo TOP + 8/4 split BELOW (h1 LEFT + side-quote RIGHT) | MATCH |
| L2 sequence | B (hero, narrative, sectors-ribbon, leadership-single, cases-magazine, cta-closer-cream) | confirmed in DOM | MATCH |
| L3 mid-strip | absent | no cs-cycle / cs-kpi-band / cs-trust mid-strip rendered | MATCH |
| L4 essay-with-anchors | drop-cap + 3 pull-quotes + side-rail | rendered with rust 84px drop-cap "L" + 3 italic pull-quotes (`prima` / `autore` / `regola`) + 4-link side-rail | MATCH |
| L5 hero-overlay | KPI tuple INSIDE photo overlay | 47/18/6 tuple bottom-left of photo · NO separate cs-kpi-band on home | MATCH |
| L6 single-portrait-feature | ONE founding-architect masthead | 2-col grid: large environmental portrait LEFT + h2+role+bio+credentials RIGHT | MATCH |
| L7 magazine-grid | 3+1 (1 hero card + 3 small) | 2-col CSS grid: hero card spans rows 1-3 LEFT + 3 small cards stacked RIGHT, photos + eyebrow + h3 + body + pill | MATCH |
| L8 split-wordmark-top | "CORNICE / studio di architettura" | rendered on cream nav with letter-spacing 0.18em uppercase + Source Sans 11px subtitle | MATCH |
| L9 4-col-with-whistleblowing | 4 cols on graphite footer with channel column | rendered: brand + sitemap + contact + segnalazioni column with D.lgs. 24/2023 paragraph + email link | MATCH |

**9/9 slots match the planner-declared LF-2 row.**

## CS rule audit

| Rule | Status | Evidence |
|---|---|---|
| CS-PAL-01 (cream-safe primary L\* ≤ 40) | PASS | `--primary: #1F2226` graphite · L\* ≈ 12 · cream-safe |
| CS-PAL-03 (no `--primary-2: #2c3e6b` hardcoded) | PASS | no occurrences in content module or skin |
| CS-PAL-04 (on-dark family on dark surfaces) | PASS | inherited via `_base.html` cluster rule |
| CS-PAL-05 (≤3 accent hits per viewport) | PASS | rust touchpoints: nav CTA + drop-cap + magazine card numerals + cta-closer button + focus ring + pull-quote em — but they NEVER co-render in a single viewport (nav top · drop-cap mid-page · CTA closer bottom) |
| CS-TYPE-02 (one italic em per heading) | PASS | 12/12 surfaces verified · single em-word each |
| CS-TYPE-03 (tabular-nums on figures) | PASS | hero KPI tuple uses `font-variant-numeric: tabular-nums` |
| CS-TYPE-04 (heading-scale tokens) | PASS | uses cluster `--fs-hero` 64px / `--fs-h2` 48px / `--fs-h3` 26px |
| CS-TYPE-05 (eyebrow tracking 0.22em uppercase) | PASS | all eyebrows at 0.22em uppercase letter-spacing |
| CS-RHYTHM-01 (max-width 1400 + padding 100×72) | PASS | `_base.html` tokens consumed; LF-2 sections use `--space-section-y` and `--space-section-x` |
| CS-RHYTHM-04 (no two adjacent sections share function) | PASS | hero (position) → narrative (essay) → sectors (typology-list) → leadership (single-portrait) → cases (case-studies) → closer — every adjacent pair functionally distinct |
| CS-DENSITY-02 (pillar count) | PASS | LF-2 has 0 pillars · narrative essay replaces them |
| CS-DENSITY-04 (KPI ≤3 figures) | PASS | hero overlay KPI: 47/18/6 = 3 figures · within cap |
| CS-DENSITY-05 (cases ≤4 on home) | PASS | magazine grid ships 4 cards (1 hero + 3 small) |
| CS-DENSITY-07 (paragraph max-width 64ch) | PASS | narrative `.body` `max-width: 64ch` |
| CS-COMP-04 (hero density) | PASS | hero ships 66w (target 60w · +6 within tolerance per copy-authoring §6.1) |
| CS-COMP-06 (no wall-of-text opener) | PASS | hero opens with photo + 8/4 split · about-page opens with feature shot |
| CS-IMG-SRC-01 (Pexels-only) | PASS | all 6 primary slots + 4 magazine extras on Pexels |
| CS-IMG-POOL-01 (canonical 6-slot shape) | PASS | `business-architecture` pool ships [hero, feature, portrait, portrait, detail, ambient] |
| CS-IMG-RHYTHM-01 (typographic / photographic alternation) | PASS | hero (photo) → narrative (typographic) → sectors-ribbon (typographic) → leadership-single (photo) → magazine grid (photo) → cta-closer-cream (typographic) |
| CS-NAV-02 (4-state cascade + focus ring) | PASS | inherited; LF-2 nav-cta uses rust focus ring `outline: 2px solid var(--accent); offset: 4px` |
| CS-NAV-03 (locale switcher pill) | PASS | inherited from mp-bar; 5 pill links present |
| CS-FOOT-02 (whistleblowing legal row + column) | PASS | 4-col-with-whistleblowing footer ships D.lgs. 24/2023 column · legal row also references whistleblowing |
| CS-CTA-01 (outline-on-cream + filled-on-dark polarity) | PASS · with LF-2-specific inversion | LF-2 declares zero dark band → cta-closer is FILLED rust on cream (inversion is documented in CS-CTA-01 ratification 2026-04-26 · the closer's filled-rust button on cream + hairline-bordered band is the LF-2 polarity exception) |
| CS-CTA-02 (banlist) | PASS | "Apri un fascicolo progetto" not banned · "Get started free" / "Iscriviti gratis" / "Fissa una call privata" / "Primo appuntamento" / "Prenota una discovery call" / "Avvia un dialogo di mandato" all ABSENT |
| CS-EXEC-04 (hyperbole banlist) | PASS | "trasforma · sblocca · rivoluziona · disrupt" ABSENT · cta-closer's closing line explicitly negates 4 sibling-CTA framings |
| CS-MARKET-01 (editor click-to-edit guard) | PASS | inherited from `body.mw-is-editor-preview` cluster guard |

## Family-level demotions (declared, not silent)

LF-2 demotes 5 cluster invariants at the family level per `factory/reports/hardening/corporate-suite-layout-divergence-plan.md §3`:

| Cluster invariant | LF-2 declares |
|---|---|
| CS-HERO-01 (55/45 hero) | stacked-editorial |
| CS-TONE-03 (one dark band on home) | zero dark bands on home |
| CS-RHYTHM-02 (sequence A) | sequence B |
| CS-NAV-01 (sticky-top primary-bg) | split-wordmark on cream |
| CS-FOOT-01 (3-col footer) | 4-col-with-whistleblowing |

All 5 demotions verified rendered as declared. Style-critic does NOT flag absence of dark band, absence of pillars, absence of cs-kpi-band, or cream nav as a regression — these are family-level deviations not silent breaks.

## Minor concern (the 0.3 score deduction)

- The cream nav's hamburger drawer (≤880px) hides the trailing rust CTA pill until the burger is opened, since the CTA is wrapped in the same `.phone` element class that the cluster's responsive rule hides. At 880px the home's first scroll loses the rust nav-CTA touchpoint. This may be acceptable (the burger drawer's expanded state shows the CTA), but it's worth a UX call: the LF-2 family could consider keeping the nav CTA visible at 880 by giving it its own visibility token. Decision deferred to workflow D pre-flip; not blocking the IT pass.

## Score: 4.7/5

LF-2 row verified at every slot · cluster invariants either honoured or family-level-demoted explicitly · all banlists clean · style-critic recommendations narrow.
