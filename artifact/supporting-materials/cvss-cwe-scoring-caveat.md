# CVSS and CWE Scoring Boundary

`cvss_cwe_scoring_notes.csv` records the authors' current CVSS v3.1 assessments. Scored rows contain complete base vectors and numerical base scores; evidence-limited rows are explicitly marked `Not scored` and `Not rated`.

The static artifact checks can confirm that the recorded vectors are structurally complete and internally consistent with the table. They do not independently prove exploitability, impact, prevalence, or the correctness of the authors' metric judgments. Potential safety or operational consequences that were not directly demonstrated are not added to CVSS impact.

Every CWE identifier in the package is a best-fit assessor mapping unless a stronger status is explicitly documented. Identifier existence was checked against the repository's pinned MITRE CWE 4.20 archive (SHA-256 `3976f599e5e5200219a3108bb896d06e2a88fbb293369e1883cb423a5e9d7d50`). This check does not confirm the applicability of a particular mapping. No CVE assignment is claimed.
