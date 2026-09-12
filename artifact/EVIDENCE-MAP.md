# Evidence Map and Claim Boundaries

Evidence labels:

- **Direct-2015.1:** observed on the tested physical unit running firmware 2015.1.
- **Follow-up-2015.1:** later analysis of preserved evidence from that unit.
- **Researcher provenance:** researcher identification or clarification, not a device-generated execution record.
- **Corroborating-2019.2:** separately examined 2019.2 implementation evidence.
- **Operational implication:** reasoned consequence that was not directly measured.

## 1. Configuration structural comparison

- **Evidence:** `configuration/threshold-diff-sanitized.md`.
- **Supports:** the two restricted XML files are well formed, have the same parsed structure and 173-setting field set, and differ in exactly three parsed numeric setting values.
- **Does not support:** vendor-XSD conformance, byte identity, on-device acceptance, or a semantic classification result.

## 2. Modified-configuration acceptance

- **Evidence:** Follow-up-2015.1 author notes plus researcher provenance identifying the restricted live-demo scripts; `configuration/live-demo-workflow-provenance-sanitized.md`.
- **Supports:** the researcher-documented 2015.1 workflow accepted a modified configuration through the configuration backup/restore process and produced a soft application reset.
- **Does not support:** a device-generated per-import transaction record, an acceptance rate, repeated controlled trials, or restoration after every activity.

## 3. Cs-137 operator-facing semantic states

- **Evidence:** Direct-2015.1 manuscript figure `figures/Semantic manipulation.png`; researcher confirmation that the same physical Cs-137 source was used across the observations; and the sanitized live-demo workflow provenance.
- **Supports:** IND, NORM, and SNM operator-facing states were photographed for the same physical source during the controlled case study. The researcher states that the SNM demonstration reused the NORM suppress workflow with the classification value changed.
- **Does not support:** release of source-identifying provenance, a device-generated import log, repeated-trial statistics, or an inference that sensor measurements themselves were altered. No preserved file contains a separately saved byte-exact SNM payload; the same NORM workflow was reused with the classification value changed.

## 4. Residual visual indication

- **Evidence:** Direct-2015.1 manuscript figure `figures/Alarm-visual fail-safe.png`.
- **Supports:** a residual visual indication was observed under the photographed tested condition.
- **Does not support:** that the mechanism is hardcoded, configuration-independent, or driven by a particular internal signal path. Those mechanisms were not directly measured.

## 5. Firmware-update signature-verification invocation

- **Evidence:** Follow-up-2015.1 minimized device log `logs/firmware-update-log-sanitized.txt`.
- **Supports:** two repeated `Signature check failed` entries confirm that the firmware-update process invoked a signature-verification step for those attempts.
- **Does not support:** cryptographic strength, algorithm or key-management quality, completeness, coverage of every update component, rejection of every attempt, or a definitive final rejection where the final preserved sequence is incomplete.

## 6. Configuration-import handler observation

- **Evidence:** Corroborating-2019.2 prose observation `reverse-engineering/README.md`.
- **Supports:** no signature, checksum, HMAC, or other configuration-integrity verification call is visible in the examined `BackupSettingsPage.HandleUploadedFile` handler.
- **Does not support:** absence of checks elsewhere in `DeserializeSettings` or the pipeline, or code identity between 2015.1 and 2019.2.

## 7. Recurrent exception entries

- **Evidence:** Follow-up-2015.1 minimized log `logs/exception-log-sanitized.txt` and Direct-2015.1 manuscript figure `figures/unhandled_exception.jpg`.
- **Supports:** two occurrences of the same exception at the same recorded stack location, 28 days apart.
- **Does not support:** a controlled trigger-and-reproduce procedure, prevalence, or a quantified availability impact.

## 8. Recovery observations

- **Evidence:** Follow-up-2015.1 author notes and system-log analysis summarized in `methodology/recovery-observations.md`.
- **Supports:** one note explicitly distinguishes a soft application reset from a hard power cycle; another mentions a soft reset; the system log contains generic startup events but no configuration-import-specific entries.
- **Does not support:** per-trial recovery actions, power-cycle attribution, restoration completeness, recovery time, or success rate.

## 9. Telemetry observation

- **Evidence:** Direct-2015.1 qualitative observation recorded in the paper; no standalone packet artifact is distributed.
- **Supports:** exposure of an unencrypted service/channel was observed.
- **Does not support:** decoded operational content, active telemetry manipulation, replay, confidentiality impact, integrity impact, or availability impact.

## 10. Hardcoded administrative credential

- **Evidence:** `supporting-materials/hardcoded-credential-finding-sanitized.md` and the restricted sources identified by hash in `supporting-materials/source-evidence-id-table.md`.
- **Supports:** a fixed application-level credential pair was identified in decompiled code from the separately obtained 2019.2 image; authentication using that pair succeeded on the tested 2015.1 unit; the authenticated session permitted privileged resource access and one bounded diagnostic-log deletion.
- **Does not support:** disclosure of the credential or login procedure, successful password modification, firmware installation, signature bypass, code identity between the two firmware versions, prevalence, or generalization to other units.
- **Scoring status:** the paper reports the author-assessed vector `CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:L/A:N` and base score 7.1 (High). The package checks only the presence and internal consistency of the recorded vector; it does not independently establish severity.

## 11. Operational implications

Potential effects on operator interpretation, escalation, telemetry trust, or downstream workflow are security and safety implications. Unless a specific Direct-2015.1 observation is identified above, these consequences were not directly measured and are not evaluated by the claim scripts in this package.

## Taxonomy and traceability boundary

CVSS scores are author assessments and CWE assignments are best-fit mappings, not independent vendor or CVE-authority determinations. See `supporting-materials/cvss-cwe-scoring-caveat.md` and `supporting-materials/finding_to_evidence_index.csv`.

The repository's historical FLIR Requirement-to-Evidence Traceability exemplar is not distributed here because it is methodology-development material and its own scope states that it is not required for this ACSAC paper. This release candidate uses the evidence map and finding-to-evidence index for paper-artifact traceability; it does not fabricate a retrospective Control-to-Evidence Traceability record.
