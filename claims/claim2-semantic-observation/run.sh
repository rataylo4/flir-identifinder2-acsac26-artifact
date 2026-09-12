#!/usr/bin/env bash
# Claim 2: Cs-137 semantic-observation boundary — static consistency check.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FIG="$HERE/../../artifact/figures/Semantic manipulation.png"
SUMS="$HERE/../../artifact/checksums/SHA256SUMS.txt"
EMAP="$HERE/../../artifact/EVIDENCE-MAP.md"

status="PASS"

if [[ ! -f "$FIG" ]]; then
  echo "FAIL: figure not found at $FIG"
  status="FAIL"
else
  echo "OK: figure present"
fi

if command -v sha256sum >/dev/null 2>&1; then
  HASHER="sha256sum"
else
  HASHER="shasum -a 256"
fi

if [[ -f "$FIG" && -f "$SUMS" ]]; then
  actual_hash=$($HASHER "$FIG" | awk '{print $1}')
  if grep -q "$actual_hash" "$SUMS"; then
    echo "OK: figure hash matches an entry in SHA256SUMS.txt"
  else
    echo "FAIL: figure hash $actual_hash not found in SHA256SUMS.txt"
    status="FAIL"
  fi
fi

if [[ -f "$EMAP" ]]; then
  if grep -q "## 3\. Cs-137" "$EMAP"; then
    echo "OK: boundary 3 present in EVIDENCE-MAP.md"
  else
    echo "FAIL: boundary 3 heading not found"
    status="FAIL"
  fi
  if grep -qi "no preserved file" "$EMAP" || grep -qi "not claimed as the source" "$EMAP"; then
    echo "OK: exact-payload-not-preserved limitation language present"
  else
    echo "FAIL: expected limitation language not found"
    status="FAIL"
  fi
else
  echo "FAIL: EVIDENCE-MAP.md not found"
  status="FAIL"
fi

echo "RESULT: $status"
[[ "$status" == "PASS" ]]
