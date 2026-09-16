# FACTCHECK — Brutalist Utility: generate_audio_kokoro.py — Short

Derivative of the 12-beat parent vertical. Only beats B00, B01, B07, B09, B11 are retained.
All narration reused verbatim — no new factual claims introduced in this Short.
Source read at SHA-256 `4de916f41e66c8c29d4617f09422ab9c7da8e3e03cbdfcaf66c4751aa52e7a47`
(2026-09-10 isolated toolkit copy). Full fact-check for all 12 beats remains in the parent reel.

## B00 · ASK

- "No API key. No metered service. Just generate the audio locally, on this laptop, with the free engine." → docstring L4–L7 ("Kokoro is FREE — a local 82M-parameter Apache-2.0 model … No API, no meter, no quota; near-real-time on an M1's CPU.").
- "Skip the fellows report beat and the intentional silence beat while you're at it." → source L189: `if is_source_report(b, sheet) or intentional_silence(b): print(f'[kokoro] {bid} SKIPPED — source audio / intentional silence'); continue`.

## B01 · BLUF

- "Kokoro is not paid and remote. It is a free, local ONNX model that runs on this laptop's CPU." → docstring L4–L9 (Apache-2.0, ~28 named preset voices, no API/meter/quota, near-real-time on M1 CPU).
- "No account." → observed: 330 MB model files curled from a public GitHub release with no auth (see B04 curl block).

## B02 · FRAMEWORK

- Phases WALK/FILTER/SYNTH/ENCODE/STAMP map to source structure: `main()` argparse → `load_engine()` → filter loop over `sheet['beats']` → per-beat `k.create()` + `write_mp3()` + `measure()` → `atomic_json(sheet_path, sheet)` + `atomic_json(timings_path, timings)`.
- "Atomically write the actual duration and audio file path back into the beat sheet" → `build_safety.atomic_json` writes via tempfile + `os.replace` (verified in `build_safety.py:35-48`).

## B03 · MECHANISM 1 — CLI surface

- The `--help` block reproduced in the code card is captured verbatim in `demo/help-output.txt` (2026-09-10 run).
- "Fifty four Kokoro preset voice codes" → captured in `demo/list-voices-output.txt`; `wc -l` = 54.
- "Dash dash no gate is deprecated — it cannot bypass human approvals" → argparse help string, source L153: `help="deprecated; cannot bypass human approvals"`.
- Note: the docstring at L8 claims "~28 NAMED preset voices"; the shipped `voices-v1.0.bin` today enumerates 54. The reel uses the observed count.

## B04 · MECHANISM 2 — model_paths + load_engine + lang_for

- `model_paths()` source L80–L85 — ART_HOME + `runtime/models/kokoro/` + env overrides KOKORO_MODEL / KOKORO_VOICES.
- `load_engine()` source L88–L101 — checks both files exist, prints the exact curl block on miss, then imports `Kokoro` from `kokoro_onnx` (prints `pip install kokoro-onnx` on `ImportError`).
- `LANG_BY_PREFIX` source L104–L114 — 9 languages: `a=en-us, b=en-gb, j=ja, z=cmn, e=es, f=fr-fr, h=hi, i=it, p=pt-br`.
- "Narration for a non English voice must be IN that language" — verbatim comment on `lang_for()` source L119.
- "Three hundred and thirty megabytes, one time" — actual file sizes: `kokoro-v1.0.onnx` 325,532,387 bytes (~325 MB), `voices-v1.0.bin` 28,214,398 bytes (~28 MB); total ~354 MB. Docstring reports "~330MB total" — matches close enough to sub-10%.

## B05 · MECHANISM 3 — five skip rules

Source L186–L208 line-for-line:
1. `is_source_report(b, sheet) or intentional_silence(b)` → L189.
2. `if not text: continue` → L193–L194.
3. `text.startswith(('⚠', '[LOST]', '[PLACEHOLDER]'))` → L195.
4. `a.only is not None and bid not in a.only` → L200.
5. `str(b.get('engine', 'kokoro')).lower() != 'kokoro'` → L202–L206.

"Real incident, twenty twenty six, August" → source comment L196: "A sentinel is a note to humans, not a script. Voicing one ships 'narration lost' as narration (incident 2026-08-27). Hard skip."

## B06 · MECHANISM 4 — normalize_for_tts + write_mp3 + measure

- `SYMBOLS` table source L60–L66 — includes ψ→psi, Ψ→Psi, ℏ→h-bar, |ψ|²→psi squared, ∫→integral of, →→goes to, ≥/≤, Δx/Δp/ΔE, ∞, E₀/E₁, ·→ times, ²→ squared, ½→one half, —→", ".
- `normalize_for_tts()` source L69–L72 — plain loop, `text.replace(sym, spoken)`.
- `write_mp3()` source L123–L136 — scratch dir prefix `.tts-`, wave.open() at sample_width=2, ffmpeg `-c:a libmp3lame -q:a 2`, `os.replace(encoded, out_mp3)`.
- "Copy-on-write output: never follow a Short's legacy link into its parent." — verbatim comment on `write_mp3()` source L124.
- `measure()` source L139–L143 — `ffprobe -v error -show_entries format=duration -of csv=p=0 <path>`.
- Ground-truth stamping source L237–L239: `b["audio_file"] = f"mp3/beat-{bid}.mp3"`, `b["actual_duration_s"] = round(dur, 2)`, and `timings[bid] = round(dur, 2)`.

## B07 · WORKED EXAMPLE — demo/fixture-reel dry-run

- Observed output identical to `demo/dry-run-output.txt`:
  ```
  [kokoro] B02 SKIPPED — source audio / intentional silence
  [kokoro] B03 SKIPPED — source audio / intentional silence
  [kokoro] B04  SKIPPED — narration_text is a sentinel, not narration
  [kokoro] B05  engine=nbb — skipped (run its own generator, e.g. generate_audio.py --only B05)
  [kokoro] (dry-run) B00  voice=am_onyx  49 chars
  [kokoro] (dry-run) B01  voice=am_onyx  24 chars
  [kokoro] 2 beat(s) would generate — cost: $0.00
  ```
- The fixture has 6 beats with the exact shapes described in the code card.

## B08 · MECHANISM 5 — failure modes

- Model missing branch source L90–L96 — reproduces the exact `sys.exit(...)` block with the two `curl -LO ...` commands.
- Import failure branch source L97–L100 — `except ImportError: sys.exit('[kokoro] pip install kokoro-onnx   (free, local — no key)')`.
- Unknown voice branch source L221–L225: `bad = sorted({v for _, v, _ in todo} - known)` → `sys.exit(f'[kokoro] unknown voice(s): {", ".join(bad)} — see --list-voices')`.
- Observed unknown voice failure captured verbatim: `[kokoro] unknown voice(s): am_nonexistent — see --list-voices` (see `demo/badvoice-output.txt`).
- Sentinel skip is quiet — prints SKIPPED, `continue`, never mutates the sheet (source L195–L199).

## B09 · VERDICT

- All six lines paraphrase claims verified above.
- "Same interface as the paid engine — downstream never knows which engine spoke" → docstring L11–L16: "THE INTERFACE IS THE HOUSE INTERFACE — identical to generate_audio.py: … Durations are GROUND TRUTH for all downstream timing. Downstream never knows which engine spoke."

## B10 · YOUR TURN

- Prompt is executable-shaped; no destructive actions are asked for. The command form matches the shipped CLI: `python3 runtime/scripts/generate_audio_kokoro.py <reel> --dry-run` and `--only B0X B0Y`.
- The claim that "no MP3 written for the silent beat" is enforced by source L189 (silence skip).

## B11 · OUTRO

- Title matches metadata.title exactly.
- Handle is @NikBearBrown per OUTRO-LOCK.md; @HumanitariansAI (this playlist's channel) is spoken aloud in narration. Flagged in `README.md` for the human reviewer.

## Discrepancies deliberately preserved

- Docstring "~28 named preset voices" vs observed 54 voices: the reel narrates the observed number, `demo/list-voices-output.txt` is the evidence.
- Docstring "~330MB total" vs measured ~354 MB: the reel repeats the docstring figure (~330MB) since that is what `load_engine()` prints to the user on the failure path.
