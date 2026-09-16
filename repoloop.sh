#!/usr/bin/env bash
# repoloop.sh — build the Brutalist/Liam playlist, one fresh Claude session per film.
# Default: drain the queue. --forever watches for new skills and feedback.
# --dry lists coverage without writes; --prepare creates briefs without invoking Claude.
# --once builds one film; --status reads progress; --stop requests a graceful stop.
# --shorts-only selects the isolated cut-first queue; every Short must be < 3:00.
set -euo pipefail
REPOLOOP_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$REPOLOOP_ROOT/runtime/scripts/repoloop.py" --repo "$REPOLOOP_ROOT" "$@"
