# SHOTLIST.md — Brutalist Command: setup

Every beat = one visual slot. All visuals render on the Claude cream (`#FAF9F5`) stage with warm ink (`#3D3929`) and terracotta (`#D97757`) as the ONE accent. Portrait uses native `916` variants where registered.

| ID | Act | Composition | What appears (in order) |
|---|---|---|---|
| **B00** | ASK | `ClaudeComposerAsk` / `ClaudeComposerAsk916` | 1. Composer card fades in on cream. 2. Serif greeting **Konnichiwa, Liam** types above the composer. 3. The ask types into the composer body. 4. `runningText: running ./setup…` lands. 5. Three output lines cascade in below. Folder chip: `@HumanitariansAI`. |
| **B01** | BLUF | `BrutalistHesitantWriter` / `BrutalistHesitantWriter916` | 1. Cream page holds; caret blinks. 2. Types "setup / installs everything." 3. The word "installs" turns terracotta, hesitates, backspaces, types "verifies". 4. The word "everything" turns terracotta, hesitates, backspaces, types "live". 5. Final line settles: "setup / verifies live.". `seed: setup-b01`, `fontSize: 260`, `lineSpacing: 2.5`. `lead_silence_s: 0.8` on the beat. Narration extends the correction out loud with the "--install installs first" caveat. |
| **B02** | FRAMEWORK | `ClaudeCodeBeat` / `ClaudeCodeBeat916` | Code card titled `setup:1-16 — shebang + surface + one honest sentence`. Body types in three passes: the shebang + two-mode block; the free-by-default paragraph; the `set -uo pipefail` line. Spark line settles: **"Two modes. One script. One honest sentence."** |
| **B03** | FRAMEWORK | `ClaudeCodeBeat` / `ClaudeCodeBeat916` | Code card titled `requirements.txt — the pip contract (verbatim)`. Full contents of `requirements.txt` type in. Spark line: **"Six lines. One pinned floor."** |
| **B04** | WORKED_EXAMPLE | `ClaudeCodeBeat` / `ClaudeCodeBeat916` | Code card titled `$ ./setup    (verbatim)`. Header line, then the seven FEATURE rows type with `✅ ready` markers, then the ready sentence, then `[exit 0]`. Spark line: **"Seven rows green. Cost $0.00. Exit 0."** |
| **B05** | MECHANISM | `ClaudeCodeBeat` / `ClaudeCodeBeat916` | Code card titled `setup:57-100 — --install: four phases`. Body types four labelled blocks (pip, npm, fonts, Kokoro model) with the actual URLs and paths. Spark line: **"Four phases. Then verify."** |
| **B06** | MECHANISM | `ClaudeCodeBeat` / `ClaudeCodeBeat916` | Code card titled `setup:117-140 — check() and dynamic OK_/MISS_ vars`. Types the top comment, then the `check()` body, then two representative `check` calls. Spark line: **"Bash 3.2-safe. OK_id / MISS_id via eval."** |
| **B07** | MECHANISM | `ClaudeCodeBeat` / `ClaudeCodeBeat916` | Code card titled `live verification, not receipts`. Body types the `kokoro_synth` check line, then the summary of `setup_smoke_kokoro.py`'s behaviour, then the top-of-file rationale from setup. Spark line: **"Kokoro must actually speak. Silence fails."** |
| **B08** | MECHANISM | `ClaudeCodeBeat` / `ClaudeCodeBeat916` | Code card titled `setup:102-115 — the ElevenLabs guard`. Body shows the four-fingerprint `EL_PAT` (with the visible-in-code concat trick), the sweep, the error path, and the file-list branch. Spark line: **"Free-by-default is a guard, not a slogan."** |
| **B09** | FAILURE_RECOVERY | `ClaudeCodeBeat` / `ClaudeCodeBeat916` | Code card titled `recovery   (verbatim; models unlinked)`. Types BEFORE (unlink `runtime/models`), AFTER (the audio row goes red + two hint lines + exit 1), and RECOVERY (`./setup --install` or restore + rerun; all-green + exit 0). Spark line: **"One dir missing. Row red. Exit 1. Fix printed."** |
| **B10** | VERDICT | `ClaudeVerdictArtifact` / `ClaudeVerdictArtifact916` | Artifact card fades in. Heading: `setup — the whole surface, in the order you use it`. Six lines type in one at a time. |
| **B11** | YOUR_TURN | `ClaudeComposerAsk` / `ClaudeComposerAsk916` | Greeting **Your Turn** above the composer. Long paste-ready prompt fills the composer body. `runningText: paste this into Claude Code…`. Three grading lines cascade in below. Folder chip: `@HumanitariansAI`. |
| **B12** | OUTRO | `ClaudeTitleOutro` / `ClaudeTitleOutro916` | Locked outro card. Title restates **Brutalist Command: setup.**; handle **@NikBearBrown** (per OUTRO-LOCK.md; flagged for the human reviewer). Slug-seeded mascot animates below the handle. Silent under the jingle. |

## Visual budget

- One terracotta accent per beat.
- 5% title-safe inset on both aspects (SAFE tokens in `runtime/remotion/src/tokens/layout.ts`).
- No captions. No SRT/VTT. No burned-in transcript.
- The Claude UI appears only in B00, B11, B12 (per ILLUSTRATE LAW).
- Typing appears only in B00 (the ask), B01 (the hesitant writer), B11 (the viewer's prompt).
