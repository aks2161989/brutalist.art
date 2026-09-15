# SCRIPT — Download Brutalist with Claude Code (episode 02)

**Playlist:** Brutalist · **Channel:** @HumanitariansAI · **Persona:** Liam, in for Bear · **Voice:** Kokoro `am_onyx`

Ten beats. Cold open on `ClaudeComposerAsk`, hesitant-writer BLUF second, six body beats (concept illustrations), a verdict artifact, a paste-ready `Your Turn`, and a title-restate outro. No captions.

---

## B00 · ASK · `ClaudeComposerAsk` (16:9) — 12.99s

> Ciao. This is Liam, in for Bear. You already have Claude Code. So downloading Brutalist is one paste into the composer. Not a wizard, not a package. A git clone, a free doctor script, and a readiness table. Here is what actually happens.

## B01 · BLUF · `BrutalistHesitantWriter` — 18.67s (`lead_silence_s: 0.8`)

> Most fellows hear download and picture an installer. A .dmg, a click through, a license. That is not what this is. Brutalist is a git clone plus a free doctor script. The clone is your source tree. The doctor tells you exactly which pieces are ready. That is the whole idea, and it is worth caring about because everything you do next is just editing files in that folder.

**Landscape (16:9):** writer types `Downloading Brutalist needs an installer-wizard.` and rewrites the three trigger tokens `needs, an, installer-wizard` → `is, a, git-clone`. Corrected line: `Downloading Brutalist is a git-clone.` — clean grammar, the reel's actual claim.

**Portrait (9:16):** six single-word rows (`Downloading / Brutalist / is / running / an / installer.`) at fontSize 320 to satisfy Gate V's 55% fill floor, triggers `running, an, installer` → `just, a, git-clone`. Corrected line: `Downloading Brutalist is just a git-clone.`

## B02 · FRAMEWORK · `DbcPasteReady` — 16.94s

> Here is the paste-ready request. Open Claude Code in an empty folder. Paste this. It clones the public toolkit repo from github dot com slash nikbearbrown slash brutalist dot art into your folder, runs the free installer for you, and reports back which features are ready. You never leave the composer.

Shows the composer-shaped card holding the ask, three chips underneath (CLONE / INSTALL / VERIFY) with the exact commands.

## B03 · WORKED EXAMPLE · CLONE · `DbcCloneTree` — 19.18s

> This is what the clone actually drops onto your disk. A shell script called setup. A shell script called art. A skills folder with the builder recipes. A runtime folder with the Kokoro voice, the Remotion project, and the Python scripts that do the work. A docs folder. A README. That is your toolkit. No hidden state, no global install, nothing outside this folder.

The tree matches the actual folder contents in `demo/clone-tree.txt`. `setup` and `art` carry a terracotta ENTRY chip.

## B04 · WORKED EXAMPLE · SETUP DOCTOR · `DbcDoctor` — 20.57s

> Now run the doctor. Dot slash setup dash dash install once, to pull the free dependencies. Then plain dot slash setup, over and over, to see the readiness table. Green means the feature is live. Red means one dependency is missing, and the doctor tells you exactly which install command to run. It is the same script the sandbox in this reel just executed — the readings on screen are real.

Table mirrors `demo/setup-output.txt`. All seven features report READY on this machine.

## B05 · FRAMEWORK · SUBSCRIPTION vs API · `DbcLanes` — 21.55s

> This part trips fellows up, so read it slowly. Your Claude Code subscription is what lets the agent think and write. That is one lane. A paid Anthropic API key is a different lane — optional, metered, only needed if you script Claude outside the desktop app. Brutalist itself doesn't spend a cent. Kokoro is a local voice model. Remotion renders on your machine. Manim runs on your machine. Free by default — that is the shape of this tool.

Three lanes, only the FIRST and THIRD are load-bearing. Middle lane muted (ghost tone) because it's marked OPTIONAL.

## B06 · FALSIFIABILITY · `DbcNotClaims` — 19.20s

> Now the honest limits. Setup does not sign you into anything — no accounts are created. Setup does not touch any file outside the folder you cloned into. Setup does not upload. It does download one thing from the public internet the first time you run install — the Kokoro voice model, about three hundred forty megabytes, straight from a GitHub release. That is the whole network footprint.

Sources: setup script lines 89–99 (Kokoro model download from `github.com/thewh1teagle/kokoro-onnx/releases`).

## B07 · VERDICT · `DbcVerdict` — 11.48s

> Verdict, in three lines. Clone the repo — you have the toolkit. Run the doctor — you know exactly what is ready. Keep the free lane — the pipeline itself never asks for a card. That is how you download Brutalist.

Artifact card with three numbered lines.

## B08 · YOUR TURN · `ClaudeComposerAsk` — 18.39s

> Your turn. Open Claude Code in an empty folder and paste this prompt. It clones the toolkit, runs the free installer, reads back the readiness table, and asks you which feature you want to try first. When Claude hands back the table, look at it — red rows are the doctor telling you which install command to run next. That is the loop. Now you have Brutalist on disk.

Greeting `Your Turn`. The composer's `command` field IS the actual paste-ready prompt the viewer copies (the prompt says: clone, run `./setup --install`, read `./setup` back, ask before running any fix). Liam reads the intent aloud and points out the loop.

## B09 · OUTRO · `DbcOutro` — 5.91s

> That was Download Brutalist with Claude Code. Liam, in for Bear. For Humanitarians AI.

Native custom outro; title restated, `@HumanitariansAI` handle hardcoded (bypasses the shipped `ClaudeTitleOutro`'s `@NikBearBrown` lock per OUTRO-LOCK.md).
