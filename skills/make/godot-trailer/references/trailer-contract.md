# `trailer.json` — the contract the gate reads

Author it in the reel folder. `./art godot-trailer --check REEL --game GAME` is
read-only. The example is **not evidence**: replace every time, hash and sentence with
measured, true ones. All paths are relative to and contained in the reel.

```json
{
  "schema_version": 1,
  "game": {"name": "my-game", "build_id": "<64-hex source-snapshot sha256>",
           "engine": "Godot 4.7.2", "build_status": "prototype"},
  "type": "store",
  "brief": {
    "audience": "players of short precision platformers",
    "goal": "play",
    "genre": "2D platformer",
    "hook": "You reverse gravity to turn every hazard into a pathway.",
    "idea": "each new rule changes what the next room asks of you",
    "tone": "bright, brisk",
    "verbs": [{"id": "jump", "input": "Space", "result": "arcs over a gap"}],
    "answers": {"what_is_this": "...", "what_do_i_do": "...", "why_care": "..."}
  },
  "features": [
    {"id": "jump", "status": "implemented"},
    {"id": "checkpoints", "status": "planned", "reason": "GDD only; not built"}
  ],
  "cuts": [{"feature": "pause_menu", "reason": "no new information; not part of the idea"}],
  "captures": {
    "take-07": {"path": "capture/take-07.mp4", "sha256": "...", "build_id": "<same>",
                "method": "scripted-input", "input_log": "capture/take-07-inputs.jsonl",
                "fps": 60,
                "state_setup": "Level loaded from the game's first scene; player at spawn",
                "integrity": {"teleport": false, "invincible": false,
                              "collisions_disabled": false, "spawned_content": false,
                              "time_scale": 1.0}}
  },
  "presentation": {"inset": 0.9, "pad_color": "#F6F3EB",
                   "contrast_regions": [{"label": "HUD top strip", "box": [0.07, 0.075, 0.85, 0.225]}],
                   "contrast_reason": "why GATE T needs named regions for this game's text"},
  "music": {"source": "supplied", "path": "music/track.wav", "sha256": "...",
            "provenance": "who made it, licence, where from", "tone_note": "why it fits this game",
            "rhythm": "metered", "beats": "music/beats.json",
            "drop": {"start_s": 49.2, "end_s": 50.0}},
  "vo": {"engine": "kokoro", "voice": "am_onyx", "persona": "liam",
         "lines": [{"id": "V01", "shot": "S01", "at_s": 0.4, "text": "One jump. Read the landing.",
                    "on_screen_equivalent": "single jumps clear the gaps; the HUD reads Space: jump"}]},
  "mix": "audio/trailer-mix.wav",
  "shots": [
    {"id": "S01", "role": "hook", "kind": "gameplay", "capture": "take-07",
     "in_s": 12.0, "out_s": 14.0, "screen": "gameplay", "feature": "jump", "verb": "jump",
     "situation": "a wide gap with a spike below", "action": "Space held, then released",
     "consequence": "Clawd clears the gap and lands on the far ledge",
     "new_information": "mechanic", "intensity": 1, "camera": "player",
     "hud": "kept", "debug_overlay": false, "shows_hook": true, "establishes_genre": true},
    {"id": "S09", "role": "cta", "kind": "card", "duration_s": 4.5,
     "card": {"pattern": "GameTrailerCard", "props": {"kind": "endcard", "title": "My Game",
              "platforms": ["macOS", "Windows"], "availability": "Playable prototype",
              "directive": "Download on GitHub"}}}
  ],
  "cta": {"title": "My Game", "platforms": ["macOS", "Windows"],
          "availability": "Playable prototype", "directive": "Download on GitHub",
          "address": "github.com/example/my-game",
          "sources": {"platforms": {"source": "export_presets.cfg", "ref": "godot/export_presets.cfg"},
                      "availability": {"source": "README", "ref": "README.md: 'Playable'"},
                      "directive": {"source": "git-remote", "ref": "origin"},
                      "address": {"source": "git-remote", "ref": "origin"}}},
  "checks": {"muted_test": {"status": "pending"}, "viewer_test": {"status": "pending"}}
}
```

## Music sources

`game` (the game's own audio), `supplied` (a track with its rights recorded in `provenance`),
`generated` (an original cue made by a script inside the reel: also give `generator` and
`generator_sha256`, and `trailer_only: true`; the description must say the game has no such
audio), or `none` (a warning). `rhythm: "metered"` needs `beats` (from `beat_grid.py`);
`"free"` skips the cut-on-the-beat check. `bpm` is informational.

## Voiceover (optional)

Omit `vo` for a music-only trailer. With it: `engine` is `kokoro` (free, local), Liam is `am_onyx`;
each line has `id`, `shot`, `at_s` (seconds into that shot when speech is heard), `text` and
`on_screen_equivalent`. `vo_kokoro.py` writes `audio/vo/<id>.wav` and `audio/vo/manifest.json`; the gate
fails a line whose text changed since its audio, an opening greeting or introduction, an adjective claim,
a line over 12 words or a total over 60, lines that overlap or crowd each other (under 0.15 s apart), a
line that starts outside its shot or runs past the end, and a missing equivalent. It warns when the voice
covers over 45 % of the runtime or speaks through the drop.

## Presentation (optional)

`inset` (0.8–<1.0) scales every gameplay clip into the title-safe box and mats it in `pad_color`
(use the game's own background colour); `contrast_regions` (normalised `[x0,y0,x1,y1]` in the
final frame) and `contrast_reason` are written into each gameplay beat's `qc` so GATE T tests the
game's real text locally. Nothing is cropped or retimed. Omit the block only if GATE T passes on
full-bleed footage.

## Shots

A **gameplay** shot plays its source window at normal speed, so its screen time is
`out_s − in_s` (plus a single `hold_s` freeze ≤ 0.5 s at the peak). A **card** shot
has `duration_s` and the `GameTrailerCard` pattern. The timeline is the running sum.

| Field | Meaning |
|---|---|
| `role` | `hook` → `establish` → `escalate` → `peak` → `title` → `button` → `cta`, in that order |
| `capture`, `in_s`, `out_s` | the source take and window (must lie inside the capture) |
| `screen` | must be `gameplay` (not menu, splash, loading) |
| `feature` | an `implemented` feature id; `planned` or unknown fails |
| `verb` | a `brief.verbs` id shown in this shot (the hook needs one) |
| `situation`, `action`, `consequence` | the sequence the viewer reads; required unless `flash` |
| `new_information` | `mechanic · environment · enemy · progression · ui · payoff`; never `none` |
| `intensity` | 1–5, non-decreasing across establish/escalate/peak unless `contrast: true` |
| `camera`, `disclosure` | `player`, or `debug` with a disclosure (≤15 % of runtime, never hook/peak) |
| `hud`, `hud_reason`, `debug_overlay` | `kept`/`hidden` (reason required), overlay explicitly `false` |
| `shows_hook`, `establishes_genre` | the hook must show by 15 s, the genre by 10 s |
| `flash` | a ≥0.4 s peak-only quick cut; at most 3 |
| `free_cut` | this cut may ignore the beat grid (≤ a quarter of cuts) |
| `text` | optional overlay: ≤ 7 words, ≤ 24 in the film, no banned adjectives |
| `sound_dependent`, `visual_equivalent` | if the shot needs sound to make sense, how it reads muted |

## What the gate fails, and what it only warns about

**Fails:** wrong or missing schema/`build_id`/`build_status`; empty brief fields
(hook, verbs, three answers); a planned or unlisted feature on screen; a core verb never
shown; roles out of order or missing; not opening on gameplay; a card in the first
5 s; a near-black first frame; hook later than 15 s or genre later than 10 s; runtime
outside 15–120 s; shots under their legibility floor (hook 1.5, establish 2.0, others
0.8, flash 0.4); missing situation/action/consequence/new information; source footage
reused; intensity falling without `contrast`; text over budget or a banned adjective;
a non-player camera in hook/peak or over 15 %; capture integrity not clean, hash or
build mismatch, footage below native 16:9 4K; music with no provenance or tone note,
or fewer than 60 % of cuts on the beat; an end card that isn't last and held, whose
text differs from `cta`, with more than one action, with unsourced or contradicting
facts (platforms vs `export_presets.cfg`; a prototype that doesn't say prototype); a
mix whose length isn't the timeline's; a done viewer test whose viewers failed.

**Warns (resolve or justify in the handoff):** runtime outside the type's window,
no music, no drop before the peak, 60–80 % of cuts on the beat, over 30 % sub-second
cutting in the first 40 %, an implemented feature neither shown nor in `cuts[]`,
muted/viewer tests pending, a hook longer than 30 words.

**Cannot check:** that a shot is actually legible, that nothing in frame is buggy,
that the music suits the game, that a described action occurs, that the attestations
are true, that a stranger understands the game. Those are frame review, a listen,
and the viewer test.
