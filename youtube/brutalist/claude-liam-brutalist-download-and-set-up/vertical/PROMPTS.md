# PROMPTS — Download Brutalist with Claude Code

Two composer prompts appear on screen: the framing ask at B00 and the paste-ready handoff at B08.

## B00 — The ask (composer, `* Ciao, Liam`)

> Clone the public Brutalist toolkit into this folder and run the free setup doctor for me.

Running indicator: `reading the setup script…`

Response lines (three chips):
- `git clone https://github.com/nikbearbrown/brutalist.art .`
- `./setup --install  →  free deps + Kokoro voice model`
- `./setup  →  readiness table (✅/❌ per feature)`

This is a **rehearsal**, not a live agent call. The commands shown are the ones a real Claude Code session would issue.

---

## B08 — The paste-ready prompt (composer, `Your Turn`)

The prompt the viewer copies verbatim into their own Claude Code session:

> In this empty folder, clone https://github.com/nikbearbrown/brutalist.art into the current directory, run ./setup --install for me, then read ./setup back and tell me which features are green and which are red. If any are red, quote the install command the doctor prints and ask me if you should run it.

Running indicator: `paste this into Claude…`

Expected-outcome lines below the composer:
- clones the public toolkit into the current folder
- runs `./setup --install` (free deps + Kokoro voice)
- reads back the readiness table and asks before running any fix

Liam reads the prompt aloud and points out the loop the fellow should watch for: when Claude prints the readiness table, red rows tell you (via the doctor's own miss messages, `setup` lines 128–140) which install command to run next. The prompt deliberately asks Claude to **stop before running a fix**, so no destructive command is issued without human approval.

---

## What is deliberately NOT shown

- No fresh `git clone` was executed on-camera. The file/folder evidence in B03 is from the isolated toolkit copy at revision `ba2d0e0`, which is byte-for-byte identical to a fresh clone of the public repo.
- No `./setup --install` was executed on-camera. The dark table in B04 mirrors real live doctor output (`demo/setup-output.txt`) from a machine where the model + deps already exist — no fresh install would have exercised the download step for the video.
- No Anthropic API key or Claude account credential is entered anywhere in the reel.
