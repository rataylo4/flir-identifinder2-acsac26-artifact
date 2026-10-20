# ACSAC 2026 Research Artifact — FLIR identiFINDER2 Security Assessment

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23507383.svg)](https://doi.org/10.5281/zenodo.23507383)

**Archived version:** `v1.0.0` · **Released:** October 20, 2026  
**Authors:** Roshane Taylor, Michael Nowatkowski, Anthony Rizi  
**Associated paper:** *Safety-Aware Security Assessment of a Fielded Radiation Detection Device: The FLIR identiFINDER2* (ACSAC 2026)

This repository contains a **sanitized, evidence-traceable research artifact** and six deterministic static claim checks. It is intended for artifact review, documentation, and bounded claim verification; the checks **do not reproduce the original physical-device experiments**.

## Quick review

In the repository root, on Linux or macOS:

```bash
./review.sh
```

Successful verification ends with `Package integrity: PASS` and `Claim checks: 6/6 PASS`. See the [full reviewer instructions](README.txt) for requirements, scope, and limitations.

## Links

- **[Permanent v1.0.0 archive (Zenodo DOI)](https://doi.org/10.5281/zenodo.23507383)**
- [GitHub v1.0.0 release](https://github.com/rataylo4/flir-identifinder2-acsac26-artifact/releases/tag/v1.0.0)
- [Full artifact README and evaluation guide](README.txt)
- [Claim-to-paper matrix](artifact/CLAIM-TO-PAPER-MATRIX.md) and [evidence map](artifact/EVIDENCE-MAP.md)
- [Content-specific licensing and third-party rights](license.txt)
- [Machine-readable citation metadata](CITATION.cff)

**Citation:** Use the DOI-linked **archived v1.0.0 version** for ACSAC 2026. The `main` branch may receive later documentation improvements; the archived v1.0.0 release is unchanged.
