#!/usr/bin/env bash
# Single offline entrypoint for package-integrity and static-claim review.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

./install.sh

claim_scripts=(claims/*/run.sh)
expected_claims=6

if [[ ! -e "${claim_scripts[0]}" ]]; then
  echo "FAIL: no claim-check scripts found"
  exit 1
fi

if [[ "${#claim_scripts[@]}" -ne "$expected_claims" ]]; then
  echo "FAIL: expected $expected_claims claim checks, found ${#claim_scripts[@]}"
  exit 1
fi

claim_count=0
for script in "${claim_scripts[@]}"; do
  echo
  echo "=== Running $script ==="
  bash "$script"
  claim_count=$((claim_count + 1))
done

echo
echo "ARTIFACT REVIEW SUMMARY"
echo "Package integrity: PASS"
echo "Claim checks: $claim_count/$expected_claims PASS"
echo
echo "These checks validate the released sanitized evidence and documented claim boundaries."
echo "They do not reproduce the original physical-device experiments."
