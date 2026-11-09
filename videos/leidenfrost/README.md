# Why is that water skating?

Original 15-second 9:16 cartoon science short, produced using this repository's `cartoon-3d-short-v2` skill and the supplied Mia/Leo script.

- Canvas: 1080 × 1920, 30 fps, 450 frames, 15 seconds.
- Original flat drawn Mia/Leo cards in a dimensional Three.js kitchen, moving pan/drop, side-view vapor explanation and reveal.
- Dialogue: exact user wording, distinct original neural voices (Kokoro af_heart/am_michael), generated sound effects, no music.
- Subtitles: actual Arial Bold, ALL CAPS, white with black outline. User-requested LEIDENFROST EFFECT appears at the spoken reveal.
- Full four-scene timings are retained: 0–3, 3–6, 6–12, 12–15 seconds.

## Watch

[Download/watch the finished MP4](Leidenfrost_15s_1080x1920.mp4).

For the editable preview, install Node 22+, then:

```bash
npm install
npm run preview
```

Open the printed localhost URL. The preview supports play/pause and scrubbing with the provided audio. It uses local Three.js and audio assets, not external render-time requests.

## Font and rendering

Use your installed Arial Bold or place your usable Arial Bold font file at `assets/Arial-Bold.ttf`. The font binary is not redistributed in this episode; current production used the verified Arial Bold asset available in the workspace. The baked captions are already present in the MP4. Windows normally has Arial Bold installed. Linux rendering needs the explicit asset or an actual Arial Bold installation, not a substitute font.

FFmpeg and an installed Chromium/Chrome are required for rendering. `CHROME_PATH` selects your browser executable. Optional `VIDEO_OUTPUT` and `FRAME_QA_DIR` select output/verification paths.

```bash
npm run render
```

The renderer serves the project locally, captures 450 deterministic frames, pipes them into FFmpeg, and muxes the exact 15-second production master `audio/audio.wav`. `puppeteer-core` does not download a browser. Set `CHROME_PATH` for your own platform. There is no Remotion host requirement for this episode: the active skill permits a deterministic Three.js/layered implementation.

## Editable source

- `scene.js`: dimensional world, original Canvas2D character artwork, camera/pose/face tracks, drop/vapor animation and depth-aware postprocessing.
- `index.html`:9:16 stage and actual Arial caption/reveal overlays.
- `captions.json`:14 caption groups and 33 aligned spoken words; cue intervals are half-open 30 fps frames.
- `audio/`: production master/browser audio, reproducible dialogue/SFX/ASR scripts and measurements. External Kokoro/Whisper models are not committed. See audio README for setup and alignment limits.
- `PROJECT_BRIEF.md`: original request, design decisions, scientific interpretation and timing.
- `verification.json`, `REVIEW.md`: final render/look/science checks and limitations.
- `CHARACTERS.jpg`, `LOOK_PROBES.jpg`, `RENDER_CHECKS.jpg`: original character sheet, look studies and actual encoded frame checks.

## Scientific interpretation

A very thin vapor cushion forms from the underside of a liquid drop over a sufficiently hot surface. Escaping vapor separates the drop from the pan; the hovercraft is an analogy. The side-view gap and pale flow are enlarged/schematic, not literal photographic measurements or a solid support pad. No universal temperature is asserted. The last scene returns to the ordinary kitchen/pan rendering; 'real drop' in the script is interpreted as normal scene view rather than inserting unrelated live-action footage into a cartoon short.

Sources: Burton et al., *Geometry of the Vapor Layer Under a Leidenfrost Drop*, Physical Review Letters 109, 074301 (2012), https://doi.org/10.1103/PhysRevLett.109.074301; APS Physics educational synopsis, https://physics.aps.org/articles/v13/s148.

## Attribution

Original scene/cast/SFX/code in this episode. Three.js 0.170.0 is MIT-licensed; see `assets/THREE-LICENSE.txt`. Synthetic voices use the externally downloaded Kokoro v1.0 model; no reference voice recording is copied. Original study videos/images are not included. Output is a new interpretation of the skill, not a claim of identical source pixels or recovered reference rigs.
