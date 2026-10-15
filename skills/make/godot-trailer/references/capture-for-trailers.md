# Capture, trim and mix for a trailer

Starts from the [walkthrough capture contract](../../godot-waikthrough/references/capture-and-coverage.md)
(Movie Maker `--write-movie --fixed-fps --quit-after`, the real main scene, input
events through the normal path, native 3840×2160, isolated project copy and
`user://`, hash after recording, `CAPTURE.md` with versions and settings). Read it
first. This file is only what a trailer changes.

## A shot bank, not a coverage run

A walkthrough must show every implemented feature. A trailer needs the **best few
moments** of the verb and its escalation. So:

- Plan the moments from `TRAILER-BRIEF.md` first: hook moment, establishing moment,
  three or four escalation moments, a peak, a possible button. Then record **several
  takes of each**, each a clean *situation → action → consequence*.
- A **rehearsed route** (an input script refined over runs) and **best-take
  selection** are legitimate craft. Say so in `CAPTURE.md`. What the game did is the
  honesty line, not how many attempts it took.
- Prefer many short takes over one long run, each with a pre-roll of a second or two
  so a cut can start before the action.
- **Reuse** a same-build walkthrough's `capture/` (its `coverage.json` hashes, input
  logs and `build_id` carry over). A changed build means new captures.

## What the footage may and may not be

| Allowed | Not allowed |
|---|---|
| a rehearsed input route; repeated takes; choosing the best | teleporting mid-level; invincibility; disabled collisions |
| window/stretch/resolution set up for native 4K | `Engine.time_scale` change, slow motion, speed-ups, time-lapse |
| hiding FPS counters, collider overlays, debug prints | spawning enemies, items or levels the game wouldn't |
| keeping HUD that explains a mechanic | hiding HUD that *is* the mechanic (health, combo, counters) |
| starting at a state a player can reach (a real level-select, the real first scene) | mid-state set-ups no player could reach, presented as played |
| the game's own in-engine cinematic, labelled if mistakable | AI video, mock-ups, concept art, re-created gameplay, screenshots-as-gameplay |
| one labelled free-camera establishing shot (≤15 % of runtime, never hook or peak) | a camera the player doesn't have, unlabelled |

`trailer.json` records, per capture, `state_setup` (how the starting state was
reached, as a player could) and an `integrity` attestation. The gate enforces that the
attestation exists and is clean; it cannot know it is true, so be honest in it.

If a start state needs more than the game offers (the second level takes 10 minutes
to reach), say how it was loaded (`scene loaded directly; player at the level spawn`),
which is a disclosed setup, not a teleport into the middle of a challenge.

## Frames

- Native 16:9 3840×2160; the gate fails below it (`--min-height` is a pilot override).
- Source fps is usually 60. The film runs at 30 fps; each window is in capture seconds
  and plays at normal speed. Give windows on frame boundaries (`in_s × source_fps`
  near an integer); the gate warns when they aren't.
- Look at the frames of every take in `_qc/` for visual bugs, clipped geometry,
  z-fighting, placeholder art, a stray debug label, a mid-load frame. A bug in a
  trailer is a promise broken in public.

## Trim (exact, normal speed)

One file per shot, re-encoded so the cut is frame-exact. `-ss` after `-i` with
re-encode is exact; use a high-quality intermediate and let the compiler do the final
encode.

```bash
# DUR = out_s - in_s, written as an exact frame fraction (e.g. 90/30), not a rounded decimal
ffmpeg -y -i capture/run-01.mp4 -ss 12.0 -t 3.0 -r 30 \
  -c:v libx264 -preset slow -crf 12 -pix_fmt yuv420p -c:a pcm_s16le media/S02.mp4
```

Keep the capture's audio in the trim; it feeds the game-sound bus below. A single
`hold_s` freeze is added at the peak only (`tpad=stop_mode=clone:stop_duration=0.4`),
never to stretch or slow the action.

## Music and the mix

The track is chosen first and measured; its beats are the cut grid.

```bash
python3 brutalist.art/skills/make/godot-trailer/scripts/beat_grid.py music/track.wav --out music/beats.json
```

`beats.json` has `bpm`, `beats`, `downbeats`, `onsets` (seconds). Plan cuts on beats;
put the peak on a downbeat; declare the quiet just before it in `music.drop`. If
`confidence` is low or the track has no steady beat, set `music.rhythm: "free"` and
cut to phrases instead. Correct a wrong phase with `--offset`, a known tempo with
`--bpm`.

Build the mix as two buses on the final timeline, music ducked under the game's own
hits so abilities and impacts punch through:

1. **Game bus.** Concatenate each shot's captured audio in timeline order, with
   10 ms fades at the joins; silence for cards.
2. **Music bus.** The track trimmed/faded to the runtime (a short fade is fine; the
   end card holds in near-silence or the track's tail, never a hard stop).
3. **Mix.** Sidechain-duck the music with the game bus (`sidechaincompress`), sum,
   then `loudnorm` to the pipeline's target. Write `audio/trailer-mix.wav`, 48 kHz
   stereo, **within 0.15 s of the timeline length**; pass it with `--audio`.
4. Run `runtime/scripts/loudness_check.py` on the finished master.

With a voiceover, a third bus carries the Liam lines (`audio/vo/*.wav`, placed at their shot offset)
and the music is ducked under both the voice and the game's own sounds (`sidechaincompress`).

A silent game with no supplied music gets a trailer whose only sound is its own
absence of one; flag it to Bear. Don't download, synthesize-and-pass-off, or invent
licensed music.

## Reading the game's facts for the end card

```bash
grep -h '^platform=' godot/export_presets.cfg      # platforms the project is configured to export
git -C GAME remote get-url origin                  # the real public address, if any
```

A project without `export_presets.cfg` has no verified platform list; the README or
Bear must supply it (record the source). Use the engine and version as the honest
floor ("Godot 4.7 project").

## Gates that read the footage (met on the first real trailer)

- **GATE T** (`art final` runs it) treats every gameplay frame as designed typography. On a
  cream-and-terracotta game it fails twice: the game's own terracotta sprite reads as accent text
  at 2.7:1, and the HUD hugging the frame edge reads as title-safe overflow. Don't relabel the shot
  type to dodge it. Use the `presentation` block (inset 0.9, matted in the game's background,
  `contrast_regions` over the HUD strips, a written reason). Find the strips by locating the
  navy text rows in one inset frame; keep regions on real text, never on the sprite.
- **GATE V** flags the title and end cards as "underfill" (content under 55 % of the safe area).
  They are sparse on purpose; the assembler declares `qc.sparse_by_design` with a reason, which waives
  only underfill/clustered and keeps edge-bleed, contrast and empty-frame.
- Look at frames of the **master** (`_qc/contact_sheet.png` plus your own samples across every cut),
  and at 0.1 s steps around the key event of each shot. A log time can lag the picture or a window can
  end a beat early: the first S07 ended just before the stomp, which no gate could see.
- Check each take for the game's own presentation defects (overlapping world signs, a popup hidden
  behind a tile). Cut around them, or keep one only if it is the moment, and say so in `SHOTLIST.md`.
