# Live-Demo Workflow Provenance — Sanitized

On 2026-08-24, the researcher identified three preserved operational scripts as the scripts
used during the physical-device live demonstration on the tested 2015.1 unit. The scripts
remain in restricted evidence because they contain live-device targets, credential/session
workflow material, exact endpoints, payload-generation logic, and automated upload behavior.

Neutral identifiers and SHA-256 hashes are provided for traceability:

| Evidence ID | SHA-256 | Sanitized role |
|---|---|---|
| `live-demo-script-001` | `16fc208263a94de44184270c403a2e21a54da007dfdb61d51da15625a08b18d5` | Threshold-modification workflow |
| `live-demo-script-002` | `94460c013f508a6094916ebeaaa72cdb1df1ababa0f5d0f6a760771fd98afd7c` | Suppress/classification workflow with alarm-indication changes |
| `live-demo-script-003` | `9daf22a16f0bd8593396c76df641e61f11642f6423055d83dbd3f69f5c2ade20` | Suppress/classification workflow preserving alarm indications |

Offline, non-networked execution of only the payload-generation functions against the
canonical baseline deterministically generated one three-value threshold variant and two
classification variants. Exact generated values and operational files are not distributed.

The researcher clarified that the SNM demonstration reused the same suppress-script workflow
used for NORM by changing the classification value from `NORM` to `SNM`; no separate SNM
script was created or required. The scripts as preserved contain the NORM form. No separately
saved, byte-exact SNM-edited script or generated SNM XML file was located.

This is researcher-provided workflow provenance, not a device-generated execution record.
The scripts alone do not prove which generated output was accepted during a particular run,
and no HTTP response transcript, configuration-import log, or per-run output is published.
