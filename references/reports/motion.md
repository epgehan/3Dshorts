# Motion, expressions, action timing, and transition study

## Evidence and coverage

Private reference analysis only; do not upload the media, sheets, or derivatives. All observations use the supplied compressed 360×640, 30 fps sources. Frame indices are zero based; source time is frame / 30. This is a targeted visual sample, not a claim to have manually inspected all 12,488 frames. I inspected all seven three-second overview sheets and 17 contact sheets containing consecutive native frames (1,020 native frames, about 34 seconds). Thumbnail inspection makes subtle eyelids and limb contacts less certain than large actions. Metrics were calculated separately across all frames; their transition candidates are prompts for review, not an edit list.

| Source | Frames | Duration | Consecutive windows visually examined |
|---|---:|---:|---|
| mirror | 1,922 | 64.0667 s | 0–59, 540–599, 1800–1859 |
| knight | 1,219 | 40.6333 s | 0–59, 780–839, 840–899 |
| spot | 1,898 | 63.2667 s | 0–59, 1500–1559 |
| cashiers | 1,732 | 57.7333 s | 0–59, 1020–1079 |
| shape | 1,895 | 63.1667 s | 0–59, 600–659 |
| railroads | 1,955 | 65.1667 s | 0–59, 1560–1619, 1680–1739 |
| sample-1 | 1,867 | 62.2333 s | 0–59, 1140–1199 |

Reproduce each window from `<private-study>/<slug>/sheets/frames-<start six digits>-<end six digits>.jpg` and inspect the corresponding individual files under `frames/`. The overview covers the entire duration at roughly three-second spacing, with the opening sampled at one second as well. Those overview thumbnails establish breadth, not precise event boundaries.

## Main finding

The distinctive motion is economical cartoon posing staged inside a highly mobile spatial world. A head tilt, eyelid change, mouth replacement, rigid-body lean, or arm rotation does much of the acting. Props and cameras often provide the largest movement. Continuous full-body character deformation is not necessary to produce the observed result. A technically elaborate walk cycle alone will not match this rhythm.

The source also uses blended transitions and effect overlays extensively. The old skill's blanket recommendation of hard cuts for big jumps and 18–40-frame smootherstep glides is too narrow as a description of the references. A useful implementation can use those tools, but must also support overlapping animated scenes, circular viewpoint inserts, fast travel behind occluders, and abrupt reframing.

## Measured microsequences

### Prop action leads the opening: mirror, frames 0–59 (0.000–1.967 s)

The hammer is already raised in the initial composition. The actor holds a readable attitude while the camera creeps. At frame 26 (0.867 s) the raised prop begins its decisive change; frame 27 shows the hammer face presented vertically, and frame 28 (0.933 s) has contact/breakup beginning. Fragments expand across frames 29–39 (0.967–1.300 s), then fall/spread through frames 40–46. Thus the decisive swing/contact occupies only about 3 sampled native frames, while the readable debris follow-through lasts roughly 18 frames (0.6 s). This is much snappier than moving every action through a generic one-second ease.

There is no need to infer a sophisticated skeletal performance: torso/head remain largely intact while the arm/prop and breakable object carry the event. By frames 47–59 (1.567–1.967 s), a lateral camera movement removes the actor from view and introduces the racetrack. Moving scenery here is not a character running.

### Tool swing and camera reveal: shape, frames 0–59 (0.000–1.967 s)

Frames 0–3 establish a scrunched effort face. The hammer lifts across frames 4–8 (0.133–0.267 s), stays high across approximately 8–11, and swings down over frames 12–16 (0.400–0.533 s). The body leans into the end pose; small bright particles appear around the rail at about 17–20. This is anticipation → compact strike → aftermath, with the tool motion more prominent than squash of the whole character.

Frames 22–39 pull back rapidly and progressively reduce the actor's size. By frames 40–59 the huge irregular coaster loop dominates. The character is not shrinking as an acting effect: the set expands in the same perspective reveal. Do not implement this as character scale animation alone.

### Leaning labor and facial changes: railroads, frames 0–59 (0.000–1.967 s)

The worker stays in a diagonal sawing posture for most of the window. Arm/tool activity is small relative to the tilted head and body. Background rails and canyon translate with camera motion. A brief closed-eye expression is visible at frames 41–42 (1.367–1.400 s), with eyes open again by 43; this provides one approximately two-frame closed state (67 ms), not evidence for a universal four-frame blink. The same bent work pose survives nearly the whole two-second window while the composition changes.

### Blink samples: spot and cashiers

In spot frames 0–59, eyes are visibly closed at 24–25 (0.800–0.833 s), open at 26, closed again at 36–37 (1.200–1.233 s), and open at 38. The closed state is two frames in each sampled event, separated by twelve frames onset-to-onset (0.4 s). These could be expressive repeated eyelid beats rather than a naturalistic blink generator. Do not derive a global blink interval from two events.

Cashiers shows closed eyes at roughly 26–27 (0.867–0.900 s), with return to open at 28. Spot and cashiers establish that very short closed-eye holds are present. Shape frames 603–604 show a similar short closed-eye beat, though small source scale makes its exact onset less secure. Expression transitions should be inspectable frame by frame rather than hidden in a random sinusoid.

### Slow expressive change on a held body: cashiers, frames 1020–1079 (34.000–35.967 s)

The seated figure begins slumped sideways. At frames 1035–1042 (34.500–34.733 s) the head rises and the face moves into a broad closed-eye smile; the raised arm follows. Around 1043 onward the smile and raised arm are held through the rest of the sampled sequence, about 37 frames (1.23 s). The chair, machine, and walls drift with a slow camera change, while the body pose remains readable. A pose hold is not a frozen video frame and should not be prohibited by a blanket “no static hold ≥4 f” instruction.

### Emotion swap and laughter: shape, frames 600–659 (20.000–21.967 s)

Frames 600–629 show the first character, with small face/head changes. Frame 630 (21.000 s) changes directly to a different actor and composition at a telescope. This inspected boundary reads as a hard cut, without the multi-frame double image seen in spot. The rival's expression progresses from narrowed eyes to a grin at about 642–646, then eyes squeezed and mouth broadly open by 647–650. The laugh face is held through 659. Laughter is expressed through a small number of clear graphic states and head/body tilt, not continuous realistic lip sync.

### Walk and load staging: knight, frames 780–899 (26.000–29.967 s)

A map-like forest travel view occupies 780–801. Across approximately 802–807 (26.733–26.900 s), a foreground canopy passes across the picture and the composition resolves to a chest carried on a horizontal pole. The detector's candidate at 804 marks the middle of this transition; it is not sufficient evidence for a one-frame hard cut.

At 807–830 the load/pole dominates and the carriers are largely masked by it. By 831–840 the right carrier emerges; frames 840–860 reveal the two figures and a standing priest while the camera withdraws. Legs alternate through simple bent-line configurations and heads tilt under the load. The prop remains the staging anchor. Foot contacts are too small and intermittently hidden to justify a measured stride length, exact foot-plant duration, or a reliable bob percentage. Existing “0.8 m stride” and “3–7% bob” values are implementation defaults, not measurements established by this sample.

At about 890–896 (29.667–29.867 s), the distant wide view overlaps the closer confrontation, with both scales visible. This is a blended shot transition. Do not count all image-motion spikes as impacts or step changes.

### Camera change mistaken for actor movement: railroads, frames 1560–1739

1560–1619 (52.000–53.967 s) approaches a seated actor/umbrella beside rails. The actor enlarges as the environment opens in perspective; this is primarily camera travel. At 1680–1691 (56.000–56.367 s), a wide-eyed standing actor is framed full body. Through 1692–1707 the camera descends/advances to the rail gap, cropping the actor off the top. His disappearance does not imply a jump or fall. Frames 1710–1732 hold attention on the gap with slow scene motion; by 1733–1739 he re-enters via reframing. This provides a useful test case for separating camera motion, cropping, and character acting.

### Crowd reaction: mirror, frames 1800–1859 (60.000–61.967 s)

A row of five figures holds individually tilted heads while background boards and floor recede with the camera. The taller right figure moves from tilted/closed eyes toward a forward, wide-eyed reaction at around 1836–1840. Other faces also change. Money enters from above around 1856–1859, a prop/effect layer that supplies escalation without needing every crowd member to move continuously. This is a sampled change, not proof of identical timing across the crowd.

### Driver and scene transitions: sample-1

Frames 0–35 (0.000–1.167 s) preserve the seated driver pose while face and body lean change. Frames 36–39 (1.200–1.300 s) travel from cabin to exterior through the windshield/body framing, then 40–59 withdraw to a wider traffic view. The driver remains associated with the vehicle; world/camera displacement supplies the large movement.

At frame 1161 (38.700 s), the pool close-up switches immediately to the driveway group; adjacent contact-sheet frames 1160 and 1161 show different settings without an obvious overlap. This is a manually inspected hard-cut example. During 1161–1199 the group keeps a spare set of standing poses, with head/face changes and camera drift rather than constant whole-body animation.

## Transition timing: use an explicit grammar

Spot frames 1500–1514 (50.000–50.467 s) demonstrate a dissolve: the large phone remains visible while the headset operator becomes visible in the same pixels. The strongest overlap is roughly 1505–1512 (50.167–50.400 s), about eight frames; the exact first/last low-opacity pixel is uncertain in compressed thumbnails. Then frames 1518–1541 withdraw from the face to the service counter over about 24 frames (0.8 s). That is a dissolve followed by a camera reveal, not one hard cut.

Mirror 540–599 demonstrates a different grammar. A circular racetrack view grows over the mirror-side character beginning around 546; by 549 it occupies the circular viewing field against a dark surround. Return begins around 570 and resolves to the outdoor character by 574. A second insert begins around 591 and becomes the racetrack circle by 594. Measured entry/exit bands are approximately 3–5 frames (0.10–0.17 s), while the first viewing interval itself is roughly 21 frames (0.7 s). These are intentional viewpoint inserts, not flashes, exposure errors, or generic transitions to be homogenized into crossfades.

Across the overview sheets, settings and framings often change within the three-second overview interval, with occasional longer acting/diagram sequences. No trustworthy median shot duration can be obtained from that sparse view. Candidate counts (for example nine for mirror and one for shape) substantially undercount real editorial changes. Keep an editorial table with start/end frames and manually classify hard cut, dissolve, camera travel, occlusion, and insert; don't present threshold peaks as authoritative shot boundaries.

## What the revised skill should specify

1. Animate in separate tracks: scene/camera transform; character root/lean/head; expression state; limbs; attached props; independent effects. A changing screen coordinate is not automatically a changed pose.
2. Write action beats as frame events. For a strike, establish the already readable preparation, use a compact 3–6-frame decisive swing, and allow 10–20 frames of aftermath when the story benefits. These are implementation ranges inspired by the measured openings, not universal source averages.
3. Hold poses long enough to read. Use occasional short eyelid and face changes while camera motion or props advance the picture. Do not require all characters to bob, walk, or change expression continuously.
4. Use a small expression vocabulary with decisive changes: narrowed/skeptical eyes, closed effort eyes, circular shock eyes, grin, open laugh mouth, neutral/small talking mouth. Mouth changes need not imply phoneme-accurate lip sync.
5. Support two-frame closed-eye states, but make blink scheduling art-directed and vary or disable it during purposeful closed-eye expressions. Never count a sustained laugh/effort squint as dozens of blinks.
6. Make walking simple and legible; attach/load props consistently; verify contacts in individual native frames. Do not claim physical stride or bob measurements without camera stabilization and visible feet.
7. Build a transition palette with hard cuts, 6–15-frame layered dissolves, brief circular inserts, camera reveals, and occluder-assisted travel. The observed examples support variety; they do not identify an exact easing polynomial.
8. Review event landing against actual narration/audio separately. Silent pictures alone cannot establish “0–3 frames before its word.” Caption changes are not a reliable substitute for voice waveform alignment.
9. Treat freezes as full-frame stasis, not character pose holds. A valid held pose can sit inside an active camera shot. Quality gates must distinguish intentional holds from accidental unchanged frames.

## Limits and implementation honesty

The pictures support flat graphic acting with stick limbs in a spatially shaded world; they do not reveal whether the original used sprites, billboards, mesh rigs, shape keys, hand-drawn swaps, a particular renderer, or any named engine. Three.js/Remotion can implement the observations but is an implementation choice, not a recovered production fact. No exact easing curve, world-unit stride, focal length, rig hierarchy, or universal blink/step period is established here. Apparent squash in the struck pig/fragment burst could include deformation, replacement drawings, debris overlays, and perspective; the compressed sample does not isolate those mechanisms.

Caption implementation follows the user's current rule: ALL CAPS Arial, white only, black outline; no yellow. Existing reference captions and the old skill's “no captions” rule do not override that instruction. Caption animation is not used as evidence for character movement in this report.
