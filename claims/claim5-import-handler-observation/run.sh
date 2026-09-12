#!/usr/bin/env bash
# Claim 5: configuration-import handler observation — static document-consistency check.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DOC="$HERE/../../artifact/reverse-engineering/README.md"

if [[ ! -f "$DOC" ]]; then
  echo "FAIL: reverse-engineering README not found at $DOC"
  exit 1
fi

python3 "$HERE/check.py" "$DOC"
