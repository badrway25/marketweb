# Audit Report — Phase 8: Residual Governance Investigation

**Data:** 2026-05-13
**Modalità:** read-only, zero cancellazioni
**Esito:** mappa completa di worktree/branch residui + raccomandazioni Phase 9

---

## 1. Stato master / local / origin

| Item | Valore |
|---|---|
| Branch corrente | `master` |
| HEAD locale | `0599a358393d1e19f90d4fe6cc545b9475951747` |
| `origin/master` | `0599a358393d1e19f90d4fe6cc545b9475951747` |
| Sync local ↔ origin | ✅ |
| Working tree principale | clean (1 file untracked nel `marketweb/` corrisponde a docs/audit script — vedi §3) |
| Stash | `stash@{0}: On master: WT cosmetic drift on master before FF merge 2026-05-13` |
| Tag locali | `v0.1-pre-mvp-master-2026-05-13`, `a2-4-deterministic-field-targeting-stable` |
| Worktree | 12 |
| Branch locali | 21 |
| Branch remoti | 33 (esclusa `origin/HEAD` simbolica) |

---

## 2. Stato default branch GitHub

✅ `git remote show origin` riporta **`HEAD branch: master`**.

Default branch è stato correttamente cambiato manualmente su GitHub.

---

## 3. Worktree rimasti (12)

Inventario dettagliato in `docs/audit/2026-05-13/_inventory_residual_worktrees.tsv`.

| # | Path | Branch | HEAD | Stato | n dirty | merged | **Classe** |
|---|---|---|---|---|---|---|---|
| 1 | `marketweb` | `master` | `0599a35` | DIRTY (1) | 1 | MERGED | **KEEP-MAIN** |
| 2 | `marketweb/.claude/worktrees/preview-realism` | `worktree-preview-realism` | `6239d33` | DIRTY (5) | 5 | MERGED | **DIRTY-NEEDS-STASH** |
| 3 | `mw-agency-live-rollout-v1` | `phase-agency-live-rollout-v1` | `9cef9a7` | DIRTY (8) | 8 | MERGED | **DIRTY-NEEDS-PATCH-BACKUP** |
| 4 | `mw-ecommerce-live-rollout-v1` | `phase-ecommerce-live-rollout-v1` | `f35b4e5` | DIRTY (1) | 1 | MERGED | **DIRTY-NEEDS-PATCH-BACKUP** |
| 5 | `mw-editor-a1-flow-fix-v1` | `phase-editor-a1-flow-fix-v1` | `aa06d0b` | DIRTY (5) | 5 | MERGED | **DIRTY-NEEDS-PATCH-BACKUP** |
| 6 | `mw-editor-full-coverage-v1` | `phase-editor-full-coverage-v1` | `badb98a` | CLEAN | 0 | NOT-MERGED | **UNMERGED-NEEDS-REVIEW** |
| 7 | `mw-editor-scroll-media-fix-v1` | `phase-editor-scroll-media-fix-v1` | `1f4310b` | DIRTY (16) | 16 | MERGED | **DIRTY-NEEDS-PATCH-BACKUP** |
| 8 | `mw-i18n-dermatologia-v2` | `phase-i18n-dermatologia-v2` | `9043836` | CLEAN | 0 | NOT-MERGED | **UNMERGED-NEEDS-REVIEW** |
| 9 | `mw-integration-baseline-v15` | `phase-x7e-lf2-variance-and-causa-retrofit` | `ab88d16` | CLEAN | 0 | MERGED | **KEEP-V15-VENV** |
| 10 | `mw-medical-polish-fix-v1` | `phase-medical-polish-fix-v1` | `623405b` | DIRTY (1) | 1 | MERGED | **DIRTY-NEEDS-PATCH-BACKUP** |
| 11 | `mw-medical-specialist-live-hardening-v2` | `phase-2g2x-medical-specialist-live-hardening-v2` | `0a5bcf2` | DIRTY (8) | 8 | MERGED | **DIRTY-NEEDS-PATCH-BACKUP** |
| 12 | `mw-medical-specialist-premium-split-v1` | `phase-medical-specialist-premium-split-v1` | `4e26b3f` | CLEAN | 0 | NOT-MERGED | **UNMERGED-NEEDS-REVIEW** |

**Nota su #1 `marketweb/` DIRTY (1):** il file untracked è `docs/audit/2026-05-13/_phase8_inventory.py` (lo script di inventory di questa fase) — non un drift reale. Verrà committato insieme ai 3 TSV.

### 3.1 Sintesi worktree

| Classe | Count |
|---|---|
| KEEP-MAIN | 1 |
| KEEP-V15-VENV | 1 |
| DIRTY-NEEDS-STASH | 1 |
| DIRTY-NEEDS-PATCH-BACKUP | 6 |
| UNMERGED-NEEDS-REVIEW | 3 |

### 3.2 Dettaglio DIRTY-NEEDS-STASH (1)
**`marketweb/.claude/worktrees/preview-realism`** — solo file *modified* (M), nessun untracked. Stash candidato:
- 4 docs (`AGENT_HANDOFF.md`, `DECISIONS.md`, `SESSION_LOG.md`, `TODO_NEXT.md`)
- 1 codice (`apps/catalog/management/commands/generate_previews.py`)
**Azione consigliata:** `git -C <path> stash push -u -m "preview-realism wip backup"` prima della rimozione futura.

### 3.3 Dettaglio DIRTY-NEEDS-PATCH-BACKUP (6)
Worktree con mix di file modified + untracked. Per ognuno, prima della rimozione futura, salvare:
- `git -C <path> diff > <backup>.patch` (per file tracciati modificati)
- `tar -czf <backup-untracked>.tar.gz $(git -C <path> ls-files --others --exclude-standard)` (per untracked)

| Path | Dirty | Composizione |
|---|---|---|
| `mw-agency-live-rollout-v1` | 8 | tutti untracked: 8 screenshot JPG `aura-*.jpeg` |
| `mw-ecommerce-live-rollout-v1` | 1 | 1 untracked: `.claude/scheduled_tasks.lock` (lock file residuo) |
| `mw-editor-a1-flow-fix-v1` | 5 | 5 modified: codice (`generate_previews.py`, `catalog/views.py`, `projects/services.py`, `projects/tests.py`, `_navbar.html`) |
| `mw-editor-scroll-media-fix-v1` | 16 | mix: docs di sessione + `apps/editor/schema.py` e altri |
| `mw-medical-polish-fix-v1` | 1 | 1 untracked: directory `audit/` (vecchi report locali) |
| `mw-medical-specialist-live-hardening-v2` | 8 | 8 modified: codice catalog (template_content, template_dna, theme_safety, specialist/_base.html, ecc.) |

### 3.4 Dettaglio UNMERGED-NEEDS-REVIEW (3)
Worktree clean ma HEAD non raggiungibile da master.

| Path | Branch | Commit unico vs master | Diff stat (file/+/-) |
|---|---|---|---|
| `mw-editor-full-coverage-v1` | `phase-editor-full-coverage-v1` | `badb98a` "feat: full editor coverage, live theme sync, page-aware preview, premium search" | 880 file, +14k / -254k |
| `mw-i18n-dermatologia-v2` | `phase-i18n-dermatologia-v2` | `9043836` "feat: extend i18n/RTL to dermatologia-elite-roma (Phase 2i.2)" | 1137 file, +8k / -412k |
| `mw-medical-specialist-premium-split-v1` | `phase-medical-specialist-premium-split-v1` | `4e26b3f` "Visual richness and premium interaction second pass" | 1137 file, +9k / -411k |

**Lettura:** i 3 sono fork antichi (aprile 2026) divergenti molto presto. Le enormi rimozioni indicano che master oggi contiene più codice. I commit unici potrebbero essere già stati rifusi via altri branch o esplicitamente lasciati fuori. Investigazione caso-per-caso prima di toccare.

---

## 4. Branch locali rimasti (21)

Inventario completo in `docs/audit/2026-05-13/_inventory_residual_branches.tsv`. Master escluso dal TSV.

### 4.1 Sintesi classi

| Classe | Count |
|---|---|
| KEEP-MASTER (non in TSV) | 1 |
| WORKTREE-ATTACHED | 11 |
| INVESTIGATE-UNMERGED | 6 |
| INVESTIGATE-LOCAL-AHEAD-OF-UPSTREAM | 3 |

### 4.2 WORKTREE-ATTACHED (11)
Non cancellabili finché il loro worktree esiste. Vedi §3 per i worktree.

### 4.3 INVESTIGATE-UNMERGED (6) — free-standing, niente upstream

Tutti con commit non in master. Ogni branch ha 1-5 commit unici. Tutti mostrano **enormi rimozioni** vs master = storia divergente antica.

| # | Branch | SHA | Commit unici | Diff vs master |
|---|---|---|---|---|
| 1 | `phase-x4-continua-build-brief` | `c45c52a` | 1 (Design orchestrator brief) | 519 file, +7,8k / -157k |
| 2 | `phase-x4-continua-public-flip` | `8b3ccc1` | 1 (Cornice fifth sibling pilot) | 420 file, +7,4k / -138k |
| 3 | `phase-x4-solaria-user-visible-passA` | `3cdbef6` | 1 (Solaria passB multilingual) | 672 file, +8,9k / -174k |
| 4 | `phase-x4-wave2-solaria-coaching-v1` | `6b70d56` | 2 (solaria-coaching fix + draft) | 807 file, +6,3k / -197k |
| 5 | `phase-x4a-corporate-factory-hardening-step0` | `921961f` | 5 (step1A..1E corporate-suite hardening) | 788 file, +8,0k / -190k |
| 6 | `phase-x4a-solaria-controlled-reentry-plan` | `cf54efa` | 1 (X.4a step2A re-entry plan) | 783 file, +7,8k / -187k |

**Nota:** `phase-x4-continua-public-flip` ha anche upstream `origin/phase-x4-continua-public-flip` sincrono (ahead=0/behind=0). I commit unici sono "fotografie" antiche di lavoro che è stato poi rifuso in master attraverso altri rami (X.4-X.5-X.6 release pipeline).

### 4.4 INVESTIGATE-LOCAL-AHEAD-OF-UPSTREAM (3)

⚠️ Correzione semantica vs Phase 7 report: questi branch **non hanno upstream-drift**. Sono **locali ahead** del proprio upstream, e Git rifiuta `branch -d` per non perdere commit non-pushati. Sono tutti merged in master, quindi i loro commit sono già consolidati altrove.

| # | Branch | SHA | Upstream | Ahead | Behind | Commit unici (locale vs upstream) |
|---|---|---|---|---|---|---|
| 1 | `phase-editor-a2-5-palette-jump-fix-v1` | `507cb0b` | `origin/phase-editor-a2-5-palette-jump-fix-v1` | 2 | 0 | `507cb0b` "A.2.6b indexed-row contract", `14247ee` "A.2.6a 23 contatti scalar+dict-key fields" |
| 2 | `phase-x4-solaria-passB-multilingual` | `6997885` | `origin/phase-x4-solaria-passB-multilingual` | 1 | 0 | `6997885` "Design orchestrator: premium template foundation and skill usage policy" |
| 3 | `phase-x6-causa-step1-planner-brief` | `8f9c06c` | `origin/phase-x6-causa-step1-planner-brief` | 1 | 0 | `8f9c06c` "X.6 step1: define Causa planner brief and prebuild proof" |

**Significato:** locali sono ahead del remoto = i 2/1/1 commit sono nei branch locali ma non sono mai stati pushati su `origin/<stesso>`. Tutti contenuti in `master` (merged), quindi nessun lavoro va perso se si elimina il branch — i commit sono già nella mainline.

---

## 5. Branch remoti (32 — esclusa `origin/HEAD`)

Inventario completo in `docs/audit/2026-05-13/_inventory_remote_branches.tsv`.

### 5.1 Sintesi classi

| Classe | Count |
|---|---|
| KEEP-MASTER-REMOTE | 1 (`origin/master`) |
| KEEP-V15-REMOTE | 1 (`origin/phase-integration-baseline-v15`) |
| FORMER-DEFAULT-CANDIDATE-REMOVE-LATER | 1 (`origin/phase-editor-field-targeting-fix-v1`) |
| REMOTE-MERGED-CANDIDATE-REMOVE-LATER | 28 |
| REMOTE-UNMERGED | 1 (`origin/phase-x4-continua-public-flip`) |

### 5.2 Da TENERE (2)
- `origin/master` — fonte di verità remota
- `origin/phase-integration-baseline-v15` — backup storico aggiornato in Phase 4

### 5.3 Ex-default rimosso a livello UI ma branch ancora presente (1)
- `origin/phase-editor-field-targeting-fix-v1` — era il default branch su GitHub fino a Phase 5.1, ora demoted a branch "feature" normale. **Candidato alla rimozione** (è merged in `origin/master`), ma da rimuovere solo dopo conferma esplicita che nessun PR/issue è ancora aperto su quel branch.

### 5.4 Remote merged candidates (28)
Tutti i restanti branch `phase-*` sul remoto, mergiati in `origin/master`. Sicuri da rimuovere via `git push origin --delete <branch>` (con OK per ogni batch).

Lista completa (28):
```
origin/phase-editor-a2-5-palette-jump-fix-v1
origin/phase-editor-a2-8-sidebar-hardening-jump-api-v1
origin/phase-x4-continua-pass1-review-lock
origin/phase-x4-continua-passB-multilingual-lf5
origin/phase-x4-continua-workflowD-release-decision
origin/phase-x4-corporate-suite-case-parent-fix
origin/phase-x4-solaria-passB-multilingual
origin/phase-x4a-corporate-factory-hardening-followup
origin/phase-x4b-continua-lf5-it-rebuild
origin/phase-x4b-corporate-suite-family-backfill
origin/phase-x4b-corporate-suite-layout-divergence
origin/phase-x4b-corporate-suite-layout-regression-walk
origin/phase-x5-cornice-a3-imagery-curation
origin/phase-x5-cornice-a4-copy-authoring
origin/phase-x5-cornice-a5-it-build
origin/phase-x5-cornice-a6-it-review-lock
origin/phase-x5-cornice-postflip-consolidation
origin/phase-x5-cornice-public-flip
origin/phase-x5-cornice-step2-paper-promotion
origin/phase-x5-cornice-workflowC-multilingual
origin/phase-x5-cornice-workflowD-release-decision
origin/phase-x5-post-cornice-reference-hardening
origin/phase-x6-causa-a3-imagery
origin/phase-x6-causa-a4-copy
origin/phase-x6-causa-a5-it-build
origin/phase-x6-causa-a6-it-review-lock
origin/phase-x6-causa-step1-planner-brief
origin/phase-x6-sixth-sibling-intake
```

### 5.5 Remote UNMERGED (1) — DA INVESTIGARE
- `origin/phase-x4-continua-public-flip` — non merged in `origin/master`. Coincide con il branch locale omonimo (anche lui INVESTIGATE-UNMERGED).
- Diff vs `origin/master`: 1 commit unico `8b3ccc1` "X.5 LF-2: define Cornice fifth sibling pilot and distinctness proof".
- Verosimilmente il lavoro è stato consolidato in master tramite il branch `phase-x5-lf2-fifth-sibling-pilot` (cancellato in Phase 7). Ma il commit unico ha un messaggio diverso, quindi Git non lo vede come merged.
- **NON rimuovere prima dell'investigazione manuale.**

---

## 6. Raccomandazione Phase 9 (NON eseguita)

### 9.A — Worktree DIRTY backup + cleanup (7 worktree)

Per ognuno dei 6 DIRTY-NEEDS-PATCH-BACKUP + 1 DIRTY-NEEDS-STASH:

1. `git -C <path> diff > docs/audit/2026-05-13/wip_<short>_modified.patch` (se ha file modified)
2. Archive untracked files via tar.gz (se ha untracked)
3. Verifica i patch/tar in `docs/audit/2026-05-13/`
4. `git -C <path> reset --hard HEAD` (con OK utente — distruttivo) o `git -C <path> stash push -u -m "..."`
5. `git worktree remove <path>`
6. `git branch -d <branch>` (se rimasto, ma alcuni dovrebbero scomparire con il worktree)

### 9.B — Worktree UNMERGED-NEEDS-REVIEW (3 worktree)

Per ognuno:
1. Verificare se il commit unico è già in master via `git log --grep="<keywords>"` su master.
2. Se sì → safe da rimuovere worktree + branch (con OK).
3. Se no → cherry-pick in master OR creare tag `attic/<name>-2026-05-13` per safety, poi rimuovere.

### 9.C — Branch INVESTIGATE-LOCAL-AHEAD-OF-UPSTREAM (3 branch)

Soluzione più pulita: **pushare i commit locali al remoto** per allineare, poi `git branch -d` riuscirebbe. Ma è inutile se i remoti devono comunque essere cancellati in §9.E.

Alternativa: **eliminare anche il remoto** prima, così `git branch -d` non rifiuterà più. Sequenza:
1. `git push origin --delete <remote-branch>` (per ognuno dei 3)
2. `git branch -d <local-branch>`

**Rischio:** se i remoti contengono commit non locali, perderemmo lavoro. Verifica:
- `phase-editor-a2-5-palette-jump-fix-v1`: behind=0 → upstream non ha commit unici, safe.
- `phase-x4-solaria-passB-multilingual`: behind=0 → safe.
- `phase-x6-causa-step1-planner-brief`: behind=0 → safe.

Tutti safe.

### 9.D — Branch INVESTIGATE-UNMERGED (6 branch)

Tutti contengono commit non in master, ma diff stats mostrano divergenza antica con perdite massive — è probabile che siano fork "morti" pre-X.4. Decisione:
1. Creare tag `attic/<branch-name>-2026-05-13` per safety (conserva il commit anche dopo delete)
2. Poi `git branch -D <branch>` (sì, `-D` è necessario qui perché Git non vede merged status)

Se preferisci approccio non distruttivo (no `-D`):
- Cherry-pick i singoli commit in un branch `attic` mantenuto vivo, poi delete con `-d`. Più lavoro per scarso valore.

### 9.E — Remote cleanup (29 branch remoti)

Sequenza consigliata, in batch da 10-15:
1. **Prima** `origin/phase-editor-field-targeting-fix-v1` (ex-default) — singolo, atomico
2. **Poi** i 28 `REMOTE-MERGED-CANDIDATE-REMOVE-LATER` in batch
3. **Lasciare per ultimo** `origin/phase-x4-continua-public-flip` (REMOTE-UNMERGED) — dopo investigazione

Comando per ognuno: `git push origin --delete <branch-name>`.

### 9.F — Worktree v15 e venv

Solo dopo che gli altri cleanup sono completi:
1. Creare `marketweb/.venv` (o equivalente in `marketweb/`) + `pip install -r requirements.txt`
2. Verificare `manage.py check` verde da `marketweb/`
3. Rimuovere worktree `mw-integration-baseline-v15`
4. `git branch -d phase-x7e-lf2-variance-and-causa-retrofit`

### 9.G — Pulizia finale
1. `git worktree prune` (metadata residue)
2. `git stash drop stash@{0}` (cosmetic drift, già documentato in patch)
3. Opzionalmente `git gc --prune=now --aggressive`

---

## 7. Elementi da NON toccare (mai senza OK esplicito)

- `master` (locale e remoto)
- `origin/phase-integration-baseline-v15`
- I tag `v0.1-pre-mvp-master-2026-05-13` e `a2-4-deterministic-field-targeting-stable`
- `stash@{0}` finché non confermi drop
- Il worktree `marketweb/` (principale)
- I 60+ worktree già rimossi in Phase 6 (non recuperabili senza ricreare)

---

## 8. Conferme di sicurezza Phase 8

| Conferma | Esito |
|---|---|
| Nessuna cancellazione di branch (locale o remoto) | ✅ |
| Nessuna cancellazione di worktree | ✅ |
| Nessun reset/rebase/squash | ✅ |
| Nessun drop stash | ✅ |
| Nessun force push | ✅ |
| Nessuna modifica al codice del progetto | ✅ |
| Solo file nuovi sotto `docs/audit/2026-05-13/` | ✅ (4 file: 3 TSV + 1 script Python) + questo report |
| Zero token/credenziali stampati | ✅ |

---

## 9. Stato Git finale

```
On branch master
nothing to commit, working tree clean (modulo i file di Phase 8 che verranno committati)

HEAD = 0599a358393d1e19f90d4fe6cc545b9475951747
origin/master = 0599a358393d1e19f90d4fe6cc545b9475951747
21 branch locali (invariato)
33 branch remoti (invariato)
12 worktree (invariato)
stash@{0}: On master: WT cosmetic drift on master before FF merge 2026-05-13
tag v0.1-pre-mvp-master-2026-05-13 → 9736da44ad68494308b5ea12063b61a4f3207891
```

Attendo tuo OK per Phase 9 (cleanup finale).
