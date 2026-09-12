# Reverse-Engineering Observation — 2019.2, Prose Only

## Evidence provenance

- Separately obtained firmware image: version 2019.2, restricted identifier
  `firmware-image-2019.2`, SHA-256
  `aa29c156a631d92a737e5580d1efc9de14639c77018be87cf8fc0a7176eea1bb`.
- Examined assembly: `Identifinder.CodeBehind.dll`, restricted identifier
  `codebehind-assembly-2019.2`, SHA-256
  `3f0328f68e9d094da372e81d67e2aa3c9be97a6297cc8def3a4eeb530ab01baf`.
- Decompiled with ilspycmd / ICSharpCode.Decompiler 8.2.0.7535. The full restricted output has
  SHA-256 `8dc1fef45530523c783542ae2fc65d35cd8ed1b721ab260387f5d79cacc31413`.

No firmware image, DLL, decompiled source, executable vendor software, or verbatim proprietary
method body is distributed in this package.

## Bounded observation

In the separately examined 2019.2 image,
`Identifinder.CodeBehind.Settings.BackupSettingsPage.HandleUploadedFile` passes the uploaded
stream to `DeserializeSettings` and converts the deserialization result, or a caught
exception, into an import-state object. No signature, checksum, HMAC, or other
configuration-integrity verification call is visible in that handler.

## Required limitations

- This observation is limited to the named handler.
- It does not establish that equivalent checks are absent elsewhere in the
  `DeserializeSettings` deserialization pipeline.
- It does not establish that the tested 2015.1 and examined 2019.2 builds are code-identical.
- It is corroborating implementation evidence, not direct evidence of the tested 2015.1
  device's code.
- The tested 2015.1 configuration-acceptance observation and this 2019.2 implementation
  observation are separate evidence sources and must not be merged into one claim.

## Redistribution status

The researcher approved this author-created prose description and hash-based provenance for
inclusion on 2026-08-24. Redistribution rights for vendor firmware, vendor software, and
decompiled vendor code are not claimed. Approval of this bounded observation does not alter
the stated evidentiary limitations. The researcher separately approved public release of the
complete sanitized package on 2026-09-08.
