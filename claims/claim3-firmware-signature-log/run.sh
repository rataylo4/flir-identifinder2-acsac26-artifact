#!/usr/bin/env bash
# Claim 3: firmware signature-check log evidence — static log-content check.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG="$HERE/../../artifact/logs/firmware-update-log-sanitized.txt"

if [[ ! -f "$LOG" ]]; then
  echo "FAIL: log not found at $LOG"
  exit 1
fi

python3 "$HERE/check.py" "$LOG"
