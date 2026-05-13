# Audit Report — Phase 6: Worktree Cleanup Result

**Data:** 2026-05-13
**Modalità:** rimozione di 66 worktree clean+merged via `git worktree remove` (senza `--force`)
**Esito:** ✅ 78 → 12 worktree, zero perdita di branch/stash/tag/commit

---

## 1. Sintesi esecutiva

| Metrica | Pre-Phase 6 | Post-Phase 6 | Δ |
|---|---|---|---|
| Worktree totali | **78** | **12** | **−66** |
| Branch locali | 158 | **158** | 0 (intatti) |
| Branch remoti | 33 | **33** | 0 (intatti) |
| Stash | 1 | **1** | 0 (intatto) |
| Tag locali | 1 + 1 = 2 (v0.1-pre-mvp + 1 preesistente) | **identico** | 0 |
| HEAD `master` | `1b8019f` | `1b8019f` | invariato |
| `origin/master` | `1b8019f` | `1b8019f` | invariato |
| Working tree principale | clean | clean | invariato |

---

## 2. Worktree rimossi (66)

Eseguiti in 7 batch (10+10+10+10+10+10+6) con verifica intermedia dopo ogni batch. Tutti via `git worktree remove "<path>"` senza `--force`. Per ognuno: status pre = CLEAN, branch merged in `master`.

### Batch A — 10 (`.claude/worktrees/*`)
- archetype-reuse-validation, backend-core, catalog-enhancements, catalog-integration, medical-pilot-fix, premium-ui, real-preview-assets, restaurant-template-pilot, specialist-copy-abstraction, template-completeness-pilot

### Batch B — 10
- `.claude/worktrees/{template-dna-system, template-polish-fixes, visual-polish-and-preview-fixes}`
- mw-agency-preview-pipeline-fix-v1, mw-audit-differentiation, mw-business-hardening, mw-business-hardening-v2, mw-business-i18n-completion-v1, mw-business-live-rollout-v1, mw-catalog-expansion-strategy-v1

### Batch C — 10
- mw-catalog-stabilization-v1, mw-commerce-completion-v2, mw-ecommerce-commerce-foundation-v1, mw-ecommerce-experience-hardening-v1, mw-editor-field-targeting-fix-v1, mw-editor-foundation-v1, mw-editor-public-customize-v1, mw-editor-ux-live-preview-v1, mw-gusto-i18n-rtl-v1, mw-i18n-pilot-cardio-v2

### Batch D — 10
- mw-integration-baseline-v1, v2, v3, v4, v5, v10, v11, v12, v13, v14

### Batch E — 10
- mw-integration-baseline-v{6, 7, 8, 9}, mw-law-realestate-live-rollout-v1, mw-live-i18n-media-hardening-v1, mw-live-motion-media-pass-v1, mw-live-preview-policy, mw-live-preview-policy-v2, mw-luxe-commerce-polish-v1

### Batch F — 10
- mw-medical-second-wave-v1, mw-motion-optin-medical-v1, mw-motion-pilot-gusto-v2, mw-pixel-perfection-pass-v1, mw-pixel-preview-coherence-fix-v1, mw-portfolio-hardening, mw-portfolio-hardening-v2, mw-portfolio-live-rollout-v1, mw-pragma-hero-visibility-fix-v1, mw-premium-components-blueprint-v1

### Batch G — 6 (ultimo)
- mw-premium-forms-polish-v1, mw-public-live-polish-v1, mw-restaurant-live-completion-v1, mw-restaurant-polish-fix-v1, mw-tier-migration-v2, mw-ultra-premium-live-v1

---

## 3. Worktree rimasti (12)

| # | Path | Branch | HEAD | Stato | Decisione |
|---|---|---|---|---|---|
| 1 | `marketweb/` | `master` | `1b8019f` | clean | **KEEP** (repository principale) |
| 2 | `marketweb/.claude/worktrees/preview-realism` | `worktree-preview-realism` | `6239d33` | **DIRTY** (5 file modified) | INVESTIGATE |
| 3 | `mw-agency-live-rollout-v1` | `phase-agency-live-rollout-v1` | `9cef9a7` | **DIRTY** (8 JPG untracked) | INVESTIGATE |
| 4 | `mw-ecommerce-live-rollout-v1` | `phase-ecommerce-live-rollout-v1` | `f35b4e5` | **DIRTY** (1 lock file) | INVESTIGATE |
| 5 | `mw-editor-a1-flow-fix-v1` | `phase-editor-a1-flow-fix-v1` | `aa06d0b` | **DIRTY** (5 file modified) | INVESTIGATE |
| 6 | `mw-editor-full-coverage-v1` | `phase-editor-full-coverage-v1` | `badb98a` | clean | **INVESTIGATE-UNMERGED** (1 commit ahead di master) |
| 7 | `mw-editor-scroll-media-fix-v1` | `phase-editor-scroll-media-fix-v1` | `1f4310b` | **DIRTY** (16 entries) | INVESTIGATE |
| 8 | `mw-i18n-dermatologia-v2` | `phase-i18n-dermatologia-v2` | `9043836` | clean | **INVESTIGATE-UNMERGED** |
| 9 | `mw-integration-baseline-v15` | `phase-x7e-lf2-variance-and-causa-retrofit` | `ab88d16` | clean | **KEEP-V15-VENV** (contiene `.venv-v15`) |
| 10 | `mw-medical-polish-fix-v1` | `phase-medical-polish-fix-v1` | `623405b` | **DIRTY** (audit/ untracked) | INVESTIGATE |
| 11 | `mw-medical-specialist-live-hardening-v2` | `phase-2g2x-medical-specialist-live-hardening-v2` | `0a5bcf2` | **DIRTY** (8 file modified) | INVESTIGATE |
| 12 | `mw-medical-specialist-premium-split-v1` | `phase-medical-specialist-premium-split-v1` | `4e26b3f` | clean | **INVESTIGATE-UNMERGED** |

**Composizione:** 1 KEEP + 1 KEEP-V15-VENV + 7 DIRTY (INVESTIGATE) + 3 UNMERGED (INVESTIGATE) = 12.

---

## 4. Conferme di sicurezza

| Conferma | Esito |
|---|---|
| Nessun branch locale cancellato | ✅ 158 → 158 |
| Nessun branch remoto cancellato | ✅ 33 → 33 |
| Nessuno stash droppato | ✅ `stash@{0}` ancora presente |
| Nessun `--force` usato | ✅ `git worktree remove` standard sempre |
| Nessun `git worktree prune` | ✅ |
| Nessun `git reset` né `git clean` | ✅ |
| Nessuna modifica al codice del progetto | ✅ |
| Nessun push remoto | ✅ |
| Nessun tag toccato | ✅ `v0.1-pre-mvp-master-2026-05-13` presente |
| HEAD `master` invariato | ✅ `1b8019f` |
| `origin/master` invariato | ✅ `1b8019f` |
| Working tree principale clean | ✅ (eccetto 3 untracked: questo report + PLAN + 2 file inventory che committeremo separatamente) |
| Nessun token/credenziale stampato | ✅ |

---

## 5. Stato Git finale

```
On branch master
nothing to commit, working tree clean (modulo i 3 untracked di Phase 6)

HEAD = 1b8019f4702452e4231d093dcab8776aa411de96
origin/master = 1b8019f4702452e4231d093dcab8776aa411de96
stash@{0}: On master: WT cosmetic drift on master before FF merge 2026-05-13
tag v0.1-pre-mvp-master-2026-05-13 → 9736da44ad68494308b5ea12063b61a4f3207891
```

```
git worktree list:
C:/tmp/sitoBadr2/marketweb                                    1b8019f [master]
C:/tmp/sitoBadr2/marketweb/.claude/worktrees/preview-realism  6239d33 [worktree-preview-realism]
C:/tmp/sitoBadr2/mw-agency-live-rollout-v1                    9cef9a7 [phase-agency-live-rollout-v1]
C:/tmp/sitoBadr2/mw-ecommerce-live-rollout-v1                 f35b4e5 [phase-ecommerce-live-rollout-v1]
C:/tmp/sitoBadr2/mw-editor-a1-flow-fix-v1                     aa06d0b [phase-editor-a1-flow-fix-v1]
C:/tmp/sitoBadr2/mw-editor-full-coverage-v1                   badb98a [phase-editor-full-coverage-v1]
C:/tmp/sitoBadr2/mw-editor-scroll-media-fix-v1                1f4310b [phase-editor-scroll-media-fix-v1]
C:/tmp/sitoBadr2/mw-i18n-dermatologia-v2                      9043836 [phase-i18n-dermatologia-v2]
C:/tmp/sitoBadr2/mw-integration-baseline-v15                  ab88d16 [phase-x7e-lf2-variance-and-causa-retrofit]
C:/tmp/sitoBadr2/mw-medical-polish-fix-v1                     623405b [phase-medical-polish-fix-v1]
C:/tmp/sitoBadr2/mw-medical-specialist-live-hardening-v2      0a5bcf2 [phase-2g2x-medical-specialist-live-hardening-v2]
C:/tmp/sitoBadr2/mw-medical-specialist-premium-split-v1       4e26b3f [phase-medical-specialist-premium-split-v1]
```

---

## 6. Conseguenze del cleanup

### File system
- Lo spazio occupato dai 66 worktree rimossi è stato liberato (i loro check-out completi del repo erano duplicati per ognuno: stimati 200-500 MB cadauno, totale ~10-30 GB potenziali, dipende da media/screenshots/db.sqlite3 locali in ognuno).
- I file `.gitignored` dei 66 worktree (screenshots `*.png`, `db.sqlite3` per-worktree, eventuali `.venv` se presenti, media/) sono persi — irreversibile, non recuperabili senza ricreare il worktree e ricostruire il contenuto.
- Tutte le screenshots `qa-*.png` generate durante le Fasi 1-4 in worktree non-principali sono perse (erano gitignored). Le screenshots di Phase 6 sono nel worktree principale e quindi conservate localmente (se non già spostate).

### Git
- I 66 branch corrispondenti **sono ancora presenti** come ref locali. Per averli "veramente" puliti serve un batch separato di `git branch -d <name>` (rimandato — non autorizzato in Phase 6).
- Le metadata `.git/worktrees/<name>/` dei 66 worktree rimossi sono in stato "rimosso" — Git le pulisce automaticamente alla prossima `git worktree list`, oppure manualmente con `git worktree prune` (rimandato).

---

## 7. Prossime raccomandazioni

### Immediate (consigliate per chiudere correttamente Phase 6)
1. **Commit dei 3 untracked di docs/audit** generati in Phase 6:
   - `docs/AUDIT_REPORT_2026-05-13_PHASE6_WORKTREE_CLEANUP_PLAN.md`
   - `docs/AUDIT_REPORT_2026-05-13_PHASE6_WORKTREE_CLEANUP_RESULT.md` (questo)
   - `docs/audit/2026-05-13/_inventory_worktrees.py` + `.tsv`
   Commit suggerito: `docs(audit): record worktree cleanup phase 6 (78 → 12 worktrees)`.

### A breve (con tuo OK separato per ognuna)
2. **Investigazione 7 DIRTY** (`worktree-preview-realism`, `mw-agency-live-rollout-v1`, `mw-ecommerce-live-rollout-v1`, `mw-editor-a1-flow-fix-v1`, `mw-editor-scroll-media-fix-v1`, `mw-medical-polish-fix-v1`, `mw-medical-specialist-live-hardening-v2`): salvare diff/patch + decidere se integrare/scartare.
3. **Investigazione 3 UNMERGED** (`mw-editor-full-coverage-v1`, `mw-i18n-dermatologia-v2`, `mw-medical-specialist-premium-split-v1`): `git log master..<branch>` + diff per capire se il singolo commit unico è utile o già rifuso.
4. **Cleanup branch locali free-standing merged** (~75 branch senza worktree): batch `git branch -d` (Phase 7 plan).
5. **Cleanup branch remoti merged** (30 branch su `origin`): batch `git push origin --delete` (Phase 7 plan).

### A medio termine
6. **`git worktree prune`** per pulire metadata residue dei worktree rimossi.
7. **Rimozione `mw-integration-baseline-v15`**: prima ricreare il venv in `marketweb/` (es. `marketweb/.venv`), poi rimuovere il worktree + branch.
8. **Drop `stash@{0}`** quando confermi che il cosmetic drift è davvero da scartare.

---

## 8. Operazioni NON eseguite (per rispetto delle regole)

- ❌ Nessun `git worktree remove --force`
- ❌ Nessun `git worktree prune`
- ❌ Nessun `git branch -d` né `-D`
- ❌ Nessun `git push --delete`
- ❌ Nessun `git stash drop`
- ❌ Nessun `git reset` né `git clean`
- ❌ Nessuna modifica al codice del progetto
- ❌ Zero token/credenziali stampati in chat o log
