"""Phase 7 inventory: classify local branches into REMOVE / KEEP / INVESTIGATE.

Read-only. Writes a TSV with the verdict for each local branch.
"""
import subprocess
from pathlib import Path

MAIN = Path("C:/tmp/sitoBadr2/marketweb")
OUT = MAIN / "docs/audit/2026-05-13/_inventory_branches.tsv"


def git(*args):
    r = subprocess.run(["git", "-C", str(MAIN), *args], capture_output=True, text=True, timeout=30)
    return r.stdout


# All local branches
all_branches = sorted(
    line.lstrip("*+ ").strip()
    for line in git("branch").splitlines()
    if line.strip()
)

# Worktree-attached branches
wt_branches = set()
for line in git("worktree", "list", "--porcelain").splitlines():
    if line.startswith("branch "):
        wt_branches.add(line.split(" ", 1)[1].replace("refs/heads/", ""))

# Merged in master
merged = {
    line.lstrip("*+ ").strip()
    for line in git("branch", "--merged", "master").splitlines()
    if line.strip()
}

rows = []
for b in all_branches:
    in_wt = b in wt_branches
    is_master = b == "master"
    is_merged = b in merged
    head_short = git("rev-parse", "--short", b).strip()

    if is_master:
        decision = "KEEP-MASTER"
    elif in_wt:
        decision = "KEEP-WORKTREE-ATTACHED"
    elif not is_merged:
        decision = "INVESTIGATE-UNMERGED"
    else:
        decision = "REMOVE"

    rows.append({"branch": b, "head": head_short, "in_wt": in_wt, "merged": is_merged, "decision": decision})

with OUT.open("w", encoding="utf-8") as f:
    f.write("branch\thead\tin_worktree\tmerged\tdecision\n")
    for r in rows:
        f.write(f"{r['branch']}\t{r['head']}\t{r['in_wt']}\t{r['merged']}\t{r['decision']}\n")

from collections import Counter
counts = Counter(r["decision"] for r in rows)
print(f"Total local branches: {len(rows)}")
for k, v in counts.most_common():
    print(f"  {k}: {v}")
print(f"\nNon-REMOVE branches:")
for r in rows:
    if r["decision"] != "REMOVE":
        print(f"  [{r['decision']:25}] {r['branch']} ({r['head']}, merged={r['merged']}, in_wt={r['in_wt']})")
print(f"\nTSV: {OUT}")
