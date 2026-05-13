"""Phase 8 — read-only inventory of residual repository state.

Produces 3 TSV files for the Phase 8 report:
  _inventory_residual_worktrees.tsv
  _inventory_residual_branches.tsv
  _inventory_remote_branches.tsv
"""
import subprocess
from pathlib import Path

MAIN = Path("C:/tmp/sitoBadr2/marketweb")
OUT = MAIN / "docs/audit/2026-05-13"


def git(*args, cwd=None):
    r = subprocess.run(
        ["git", "-C", str(cwd or MAIN), *args],
        capture_output=True, text=True, timeout=60,
    )
    return r.stdout, r.stderr, r.returncode


# ── 1. WORKTREES ─────────────────────────────────────────────────
out, _, _ = git("worktree", "list", "--porcelain")
wts = []
cur = {}
for line in out.splitlines():
    if line.startswith("worktree "):
        if cur:
            wts.append(cur)
        cur = {"path": line.split(" ", 1)[1]}
    elif line.startswith("HEAD "):
        cur["head"] = line.split(" ", 1)[1]
    elif line.startswith("branch "):
        cur["branch"] = line.split(" ", 1)[1].replace("refs/heads/", "")
if cur:
    wts.append(cur)


def classify_worktree(w):
    path = w["path"].replace("\\", "/")
    branch = w.get("branch", "(detached)")
    head = w.get("head", "?")
    short = path.replace("C:/tmp/sitoBadr2/", "")
    is_main = short.rstrip("/") == "marketweb"
    is_v15_venv = "mw-integration-baseline-v15" in short

    status_out, _, _ = git("status", "--porcelain", cwd=path)
    is_clean = (status_out.strip() == "")
    n_dirty = len(status_out.splitlines())

    untracked_out, _, _ = git("ls-files", "--others", "--exclude-standard", cwd=path)
    n_untracked = len([x for x in untracked_out.splitlines() if x])

    m_out, _, m_rc = git("merge-base", "--is-ancestor", head, "master")
    merged = (m_rc == 0)

    if is_main:
        klass = "KEEP-MAIN"
    elif is_v15_venv:
        klass = "KEEP-V15-VENV"
    elif not is_clean and merged:
        if all("?? " in line or " M " in line for line in status_out.splitlines()):
            klass = "DIRTY-NEEDS-PATCH-BACKUP"
        else:
            klass = "DIRTY-NEEDS-STASH"
    elif is_clean and not merged:
        klass = "UNMERGED-NEEDS-REVIEW"
    elif is_clean and merged:
        klass = "REMOVE-SAFE-LATER"
    else:
        klass = "DO-NOT-TOUCH"

    return {
        "path": short,
        "branch": branch,
        "head": head[:7],
        "clean": "CLEAN" if is_clean else "DIRTY",
        "n_dirty": n_dirty,
        "n_untracked": n_untracked,
        "merged": "MERGED" if merged else "NOT-MERGED",
        "klass": klass,
    }


rows = [classify_worktree(w) for w in wts]
with (OUT / "_inventory_residual_worktrees.tsv").open("w", encoding="utf-8") as f:
    f.write("path\tbranch\thead\tclean\tn_dirty\tn_untracked\tmerged\tclass\n")
    for r in rows:
        f.write(f"{r['path']}\t{r['branch']}\t{r['head']}\t{r['clean']}\t{r['n_dirty']}\t{r['n_untracked']}\t{r['merged']}\t{r['klass']}\n")
print(f"Worktrees: {len(rows)} rows")
for r in rows:
    print(f"  [{r['klass']:25}] {r['path']:60} | {r['branch']:55} | {r['clean']} ({r['n_dirty']}) | {r['merged']}")


# ── 2. RESIDUAL LOCAL BRANCHES ───────────────────────────────────
all_local = [
    line.lstrip("*+ ").strip()
    for line in git("branch")[0].splitlines() if line.strip()
]
wt_branches = {w.get("branch") for w in wts}

# For each non-master branch, compute upstream, ahead/behind, merged, attached-worktree
branch_rows = []
for b in sorted(all_local):
    if b == "master":
        continue
    sha = git("rev-parse", "--short", b)[0].strip()
    upstream = git("rev-parse", "--abbrev-ref", "--symbolic-full-name", b + "@{upstream}")[0].strip()
    if upstream and not upstream.startswith("fatal"):
        ahead = git("rev-list", "--count", f"{upstream}..{b}")[0].strip()
        behind = git("rev-list", "--count", f"{b}..{upstream}")[0].strip()
    else:
        upstream = "(none)"
        ahead = behind = "n/a"
    in_wt = b in wt_branches
    m_out, _, m_rc = git("merge-base", "--is-ancestor", b, "master")
    merged = (m_rc == 0)
    if in_wt:
        klass = "WORKTREE-ATTACHED"
    elif not merged:
        klass = "INVESTIGATE-UNMERGED"
    elif upstream != "(none)" and behind != "n/a" and behind != "0":
        klass = "INVESTIGATE-UPSTREAM-DRIFT"
    else:
        klass = "OTHER"
    branch_rows.append({
        "branch": b, "sha": sha, "upstream": upstream,
        "ahead": ahead, "behind": behind, "in_wt": in_wt,
        "merged": "MERGED" if merged else "NOT-MERGED", "klass": klass,
    })

with (OUT / "_inventory_residual_branches.tsv").open("w", encoding="utf-8") as f:
    f.write("branch\tsha\tupstream\tahead\tbehind\tin_worktree\tmerged\tclass\n")
    for r in branch_rows:
        f.write(f"{r['branch']}\t{r['sha']}\t{r['upstream']}\t{r['ahead']}\t{r['behind']}\t{r['in_wt']}\t{r['merged']}\t{r['klass']}\n")
print(f"\nResidual local branches: {len(branch_rows)} rows")
for r in branch_rows:
    print(f"  [{r['klass']:25}] {r['branch']:50} | {r['sha']} | upstream={r['upstream']:60} | ahead={r['ahead']:>3} behind={r['behind']:>3} | merged={r['merged']:10} | in_wt={r['in_wt']}")


# ── 3. REMOTE BRANCHES ───────────────────────────────────────────
remote_branches = [
    line.strip()
    for line in git("branch", "-r")[0].splitlines()
    if line.strip() and "->" not in line  # skip "origin/HEAD -> origin/master"
]
remote_rows = []
for rb in sorted(remote_branches):
    sha = git("rev-parse", "--short", rb)[0].strip()
    m_out, _, m_rc = git("merge-base", "--is-ancestor", rb, "origin/master")
    merged = (m_rc == 0)
    points_at_master = (git("rev-parse", rb)[0].strip() == git("rev-parse", "origin/master")[0].strip())
    is_master = rb == "origin/master"
    is_v15 = rb == "origin/phase-integration-baseline-v15"
    is_old_default = rb == "origin/phase-editor-field-targeting-fix-v1"
    if is_master:
        klass = "KEEP-MASTER-REMOTE"
    elif is_v15:
        klass = "KEEP-V15-REMOTE"
    elif is_old_default:
        klass = "FORMER-DEFAULT-CANDIDATE-REMOVE-LATER"
    elif not merged:
        klass = "REMOTE-UNMERGED"
    else:
        klass = "REMOTE-MERGED-CANDIDATE-REMOVE-LATER"
    remote_rows.append({
        "remote": rb, "sha": sha,
        "merged_in_origin_master": "MERGED" if merged else "NOT-MERGED",
        "points_at_master": points_at_master,
        "klass": klass,
    })
with (OUT / "_inventory_remote_branches.tsv").open("w", encoding="utf-8") as f:
    f.write("remote_branch\tsha\tmerged_in_origin_master\tpoints_at_master\tclass\n")
    for r in remote_rows:
        f.write(f"{r['remote']}\t{r['sha']}\t{r['merged_in_origin_master']}\t{r['points_at_master']}\t{r['klass']}\n")
print(f"\nRemote branches: {len(remote_rows)} rows")
from collections import Counter
counts = Counter(r["klass"] for r in remote_rows)
for k, v in counts.most_common():
    print(f"  {k}: {v}")
