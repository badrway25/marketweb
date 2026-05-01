# Cornice · A.6 IT review-lock · Style-critic panel

```yaml
panel:    style-critic
phase:    A.6 review-lock (IT-only)
date:     2026-05-01
score:    4.85 / 5
floor:    4.5
verdict:  PASS
```

## §1 · LF-2 layout declaration verification (post-fix)

| Slot | LF-2 declared | Live render verdict |
|---|---|---|
| L1 hero | stacked-editorial (full-bleed photo top, 8/4 split below) | PASS — photo is full-bleed, KPI + credit overlay inside photo's bottom-left, 8/4 split below has h1 LEFT (with rust em on `argomento`) and side-quote RIGHT (with rust em on `argomenta`) |
| L2 sequence | B = `[hero, narrative, sectors-ribbon, leadership-single, cases-magazine, cta-closer-cream]` | PASS — DOM section order matches verbatim |
| L3 mid-strip | absent | PASS — zero `cs-cycle` / `cs-kpi-band` / `cs-trust` mid-strip |
| L4 essay-with-anchors | rust drop-cap + 3 pull-quotes + sticky 4-link side-rail | PASS — drop-cap "L" Cormorant 84px in rust on para 1; 3 pull-quotes intersperse with em-words on `prima · autore · regola`; side-rail anchors `Lo studio · Servizi · Progetti · Contatti` are sticky |
| L5 hero-overlay | KPI tuple lives inside photo's bottom-left overlay | PASS — `47 PROGETTI / 18 ANNI / 6 CITTÀ` sits inside photo overlay; CS-TONE-03 demoted at family level (zero dark band on home — verified live) |
| L6 single-portrait-feature | ONE founding architect, environmental NOT headshot | PASS — F1 fix landed; single portrait reads Marta Roveri at her studio drafting table (senior, white hair, glasses, suit jacket, holding coffee, drawings on desk) — environmental, NOT LinkedIn |
| L7 magazine-grid | 3+1 grid with hero card on left + 3 small stacked on right | PASS — F3 fix landed; hero card photo now ~720px tall dominates the spread; right column stacks card 02 / 03 / 04 normally; card foots align at y=7461 |
| L8 split-wordmark-top | cream nav, line 1 = CORNICE, line 2 = studio di architettura | PASS — F2 fix landed; cream nav consistent across home + 8 inner pages; split wordmark renders on every page |
| L9 4-col-with-whistleblowing | STUDIO + PAGINE + CONTATTI + SEGNALAZIONI columns | PASS — 4 columns render on every LF-2 page; SEGNALAZIONI has D.lgs. 24/2023 channel name + email + linked policy |

**9/9 LF-2 cells verified live.**

## §2 · CS rule audit (CS-TYPE-02, CS-PAL-05, CS-TONE-03, CS-NAV-01, CS-FOOT-01)

| Rule | Verdict |
|---|---|
| CS-TYPE-02 single em per heading | PASS — 12 italic em occurrences on home; each on a distinct heading/quote; rust polarity consistent; em on `Roveri` (surname) preserved through F1 rename |
| CS-PAL-05 one accent per chrome | PASS — chrome's only filled-rust element is the cs-nav-cta--lf2 button; consistent across all 9 pages now (was inconsistent pre-F2) |
| CS-TONE-03 dark KPI band | DEMOTED at LF-2 family level (declared in intake §4 + planner-brief §6) — verified zero dark sections on Cornice home |
| CS-NAV-01 sticky-top primary-bg nav | DEMOTED at LF-2 family level — replaced with cream-paper masthead chrome (now consistent across all 9 pages post-F2) |
| CS-FOOT-01 standard 3-col footer | DEMOTED at LF-2 family level — replaced with 4-col-with-whistleblowing (shared with LF-5; column-content sub-cluster-specific) |
| CS-NAV-04 one accent CTA per nav | PASS — single filled-rust CTA in cs-nav-cta--lf2 |
| CS-IMG-SRC-01 Pexels-only | PASS — all 6 business-architecture pool URLs are Pexels CDN |
| CS-EXEC-04 hyperbole banlist | PASS — `trasforma · sblocca · rivoluziona · disrupt` all ABSENT from Cornice copy |
| Sibling-anchor banlist | PASS — Pragma's `Fissa una call privata`, Fiscus's `Primo appuntamento`, Solaria's `Prenota una discovery call`, Continua's `Avvia un dialogo di mandato` all ABSENT; Cornice's `Apri un fascicolo progetto` is fresh + architectural |

## §3 · Voice + content fidelity (post-fix · cross-checked against copy authoring)

**Voice anchor verbatim**:

- Hero h1: `Ogni progetto è un <em>argomento</em> costruito, non un servizio reso.` ✓
- CTA-closer h2: same ✓ (verbatim recurrence)

**Curatorial-architectural register first 30s** (Risk C-1 mitigation):

- Eyebrow: `STUDIO DI ARCHITETTURA · MILANO · DAL 2008`
- H1: `Ogni progetto è un argomento costruito, non un servizio reso.`
- Subhead: `Studio di architettura editoriale · committenze pubbliche e private · novanta fascicoli aperti dal 2008.`
- Side-quote: `L'architettura buona si argomenta — non si dimostra, non si vende, non si decora.`
- KPI labels: `47 PROGETTI REALIZZATI / 18 ANNI DI PRATICA / 6 CITTÀ ITALIANE`
- Credit: `BOLOGNA · PORTICO RESTAURATO · 2023 · fascicolo n. 31`

11+ Tier 1/2 architectural-vocabulary hits in the first viewport
at 1440. The narrative drop-cap paragraph 1 surfaces 14 more.
Cluster-vocabulary mitigation (Risk C-1) holds.

## §4 · Founder masthead post-F1 (Risk 4 re-audit)

The leadership masthead is the LF-2 L6 load-bearing cell. Risk 4
("LF-2 single-portrait stock-headshot collapse") needed a binding
triple at A.5: senior-or-50s + drafting-tools-mid-ground +
environmental-NOT-studio-backdrop. The chosen RDNE Stock 5915290
photo cleared all three. A.5 also bound a 4-credential list
(OAPPC + CNAPPC + MIBAC + Politecnico Professore a contratto)
beside the bio to reinforce the editorial portrait register.

A.6 added the missing fourth binding: **founder identity matches
photo gender**. Pre-F1 the photo and copy disagreed; post-F1 the
masthead reads unified:

- Eyebrow: `STUDIO FOUNDER · ARCHITETTA`
- H2: `Marta <em>Roveri</em>` (rust em on Roveri)
- Role: `fondatrice · responsabile editoriale dei fascicoli`
- Bio para 1: `Marta Roveri ha aperto Cornice nel 2008, dopo dieci anni di pratica tra Milano e Bologna in due studi di restauro pubblico. Si è formata al Politecnico di Milano sotto la cattedra di restauro architettonico, con un periodo di ricerca all'École Polytechnique de Lausanne sui caratteri stereotomici delle volte in pietra. Lavora a tempo pieno sui progetti dello studio: dirige il rilievo, scrive l'argomento del fascicolo, segue il cantiere fino al collaudo, e cura la collana monografica che pubblica le opere realizzate.`
- 4 credentials: `Albo OAPPC · CNAPPC · MIBAC qualifica restauro · Politecnico di Milano · Professoressa a contratto · Cattedra di Restauro`

Risk 4 is now structurally tighter than at A.5.

## §5 · Magazine-grid editorial spread post-F3

The LF-2 L7 case-shape signature (3+1 magazine grid) is the
distinctness-load-bearing cell that separates Cornice from
Pragma/Fiscus/Solaria's numbered list-row and Continua's vertical
timeline. F3 strengthens the spread by giving the hero card a
dominant lead photo (~720px tall b&w concrete concorso shot vs
~480px pre-fix). The right column's 3 small cards stack normally;
both columns end at the same baseline (y=7461 in DOM).

The visual rhythm now reads as Casabella / Domus magazine spread:
hero photo dominates the spread, body + meta clustered at the
foot of the hero column, right column shows 3 sequential project
tiles (residenziale / restauro / pubblicazione) for typological
breadth.

## Why score = 4.85 / 5

All declared LF-2 cells render to spec. All CS rules clear or
declared-demoted. F1/F2/F3 fixes structurally tighten three of
the most distinctness-critical surfaces (leadership, chrome
consistency, magazine spread). The 0.15 deduction is for the F3
mid-session iteration (margin-top:auto attempt that didn't
ship) — a process cost, not a final-render cost. The shipped
render is 5/5.
