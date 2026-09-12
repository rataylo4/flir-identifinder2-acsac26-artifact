#!/usr/bin/env python3
"""Claim 4 static check: recurrent exception occurrence.
Standard library only. No network or device access.
"""
import re
import sys
from datetime import datetime

def main():
    log_path, evmap_path = sys.argv[1], sys.argv[2]
    with open(log_path, "r", encoding="utf-8") as f:
        text = f.read()

    status = "PASS"

    # Find each "IndexOutOfRangeException" occurrence together with its preceding timestamp line.
    pattern = re.compile(
        r"(\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2})\nIndexOutOfRangeException\n"
        r"   at Identifinder\.NetworkServices\.Dns\.ResponseBuilder\.GenerateResponse\(Byte\[\] data\)\n"
        r"   at Identifinder\.NetworkServices\.Dns\.DnsServer\.Listener\(\)"
    )
    matches = pattern.findall(text)

    if len(matches) == 2:
        print("OK: exactly two matching IndexOutOfRangeException occurrences found")
    else:
        print(f"FAIL: expected exactly 2 occurrences, found {len(matches)}")
        status = "FAIL"

    if len(matches) == 2:
        d1 = datetime.strptime(matches[0], "%m/%d/%Y %H:%M:%S")
        d2 = datetime.strptime(matches[1], "%m/%d/%Y %H:%M:%S")
        delta_days = abs((d2 - d1).days)
        if 20 <= delta_days <= 40:
            print(f"OK: occurrences are {delta_days} days apart (within 20-40 day 'approximately one month' band)")
        else:
            print(f"FAIL: occurrences are {delta_days} days apart, outside expected band")
            status = "FAIL"

    with open(evmap_path, "r", encoding="utf-8") as f:
        evmap_text = f.read()

    # These terms are allowed to appear ONLY inside an explicit negation/disclaimer
    # (e.g. "Does not support: 'reproducible finding'"). A bare, affirmative use of either
    # term (asserting the finding IS reproducible / IS a controlled reproduction) is an
    # overclaim and should fail this check.
    forbidden = ["reproducible finding", "controlled reproduction"]
    negation_cues = ["does not support", "not described as", "not claimed", "no controlled"]
    lower_text = evmap_text.lower()
    overclaims = []
    for term in forbidden:
        start = 0
        while True:
            idx = lower_text.find(term, start)
            if idx == -1:
                break
            window = lower_text[max(0, idx - 60):idx]
            if not any(cue in window for cue in negation_cues):
                overclaims.append(term)
            start = idx + 1
    if not overclaims:
        print("OK: overclaim terms either absent or only used within an explicit disclaimer")
    else:
        print(f"FAIL: overclaim terms used affirmatively (not disclaimed): {overclaims}")
        status = "FAIL"

    print(f"RESULT: {status}")
    sys.exit(0 if status == "PASS" else 1)

if __name__ == "__main__":
    main()
