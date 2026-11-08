---
name: cartoon-3d-short-v2
description: Create original animated history/science/story shorts with flat ink-drawn characters in dimensional illustrated sets. Use when asked for cartoon shorts, the Clip Scout style, cartoon-3d-short, or videos matching the supplied seven-video study. Covers character design, varied lighting, scene depth, camera movement, frame-based animation, narration alignment, ALL-CAPS Arial white subtitles with black outline, and measurable visual QA. This is the evidence-based successor to cartoon-3d-short, not a guarantee of identical source rigs or pixels.
---

# Cartoon 3D Short v2 — Clip Scout

Build the visual language, not the source video's identities or story. The user wants the supplied samples' character construction, color separation, staging, camera grammar and concise acting. Keep new characters, scripts, sets and narration original. The observed medium is **flat illustrated people inside dimensional environments**; exported video does not identify the original software, geometry, rig, lens or shader.

## Authority and evidence

1. Current explicit user instructions override this skill, old project rules and examples.
2. Default subtitles are **ALL CAPS, Arial, white only, black outline**. No yellow/current-word color, serif, random font substitution, automatic labels or added titles. This is a deliberate user override of the samples' mixed-case captions and the old skill's no-caption default.
3. This `SKILL.md` is the active workflow. [Production guide](references/PRODUCTION_GUIDE.md) contains the detailed implementation instructions. Load the relevant topic reports before changing that part of the look.
4. [Seven-video study](references/SEVEN_VIDEO_STUDY.md) and its reports are new evidence. [User design guide](references/source-guides/USER_DESIGN_GUIDE.md) remains a visual prior, except where new observations or user instructions refine it.
5. [Legacy skill](references/source-guides/LEGACY_SKILL.md) and `templates/bridge/` are MIT-attributed historical implementation material. Their fixed numerical defaults are not measurements of these seven videos and do not override this skill.

Use three evidence labels: **OBSERVED** (named source frame/window or measured export), **INFERRED** (plausible rendering explanation), **RECOMMENDED** (implementation starting point). Never convert an estimate or inherited preset into a recovered source setting. See [measurement methods](references/MEASUREMENT_METHODS.md).

## Read by task

| Task | Read |
|---|---|
| New episode / full workflow | [Production guide](references/PRODUCTION_GUIDE.md), [study](references/SEVEN_VIDEO_STUDY.md) |
| Character / expression / costume | [Character report](references/reports/characters.md) |
| Light, exposure, faces, shadow | [Lighting report](references/reports/lighting.md), [sampled patches](references/reports/lighting-patches.json) |
| Shot angles, moves, reveals | [Camera report](references/reports/camera.md) |
| Poses, gestures, blinks, transitions | [Motion report](references/reports/motion.md) |
| Grounding, overlap, focus | [Depth report](references/reports/depth.md) |
| Sets / wood / metal / glass / water | [Materials report](references/reports/textures.md) |
| Contours, color/grade, post | [Outlines report](references/reports/outlines.md), [grade report](references/reports/grade.md) |
| Subtitles and narration | [Captions and audio](references/CAPTIONS_AND_AUDIO.md) |
| Verification / final delivery | [Acceptance checklist](references/ACCEPTANCE_CHECKLIST.md) |

## Required production loop

### 1. Establish the brief

Record subject, evidence sources, audience, aspect ratio, target duration, narration source, output resolution/fps, subtitle policy, and the important reference IDs. Ask only when a material choice is unresolved; proceed with independent work while waiting. Do not add approval gates already resolved by the user's instructions. Explicit timing instructions override an aesthetic preference for a particular shot length.

**Default proposal:** vertical 1080 × 1920 at30 fps; an optional1440 × 2560 final if requested and supported. Do not impose the legacy55–70second duration: one supplied sample is40.63seconds. Do not generate vertical when the user requests landscape. The360 × 640 references are inspection sources, not an output-resolution target.

### 2. Lock character construction before whole scenes

Create an original character sheet: front, useful three-quarter, back, seated, five readable expressions, hand/prop contacts and costume palette. Use a broad pale irregular near-round/bean head, sparse eyes/brows/mouth, compact capsule torso, little neck, thin plum limbs and small dot/mitten hands. Hair is a broad painted silhouette; hats/costume establish the role. Adults in selected views read roughly2.7–3.5head heights, but pose and perspective change that ratio; treat it as a starting range, not an immutable constraint. No automatic modeled ears/nose, sculpted cheeks, glossy skin or tubular arms. Selective ears, profile details, hair shading and armor volume can be justified by the shot.

Front, three-quarter and back views require appropriate artwork. Do not rotate every actor to always show its frontal face. Preserve silhouette, face spacing, costume colors and limb thickness as scale changes. Keep character ink separate from world-outline passes to avoid doubled contours.

### 3. Build a scene-specific world and light recipe

Stage foreground, acting plane, rear set and horizon with clear overlap and diminishing scale. Support hands on tables, bodies on chairs, feet on ground, and props in hands. Use real depth or layered perspective when the shot needs near/far parallax or newly revealed surfaces; a2D camera move is acceptable for a deliberate graphic insert.

Choose a recipe for the scene: open day, warm practical interior, fluorescent shop, cobalt night, peach/pink dusk, or overcast wet exterior. Pale character faces normally stay readable while the set takes stronger light/color changes. Motivated glow and expressive face-color changes are exceptions, not a global tint. Warm highlights/cool shadows are common, **not universal**; warm cast shadows also occur.

World materials vary: sparse drawn wood and stone, denser canyon/ballast, glossy cars, glass, wet roads and water can coexist with flat characters. Do not force every surface to be matte, uniformly noisy, heavily inked or equally sharp. Focus on the narrative acting plane, which may be behind a blurred foreground figure.

### 4. Build the timeline from narration and frames

Use the actual approved audio and word/segment timestamps. Keep integer frame intervals `[startFrame,endFrame)` at the chosen fps. Track character pose, expression, limb/prop action, camera, effects, subtitle and edit opacity independently. Check that a moving camera has not been misread as an actor moving, falling or shrinking.

Use economical acting: held pose, head tilt, brow/lid swap, concise arm/prop action. A valid pose may hold while the camera or props move. Observed examples include2-frame closed-eye states and a37-frame readable pose hold; there is no mandatory blink interval or ban on static poses. Do not run random blinks during a purposeful closed-eye expression.

Camera grammar includes low/high/overhead, over-shoulder, extreme close-up, broad perspective, large pullback, circular POV inserts and foreground reveals. Support hard cuts, short layered dissolves, and occluder-assisted transitions. Do not apply a fixed push/roll/ease/dissolve duration to every shot. Proposed action and transition ranges are in the reports; confirm against narration and actual frames rather than claiming recovered curves.

### 5. Make look probes and verify contacts

Before a full episode, render: a daytime full-body pose, a face close-up, a night/interior pose, a seated/prop-contact interaction, and a foreground reveal. Reuse one character across probes. Inspect at intended output size and at360 × 640 equivalent. Compare silhouette, face readability, subject/world exposure, material detail, occlusion, motion and framing separately. Change one category at a time.

When independent reviewers are available, assign bounded topics and provide frame/time evidence. A fresh review should challenge unsupported claims. No particular unavailable model or named reviewer is required; state what was actually checked. Never claim a visual match based solely on numerical render settings or passing a linter.

### 6. Render and review

Render deterministic frames from timeline state; avoid `Math.random()`, wall-clock time and unseeded procedural changes. Separate world ink, depth-aware blur, restrained localized glow/tone/grade and final captions. Captions stay crisp and white after scene postprocessing. Preserve correct alpha/depth around card edges.

Run the full program decode and audio checks, confirm resolution/fps/frame count/duration, and inspect all cuts, expression changes, prop contacts and effect onsets frame by frame. Compute per-frame diagnostics, but distinguish an intentional hold from a broken freeze, a white graphic effect from an accidental blank, and a caption swap from scene movement. Review representative whole shots in motion, not only stills.

### 7. Deliver evidence, not promises

Provide final output, editable source, timing/word data, validation results and any specific unresolved limits. Keep supplied study videos, full frames, contact sheets and transcripts private by default. Commit derived guides, measurements, scripts and original code/assets only. Do not upload reference pixels just because a repository is public. Reference-exact appearance requires iterative look checks; exported samples cannot guarantee recovery of original source files or exact pixel identity.

## Hard failures

Reject spherical/glossy replacement heads; bulky limbs; inconsistent face/costume identity; floating feet; hand/prop intersections; frontal faces on back-facing bodies; automatic shadow coloring of the whole face; uniformly blurred scenery; text hidden behind scene geometry; non-Arial or mixed-color subtitles; chronology/audio drift; and unsupported claims of original3D parameters or exhaustive human inspection.

## Tooling and portability

The scripts in `scripts/` analyze supplied local videos without uploading their pixels. `analyze_references.py` checks native30 fps, exports every frame and measurements; `verify_study.py` checks coverage; `build_private_viewer.py` makes frame stepping; `measure_audio.py` measures the mixed soundtrack. See [README](README.md) for commands and installation. The inherited bridge renderer requires a configured Remotion project and separately supplied assets; it is not a ready-to-render new episode.
