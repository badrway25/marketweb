# Cornice · A.6 IT review-lock · Browser-verifier panel

```yaml
panel:    browser-verifier
phase:    A.6 review-lock (IT-only)
date:     2026-05-01
score:    4.85 / 5
floor:    4.5
verdict:  PASS
tool:     Playwright MCP (mandatory per task constraints)
```

## §1 · Browser walk evidence

| Layer | Walked | Captured |
|---|---|---|
| 9 IT routes pre-fix | yes | 17 captures (`01-cornice-*` to `17-cornice-*` + responsive `r1-r3`) |
| 4 frozen siblings pre-fix | yes (anonymous) | 4 captures (`sib-pragma-pre`, `sib-fiscus-pre`, `sib-solaria-pre`, `sib-continua-pre`) |
| Cornice post-fix walk | yes | 11 captures (`post-01` to `post-11`) including 2 between-fix iteration captures (`post-04` + `post-05`) showing the F3 first-attempt rejected |
| 4 frozen siblings post-fix | yes (anonymous) | 4 captures (`post-sib-*`) |
| Total captures | — | 36 |

## §2 · Server status at hand-back

```
URL prefix:     http://127.0.0.1:8052/
process:        python manage.py runserver 8052 --noreload
state:          running (background bash task)
auth:           cornice_review · is_staff=True · is_superuser=True
session:        active in browser at hand-back (used by user-handshake)
```

The server stays open at port 8052 for the user to perform the
visual handshake.

## §3 · DOM structural verification (post-fix)

Live DOM measurements at 1440:

| Element | Selector | Verified |
|---|---|---|
| Cornice nav class | `nav.cs-nav.cs-nav--lf2` | present on home + all 8 inner pages (grep'd via Playwright) |
| Cream nav background | `.cs-nav.cs-nav--lf2 { background: var(--paper) }` | resolved to #F4F1EC at runtime (from _base.html post-F2) |
| Split wordmark spans | `.wm-line-1` + `.wm-line-2` | rendered on every LF-2 page |
| Filled rust CTA | `.cs-nav-cta--lf2 .cs-nav-cta-btn` | rendered on every LF-2 page |
| Hero overlay | `.cs-hero .photo .overlay` | KPI cluster nested inside photo div |
| Magazine hero card | `.cs-cases-magazine .card--hero` | photo flex:1 + min-height:360px (post-F3) |
| Magazine card foots align | hero-card.bottom === lastSmallCard.bottom | both = y=7461 (DOM-measured) |
| Footer whistleblowing column | `.cs-foot-col--whistleblowing` | rendered on every LF-2 page |

## §4 · Content fidelity verification (post-F1)

| Surface | Live render | Verdict |
|---|---|---|
| Home leadership eyebrow | `STUDIO FOUNDER · ARCHITETTA` | PASS |
| Home leadership h2 | `Marta Roveri` (rust em on Roveri) | PASS |
| Home leadership role | `fondatrice · responsabile editoriale dei fascicoli` | PASS |
| Home leadership bio para 1 | `Marta Roveri ha aperto Cornice... Si è formata al Politecnico...` | PASS |
| Home leadership credentials line 4 | `Politecnico di Milano · Professoressa a contratto · Cattedra di Restauro` | PASS |
| Studio (about) intro | `Milano. Un'architetta fondatrice, due collaboratori, novanta fascicoli aperti.` | PASS |
| Studio history 2008 | `Marta Roveri apre Cornice in via Paoli a Milano...` | PASS |
| Studio history 2014 | `Marta Roveri ottiene la qualifica per il restauro architettonico...` | PASS |
| Studio history 2017 | `Marta Roveri viene nominata Professoressa a contratto...` | PASS |
| Studio team[0] | `Marta Roveri · Studio Founder · Architetta · Fondatrice. Politecnico...` | PASS |
| Studio team[2] junior | `(relatrice: Roveri)` | PASS |
| Servizi card 03 | `Marta Roveri è abilitata al restauro architettonico secondo il D.M. 154/2017.` | PASS |
| Case detail meta `ARCHITETTO REFERENTE` | `Marta Roveri · Studio Founder` | PASS |

Zero "Marco" remnants on the live render (verified via grep on
Cornice source post-edit and via browser snapshot inspection).

## §5 · F1/F2/F3 fix verification (live render)

| Fix | Pre-fix render | Post-fix render | Verdict |
|---|---|---|---|
| F1 founder rename | `STUDIO FOUNDER · ARCHITETTO` + `Marco Roveri` + `Si è formato` + `fondatore` | `STUDIO FOUNDER · ARCHITETTA` + `Marta Roveri` + `Si è formata` + `fondatrice` | PASS |
| F2 cream nav inner pages | studio/servizi/progetti/contatti/case-detail had dark `cs-nav` (LF-1 default) | all 9 pages render cream `cs-nav.cs-nav--lf2` with split wordmark + filled rust CTA + graphite hamburger | PASS |
| F3 magazine grid hero | hero card photo ~480px + visible empty band ~350-450px below pill | hero card photo ~720px + body+meta clustered at foot + card baselines align at y=7461 | PASS |

## §6 · Console + network sanity

Browser console during the walk: zero JS errors related to
Cornice. The marketplace top-bar JS, the Cornice CSS-only nav
toggle, and the Cornice CSS-only hover transitions all work.

Network: all asset requests 200 (Pexels CDN images, Cornice
CSS in the included home stylesheet, base.html chrome CSS).
Catalog `/api/v1/templates/` not invoked during the walk (no
spurious API hits).

## §7 · Pre-fix vs post-fix delta capture pairs

For the user-handshake, here are the recommended diff pairs:

| Surface | Pre-fix | Post-fix |
|---|---|---|
| Leadership masthead | `captures/07-cornice-leadership-1440.png` | `captures/post-03-cornice-leadership-1440.png` |
| Studio (about) page navbar | `captures/13-cornice-studio-1440-vp.png` | `captures/post-08-cornice-studio-1440-vp.png` |
| Servizi page navbar | `captures/14-cornice-servizi-1440-vp.png` | `captures/post-09-cornice-servizi-1440-vp.png` |
| Case detail page navbar | `captures/17-cornice-case-detail-1440-vp.png` | `captures/post-10-cornice-case-detail-1440-vp.png` |
| Magazine grid bottom | `captures/10-cornice-cases-bottom-1440.png` | `captures/post-07-cornice-cases-bottom-1440.png` |

Side-by-side viewing of these pairs is the fastest review path
for the user-handshake.

## Why score = 4.85 / 5

The browser walk used Playwright MCP throughout (mandatory).
36 captures across pre-fix, between-fix iterations, post-fix
Cornice, and post-fix frozen siblings. Live DOM verification
of card-foot alignment (y=7461 for both columns). Voice + content
fidelity grepped on source + verified visually.

The 0.15 deduction is for the F3 between-fix iteration capture
discipline — the iteration captures (`post-04`, `post-05`) show
a configuration that did NOT ship, which a future reader could
mistake for the final state. Mitigated by the explicit
"BETWEEN-FIX" + "NOT shipped" tags in the captures table; could
have been cleaner to discard those captures, but they're useful
for the iteration narrative.
