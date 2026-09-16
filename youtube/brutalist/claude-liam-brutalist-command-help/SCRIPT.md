# SCRIPT — Brutalist Command: art help

Persona: **Liam, in for Bear** — Kokoro `am_onyx` (free, local).
Playlist: **Brutalist**, adapted for `@HumanitariansAI` folder chip.
Total narration audio (measured): **~178.1s** before per-beat conform. Actual master duration: 177.0s.

Narration is the WORDS; SHOTLIST.md describes the VISUALS. No captions.

---

### B00 · ASK · ClaudeComposerAsk · ~17.1s
> Namaste, this is Liam, in for Bear. Every fellow in Brutalist has typed dot slash art help. What most people miss is that four different aliases hit that same line, and the help text you see is not stored anywhere. It is the file's own header, extracted by sed at run time. Here is what that means, and where it stops.

### B01 · BLUF · BrutalistHesitantWriter · ~9.7s
> Watch the writer walk this back. Art help does not list every skill. It prints every command, straight from the file's own header. The skills catalog is a different command.

### B02 · FRAMEWORK · ClaudeCodeBeat · ~15.5s
> The whole toolkit is one bash script called art. Inside is a single case statement — one branch per command. The very first branch matches four patterns with pipes between them: empty string, dash h, dash dash help, and the word help. All four aliases hit the same body.

### B03 · MECHANISM · ClaudeCodeBeat · ~14.8s
> This is the whole body. Two sed calls. The first grabs lines two through eighteen of the art file itself. The second strips the leading hash and space that make those lines a shell comment. What you see on your terminal is the file reading its own head, without the hash marks.

### B04 · WORKED_EXAMPLE · ClaudeCodeBeat · ~12.5s
> So this is what runs. Seventeen lines. The first line is a title. The other sixteen are commands, each with a short description. There are no colours, no pager, no interactive prompt. It prints, it exits zero, it is done.

### B05 · MECHANISM · ClaudeCodeBeat · ~15.7s
> The alias set is the interesting part. Bash pipes inside a case pattern mean this branch matches four different things. The empty string, so bare dot slash art matches. Dash h. Dash dash help. And the literal word help. All four hit the same sed line. Same output, no duplicated code.

### B06 · MECHANISM · ClaudeCodeBeat · ~15.0s
> Now the near miss. Dot slash art dash dash list is a different command. It is not an alias for help. It prints the skills table — every skill in the toolkit with a one-line role. If you want the commands, use help. If you want the skills, use dash dash list. They cover different scopes.

### B07 · FALSIFIABILITY · ClaudeCodeBeat · ~15.7s
> And here is what a wrong guess actually does. Dot slash art bogus does not print help. It falls through the case into the star branch and exits with status two. One line to standard error, pointing you at dash dash list. This is the recovery hint that keeps you from typing help six different ways.

### B08 · MECHANISM · ClaudeCodeBeat · ~19.0s
> The recovery is two commands. Dot slash art dash dash list shows every skill by name. Then dot slash art followed by the skill name and dash dash help opens that skill's SKILL dot m-d in your pager. So the arc is: help for commands, dash dash list for skills, skill dash dash help for a specific one. Three commands cover the whole surface.

### B09 · VERDICT · ClaudeVerdictArtifact · ~17.3s
> So the split. Art help is the 17-line command sheet, pulled from the file's own header. Dash dash list is the skills table. Skill dash dash help is that skill's SKILL dot m-d. An unknown token is exit two, one line, pointing at dash dash list. Four scopes, one dispatcher, zero surprises.

### B10 · YOUR_TURN · ClaudeComposerAsk · ~19.4s
> Your turn. Paste this into Claude Code from the brutalist toolkit root. Ask Claude to run each alias, capture the output, diff them line by line, then confirm the exit codes. What you should see is four identical outputs, four zero exit codes, and one unknown token that exits two. If any pair differs, you have found a bug — file it against the case block at art line 38.

### B11 · OUTRO · ClaudeTitleOutro · ~5.1s
> Brutalist Command: art help. Liam, in for Bear, for at Humanitarians A I.
