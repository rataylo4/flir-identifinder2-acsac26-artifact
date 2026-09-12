# Experimental Sequence (Research-Method Level)

This describes the general shape of the validation sequence behind the paper's
configuration-integrity finding, at a method level. Specific endpoints, credentials, request
formats, and payload contents are withheld — see `../WITHHELD-ARTIFACTS.md`.

## Sequence

1. **Baseline capture.** The device's configuration was exported through its standard,
   vendor-supported backup workflow and preserved as the canonical baseline
   (`config-baseline-001`).
2. **Baseline behavioral observation.** With the device in its baseline configuration, a
   known Cs-137 check source was presented and the resulting classification/alarm behavior
   was recorded (figure evidence).
3. **Targeted modification.** A small number of numeric alarm-threshold fields were changed
   in an exported configuration. `../configuration/threshold-diff-sanitized.md` documents the
   exact three-field difference for one preserved variant; other preserved variants changed a
   different small set of numeric and/or boolean fields (documented by hash only).
4. **Restore.** A modified configuration was submitted back to the device through the same
   supported backup/restore workflow used in step 1.
5. **Modified-state behavioral observation.** With the same physical Cs-137 check source
   presented under materially the same conditions as step 2, the resulting
   classification/alarm behavior was recorded again and is reported in the manuscript's
   figure.
6. **Comparison.** Baseline and modified-state observations were compared to characterize
   the semantic/alarm-behavior effect of configuration change alone, without firmware
   modification.
7. **Independent firmware-update-path check.** Separately from the configuration workflow
   above, update attempts using a repacked firmware image were submitted through the
   device's firmware update path. See `../logs/firmware-update-log-sanitized.txt`.
8. **Independent reverse-engineering check.** A separately obtained firmware image (a
   different version than the tested device) was examined offline to understand the
   configuration-import code path. This is corroborating, version-bounded evidence — see
   `../reverse-engineering/README.md`.

## Evidentiary limitation — read before citing step 4/5 as a captured transaction

No HTTP response transcript, per-import device log, post-import configuration export, or
per-trial hash was preserved for the configuration-restore step. Acceptance of the modified
configuration on the tested 2015.1 device is documented through contemporaneous
author-maintained assessment notes and the resulting behavioral figure, not through a
device-generated import log. See `../EVIDENCE-MAP.md`, boundary 2, for the exact evidentiary
status of this claim.

## Scope notes

- This was a controlled case-study validation on a single physical unit, not a
  statistically characterized trial series. No trial counts, success rates, or
  probability/uncertainty estimates were collected, and none are claimed.
- The same physical Cs-137 check source was used across the baseline and modified-state
  observations in steps 2 and 5 (researcher-confirmed).
- Steps 7 and 8 characterize a *different* trust boundary (firmware update integrity) from
  steps 1–6 (configuration-state integrity) and are not conflated in this package's claims.
