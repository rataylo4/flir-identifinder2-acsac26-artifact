#!/usr/bin/env bash
# Offline prerequisite and full-package integrity verification.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MANIFEST="$ROOT/artifact/checksums/SHA256SUMS.txt"

echo "=== FLIR identiFINDER2 ACSAC 2026 artifact verification ==="

for tool in bash python3; do
  if ! command -v "$tool" >/dev/null 2>&1; then
    echo "FAIL: required tool not found: $tool"
    exit 1
  fi
done

if command -v sha256sum >/dev/null 2>&1; then
  HASH_CHECK=(sha256sum -c)
elif command -v shasum >/dev/null 2>&1; then
  HASH_CHECK=(shasum -a 256 -c)
else
  echo "FAIL: sha256sum or shasum is required"
  exit 1
fi

if [[ ! -f "$MANIFEST" ]]; then
  echo "FAIL: checksum manifest not found"
  exit 1
fi

if find "$ROOT" -type l -print -quit | grep -q .; then
  echo "FAIL: symbolic links are not permitted in this package"
  exit 1
fi

echo "OK: required local tools are available"
echo "OK: package contains no symbolic links"

(
  cd "$ROOT"
  "${HASH_CHECK[@]}" artifact/checksums/SHA256SUMS.txt
)

echo "OK: every file listed in the full-package manifest matches"
echo "Verification complete. No network or device access was used."
