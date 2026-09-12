# Local Release-Readiness Audit

Audit date: 2026-09-08

Scope: `flir-identifinder2-acsac26-artifact` only. The original evidence tree was not modified. Review was static and offline; no device or external service was accessed.

| Area | Result | Evidence reviewed |
|---|---|---|
| Secrets and cached credentials | Pass | Restricted credential-bearing values were compared without publishing them; no match was found. No key, token, cookie, environment file, history, cache, or credential store is included. |
| IP and MAC addresses | Pass | No IPv4, IPv6, or MAC address was found in release content. |
| Researcher/institution identifiers | Pass | No researcher name, email, user-home path, or institution-identifying path was found. |
| Embedded paths and terminal history | Pass | No restricted repository path, user-home path, terminal-session transcript, or command history is included. |
| Filenames | Pass | No release filename contains a device/source serial, live address, username, token, capture suffix, or restricted operational script name. |
| EXIF and document properties | Pass | The three included images contain no reviewed GPS, author, owner, serial, software identifier, or local-path metadata. No Office document or PDF is included in the artifact package. |
| Screenshots/figures | Pass | All three included figures were visually reviewed. No credential, network address, researcher identity, readable source serial, activity/reference data, or terminal content is visible. A small non-readable portion of the check-source collar appears in one panel. |
| Proprietary/vendor content | Pass with documented boundary | No firmware, executable, DLL, archive, vendor documentation, or decompiled code is included. Product names/logos and bounded prose observations remain; no trademark or vendor-content license is granted. |
| Claims and evidence boundaries | Pass | Static claims match minimized derivatives; unsupported trial counts, definitive firmware rejection, configuration-pipeline-wide absence, and cross-version code identity are not claimed. |
| Git history | Pass | The dedicated repository uses standalone history and does not import the parent research-repository history. |
| Symlinks and hidden files | Pass | No symbolic link or hidden release-content entry is present. |
| Network behavior | Pass | Static inspection found no network client/import or process-launch behavior in package executables. Standalone tests require no device or network access. |

## Deliberately retained identifiers

- `910383-2524 Settings.xml` appears in the overview solely to distinguish the accepted 2015.1 configuration workflow from the separate 2019.2 firmware evidence; the file is not distributed.
- Assembly, type, and handler names needed for the bounded 2019.2 observation are retained without proprietary code.
- SHA-256 source identifiers are retained for evidence traceability; hashes do not grant redistribution rights.
- Complete CVSS v3.1 vectors and author-assessed scores are retained as manuscript metadata with explicit scoring caveats.

## Release notes

- The researcher approved public release of the sanitized package on 2026-09-08.
- Public accessibility should be confirmed after the repository owner changes the GitHub visibility setting.
- Zenodo archival remains a later, separately reviewed action.
- The NORM-to-SNM statement remains researcher provenance; no separate byte-exact SNM artifact exists.

Current conclusion: technically sanitized, mechanically testable, and approved for public
release. Zenodo archival remains subject to the steps listed in `RELEASE-READINESS.md`.
