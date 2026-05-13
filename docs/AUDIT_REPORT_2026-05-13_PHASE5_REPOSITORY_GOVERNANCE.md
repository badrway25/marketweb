# Audit Report — Phase 5: Repository Governance Inventory

**Data:** 2026-05-13
**Modalità:** read-only, zero cancellazioni, zero distruttività
**Esito:** inventario completo, classificazione candidati, piano di cleanup futuro (NON eseguito)

---

## 1. Stato attuale della fonte di verità

| Riferimento | Hash | Note |
|---|---|---|
| Local `master` (HEAD del worktree marketweb/) | `040bc5104626cb00eb20913997d03f6282af5ece` | Branch corrente, working tree clean |
| `origin/master` | `040bc5104626cb00eb20913997d03f6282af5ece` | Pubblicato in Phase 4 push 1, == local |
| `origin/phase-integration-baseline-v15` | `040bc5104626cb00eb20913997d03f6282af5ece` | FF avanzato in Phase 4 push 2, == local |
| Tag locale `v0.1-pre-mvp-master-2026-05-13` | tag obj `dc2ff1e0…` → commit `9736da44ad68494308b5ea12063b61a4f3207891` | Pre-MVP snapshot |
| Tag remoto `v0.1-pre-mvp-master-2026-05-13` | identico | Pubblicato in Phase 4 push 3 |
| `stash@{0}` | `On master: WT cosmetic drift on master before FF merge 2026-05-13` | Intatto, contiene solo line-ending drift |
| Default branch remoto (GitHub) | `phase-editor-field-targeting-fix-v1` | **Da cambiare manualmente** su GitHub UI a `master` |
| Working tree | clean | 0 modified, 0 untracked |

---

## 2. Inventario worktree locali

**Totale:** **78 worktree** attivi.

### 2.1 Suddivisione per tipo

| Tipo | Count | Posizione |
|---|---|---|
| Master canonical (la "casa" del repo) | 1 | `C:/tmp/sitoBadr2/marketweb/` |
| Claude internal | 14 | `C:/tmp/sitoBadr2/marketweb/.claude/worktrees/*` |
| Rollout top-level (`mw-*`) | 63 | `C:/tmp/sitoBadr2/mw-*/` |

### 2.2 Worktree → branch (estratto)

| Path | Branch attaccato | Branch è merged in master? | Note |
|---|---|---|---|
| `C:/tmp/sitoBadr2/marketweb` | `master` | n/a (è master) | KEEP — fonte di verità |
| `C:/tmp/sitoBadr2/mw-integration-baseline-v15` | `phase-x7e-lf2-variance-and-causa-retrofit` | sì (FF target) | KEEP — contiene venv attivo `.venv-v15`, base lavoro corrente |
| `C:/tmp/sitoBadr2/mw-integration-baseline-{v1..v14}` | `phase-integration-baseline-v{1..14}` | sì tutti | Archivio storico, candidati alla futura rimozione |
| `C:/tmp/sitoBadr2/mw-editor-*` (10 cartelle) | `phase-editor-*` vari | sì tutti i 10 | Archivio storico Phase A editor work, candidati |
| `C:/tmp/sitoBadr2/mw-business-*` (4 cartelle) | `phase-business-*` / `phase-2g2x-business-*` | sì | Storico business vertical, candidati |
| `C:/tmp/sitoBadr2/mw-medical-*` (3 cartelle) | `phase-medical-*` / `phase-2g2x-medical-*` | sì (con 1 eccezione, vedi §5) | Storico medical vertical |
| `C:/tmp/sitoBadr2/mw-ecommerce-*` (3 cartelle) | `phase-ecommerce-*` | sì | Storico ecommerce |
| `C:/tmp/sitoBadr2/mw-restaurant-*` (2 cartelle) | `phase-restaurant-*` | sì | Storico restaurant |
| `C:/tmp/sitoBadr2/mw-i18n-*` (3 cartelle) | `phase-i18n-*` / `phase-gusto-i18n-*` | sì (con 1 eccezione, vedi §5) | Storico i18n rollout |
| `C:/tmp/sitoBadr2/mw-{audit,catalog,commerce,live-*,motion-*,pixel-*,portfolio-*,premium-*,public-*,tier-*,ultra-*}-*` (vari) | branch `phase-*` corrispondenti | sì | Storico phase-2g/A varie |
| `C:/tmp/sitoBadr2/mw-{agency,law-realestate,luxe-*}-*` (4 cartelle) | `phase-*` rollout | sì | Storico rollout verticali |
| `C:/tmp/sitoBadr2/marketweb/.claude/worktrees/*` (14 cartelle) | `worktree-*` interni | sì tutti i 14 | Uso interno Claude Code, candidati |

**Lista completa:** `git worktree list --porcelain` (output completo non inserito qui per leggibilità — vedi inventory script in §7).

---

## 3. Inventario branch locali

**Totale:** **158 branch locali**.

| Categoria | Count |
|---|---|
| Branch con worktree attaccato | 78 |
| Branch free-standing (senza worktree) | 80 |
| Branch merged in `master` | 149 |
| Branch NOT merged in `master` | 9 |
| Branch attivo (`master`) | 1 |

### 3.1 Branch locali NOT merged in master (9 totali) — da investigare

| Branch | Ultimo commit | Hash | Note |
|---|---|---|---|
| `phase-editor-full-coverage-v1` | 2026-04-16 | `badb98a` | "feat: full editor coverage, live theme sync, page-aware preview, premium search" |
| `phase-i18n-dermatologia-v2` | 2026-04-12 | `9043836` | "feat: extend i18n/RTL to dermatologia-elite-roma (Phase 2i.2)" |
| `phase-medical-specialist-premium-split-v1` | 2026-04-12 | `4e26b3f` | "Visual richness and premium interaction second pass" |
| `phase-x4-continua-build-brief` | 2026-04-29 | `c45c52a` | "Design orchestrator: add first real build brief for Continua candidate" |
| `phase-x4-continua-public-flip` | 2026-04-30 | `8b3ccc1` | "X.5 LF-2: define Cornice fifth sibling pilot and distinctness proof" |
| `phase-x4-solaria-user-visible-passA` | 2026-04-27 | `3cdbef6` | "X.4 Solaria passB: complete multilingual rollout and locale verification" |
| `phase-x4-wave2-solaria-coaching-v1` | 2026-04-21 | `6b70d56` | "fix(catalog): X.4 pilot #2 · solaria-coaching palette polarity" |
| `phase-x4a-corporate-factory-hardening-step0` | 2026-04-24 | `921961f` | "X.4a step1E: add corporate-suite hardening readiness verdict" |
| `phase-x4a-solaria-controlled-reentry-plan` | 2026-04-24 | `cf54efa` | "X.4a step2A: add Solaria controlled re-entry plan and checklist" |

**Interpretazione:** la maggior parte sono branch intermedi (build brief, plan, controlled re-entry, ecc.) il cui lavoro è poi confluito in altri branch via cherry-pick/rebase consolidato sui rollout principali. Vanno verificati uno-a-uno prima di considerare la rimozione.

**Conclusione provvisoria:** non sicuri da rimuovere senza diff-check con master. Vedi §5.

---

## 4. Inventario branch remoti

**Totale:** **33 branch remoti** + il default ref `origin/HEAD`.

| Categoria | Count |
|---|---|
| `origin/master` (nuovo) | 1 |
| `origin/phase-integration-baseline-v15` (FF-aggiornato) | 1 |
| `origin/phase-editor-*` (varianti) | 5 |
| `origin/phase-x4-*` (Continua/Solaria/Corporate) | 6 |
| `origin/phase-x4a-*` / `origin/phase-x4b-*` (corporate factory + LF-5) | 5 |
| `origin/phase-x5-*` (Cornice) | 9 |
| `origin/phase-x6-*` (Causa) | 6 |
| Branch remoti merged in `origin/master` | 32 |
| Branch remoti NOT merged in `origin/master` | 1 — `origin/phase-x4-continua-public-flip` |

### 4.1 Remoti merged in `origin/master` (sicuri come archivio, candidati a rimozione futura)

Lista completa (30 oltre a `origin/master` e `origin/phase-integration-baseline-v15`):

```
origin/phase-editor-a2-5-palette-jump-fix-v1
origin/phase-editor-a2-8-sidebar-hardening-jump-api-v1
origin/phase-editor-field-targeting-fix-v1   ← ATTUALE default branch GitHub
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

### 4.2 Remoto NOT merged

- **`origin/phase-x4-continua-public-flip`** — coincide con un branch locale anche NOT merged. Potrebbe contenere lavoro intermedio non integrato. **Da investigare prima di toccare.**

---

## 5. Classificazione finale

### 5.1 SICURI DA ARCHIVIARE / CANDIDATI ALLA RIMOZIONE (NON rimuoverli ora)

**Criterio:** merged in `master` (locale o `origin/master` rispettivamente), nessun lavoro unico residuo, worktree non più attivo per il flusso corrente.

- **Worktree locali** (76 candidati — tutti tranne `marketweb/` e `mw-integration-baseline-v15/`):
  - 14 sotto `.claude/worktrees/*` (uso interno Claude Code, branch `worktree-*`)
  - 62 sotto `mw-*` (escluso v15) — branch `phase-*` tutti merged in master
- **Branch locali free-standing** (80 totali) tutti merged in master:
  - I `phase-editor-a*-v1` (~24 branch granular dell'editor Phase A) — tutti merged
  - I `phase-x4*-*` / `phase-x5*-*` / `phase-x6*-*` step intermedi (~25 branch) — tutti merged
  - I `phase-integration-baseline-v15` orphan (= il branch del worktree v15, già in master via FF) e qualsiasi altro free-standing merged
- **Branch remoti merged in `origin/master`** (30 candidati, esclusi `origin/master` e `origin/phase-integration-baseline-v15`):
  - vedi lista §4.1
  - **MA con un'eccezione operativa:** `origin/phase-editor-field-targeting-fix-v1` è l'attuale **default branch** del repo GitHub. Cambia il default a `master` PRIMA di considerarne la rimozione, altrimenti GitHub blocca la cancellazione.

### 5.2 DA TENERE (mai rimuovere senza causa esplicita)

- **`master`** locale + `origin/master` — fonte di verità
- **`origin/phase-integration-baseline-v15`** — branch di integrazione storica, può servire come "secondo punto di verità" per chi ha già cloni con quel branch. Anche se ridondante con master, è gratis tenerlo
- **`mw-integration-baseline-v15/`** worktree locale — contiene il venv attivo `.venv-v15`, le screenshots di QA, ed è la base di lavoro della sessione corrente. Solo dopo cleanup pianificato e sostituzione del venv si può rimuovere
- **Tag `v0.1-pre-mvp-master-2026-05-13`** — storico, non si rimuove (locale + remoto)
- **`stash@{0}`** — autorizzato a non droppare in questa fase

### 5.3 DA INVESTIGARE (NON toccare senza diff-review)

- I **9 branch locali NOT merged in master** (vedi §3.1) — verifica con `git log master..<branch>` e `git diff master <branch>` per ogni branch prima di decidere
- **`origin/phase-x4-continua-public-flip`** remoto (l'unico NOT merged in `origin/master`)
- Il **commit pre-MVP `9736da44`** taggato come `v0.1-pre-mvp-master-2026-05-13` è **diverso** dall'antenato lineare di v15. La storia di v15 passa attraverso commit precedenti (`8ef3970`, `caa1384`, ecc.) ma NON include `9736da44` come merge base diretto: il tag è una "fotografia" dello stato locale del vecchio master, non un commit di v15. **Non rimuovere il tag** anche se i branch corrispondenti vengono archiviati

### 5.4 RISCHIOSI / NON TOCCARE

- `marketweb/.git/worktrees/<name>/` metadata interni di Git: NON manipolare a mano
- Le screenshot `*.png` nei worktree: ignorate via `.gitignore`, ma se cancelli un worktree perdi anche le sue screenshot locali (irrecuperabili senza ri-fare la QA)
- Il **default branch remoto** `phase-editor-field-targeting-fix-v1` su GitHub: se vuoi rimuoverlo, devi PRIMA cambiare il default a `master` da GitHub UI, altrimenti GitHub rifiuta la delete
- Il venv `.venv-v15` dentro `mw-integration-baseline-v15/` — se rimuovi quel worktree, devi ricostruire il venv in `marketweb/` o altrove prima
- Eventuali screenshots / `qa-*.png` accumulate durante le Fasi 1-4 (gitignored, ma utili come reference visiva)

---

## 6. Piano operativo cleanup futuro (proposta, NON eseguita)

### Batch A — Worktree + branch Claude-internal (basso rischio)
**Trigger:** rimozione 14 worktree sotto `.claude/worktrees/*` e relativi branch `worktree-*`. Tutti merged in master, uso esaurito.

```
# Per ciascuno dei 14:
git worktree remove .claude/worktrees/<name>
git branch -d worktree-<name>
```

### Batch B — Worktree rollout `phase-integration-baseline-v{1..14}` (medio rischio)
**Trigger:** rimozione 14 worktree intermedi + i loro branch. Tutti merged in master.

```
# Per ciascuno di v1..v14:
git worktree remove ../mw-integration-baseline-v<N>
git branch -d phase-integration-baseline-v<N>
```

### Batch C — Worktree editor Phase A (`mw-editor-*`)
**Trigger:** 10 worktree dell'editor Phase A, tutti merged. Da fare DOPO la conferma che Phase A non riprenderà da uno di questi worktree.

```
# Per ciascuno dei 10:
git worktree remove ../mw-editor-<suffix>
git branch -d phase-editor-<suffix>
```

### Batch D — Worktree rollout verticali (medical/restaurant/business/ecommerce/agency/lawyer/portfolio/real-estate)
**Trigger:** ~24 worktree storici di rollout, tutti merged in master.

### Batch E — Free-standing branches (no worktree associato)
**Trigger:** 80 branch locali senza worktree, di cui ~75 merged in master.

```
# Per i merged (NON i 9 not-merged):
git branch -d <branch-name>
```

### Batch F — Branch remoti merged
**Trigger:** 30 branch remoti merged in `origin/master`. Da fare **dopo** aver cambiato il default branch GitHub a `master`.

```
# Per ciascuno (eccetto origin/master e origin/phase-integration-baseline-v15):
git push origin --delete <remote-branch>
```

### Batch G — Investigazione + decisione sui 9 not-merged
**Trigger:** per ognuno dei 9 branch locali NOT merged + `origin/phase-x4-continua-public-flip`:
```
git log master..<branch> --oneline
git diff master <branch> --stat
```
Confronto con `SESSION_LOG.md` / `DECISIONS.md` per capire se contengono lavoro recuperabile o solo intermediate iterations.

**Ordine consigliato:** A → B → C → D → E → F → G. Sempre con tuo OK esplicito per ogni batch.

---

## 7. Conferma finale Fase 5

| Verifica | Esito |
|---|---|
| Nessun branch locale cancellato | ✅ |
| Nessun branch remoto cancellato | ✅ |
| Nessun worktree rimosso | ✅ |
| Nessun reset/rebase/squash/force | ✅ |
| Nessuna modifica al codice del progetto | ✅ (eccetto questo report) |
| Nessun drop dello stash | ✅ `stash@{0}` ancora presente |
| Nessuna modifica al remote URL | ✅ HTTPS, invariato |
| Working tree clean | ✅ |
| Default branch GitHub non cambiato da CLI | ✅ ancora `phase-editor-field-targeting-fix-v1` (da cambiare manualmente da te su UI) |
| Nessun token/credenziale stampato in chat o log | ✅ |

**Stato Git finale (post Fase 5):**
- Branch corrente: `master`
- HEAD locale: `040bc5104626cb00eb20913997d03f6282af5ece`
- HEAD `origin/master`: `040bc5104626cb00eb20913997d03f6282af5ece`
- HEAD `origin/phase-integration-baseline-v15`: `040bc5104626cb00eb20913997d03f6282af5ece`
- Tag locale + remoto `v0.1-pre-mvp-master-2026-05-13` → `9736da44ad68494308b5ea12063b61a4f3207891`
- `stash@{0}: On master: WT cosmetic drift on master before FF merge 2026-05-13`
- 78 worktree
- 158 branch locali
- 33 branch remoti
- 2 tag remoti totali (questo + `a2-4-deterministic-field-targeting-stable` già preesistente)

---

## 8. Raccomandazione successiva

1. **Manuale su GitHub UI:** cambia il default branch da `phase-editor-field-targeting-fix-v1` a `master`. Operazione 10 secondi su `github.com/badrway25/marketweb/settings/branches`. Sblocca tutti i batch successivi.

2. **Decidi se vuoi affrontare il cleanup batch-by-batch ora** o rimandarlo a una sessione futura. Vista la quantità (76 worktree + 80 free-standing + 30 remote candidati), serve almeno 1-2 ore dedicate. Posso suggerire di farlo solo nel momento in cui il PC inizia a sentire l'overhead (file system, IDE indexing).

3. **In alternativa** (zero pulizia, focus tecnico): passare a Phase A Editor Foundation, oppure ai fix incrementali RR3-RR5 (registry magre, travel pending, favicon), oppure all'audit UI/UX premium sui 33 brand.

4. **Cosa rimando esplicitamente:** drop `stash@{0}`, cleanup ruff/black, eliminazione branch/worktree, modifica default branch da CLI — tutto richiede tua autorizzazione separata.
