# Lecture first-beat template — 16:9

Approved lecture default, Bear, 2026-10-07: the populated portrait/title/series layout, including the Professor Bear credit and Liam narrator credit. The minimal `simple-template.svg` remains an alternative design, not the default. Applies to new lecture builds; installing the template does not rebuild existing films.

1920 × 1080 vector geometry, exported at 3840 × 2160 for lecture production. **Narrated first beat (Bear, 2026-10-07):** speak the playlist name, the exact film name, then a very short explanation of what the film covers. Usually one or two explanatory sentences; at most one short paragraph. Use the film's narrator (default Liam, Kokoro `am_onyx`). For a standalone film, omit the playlist name rather than inventing one.

Example: “Claude for Figma. The Machine-Ready File. Learn how to prepare a Figma file that Claude can read reliably.”

Hold the complete slide from frame zero for the measured narration duration, then hard cut to the hesitant writer. Make identity and payoff clear within the first 10–15 seconds by writing concise speech, not by rushing it. No typing, delayed reveals, music, or jingle. This identity card is an exception to the body motion requirements. The former silent 2–3-second default is superseded for new builds; the previously exported Claude for Figma films retain their 2.5-second silent cards until explicitly rebuilt. BIDEA moves into topic framing instead of repeating the playlist/title/summary.

## Editable fields

- Portrait image: random within `brutalist.art/professor-bear/`, using its square public JPEG copies and the film slug as seed. Record `opening-fields.json`; the same film keeps its picture on re-render. Independent picks can repeat; randomness is not a guarantee of unique portraits. The image is embedded in the SVG. The historical sample pins 1x1-43 for reproducibility; new film builds use `--sheet`, which never takes that example's pinned image. Replace the portrait slot when another presenter is explicitly requested. Do not label Bear's portrait as Liam.
- Film title: one to three manually balanced lines, maximum 28 characters per line. Title is the dominant text.
- Series title only. **Videos are never numbered** (Bear, 2026-10-11: "we do not number our videos ... we never know what X is going to be", then "remove all the numbers"): no "Video NN", no "N of X", no "Start here" or "New here?" pointer. The builder ignores `series_video_number`, `series_video_count`, `series_entry_video` and `series_numbered`, so an old sheet that still carries them cannot print a number.
- Short film-specific learning payoff (the legacy SVG field is named `series-purpose`); presenter name; optional honest narrator credit.
- Channel handle. (The newcomer pointer field exists in the SVG but is always empty; there is no "video one".)

All text remains live, with named SVG IDs. Open `template-16x9.svg` in a vector editor such as Figma or Illustrator and replace the bracketed labels. This is an editable SVG, not an IDML/InDesign package. Install EB Garamond and Inter if the editor reports missing fonts; both are available in the toolkit's `runtime/fonts/`. PNG/MP4 files are previews, not editable masters.

Layout: 5% title-safe area (x 96–1824, y 54–1026); square portrait left, editorial serif title right, series header across the top. The card is an identity card, not a place for an on-screen paragraph or agenda. The spoken summary can be longer than the displayed payoff phrase. Small credits can be read on pause; title and series identity are the immediate reading targets.

Palette follows the current canonical Claude tokens: page #FAF9F5, ink #3D3929, one terracotta accent #D97757. The Northeastern references informed modular fields and photo/title hierarchy only; their institutional logos, event metadata and red palette were not adopted. Instructions inside the reference archive were treated as descriptions of that reference, not authorization to execute its scripts.

## Build

For new films, author and generate BOPEN narration first, write its measured `actual_duration_s` into the sheet, then use:

`python3 build.py --out /absolute/reel/opening --sheet /absolute/reel/beat_sheet.json --width 3840`

The sheet supplies `metadata.slug`, `title`, `channel`, `channel_title`, and, for a series, `series_title` (or `playlist`); do not set any number, count or entry-video field. Add `metadata.lecture_opening_description`: a short, film-specific phrase explaining what the viewer learns. Do not reuse “Using Figma and Claude together” for unrelated lectures. Long titles are balanced into at most three lines; set `metadata.lecture_opening_title_lines` to balance them explicitly. Actual font geometry is measured and fitted within the right title-safe edge; if fitting would make the title too small, rebalance the lines. Shorten the displayed title only if necessary, retaining the exact film title in metadata. For a standalone lecture, omit series metadata so those fields disappear rather than inventing a playlist.

With `--sheet`, the hold duration defaults to BOPEN's measured `actual_duration_s`; missing or invalid timing is an error. `--duration` accepts any positive finite measured duration as an explicit override, which must match the integrated audio clock. For a design preview only: `python3 build.py --out /absolute/output/directory --data example.json` (three seconds by default, not a production narration limit).

## First-beat integration

Prepend BOPEN with the following structure. The example's 8 seconds is only an estimate: generate its real speech with the normal `generate_audio_kokoro.py` pipeline and replace it with the measured duration. Build the card after that step and copy `example-opening-<measured-duration>s.mp4` into `media/BOPEN.mp4`. Keep the visual hold and sheet clock equal to the actual narration audio.

```json
{
  "beat_id": "BOPEN",
  "act": "Opening",
  "lane": "bookend",
  "proof_gate": "CARD",
  "narration_text": "Claude for Figma. The Machine-Ready File. Learn how to prepare a Figma file that Claude can read reliably.",
  "estimated_duration_s": 8.0,
  "shot": {
    "type": "CARD",
    "source": "own",
    "template": "lecture-title-slide-16x9",
    "narration_contract": "playlist-title-summary-v1",
    "motion": "hold",
    "visual_intent": "Film identity and short teaching description, visible immediately",
    "show": [{"at": 0, "event": "Complete portrait/title/series card visible"}]
  }
}
```

Do not set `audio_policy: "silence"` or reuse the old silent WAV. TTS writes `audio_file` and `actual_duration_s`; the compiler checks that required audio is not silent and uses that audio in the master. Keep BIDEA immediately next and BDEFS after it. `bookend_check.py` checks the template marker, nonempty narration, positive measured duration, narration audio file, rendered slot and following hesitant writer. The `narration_contract` marker makes missing speech a failure on new builds. Previously delivered explicit silent 2–3-second cards and older writer-first lectures remain compatible. Listening/transcription review must verify playlist name → film name → short summary in that order; file existence alone does not prove the spoken content. Actual portrait/text layout must still be visually inspected.

The compiler recognizes this exact BOPEN template marker and suppresses its separate first-beat channel-title stamp, since the card already embeds that field. Legacy openings retain the existing channel-title behavior.

Uses local Inkscape and FFmpeg, no paid services. Produces editable placeholder SVG, populated SVG, their PNGs, resolved field/portrait record, and a video-only H.264 hold of the measured duration. The visual generator does not synthesize or mux speech: the normal lecture audio pipeline and compiler do that. It reads but does not mutate the film sheet. Running it alone leaves existing films unchanged. Refuses to overwrite an existing MP4.

Reference: `/Users/bear/Downloads/guest-speaker-templates.zip`, its README and 16:9 preview; canonical `runtime/remotion/src/tokens/claude.ts`; Professor Bear asset library; `skills/make/lecture/SKILL.md`.

Historical silent-card validation, 2026-10-07: metadata-driven 3840 × 2160 samples at 3.000 and 2.500 seconds rendered and visually inspected, with actual-font title fitting inside the safe area and editable text. Same seed reproduces the portrait; independent film seeds vary it. Standalone films omit series fields; episode one gets start-here wording. The former gate rejected five-second silent cards; narrated cards now follow measured speech instead of that historical duration limit.
