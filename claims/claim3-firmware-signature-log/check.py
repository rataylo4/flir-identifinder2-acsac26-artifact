#!/usr/bin/env python3
"""Claim 3 static check: firmware signature-check log evidence.
Standard library only. No network or device access.
"""
import sys

def main():
    path = sys.argv[1]
    with open(path, "r", encoding="utf-8") as f:
        lines = [l.rstrip("\n") for l in f]

    # Only the actual log lines (start with a date), not the '#' preamble comments.
    log_lines = [l for l in lines if l and l[0].isdigit()]

    status = "PASS"

    sig_failures = [l for l in log_lines if "[ERROR]Signature check failed" in l]
    if len(sig_failures) == 2:
        print(f"OK: exactly two 'Signature check failed' events found")
    else:
        print(f"FAIL: expected exactly 2 'Signature check failed' events, found {len(sig_failures)}")
        status = "FAIL"

    # Find the last "Beginning Update" block and check it ends without a final result.
    begin_indices = [i for i, l in enumerate(log_lines) if "Beginning Update" in l]
    if not begin_indices:
        print("FAIL: no 'Beginning Update' entries found")
        status = "FAIL"
    else:
        last_begin = begin_indices[-1]
        tail = log_lines[last_begin:]
        has_final_result = any(
            ("[ERROR]" in l or "Finished successfully" in l) for l in tail[1:]
        )
        ends_with_verification = tail[-1].strip().endswith("Update version verification ends.")
        if not has_final_result and ends_with_verification:
            print("OK: final logged update attempt has no recorded final result (ends at version verification)")
        else:
            print(f"FAIL: final update attempt does not match expected 'no final result' shape (has_final_result={has_final_result}, ends_with_verification={ends_with_verification})")
            status = "FAIL"

    contains_config_terms = any(
        ("settings" in l.lower() or "xml" in l.lower()) for l in log_lines
    )
    if not contains_config_terms:
        print("OK: no configuration/XML-import terms found in this log (firmware-scoped only)")
    else:
        print("FAIL: unexpected configuration/XML-import terms found in firmware log")
        status = "FAIL"

    print(f"RESULT: {status}")
    sys.exit(0 if status == "PASS" else 1)

if __name__ == "__main__":
    main()
