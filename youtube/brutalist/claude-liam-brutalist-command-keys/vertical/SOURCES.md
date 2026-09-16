# SOURCES — Brutalist Command: art keys

Episode 36 of the Brutalist playlist. Command teardown of `./art keys`,
delivered as `claude-liam` (Liam in for Bear, Kokoro `am_onyx`, Teardown
register) for the @HumanitariansAI channel adaptation.

## Primary source files (this invocation's snapshot)

Both hashes match `SOURCE-SNAPSHOT.json` for `run_id abdef8f04e1246deaf8cf7ab26ae350b`
and the invocation's `episode.source_sha256 7c3b6abf2ec61bb70122fe12ba1e2d5bad049db19db16ddb3a1026cad274e8c6`.
(Re-verified 2026-09-12: art and check_keys.py SHA-256 are unchanged from the original build.
Rebuild was triggered by updated SKILL.md files, not by source file changes.)

| Path (isolated toolkit) | SHA-256 | Role in this reel |
|---|---|---|
| `art` | `9bb77a7c84701d23ab6e73f0a4f48592f17748ffad2c7114b62687bb7f97d0e9` | Top-level dispatcher. The `keys)` case at art:103-104 is quoted verbatim in B02. |
| `runtime/scripts/check_keys.py` | `95ad03f14cac59d2b9f84584d305eb3df0a5f8470d5fb6688f79a5b605fcaaa0` | The whole script (83 lines). Docstring quoted in B00's ask, higgsfield probe body quoted in B06, `.env` loader quoted in B07, three status-row taxonomy quoted in B03. |

## Read-only example leads (from BRIEF.md)

Both are read-only fellows beat sheets whose *shape* informed the pacing (cold
open + BLUF + code-heavy body + Your Turn + outro). Neither reel was cloned;
neither human signature was reused; no old renders are presented as this run's
output.

| Lead | SHA-256 | Adapted here as |
|---|---|---|
| `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` | `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22` | Command-teardown pacing (paste-ready ask, ~20s framework beats, verdict artifact). |
| `yatra-r/2026-09-03-this-week-gordy/beat_sheet.json` | `7e3ea1f61c421e605e583be9b2a7b5f554aa8cadfb6e14dabaee66f471856083` | The Your-Turn beat that spends words on WHY the prompt (not just paste-and-run). |

## Playlist siblings

Command-teardown episodes 22–35 for the same channel (`claude-liam` · Teardown ·
@HumanitariansAI adaptation). This episode carries the same visual grammar,
same outro lock (`ClaudeTitleOutro` with the hardcoded `@NikBearBrown` handle
per `OUTRO-LOCK.md`), and the same `ClaudeCodeBeat916` portrait shim registered
in `runtime/remotion/src/Root.tsx` (added in this workspace's local override).

## Demonstration log

`demo/RUN-LOG.txt` is verbatim from this workstation on 2026-09-09. It contains
five sections:

1. **`./art keys` with higgsfield CLI installed, network unreachable** — the
   "invalid" row. Exit 0.
2. **`./art keys` with higgsfield removed from `$PATH`** — the "· unset" row.
   Exit 0.
3. **The exact source** — `wc -l`, docstring, and the higgsfield probe body
   (`check_keys.py` lines 38–58).
4. **The dispatcher case** — `grep -n -A1 '^  keys)' art` → art:103-104.
5. **Redaction proof** — a synthetic `.env` containing `MY_SECRET=this-should-never-print`;
   `grep -c` returns 0 occurrences in the command output. The `.env` was
   deleted before the run ended.

No paid API was called. No network upload happened. No credentials were read.
`higgsfield` is installed on this workstation (bin `/Users/bear/.nvm/versions/node/v24.17.0/bin/higgsfield`,
version `0.2.3`, no active login) — the demos never generate media, they only
probe `higgsfield account status` and report the exit code.

## Channel adaptation

- Metadata `channel: "@HumanitariansAI"`, composer `folderLabel:
  "@HumanitariansAI"`.
- Landscape metadata carries `channel_title: "@HumanitariansAI"` for the
  compile-time PIL overlay (Gate V confirmed clean for landscape — the overlay
  fits inside the burn-in exclude on 3840×2160).
- Portrait metadata **omits** `channel_title` per
  [[feedback-channel-title-portrait-bleed]] — the same overlay bleeds past
  SAFE916 on 2160×3840. The folder chip on the composer scenes carries channel
  identity in vertical.
- Outro is the locked `ClaudeTitleOutro` (`slug: "claude-liam-brutalist-command-keys"`)
  which hardcodes `@NikBearBrown` per `OUTRO-LOCK.md`. This is flagged in
  `README.md` for the human reviewer before publication.
