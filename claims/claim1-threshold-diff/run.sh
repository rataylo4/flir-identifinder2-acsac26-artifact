#!/usr/bin/env bash
# Claim 1: static check of the sanitized configuration-difference derivative.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DOC="$HERE/../../artifact/configuration/threshold-diff-sanitized.md"
status="PASS"

if [[ ! -f "$DOC" ]]; then
  echo "FAIL: sanitized configuration difference not found"
  exit 1
fi

rows=$(grep -c '^| `threshold-field-[ABC]` |' "$DOC" || true)
if [[ "$rows" -eq 3 ]]; then
  echo "OK: exactly three sanitized changed-field rows found"
else
  echo "FAIL: expected 3 sanitized changed-field rows, found $rows"
  status="FAIL"
fi

if grep -q "same category and setting order" "$DOC" && grep -q "173 settings" "$DOC"; then
  echo "OK: parsed-structure result and setting count present"
else
  echo "FAIL: parsed-structure result or setting count missing"
  status="FAIL"
fi

if grep -q "No vendor XSD validation result is claimed" "$DOC" && grep -q "not described as byte-identical" "$DOC"; then
  echo "OK: XSD and byte-identity limitations present"
else
  echo "FAIL: required XSD/byte-identity limitations missing"
  status="FAIL"
fi

if grep -q "Exact field names and numeric values are withheld" "$DOC"; then
  echo "OK: operational field names and exact values are withheld"
else
  echo "FAIL: operational-value withholding statement missing"
  status="FAIL"
fi

echo "RESULT: $status"
[[ "$status" == "PASS" ]]
