## beat-B00

Hey Claude, I just installed Remotions own agent skills into the Brutalist Toolkit. What do they actually do? And what do they let the Toolkit do that it couldn't before?

---

## beat-B01

Saoabona, this is Liam in for bear, first a correction. These skills are not a plugin that renders anything. They are 50 short rule files that load into an agent mine included when it writes emotion code so the code it writes is the current correct way. Frame-driven motion, timing on the node, permitted media, measured text, captions as data. This film shows each rule running for real in the brutalist toolkit. And then the three things that needed a newer emotion, now rendered live.

---

## beat-B10

What a skill is, one command inside the Remoshing project installs them, seven folders under .agents slash skills, and a Simlink from .clod slash skills so Claude code finds them. A lock file records the exact version so an update never changes the rules halfway through a film.

---

## beat-B11

Open 1, a skill is a markdown file with a name, a version, and rules. The markup skill opens with the two that matter most. Take the frame rate from the video config and keep timing on the JSX node and drive every animation from the current frame. A CSS transition will not render. The router skill sends an agent to the right file for the task.

---

## beat-B20

The first rule shown two boxes are told to slide across the stage. The left one uses a CSS transition. The right one uses interpolate over the current frame. Remote-shin renders one frame at a time as a screenshot, so a CSS transition never gets its two seconds. The left box teleport to the end in a single frame and sits there. The right box moves and lands in the same place in every render. That is the whole reason for the rule.

---

## beat-B21

Easing four dots travel the same distance in the same time, linear is mechanical. The bezier the skills recommend .16, 1.31 arrives fast in settles. A spring with heavy damping pushes with no bounce. In the last pair show scale, the same growth looks slow at the end unless you ask for perceptual scale, which the skills now call out.

---

## beat-B22

Sequencing a series lays clips end to end and the skills say, Promount every timed item one second early with Promount for equal to the frame rate so media and fonts are ready before the cut. Watch the ruler, the gray band before each clip is the Promount, the playhead crosses it, and the clip is already there when its turn comes.

---

## beat-B23

Transitions, the Transitions package gives a transition series with fade, slide, and white between scenes, and the skills explain the trap. A transition overlaps its neighbors, so the composition is shorter than the some of its scenes, and you subtract the overlap when you compute the length. Three cards, three cuts, and the running frame count shows the overlap.

---

## beat-B24

Measuring text, the layout utilities measure a string in its real font before it is placed. The left box sets a long title at one size and clips it. The right box asks fit text for the largest size that fits the width and shows the size it found. For this toolkit, that is the difference between catching a truncated title in a gate and never producing one.

---

## beat-B25

Captions as data, the captions package parses a subtitle file into caption objects with start and end times in milliseconds. This is a real caption file from the first film in the Northeastern Research Computing series, and these are its first cues drawn as pages each word lighting on its own time. The toolkit already writes these files, now a composition can read them.

---

## beat-B26

Audio visualization, the media utilities read the waveform of an audio file and give a spectrum per frame. These bars are this sentence, my own narration, analyzed as it plays nothing faked. This on the left treble on the right and the shape follows the voice.

---

## beat-B30

Media, the multimedia skill, reads a file's duration with the Media Bunny Library instead of shelling out to FF Probe. Here it measures the opening card of that same research computing film, 12.528 seconds, where FF Probe says 12.48, the gap being how each counts the last MP3 frame. The toolkits clock stays in Python, but a composition can now size itself from the audio at

---

## beat-B31

Render, the render skill is the command line. Render, still in a frames mode that writes several frames as images in one call, which is exactly how this tool gets gate sample of beat. It also documents transparent output, PNG frames and alpha pixel format, ProRes 4444 or VP9, for a clip that drops onto another video with no background.

---

## beat-B32

And the toolkit already renders every card this way. The writing quill from the previous film rendered as a still with alpha sits on a craft checkerboard with nothing behind it. That is the same render path with the flags the skill names.

---

## beat-B39

Now the part that needed the upgrade, three of the rules described features newer than the emotion this toolkit was running. So the toolkit moved from 4.0.486 to the latest, 4.0.534, every emotion package at once as the upgrade skill says. React went to 19 with it because the new transitions build carries React 19 inside, then every composition was re-rendered in the effects. Highlights and blur below are real renders, not captures.

---

## beat-B40

First effects and effects array on images, video and solids drawn by the graphics card. Here is one portrait of Professor Bear Four Ways, Grace Kale, Duton in the Toolkit's owning can craft, a terracotta half-tone and a vignette with roughened edges. Each is one line driven by the frame, and the documentary still treatment the tool kit used to build by hand is now exactly that.

---

## beat-B41

Second, text highlights, hand drawn circles, highlights, underlines, strike-throughs, and boxes, each a component driven by a progress value from the frame. The terracotta ring this toolkit used to draw by hand in every scene is now a circle around a word.

---

## beat-B42

Third motion blur, the top card is a hard-edged move every frame sharp. The bottom is wrapped in camera motion blur, which renders each frame at 12 moments inside a 240 degree shutter and averages them, so the card smears the way a real camera sees it. The newer HTML and canvas blur needs a chrome flag, so this is the component that runs everywhere.

---

## beat-B50

Keeping it current, the skills come from a public repository and one command pulls updates. The lock file changes with them, so the update is a diff you can read before the next film, and a commit you can roll back. The old snapshot in the Toolkit's Docs folder now points at the live set.

---

## beat-BHTF

Turn, paste this into Claude. In my Remotion project, read the installed Remotion Markup skill and audit this component, paste one component. List every place it breaks a rule such as CSS transitions, transform strings, missing per mount for, timing not derived from FPS or unmeasured text, and rewrite only those lines. Then check two things yourself. Render three frames with a frames flag and look at them. Does anything still animate by CSS? And did it change only the lines it named?

---

## beat-BOUT

what the emotion skills do at Nick Bear Brown.

---

## beat-BVDT

Let's recap with Claude. The skills are rule files and agent reads while it writes remotion code, not a renderer. The rules that matter frame driven motion timing on the node promount a second early measure text before placing it. They are installed at a pinned version with transitions, layout utilities, captions, and media utilities added to match. Captions and audio become data, a composition can read while the toolkits clock stays in Python. The toolkit then upgraded to the latest promotion with React 19 and effects, text highlights, and motion blur now render live. And an update is a command and a diff.

---

