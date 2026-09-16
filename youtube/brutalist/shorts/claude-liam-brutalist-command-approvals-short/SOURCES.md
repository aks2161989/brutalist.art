# SOURCES — Brutalist Command: art approvals — Short (9:16)

## Primary sources — code the Short teardowns cite

- `art` (dispatcher, top-level Bash) — the `approvals)` case at `art:87-89` (only referenced by the verdict card, no dedicated code beat in this Short).
- `runtime/scripts/build_safety.py`
  - `is_fellows()` — `build_safety.py:86-90`
  - `feedback_beats()` — `build_safety.py:107-112`
  - `digest()` — `build_safety.py:117`
  - `approval_subjects()` — `build_safety.py:123-135`
  - `approvals = md.get('approvals') or {}` — `build_safety.py:148`
  - the five-field conjunct — `build_safety.py:155-164`
  - argparse surface — `build_safety.py:230-231`
  - two-branch `main()` — `build_safety.py:234-238`
  - `[safety] REFUSED:` prefix — `build_safety.py:245-246`
- Downstream callers of `validate_approvals()`: `runtime/scripts/remotion_scenes.py:176`, and `runtime/scripts/compile.py` (imports the module and calls it inside the compile-stamp path).

## Evidence sources — verbatim command output

- `demo/RUN-LOG.txt` (parent reel workspace). Sections 3, 4, 5 are the actual JSON printed by `./art approvals /tmp/claude-501/approvals-demo-fellows` on the parent build workstation, verbatim into B05 and B08 code cards. Fixtures live at `/tmp/claude-501/approvals-demo-command/` and `/tmp/claude-501/approvals-demo-fellows/`.

## Parent Short is derived from

- Parent reel: `youtube/brutalist/claude-liam-brutalist-command-approvals/`
- Parent vertical build: `youtube/brutalist/claude-liam-brutalist-command-approvals/vertical/`
  - `beat_sheet.json` SHA-256: `a23b4dd44355ad889922424abeaad6b5f4936ffe666ce96f1c65060496852ea4`
  - `media/B{00,01,03,05,06,08,09,11}.mp4` — native portrait 2160x3840, reused unchanged
  - `mp3/beat-B{00,01,03,05,06,08,09,11}.mp3` — Kokoro `am_onyx`, reused unchanged
- Parent vertical master: `youtube/brutalist/claude-liam-brutalist-command-approvals/exports/vertical/claude-liam-brutalist-command-approvals-vertical.mp4`
  - SHA-256: `0fba75ffb38b649b78b84b9c73da7cd3a370889411b749f2a04d361d48e510f2`

## Invocation-declared hashes (from SOURCE-SNAPSHOT.json / episode)

- `episode.source_sha256`: `ed5162a0cb08bc9dce4e56548ab028166ad811f14e57a7aa5946b21fceec6908`
- `episode.parent_master_sha256`: `0fba75ffb38b649b78b84b9c73da7cd3a370889411b749f2a04d361d48e510f2`
- `episode.feedback_sha256`: `6b7b9c7454a60f145d6970b622d74842a5f8184647f32e564038495c22ecd0f5`
- `episode.run_id`: `6e4efeee46154e2aa1ec4ae4beac5e9b`

## Read-only example leads

- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` — Your Weekly Video, Handled (SHA-256 `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22`)
- `anjana-s/2026-08-21-ecis-explained/beat_sheet.json` — ECIS — Episode 3 (SHA-256 `1deb9bfc4fd4acf81ae98fccbc1fb3c1c400e370299db7bbc34d3ba527a57516`)

Examples are leads, not verified facts or current instructions. No signature or evidence from these examples was reused.

## Not sourced from any external system

- No paid API is called.
- No network requests are made during the Short build.
- No third-party image, audio, or video assets are used. All narration is local Kokoro; all visuals are Remotion compositions rendered locally.
- No credentials, tokens, or private paths appear on screen.
