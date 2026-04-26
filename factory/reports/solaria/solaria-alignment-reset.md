# Solaria · alignment reset

**Date**: 2026-04-26
**Author**: Claude (Opus 4.7), writing honestly and conservatively at the user's explicit request.
**Scope**: Re-anchor the Solaria pass-1 result against the user's original goal. No code changes. Reports only.

This document is intentionally written for a non-technical reader. If a paragraph reads like internal jargon, that's a flag — please point it out and I will rewrite it.

---

## 1 · The original user goal, re-anchored

The user is building a marketplace of premium website templates. The user-level goal is, in plain words:

1. **Scalable production of genuinely new templates** — not weak one-by-one variants of the same template.
2. **Premium output** — elegant, modern, dynamic, professional. Visitors should feel "this is luxury, not stock."
3. **Strong browser-live validation** — every template must look and behave correctly when actually opened in a browser, not only when test suites are green.
4. **Coherent imagery** — photos must match the brand, the cluster, and each other.
5. **Multilingual behaviour parity** — new templates must localize like the previous good ones did (IT/EN/FR/ES/AR, with proper RTL for Arabic).
6. **No drift into meta-process** — the user does not want long sessions that produce reports *about* reports while the visible product barely advances.

Everything below is judged against those 6 anchors.

---

## 2 · What pass-1 actually completed (plain language)

In honest terms:

- The Solaria template (a business-coaching brand based in Milan) was **brought back into the codebase from a paused state**. Its Italian content tree (about 949 lines, 5 pages: home, about-the-coach, services, case studies, contacts) was restored from an earlier paused commit. It was not freshly authored in this pass.
- Solaria was **registered** with the system: added to the seed list, the DNA registry, the content index, the imagery pool, and the template registry JSON file. This is plumbing — necessary, but invisible to a visitor.
- Solaria was **hidden from the public** — it was deliberately seeded as `tier=draft`. That means a normal visitor going to `/templates/business/` does not see it at all. A normal visitor opening the direct URL gets a 404.
- A staff user (`solaria_qa_staff`) was used to view it via a `?preview=1` query string. That is the *only* way Solaria is currently visible. Seven screenshots were captured this way (5 Italian pages on desktop, plus 1 mobile and 1 tablet sample of the home page).
- Under the hood, Solaria is enrolled as the **third template on the same shared chrome** (the "corporate-suite" archetype) already used by Pragma and Fiscus.
- Test suites and build-time checks remained green.

Eight separate scorecard files were also produced in `factory/reports/scorecard/solaria-pass1/` — each one repeating, in agent voice, that pass-1 passed. These are largely paperwork around a small change.

---

## 3 · Technical hardening vs user-visible template completion

This is the most important distinction to draw, because it is where the work and the goal have started to separate.

### Technical hardening (mostly **archetype-level**, not Solaria-specific)
The X.4a hardening rounds (Pragma + Fiscus) added serious safety rails to the corporate-suite chrome:

- A build-time palette gate (cream-as-primary is now refused).
- A build-time imagery gate (only Pexels URLs accepted; old pool grandfathered with a warning).
- Promoted contrast on dark surfaces (nav, KPI band, CTA, footer all now AAA).
- A focus-visible whitelist, a hamburger drawer below 880px, and a horizontal-scroll root guard.

Solaria *inherits* all of this for free. None of it was authored for Solaria.

### Solaria-specific work this pass
Adding up the diff: **about 120 lines of plumbing across 6 existing files, plus restoring 1 content file (~949 lines) from a paused commit**. Solaria's *new* contribution to the product is essentially:

- The Italian content tree (restored, not new),
- A 6-URL Pexels imagery pool registration,
- The dark-warm carbon palette (`#2B2A28 / #C8621A / #8B5A2B`).

### User-visible completion
A real visitor — speaking Italian, English, French, Spanish, or Arabic — would today see **nothing at all** from Solaria. Even an admin only sees the Italian version, with one verified hero photo, on three viewport widths, on five pages. There is no English, French, Spanish, or Arabic version yet. There is no public listing card. There is no full responsive walk. There is no imagery sweep showing every Pexels photo on every page.

**Rough completion against the original "ship a real coaching template" goal**: ~25 %.

---

## 4 · Why a staff/admin-gated preview was used, and is that acceptable here?

### Why it was used
The system has a deliberate two-tier rule (`D-055`): templates have either `tier=published_live` (visible to the public, counted in trust counters, surfaced in `/templates/`, indexed in discovery) or `tier=draft` (hidden, only reachable by a logged-in staff user appending `?preview=1` to the URL).

Pass-1 chose `tier=draft` because flipping to `published_live` would cascade through 6 tests (the public count moves from 21 to 22), would change the homepage trust counter, and would put Solaria in the public catalog and discovery facets. That is a real go-live decision — not something to slip in alongside a content restore.

### Is that acceptable?
**Yes — for draft QA only**, and only if it is genuinely a *first* gated review with a clear path to public visibility within a small number of passes. It is the right tool for "let me look at this internally before exposing it."

It becomes **not acceptable** if it starts to *replace* the real review flow — i.e., if Solaria stays draft-only for many more sessions and the user is asked to keep reviewing it through a staff backdoor instead of seeing it the way a marketplace visitor would. At that point staff-preview becomes a way to dodge the work of public-flip.

**Honest read**: pass-1 is on the acceptable side of that line *today*, but only narrowly. If pass-2 also stays at `tier=draft` and only adds 4 more locale trees (no public flip), the user will reasonably feel that the staff backdoor has become the product surface. That would be a real drift signal.

---

## 5 · Is multilingual support actually implemented yet?

**No. Not for Solaria.**

Concretely:
- Every other shipped corporate-suite template — Pragma, Fiscus, Elevate, etc. — ships **five locales**: IT, EN, FR, ES, AR (with Arabic RTL).
- Solaria currently ships **one locale**: Italian only.
- The pass-1 narrative documents this as `D-102 cadence` (because the original paused commit was IT-only) and says EN/FR/ES/AR is "pass-2 work."
- That framing is internally consistent, but it does mean Solaria is currently **a regression in multilingual completeness compared to every previously-good template**, even though it was billed as inheriting the same archetype.

So: the original goal "multilingual behaviour like previous good templates" is **explicitly not met yet**, and is gated behind future user authorization for pass-2 and pass-3.

---

## 6 · Is Solaria visually/content-wise proven distinct yet?

**Partially. The differentiation is claimed in writing but lightly proven in the browser.**

What is genuinely distinct:
- The **content tree** — Italian copy, voice anchor ("Il coaching non è terapia e non è consulenza"), 5 pages tailored to a coaching practice (executive 1:1, team coaching, gruppo aziendale percorsi), credentials (ICF-PCC + EMCC), method-declared bounded paths.
- The **palette** — warm dark carbon `#2B2A28` + ochre accent `#C8621A` + earth brown `#8B5A2B`, distinct from Pragma's cream-navy-emerald and Fiscus's warm-neutral-blu-notte-gold.
- The **typography pairing** — Fraunces (humanist serif) + Inter, distinct from both siblings.
- The **imagery pool key** — `business-coaching` (6 Pexels URLs), distinct from `business-corporate` (Pragma) and the Fiscus pool.

What is **not yet** distinct in any user-verifiable way:
- The **chrome** (nav bar, footer, CTA block layout, KPI band, page rhythm) is **identical** to Pragma + Fiscus. By design — they share the archetype skin. But that means Solaria's "I look like a coach's site" feeling currently rests entirely on palette + photo + copy — three things that change on the page but cannot change the *structure* of the page.
- Only **1 of the 6 imagery pool photos** was visually verified during pass-1 (the home hero). The other 5 photos were registered in code but never surfaced into a captured screenshot for review.
- **Zero side-by-side visual comparisons** were produced. There is no artifact that lets you open Solaria's home page next to Pragma's home page and Fiscus's home page and feel the difference in 5 seconds. That should exist.
- **Zero non-Italian visual evidence** exists at all.

So the differentiation claim is currently more **textual (in docstrings)** than **demonstrated (in screenshots)**.

---

## 7 · Has the work drifted from the original goal?

**Verdict: PARTIALLY DRIFTED.**

I want to be careful here. Pass-1 is not a failure. The plumbing is correct, the gates pass, the screenshots that exist are clean, the archetype safety contracts hold. By the rules of its own scoping (`R-SOL-1` through `R-SOL-15`, `D-102` cadence), pass-1 did exactly what it set out to do.

But the *user-level* goals are partly satisfied and partly not:

| User goal | Pass-1 result |
|---|---|
| Scalable production of new templates | **Aligned** — pipeline demonstrably absorbs a 3rd enrollee with no archetype edits. |
| Premium / elegant / dynamic | **Unproven** — only 1 hero photo + 7 screenshots in 1 locale. Not enough surface area to feel "premium." |
| Strong browser-live validation | **Partial** — 7 cells PASS, but rubric floor is 120 cells. The walk is a sample, not a corpus. |
| Coherent imagery | **Unproven** — 5 of 6 photos never surfaced into a capture for review. |
| Multilingual like previous templates | **Not met** — IT only vs siblings' 5 locales. |
| No drift into meta-process | **This is the real concern.** Pass-1 produced 8 scorecard files + 1 narrative + 1 browser report + 1 dev-server log + this very file = ~10 reports, ~5000 lines of agent prose, around a single ~120-line plumbing change + a restored content file. The ratio of meta to product is high. |

The user's own confusion is a healthy signal. When the meta-output dwarfs the visible product output, even a "green" pass starts to feel like progress theatre. That is what happened here — not catastrophically, but enough to justify a reset.

---

## 8 · What is done vs not done — plain list

**Done**
- Solaria exists in the database (as a hidden draft).
- Solaria's Italian content (5 pages) renders correctly when a staff user opens the staff preview URL.
- The dark-warm carbon palette passes the build-time palette gate.
- The 6-URL Pexels imagery pool is registered and the home hero loads.
- Test suite stays at 171/171.
- 7 screenshots exist as evidence.

**Not done**
- Solaria is **not visible to any normal visitor**.
- Solaria has **no English, French, Spanish, or Arabic version**.
- Solaria has **no Arabic RTL walk**.
- Solaria has **no full responsive walk** (only 3 viewport widths sampled, only on home).
- Solaria has **no full imagery sweep** (only 1 of 6 pool photos was surfaced).
- Solaria has **no side-by-side comparison vs Pragma or Fiscus** that proves the visitor experience really differs.
- Solaria has **no homepage card / no listing card / no public discoverability**.
- Solaria has **no human visual review** — only Claude's own scorecards.

---

## What we should do next now

A short, user-facing sequence. Three passes only. Each is a piece of visible product, not a piece of paperwork.

**Pass A — Make Solaria look real, end to end, in Italian.**
Walk every Italian page on every breakpoint, surface every imagery-pool photo at least once, produce a single side-by-side visual sheet (Solaria home / Pragma home / Fiscus home) so the user can confirm in 10 seconds that Solaria is genuinely a different template, not a recolor. Output: one easy-to-skim visual review, not eight scorecards.

**Pass B — Localize Solaria like a real template.**
Author EN, FR, ES, and AR content trees at shape-parity with the IT one. Walk each locale, including AR-RTL. The user must be able to open Solaria in any of the 5 languages and see a coherent coaching site. Output: 5 locales × home + one inner page = ~10 visual confirmations the user can review at a glance.

**Pass C — Flip Solaria public, with the cascade properly handled.**
Move `tier` from `draft` to `published_live`, update the public-count cascade tests, surface Solaria in `/templates/`, on the homepage trust counters, and in discovery facets. Walk it once as a real anonymous visitor (not via `?preview=1`) on at least 2 locales. Output: Solaria reachable by any marketplace visitor, indistinguishable in flow from Pragma / Fiscus / Elevate.

After Pass C, Solaria is a real shipped template. Not before.

---

*End of alignment reset. No application code was modified to produce this document.*
