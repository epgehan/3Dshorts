# Production instruction guide

This is the working specification for `cartoon-3d-short-v2`. Read the topic reports for timestamped examples, measured windows and uncertainty. The seven exports establish a visual/motion target; they do not reveal their original authoring files.

## 1. Project brief and evidence

Create `PROJECT_BRIEF.md` before production. Record the original story, factual sources, audience, aspect ratio, fps, output dimensions, approved narration file, whether narration is locked, caption style, language, and important reference IDs. Preserve user-specified timing. Ask when the answer materially changes the result; don't ask again for already resolved choices.

Use a versioned evidence folder containing only permitted reference files locally. Map each source to an ID and SHA-256. Probe video and audio separately, retaining source PTS. Study native cadence before making frame-based claims. For this package every source is30 fps360 × 640; upscaling is useful for inspection but creates no new detail. The native-frame extractor rejects other rates so conversions cannot happen silently.

Keep `OBSERVED`, `INFERRED` and `RECOMMENDED` labels in working notes. 'Face stays pale against blue wall in cashiers f660' is observed. 'A protected card material may produce this' is an inference. 'Try a separate character-light response' is a recommendation. Do not report a guessed shader parameter as a source measurement.

## 2. Character drawing specification

### Shape and proportions

Start with a large near-round/soft bean head, slightly irregular forehead/chin, compact capsule torso and narrow limbs. Most selected standing adults are in an approximate2.7–3.5head-height envelope, but hats, hair, leaning, seated poses and camera perspective alter the apparent ratio. Use relative measurements against the same actor's neutral sheet instead of forcing every body to3.5heads.

The face is a broad pale graphic region, with little or no visible neck. Keep eyes, brows and mouth sparse; do not add realistic anatomy to fill blank space. A tiny profile/nose/ear detail is possible when motivated by a view, but not a default sculpted head. Draw face features independently of world meshes. The base should never become a sphere with a projected smile.

Hair is a clear silhouette with broad curved streaks and limited painted volume. It can have highlights; 'flat character' does not mean one uniform fill for all hair and costume. Tunics, polos, vests, ties, aprons, hats and badges identify roles with a few graphic marks. Armor is a deliberate plate/rivet/metal-volume exception, not a new muscular human base. Avoid cloth simulation or densely wrinkled fabric unless the scene specifically calls for it.

Arms/legs are dark plum/charcoal strokes, with small circular/mitten hands and short turned feet. In large reference views, a limb can read around4–6%of face width; treat that as a manually estimated starting relation, not a calibrated source pen size. Outline weight varies with shot scale and lower/shadow edges. Use at least two scales of line detail: strong silhouette and finer face/costume marks.

### Expressions

Build neutral, half-lidded confidence, skeptical/asymmetric brow, surprise, concern, effort/squint, smile, laugh and neutral speaking states. Surprise uses outlined circular white eyes and small pupils; a tiny oval mouth and lifted brow carry the change. A grin/teeth grid is a deliberately graphic shape, not modeled individual teeth. Give expression changes a motivated beat and avoid unexplained constant mouth motion.

Match hair, costume patches, face spacing, head width and limb thickness across expression replacements. Blinking is not the same as laughter, sleep or exertion: a closed-eye acting state can hold. Two-frame closed states occur in the new samples, but an arbitrary repeating two-frame blink loop would not reproduce their art-directed rhythm.

### Facing and contacts

Supply front, three-quarter and back artwork as needed. Cashiers and sample-1 show viewpoint changes inconsistent with one permanent frontal billboard. Do not rotate eyes to camera while the body faces away. Split front arm, rear arm, held object and body layers where overlap demands it.

Every action should answer: which hand touches which prop, what supports the body, where do feet plant, and which object is in front? Check gripping the wheel, resting on a counter, sitting on a chair, carrying a pole/chest, crossing a door and leaning over a desk in adjacent frames. Keep small feet grounded with contact shadow plus directional cast shadow when visible.

## 3. Dimensional set construction

Make a simple depth plan before building detail: near framing object → actor/prop plane → rear set → far scenery/horizon. Floors, rails, tiles, floorboards and desks converge consistently. Repeated objects diminish with depth. Avoid a flat background image that cannot support the intended reveal.

Use sparse illustrative wood/stone where the setting supports it; use denser rock/ballast, reflected cars, glass, pool water and wet roads when the scene needs those cues. The samples are not uniformly matte. Preserve the simpler flat actor against a world with more complex material response. Don't let texture density consume the expression or causal prop.

A real3D set is useful for changing visible surfaces, layered occlusion and near/far parallax; layered2.5D compositing may be sufficient. No particular renderer is established by the sources. When adapting the inherited Three.js/Remotion scaffold, retain its useful separation of world, actors, camera and post while replacing story-specific assumptions.

## 4. Lighting recipes

Choose per-shot intent rather than a global look preset. Define ambient world color, key direction/color, face response, contact/cast shadow, practical lights and optional haze. Record each as a proposed control, not a recovered original parameter.

- **Open daylight:** pale faces/dark contours remain clear; skies can be vivid blue/cyan; ground/wood can be warm; use controlled contact and cast shadows. Do not crush shadowed foliage to black.
- **Warm practical interior:** local amber lamp/candle/windows provide pools and edges while rear set can stay green, teal, brown or plum. Keep the face readable and the practical's bloom localized.
- **Fluorescent shop:** ceiling planes, tiles, green walls and white panels establish a bright mundane room. No unnecessary golden cinematic wash.
- **Cobalt night:** set and sky can shift strongly blue while pale face stays cream/pale lavender. Use motivated warm windows or white ride bulbs. Don't simply multiply every actor pixel by saturated blue.
- **Peach/pink dusk:** horizon key and long graphic shadows can be warm or mixed; universal violet cast shadows are not supported by knight's sunset examples.
- **Overcast wet exterior:** gray-blue ambient, subdued world saturation, reflective road/headlights and visible actor outline. A sunny amber grade would contradict this recipe.

Motivated glowing props may color a face, and an expressive purple anger face is present in railroads. Use those as explicit state/effect overrides. Separate face protection from emission: a clear face need not behave as a glowing lamp. For Three.js, a controllable character response or painted light tint is a reasonable starting solution, but verify shadows and scene integration.

## 5. Camera and lens grammar

Plan each shot around what the viewer must understand. Use extreme object inserts, face close-ups, full figures, over-shoulder views, overheads, low track-level views, broad environments, scale reveals, optical/POV circles and vehicle/window frames. A large world reveal explains scale; a generic slow push does not substitute for it.

Separate camera transform, focal framing, scene scale, actor root movement and transition opacity. In the samples a figure disappearing from frame may be a camera crop, not a jump/fall. A figure shrinking along with the set may be a pullback, not body squash. A fitted image scale cannot uniquely distinguish optical zoom, dolly toward a plane or2D scaling.

Choose physical/layered depth when near objects sweep faster than the rear set and new surfaces become visible. For graphic inserts or a nearly flat poster, an intentional2D reframing can be adequate. Keep motion deterministic and inspect landmark paths. Do not bake a4–5°roll or identical18–40frame ease into every shot.

Use foreground occlusion deliberately: tree trunk, door jamb, window, close board, rail or dashboard. Plan entry, maximum coverage, exit and the reveal. Brief total subject occlusion can be correct during a wipe; prolonged accidental face blockage during explanation is a failure.

Depth of field follows the narrative plane, not always the nearest row's eyes. A near shoulder can be soft while the rear speaker is sharp. Wide views retain enough geography to explain location. Check card alpha/depth edges and caption separation. Do not use bloom, blur or haze as a universal mask for weak geometry.

## 6. Acting and timing

Use independent tracks for actor root, body lean, head tilt, expression, near/rear arms, held prop, free effect, camera and edit. Maintain consistent pose transforms and contact constraints. Don't animate every layer constantly.

Measured examples show compact decisive actions: mirror's opening strike/contact occurs aroundf26–28, with debris continuing roughly18frames; shape's hammer lift/strike and rapid pullback occupy distinct phases. This suggests a recommended action grammar of readable preparation → short decisive change → longer aftermath. The precise duration belongs to the narration and action, not a universal easing constant.

Held poses are valuable. Cashiers f1043–1079 holds a raised-arm smile for about37-frames while scene/camera motion continues. A rule banning a static character for four frames would force unnecessary motion. For walks/carries, keep leg shapes simple and readable; don't claim a recovered stride in meters from small occluded feet.

Separate edit grammar:

- A hard cut for a clear immediate change.
- A short layered dissolve when old/new settings visibly overlap.
- Continuous camera travel through a frame/doorway when geometry supports the reveal.
- An occluder-assisted scene swap when a foreground object masks the change.
- A circular optical/POV insert when the story involves looking through an object.

Some examined blends span roughly several to a dozen frames. That does not set all transitions to one duration. Review the first/last low-opacity frame and keep outgoing/incoming timing explicit.

## 7. Narration and captions

Use approved original/provided narration; do not imitate or claim to recover the reference voice. Align words/segments to that exact file. If the user locks image timing, fit visuals first; only retime narration with explicit authorization. Validate final audio and video end together.

Current default: ALL CAPS, Arial, solidwhite, black outline. See [caption guide](CAPTIONS_AND_AUDIO.md). Captions follow voice and sit after scene postprocessing. Keep word changes crisp and grouping short. No yellow highlighting, italic emphasis or extra scene titles by default. Props' incidental text is not a request to generate captions or new labels.

## 8. Look-development and acceptance

Render original probes before an entire episode: full-body day, close-up face, dark interior/night, seated/hand contact, back/three-quarter and foreground reveal. Inspect both output size and360 × 640-equivalent playback. Compare the same actor through lighting/view changes. Change one category at a time so the cause of improvement is visible.

Use [acceptance checklist](ACCEPTANCE_CHECKLIST.md). Record exact frame/time and what was actually checked. Programmatic all-frame checks are valuable, but semantic visual review remains necessary. Sample sources are compressed; do not announce exact pixel reproduction, an original-rig recovery or an Opus review that did not occur.

A finished delivery contains final render, editable original source/assets, word/shot data, source attributions, output metadata, full-decode/frame checks and a concise list of unresolved limits. Study videos, extracted frames, sheets and source transcripts stay private unless the user separately authorizes an appropriate distribution workflow; this repository does not contain them.
