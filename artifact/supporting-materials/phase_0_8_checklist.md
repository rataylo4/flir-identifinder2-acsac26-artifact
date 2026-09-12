# Sanitized Nine-Phase Assessment Checklist

This checklist is intentionally non-operational and omits device-specific commands, endpoints, payloads, credentials, and implementation details.

| Phase | Focus | Safe reviewer-visible outputs |
|---:|---|---|
| 0 | Scope, Safety, and Ground Rules | Assessment boundaries, lab isolation, safety constraints, ethical controls, stop conditions. |
| 1 | Reconnaissance and OSINT | Device identity, documentation baseline, vendor/manual references, initial risk hypotheses. |
| 2 | Interface, Network, and Service Enumeration | Exposed interfaces, service categories, communication paths, instability observations, rate-limiting notes. |
| 3 | Application and Ecosystem Interface Analysis | Authentication/authorization observations, web-interface hardening issues, import/export workflow risks. |
| 4 | Firmware, Embedded System, and Supply Chain Analysis | Firmware/update artifact categories, configuration artifact categories, provenance notes, legacy platform observations. |
| 5 | Hardware and Physical Interface Enumeration | USB/removable media paths, hardware-facing interfaces, physical access assumptions, non-destructive inspection notes. |
| 6 | Security Controls Assessment | Controls that held, controls that failed or weakened trust, partial protections, fail-safe observations. |
| 7 | Vulnerability Analysis and Tiered Controlled Validation | Controlled validation categories, observable impacts, safety stop conditions, sanitized figure evidence. |
| 8 | Risk Assessment, Reporting, and Disclosure | CWE/CVSS-informed prioritization, mitigation guidance, disclosure-ready findings, artifact-withholding rationale. |

## Safety controls used across phases

- Isolated laboratory network with no production connectivity.
- Researcher-controlled device and authorized check-source use.
- Rate-limited interaction with legacy or fragile services.
- Stop conditions for instability, unexpected crash behavior, or unrecoverable device state.
- Non-destructive hardware review.
- Sanitized public reporting of effects rather than reproduction-ready exploit procedures.
