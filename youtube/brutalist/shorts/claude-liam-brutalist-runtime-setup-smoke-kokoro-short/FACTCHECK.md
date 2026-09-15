# FACTCHECK — Brutalist Utility: setup_smoke_kokoro.py — Short

**Short cut: B00, B01, B06, B08, B09, B10 retained. No new claims added.**  
All narration carried from parent without modification. Parent FACTCHECK verified claims against source SHA-256: 4e4df6611a34dcc1e001241769bc6479abf947effa58315d09cec4e8a04a0e30.

---

All claims verified against `runtime/scripts/setup_smoke_kokoro.py` (SHA-256: 4e4df6611a34dcc1e001241769bc6479abf947effa58315d09cec4e8a04a0e30).

| Claim | Beat | Verdict | Source / Derivation |
|---|---|---|---|
| Script is "setup's audio gate" | B00, B02 | ✓ | Module docstring line 1: "setup's audio gate." |
| Script exits 0 only if audio is real | B00 | ✓ | main() returns 0 only on line 70 after mean_db > THRESHOLD_DB |
| Three prerequisites: model files, ffmpeg, kokoro_onnx | B02, B03 | ✓ | Lines 31–39: MODEL.exists(), shutil.which("ffmpeg"), ImportError guard |
| One synthesis step | B02, B04 | ✓ | Lines 41–43: k.create("This is a setup smoke test.") |
| One volume gate at -40 dB | B02, B05 | ✓ | THRESHOLD_DB = -40.0 (line 22); comparison at line 66 |
| Phrase used: "This is a setup smoke test." | B04 | ✓ | Line 43 verbatim |
| Voice used in smoke test: "af_bella" | B04 | ✓ | Line 43: voice="af_bella" — NOT am_onyx (narration voice) |
| Model path: runtime/models/kokoro/kokoro-v1.0.onnx | B03 | ✓ | Lines 19–20: ROOT/runtime/models/kokoro/kokoro-v1.0.onnx |
| Voices path: runtime/models/kokoro/voices-v1.0.bin | B03 | ✓ | Lines 19–21: ROOT/runtime/models/kokoro/voices-v1.0.bin |
| ffmpeg detected via shutil.which | B03 | ✓ | Line 33: ffmpeg = shutil.which("ffmpeg") |
| Float samples → int16 via clamped multiply | B04 | ✓ | Lines 48–49: max(-32768, min(32767, int(s * 32767))) |
| WAV written to temp file via tempfile.mkstemp | B04 | ✓ | Line 50: tempfile.mkstemp(suffix=".wav") |
| ffmpeg volumedetect run via subprocess.run | B05 | ✓ | Lines 58–61 |
| mean_volume parsed from stderr | B05 | ✓ | Lines 63–65: loop over out.stderr.splitlines() |
| mean_db <= -40.0 → fail | B05 | ✓ | Line 66: if mean_db <= THRESHOLD_DB |
| Fail message format: "[smoke] {msg}" to stderr | B06 | ✓ | Lines 25–26: fail() function |
| All five failure paths exit 1 | B06 | ✓ | fail() returns 1; main() returns fail() on each guard |
| Setup discards output, reports own MISS | B02 | ✓ | Module docstring: "setup's check() discards output either way and reports its own MISS message" |
| try/finally deletes temp WAV unconditionally | B07 | ✓ | Lines 52–72: try/finally with Path(wav_path).unlink(missing_ok=True) |
| "one throwaway phrase" — docstring | B07 | ✓ | Docstring line 3: "Synthesizes one throwaway phrase with Kokoro" |
| Real speech ~-12 to -20 dB typical | B05 | ✓ | Standard audio engineering knowledge; not from source (labeled as context only) |
| -14.3 dB in success example | B06 | EDITORIAL | Representative value; actual dB varies by host hardware. Labeled as representative in SOURCES.md |

## Teaching-arc classification

| Arc item | Status |
|---|---|
| FRAMEWORK beat (B02) | ✓ — explicit pipeline beat before any code detail |
| WORKED EXAMPLE (B03–B07) | ✓ — real code from source, step by step |
| FALSIFIABILITY / failure beat (B06) | ✓ — all five failure modes shown |
| SCAFFOLDED viewer task (B09) | ✓ — prompt + what to look for ("what's separated from what's shared") |
| Four bookends | ✓ — B00 (ask) · B08 (verdict) · B09 (your turn) · B10 (outro) |
| No source, no verdict | ✓ — all code on screen is source-backed verbatim excerpt |
