#!/usr/bin/env bash
# Phase 9.A — backup 7 dirty worktrees OUTSIDE the repo.
# Per worktree saves: branch.txt, head.txt, status.txt, diff-stat.txt,
# diff-name-status.txt, tracked.patch, untracked-files.txt, untracked/.
# No git ops, no commit, no push.

set -euo pipefail
BACKUP_ROOT="C:/tmp/sitoBadr2/_marketweb_cleanup_backups/2026-05-13-phase9"
mkdir -p "$BACKUP_ROOT"

dirty_paths=(
  "C:/tmp/sitoBadr2/marketweb/.claude/worktrees/preview-realism"
  "C:/tmp/sitoBadr2/mw-agency-live-rollout-v1"
  "C:/tmp/sitoBadr2/mw-ecommerce-live-rollout-v1"
  "C:/tmp/sitoBadr2/mw-editor-a1-flow-fix-v1"
  "C:/tmp/sitoBadr2/mw-editor-scroll-media-fix-v1"
  "C:/tmp/sitoBadr2/mw-medical-polish-fix-v1"
  "C:/tmp/sitoBadr2/mw-medical-specialist-live-hardening-v2"
)

for wt in "${dirty_paths[@]}"; do
  name=$(basename "$wt" | tr '/' '_')
  out="$BACKUP_ROOT/$name"
  mkdir -p "$out/untracked"
  echo "=== $name → $out ==="

  git -C "$wt" branch --show-current > "$out/branch.txt" 2>&1 || true
  git -C "$wt" rev-parse HEAD > "$out/head.txt" 2>&1 || true
  git -C "$wt" status --short > "$out/status.txt" 2>&1 || true
  git -C "$wt" diff --stat > "$out/diff-stat.txt" 2>&1 || true
  git -C "$wt" diff --name-status > "$out/diff-name-status.txt" 2>&1 || true
  git -C "$wt" diff > "$out/tracked.patch" 2>&1 || true
  git -C "$wt" ls-files --others --exclude-standard > "$out/untracked-files.txt" 2>&1 || true

  # Copy untracked files preserving structure
  while IFS= read -r f; do
    [ -z "$f" ] && continue
    src="$wt/$f"
    dst="$out/untracked/$f"
    mkdir -p "$(dirname "$dst")"
    cp -r "$src" "$dst" 2>/dev/null || true
  done < "$out/untracked-files.txt"

  echo "  branch=$(cat "$out/branch.txt")"
  echo "  head=$(cat "$out/head.txt")"
  echo "  status lines=$(wc -l < "$out/status.txt")"
  echo "  tracked.patch size=$(wc -c < "$out/tracked.patch") bytes"
  echo "  untracked files=$(wc -l < "$out/untracked-files.txt")"
  echo ""
done

echo "=== backup tree ==="
ls -la "$BACKUP_ROOT"
