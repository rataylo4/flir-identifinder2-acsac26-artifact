# Withheld Artifacts

The following categories were reviewed and deliberately excluded from this release candidate.
Restricted paths and operational filenames are not reproduced here.

| Withheld Category | Why Withheld | Released Substitute |
|---|---|---|
| Raw configuration exports | Credential-bearing and device-specific values | `configuration/threshold-diff-sanitized.md` and `configuration/live-demo-workflow-provenance-sanitized.md` |
| Operational/live-demo scripts | Live targets, access/session logic, and automated modification/upload behavior | `configuration/live-demo-workflow-provenance-sanitized.md` and `methodology/experimental-sequence.md` |
| Proprietary firmware and decompiled code bodies | Vendor intellectual property and misuse risk | `reverse-engineering/README.md` and hash-based identifiers in `supporting-materials/source-evidence-id-table.md` |
| Full update, exception, and system logs | Device identifiers and extended operational history | Minimized logs in `logs/` and `methodology/recovery-observations.md` |
| Credential-validation captures | Credentials, session mechanics, and privileged-access detail | `supporting-materials/hardcoded-credential-finding-sanitized.md` and a neutral hash-based identifier |
| Raw/source photographs | Source provenance, labels, activity/reference information, or identifying metadata | Approved metadata-clean manuscript figures where available; otherwise description or hash only |

## Security, privacy, and safety boundary

- Raw configuration exports, because they contain credential-bearing and device-specific values.
- Literal usernames, passwords, PINs, cookies, tokens, authenticated pages, and session captures.
- Exact endpoints, request formats, form-field names, payloads, and reproduction-ready values.
- Live-demo and exploitation scripts, because they contain live targets, access/session logic, and automated modification/upload behavior.
- Packet captures, raw spectra, and full device logs containing extended operational history.
- Raw photographs and the redacted check-source photograph, because source labels, activity/reference information, GPS/device metadata, or other sensitive provenance may remain even where a serial is obscured.
- Terminal history, caches, credentials, private network identifiers, and researcher/institution-identifying metadata.

## Redistribution boundary

- Proprietary firmware images, extracted update members and packages, vendor executables or DLLs, complete decompiled output, and vendor documentation.
- Verbatim proprietary method bodies and materials with unclear third-party redistribution rights.

The package publishes only an author-created prose observation for the examined 2019.2 import handler and hash-based identifiers for restricted sources. It does not grant rights in vendor or third-party materials.

## Description or hash only

- The canonical 2015.1 configuration export and modified variants.
- Full update, exception, and system logs.
- Author notes and restricted validation records.
- The three operational live-demo scripts.
- The separately obtained 2019.2 firmware and extracted/decompiled components.
- Credential-validation captures and the bounded diagnostic-log-deletion record.

Neutral identifiers and hashes are provided in `supporting-materials/source-evidence-id-table.md` where doing so does not disclose an operational secret.

## Known evidence gaps not reconstructed

- No device-generated, per-import transaction record was preserved.
- No separately saved byte-exact SNM script or generated SNM XML is distributed. The researcher records that the NORM workflow was reused with the classification value changed.
- The final preserved firmware-update sequence lacks a recorded final accept/reject result.
- No controlled trigger-and-reproduce record exists for the recurrent exception entries.
- No per-trial restoration or power-cycle record exists.
- Successful password modification, firmware installation, and signature bypass were not demonstrated.

The package does not recreate or infer missing evidence.

## Hardcoded-credential disclosure decision

The manuscript and package include only a high-level sanitized finding description. Literal credential values, sensitive usernames, login/session details, proprietary code, and reproduction instructions are permanently withheld. See `supporting-materials/hardcoded-credential-finding-sanitized.md`.
