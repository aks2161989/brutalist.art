# PROMPTS — The logo Skill

## Cold-open ask (B00)

> What does the `logo` skill actually do to a reel?
> Read `skills/make/logo/SKILL.md` and tell me — the mental model, not the README summary.

Runs against the installed Claude Code subscription; no external services.

## Your-Turn dry-run prompt (B10)

Paste-ready into Claude Code:

```
Read skills/make/logo/SKILL.md. Pick one delivered reel at <book>/youtube/<my-slug>/
and pick a brand pool that fits (hai | medhavy | muz). Then run:

  python3 skills/make/logo/scripts/logo.py <book>/youtube/<my-slug> <brand> \
      --no-render --no-compile

Then verify:
  (1) the beat sheet now carries shot.remotion.picked =
      {brand, animation, svg, mp3, locked:true};
  (2) ffprobe mp3/beat-<BID>.mp3 shows length ≈ (jingle length) + (--tail, default 1.0s);
  (3) re-running the SAME command without --reroll reuses the pick byte-for-byte.

Do NOT run --reroll, do NOT run compile.py, do NOT touch the source beat_sheet.json
outside this run.
```

Why this prompt: it exercises three distinct laws in one dry-run —
random-once-then-locked (check 1 + 3), the-mp3-is-the-clock (check 2), and
non-destructive scaffolder posture (nothing else edited). No render, no
compile, no publish — safe against any real delivered reel.

## Prompts used to build the reel

- Beat-authoring: the AUTHOR (this Claude session) read the four source files
  above and wrote `beat_sheet.json` directly, no scaffolder invoked, no Claude
  Code prompt used for the writing step itself.
- Audio: `python3 runtime/scripts/generate_audio_kokoro.py <reel>` (Kokoro
  am_onyx, local, no keys, cost $0.00).
- Render: `ART_CHROME=<chrome-headless-shell> ART_CHROME_MODE=chrome-for-testing
  ART_CHROME_SINGLE_PROCESS=1 python3 runtime/scripts/remotion_scenes.py <reel>
  --force`. The `ART_CHROME_SINGLE_PROCESS=1` env is honored by a local patch
  to `@remotion/renderer/dist/open-browser.js` inside the isolated toolkit's
  shadow node_modules — it appends `--single-process --in-process-gpu
  --disable-crash-reporter` so chrome-headless-shell can boot inside macOS
  App Sandbox (Mach-port bind is otherwise denied). See
  `CHECKS-REPORT.md` for the exact edits and why they were needed.
- Compile: `python3 runtime/scripts/compile.py <reel> --height 2160 --out
  <reel>/exports/landscape --force`.

No paid API calls were made. The Claude Code subscription was used only to
author the beat sheet and this paperwork; no ANTHROPIC_API_KEY fallback.
