# SCRIPT — Brutalist Utility: fill_slates.py (Short)

Native 9:16 Short cut from the full-length vertical parent by whole-beat cut
only. Every beat below is copied byte-for-byte (mp4 + mp3) from the parent's
`vertical/` directory — no rewrite, no re-render. Total runtime 123.79 s.

## Focus (what this Short teaches)

`fill_slates.py` is the safety net. When a batch reel build finishes but a
few beats end up with **no rendered media on disk and no Remotion pattern
in the sheet**, one invocation stamps a Form A card on every such beat so
the slate review cut still plays. The good beats are never touched.

The Short answers four questions and stops:
1. What is the ask? (B00) — three empty beats across two reels, one command.
2. What does it actually do? (B01, B02) — stamp only the empty beats, per a
   four-condition rule; walk → find → stamp → render → recut.
3. Does it work on real material? (B07) — disposable 5-beat fixture, dry-run
   output shows the four skip conditions in action.
4. What can go wrong? (B08, B09) — four honest failure modes; verdict.

The four MECHANISM code deep-dives (`--help` CLI surface, `slate_resolves()` /
`find_slates()`, `_truncate()` / `stamp_slates()`, `render_reel()`) and the
extended YOUR TURN composer live in the full-length teardown, not here.

## Kept beats — narration copied unchanged from the parent

### B00 · ASK · ClaudeComposerAsk916 · 14.71 s
> Hej, this is Liam, in for Bear. The ask — a batch job finished, but three
> beats across two reels have no media on disk and no remotion pattern yet.
> Fill them all with a Form A card so the review cuts still play through.
> One command. No rebuild of the ones that are already good.

### B01 · BLUF · BrutalistHesitantWriter916 · 10.46 s
> Watch the writer walk this back. Fill slates does not rewrite every beat
> in a reel. It stamps only the empty ones — no media on disk, no pattern
> in the sheet. The good beats are untouched.

Hesitant-writer corrections: `rewrites` → `stamps`, `all` → `empty`.

### B02 · FRAMEWORK · SkillTeardownMechanism916 · 23.08 s
> The pipeline. One invocation. Walk books slash for every reel that has a
> beat sheet. Find the slate beats — no media, no manim, no silent flag, no
> pattern. Stamp each one with a Form A card whose lines are the first eleven
> words of the narration. Then shell out to remotion scenes dot py — the
> slate renders to media slash B whatever dot mp4. Then shell out to run dot
> sh — the review cut recompiles. Dry run is the default. Apply is the flag.

### B07 · WORKED EXAMPLE · ClaudeCodeBeat916 · 22.46 s
> Worked example. Disposable fixture — one beat sheet with five beats. B zero
> and B one have no media and no pattern. B two already has a composer
> pattern. B three is silent. B four has a stub media file on disk. Point
> dash dash books at the fixture and dry run. Fill slates prints one reel,
> two slates: B zero, B one. Silent gets skipped. Patterned gets skipped.
> Rendered gets skipped. Exactly what the four skip conditions promise.

### B08 · FAILURE MODES · ClaudeCodeBeat916 · 27.42 s
> Failure modes. Four. One — the beat sheet doesn't exist. Find slates
> returns an empty list and None. The reel is quietly skipped. Two —
> remotion scenes exits non zero. Render reel appends REMOTION FAIL with
> the last three hundred characters of stderr, and never even calls run dot
> sh. Three — run dot sh exits non zero. ART underscore RUN FAIL, same
> shape. Four — no slates at all. The loop reports zero affected reels and
> does nothing. One bad reel never takes the batch down.

### B09 · VERDICT · ClaudeVerdictArtifact916 · 19.54 s
> So — fill slates dot py. The safety net. One walk of books slash. One rule
> for what counts as a slate — no media, no manim, no silent flag, no
> pattern. One stamp — Form A card with a truncated headline. Two shell
> outs — remotion scenes, then run dot sh. Dry run is the default. Apply is
> the flag. Silent beats and pre patterned beats are never touched. That's
> the whole tool.

### B11 · OUTRO · ClaudeTitleOutro916 · 6.13 s
> Brutalist Utility: fill slates dot py. Liam, in for Bear, for at
> Humanitarians A I.

## Dropped from the long

- **B03** — MECHANISM 1 · `--help` CLI surface + module docstring usage lines
- **B04** — MECHANISM 2 · `slate_resolves()` + `find_slates()` bodies
- **B05** — MECHANISM 3 · `_truncate()` + `stamp_slates()` bodies
- **B06** — MECHANISM 4 · `render_reel()` two-subprocess block
- **B10** — YOUR TURN · long-form assignment composer

The retained narration references the pipeline steps (`find_slates`, the four
skip conditions, `stamp_slates`'s 11-word truncation, the two shell-outs to
`remotion_scenes.py` and `run.sh`, and the four failure modes) at the
_function-name and behaviour_ level in B02, B07, B08 and B09 — so no
transition depends on the dropped code cascades. No numbered forward
references to dropped beats. No dangling caveats.

## Voice / brand

- Persona: **Liam (in for Bear)**
- Engine: Kokoro (`am_onyx`)
- Palette: claude · cream ground · terracotta accents
- Playlist: Brutalist · channel `@HumanitariansAI`
- Captions: **false** (no burned-in subtitles)
- Aspect ratio: 9:16 · native portrait 2160×3840 · no landscape crop
