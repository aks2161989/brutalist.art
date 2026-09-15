# SHOTLIST.md — Brutalist Command: art vertical

Twelve beats. Every SHOW block is authored before the narration so the
visual carries the argument; the voice reacts.

## B00 — ClaudeComposerAsk (COLD OPEN)
- greeting: `Hola, Liam`
- topic: `BRUTALIST · COMMAND: ART VERTICAL`
- segment: `art vertical`
- command: the ask, plain English — "how do I make the full-length 9:16
  twin of this reel without cropping anything?"
- runningText: `planning the twin; rewiring, no cutting…`
- output: three answer lines; one names the wrapper, one names the
  script, one names the editorial contract.
- Composer types the ask; running indicator arms; output cascades.

## B01 — BrutalistHesitantWriter (BLUF)
- text (final corrected): `vertical preserves.\nand rewires it.`
- triggerWords: `preserves, rewires` (positional matches for the deleted
  words below)
- replacementWords: same as final — the writer types the WRONG framing
  first and corrects toward the final. Positional matching means the
  authored text is the CORRECTED version; the triggerWords list the
  wrong words the writer starts with, replacementWords list the fixes.
  See HesitantWriter component contract: `triggerWords` names the word
  typed first, `replacementWords` names what it becomes.

  So we actually author:
    text = `vertical shrinks.\nand crops it.`
    triggerWords = `shrinks, crops`
    replacementWords = `preserves, rewires`

  The writer types `vertical shrinks. / and crops it.`, hesitates,
  backspaces `shrinks`, retypes `preserves`, hesitates, backspaces
  `crops`, retypes `rewires`. Final on-screen sentence: `vertical
  preserves. / and rewires it.` — the reel's actual argument.

- fontSize: 240 (landscape) — recipe from prior episodes; portrait pass
  will use fontSize 180 / lineSpacing 2.6 via BrutalistHesitantWriter916.
- lineSpacing: 2.5
- seed: `command-vertical-b01`
- Lead silence 0.8 s so the initial mis-typed framing lands before the
  narration begins to correct it.

## B02 — ClaudeCodeBeat (FRAMEWORK, dispatcher)
- Title: `art:78-86 — the two adjacent cases`
- Body: the actual bash `case` block from `art`, unedited.

## B03 — ClaudeCodeBeat (MECHANISM — THE VERTICAL CONTRACT)
- Title: `shorts.py — rule 5 (verbatim)`
- Body: the module docstring's rule 5, quoted exactly.

## B04 — ClaudeCodeBeat (MECHANISM — the guardrails)
- Title: `shorts.py — main() guardrails`
- Body: the four lines that gate every difference between shorts and
  vertical.

## B05 — ClaudeCodeBeat (MECHANISM — ONDA CHECK, unchanged)
- Title: `shorts.py — the ONDA CHECK (still fires)`
- Body: the same helpers Ep 30 quoted, showing that vertical does NOT
  soften them; every REMOTION beat is rewired.

## B06 — ClaudeCodeBeat (MECHANISM — cap check is skipped)
- Title: `shorts.py — one line, one delta`
- Body: the `if not a.vertical: require_short_duration(...)` block —
  the entire duration-side delta between the two verbs.

## B07 — ClaudeCodeBeat (WORKED EXAMPLE)
- Title: `$ ./art vertical /tmp/claude-501/claude-shorts-demo   (verbatim)`
- Body: the actual stdout from `demo/VERTICAL-LOG.txt` invocation 1.
- Sparkline: `Full length. No drops. No endcard.`

## B08 — ClaudeCodeBeat (FALSIFIABILITY — the refusal)
- Title: `failure + recovery (verbatim)`
- Body: the two spellings of the refusal side by side, plus the
  recovery — pick one intent — with real command lines.

## B09 — ClaudeVerdictArtifact (VERDICT — the whole surface)
- artifactTitle: `Verdict`
- artifactHeading: `art vertical — the whole surface, in the order you use it`
- artifactLines (8):
  1. bare invocation — `./art vertical <reel>`; wraps `python3
     runtime/scripts/shorts.py <reel> --vertical`.
  2. full length — every source beat retained; no cap, no drops.
  3. no endcard — `--vertical` forces `no_endcard = True`.
  4. no rewritten outro — `--vertical` forces `no_outro_rewrite = True`.
  5. `--drop` refused — vertical + drop raises `BuildError` before any
     directory is written.
  6. ONDA CHECK still fires — every REMOTION beat rewired to its
     `<pattern>916`; missing composition = BLOCKED.
  7. captured portrait media — reused unchanged when the parent reel's
     aspect_ratio is already `9:16`.
  8. render only — no upload, no scheduling; publishing is a separate
     authorized human workflow.

## B10 — ClaudeComposerAsk (YOUR TURN)
- greeting: `Your Turn`
- topic: `BRUTALIST · YOUR TURN`
- segment: `Build the full-length 9:16 twin`
- command: the paste-ready 4-step prompt (read aloud verbatim in the
  narration — HANDOFF LAW).
- runningText: `paste this into Claude Code…`
- output: 4 expected outcome lines corresponding to the four numbered
  steps in the prompt.

## B11 — ClaudeTitleOutro (TITLE RESTATE)
- title: `Brutalist Command: art vertical.`
- slug: `claude-liam-brutalist-command-vertical`
- Silent under the jingle (per OUTRO-LOCK); narration is the sign-off
  read once ("Liam, in for Bear, for at Humanitarians A I").

## Portrait aspect (9:16 twin — 2160×3840 target)

Every REMOTION beat above rewires to its `<pattern>916` composition when
the vertical/beat_sheet.json is compiled. Existing 916 compositions
verified in this workspace's `Root.tsx`:

- `ClaudeComposerAsk916`     → registered, 1080×1920 (B00, B10)
- `BrutalistHesitantWriter916` → registered (B01)
- `ClaudeCodeBeat916`        → **added** in this workspace's Root.tsx
  (uses the responsive ClaudeCodeBeat component at 1080×1920) — same
  pattern as Ep 30 (B02–B08)
- `ClaudeVerdictArtifact916` → registered (B09)
- `ClaudeTitleOutro916`      → registered (B11)

Portrait BLUF (B01) uses the recipe from
`feedback_hesitant_writer_portrait_bluf_recipe.md`:
`text` shorter (4 line-breaks max), `fontSize` 180, `lineSpacing` 2.6 —
plus the portrait-scale patch already applied to
`BrutalistHesitantWriter.tsx`.

Portrait B00 and B10 composer commands and output lines are shortened
to fit the safe area (per `channel_title_portrait_bleed` and prior
episodes' portrait recipes). The full ask/prompt lives in the landscape
beat sheet; portrait renders the argument, not the wall of text.
