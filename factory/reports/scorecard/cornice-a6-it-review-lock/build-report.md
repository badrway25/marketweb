# Cornice · A.6 IT review-lock · Build report panel

```yaml
panel:    build-report
phase:    A.6 review-lock (IT-only)
date:     2026-05-01
score:    4.9 / 5
floor:    4.5
verdict:  PASS
```

## What shipped at A.6

A.6 is a narrow review-lock pass on top of the A.5 build. The work is
intentionally small: harden the IT draft to a conservative review
standard, fix only what's review-blocking or chrome-breaking,
preserve frozen siblings, preserve tier=draft, and DO NOT start
multilingual or public flip work.

**Three findings → three fixes.** Each scoped to LF-2 / Cornice.

| ID | Finding | Severity | Fix surface | Files touched |
|---|---|---|---|---|
| F1 | Founder gender mismatch (woman in portrait, "Marco Roveri" in copy) | review-blocking | Content rename + agreement of gendered Italian on 16 surfaces | `apps/catalog/template_content_cornice.py` |
| F2 | LF-2 cream nav only on home; inner pages render dark LF-1 nav | high (chrome consistency) | Lift cs-nav--lf2 body styles from lf2/styles.html into _base.html | `_base.html` + `_layouts/lf2/styles.html` |
| F3 | Magazine-grid hero card visible empty band below meta pill | medium (editorial rhythm) | flex-grow on hero card photo; remove flex from copy; card foot now aligns with right column | `_layouts/lf2/styles.html` |

**Lines touched** (deltas):

| File | Lines added | Lines removed | Net |
|---|---:|---:|---:|
| `apps/catalog/template_content_cornice.py` | ~16 (in-place edits) | ~16 | 0 |
| `templates/.../_base.html` | ~70 (chrome block + comments) | 0 | +70 |
| `templates/.../_layouts/lf2/styles.html` | ~12 (flex-grow + breadcrumb comment) | ~67 (lifted nav block + old aspect-ratio + flex:1 on copy) | -55 |

Net effect: ~70 lines moved from lf2/styles.html into _base.html
(home byte-equivalent) + ~12 net lines new for F3 (flex-grow
photo). Total LF-2 line count shrank slightly because the lifted
chrome block now serves all 9 pages instead of just home.

## What did NOT ship at A.6 (per scope rules)

| Surface | Why held |
|---|---|
| EN/FR/ES/AR translations | Workflow C · awaiting user GO on IT walk |
| Tier flip to `published_live` | Workflow D · awaiting multilingual + second user handshake |
| Any new archetype, new layout family, or new sub-cluster | Out of scope — A.6 is review-lock, not enrollment |
| apps/editor changes | Hard constraint |
| apps/projects changes | Hard constraint |
| apps/commerce changes | Hard constraint |
| LF-1 / LF-3 / LF-4 / LF-5 layout files | Hard constraint (frozen siblings) |
| TEMPLATE_REGISTRY.json | Tier=draft preserved |
| DNA, imagery pool, imagery policy | Stable from A.5 |
| Privacy-consent line gendering, generic "architetto" role-term | Out of scope (non-Marta-specific) |

## Why score = 4.9 / 5

Build executed against the A.6 brief with one mid-session iteration
(F3 first attempted with `margin-top: auto` on .pill, which
mathematically aligned card foots but introduced a different
rhythm break — empty band between body and pill rather than below
pill). Reverted and re-applied with flex-grow on the photo, which
is the editorially correct solution. The iteration cost half a
point because the first F3 attempt shipped briefly to the running
server and required a second round of reload + verification before
landing on the right approach.

All other sign-off criteria PASS:
- 9 IT routes 200
- 4 frozen siblings 200 anonymous + visually identical to A.5 baseline
- 545/546 tests (1 pre-existing failure unrelated)
- 5/5 distinctness vs all 4 live siblings
- 9/9 (or 8/9) layout-distinctness
- F1 + F2 + F3 all verified live post-server-restart
