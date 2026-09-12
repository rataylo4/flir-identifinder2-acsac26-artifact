# Claim-to-Paper Matrix

This matrix maps the six static artifact checks to the final paper. A passing check establishes
only the released evidence condition and boundary stated below; it does not reproduce a
physical-device experiment or independently validate the paper's conclusions.

| Artifact Claim | Paper Location | Evidence Artifact(s) | Static Check | Evidence Boundary |
|---|---|---|---|---|
| Claim 1: Sanitized configuration structural comparison | Section 5.2, *Phases 3–5: Application, System, and Physical Interface Analysis* | `artifact/configuration/threshold-diff-sanitized.md` | `claims/claim1-threshold-diff/run.sh` | Structural comparison alone does not prove on-device acceptance or semantic effect. It does not establish XSD conformance or byte identity. |
| Claim 2: Cs-137 IND/NORM/SNM semantic observation | Section 5.4, *Phase 7: Vulnerability Analysis and Controlled Exploitation*; Table 3; Figure 2 | `artifact/figures/Semantic manipulation.png`; `artifact/EVIDENCE-MAP.md` (boundary 3); `artifact/configuration/live-demo-workflow-provenance-sanitized.md` | `claims/claim2-semantic-observation/run.sh` | The observations used the same physical Cs-137 source. No full raw-measurement-path integrity, trial-count, or success-rate claim is made. |
| Claim 3: Firmware signature-check log evidence | Section 5.3, *Phase 6: Security Controls Assessment* | `artifact/logs/firmware-update-log-sanitized.txt`; `artifact/EVIDENCE-MAP.md` (boundary 5) | `claims/claim3-firmware-signature-log/run.sh` | Confirms invocation of a signature-verification step only; it does not establish cryptographic strength, completeness, coverage, or final disposition. |
| Claim 4: Recurrent exception observation | Section 5.1, *Phases 0–2: Scope, Reconnaissance, and Enumeration*; Figure 1 | `artifact/logs/exception-log-sanitized.txt`; `artifact/figures/unhandled_exception.jpg`; `artifact/EVIDENCE-MAP.md` (boundary 7) | `claims/claim4-recurrent-exception/run.sh` | Static preserved evidence records two logged occurrences; no reproduction rate, success rate, or controlled trigger-and-reproduce claim is made. |
| Claim 5: Configuration-import handler observation | Section 5.2, *Phases 3–5: Application, System, and Physical Interface Analysis* | `artifact/reverse-engineering/README.md`; `artifact/EVIDENCE-MAP.md` (boundary 6) | `claims/claim5-import-handler-observation/run.sh` | The 2019.2 firmware is corroborating evidence only; the live tested unit ran 2015.1. No code-identity claim is made, and equivalent checks elsewhere cannot be excluded. |
| Claim 6: CVSS record consistency | Section 5 findings lead-in; Table 2 | `artifact/supporting-materials/cvss_cwe_scoring_notes.csv`; `artifact/supporting-materials/hardcoded-credential-finding-sanitized.md`; `artifact/supporting-materials/cvss-cwe-scoring-caveat.md` | `claims/claim6-cvss-record/run.sh` | Verifies internal consistency of the recorded author-assessed CVSS entry; it does not independently validate severity correctness. |

See `artifact/EVIDENCE-MAP.md` for the complete evidence boundaries and
`artifact/EVIDENCE-LINEAGE.md` for the released-evidence lineage model.
