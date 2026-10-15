#!/bin/bash
# git-sync.sh — commit local changes, pull remote changes, push. Safe for cron.
# Usage: ./git-sync.sh [folder]   (defaults to the folder this script lives in)

set -uo pipefail
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:$PATH"   # cron has a bare PATH

REPO_DIR="${1:-$(cd "$(dirname "$0")" && pwd)}"
NAME="$(basename "$REPO_DIR")"
LOG_DIR="$HOME/Library/Logs/git-sync"
LOG="$LOG_DIR/$NAME.log"
LOCK="/tmp/git-sync-$NAME.lock"
MAX_MB=95   # GitHub rejects files >100MB

mkdir -p "$LOG_DIR"
log()  { echo "$(date '+%Y-%m-%d %H:%M:%S') [$NAME] $*" >> "$LOG"; }
fail() {
  log "ERROR: $*"
  osascript -e "display notification \"$*\" with title \"git-sync: $NAME\"" 2>/dev/null
  exit 1
}

# One run at a time
mkdir "$LOCK" 2>/dev/null || { log "already running, skipping"; exit 0; }
trap 'rmdir "$LOCK"' EXIT

cd "$REPO_DIR" || fail "cannot cd to $REPO_DIR"
git rev-parse --is-inside-work-tree >/dev/null 2>&1 || fail "not a git repo"

GITDIR="$(git rev-parse --git-dir)"
if [ -d "$GITDIR/rebase-merge" ] || [ -d "$GITDIR/rebase-apply" ] || [ -f "$GITDIR/MERGE_HEAD" ]; then
  fail "repo is mid-merge/rebase — fix manually"
fi

BRANCH="$(git symbolic-ref --short HEAD 2>/dev/null)" || fail "detached HEAD — check out a branch"

# 1. Commit local changes (scoped to this folder only)
if [ -n "$(git status --porcelain -- .)" ]; then
  git add -A -- .

  # Guard against files GitHub will reject
  BIG=""
  while IFS= read -r f; do
    [ -f "$f" ] || continue
    size=$(stat -f%z "$f")
    if [ "$size" -gt $((MAX_MB * 1024 * 1024)) ]; then BIG="$BIG $f"; fi
  done < <(git diff --cached --name-only --relative)
  if [ -n "$BIG" ]; then
    git reset -q
    fail "files over ${MAX_MB}MB, add to .gitignore:$BIG"
  fi

  git commit -q -m "auto-sync: $(date '+%Y-%m-%d %H:%M')" >> "$LOG" 2>&1 || fail "commit failed"
  log "committed local changes"
fi

# 2. Pull remote changes
git fetch -q origin >> "$LOG" 2>&1 || fail "fetch failed (network or auth)"
if git rev-parse --verify -q "origin/$BRANCH" >/dev/null; then
  if ! git rebase -q --autostash "origin/$BRANCH" >> "$LOG" 2>&1; then
    git rebase --abort >> "$LOG" 2>&1
    fail "conflict with remote — local commit kept, rebase aborted, resolve manually"
  fi
fi

# 3. Push
git push -q -u origin "$BRANCH" >> "$LOG" 2>&1 || fail "push failed"
log "synced $BRANCH @ $(git rev-parse --short HEAD)"
