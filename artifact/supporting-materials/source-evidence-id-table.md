# Restricted Source Evidence Identifier Table

This table provides neutral identifiers and SHA-256 values without disclosing restricted
repository paths, credential-bearing content, live endpoints, or operational filenames.

| Evidence ID | Restricted type | SHA-256 | Public role |
|---|---|---|---|
| `config-baseline-001` | Canonical 2015.1 configuration export; 173 settings | `0a755e1faa862b809f4d989379300bb09357c4d9afa9a1c33bd4f5206f386e0a` | Baseline for sanitized structural comparison |
| `config-variant-001` | Modified configuration variant | `729d66beb84e67d8ff120db0328dcf921a7be7f87f1588d82c296063318a0aa8` | Three-value threshold comparison only |
| `config-variant-002` | Additional modified configuration | `8feba23e995bd5185d4aba65e73a70b79d60475916fd28be5d943b4ff2ac9ed2` | Hash-only; not used in a public claim |
| `config-variant-003` | Additional modified configuration | `b02697a8b8c7de4d3c16406344845d643d2cfaa1f3c20e6718df9bc580772d0d` | Hash-only; not used in a public claim |
| `config-candidate-malformed` | Non-XML/HTML content saved with XML suffix | `6a12be98783f68715e2195b84874d8af68780d9e16ef44a12986b22ead4ce4ea` | Excluded from all claims |
| `log-update-001` | Raw device firmware-update response/log | `d5458556950218f7d3a57de000ea0f0c46f2273061e5a36b2aa5e0e8423d1be1` | Source for minimized firmware-update excerpt |
| `log-exception-001` | Raw device exception response/log | `c0c9c7c68e21557bcb07cf0274c8cfc01c67797f842eb33fd09734df14317e40` | Source for minimized recurrent-exception excerpt |
| `log-system-001` | Full device system log | `66ae953d7cc2775177d667cd042289277d71467540ffa77853ce140c5781993d` | Qualitative recovery limitation only |
| `author-note-001` | Researcher-authored assessment document | `24655cb1cc535ed4bdf72f84e499b6cc735998ba8db4ab87992fb6285704f7af` | Soft-reset/recovery observation |
| `author-note-002` | Researcher-authored assessment document | `c0f475039d84540886241b698a29a1068c70582307f8c586a9628becf45cd2b0` | Soft-reset mention; not an independent reproduction |
| `live-demo-script-001` | Restricted operational script | `16fc208263a94de44184270c403a2e21a54da007dfdb61d51da15625a08b18d5` | Researcher-identified threshold workflow |
| `live-demo-script-002` | Restricted operational script | `94460c013f508a6094916ebeaaa72cdb1df1ababa0f5d0f6a760771fd98afd7c` | Researcher-identified classification/alarm workflow |
| `live-demo-script-003` | Restricted operational script | `9daf22a16f0bd8593396c76df641e61f11642f6423055d83dbd3f69f5c2ade20` | Researcher-identified classification workflow |
| `firmware-image-2019.2` | Proprietary firmware image | `aa29c156a631d92a737e5580d1efc9de14639c77018be87cf8fc0a7176eea1bb` | Source of separate reverse-engineering observation |
| `firmware-update-member-2019.2` | Extracted update member | `86f6728c128c10f04bc6f6d6547ba5f4b481ee274a38d98f92ac5ae8ce95653b` | Restricted extraction-chain intermediate |
| `firmware-applicationpackage-2019.2` | Extracted application package | `37fbe12f8e8392f42a80354fa3fffff9fe16154e65522f0938b43659dabfa505` | Restricted extraction-chain intermediate |
| `codebehind-assembly-2019.2` | Proprietary extracted DLL | `3f0328f68e9d094da372e81d67e2aa3c9be97a6297cc8def3a4eeb530ab01baf` | Source assembly for prose-only observation |
| `codebehind-decompiled-2019.2` | Proprietary decompiled output | `8dc1fef45530523c783542ae2fc65d35cd8ed1b721ab260387f5d79cacc31413` | Restricted corroborating implementation evidence |
| `mainapplication-assembly-2019.2` | Proprietary extracted executable | `16cacc5d33cc5f80f8474582191cd408d7d7b5663cc78135d4e8fd78948b9a74` | Code-level source for the hardcoded-credential finding; not distributed |
| `mainapplication-decompiled-2019.2` | Proprietary decompiled output | `f55af0ae20f3d3dfeca1c2d43a6b94c7929b070a6738a983be953aba5b6a08d5` | Restricted corroborating source for the credential pair; not distributed |
| `credential-validation-record-2015.1` | Researcher-authored bounded validation record | `1e9d63fe90f6541489eb20578086176eb1156e68e80e5d4d95e255e28f9f874b` | Direct authentication and bounded diagnostic-log-deletion record; credential-bearing supporting captures are not distributed |
| `figure-alarm-observation` | Manuscript figure | `aba7c56bfee607b2215a2de14e48a2e8caf00a75c9cf840af044c1d6f67895f0` | Direct 2015.1 visual observation |
| `figure-semantic-source` | Original manuscript figure before metadata removal | `45615d1767656ef90832e764bb6b306784639aa51be2528ff5d793c3ef445783` | Source provenance only; not distributed |
| `figure-semantic-sanitized` | Metadata-clean manuscript figure | `f3d07b8bd3f78623e9a2d986201ce371ad3181f37e6784c6534a5e98e61db9d5` | Direct 2015.1 semantic observation |
| `figure-exception-source` | Original manuscript figure before metadata removal | `be5ab5eb3b4d92986ab4ceb91081ddf17a3c46c7cc5a07fbee5b03fcf7dd980c` | Source provenance only; not distributed |
| `figure-exception-sanitized` | Metadata-clean manuscript figure | `1a6fb3b50a390e0db8a22721d8d9a740001f447f0d34539b1f10267d23ae0b8f` | Direct 2015.1 exception observation |

The existence of a hash does not make a restricted artifact publicly releasable. It provides
identity and traceability only.
