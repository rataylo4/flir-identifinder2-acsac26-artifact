#!/usr/bin/env bash
# Claim 4: recurrent exception occurrence — static log-content check.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG="$HERE/../../artifact/logs/exception-log-sanitized.txt"
EMAP="$HERE/../../artifact/EVIDENCE-MAP.md"

if [[ ! -f "$LOG" ]]; then
  echo "FAIL: log not found at $LOG"
  exit 1
fi

python3 "$HERE/check.py" "$LOG" "$EMAP"
