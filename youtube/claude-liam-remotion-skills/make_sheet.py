#!/usr/bin/env python3
"""make_sheet.py — claude-liam-remotion-skills: a deep explainer of the Remotion agent skills installed into
brutalist.art on 2026-10-10 (remotion-dev/skills v4.0.534). Every body beat SHOWS a rule or capability the
skills teach, rendered for real in this toolkit's Remotion project (4.0.534). Liam, Kokoro am_onyx."""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "What the Remotion Skills Do"
FPS = 30


def remotion(bid, act, narration, pattern, props, show, gate="SHOW", lane="remotion", **extra):
    b = {"beat_id": bid, "act": act, "lane": lane, "proof_gate": gate, "narration_text": narration,
         "estimated_duration_s": round(len(narration.split()) / 2.5, 1), "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show, "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


def shell(bid, act, narration, lines, show, start=20, gap=40, title="zsh — brutalist.art/runtime/remotion"):
    return remotion(bid, act, narration, "CCPlainShell", {"title": title, "lines": lines, "startCue": start, "lineGap": gap}, show,
                    motion_claim="Real commands and their real output land in order.")


def demo(bid, act, narration, kind, show, **props):
    return remotion(bid, act, narration, "SkillDemo", {"kind": kind, **props}, show,
                    motion_claim="A live Remotion composition demonstrates the rule.")


def capture(bid, act, narration, url, image, caption, moves, show):
    return remotion(bid, act, narration, "BrowserCapture", {"url": url, "image": image, "caption": caption, "moves": moves, "imageAspect": 16 / 9}, show,
                    motion_claim="The real documentation page, camera pushing to the part named.",
                    qc={"sparse_by_design": True, "sparse_reason": "A real page capture in a browser window; the ring marks the spoken part."})


A = ["I · What A Skill Is", "II · The Markup Rules, Shown", "III · Media And Render", "IV · What The Upgrade Unlocked", "V · Keeping It Current"]
ASK = ("Hey Claude. I just installed Remotion's own agent skills into the brutalist toolkit. What do they actually do, "
       "and what do they let the toolkit do that it couldn't before?")

OPEN = [
 remotion("B00", "cold open", ASK, "ClaudeComposerAsk",
    {"command": ASK, "topic": "BRUTALIST · REMOTION SKILLS", "segment": TITLE, "greeting": "The ask,", "runningText": "composer prompt",
     "folderLabel": "@NikBearBrown", "modelLabel": "Fable 5.1", "effortLabel": "High"},
    [{"at": 0.0, "event": "the ask types"}, {"at": 0.85, "event": "sent"}], lane="bookend"),
 remotion("B01", "the idea",
    "Sawubona. This is Liam, in for Bear. First, a correction. These skills are not a plugin that renders anything. They are "
    "fifty short rule files that load into an agent, mine included, when it writes Remotion code, so the code it writes is the "
    "current, correct way: frame-driven motion, timing on the node, premounted media, measured text, captions as data. This film "
    "shows each rule running for real in the brutalist toolkit, and then the three things that needed a newer Remotion, now rendered live.",
    "BrutalistHesitantWriter",
    {"text": "The skills are\na rendering plugin", "triggerWords": "a rendering plugin", "replacementWords": "rules an agent reads",
     "fontSize": 72, "charMs": 55, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20, "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types the assumption"}, {"at": 0.3, "event": "corrects it"}], lane="bookend", lead_silence_s=0.8,
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
]

B = [
 # I
 shell("B10", A[0],
    "What a skill is. One command inside the Remotion project installs them: seven folders under dot agents slash skills, and a "
    "symlink from dot claude slash skills so Claude Code finds them. A lockfile records the exact version, so an update never "
    "changes the rules halfway through a film.",
    ["$ npx remotion skills add", "$ ls .agents/skills", "remotion-best-practices  remotion-captions  remotion-docs",
     "remotion-markup  remotion-multimedia  remotion-render", "remotion-upgrade", "$ ls -l .claude/skills | head -3",
     "remotion-captions -> ../../.agents/skills/remotion-captions", "remotion-docs -> ../../.agents/skills/remotion-docs",
     "$ head -4 skills-lock.json", "{", "  \"version\": 1,", "  \"skills\": {", "    \"remotion-best-practices\": {"],
    [{"at": 0.1, "event": "install"}, {"at": 0.35, "event": "seven folders"}, {"at": 0.6, "event": "symlink"}, {"at": 0.85, "event": "lockfile"}], start=20, gap=30),
 shell("B11", A[0],
    "Open one. A skill is a markdown file with a name, a version, and rules. The markup skill opens with the two that matter most: "
    "take the frame rate from the video config and keep timing on the J S X node, and drive every animation from the current frame. "
    "A C S S transition will not render. The router skill sends an agent to the right file for the task.",
    ["$ head -20 .agents/skills/remotion-markup/SKILL.md", "---", "name: remotion-markup", "description: Content, animation and effects best practices",
     "version: 4.0.534", "---", "## General rules", "Inside a composition or scene component, get `fps` from",
     "`useVideoConfig()` for all seconds-to-frames calculations …", "Drive animations using `useCurrentFrame()` and `interpolate()`.",
     "CSS `transition` or `animation` will not render correctly …"],
    [{"at": 0.1, "event": "the file"}, {"at": 0.45, "event": "fps from config"}, {"at": 0.7, "event": "current frame"}], start=20, gap=30),
 # II
 demo("B20", A[1],
    "The first rule, shown. Two boxes are told to slide across the stage. The left one uses a C S S transition. The right one uses "
    "interpolate over the current frame. Remotion renders one frame at a time, as a screenshot, so a C S S transition never gets its "
    "two seconds: the left box teleports to the end in a single frame and sits there. The right box moves, and lands in the same "
    "place in every render. That is the whole reason for the rule.",
    "frameDriven", [{"at": 0.2, "event": "both boxes told to move"}, {"at": 0.5, "event": "left frozen, right moving"}]),
 demo("B21", A[1],
    "Easing. Four dots travel the same distance in the same time. Linear is mechanical. The bezier the skills recommend, point one "
    "six, one, point three, one, arrives fast and settles. A spring with heavy damping pushes with no bounce. And the last pair "
    "shows scale: the same growth looks slow at the end unless you ask for perceptual scale, which the skills now call out.",
    "easing", [{"at": 0.1, "event": "four dots set off"}, {"at": 0.6, "event": "scale pair"}]),
 demo("B22", A[1],
    "Sequencing. A series lays clips end to end, and the skills say: premount every timed item one second early, with premount "
    "for equal to the frame rate, so media and fonts are ready before the cut. Watch the ruler: the grey band before each clip "
    "is the premount, the playhead crosses it, and the clip is already there when its turn comes.",
    "sequence", [{"at": 0.15, "event": "three clips on a ruler"}, {"at": 0.5, "event": "premount bands"}]),
 demo("B23", A[1],
    "Transitions. The transitions package gives a transition series with fade, slide and wipe between scenes, and the skills "
    "explain the trap: a transition overlaps its neighbours, so the composition is shorter than the sum of its scenes, and you "
    "subtract the overlap when you compute the length. Three cards, three cuts, and the running frame count shows the overlap.",
    "transitions", [{"at": 0.25, "event": "fade"}, {"at": 0.5, "event": "slide"}, {"at": 0.75, "event": "wipe"}]),
 demo("B24", A[1],
    "Measuring text. The layout utilities measure a string in its real font before it is placed. The left box sets a long title "
    "at one size and clips it. The right box asks fit text for the largest size that fits the width, and shows the size it found. "
    "For this toolkit that is the difference between catching a truncated title in a gate and never producing one.",
    "fitText", [{"at": 0.2, "event": "left clips"}, {"at": 0.55, "event": "right fits, size shown"}]),
 demo("B25", A[1],
    "Captions as data. The captions package parses a subtitle file into caption objects with start and end times in milliseconds. "
    "This is a real caption file, from the first film in the Northeastern research computing series, and these are its first "
    "cues, drawn as pages, each word lighting on its own time. The toolkit already writes these files; now a composition can read them.",
    "captions", [{"at": 0.15, "event": "the srt parses"}, {"at": 0.4, "event": "cues page"}]),
 demo("B26", A[1],
    "Audio visualization. The media utilities read the waveform of an audio file and give a spectrum per frame. These bars are "
    "this sentence: my own narration, analysed as it plays, nothing faked. Bass on the left, treble on the right, and the shape "
    "follows the voice.",
    "audioViz", [{"at": 0.1, "event": "bars follow the voice"}]),
 # III
 shell("B30", A[2],
    "Media. The multimedia skill reads a file's duration with the media bunny library instead of shelling out to F F probe. Here it "
    "measures the opening card of that same research computing film: twelve point five two eight seconds, where F F probe says "
    "twelve point four eight, the gap being how each counts the last M P three frame. The toolkit's clock stays in Python, but a "
    "composition can now size itself from the audio it plays.",
    ["$ node get-audio-duration.mjs ../../hpc/.../mp3/beat-BOPEN.mp3", "12.528", "$ ffprobe -v error -show_entries format=duration \\",
     "    -of csv=p=0 ../../hpc/.../mp3/beat-BOPEN.mp3", "12.480000"],
    [{"at": 0.3, "event": "mediabunny"}, {"at": 0.7, "event": "ffprobe"}], start=30, gap=56),
 shell("B31", A[2],
    "Render. The render skill is the command line: render, still, and a frames mode that writes several frames as images in one "
    "call, which is exactly how this toolkit's gates sample a beat. It also documents transparent output: P N G frames, an alpha "
    "pixel format, Pro Res four four four four or V P nine, for a clip that drops onto another video with no background.",
    ["$ npx remotion render Root.tsx SkillDemo out.mp4 \\", "    --scale=2 --image-format=png", "$ npx remotion still Root.tsx SkillDemo frame.png --frame=45",
     "$ npx remotion render Root.tsx SkillDemo out/ \\", "    --frames=10,45,80 --image-format=png",
     "$ npx remotion render Root.tsx Logo out.mov --image-format=png \\", "    --pixel-format=yuva444p10le --codec=prores \\", "    --prores-profile=4444"],
    [{"at": 0.15, "event": "render"}, {"at": 0.4, "event": "frames"}, {"at": 0.7, "event": "transparent"}], start=20, gap=52),
 demo("B32", A[2],
    "And the toolkit already renders every card this way: the writing quill from the previous film, rendered as a still with alpha, "
    "sits on a kraft checkerboard with nothing behind it. That is the same render path, with the flags the skill names.",
    "transparent", [{"at": 0.2, "event": "the alpha still lands on the checker"}]),
 # IV
 shell("B39", A[3],
    "Now the part that needed the upgrade. Three of the rules describe features newer than the Remotion this toolkit was running. So "
    "the toolkit moved from four point oh point four eight six to the latest, four point oh point five three four, every Remotion "
    "package at once, as the upgrade skill says. React went to nineteen with it, because the new transitions build carries React "
    "nineteen inside. Then every composition was re-rendered, and the effects, highlights and blur below are real renders, not captures.",
    ["$ node -p \"require('remotion/package.json').version\"", "4.0.534", "$ npm ls --depth=0 | grep -E 'react@|effects|rough|blur'",
     "+-- @remotion/effects@4.0.534", "+-- @remotion/motion-blur@4.0.534", "+-- @remotion/rough-notation@4.0.534", "+-- react@19.3.0"],
    [{"at": 0.15, "event": "version"}, {"at": 0.5, "event": "packages"}, {"at": 0.85, "event": "react"}], start=20, gap=50),
 demo("B40", A[3],
    "First, effects: an effects array on images, video and solids, drawn by the graphics card. Here is one portrait of Professor Bear, four "
    "ways: grayscale, duotone in the toolkit's own ink and kraft, a terracotta halftone, and a vignette with roughened edges. Each is one "
    "line, driven by the frame, and the documentary still treatment the toolkit used to build by hand is now exactly that.",
    "effects", [{"at": 0.1, "event": "four treatments on one portrait"}, {"at": 0.8, "event": "they settle"}], durationSeconds=12),
 demo("B41", A[3],
    "Second, text highlights: hand-drawn circles, highlights, underlines, strike-throughs and boxes, each a component driven by a "
    "progress value from the frame. The terracotta ring this toolkit used to draw by hand in every scene is now a Circle around a word.",
    "highlights", [{"at": 0.1, "event": "circle draws"}, {"at": 0.4, "event": "highlight"}, {"at": 0.8, "event": "box"}], durationSeconds=12),
 demo("B42", A[3],
    "Third, motion blur. The top card is a hard-edged move, every frame sharp. The bottom is wrapped in camera motion blur, which renders "
    "each frame at twelve moments inside a two-hundred-and-forty-degree shutter and averages them, so the card smears the way a real "
    "camera sees it. The newer H T M L in canvas blur needs a Chrome flag, so this is the component that runs everywhere.",
    "motionBlur", [{"at": 0.1, "event": "sharp card"}, {"at": 0.15, "event": "blurred card"}], durationSeconds=10),
 # V
 shell("B50", A[4],
    "Keeping it current. The skills come from a public repository, and one command pulls updates. The lockfile changes with them, "
    "so the update is a diff you can read before the next film, and a commit you can roll back. The old snapshot in the "
    "toolkit's docs folder now points at the live set.",
    ["$ npx remotion skills update", "$ git diff --stat skills-lock.json", " skills-lock.json | 14 ++++++-------",
     "$ cat docs/remotion-best-practices/README.md | head -2", "# Superseded — the live Remotion skills are installed, not copied"],
    [{"at": 0.15, "event": "update"}, {"at": 0.45, "event": "diff"}, {"at": 0.8, "event": "superseded"}], start=20, gap=56,
    title="zsh — brutalist.art"),
]

RECAP = ["The skills are rule files an agent reads while writing Remotion code, not a renderer.",
         "Frame-driven motion, timing on the node, premount one second, measure text first.",
         "Installed at a pinned version; transitions, layout-utils, captions, media-utils added to match.",
         "Captions and audio become data a composition can read; the toolkit's clock stays in Python.",
         "Remotion went from 4.0.486 to 4.0.534, React to 19; effects, highlights and blur now render live.",
         "Update is a command and a diff; the old docs snapshot is superseded."]
VERDICT = remotion("BVDT", "recap",
    "Let's recap with Claude. The skills are rule files an agent reads while it writes Remotion code, not a renderer. The rules "
    "that matter: frame-driven motion, timing on the node, premount a second early, measure text before placing it. They are "
    "installed at a pinned version, with transitions, layout utilities, captions and media utilities added to match. Captions and "
    "audio become data a composition can read, while the toolkit's clock stays in Python. The toolkit then upgraded to the latest "
    "Remotion, with React nineteen, and effects, text highlights and motion blur now render live. And an update is a command and a diff.",
    "ClaudeVerdictArtifact", {"artifactTitle": "Recap", "artifactHeading": TITLE, "artifactLines": RECAP},
    [{"at": 0.0, "event": "artifact page opens"}, {"at": 0.1, "event": "six recap lines land"}],
    lane="bookend", lead_silence_s=0.5, qc={"sparse_by_design": True, "sparse_reason": "Mandated ClaudeVerdictArtifact bookend."})

YT = ("In my Remotion project, read the installed remotion-markup skill and audit this component: [paste one component]. List every "
      "place it breaks a rule, such as CSS transitions, transform strings, missing premountFor, timing not derived from fps, or "
      "unmeasured text, and rewrite only those lines.")
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + YT + " Then check two things yourself. Render three frames with the frames flag and look at "
    "them: does anything still animate by C S S? And did it change only the lines it named?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE · YOUR TURN", "segment": "Audit One Component Against The Skills", "command": YT,
     "runningText": "paste this into Claude…",
     "output": ["Check: render three frames with --frames and look; nothing animates by CSS.", "Check: it changed only the lines it named."],
     "folderLabel": "@NikBearBrown", "modelLabel": "Fable 5.1", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}],
    lane="bookend")
OUTRO = {"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW", "narration_text": f"{TITLE}. At Nik Bear Brown.",
         "estimated_duration_s": 4.0, "voice": "am_onyx", "engine": "kokoro", "kind": "outro_voice", "tail_silence_s": 1.0,
         "shot": {"type": "REMOTION", "source": "own", "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
                  "remotion": {"pattern": "ClaudeTitleOutro", "props": {"title": TITLE, "slug": SLUG, "handle": "@NikBearBrown", "subline": ""}}}}

BEATS = OPEN + B + [VERDICT, YOURTURN, OUTRO]
sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "BRUTALIST · REMOTION SKILLS", "skill": "deep-explainer", "style_preset": "claude",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "Zulu (Sawubona)",
    "audience": "Bear and toolkit users: what the installed Remotion agent skills do, shown running",
    "source_doc": "github.com/remotion-dev/skills v4.0.534, installed 2026-10-10 into brutalist.art/runtime/remotion/.agents/skills; the rules demonstrated in this toolkit's own Remotion 4.0.534 project",
    "playlist": "Claude", "chapter_number": 0,
    "tags": ["Remotion", "agent skills", "brutalist.art", "Claude Code", "video toolkit", "Nik Bear Brown"]},
    "beats": BEATS}
old = {}
p = HERE / "beat_sheet.json"
if p.exists():
    for ob in json.load(open(p))["beats"]:
        old[ob["beat_id"]] = ob
for b in BEATS:
    ob = old.get(b["beat_id"])
    if ob and ob.get("narration_text") == b["narration_text"]:
        for k in ("actual_duration_s", "audio_file"):
            if k in ob:
                b[k] = ob[k]
    dur = b.get("actual_duration_s"); props = (b["shot"].get("remotion") or {}).get("props")
    if dur and props is not None and b["shot"]["remotion"]["pattern"] in ("BrowserCapture", "CCPlainShell", "SkillDemo", "ClaudeCodeBeat"):
        props["durationSeconds"] = dur
p.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(len(BEATS), "beats; est", round(sum(b.get("actual_duration_s") or b["estimated_duration_s"] for b in BEATS)), "s")
for b in BEATS:
    r = b["shot"].get("remotion") or {}
    if r.get("pattern") == "CCPlainShell":
        long = [l for l in r["props"]["lines"] if len(l) > 66]
        if len(r["props"]["lines"]) > 14 or long: print("WARN", b["beat_id"], long)
