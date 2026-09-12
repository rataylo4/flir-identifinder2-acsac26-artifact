FLIR identiFINDER2 ACSAC 2026 Artifact Package
Safety-Aware Security Assessment of a Fielded Radiation Detection Device

STATUS: APPROVED FOR PUBLIC RELEASE

REVIEWER-FIRST EVALUATION

A. 5-MINUTE REVIEW

From the package root, run:

  ./review.sh

The expected final summary is:

  ARTIFACT REVIEW SUMMARY
  Package integrity: PASS
  Claim checks: 6/6 PASS

A PASS confirms that the released files match the package checksums and that all six static
claim checks satisfy their documented, bounded conditions. It does not reproduce or rerun the
original physical-device experiments. This is static, sanitized evidence support: no network
access, physical device, proprietary runtime, or third-party Python packages are required. The
expected runtime is under one minute.

B. 30-MINUTE REVIEW

After running ./review.sh, review the paper-to-artifact mappings and release boundaries in:

  artifact/CLAIM-TO-PAPER-MATRIX.md
  artifact/EVIDENCE-MAP.md
  artifact/SANITIZATION-MANIFEST.csv
  artifact/WITHHELD-ARTIFACTS.md
  claims/

C. FULL REVIEW

For the methodology, provenance, and release-control detail, continue with:

  artifact/methodology/
  artifact/supporting-materials/
  artifact/reverse-engineering/
  infrastructure/evidence-boundary.txt
  infrastructure/release-audit.md

The researcher approved the package licensing terms, figure redistribution, the bounded
2019.2 reverse-engineering description, dedicated GitHub repository creation, and later
Zenodo use on 2026-08-24. On 2026-09-08, the researcher reviewed the sanitized package and
approved it for public release. The package is hosted in its dedicated GitHub repository.
Zenodo archival has not yet occurred.

PURPOSE

This package provides sanitized evidence derivatives and deterministic static checks for
review of bounded claims from the associated paper. It does not reproduce the original
physical-device assessment and is not presented as a Results Reproduced artifact. The
intended initial evaluation scope is artifact availability, documentation, internal
consistency, and evidence traceability.

EVIDENCE BOUNDARIES

- Live-device observations apply only to the tested physical unit running firmware 2015.1.
- The accepted modified-configuration workflow used the device configuration identified in
  the restricted record as 910383-2524 Settings.xml. Raw configuration files and their
  credential-bearing values are not distributed.
- Firmware-update logs support only that repeated "Signature check failed" entries confirm
  invocation of a signature-verification step. They do not establish cryptographic strength,
  completeness, coverage, or a definitive final rejection where the record is incomplete.
- Reverse-engineering evidence comes from a separately obtained 2019.2 firmware image and is
  corroborating only. It is not proof that the 2015.1 and 2019.2 builds are code-identical.
- Operational consequences not directly measured are labeled as implications, not results.
- This is a controlled single-device qualitative case study. No prevalence, trial-count,
  success-rate, uncertainty, or cross-device generalizability claim is made.

PACKAGE LAYOUT

  artifact/        Sanitized evidence derivatives, evidence maps, manifests, and checksums.
  infrastructure/  Execution constraints, access limitations, hosting plan, and readiness.
  claims/          Static checks with claim.txt, run.sh, and expected output.
  install.sh       Verifies prerequisites and full-package SHA-256 integrity.
  review.sh        Single entrypoint for integrity verification and all six claim checks.
  metadata.toml    Machine-readable package metadata and claim/path index.
  README.txt       This overview and execution guide.
  license.txt      Researcher-approved content-specific license terms.
  use.txt          Intended-use, safety, and evidentiary limitations.

artifact/ARTIFACT-MANIFEST.csv inventories the non-index evidence/document files under
artifact/. The manifest does not list itself or the checksum index. The full-package
artifact/checksums/SHA256SUMS.txt covers every regular release-content file except the
checksum index itself, avoiding a self-referential hash. Local `.git` control metadata is not
release content and is excluded from the checksum scope.

RUNNING THE STATIC CHECKS

From the package root:

  ./review.sh

Requirements: Linux or macOS with a Bash-compatible shell, Python 3 standard library,
and sha256sum or shasum. No network, device, compiler, decompiler, proprietary software,
GUI, or third-party Python package is required. Expected runtime is under one minute.

INTERPRETING PASS RESULTS

A PASS means that the included sanitized file has the documented structure, hash, or bounded
content. It does not mean the corresponding live-device experiment was rerun, that a physical
result was independently reproduced, or that a withheld operational artifact was examined by
the evaluator. See artifact/EVIDENCE-MAP.md and infrastructure/evidence-boundary.txt.

SANITIZATION AND WITHHOLDING

The package excludes credentials, sensitive usernames, session material, live/private network
identifiers, operational scripts and payloads, proprietary firmware/software, raw photographs,
sensitive source provenance, researcher-identifying paths/metadata, and material with unclear
redistribution rights. See artifact/SANITIZATION-MANIFEST.csv and
artifact/WITHHELD-ARTIFACTS.md.

LICENSING

The researcher approved CC BY 4.0 for eligible author-created documentation and sanitized
research derivatives, and MIT for eligible author-created code, on 2026-08-24. Manuscript
figures are approved for distribution in this package but are not relicensed by license.txt.
Third-party and vendor material is not relicensed.

PUBLICATION STATE

The dedicated GitHub repository is connected as the local `origin`. The standalone
repository does not import the parent research-repository history. Public release was
authorized by the researcher on 2026-09-08. infrastructure/hosting-plan.txt records the
repository-maintenance and archival controls. No Zenodo record or upload has been created.
