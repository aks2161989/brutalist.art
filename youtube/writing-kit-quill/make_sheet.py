#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for writing-kit-quill: the toolkit meta-series film that shows the
writing quill set (six icons, QuillWriter's four kinds, the Manim writing kit). Liam, Kokoro am_onyx."""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "The Writing Quill"
SPARSE = "show-tell: one drawn object on a cream stage, a label or two; the voice explains. Only underfill and clustered are waived."


def beat(bid, narration, pattern=None, props=None, cls=None, show=None, lane="remotion", gate="SHOW", sparse=True, **extra):
    b = {"beat_id": bid, "act": "writing kit", "lane": lane, "proof_gate": gate, "narration_text": narration,
         "estimated_duration_s": round(len(narration.split()) / 2.5, 1), "voice": "am_onyx", "engine": "kokoro"}
    if cls:
        b["shot"] = {"type": "GRAPHIC", "source": "own", "visual_intent": extra.pop("intent"), "show": show or [], "manim": {"class": cls}}
        b["lane"] = "manim"
    else:
        b["shot"] = {"type": "REMOTION", "source": "own", "show": show or [], "remotion": {"pattern": pattern, "props": props}}
    if sparse:
        b["qc"] = {"sparse_by_design": True, "sparse_reason": SPARSE}
    b.update(extra)
    return b


YT = ("Add one writing beat to my explainer: the moment where [who] drafts [what]. Pick the best of the Brutalist writing kit for it, "
      "the QuillWriter pages, scroll, page or spinner card, or the Manim quill with write_lines, and write the beat's narration and "
      "the exact props or scene code.")

BEATS = [
 beat("BIDEA",
    "Hej. This is Liam, in for Bear. A new set in the Brutalist toolkit: the writing quill. It began as the little spinner in "
    "the Claude app, the terracotta quill that turns while Claude writes. Now it is six icons, four Remotion animations, and a "
    "Manim writing kit. Here is each one.",
    "BrutalistHesitantWriter",
    {"text": "Just a loading\nspinner", "triggerWords": "loading spinner", "replacementWords": "quill that writes", "fontSize": 78,
     "charMs": 50, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20, "seed": SLUG, "banner": ""},
    show=[{"at": 0.0, "event": "types the assumption"}, {"at": 0.3, "event": "corrects it"}], lane="bookend", lead_silence_s=0.8),
 beat("BDEFS",
    "Six terms. A quill: the drawn feather pen, nib first. An inkwell: the dark bottle with one terracotta drop. A scribble: a "
    "wavy stroke that reads as handwriting, never as type. An outline: a branching tree from one trunk, a terracotta dot at every "
    "tip. A spinner: the app's writing mark, a terracotta quill looping one stroke. And the writing kit: all of it, in Manim and "
    "in Remotion.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "quill", "meaning": "the drawn feather pen, nib first"},
               {"term": "inkwell", "meaning": "the dark bottle with one terracotta drop"},
               {"term": "scribble", "meaning": "a wavy stroke that reads as handwriting, never as type"},
               {"term": "outline", "meaning": "a branching tree from one trunk, a dot at every tip"},
               {"term": "spinner", "meaning": "the app's writing mark: a terracotta quill looping one stroke"},
               {"term": "writing kit", "meaning": "all of it, in Manim and in Remotion"}],
     "folderLabel": "@NikBearBrown"},
    show=[{"at": 0.08, "event": "quill"}, {"at": 0.25, "event": "inkwell"}, {"at": 0.4, "event": "scribble"}, {"at": 0.58, "event": "outline"}, {"at": 0.72, "event": "spinner"}, {"at": 0.87, "event": "writing kit"}],
    gate="CARD", lane="bookend"),
 beat("B00",
    "The icons first. Six originals drawn in the house line, twenty-four by twenty-four, stroke two: a quill, an inkwell, a quill "
    "on a scroll, a quill with pages, and two more, a plain scroll and a scribbled page. They sit in the canonical set, so art "
    "icons quill finds them, and they drop straight onto an icon row.",
    "LibraryIconRow",
    {"title": "Six Original Icons",
     "items": [{"label": "quill", "icon": "quill", "cue_phrase": "a quill,", "mono": True},
               {"label": "inkwell", "icon": "inkwell", "cue_phrase": "an inkwell", "mono": True},
               {"label": "quill-scroll", "icon": "quill-scroll", "cue_phrase": "on a scroll", "mono": True},
               {"label": "quill-pages", "icon": "quill-pages", "cue_phrase": "with pages", "mono": True}]},
    show=[{"at": 0.3, "event": "quill"}, {"at": 0.4, "event": "inkwell"}, {"at": 0.5, "event": "quill-scroll"}, {"at": 0.6, "event": "quill-pages"}]),
 beat("B01",
    "The spinner itself. A terracotta quill writes one short stroke, lifts, and starts again, every one point six seconds, with "
    "a status word beside it. Use it when the point is that the model is writing.",
    "QuillWriter", {"kind": "spinner", "status": "Writing…"},
    show=[{"at": 0.1, "event": "the quill loops"}]),
 beat("B02",
    "Pages. Three scattered sheets, and the quill writes each one line by line, the nib riding the stroke. Scribbles, not "
    "letters, so the type gate has nothing to read, and the voice says what is being written.",
    "QuillWriter", {"kind": "pages", "title": "Pages", "lines": 5, "caption": "three sheets, one quill"},
    show=[{"at": 0.1, "event": "pages land"}, {"at": 0.3, "event": "writing"}]),
 beat("B03",
    "The scroll. It unrolls, then the quill draws an outline: one trunk, two forks, a terracotta dot at every tip. The reference "
    "drawing, as a motion.",
    "QuillWriter", {"kind": "scroll", "title": "Scroll", "levels": 2},
    show=[{"at": 0.1, "event": "unrolls"}, {"at": 0.3, "event": "the outline grows"}]),
 beat("B04",
    "One page. The draft grows down the sheet, eight lines, the quill always at the last stroke. Good for a long beat where "
    "something is being written while the voice explains.",
    "QuillWriter", {"kind": "page", "lines": 8, "caption": "a draft grows"},
    show=[{"at": 0.1, "event": "the page"}, {"at": 0.3, "event": "lines grow"}]),
 beat("B05",
    "And in Manim, the same objects as drawn primitives in the show-tell kit: paper, quill, scribbles on, and write lines, "
    "which hops the nib to each stroke and rides it as it draws. It paces to the narration like every other kit scene.",
    cls="B05_PagesWriting", intent="Three tilted paper() sheets land; a quill() writes scribbles_on() each in turn via write_lines(); mono labels name the helpers as they are spoken.",
    show=[{"at": 0.1, "event": "paper"}, {"at": 0.25, "event": "quill"}, {"at": 0.45, "event": "write lines"}]),
 beat("B06",
    "The outline tree and the inkwell, in the isometric kit: grow tree draws each branch with the quill and lands the "
    "terracotta tips last. Six icons, four cards, two Manim rigs. One quill.",
    cls="B06_ScrollOutline", intent="A paper() sheet, an inkwell() on the iso grid, a quill(); grow_tree() draws an outline_tree() branch by branch, dots last; the count '6 · 4 · 2' lands as ink numerals.",
    show=[{"at": 0.1, "event": "inkwell"}, {"at": 0.3, "event": "grow tree"}, {"at": 0.85, "event": "6 · 4 · 2"}]),
 beat("BHTF",
    "Your turn. Paste this into Claude: " + YT + " Then check two things yourself. Is the stroke a scribble, never a word? "
    "And is terracotta only the drop, the tips, or the spinner?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE · YOUR TURN", "segment": "Add One Writing Beat", "command": YT,
     "runningText": "paste this into Claude…",
     "output": ["Check: the stroke is a scribble, never a word.", "Check: terracotta is only the drop, the tips, or the spinner."],
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    show=[{"at": 0.0, "event": "Composer opens"}, {"at": 0.1, "event": "the prompt types"}, {"at": 0.8, "event": "two checks"}], lane="bookend", sparse=False),
 {"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW", "narration_text": f"{TITLE}. At Nik Bear Brown.",
  "estimated_duration_s": 4.0, "voice": "am_onyx", "engine": "kokoro", "kind": "outro_voice", "tail_silence_s": 1.0,
  "shot": {"type": "REMOTION", "source": "own", "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
           "remotion": {"pattern": "ClaudeTitleOutro", "props": {"title": TITLE, "slug": SLUG, "handle": "@NikBearBrown", "subline": ""}}}},
]

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "BRUTALIST · WRITING KIT", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "Swedish (Hej)", "bookend_exempt": ["cold-open", "bvdt"],
    "audience": "Bear and toolkit users: what the writing quill set is and when to use each piece",
    "source_doc": "brutalist.art writing kit (icons/svg quill*, runtime/remotion/src/scenes/QuillWriter.tsx, skills/make/show-tell/templates/iso_kit.py), built 2026-10-07",
    "playlist": "Claude", "chapter_number": 0,
    "tags": ["brutalist.art", "writing", "quill", "Manim", "Remotion", "icons", "Nik Bear Brown"]},
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
    dur = b.get("actual_duration_s")
    props = (b["shot"].get("remotion") or {}).get("props")
    if dur and props is not None:
        pat = b["shot"]["remotion"]["pattern"]
        if pat in ("ClaudeDefinitions", "LibraryIconRow", "QuillWriter"):
            props["durationSeconds"] = dur
        if pat == "LibraryIconRow":
            n = b["narration_text"]
            for it in props["items"]:
                at = round(n.index(it["cue_phrase"]) / len(n), 3)
                it["at"] = at if not 0.43 <= at <= 0.57 else 0.58
p.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(len(BEATS), "beats; est", round(sum(b.get("actual_duration_s") or b["estimated_duration_s"] for b in BEATS)), "s")
