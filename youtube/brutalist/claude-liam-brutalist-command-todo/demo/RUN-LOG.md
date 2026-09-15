# RUN-LOG — demonstration transcripts for the todo command reel

Captured live on this workstation. Verbatim stdout / stderr. All commands run from the isolated toolkit copy at `.repoloop/workspaces/claude-liam-brutalist-command-todo/toolkit`.

## 1) `./art todo demo/example-reel` — baseline
```text
$ ./art todo demo/example-reel
[todo] example-reel: 0/5 filled → todo.json + STATUS.md + ToDo.md
    B00  needs-fill remotion          pipeline media/B00.mp4
    B01  needs-fill manim             pipeline manim/B01.mp4
    B02  needs-fill historical-image  human    media/B02.png (or .mp4)  · prompt: find: The 1963 chart of energy demand, then and now.
    B03  needs-fill user-capture      human    media/B03.mp4
    B04  needs-fill ai-video-prompt   human    media/B04.mp4  · prompt: A short generated clip: a slow zoom on a paper diagram.
```

## 2) `./art todo demo/example-reel --method manim --open` — filter
```text
$ ./art todo demo/example-reel --method manim --open
[todo] example-reel: 0/5 filled → todo.json + STATUS.md + ToDo.md
    B01  needs-fill manim             pipeline manim/B01.mp4
```

## 3) `./art todo demo/example-reel --json` — machine-readable
```json
{
  "video": "example-reel",
  "metadata": {
    "title": "Demo reel for the todo ledger",
    "slug": "todo-demo-reel",
    "voice_kokoro": "am_onyx",
    "engine": "kokoro"
  },
  "source_of_truth": "beat_sheet.json \u2014 edit the sheet, not this file",
  "beats_total": 5,
  "beats_open": 5,
  "beats": [
    {
      "beat_id": "B00",
      "status": "needs-fill",
      "on_disk": null,
      "method": "remotion",
      "who": "pipeline",
      "scene_hint": null,
      "prompt": null,
      "slot": "media/B00.mp4",
      "label": "Cold open \u2014 the composer with the ask."
    },
    {
      "beat_id": "B01",
      "status": "needs-fill",
      "on_disk": null,
      "method": "manim",
      "who": "pipeline",
      "scene_hint": "animated_graphics",
      "prompt": null,
      "slot": "manim/B01.mp4",
      "label": "A worked example of a diffusion equation, in one breath."
    },
    {
      "beat_id": "B02",
      "status": "needs-fill",
      "on_disk": null,
      "method": "historical-image",
      "who": "human",
      "scene_hint": null,
      "prompt": "find: The 1963 chart of energy demand, then and now.",
      "slot": "media/B02.png (or .mp4)",
      "label": "The 1963 chart of energy demand, then and now."
    },
    {
      "beat_id": "B03",
      "status": "needs-fill",
      "on_disk": null,
      "method": "user-capture",
      "who": "human",
      "scene_hint": null,
      "prompt": null,
      "slot": "media/B03.mp4",
      "label": "The desk-shot of the notebook \u2014 a five-second insert."
    },
    {
      "beat_id": "B04",
      "status": "needs-fill",
      "on_disk": null,
      "method": "ai-video-prompt",
      "who": "human",
      "scene_hint": null,
      "prompt": "A short generated clip: a slow zoom on a paper diagram.",
      "slot": "media/B04.mp4",
      "label": "A short generated clip: a slow zoom on a paper diagram."
    }
  ]
}
```

## 4) `./art todo demo/empty-reel` — failure + recovery
```text
$ ./art todo demo/empty-reel
[todo] no beat_sheet.json in /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/youtube/brutalist/claude-liam-brutalist-command-todo/demo/empty-reel
exit=1
```

## 5) No arguments — usage line
```text
$ ./art todo
usage: todo.py [-h] [--method METHOD] [--open] [--json] reel
todo.py: error: the following arguments are required: reel
exit=2
```
