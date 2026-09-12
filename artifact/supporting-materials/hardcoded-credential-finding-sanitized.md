# Hardcoded Administrative Credential — Sanitized Finding Summary

## Evidence and version boundary

A fixed application-level credential pair was identified in decompiled code from the separately obtained 2019.2 firmware image. Authentication using the same pair was tested directly against the assessed physical unit running firmware 2015.1 and succeeded. The resulting authenticated session permitted privileged administrative resource access. During a later bounded validation, one diagnostic log was deleted and its subsequent absence from the resource listing was preserved.

The 2019.2 code evidence establishes the credential pair's code-level origin in that image. The live 2015.1 evidence establishes the observed authentication and bounded administrative effect on the tested unit. These evidence sources do not establish that the 2015.1 and 2019.2 builds are code-identical or that the condition applies to other units.

Neutral source identifiers and hashes are listed in `source-evidence-id-table.md`.

## Finding classification

- **Best-fit CWE:** CWE-798 (Use of Hard-coded Credentials).
- **Author-assessed CVSS v3.1 vector:** `CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:L/A:N`.
- **Author-assessed base score:** 7.1 (High).

The low integrity impact reflects the one bounded diagnostic-log deletion. Successful password modification, firmware installation, and signature bypass were not demonstrated. The scoring is an author assessment and is not independently established by the package's static checks; see `cvss-cwe-scoring-caveat.md`.

## Permanently withheld

- Literal credential values and sensitive usernames.
- Authentication endpoints, request formats, session mechanics, and reproduction steps.
- Credential-bearing captures and authenticated page contents.
- Proprietary assembly, full decompiled output, and verbatim vendor code.

No included file provides a reproduction-ready authentication procedure.
