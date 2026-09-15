# SHOTLIST — Brutalist Command: art keys

Twelve beats. Cold open on `ClaudeComposerAsk`; BLUF on `BrutalistHesitantWriter`;
five `ClaudeCodeBeat` mid-body beats plus one `ClaudeVerdictArtifact`; Your Turn
on `ClaudeComposerAsk`; outro on `ClaudeTitleOutro` (locked). Every visual is a
registered composition in `runtime/remotion/src/Root.tsx` — the 916 shims
(`ClaudeComposerAsk916`, `ClaudeCodeBeat916`, `ClaudeVerdictArtifact916`,
`BrutalistHesitantWriter916`, `ClaudeTitleOutro916`) render the same components
against native 1080×1920 canvases.

| # | Beat | Act | Scene | Purpose |
|---|---|---|---|---|
| B00 | ASK | Cold open | ClaudeComposerAsk | Habari, Liam — "before I fill a single beat sheet, tell me which optional keys this box has, and whether the toolkit needs any of them." Ask lands answered with the three output lines. |
| B01 | BLUF | EXECUTIVE-SUMMARY | BrutalistHesitantWriter | Hesitant writer types "art keys / blocks renders." Terracotta on `blocks` → backspaces → `audits`. Terracotta on `renders` → backspaces → `upgrades`. Corrected sentence: "art keys / audits upgrades." |
| B02 | FRAMEWORK | Dispatcher case | ClaudeCodeBeat | Two-line `keys)` case at `art:103-104` — no aliases, forwards `"$@"` verbatim to the Python script. |
| B03 | FRAMEWORK 2 | Three status states | ClaudeCodeBeat | The `row(service, var, status, detail)` taxonomy: `valid` (rc == 0), `invalid` (rc ≠ 0), `unset` (FileNotFoundError), plus the fourth `warn`/`inconclusive` fallback. |
| B04 | WORKED_EXAMPLE 1 | The "invalid" run | ClaudeCodeBeat | Verbatim from `demo/RUN-LOG.txt § 1` — higgsfield installed, offline, red row, "All present keys validated." footer, `[exit 0]`. |
| B05 | WORKED_EXAMPLE 2 | The "unset" run | ClaudeCodeBeat | Verbatim from `demo/RUN-LOG.txt § 2` — higgsfield removed from `PATH`, yellow "· unset" row, free-path fallback text, `[exit 0]`. |
| B06 | MECHANISM 1 | The probe body | ClaudeCodeBeat | `check_keys.py:38-58` verbatim — the `subprocess.run(["higgsfield", "account", "status"], timeout=25)` and its three-way branching. |
| B07 | MECHANISM 2 | .env + redaction | ClaudeCodeBeat | `check_keys.py:20-30` — `load_env` uses `setdefault` (shell wins). Then the redaction proof: `grep -c 'this-should-never-print' = 0`. |
| B08 | FAILURE_RECOVERY | The design tell | ClaudeCodeBeat | The docstring says exit 1 on invalid, but line 40 declares `any_invalid = False` and never reassigns it. `art:20` help line advertises "SI key" — no SI probe exists in the script. |
| B09 | VERDICT | Artifact page | ClaudeVerdictArtifact | Six lines summarising the whole surface. |
| B10 | YOUR_TURN | Handoff composer | ClaudeComposerAsk | Grade the script against its own docstring — write a one-line failing test that the current exit code would let through. |
| B11 | OUTRO | Title restate | ClaudeTitleOutro | "Brutalist Command: art keys." · @NikBearBrown handle (locked). Liam, in for Bear, for @HumanitariansAI. |

## Per-beat show blocks

Each body beat carries `shot.show` events tied to audio-clock fractions. See
the `beat_sheet.json` for the authoritative list. Rough intent below.

- **B00 · type-on** — composer card fades in, greeting "Habari, Liam" types
  above it, the ask types into the composer, runningText appears
  ("running check_keys.py…"), three output lines cascade in.
- **B01 · hesitant-type** — page holds; first lines "art keys / blocks
  renders." type; `blocks` turns terracotta, backspaces, types `audits`;
  `renders` turns terracotta, backspaces, types `upgrades`; final settled
  state is the sentence quoted.
- **B02 · code-cascade** — code card fades in with "art" in the title bar;
  `case "$cmd" in` types; `keys)` pattern; the single `exec` line; spark
  line settles.
- **B03 · code-cascade** — three (four) status paths type as a Python
  literal table with the emoji marks that actually print.
- **B04 · code-cascade** — verbatim invocation and output. The red `❌
  invalid` row lands, then the green "All present keys validated." with
  `[exit 0]` — the point of the beat is that the two disagree.
- **B05 · code-cascade** — verbatim invocation showing higgsfield removed
  from PATH, yellow `· unset` row, `[exit 0]`.
- **B06 · code-cascade** — the probe body types; three status-branch
  arrows point to `valid`, `invalid`, `unset`, plus the `warn` catch.
- **B07 · code-cascade** — `load_env` body; then `$ echo MY_SECRET=… > .env`
  then `grep -c` line and the answer `0`.
- **B08 · code-cascade** — side-by-side: the docstring ("exit 1 if invalid")
  vs the reality (`any_invalid = False` never reassigned). Then `art:20`
  help vs the actual `SI` grep (no matches).
- **B09 · artifact-in** — six lines cascade onto the artifact card.
- **B10 · type-on** — Your Turn composer with the paste-ready prompt +
  three grading lines under runningText.
- **B11 · outro-card** — cream page in, poster-serif title types, terracotta
  period, `@NikBearBrown` handle, mascot animates below.

## Portrait (9:16) framing notes

- Every landscape composition has a native 1080×1920 variant registered in
  the isolated toolkit's `Root.tsx`. `ClaudeCodeBeat916` and
  `BrutalistHesitantWriter916` were required (the second inherits the
  portrait-scale patch — `Math.min(width/1080, height/1920)` when
  `height > width`; see `feedback_brutalist_hesitant_writer_portrait_scale_patch`).
- Portrait BLUF (B01): fontSize 260, lineSpacing 2.5 — same as landscape
  because the corrected sentence's widest line ("art keys" is 8 chars,
  "audits upgrades." is 16) fits comfortably inside SAFE916; per
  `feedback_hesitant_writer_portrait_bluf_recipe` we can push fontSize
  higher when the widest line is ≤ 14 chars and lineSpacing stays ≥ 2.4.
  If the frame check flags edge-bleed we iterate DOWN (per the recipe:
  widen line spacing before shrinking font).
- Portrait `channel_title` is **omitted** from metadata per
  `feedback_channel_title_portrait_bleed`. Landscape keeps it.
