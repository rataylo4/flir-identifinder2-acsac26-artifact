# Sanitized Configuration Difference

## Restricted source identifiers

- `config-baseline-001`: canonical configuration export, 173 parsed settings, SHA-256
  `0a755e1faa862b809f4d989379300bb09357c4d9afa9a1c33bd4f5206f386e0a`.
- `config-variant-001`: preserved modified variant, SHA-256
  `729d66beb84e67d8ff120db0328dcf921a7be7f87f1588d82c296063318a0aa8`.

The raw files are withheld because they contain real device and credential-bearing values.
This document is an authored sanitized derivative, not a distributed configuration payload.

## Supported structural result

Offline parsing of the two restricted XML files established that:

- both files are well-formed XML;
- both contain 173 settings in the same category and setting order;
- their root element, root attribute names and values, category structure, setting names,
  and setting attribute sets are equal;
- exactly three parsed numeric setting values differ; and
- all other parsed setting values and element text are unchanged.

The source files use different line-ending serialization, so the files and their unchanged
lines are not described as byte-identical. No vendor XSD validation result is claimed; the
supported result is equality of the parsed structure and field set described above.

## Sanitized difference table

Exact field names and numeric values are withheld because they form part of the operational
payload. Opaque labels preserve the verified cardinality and functional category without
publishing reproduction-ready values.

| Sanitized field label | Functional category | Difference status |
|---|---|---|
| `threshold-field-A` | Numeric alarm threshold | Changed |
| `threshold-field-B` | Numeric alarm threshold | Changed |
| `threshold-field-C` | Numeric neutron warning threshold | Changed |

No alarm-indication Boolean value differs between `config-baseline-001` and
`config-variant-001`.

## Evidentiary limits

- This static comparison does not independently prove that the device accepted the variant.
- `config-variant-001` changes threshold values but does not change an isotope-usage or
  IND/NORM/SNM classification mapping.
- The researcher-identified live-demo scripts are separate restricted evidence. Their
  sanitized provenance is summarized in `live-demo-workflow-provenance-sanitized.md`.
- No raw configuration, credential value, device serial, endpoint, upload field, or
  reproduction-ready payload is distributed.
