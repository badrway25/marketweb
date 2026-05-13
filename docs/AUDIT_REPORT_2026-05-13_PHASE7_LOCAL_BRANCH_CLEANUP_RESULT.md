# Audit Report — Phase 7: Local Branch Cleanup Result

**Data:** 2026-05-13
**Modalità:** rimozione branch locali merged via `git branch -d` (mai `-D`)
**Esito:** ✅ 158 → 21 branch locali, **137 cancellati**, **3 INVESTIGATE-UPSTREAM-DRIFT** rilevati, **6 INVESTIGATE-UNMERGED** intatti, zero modifiche al remoto

---

## 1. Sintesi esecutiva

| Metrica | Pre Phase 7 | Post Phase 7 | Δ |
|---|---|---|---|
| Branch locali totali | **158** | **21** | **−137** |
| Branch attaccati a worktree | 12 | 12 | 0 (invariato) |
| Branch INVESTIGATE-UNMERGED (originali) | 6 free-standing | 6 free-standing | 0 (mai toccati) |
| **NUOVO: Branch INVESTIGATE-UPSTREAM-DRIFT** | — | **3** | +3 (rilevati durante batch, skip + `-D` mai usato) |
| Branch REMOVE candidati | 140 | 0 | **137 deleted + 3 skipped** |
| Branch remoti | 33 | **33** | 0 (mai toccati) |
| Worktree totali | 12 | **12** | 0 (mai toccati) |
| Stash | 1 | **1** | 0 (mai droppato) |
| Tag | 1 (+1 preesistente) | identico | 0 |
| HEAD `master` | `2729934` | `2729934` | invariato (commit pre-Phase 7) |
| `origin/master` | `2729934` | `2729934` | invariato (push avverrà alla fine) |

---

## 2. Esecuzione batch (alfabetica, da 20 ciascuno)

| Batch | Range | Eseguito | Falliti | Branch rimasti dopo |
|---|---|---|---|---|
| 1 | 1..20 | 20 ✅ | 0 | 138 |
| 2 | 21..40 | 19 ✅ | **1** (`phase-editor-a2-5-palette-jump-fix-v1`) | 119 |
| 3 | 41..60 | 20 ✅ | 0 | 99 |
| 4 | 61..80 | 20 ✅ | 0 | 79 |
| 5 | 81..100 | 19 ✅ | **1** (`phase-x4-solaria-passB-multilingual`) | 60 |
| 6 | 101..120 | 20 ✅ | 0 | 40 |
| 7 | 121..140 | 19 ✅ | **1** (`phase-x6-causa-step1-planner-brief`) | 21 |
| **TOTALE** | | **137** | **3** | **21** |

---

## 3. Branch INVESTIGATE-UPSTREAM-DRIFT (3, nuovi)

Tutti merged in master HEAD locale, **rifiutati da `git branch -d`** perché Git rileva che il loro upstream remoto contiene commit che il branch locale non ha.

| Branch | Upstream | Drift |
|---|---|---|
| `phase-editor-a2-5-palette-jump-fix-v1` | `origin/phase-editor-a2-5-palette-jump-fix-v1` | ahead 2 commit |
| `phase-x4-solaria-passB-multilingual` | `origin/phase-x4-solaria-passB-multilingual` | ahead 1 commit |
| `phase-x6-causa-step1-planner-brief` | `origin/phase-x6-causa-step1-planner-brief` | ahead 1 commit |

**Spiegazione tecnica:** `git branch -d` rifiuta di cancellare un branch se ha un tracking upstream che contiene commit non presenti localmente — protezione contro la perdita accidentale di lavoro remoto. **Niente `-D` è stato usato** (per regola Phase 7).

**Cosa fare in futuro (Phase 8 candidato):**
- Investigare i 2/1/1 commit upstream tramite `git fetch && git log <branch>..origin/<branch>`
- Se contengono solo lavoro storico irrilevante, fare `git branch -D` (con OK esplicito)
- Se contengono qualcosa da preservare, prima cherry-pick in master e poi delete

---

## 4. Branch INVESTIGATE-UNMERGED (6, originali pre-Phase 7)

Free-standing, mai cancellati come da regola Phase 7. Restano intatti.

| # | Branch | HEAD | Note |
|---|---|---|---|
| 1 | `phase-x4-continua-build-brief` | `c45c52a` | 2026-04-29 Design orchestrator brief |
| 2 | `phase-x4-continua-public-flip` | `8b3ccc1` | 2026-04-30 LF-2 Cornice pilot (ha anche upstream `origin/phase-x4-continua-public-flip`) |
| 3 | `phase-x4-solaria-user-visible-passA` | `3cdbef6` | 2026-04-27 X.4 Solaria passB completion |
| 4 | `phase-x4-wave2-solaria-coaching-v1` | `6b70d56` | 2026-04-21 fix solaria-coaching palette |
| 5 | `phase-x4a-corporate-factory-hardening-step0` | `921961f` | 2026-04-24 corporate-suite readiness verdict |
| 6 | `phase-x4a-solaria-controlled-reentry-plan` | `cf54efa` | 2026-04-24 Solaria re-entry plan |

---

## 5. 21 branch rimasti (composizione completa)

### 5.1 KEEP-MASTER (1)
- `master` → `2729934` ✅ fonte di verità

### 5.2 KEEP-WORKTREE-ATTACHED (11)
1. `worktree-preview-realism` → `marketweb/.claude/worktrees/preview-realism`
2. `phase-agency-live-rollout-v1` → `mw-agency-live-rollout-v1`
3. `phase-ecommerce-live-rollout-v1` → `mw-ecommerce-live-rollout-v1`
4. `phase-editor-a1-flow-fix-v1` → `mw-editor-a1-flow-fix-v1`
5. `phase-editor-full-coverage-v1` → `mw-editor-full-coverage-v1`
6. `phase-editor-scroll-media-fix-v1` → `mw-editor-scroll-media-fix-v1`
7. `phase-i18n-dermatologia-v2` → `mw-i18n-dermatologia-v2`
8. `phase-x7e-lf2-variance-and-causa-retrofit` → `mw-integration-baseline-v15`
9. `phase-medical-polish-fix-v1` → `mw-medical-polish-fix-v1`
10. `phase-2g2x-medical-specialist-live-hardening-v2` → `mw-medical-specialist-live-hardening-v2`
11. `phase-medical-specialist-premium-split-v1` → `mw-medical-specialist-premium-split-v1`

### 5.3 INVESTIGATE-UNMERGED (6) — vedi §4

### 5.4 INVESTIGATE-UPSTREAM-DRIFT (3) — vedi §3

---

## 6. 137 branch cancellati (composizione per pattern)

- 34 `phase-editor-a*-v1` (granular editor Phase A — 1 in INVESTIGATE)
- 15 `phase-integration-baseline-v{1..14}` + extras (15/15)
- 13 `worktree-*` (13/13, escluso `worktree-preview-realism` che ha worktree)
- 13 `phase-x4-*` step intermedi (12/13 — 1 in INVESTIGATE)
- 11 `phase-x5-*` step intermedi (11/11)
- 8 `phase-x6*` step intermedi (7/8 — 1 in INVESTIGATE)
- 8 `phase-2g2x-*` hardening (8/8)
- 4 `phase-x4b-*` corporate-suite layouts (4/4)
- 4 `phase-editor-*` non-`a*` (foundation, field-targeting-fix, public-customize, ux-live-preview)
- 2 `phase-x4a-*` (2/2)
- 2 ciascuno: `phase-restaurant-*`, `phase-premium-*`, `phase-pixel-*`, `phase-motion-*`, `phase-live-*`, `phase-i18n-*`, `phase-ecommerce-*`, `phase-catalog-*`, `phase-business-*`
- 1 ciascuno: `phase-ultra-*`, `phase-real-estate-/law-*`, `phase-public-*`, `phase-pragma-*`, `phase-portfolio-*`, `phase-medical-*`, `phase-luxe-*`, `phase-commerce-*`, `phase-agency-*`

**Lista completa nel TSV** `docs/audit/2026-05-13/_inventory_branches.tsv` (filtrare per `decision == REMOVE`).

---

## 7. Conferme di sicurezza

| Conferma | Esito |
|---|---|
| Nessun branch remoto cancellato | ✅ 33 → 33 |
| Nessun `git push --delete` eseguito | ✅ |
| Nessun `-D` usato | ✅ (3 fallimenti `-d` skippati, NON forzati) |
| Nessun `--force` | ✅ |
| Nessun reset/rebase/squash | ✅ |
| Nessun worktree rimosso | ✅ 12 → 12 |
| Nessun `git worktree prune` | ✅ |
| Nessuno stash droppato | ✅ `stash@{0}` presente |
| Nessun tag toccato | ✅ |
| Nessuna modifica al codice del progetto | ✅ |
| HEAD `master` invariato | ✅ `2729934` |
| `origin/master` invariato | ✅ `2729934` |
| Zero token/credenziali stampati | ✅ |

---

## 8. Stato Git finale

```
On branch master
nothing to commit, working tree clean

HEAD = 2729934f9efe770e175ad5999ed77e3b10b24f60
origin/master = 2729934f9efe770e175ad5999ed77e3b10b24f60
21 branch locali (era 158, -137)
33 branch remoti (invariati)
12 worktree (invariati)
stash@{0}: On master: WT cosmetic drift on master before FF merge 2026-05-13
tag v0.1-pre-mvp-master-2026-05-13 → 9736da44ad68494308b5ea12063b61a4f3207891
```

---

## 9. Raccomandazione Phase 8

### Phase 8.A — Risoluzione INVESTIGATE-UPSTREAM-DRIFT (3 branch)
Per ciascuno dei 3 con upstream ahead:
```
git fetch origin
git log <branch>..origin/<branch> --oneline
git diff <branch>..origin/<branch> --stat
```
Decisione: cherry-pick il/i commit utili in master, poi `git branch -D <branch>` (con tuo OK esplicito), poi opzionalmente `git push origin --delete <remote-branch>` se vuoi rimuovere anche il remoto.

### Phase 8.B — Risoluzione INVESTIGATE-UNMERGED (6 branch)
Per ognuno dei 6, confronto `git log master..<branch>` per capire se il commit è recuperabile o irrilevante. Possibili azioni: cherry-pick + delete, o creazione tag attic + delete.

### Phase 8.C — Cleanup branch remoti merged (30 branch)
Eliminazione branch remoti merged in `origin/master` (esclusi `origin/master` e `origin/phase-integration-baseline-v15`). Comando: `git push origin --delete <branch>`. Solo dopo OK per ogni batch.

### Phase 8.D — Cleanup worktree DIRTY rimanenti (7 worktree)
Investigazione dei 7 DIRTY: salvare diff in patch, decidere se integrare/scartare, poi `git worktree remove`.

### Phase 8.E — Cleanup `mw-integration-baseline-v15`
Preparare venv alternativo in `marketweb/.venv`, poi rimuovere worktree v15 + branch `phase-x7e-...`. Solo dopo ricreazione venv.

### Phase 8.F — `git worktree prune` finale + drop `stash@{0}`
Solo quando hai validato che il cleanup è completo.

---

## 10. Operazioni NON eseguite (per rispetto delle regole)

- ❌ `git branch -D` (mai)
- ❌ `git push --delete` (mai)
- ❌ `--force` (mai)
- ❌ `git reset` / `git rebase` / `git squash`
- ❌ `git worktree remove` né `prune`
- ❌ `git stash drop`
- ❌ Modifiche al codice del progetto
- ❌ Zero token/credenziali esposti
