# Browser quality gate

The browser walk is the **single source of truth** for whether a template ships. Every test in the suite is a lower bound; only the browser walk is a ship signal. This is not a philosophical preference — it is the lesson the Solaria `e8f38b5` defect taught (1148 lines · 506/506 tests · `generate_previews` succeeded · every heading rendered cream-on-cream). 30 minutes of browser walk caught what ~650 automated checks did not.

This document is short on purpose. The full rubric lives in `factory/standards/corporate-suite-browser-rubric.md`. This file is the orchestrator's gate-discipline, not a re-derivation of the rubric.

---

## 1 · The gate · in one paragraph

A template does not flip from `draft` to `published_live` until: (a) the browser-verifier agent has produced a PASS rubric verdict against the cluster's rubric file, (b) every locale on the rollout list has its own per-locale walk verdict, (c) RTL parity is verified for AR if AR is on the list, (d) the imagery is checked on the live DOM (not just in the pack file), (e) the Pexels-only audit is re-confirmed on the live render, (f) the user has signed off in the parallel-verification handshake, and (g) the gatekeeper has aggregated all of the above into the scorecard and stamped Layer 1 / 2 / 3.

If any of (a)-(g) is missing, the orchestrator does not flip. There is no "we'll catch it post-flip" path.

---

## 2 · Why browser-live · not screenshots · not CI

| Surface | What it can verify | What it cannot |
|---|---|---|
| CLI tests (375/375, 834/834 smoke) | Wire-up correctness · data integrity · render does not exception | Visual hierarchy · contrast on actual paint · imagery placement · motion behaviour · responsive at real viewports |
| `generate_previews` output | Static screenshots are produced | The screenshots themselves are not visually QA'd by the script |
| Screenshots in PR | Hierarchy at one viewport · gross visible defects | Multi-viewport behaviour · interaction · motion · RTL · focus rings |
| Browser-live walk (Playwright MCP + human/agent eye) | Everything the rubric asks · interaction · motion · per-locale text reflow · RTL · imagery on live DOM · Pexels-only on live render | None worth gating on |

The browser walk supersedes the others as the ship signal because the others are necessary but not sufficient. Solaria proved that.

---

## 3 · What the walk must produce

Per `corporate-suite-browser-rubric.md`, the walk produces a structured verdict: PASS · BORDERLINE · FAIL with per-cell evidence (screenshots · DOM snippets · computed styles where contrast is at issue · viewport notes · RTL parity notes for AR).

The orchestrator-side reading rules:

- **PASS** → Commit A draft-landing authorised; LIVE flip authorised after user-handshake.
- **BORDERLINE** → fix pass required; cannot flip. The fix targets the borderline cells specifically; no scope expansion.
- **FAIL** → fix pass required; cannot land draft if fail is `[BLOCKING]` per `corporate-suite-blocking-rules.md`.
- **No verdict on file** → no flip. Period.

A verdict more than 30 days old does not satisfy the gate. Templates that sat at `draft` past 30 days re-walk before flip.

---

## 4 · Per-locale walks for multilingual rollouts

Each locale gets its own walk. This is non-negotiable because:

- Text reflow differs per language (German is longer than English; Arabic uses different metrics; Chinese differs in line-height inheritance).
- The voice anchor's preservation depends on translator interpretation; only a walk catches a corrupted anchor.
- RTL (AR) inverts the layout; logical-property compliance is testable only at runtime in `dir=rtl`.
- Imagery captions in some templates carry locale-specific text; the live walk catches missing translations.

The Solaria Pass B precedent (11/11 captures across IT/EN/FR/ES/AR with 0 fixes mid-walk) is the bar.

The orchestrator does not approve a multilingual rollout until every locale's verdict is on file. It is acceptable to flip a subset (e.g. IT/EN/FR/ES at LIVE while AR remains at draft) if AR specifically failed and the others passed.

---

## 5 · Imagery quality on the live DOM

The pack file's metadata is necessary but not sufficient. The walk re-verifies on the live render:

1. **Pexels-only** — every image URL on the rendered page traces to a Pexels source. No CDN-laundering, no thumbnails embedded from elsewhere. The Pragma legacy exception is the only documented carve-out.
2. **Subject coherence** — the rendered image at the rendered size still reads as the intended subject. Pack metadata can be approved at large resolution; live rendering may crop or scale into incoherence.
3. **Mood coherence** — the image's mood matches the section it sits in. Two coherent images placed in the wrong sections collide.
4. **No stock-collage feel** — single hero photo discipline; no 4-up grids of generic stock unless the cluster pattern explicitly uses them.
5. **Caption / credit policy** — applied per cluster's imagery standard.

Any failure is a `[REQUIRED]` minimum and may be `[BLOCKING]` per the cluster imagery standard.

---

## 6 · The user-handshake

LIVE flip requires the user (Badr) to do a parallel walk and confirm. The orchestrator does not simulate this; it presents the evidence pack and waits.

The evidence pack is:
- The rubric verdict file.
- 6-12 captures per locale, including hero · KPI band · CTA · footer · the section the cluster's standard most often regresses on.
- The scorecard with Layer 1 / 2 / 3 stamped.
- Any deviation notes (`§ deviation`) the gatekeeper logged.
- The Pexels-only confirmation.

The user's handshake is a binary: ship or hold. The orchestrator does not negotiate the gate; it carries the request and the evidence.

---

## 7 · After LIVE · the regression watch

The gate does not end at flip. After LIVE:

- Any subsequent edit pass to the template re-runs the walk on the touched surfaces (workflow B.4).
- Any cluster-wide standards change triggers a re-walk on every published template in the cluster, scheduled before next pass starts.
- A defect reported on a LIVE template is treated as a `[BLOCKING]` regression; the orchestrator opens a workflow B pass and the template stays LIVE only if the defect is `[STRONG]` or lower.

This is the "scalable without losing quality" mechanism. Quality does not degrade with catalog growth because each new template enters the regression-watch surface and each LIVE flip is gated on evidence the previous LIVE flip would also have had to provide.

---

## 8 · What the gate is not

- It is not a substitute for tests. CLI green is a precondition · the gate runs after.
- It is not a stylistic review by a single reviewer. The walk is rubric-bound; the rubric is in `factory/standards/`.
- It is not skippable for hot-fixes. Hot-fixes use workflow B and re-walk the touched surface; they do not bypass.
- It is not negotiable when the calendar is tight. The Solaria precedent stands: missing the gate cost more time than running it would have.
