# Evidence Lineage

The artifact uses the following bounded lineage for released claim support:

```text
Original/restricted observation
    -> research evidence record
    -> sanitized derivative
    -> artifact claim
    -> static verifier
    -> bounded paper claim
```

The evidence classes carried through this lineage are:

- **Direct-2015.1:** observed on the tested physical unit running firmware 2015.1.
- **Follow-up-2015.1:** later analysis of preserved evidence from that unit.
- **Researcher provenance:** researcher identification or clarification rather than a
  device-generated execution record.
- **Corroborating-2019.2:** evidence from the separately examined 2019.2 firmware; it is not
  direct evidence of code identity with the tested 2015.1 unit.
- **Operational implication:** a reasoned consequence that was not directly measured.

Sanitization and static verification preserve traceability while narrowing what the release can
establish. They do not transform corroborating evidence into direct evidence, convert an
implication into an observed result, or reproduce the physical-device experiment. See
`artifact/EVIDENCE-MAP.md` for claim-specific support and exclusions.
