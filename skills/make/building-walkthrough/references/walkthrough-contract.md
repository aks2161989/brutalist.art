# `walkthrough.json` and `route.json` — the contract the gate reads

## Executive summary

**What this is.** The two JSON files that describe a walkthrough film, and exactly what
`./art building-walkthrough --check` tests in them.

**Why read it.** The gate fails on contract problems that a viewer would feel (a shot with no job,
a line that cannot be spoken in its shot, a light that changed for no reason) and on things the
film would otherwise hide (a model that is not what the narration implies). Knowing the fields
saves a failed build.

**What it cannot do.** It cannot tell you whether the route is understandable, whether a frame is
beautiful, or whether the model is right. Those need frames, a person who has not seen the model,
and the sources. The example below is **not evidence**: replace every number, hash and sentence.

## `route.json` — geometry (read by `camera_rig.py` and `route_check.py`)

```json
{
  "schema_version": 1,
  "fps": 24,
  "defaults": {"lens_mm": 28, "sensor_mm": 36, "clip_start_m": 0.05, "ease": "linear"},
  "limits": {"max_speed_mps": 1.2},
  "shots": [
    {"id": "S01", "type": "walk", "frames": [1, 360], "ease": "linear",
     "waypoints": [[1.8, -7.0, 1.6], [1.8, -4.0, 1.6], [0.0, 0.5, 1.6], [0.0, 6.5, 1.6]],
     "look": {"mode": "travel", "yaw_deg": 0, "pitch_deg": 0}},
    {"id": "S02", "type": "still", "frames": [361, 456], "position": [0, 6.0, 1.6],
     "look": {"mode": "target", "point": [0, -6.0, 1.2]}},
    {"id": "S03", "type": "orbit", "frames": [457, 936], "center": [0, -4, 0],
     "radius_m": 3.0, "height_m": 1.4, "degrees": 360, "look_height_m": 0.9}
  ]
}
```

- Units are metres; world axes, Z up. Shot frame ranges are inclusive and must not overlap.
- `type`: `walk` (eye height enforced), `still` (must not move), `aerial`, `crane`, `orbit`
  (eye height not enforced; higher speed limits). Per-shot `limits` override defaults:
  `eye_height_m`, `eye_height_tol_m`, `max_speed_mps`, `max_yaw_dps`, `roll_tol_deg`,
  `pitch_warn_deg`, `min_clearance_m`, `max_accel_mps2`, `still_tol_m`.
- `ease`: `linear`, `in_out`, `in`, `out`. Use `linear` for a shot that cuts on motion; ease only
  a shot that starts or ends at rest.
- `look.mode`: `travel` (face the way you are going; `yaw_deg`/`pitch_deg` offsets), `target`
  (a fixed point), `path` (a point riding its own path; `waypoints`).
- Optional per shot: `lens_mm`, `shift_x`, `shift_y`, `smooth` (false for a polyline path),
  `dof` `{ "enabled": true, "focus_point": [x,y,z], "fstop": 4.0 }`.

## `walkthrough.json` — editorial (read by `verify_walkthrough.py`)

```json
{
  "schema_version": 1,
  "mode": "building",
  "title": "Walking the west end of the model",
  "model": {"name": "west-end", "path": "/abs/path/model.blend", "sha256": "<64 hex>",
            "blender": "5.1.2", "status": "interpretive", "card": "MODEL-CARD.md"},
  "brief": {"idea": "one sentence", "audience": "...", "variant": "a quiet weekday, midday",
            "viewer_height_m": 1.6},
  "disclosure": {"shot": "S01", "text": "what kind of model this is and what it does not show"},
  "departures": [{"id": "X1", "what": "interior modelled in one colour",
                  "effect": "colour is not evidence here", "disclosed_in": "S01"}],
  "looks": {"L1": {"name": "overcast noon", "time": "12:00", "note": "soft, no hard shadows"}},
  "route": {"file": "route.json", "report": "route_report.json"},
  "shots": [
    {"id": "S01", "section": "entrance", "purpose": "orientation", "framing": "wide",
     "look": "L1", "reveals": "the doorway is the only way through",
     "narration": {"source": "model", "line": "One doorway joins the two rooms.",
                   "evidence": "survey.geometry.size"}},
    {"id": "S02", "section": "main", "purpose": "scale", "framing": "medium", "look": "L1",
     "reveals": "the room is eight metres wide",
     "scale_reference": {"kind": "human", "size_m": 1.8}},
    {"id": "S03", "section": "closing", "purpose": "connection", "framing": "wide", "look": "L1",
     "reveals": "the second room is a dead end",
     "narration": {"source": "world", "line": "...", "fact": "F01"}}
  ],
  "budget": {"engine": "CYCLES", "samples": 128, "resolution": [3840, 2160], "where": "mac",
             "samples_measured": [{"kind": "interior", "sec_per_frame": 80},
                                  {"kind": "exterior", "sec_per_frame": 55},
                                  {"kind": "detail", "sec_per_frame": 120}]},
  "renders": {"dir": "renders", "format": "PNG"},
  "checks": {"orientation_test": "pending", "promise_check": "pending"}
}
```

- `mode`: `building`, `environment` (a game level seen as a model, not running), `asset`.
  Sections: building/environment `site, approach, entrance, main, connected, closing` (+ `detail`
  anywhere); asset `establish, silhouette, scale, material, topology, closing` (+ `detail`).
- `model.status`: `measured` (built from measurements, with a controls file), `interpretive`,
  `stylized`, `invented`. `model.path` is absolute; the gate re-hashes the file.
- `purpose`: `orientation, scale, connection, material, atmosphere, feature`.
  `framing`: `wide, medium, close`.
- `narration.source`: `model` (needs `evidence`), `world` (needs `fact`, a verified row in the
  reel's `FACTCHECK.md`), `none`.

## What the gate checks

| Area | Fails when | Warns when |
|---|---|---|
| Model | hash is not 64 hex, status unknown, card missing, **file changed since the film was laid out** | model file not on this machine |
| Brief | idea, audience, variant empty; viewer height outside 0.2–2.5 m | idea over 40 words |
| Route | `route.json` or its report missing; report measured a different `route.json` or model; any route failure; a shot not measured; shot ids differ between files | route warnings (acceleration, pitch, depth of field) |
| Sections | unknown section; the route doubles back; required section missing; `closing` not last; asset not opening on `establish` | recommended section missing |
| Shots | no `reveals`; bad purpose or framing; moving shot under 3 s, still under 1.5 s, orbit under 8 s; scale shot with no reference | moving shot under 6 s; one shot over 30 s without `hold_reason`; four equal framings in a row; repeated `reveals`; average shot under 3 s |
| Light | a shot's look is undeclared; look changes inside a section with no `look_change.reason` | look changes between sections with no reason |
| Narration | source or evidence missing; fact not verified or unsourced in `FACTCHECK.md`; line cannot be spoken inside its shot; a number or total for the film ("part 2", "3 of 5") | evaluative adjective; line over 40 words; over 2.2 words a second overall |
| Disclosure | not in the first two shots; under a sentence; a departure not disclosed in a real shot | interpretive model with no departures listed |
| Budget | (`--final`) fewer than three timed frames of two kinds; resolution malformed | (`--final` off) the same; a render over 8 h estimated on the Mac |
| Renders | (`--renders`, `--final`) a shot's frame count wrong, or gaps in the numbering | a still shot's frames flicker (> 1/255 mean difference) |
| Human tests | (`--final`, `--require-human-tests`) either still pending; a "done" with no name and date | pending: "not audience-tested" |

```bash
./brutalist.art/art building-walkthrough --check REEL/walkthrough.json
./brutalist.art/art building-walkthrough --check REEL/walkthrough.json --final
```
