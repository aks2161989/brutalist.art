# FACTCHECK — The godot-waikthrough Skill (portrait)
# run_id: 4d4269b669dd4b84a92a266e5bff804f
# source_sha256: a0cfc6ba0c3e56fd162d80c940e4fbf31594739d7c7283dcfe3c9a0ae90c39ed
# Re-verified 2026-09-12: same teaching content as landscape; SKILL.md §4 additions do not affect narration claims.

All narration claims are verified against the source files read.

## Claims and verification

| Claim | Verification | Source |
|---|---|---|
| "godot-waikthrough is an agent-driven builder like ai-explainer, not a shell command" | SKILL.md §intro: "This is an agent-driven builder like ai-explainer, not a shell command that invents a play route without reading the project." ✓ | SKILL.md verbatim |
| "godot-walkthrough is an alias" | SKILL.md §intro: "`godot-waikthrough` is the requested command spelling; `godot-walkthrough` is an alias." ✓ | SKILL.md verbatim |
| "Standard mode: open on the game and its objective, with Liam's brief introduction" | SKILL.md §3: "Standard mode: open on the game and its objective, with Liam's brief introduction" ✓ | SKILL.md verbatim |
| "Walker mode uses four bookends in exact order" | SKILL.md §3 lists B00→B01→gameplay body→verdict/your-turn ✓ | SKILL.md §3 |
| "Walker mode B00 prompt begins 'Please use Walker to convert my game design document about…'" | SKILL.md §3 B00: "Prompt begins 'Please use Walker to convert my game design document about …'" ✓ | SKILL.md verbatim |
| "Riff mechanic: inspect first; narrate what is happening on screen, the mechanism, and a useful trade-off" | SKILL.md §2: "Inspect first; narrate what is happening on screen, the mechanism, and a useful trade-off." ✓ | SKILL.md verbatim |
| "A driver may observe position/state to choose inputs, but must not teleport, set completion, disable collisions, or call test-only gameplay shortcuts" | SKILL.md §2 verbatim ✓ | SKILL.md |
| "Clearly label scripted-input captures as such; they are not human playtests" | SKILL.md §2 verbatim ✓ | SKILL.md |
| "Write coverage.json using the reference contract" | SKILL.md §2 ✓; schema verified in capture-and-coverage.md ✓ | Both files |
| "Do not secretly fix the game to make a demonstration succeed" | SKILL.md §1 verbatim ✓ (quoted on screen B08) | SKILL.md |
| "If it cannot run, report the exact blocker; no fake gameplay in place of an engine run" | SKILL.md §1 verbatim ✓ (quoted on screen B08) | SKILL.md |
| "art godot-waikthrough --check REEL validates coverage contract, clip hashes, dimensions, time ranges, input-log presence, and beat references" | SKILL.md §4 + capture-and-coverage.md verbatim ✓ | Both files |
| "For 30 fps captures, preserve exact frame-fraction durations" | SKILL.md §4 ✓ | SKILL.md |
| "Deliver the MP4's absolute path, a quoted open command, feature coverage, limitations, and QC results" | SKILL.md §4 ✓ | SKILL.md |

## Narration claims NOT in source (flagged)

- B04: The walker-jumpman project (jump, spike, flag, cherries, settings menu) is a **teaching illustration** constructed from SKILL.md's own use of walker-jumpman as an example game. capture-and-coverage.md explicitly mentions walker-jumpman. No actual game project verified — labeled "teaching illustration — not this build's output" in all scene source fields. ✓ (appropriate labeling)
- B05: Terminal output lines are teaching illustrations consistent with Godot Movie Maker and capture-and-coverage.md's documented approach — labeled as such.
- B06: RIFF.md structure is a teaching illustration derived from riff/SKILL.md's documented RIFF.md format — labeled as such.

## No fabricated claims

- No invented model version numbers, dates, or count statistics appear in narration.
- No human playtest results or fun/accessibility claims are made.
- The limitation (no real game available) is explicitly stated on screen.

## Teaching-arc checklist

- [x] FRAMEWORK beat — B02 (pipeline) presents framework before examples
- [x] WORKED EXAMPLE — B04 (feature inventory) walks through the framework step-by-step
- [x] FALSIFIABILITY — B09 (cannot-run gate + self-demo limitation)
- [x] SCAFFOLDED viewer task — B11 (paste-ready prompt + rubric: verify inventory against known game)
- [x] Four bookends — B00 (cold open), B10 (verdict), B11 (your turn), B12 (outro)
- [x] No source, no verdict — verdict B10 recapitulates; all body beats carry on-screen source labels
