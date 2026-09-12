#!/usr/bin/env python3
"""Check only the internal consistency of the sanitized CVSS record."""

import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent
SUPPORT = HERE / "../../artifact/supporting-materials"
VECTOR = "CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:L/A:N"

with (SUPPORT / "cvss_cwe_scoring_notes.csv").open(newline="", encoding="utf-8") as handle:
    rows = list(csv.DictReader(handle))

matching = [row for row in rows if row["Primary CWE"] == "CWE-798"]
if len(matching) != 1:
    raise SystemExit(f"FAIL: expected one CWE-798 row, found {len(matching)}")

row = matching[0]
if (row["CVSS v3.1 vector"], row["Author-assessed base score"], row["Severity"]) != (
    VECTOR,
    "7.1",
    "High",
):
    raise SystemExit("FAIL: CWE-798 vector, score, or severity does not match the approved record")
print("OK: CWE-798 CSV row records the complete vector, 7.1 score, and High severity")

summary = (SUPPORT / "hardcoded-credential-finding-sanitized.md").read_text(encoding="utf-8")
if VECTOR not in summary or "7.1 (High)" not in summary:
    raise SystemExit("FAIL: sanitized finding summary does not match the CSV")
print("OK: sanitized finding summary matches the CSV")

caveat = (SUPPORT / "cvss-cwe-scoring-caveat.md").read_text(encoding="utf-8")
if "author" not in caveat.lower() or "do not independently prove" not in caveat:
    raise SystemExit("FAIL: author-assessment limitation is missing")
print("OK: author-assessment limitation is present")
print("RESULT: PASS")
