# SCRIPT — Brutalist Utility: remotion_scenes.py — Short

Retained beats: B00, B01, B02, B03, B06, B08, B09, B11
Total: ~128.96s

---

**B00 — COLD OPEN (16.29s)**
Sawadee — this is Liam, in for Bear. remotion_scenes.py is the Brutalist pipeline's Remotion runner. It looks like a thin shell around npx remotion render. It's not. It's a gated, provenance-stamping layer that makes scene rendering safe, repeatable, and traceable for every beat in the reel.

---

**B01 — BLUF (12.75s)**
remotion_scenes.py renders only pattern-tagged slate beats — not every scene, not anything you point it at. It's a gated provenance-stamper: it reads the beat sheet, checks what's already filled, renders the gaps, then writes the receipts.

---

**B02 — FRAMEWORK (21.79s)**
Four steps, one pass. First, detect: slate_resolves checks each beat — if media slash BXX dot mp4 already exists, skip it. Second, render: npx remotion render, scale two, CRF sixteen. Third, extend: the last frame freeze-holds to match the measured audio duration. Fourth, stamp: provenance is written back into beat_sheet.json, and the consumer index is updated.

---

**B03 — THE ENTRY TICKET (13.88s)**
The script ignores every beat that doesn't have shot dot remotion dot pattern set. That single field is the entry ticket. No pattern, no render — the beat stays a slate. The pattern also selects which Remotion composition to render by name.

---

**B06 — THREE GATES (17.83s)**
Three gates run before any beat renders. validate_project checks the beat sheet is structurally sound. validate_approvals is the fellows safety gate — a reel that requires approval cannot render until it has one. slate_resolves is the idempotency check: media file already there and no --force flag? Skip. Reruns are always safe.

---

**B08 — FAILURE MODE (22.96s)**
When npx remotion render exits nonzero, render_beat returns a FAIL: string with the pattern name and the last 800 bytes of stderr. The beat goes into the failures list. The script continues to the next beat. At the end, failures go to stderr and exit code two is returned. The previous media slot is never overwritten — atomic_json and os.replace keep it clean. Fix the composition, run again with --force --only BXX.

---

**B09 — VERDICT (17.46s)**
The verdict: remotion_scenes.py is the safe boundary between your beat sheet and Remotion. You get supersampled 4K output, audio-clock-matched clips, idempotent reruns, approval gates, and failure isolation — none of which npx remotion render gives you on its own. Run it before compile.py, never after.

---

**B11 — OUTRO (6.0s, silence)**
Brutalist Utility: remotion_scenes.py. Liam, in for Bear.
