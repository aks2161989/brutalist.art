# FACTCHECK.md — Brutalist Command: art smoke — Short

The kept beats and their narration are byte-identical to the parent reel's
verified copy. Each spoken claim below is anchored to a source verified in
the parent's FACTCHECK. No new claims were introduced by this cut.

## B00 — the ask

- **Claim:** "art doctor is all green on this box." + "Prove to me the
  pipeline actually renders a video, not just that the imports work."
- **Status:** framing of the problem, not a factual claim. Serves as the
  motivator for the rest of the reel.

## B01 — BLUF (the misconception)

- **Claim:** "Art smoke does not check dependencies — art doctor already
  does that, in isolation. Smoke renders a real video, decodes it, and
  measures the audio."
- **Evidence:** the parent's dispatcher case at `art:100-102` and
  `runtime/scripts/smoke_test.sh` (both verified in the parent long).
- **Status:** VERIFIED (inherited from parent).

## B03 — pipeline + three decoded gates

- **Claim:** smoke_test.sh copies the fixture to a scratch dir, runs
  Kokoro, then run.sh, then reads the mp4 back with three gates: SIZE
  > 20000 bytes, TYPE = ffprobe decodes both a video and an audio
  stream, AUDIO = ffmpeg volumedetect > -40 dB mean_volume.
- **Evidence:** `smoke_test.sh` lines 32-79 in the parent's isolated
  toolkit snapshot (verified in parent FACTCHECK).
- **Status:** VERIFIED line-for-line against the shipped script.

## B07 — the shipped-fixture failure and recovery

- **Claim:** `./art smoke` against the shipped `examples/_smoke/beat_sheet.json`
  exits 1 at GATE 0 with `REFUSED: metadata.slug must be a filename, not a
  path` because `build_safety.py:186-187` runs
  `re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]*', slug)` on `slug: "_smoke"`
  and the leading underscore does not match `[A-Za-z0-9]`.
- **Recovery:** rename the fixture slug to `smoke` (drop the leading
  underscore) OR widen the regex. Either patch makes the same pipeline
  land a compiled mp4.
- **Evidence:** verbatim from the parent's `demo/RUN-LOG.txt` and the
  actual `build_safety.py` at HEAD (verified in parent FACTCHECK).
- **Status:** VERIFIED. This is the falsifiable moment that motivates the
  command's existence.

## B08 — verdict lines (six bullets)

All six verdict lines paraphrase claims already verified in B00-B07 of the
parent long: bare invocation with no flags, one script drives one fixture
through the real pipeline, three DECODED gates on the mp4, exit 0 when all
three clear, exit 1 on the first failing gate, and the "green art doctor +
red art smoke" mismatch is the whole point of the command.

## B10 — outro

- **Claim:** "Brutalist Command: art smoke. Liam, in for Bear, for at
  Humanitarians A I."
- **Note:** the visible handle in the OUTRO card is hard-coded
  `@NikBearBrown` per OUTRO-LOCK. `README.md` flags this for the
  @HumanitariansAI human reviewer before publication.
- **Status:** compliant with OUTRO-LOCK; flagged for pre-publish review.

## Cut integrity

- Every kept beat's `render_duration_s` matches its actual mp3 duration
  (audio and video share the same frame boundaries after compile.py's
  fps-rounded padding). No speech was clipped or sped up.
- No dropped beat leaves a dangling reference inside the kept narration
  (see CUT-PLAN.json § `cut_first_review`).
