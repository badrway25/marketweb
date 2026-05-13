# Audit Report — Phase 7: Local Branch Cleanup Plan (PRE-execution)

**Data:** 2026-05-13
**Modalità:** piano cancellazione branch locali merged, senza toccare remoto/stash/worktree/codice
**Esito target:** ridurre 158 → 18 branch locali (master + 11 worktree-attached + 6 INVESTIGATE-UNMERGED)

---

## 1. Premesse e regole

- **Solo branch locali**, mai branch remoti.
- **Solo `git branch -d`**, mai `-D`. Se Git rifiuta la delete, fermarsi e classificare come INVESTIGATE.
- Mai `--force`, mai `git push --delete`, mai `git stash drop`, mai `git reset`, mai `git worktree prune`.
- Mai modifiche al codice.
- Ogni batch ha verifica intermedia + stop al primo errore.

---

## 2. Stato attuale (post Phase 6 + commit `bf12943`)

| Risorsa | Valore |
|---|---|
| Branch locali totali | **158** |
| Branch attaccati a worktree (KEEP) | 12 (master + 11 altri) |
| Branch free-standing | 146 |
| Branch merged in master (locale) | 152 |
| Branch NOT merged in master | 6 (tutti free-standing — i 3 not-merged dei worktree restanti sono coperti da KEEP-WORKTREE-ATTACHED) |
| **Candidati REMOVE** (free-standing + merged) | **140** |

Dati salvati in `docs/audit/2026-05-13/_inventory_branches.tsv` (TSV con colonne: `branch`, `head`, `in_worktree`, `merged`, `decision`).

---

## 3. Branch da TENERE (18 totali)

### 3.1 KEEP-MASTER (1)
- `master` → `bf12943` — fonte di verità, mai cancellare

### 3.2 KEEP-WORKTREE-ATTACHED (11)
Branch attaccati ai 12 worktree (esclusi master). Git rifiuterà automaticamente la delete di questi via `branch -d` (protezione).

| # | Branch | HEAD | Worktree |
|---|---|---|---|
| 1 | `worktree-preview-realism` | `6239d33` | `marketweb/.claude/worktrees/preview-realism` |
| 2 | `phase-agency-live-rollout-v1` | `9cef9a7` | `mw-agency-live-rollout-v1/` |
| 3 | `phase-ecommerce-live-rollout-v1` | `f35b4e5` | `mw-ecommerce-live-rollout-v1/` |
| 4 | `phase-editor-a1-flow-fix-v1` | `aa06d0b` | `mw-editor-a1-flow-fix-v1/` |
| 5 | `phase-editor-full-coverage-v1` | `badb98a` | `mw-editor-full-coverage-v1/` |
| 6 | `phase-editor-scroll-media-fix-v1` | `1f4310b` | `mw-editor-scroll-media-fix-v1/` |
| 7 | `phase-i18n-dermatologia-v2` | `9043836` | `mw-i18n-dermatologia-v2/` |
| 8 | `phase-x7e-lf2-variance-and-causa-retrofit` | `ab88d16` | `mw-integration-baseline-v15/` |
| 9 | `phase-medical-polish-fix-v1` | `623405b` | `mw-medical-polish-fix-v1/` |
| 10 | `phase-2g2x-medical-specialist-live-hardening-v2` | `0a5bcf2` | `mw-medical-specialist-live-hardening-v2/` |
| 11 | `phase-medical-specialist-premium-split-v1` | `4e26b3f` | `mw-medical-specialist-premium-split-v1/` |

### 3.3 INVESTIGATE-UNMERGED (6 free-standing)
Branch con commit non in master, senza worktree. NON cancellare in Phase 7. Da investigare in fase separata (vedi §6).

| # | Branch | HEAD | Diff con master |
|---|---|---|---|
| 1 | `phase-x4-continua-build-brief` | `c45c52a` | 2026-04-29 "Design orchestrator: add first real build brief for Continua candidate" |
| 2 | `phase-x4-continua-public-flip` | `8b3ccc1` | 2026-04-30 "X.5 LF-2: define Cornice fifth sibling pilot and distinctness proof" |
| 3 | `phase-x4-solaria-user-visible-passA` | `3cdbef6` | 2026-04-27 "X.4 Solaria passB: complete multilingual rollout and locale verification" |
| 4 | `phase-x4-wave2-solaria-coaching-v1` | `6b70d56` | 2026-04-21 "fix(catalog): X.4 pilot #2 · solaria-coaching palette polarity" |
| 5 | `phase-x4a-corporate-factory-hardening-step0` | `921961f` | 2026-04-24 "X.4a step1E: add corporate-suite hardening readiness verdict" |
| 6 | `phase-x4a-solaria-controlled-reentry-plan` | `cf54efa` | 2026-04-24 "X.4a step2A: add Solaria controlled re-entry plan and checklist" |

---

## 4. Branch REMOVE (140) — composizione per pattern

| Pattern | Count | Note |
|---|---|---|
| `phase-editor-a*-v1` | 35 | Branch granulari Phase A editor (a2..a17b, a3, a3b, a3c, a4, a5, ecc.) — tutti merged via integration |
| `phase-integration-baseline-*` | 15 | Baseline storiche v1..v14 + extras (i loro worktree erano in Phase 6) |
| `worktree-*` | 13 | Branch Claude-internal residui dopo rimozione worktree in Phase 6 |
| `phase-x4-*` | 13 | Step intermedi X.4 Continua/Solaria/Corporate |
| `phase-x5-*` | 11 | Step intermedi X.5 Cornice |
| `phase-2g2x-*` | 8 | Hardening 2g2x (live-preview-policy, business-hardening, audit-differentiation, ecc.) |
| `phase-x6*` | 8 | Step intermedi X.6 Causa |
| `phase-x4b-*` | 4 | Sub-step X.4b corporate-suite layouts |
| `phase-editor-*` (non-`a*`) | 4 | `phase-editor-{foundation, field-targeting-fix, public-customize, ux-live-preview, scroll-media-fix}-v1` (esclusi `a*-v1` e quelli ancora con worktree) |
| `phase-x4a-*` | 2 | Step intermedi X.4a (esclusi i 2 unmerged step0/reentry-plan) |
| `phase-restaurant-*` | 2 | Rollout restaurant |
| `phase-premium-*` | 2 | Premium components + forms polish |
| `phase-pixel-*` | 2 | Pixel perfection + preview coherence |
| `phase-motion-*` | 2 | Motion media pass + optin medical |
| `phase-live-*` | 2 | Live i18n media + motion media |
| `phase-i18n-*` | 2 | Gusto + cardio |
| `phase-ecommerce-*` | 2 | Commerce foundation + experience hardening |
| `phase-catalog-*` | 2 | Stabilization + expansion strategy |
| `phase-business-*` | 2 | i18n completion + live rollout |
| `phase-ultra-*` / `phase-real-estate-`/`law-*` / `phase-public-*` / `phase-pragma-*` / `phase-portfolio-*` / `phase-medical-*` / `phase-luxe-*` / `phase-commerce-*` / `phase-agency-*` | 1 ciascuno (10) | Rollout vari |

**Lista completa nel TSV** `docs/audit/2026-05-13/_inventory_branches.tsv` (riga per riga, ordinabile/filtrabile).

---

## 5. Piano di esecuzione batch (140 in 14 batch da 10)

Ogni batch:
1. Eseguo `git branch -d <name>` per ognuno dei 10 candidati
2. Mostro output (Git restituisce "Deleted branch X (was <sha>)")
3. Verifico: branch count, stato master, stash intatto, tag intatto, worktree count invariato
4. Se un `branch -d` fallisce (es. "not fully merged"), **lo skippo** e lo segnalo come INVESTIGATE — niente `-D`

| Batch | Range | Pattern | Rischio |
|---|---|---|---|
| **A** | 1..10 | mix worktree-* + phase-editor-a*-v1 | basso |
| **B** | 11..20 | phase-editor-a*-v1 (continuazione) | basso |
| **C** | 21..30 | phase-editor-a*-v1 + phase-integration-baseline-v* | basso |
| **D** | 31..40 | phase-integration-baseline-v* (continuazione) | basso |
| **E** | 41..50 | phase-x4-* + phase-x4a-* + phase-x4b-* | basso |
| **F** | 51..60 | phase-x5-* + phase-x6* | basso |
| **G** | 61..70 | phase-x6* (continuazione) + phase-x7* (se any merged) | basso |
| **H** | 71..80 | phase-2g2x-* + phase-business-* + phase-ecommerce-* | basso |
| **I** | 81..90 | phase-medical-* + phase-restaurant-* + phase-portfolio-* | basso |
| **J** | 91..100 | phase-i18n-* + phase-live-* + phase-motion-* | basso |
| **K** | 101..110 | phase-pixel-* + phase-pragma-* + phase-premium-* | basso |
| **L** | 111..120 | phase-catalog-* + phase-commerce-* + phase-luxe-* | basso |
| **M** | 121..130 | phase-public-* + phase-tier-* + phase-ultra-* + phase-audit-* | basso |
| **N** | 131..140 | residui + retake errori | basso |

**Nota:** la ripartizione precisa batch-per-batch sarà determinata dall'ordine alfabetico del TSV `_inventory_branches.tsv` filtrato per `decision == REMOVE`. Posso anche organizzarli per pattern logico (worktree-*, integration-baseline, editor-a, ecc.) se preferisci leggibilità maggiore — fammi sapere quale ordine vuoi.

**Verifiche intermedie dopo ogni batch:**
- `git branch | wc -l` deve essere `158 - 10 * <batch_index>` (assumendo nessun fallimento)
- `git status` → clean su master
- `git rev-parse HEAD` → `bf12943` (invariato)
- `git stash list -n 1` → stash intatto
- `git worktree list --porcelain | grep -c '^worktree '` → 12 (invariato)

**Stop conditions:**
- Più di 1 fallimento `not fully merged` in un singolo batch → fermare e investigare prima di proseguire
- Working tree principale diventa dirty
- HEAD master cambia
- Conta worktree cambia
- Stash sparisce

---

## 6. Branch da NON cancellare (riassunto sicurezza)

- ❌ `master` (mai)
- ❌ Gli 11 branch attaccati ai 12 worktree restanti (Git rifiuta automaticamente)
- ❌ I 6 INVESTIGATE-UNMERGED — investigation separata in futuro (es. tag attic per safety se decidi di rimuoverli)
- ❌ Tutti i 33 branch remoti su `origin` (Phase 7 NON tocca remote)

---

## 7. Rollback

Se vuoi recuperare un branch cancellato:

```
git reflog show <branch-name>    # mostra commit chain
git branch <name> <sha>           # ri-crea il branch dal commit
```

Il reflog conserva i ref cancellati per **90 giorni** (default `gc.reflogExpire`). Dopo, il `git gc` potrebbe rimuovere gli oggetti unreachable.

Per safety extra prima del batch, posso creare un file di backup:

```
git for-each-ref --format='%(refname:short) %(objectname)' refs/heads/ > docs/audit/2026-05-13/_branches_backup_pre_phase7.txt
```

Salva nome + SHA di ogni branch locale prima del cleanup. Se serve recuperarne uno, cerca lo SHA nel file e `git branch <name> <sha>`.

---

## 8. Operazioni NON eseguite in questo plan

- ❌ Nessun branch cancellato
- ❌ Nessun push
- ❌ Nessun stash drop
- ❌ Nessun worktree rimosso
- ❌ Nessun reset/rebase/squash
- ❌ Nessuna modifica al codice
- ❌ Nessun token/credenziale esposto

---

## 9. Domande aperte per te

1. **Ordine di esecuzione preferito**: alfabetico (semplice) o per pattern logico (es. prima tutti `worktree-*`, poi tutti `phase-editor-a*-v1`, ecc.)?
2. **Backup pre-Phase 7**: vuoi che salvi `_branches_backup_pre_phase7.txt` con tutti i 158 ref prima di iniziare? Consigliato — costa zero e dà rollback istantaneo.
3. **Procedo subito dopo tua approvazione del plan**, oppure preferisci che io aspetti un secondo OK separato per ogni batch?
4. **6 INVESTIGATE-UNMERGED**: vuoi che tagghi i loro commit come `attic/<branch-name>-2026-05-13` prima di lasciarli lì (per safety future)? È opzionale; per ora non li tocco.

Aspetto risposte prima di eseguire qualsiasi `git branch -d`.
