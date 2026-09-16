# PROMPTS — The screen-clean Skill

## B00 · Composer ask (cold open, typed on screen, spoken as intro)

```
What does the `screen-clean` skill actually do to a screen recording?
Read skills/make/screen-clean/SKILL.md and tell me — the mental model,
not the frontmatter blurb.
```

Output lines shown after the send button arms:

- shared preprocessor called by `fellows` and `guests`
- five passes: PROBE / ASPECT-FIT / LEGIBILITY / PRIVACY-SCAN / TRIM
- returns a 1920×1080 beat + a contact sheet — never publishes

## B10 · Composer handoff (Your Turn — paste-ready dry run)

Paste this into Claude Code. It exercises Pass 1 on a synthetic fixture and
reasons about Pass 2 without touching any real recording.

```
Read skills/make/screen-clean/SKILL.md end to end.

Then make ONE synthetic screen recording so nothing personal is at risk:

  ffmpeg -y -f lavfi -i "color=c=0x2D2D2D:s=2560x1600:d=6:r=30" \
         -f lavfi -i "anullsrc=cl=stereo:r=44100" \
         -c:v libx264 -pix_fmt yuv420p -c:a aac -shortest fixture.mp4

Follow the doctrine of Pass 1:

  ffprobe -v error -select_streams v:0 -show_entries \
    stream=codec_name,width,height,r_frame_rate -of default=nw=1 fixture.mp4
  ffprobe -v error -select_streams a:0 -show_entries \
    stream=codec_name,sample_rate,channels -of default=nw=1 fixture.mp4
  ffmpeg -hide_banner -i fixture.mp4 -af volumedetect -f null - \
    2>&1 | grep -E 'mean_volume|max_volume'

Read the mean_volume. If it is below -40 dB, print the STOP verdict and
halt — do NOT proceed to Pass 2.

Then WITHOUT running any crop, reason about Pass 2 on a 2560×1600 source
with a ~72 px taskbar. State the output dimensions and bar widths for each
of the three routes:
  A — pillarbox, no crop
  B — crop the taskbar only (~72 px)  [the default]
  C — full crop to 16:9

Do NOT touch a real screen recording. Do NOT run the crop. This is a
doctrine dry-run of screen-clean's own Pass 1 and Pass 2 tables.
```

Follow-up (dig deeper):

- Why is the mean_volume gate at -40 dB specifically, and what would
  happen downstream if the gate were set to -60 dB instead?
- What could go wrong if a screen recording had a Zoom control bar at the
  bottom in addition to the OS taskbar — which of A / B / C / D would you
  pick, and why?

## Prompt principles applied

- Paste-ready — one block, self-contained, produces a useful reasoning
  output without watching the film again.
- Real tools only — `ffmpeg`, `ffprobe`, `grep`. Nothing paid; no publishing.
- Safe by construction — the fixture is synthetic, the file is disposable,
  the crop is deliberately not executed. This is a doctrine walkthrough,
  not a preprocessor run against a personal recording.
