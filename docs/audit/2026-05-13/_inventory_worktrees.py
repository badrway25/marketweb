"""One-shot inventory of all worktrees: status, branch, HEAD, merged in master.

Read-only. Writes a CSV-like text file for the Phase 6 plan.
"""
import os
import subprocess
import sys
from pathlib import Path

MAIN = Path("C:/tmp/sitoBadr2/marketweb")
OUT = MAIN / "docs/audit/2026-05-13/_inventory_worktrees.tsv"

# Parse worktree list
proc = subprocess.run(
    ["git", "-C", str(MAIN), "worktree", "list", "--porcelain"],
    capture_output=True, text=True, timeout=30,
)
wts = []
cur = {}
for line in proc.stdout.splitlines():
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

print(f"Total worktrees parsed: {len(wts)}")

clean_count = dirty_count = 0
merged_count = unmerged_count = 0
rows = []
for w in wts:
    path = w["path"]
    branch = w.get("branch", "(detached)")
    head = w.get("head", "?")
    short = path.replace("C:/tmp/sitoBadr2/", "").replace("\\", "/")
    is_main = short.rstrip("/") == "marketweb"
    if is_main:
        rows.append({"path": short, "branch": branch, "head": head, "state": "MAIN", "merged": "n/a", "decision": "KEEP"})
        continue
    # status
    r = subprocess.run(["git", "-C", path, "status", "--porcelain"], capture_output=True, text=True, timeout=15)
    clean = r.returncode == 0 and r.stdout.strip() == ""
    state = "CLEAN" if clean else "DIRTY"
    # merged check
    m = subprocess.run(["git", "-C", str(MAIN), "merge-base", "--is-ancestor", head, "master"], capture_output=True, text=True, timeout=15)
    merged = "MERGED" if m.returncode == 0 else "NOT-MERGED"
    # decision
    is_v15 = "mw-integration-baseline-v15" in short
    if is_v15:
        decision = "KEEP-V15-VENV"
    elif state == "DIRTY":
        decision = "INVESTIGATE-DIRTY"
    elif merged == "NOT-MERGED":
        decision = "INVESTIGATE-UNMERGED"
    else:
        decision = "REMOVE"
    rows.append({"path": short, "branch": branch, "head": head[:7], "state": state, "merged": merged, "decision": decision})
    if state == "CLEAN":
        clean_count += 1
    else:
        dirty_count += 1
    if merged == "MERGED":
        merged_count += 1
    else:
        unmerged_count += 1

# Write TSV
with OUT.open("w", encoding="utf-8") as f:
    f.write("path\tbranch\thead\tstate\tmerged\tdecision\n")
    for r in rows:
        f.write(f"{r['path']}\t{r['branch']}\t{r['head']}\t{r['state']}\t{r['merged']}\t{r['decision']}\n")

print(f"CLEAN: {clean_count}, DIRTY: {dirty_count}")
print(f"MERGED: {merged_count}, NOT-MERGED: {unmerged_count}")
print(f"TSV written: {OUT}")

# Group by decision
from collections import Counter
counts = Counter(r["decision"] for r in rows)
print("\nDecisions:")
for k, v in counts.most_common():
    print(f"  {k}: {v}")

# Print details for non-REMOVE
print("\n=== Non-REMOVE worktrees ===")
for r in rows:
    if r["decision"] != "REMOVE":
        print(f"  [{r['decision']:20}] {r['path']} | {r['branch']} | {r['state']} | {r['merged']}")
