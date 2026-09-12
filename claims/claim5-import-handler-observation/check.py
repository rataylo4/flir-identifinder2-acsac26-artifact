#!/usr/bin/env python3
"""Claim 5 static check: configuration-import handler observation.
Standard library only. No network or device access.
"""
import sys

def main():
    path = sys.argv[1]
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    status = "PASS"

    if "Identifinder.CodeBehind.dll" in text and "BackupSettingsPage.HandleUploadedFile" in text:
        print("OK: correct assembly and method named")
    else:
        print("FAIL: correct assembly/method not both present")
        status = "FAIL"

    # MainApplication.exe may be mentioned only in a correction/disclaimer sentence, not
    # asserted as the current source. Require it to appear near correction language.
    if "MainApplication.exe" in text:
        idx = text.find("MainApplication.exe")
        window = text[max(0, idx - 200):idx + 50].lower()
        if "incorrect" in window or "error" in window or "corrected" in window:
            print("OK: MainApplication.exe appears only in corrective/disclaimer context")
        else:
            print("FAIL: MainApplication.exe appears without corrective context — possible misattribution")
            status = "FAIL"
    else:
        print("OK: MainApplication.exe not mentioned at all")

    required_caveats = ["code-identical", "elsewhere in the"]
    missing = [c for c in required_caveats if c.lower() not in text.lower()]
    if not missing:
        print("OK: required version-boundary caveats present")
    else:
        print(f"FAIL: missing caveats: {missing}")
        status = "FAIL"

    forbidden_code_markers = ["```csharp", "```cs\n", "private ImportState", "DeserializeSettings(stream)"]
    found_code = [m for m in forbidden_code_markers if m in text]
    if not found_code:
        print("OK: no verbatim code / method body found (prose-only)")
    else:
        print(f"FAIL: verbatim code markers found: {found_code}")
        status = "FAIL"

    print(f"RESULT: {status}")
    sys.exit(0 if status == "PASS" else 1)

if __name__ == "__main__":
    main()
