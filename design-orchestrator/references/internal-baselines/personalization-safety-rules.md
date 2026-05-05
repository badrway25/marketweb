# Personalization safety rules

```yaml
file_type:    internal-baseline · rule book · enforcement document
status:       v1 · paper-only · binding once committed (Phase X.7c
                implementation pass adopts these as `[REQUIRED]` /
                `[BLOCKING]` rules in the per-cluster + per-archetype
                design standards)
date:         2026-05-05
authority:    orchestrator-side · binding for every project fork, save,
                publish, and template authoring pass
audience:     editor-team at every X.7c slice · style-critic at A.6 ·
                browser-verifier at workflow C/D · release-gatekeeper at
                customer-side publish · product-owner when reviewing UX
                proposals for editor extensions
purpose:      define WHEN a personalization control may be added, WHEN it
                requires escalation, WHAT triggers a refusal, and HOW the
                preview-verification gate fires
companion:    factory/reports/hardening/template-personalization-
                architecture.md (the system design)
              design-orchestrator/references/internal-baselines/
                personalization-control-surface-map.md (the control catalog
                with 17 surfaces × 4-layer assignment)
              factory/reports/hardening/premium-dynamic-pattern-library.md
                (motion patterns whose `personalization_knobs` map here)
              design-orchestrator/references/internal-baselines/
                dynamic-pattern-usage-rules.md (sister rule book for motion
                · USAGE-PERSONAL-* binding · this rule book extends with
                non-motion personalization)
              factory/standards/corporate-suite-{design-standard,blocking-
                rules,quality-scorecard}.md (cluster contract)
              apps/projects/models.py (ProjectDesignTokens · CURATED_FONTS
                whitelist already shipped)
```

## §0 · Severity ladder (binding · same as the existing CS-* rule book)

| Tier | Meaning | Where it gates |
|---|---|---|
| **[BLOCKING]** | save-blocker · publish-blocker · no waiver without § decision | every save · every publish · every template-fork |
| **[REQUIRED]** | publish-blocker · save-block iff savable state would publish broken · waiver only with § decision in design-standard | every save (with publish gate) |
| **[STRONG]** | warning surfaced to customer · save proceeds · publish proceeds with audit log entry | preview-verification stage |
| **[GUIDELINE]** | preference · documented for orchestrator-side guidance | architecture annotation only |

---

## §1 · Cluster + family invariants (every customer · every project · every save)

These hold across every cluster, every layout family, every template, every
project, every save. A change that violates any of them is rejected
immediately at the editor.

### PERSONAL-INV-01 [BLOCKING] · Project's source archetype is immutable
- The `CustomerProject.source_archetype` field is set at fork time and
  cannot be changed. A customer cannot migrate their project from Pragma
  to Cornice without forking a fresh project.
- **Failure mode**: customer projects accumulate state from multiple
  archetypes · renderer cannot dispatch correctly.
- **Evidence**: `CustomerProject.source_archetype` is `CharField` with no
  edit endpoint. Save validation rejects any payload that mutates it.

### PERSONAL-INV-02 [BLOCKING] · Voice-anchor recurrence preserved
- The voice-anchor sentence (CS-EXEC-01) appears verbatim on hero h1 + CTA
  closer h2 (corporate-suite cluster invariant; LF-5 widens to 3 surfaces).
  The customer can edit copy AROUND the anchor; the anchor sentence itself
  is system-locked at the cluster's declared sentence per the template's
  language locale.
- **Failure mode**: customer edits h1 to "Welcome to our firm" — voice
  anchor lost · cluster identity collapses.
- **Evidence**: regex check at save · the configured anchor sentence must
  appear verbatim within the rendered home h1. If not, save is blocked
  with the message: "The phrase '{anchor}' must appear in the hero
  heading. This phrase carries this template's identity across translations."

### PERSONAL-INV-03 [BLOCKING] · Layout family L1–L9 cells are non-editable
- The customer cannot change hero geometry (L1) · section sequence (L2)
  · mid-strip slot (L3) · pillars treatment (L4) · KPI placement (L5) ·
  leadership presence (L6) · cases-preview shape (L7) · navbar geometry
  (L8) · footer structure (L9). These are family-determined per CS-LAYOUT-*.
- **Failure mode**: customer breaks family identity · cluster contract collapses.
- **Evidence**: editor never offers a knob for these cells; backend save
  refuses any payload trying to mutate the layout-family field on
  `WebTemplate` or any L-cell-derived field.

### PERSONAL-INV-04 [BLOCKING] · Pexels-only imagery (CS-IMG-SRC-01)
- New imagery comes from one of: (a) the template's preset pool · (b)
  customer upload via `ProjectAsset` · (c) explicitly listed alternate
  Pexels URL from the catalog. NEVER a free Unsplash URL · free CDN
  paste · AI-generated.
- Pragma's legacy `business-corporate` Unsplash pool is grandfathered
  (W001) but the customer cannot ADD new Unsplash URLs · only existing
  pool URLs are available.
- **Failure mode**: customer wires unlicensed photo · brand integrity
  collapse · legal exposure.
- **Evidence**: save payload validation refuses any URL not on
  whitelisted source list (Pexels CDN · the project's `ProjectAsset`
  pool · grandfathered legacy paths).

### PERSONAL-INV-05 [BLOCKING] · D.lgs. 24/2023 whistleblowing column not removable
- For clusters/locales where compliance applies (corporate-suite forensic
  · stewardship · architectural · audit-led methodology · medical), the
  whistleblowing footer column cannot be hidden by customer.
- **Failure mode**: legal compliance violation surfaces at customer-published
  page.
- **Evidence**: editor does not offer a hide-toggle for the column when
  `WebTemplate.requires_whistleblowing` is true. Backend rejects payload
  attempting to disable.

### PERSONAL-INV-06 [BLOCKING] · `prefers-reduced-motion` always wins
- Per `dynamic-pattern-usage-rules.md USAGE-PERSONAL-01`. The customer
  cannot ship a project that disables reduced-motion fallback. Even if
  the customer picks "expressive" motion intensity, every animation
  retains its reduced-motion equivalent.
- **Failure mode**: motion-sensitive visitor cannot use the customer's
  site.
- **Evidence**: browser-verifier at customer-side publish emulates
  `prefers-reduced-motion: reduce` and confirms fallbacks fire.

### PERSONAL-INV-07 [BLOCKING] · Latin wordmark + Latin numerics in RTL
- For AR locale (and any future RTL locale), the wordmark stays Latin
  (CS-NAV-06) and KPI numerics stay Western Arabic 0-9 (CS-FOOT-03). The
  customer can edit the wordmark text but cannot translate it AR-script.
  KPI numerics auto-render Latin even when Arabic-Indic numerals would
  otherwise apply.
- **Failure mode**: brand fragmentation across locales.
- **Evidence**: save validation enforces. Renderer auto-substitutes.

### PERSONAL-INV-08 [BLOCKING] · `:focus-visible` gold ring never removable
- Per CS-NAV-02. The accessibility focus ring (2px outline · 4px offset
  · accent color · static) is enforced regardless of customer preference.
- **Failure mode**: keyboard accessibility regression.
- **Evidence**: editor does not offer a "disable focus ring" toggle. CSS
  is rendered from cluster baseline.

### PERSONAL-INV-09 [BLOCKING] · About + Contact pages always present
- The customer cannot delete the About page or the Contact page. They
  can edit copy on both.
- **Failure mode**: site missing required pages · trust-signal loss ·
  legal-info-display loss.
- **Evidence**: editor does not surface a "delete page" affordance for
  these two routes. Backend rejects any payload setting their visibility
  to false.

### PERSONAL-INV-10 [REQUIRED] · Minimum 4 sections on home
- A home page must render at least 4 distinct `cs-*` sections. The
  customer can hide individual optional sections but cannot reduce the
  home to a hero-and-CTA collapse.
- **Failure mode**: home looks unfinished · perceived quality crash.
- **Evidence**: save validation counts visible sections post-customization.
  If <4, save is blocked with the message: "Your home page would have
  fewer than 4 sections, which makes it look unfinished. Re-enable a
  section."

---

## §2 · Layer A enforcement rules

These rules say "the editor never offers this knob." A breach happens
only if a future X.7c slice accidentally surfaces a Layer A field. The
review at slice-design time gates this.

### PERSONAL-A-01 [BLOCKING] · No knob for L1–L9 cells
- Per PERSONAL-INV-03. No layout-family cell is exposed.

### PERSONAL-A-02 [BLOCKING] · No knob for cluster identity
- The editor does not surface a "change cluster" or "change archetype"
  knob.

### PERSONAL-A-03 [BLOCKING] · No knob for voice-anchor sentence
- The customer can edit copy but the anchor sentence is template-locked
  per locale per cluster (CS-EXEC-01). Surfacing an editor for it would
  break PERSONAL-INV-02.

### PERSONAL-A-04 [BLOCKING] · No knob for whistleblowing column visibility
- Per PERSONAL-INV-05.

### PERSONAL-A-05 [BLOCKING] · No knob for `prefers-reduced-motion` override
- Per PERSONAL-INV-06.

### PERSONAL-A-06 [BLOCKING] · No knob for nav background polarity
- Per CS-PAL-06 + CS-NAV-01 + PERSONAL-INV-08. The nav uses primary-bg
  OR family-cream variant.

### PERSONAL-A-07 [BLOCKING] · No knob for typography heading scale
- Per CS-TYPE-04. Heading scales (h1 44-72 · h2 32-48 · h3 22-28 · drop-cap
  84) are template-locked.

### PERSONAL-A-08 [BLOCKING] · No knob for letter-spacing
- Per CS-TYPE-05. Eyebrow tracking 0.22em · body tracking 0 · RTL resets
  to 0.

### PERSONAL-A-09 [BLOCKING] · No knob for 100×72 padding · 1400px max-width
- Per CS-RHYTHM-01. Density preset (CS-13) shifts WITHIN the rhythm; the
  rhythm itself is locked.

### PERSONAL-A-10 [BLOCKING] · No knob for accent budget ≤3 hits per viewport
- Per CS-PAL-05. The customer's palette and accent placement are validated
  at preset-authoring time so this rule holds; but no knob "show 5 accent
  hits" is exposed.

---

## §3 · Layer D ban list (banned freeform controls · permanent)

Each ban here is a [BLOCKING] rule. A future pass that proposes lifting any
of these requires a § decision at the standards level, accompanied by:
- Why the ban was originally erected.
- Why current circumstances justify lifting.
- What replacement constraint enforcement is shipped (i.e., the same
  protection achieved a different way).

### PERSONAL-D-01 [BLOCKING] · No free hex color picker
- **Why banned**: customer can pick `#FFD700` primary on cream paper.
  CS-PAL-01 violation invisible to them.
- **Detector**: any field of type "hex string" with no enum constraint.
- **Replacement**: Layer B palette preset picker · per cluster · 5-7 options.
- **Evidence**: code review at slice-design.

### PERSONAL-D-02 [BLOCKING] · No free font name input
- **Why banned**: customer picks "Comic Sans" or arbitrary Google font ·
  CS-TYPE-01 + CURATED_FONTS bypass.
- **Detector**: any field of type "string" attached to font.
- **Replacement**: Layer B font-pair preset picker per cluster.

### PERSONAL-D-03 [BLOCKING] · No drag-and-drop section reorderer
- **Why banned**: customer moves CTA to slot-1 · breaks CS-RHYTHM-02 ·
  cluster section-rhythm collapses.
- **Detector**: any UI surface allowing reorder of cs-* sections.
- **Replacement**: section reorder happens at family-authoring time · NOT
  customer-side.

### PERSONAL-D-04 [BLOCKING] · No custom CSS injection
- **Why banned**: bypasses every cluster contract simultaneously.
- **Detector**: any text input that flows into rendered HTML/CSS without
  sanitization.
- **Replacement**: customer injects nothing into CSS.

### PERSONAL-D-05 [BLOCKING] · No motion-curve free editor
- **Why banned**: customer picks 50ms slot-machine timings or 5000ms loading
  reveals.
- **Detector**: any timing-input field with no enum.
- **Replacement**: Layer B `motion_profile` master + Layer C per-pattern
  toggle. Every duration is enum-bound.

### PERSONAL-D-06 [BLOCKING] · No free imagery URL paste
- **Why banned**: bypasses CS-IMG-SRC-01.
- **Detector**: text-input field for image-URL in editor.
- **Replacement**: Layer C upload via `ProjectAsset` OR Layer B preset pool.

### PERSONAL-D-07 [BLOCKING] · No cluster/family change after fork
- **Why banned**: PERSONAL-INV-01 binding.
- **Detector**: editable `source_archetype` field in admin/UI.
- **Replacement**: customer forks a new project from a different template.

### PERSONAL-D-08 [BLOCKING] · No customer-supplied translations
- **Why banned**: would bypass voice-anchor verbatim recurrence guarantee
  (CS-EXEC-01).
- **Detector**: any UI surface allowing arbitrary translation upload.
- **Replacement**: locales are template-shipped at workflow C; customer
  toggles locale on/off only.

### PERSONAL-D-09 [BLOCKING] · No new locale outside shipped set
- **Why banned**: bypasses workflow C multilingual rollout.
- **Detector**: any locale-add UI affordance.
- **Replacement**: orchestrator ships locales; customer cannot add.

### PERSONAL-D-10 [BLOCKING] · No "make all caps" typography toggle
- **Why banned**: violates CS-TYPE-01/02. Uppercase-headings reads SaaS.
- **Detector**: any text-transform: uppercase toggle in editor.
- **Replacement**: italic-em is the only emphasis mechanism (CS-TYPE-02).

### PERSONAL-D-11 [BLOCKING] · No "stronger animation" master beyond `expressive`
- **Why banned**: would let customer override gravity-allow-list for the
  cluster.
- **Detector**: motion-intensity enum with values beyond `expressive`.
- **Replacement**: `expressive` is the maximum · only available in G5/G6
  clusters.

### PERSONAL-D-12 [BLOCKING] · No exit-intent popup · no scarcity timer ·
no manipulative SaaS modal
- **Why banned**: USAGE-BAN-02 from `dynamic-pattern-usage-rules.md §6`.
- **Detector**: any modal-trigger affordance · any countdown-timer
  affordance · any "viewing now" notification.
- **Replacement**: NONE. The categories are permanently banned.

### PERSONAL-D-13 [BLOCKING] · No fake credentials · invented albo IDs
- **Why banned**: CS-EXEC-03. Fake credentials damage brand AND legal.
- **Detector**: customer can edit credential-text fields but no validation
  prevents fake IDs. Editor surfaces a warning ("Credentials should be
  verifiable. Please confirm before publishing.") and logs the customer's
  acknowledgement.
- **Replacement**: warning + acknowledgement at publish time.

### PERSONAL-D-14 [BLOCKING] · No "delete legal row" or "delete cookie banner"
- **Why banned**: PERSONAL-INV-09 is broader · legal compliance violation.
- **Detector**: visibility toggle on legal row OR cookie banner.
- **Replacement**: system-managed.

### PERSONAL-D-15 [BLOCKING] · No live-counter with customer-supplied backend feed
- **Why banned**: USAGE-PERSONAL-04. Customer cannot wire arbitrary feeds
  · CORS · trust · perf risks.
- **Detector**: any field accepting a backend URL in editor.
- **Replacement**: ops-side configuration only · customer toggles on/off
  if feed is wired.

---

## §4 · Anti-collapse safety (per template-fork)

Rules that prevent customization from converging customer projects.

### PERSONAL-COLLAPSE-01 [REQUIRED] · Per-cluster preset narrowing
- Each cluster's Layer B preset libraries (palette · font · imagery pool ·
  CTA copy) are per-cluster · NOT global.
- **Failure mode**: a customer's choices look identical to a different
  cluster's customer's choices.
- **Evidence**: editor reads `WebTemplate.cluster_id` and presents only
  that cluster's preset library.

### PERSONAL-COLLAPSE-02 [REQUIRED] · Sibling-aware preset subtraction
- When a customer forks a 2nd LF-2 corporate-suite sibling (after Cornice
  has shipped), the palette picker excludes Cornice's claimed palette ·
  the font-pair picker excludes Cornice's claimed pair · the CTA-copy
  picker excludes Cornice's claimed copy.
- **Failure mode**: a 2nd LF-2 sibling can accidentally match Cornice on
  multiple Layer-B axes simultaneously.
- **Evidence**: preset registry is computed at fork-time · reads live
  `TEMPLATE_REGISTRY.json`.

### PERSONAL-COLLAPSE-03 [REQUIRED] · Layer A invariants enforce cluster identity
- Per §2 above. The cluster contract is enforced regardless of customer
  choices.

### PERSONAL-COLLAPSE-04 [STRONG] · Warn on near-collision
- When a customer's choice combo approaches an existing sibling's identity
  (palette + font + cluster + 2 of 3 toggles), the editor surfaces a
  warning: "This combination is similar to {sibling_name}. Consider
  picking a different palette to make your site visually distinct."
- **Failure mode**: the customer ships a project that visually clones a
  cataloged sibling.
- **Evidence**: editor at preview time runs a similarity check against
  cataloged sibling identities; surfaces warning text.

### PERSONAL-COLLAPSE-05 [GUIDELINE] · Preset library refresh cycle
- The orchestrator refreshes preset libraries when:
  - A new sibling ships (Mechanism 2 · `corporate-suite-distinctness-
    matrix.md` row added).
  - A new cluster ships at hardening parity (per Phase X.7a).
  - A § decision changes a cluster invariant.
- Refresh happens at the same hardening pass that ships the new sibling/cluster.
- **Failure mode**: preset library drifts from live state.
- **Evidence**: hardening pass closes with both the per-sibling update AND
  the preset-registry update in the same commit.

---

## §5 · Preview-verification gating (per save)

Every customer save fires the preview-verifier. Fail = save blocked.

### PERSONAL-PREVIEW-01 [BLOCKING] · Run preview-verifier before save
- Editor runs the verifier at every save.
- **Failure mode**: customer ships a broken state.

### PERSONAL-PREVIEW-02 [BLOCKING] · Show customer the failure reason
- If preview-verifier fails, customer sees the rule that failed in
  human-readable text. Example:
  - "Contrast is too low between your accent color and cream paper. Try
    a darker accent or pick a different palette preset."
  - "Your hero photo is below the recommended resolution (1600px wide).
    Upload a larger image OR pick from the photography preset pool."
- **Failure mode**: customer doesn't know why the save failed · churns.

### PERSONAL-PREVIEW-03 [BLOCKING] · Preserve customer's input on failure
- The failed input is preserved in the editor session (not committed to
  `ProjectContent`/`ProjectDesignTokens`/`ProjectAsset`). Customer can
  adjust and retry.
- **Failure mode**: customer loses their work.

### PERSONAL-PREVIEW-04 [REQUIRED] · Verifier uses the same checks as A.6 critic
- The preview-verifier shares its rule library with the orchestrator-side
  style-critic at workflow A.6. This means the same `[BLOCKING]` rules
  catch broken state at customer-side AND at template-authoring side.
- **Failure mode**: customer ships a state that the orchestrator would
  have blocked at A.6.

### PERSONAL-PREVIEW-05 [REQUIRED] · Verifier reads Layer A invariants
- The verifier reads `factory/standards/<cluster>-design-standard.md` for
  the source archetype's cluster · enforces all `[BLOCKING]` rules from
  there.
- **Failure mode**: divergence between customer-side and orchestrator-side
  enforcement.

### PERSONAL-PREVIEW-06 [STRONG] · Surface near-edge warnings
- Per PERSONAL-COLLAPSE-04. Warnings (not blocks) for:
  - Palette near contrast floor.
  - Font choice nearly matching a shipped sibling.
  - Section-count near minimum-4 floor.
- The customer can save and proceed; the warning is logged for audit.

---

## §6 · Customer-side publish gating

Beyond per-save, before a customer publishes (`status: draft → published`),
additional gates fire.

### PERSONAL-PUBLISH-01 [BLOCKING] · Browser-verifier rubric runs at publish
- Customer publish triggers a browser-walk: home + about + contact + 1
  case-detail (if cases section enabled). Walk emulates `prefers-reduced-
  motion: reduce` once and `prefers-reduced-motion: no-preference` once.
- **Failure mode**: customer publishes a state that fails browser-rubric.

### PERSONAL-PUBLISH-02 [BLOCKING] · Frozen-sibling regression check
- The customer's project's source template's "frozen sibling state" (i.e.,
  the state of the source's cluster siblings at fork time) is preserved.
  Publishing a customer project does NOT cause regressions on cluster
  templates the customer doesn't own.
- **Failure mode**: customer's project leaks CSS into the cluster's
  shared chrome (which is impossible by architecture · the customer's
  project renders under its own URL prefix · this rule is the architectural
  guard).

### PERSONAL-PUBLISH-03 [REQUIRED] · `ProjectRevision` snapshot at publish
- Per existing A.1b model. Each publish creates a `Reason: PUBLISH`
  revision row.

### PERSONAL-PUBLISH-04 [BLOCKING] · Whistleblowing column verified
- For applicable clusters/locales, the publish-gate confirms the
  whistleblowing footer column is present.

### PERSONAL-PUBLISH-05 [STRONG] · Acknowledgement of fake-credential warning
- Per PERSONAL-D-13. If customer edited credential fields, publish
  prompts: "Are these credentials verifiable? Customer projects with
  unverifiable credentials may be flagged for marketplace review."
  Customer must explicitly acknowledge.

### PERSONAL-PUBLISH-06 [REQUIRED] · Locale parity at publish
- Each enabled locale must have copy for: hero h1 · CTA copy · about
  intro · contact intro. Empty locales are blocked at publish.

---

## §7 · § decision triggers (escalation paths)

A § decision is required when the orchestrator wants to deviate from
any [BLOCKING] / [REQUIRED] rule above.

§ decisions are filed in:
- `factory/standards/<cluster>-design-standard.md` (per cluster).
- `factory/reports/hardening/personalization-decision-log.md` (cumulative
  · created at first § decision · monotonically extended).

A § decision MUST include:
1. Which rule is being deviated from.
2. The control surface affected.
3. The semantic justification.
4. Whether the deviation is per-sibling, per-cluster, or system-wide.
5. The replacement constraint enforcement (i.e., what new check protects
   what the old rule was protecting).

The orchestrator does NOT silently waive a [BLOCKING] rule. Always § decision.

Common § decision triggers:
- Lifting a Layer D ban (e.g., adding a free hex picker WITH constraint
  engine attached). Almost always rejected unless engine is rock-solid.
- Adding a Layer C toggle that affects an L-cell (would need to escalate
  to Layer A discussion).
- Lowering preview-verification severity from BLOCKING to STRONG (i.e.,
  letting a customer publish a state with low-contrast palette · only
  acceptable if the cluster contract explicitly waives CS-PAL-01 for
  customer-overrides · which would be controversial).

---

## §8 · How an editor-team uses these rules at every X.7c slice

Implementation pattern for each X.7c slice:

1. **Identify the control surface** the slice adds (CS-1 to CS-17).
2. **Confirm layer assignment** via `personalization-control-surface-map.md`.
3. **Verify against Layer D bans** in §3 here. If the slice would surface
   a Layer D control, it's a § decision.
4. **Implement model + UI**:
   - Model field (extends `ProjectContent` or `ProjectDesignTokens` or
     `ProjectAsset`).
   - UI: picker (Layer B) · toggle (Layer C) · NEVER free-input (Layer D).
5. **Implement the preview-verifier rule(s)** for that surface (per
   `personalization-control-surface-map.md §6`).
6. **Implement the publish-gate** if any new rule applies.
7. **Author the cluster's preset library** for that surface (Layer B work).
8. **Author the warnings copy** for near-edge warnings (PERSONAL-COLLAPSE-04
   + PERSONAL-D-13 acknowledgement).
9. **Add browser-rubric checks** for the new pattern at customer-publish.
10. **Document the slice** in this rule book + add the rule ID for any new
    invariant.

---

## §9 · Customer warning copy (the user-visible side of these rules)

The customer never sees rule IDs. They see warning copy that maps to rules.
The orchestrator authors these copies once; they're shared across slices.

| Rule | Customer-visible copy |
|---|---|
| PERSONAL-INV-02 (voice anchor missing) | "Your hero heading needs to include the phrase '{anchor}'. This phrase carries this template's identity across translations." |
| PERSONAL-INV-04 (non-Pexels URL) | "We can't accept image URLs from outside our editorial library. Upload your own photo or pick from the photography presets." |
| PERSONAL-INV-10 (minimum 4 sections) | "Your home page would have fewer than 4 sections, which makes it look unfinished. Re-enable a section." |
| PERSONAL-D-01 (free hex tried) | (no copy — Layer D never surfaces) |
| PERSONAL-D-13 (credentials) | "These credentials should be verifiable. Customer projects with unverifiable credentials may be flagged for marketplace review." |
| PERSONAL-COLLAPSE-04 (near-sibling collision) | "Your color and font combination is close to {sibling_name}. Consider picking a different palette to make your site visually distinct." |
| PERSONAL-PREVIEW-02 (contrast fail) | "Contrast is too low between your accent color and cream paper. Try a darker accent or pick a different palette preset." |
| PERSONAL-PREVIEW-02 (font-pair fail) | "This font pair isn't allowed for this template's cluster. Pick from the typography preset list." |

---

## §10 · Maintenance protocol

- Each new cluster's hardening pass adds rules to §1 (cluster invariants
  for that cluster) AND extends the per-cluster A/B/C surface coverage
  in §2.
- Each new Layer-D ban gets a new PERSONAL-D-N row in §3 with the why-banned
  + detector + replacement triple.
- Each new preview-verifier check gets a new PERSONAL-PREVIEW-N row in §5.
- Each warning copy goes in §9.
- § decisions go to `factory/reports/hardening/personalization-decision-
  log.md` (created at first decision · monotonically extended).
- Rule IDs are monotonic · never reused after deprecation.

---

## §11 · One-paragraph summary

10 cluster-and-family invariants (PERSONAL-INV-01..10) cover source-
archetype immutability · voice-anchor preservation · L1-L9 lockdown ·
Pexels-only imagery · whistleblowing column requirement · reduced-motion
override · Latin wordmark + numerics in RTL · focus-ring uniformity ·
about+contact required · minimum-4-sections-on-home. 10 Layer-A enforcement
rules (PERSONAL-A-01..10) ensure no editor knob is built that violates
the cluster contract. 15 Layer-D bans (PERSONAL-D-01..15) codify the
freeform controls the system deliberately does NOT ship: free hex · free
font · section reorder · custom CSS · motion-curve · free imagery URL ·
cluster change after fork · customer translation · new locale · all-caps
· "stronger" animation · manipulative SaaS modal · fake credentials ·
legal-row removal · customer-wired live-counter feed. 5 anti-collapse
mechanisms (PERSONAL-COLLAPSE-01..05) include per-cluster preset narrowing
and sibling-aware preset subtraction. 6 preview-verification rules and 6
publish-gate rules ensure no broken state ships. § decisions are required
for every deviation; silent waivers are forbidden. The book is monotonic
and rule IDs never reuse. Customer-visible warnings are authored once and
shared across slices.
