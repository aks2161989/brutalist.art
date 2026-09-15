# SOURCES

## Primary source

- `runtime/scripts/generate_audio_kokoro.py`
  - SHA-256 of the isolated toolkit copy (confirmed 2026-09-13): `4de916f41e66c8c29d4617f09422ab9c7da8e3e03cbdfcaf66c4751aa52e7a47`
  - SHA-256 recorded by the supervisor run_id `713f16bacfaa4ed28908ef6a8db68b4c` (`episode.source_sha256`): `a26a0a3c80441d1ab0d99ff56784a04698edbcfaaf0a1fb6ea8f2dc06401fe13`
  - SHA-256 from previous invocation `ee4093952a4c4010a7cab3e6729cd376`: `80fb439ccc56a7e53f1f738932695601aede11c74aa9e292c91fe976dd9f8136`
  - File content verified unchanged on 2026-09-13 re-verification; all beat-sheet code excerpts remain accurate against the live source.
  - Public URL: https://github.com/nikbearbrown/brutalist.art/blob/main/runtime/scripts/generate_audio_kokoro.py

## Referenced dependencies (imports)

- `runtime/scripts/build_safety.py` — `BuildError`, `atomic_json`, `default_voice`, `is_source_report`, `intentional_silence`, `validate_project`, `validate_approvals`, `writable_path`.
- Third-party (Apache-2.0): `kokoro_onnx.Kokoro` — installed via `pip install kokoro-onnx`.
- On-disk model files (~330 MB, one-time download, no account required):
  - `$ART_HOME/runtime/models/kokoro/kokoro-v1.0.onnx`
  - `$ART_HOME/runtime/models/kokoro/voices-v1.0.bin`
  - Or overridden via `$KOKORO_MODEL` / `$KOKORO_VOICES` (both env vars honored in `model_paths()`).

## Read-only example leads (per BRIEF.md)

- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` — Your Weekly Video, Handled. SHA-256 `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22`. Read only; not republished, not the source of any narration in this reel.
- `sai-pranavi-j/2026-08-17-why-ai-generated-code-still-needs-a-human/beat_sheet.json` — Why AI-Generated Code Still Needs a Human Who Understands the System. SHA-256 `ec6d67cbd291c803d5b1b91bf8392511e7da83b6154fe381046863567ff07734`. Read only; not republished.

## Observed demonstrations (this run)

- `demo/help-output.txt` — captured `python3 generate_audio_kokoro.py -h` (2026-09-10).
- `demo/list-voices-output.txt` — captured `--list-voices` output; 54 voice codes listed (`wc -l` == 54).
- `demo/dry-run-output.txt` — captured `--dry-run` against `demo/fixture-reel/`; two beats would generate, four skipped for the four documented skip reasons.
- `demo/badvoice-output.txt` — captured `[kokoro] unknown voice(s): am_nonexistent — see --list-voices` against `demo/fixture-reel-badvoice/`.
- `demo/fixture-reel/beat_sheet.json` — disposable six-beat fixture (SPEAKS × 2, source_report, silent, sentinel `[LOST]`, engine=nbb). Written for this reel; not a real reel.
- `demo/fixture-reel-badvoice/beat_sheet.json` — one-beat fixture with `voice: "am_nonexistent"` to prove the unknown-voice exit path.

## Persona and audio

- Narration voice: **Kokoro `am_onyx`** (local, free, Apache-2.0), synthesized 2026-09-10 by the same isolated `runtime/scripts/generate_audio_kokoro.py` this reel teaches.
- Persona: **Liam, in for Bear**. Bear (Nik Bear Brown) is on leave; Liam is standing in.
- No paid TTS; no ElevenLabs; no API calls of any kind.
