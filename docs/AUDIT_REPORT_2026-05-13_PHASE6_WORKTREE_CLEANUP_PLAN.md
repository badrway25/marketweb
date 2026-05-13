# Audit Report — Phase 6: Worktree Cleanup Plan (PRE-execution)

**Data:** 2026-05-13
**Modalità:** piano di rimozione + decisioni per-worktree (esecuzione avviene **dopo** questo documento)
**Esito target:** ridurre da 78 worktree a 12, mantenendo `marketweb/` (principale) + 1 KEEP-V15-VENV + 7 INVESTIGATE-DIRTY + 3 INVESTIGATE-UNMERGED

---

## 1. Preflight — tutto verde

| # | Check | Esito |
|---|---|---|
| Branch corrente | ✅ `master` |
| Working tree | ✅ clean |
| Local `master` = `origin/master` | ✅ `1b8019f` |
| GitHub default branch | ✅ `master` |
| Tag `v0.1-pre-mvp-master-2026-05-13` | ✅ presente |
| `stash@{0}` | ✅ disponibile |
| Worktree totali | 78 |

---

## 2. Inventario completo: 78 worktree

| Categoria | Count |
|---|---|
| KEEP (principale) | 1 |
| KEEP-V15-VENV | 1 |
| REMOVE (clean + merged) | **66** |
| INVESTIGATE-DIRTY | 7 |
| INVESTIGATE-UNMERGED | 3 |

Dati grezzi salvati in `docs/audit/2026-05-13/_inventory_worktrees.tsv`.

---

## 3. Worktree da MANTENERE

### 3.1 KEEP — Repository principale (1)
- `marketweb/` → branch `master`. Fonte di verità. **Mai rimuovere.**

### 3.2 KEEP-V15-VENV (1)
- `mw-integration-baseline-v15/` → branch `phase-x7e-lf2-variance-and-causa-retrofit`
  - Stato: CLEAN, MERGED in master (il branch è stato consolidato in Phase 3)
  - **Perché non rimuovere ora:** contiene il venv attivo `.venv-v15/` con Django 5.2.7 e tutte le 61 dipendenze. Rimuoverlo ora cancellerebbe l'ambiente Python operativo.
  - **Prerequisito per rimozione:** ricreare il venv dentro `marketweb/` (es. `marketweb/.venv`) e re-installare `requirements.txt`, poi rimuovere il worktree v15.
  - **Azione consigliata:** lasciare per Batch F separato (Phase 5 plan).

---

## 4. Worktree DIRTY da NON rimuovere (7) — INVESTIGATE

Tutti CLEAN secondo il criterio "merged in master", ma il working tree contiene modifiche non committate. Per regola: **niente `--force`, niente rimozione**.

| # | Path | Branch | Dirty entries | Note |
|---|---|---|---|---|
| 1 | `marketweb/.claude/worktrees/preview-realism` | `worktree-preview-realism` | 5 file modified | AGENT_HANDOFF/DECISIONS/SESSION_LOG/TODO_NEXT + `generate_previews.py` — vecchia sessione con docs modificati ma non committati |
| 2 | `mw-agency-live-rollout-v1` | `phase-agency-live-rollout-v1` | 8 untracked | Screenshot JPG (`aura-*.jpeg`) generati durante QA, mai committati. Sono asset visivi locali, potresti conservarli o cancellarli |
| 3 | `mw-ecommerce-live-rollout-v1` | `phase-ecommerce-live-rollout-v1` | 1 untracked | `.claude/scheduled_tasks.lock` — file di lock residuo di Claude Code |
| 4 | `mw-editor-a1-flow-fix-v1` | `phase-editor-a1-flow-fix-v1` | 5 modified | Codice (`generate_previews.py`, `catalog/views.py`, `projects/services.py`, `projects/tests.py`, `_navbar.html`) — lavoro non committato Phase A editor |
| 5 | `mw-editor-scroll-media-fix-v1` | `phase-editor-scroll-media-fix-v1` | 16 entries | Sessione log + `editor/schema.py` e altri — sessione interrotta |
| 6 | `mw-medical-polish-fix-v1` | `phase-medical-polish-fix-v1` | 1 untracked | Directory `audit/` untracked, probabilmente vecchi report locali |
| 7 | `mw-medical-specialist-live-hardening-v2` | `phase-2g2x-medical-specialist-live-hardening-v2` | 8 modified | Codice (template_content, template_dna, theme_safety, specialist/_base.html) — lavoro non committato pre-Phase 2g2x |

**Azione consigliata per ciascuno (in sessione futura):**
- `git -C <path> diff > <backup>.patch` (salvare il diff)
- Decidere: integrare in master via cherry-pick, scartare, o conservare worktree intatto
- Solo dopo, rimozione clean

---

## 5. Worktree UNMERGED da NON rimuovere (3) — INVESTIGATE

Tutti CLEAN ma il HEAD del worktree non è raggiungibile da master. Hanno commit propri.

| # | Path | Branch | Commit | Diff vs master |
|---|---|---|---|---|
| 1 | `mw-editor-full-coverage-v1` | `phase-editor-full-coverage-v1` | `badb98a` "feat: full editor coverage, live theme sync, page-aware preview, premium search" | 880 file: +14k / -254k (storia divergente, branch antico) |
| 2 | `mw-i18n-dermatologia-v2` | `phase-i18n-dermatologia-v2` | `9043836` "feat: extend i18n/RTL to dermatologia-elite-roma (Phase 2i.2)" | 1137 file: +8k / -412k (storia divergente, branch antico) |
| 3 | `mw-medical-specialist-premium-split-v1` | `phase-medical-specialist-premium-split-v1` | `4e26b3f` "Visual richness and premium interaction second pass" | 1137 file: +9k / -411k (storia divergente, branch antico) |

**Interpretazione:** i 3 branch hanno divergato MOLTO presto (aprile 2026, prima del massive integration X.4-X.7). I "+ righe" sono molto inferiori alle "− righe" → significa che master oggi contiene molto più codice di quei branch, ma quei branch hanno **1 commit unico** che non è stato cherry-pickato esplicitamente in master.

**Possibili scenari:**
- Il commit unico potrebbe essere stato rifuso in master via altri branch (delete safe)
- Oppure contiene lavoro che è stato consciamente lasciato fuori (delete = perdita)

**Azione consigliata:** non rimuovere in questa fase. Investigazione caso-per-caso con confronto `SESSION_LOG.md` per capire se il commit unico è già altrove in master.

---

## 6. Worktree da RIMUOVERE (66)

Tutti CLEAN + MERGED in master. Sicuri.

### 6.1 `.claude/worktrees/*` (13 — preview-realism escluso DIRTY)

```
.claude/worktrees/archetype-reuse-validation
.claude/worktrees/backend-core
.claude/worktrees/catalog-enhancements
.claude/worktrees/catalog-integration
.claude/worktrees/medical-pilot-fix
.claude/worktrees/premium-ui
.claude/worktrees/real-preview-assets
.claude/worktrees/restaurant-template-pilot
.claude/worktrees/specialist-copy-abstraction
.claude/worktrees/template-completeness-pilot
.claude/worktrees/template-dna-system
.claude/worktrees/template-polish-fixes
.claude/worktrees/visual-polish-and-preview-fixes
```

### 6.2 `mw-integration-baseline-v{1..14}` (14)

```
mw-integration-baseline-v1
mw-integration-baseline-v2
mw-integration-baseline-v3
mw-integration-baseline-v4
mw-integration-baseline-v5
mw-integration-baseline-v6
mw-integration-baseline-v7
mw-integration-baseline-v8
mw-integration-baseline-v9
mw-integration-baseline-v10
mw-integration-baseline-v11
mw-integration-baseline-v12
mw-integration-baseline-v13
mw-integration-baseline-v14
```

### 6.3 `mw-editor-*` (8 — escludendo a1-flow-fix DIRTY, scroll-media-fix DIRTY, full-coverage UNMERGED)

```
mw-editor-field-targeting-fix-v1
mw-editor-foundation-v1
mw-editor-public-customize-v1
mw-editor-ux-live-preview-v1
```
*(+ altri se presenti — la lista completa è nel TSV)*

### 6.4 Restanti (31)

Rollout verticali, audit, business, ecommerce, gusto, agency-preview-pipeline, law-realestate, live-i18n/motion, luxe, medical-second-wave, motion-pilot, pixel-perfection, portfolio, pragma-hero, premium-components/forms, public-live-polish, restaurant, tier-migration, ultra-premium, business-hardening x2, audit-differentiation, 2g2x-portfolio-hardening x2, 2g2x-live-preview-policy x2, business-i18n, business-live-rollout, catalog-expansion-strategy, catalog-stabilization, commerce-completion, ecommerce-commerce-foundation, ecommerce-experience-hardening, motion-optin-medical, pixel-preview-coherence, pragma-hero-visibility, ecc.

**Lista completa nel TSV `_inventory_worktrees.tsv`.**

---

## 7. Piano di esecuzione (batch da 10)

| Batch | Range | Rischio | Note |
|---|---|---|---|
| A | `.claude/worktrees/*` (13 elementi, batch unico) | basso | Worktree interni Claude Code |
| B | `mw-integration-baseline-v{1..10}` (10) | basso | Baseline storiche v1-v10 |
| C | `mw-integration-baseline-v{11..14}` + 6 altri (10) | basso | Resto delle baseline + worktree generici |
| D | 10 worktree rollout verticali | basso-medio | Possibili screenshot locali persi |
| E | 10 worktree rollout verticali | basso-medio | idem |
| F | 10 worktree rollout verticali | basso-medio | idem |
| G | restanti ~13 worktree | basso-medio | ultimo batch + chiusura |

**Verifiche dopo ogni batch:**
- `git worktree list` per conteggio rimanenti
- `git status` su `marketweb/` (deve restare clean su master)
- `git stash list` (deve restare con `stash@{0}` intatto)
- `git rev-parse HEAD` (master deve restare `1b8019f`)

**Stop immediato se:**
- Un worktree rifiuta la rimozione (es. lock di file system, file modificati non rilevati prima)
- `git status` su master diventa dirty
- Stash sparisce
- HEAD master cambia

---

## 8. Operazioni vietate

- ❌ `git worktree remove --force` (mai)
- ❌ `git worktree prune` (rimandato a Batch G di Phase 6 plan, con OK separato)
- ❌ `git branch -d` / `-D` (rimandato a fase successiva)
- ❌ `git push --delete` (rimandato)
- ❌ `git stash drop` (rimandato)
- ❌ `git reset` / `git clean` (mai senza OK esplicito)
- ❌ Modifiche al codice

---

## 9. Stato attuale a inizio Phase 6

- HEAD `master`: `1b8019f4702452e4231d093dcab8776aa411de96`
- `origin/master`: `1b8019f` (sync ✅)
- 78 worktree
- 158 branch locali (zero toccato)
- 33 branch remoti (zero toccato)
- `stash@{0}` intatto
- tag `v0.1-pre-mvp-master-2026-05-13` intatto

**Conta target a fine Phase 6:** 12 worktree (1 principale + 1 KEEP-V15-VENV + 7 INVESTIGATE-DIRTY + 3 INVESTIGATE-UNMERGED).
