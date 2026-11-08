# Captions and audio specification

## Explicit current user choice

**ALL CAPS · ARIAL · WHITE ONLY · BLACK OUTLINE.** This overrides both the legacy skill's no-caption rule and Salme's earlier white/yellow treatment. Samples' mixed-case text is observed evidence, not the requested output style. Do not add yellow word emphasis, a second typeface, italics, large title cards or explanatory labels without a new instruction.

## Practical typography

Use the actual Arial font selected for production, preferably Arial Bold with a consistent weight. Supply a usable licensed font file or a verified platform installation; do not silently substitute Arial Black, Impact, Helvetica or a serif font and call it Arial. The provided Remotion component loads an explicit font asset and fails if it cannot load.

As a proposed1080-wide vertical starting point, use about70 px font size and6 px black outer stroke, white fill, line-height near1.02. These are implementation starting values, not measured original typography. Scale with canvas width and inspect at360 × 640 equivalence. Center horizontally, initially place the baseline around the lower-middle/three-quarter region, and adjust for the subject and UI safe area. Landscape needs a different placement profile; don't blindly reuse vertical y-values.

Prefer a single word or a compact1–3word group. Uppercasing makes many words wider; split a phrase before shrinking below a readable size. Keep a short maximum line count and avoid covering the causal prop or expression. No word-by-word elastic bouncing is required by the study. White letters and outline remain full-opacity during their interval unless an explicit edit says otherwise.

Use frame-quantized, half-open intervals `[startFrame,endFrame)`, with no overlap for mutually exclusive cue groups. When converting seconds, retain the original timestamps and document the rounding convention. Recommended: round a boundary to the nearest frame once, then share it between adjacent cues so drift cannot accumulate. Do not independently round every duration and sum the errors.

Do not hold an old caption through a new utterance, display captions during unrelated pauses, invent narration words or use screenshot OCR as the final transcript. Caption text/word timing must be reviewed against the actual approved voice. A source caption's swap can lag or lead the audible word; it is not a substitute for audio alignment.

## Renderer placement

Render subtitles after scene ink, depth blur, glow and grade. That keeps them crisp and solidwhite even when the environment is blue, purple, dark or amber. Use an overlay plane that never goes behind a3D prop. Apply correct text-stroke paint order so the outline does not eat the white letter interior. Test long capitals, punctuation and one/two-line cues at the smallest target display size.

`templates/captions/ArialCaptions.tsx` is a small deterministic Remotion overlay, not a complete video project. It expects a configured React/Remotion project, an actual Arial Bold asset URL, reviewed frame cues and the project's canvas configuration. It contains no reference captions or media. Verify font loading and fit in the target renderer before final capture.

## Sound observations and limits

Complete mixed-program FFmpegEBUR128 measurements:

| Source | IntegratedLUFS | LRA(LU) | Truepeak(dBFS) |
|---|---:|---:|---:|
| mirror |−14.0|2.6|−2.1|
| knight |−15.0|2.4|−3.1|
| spot |−14.0|2.1|−2.1|
| cashiers |−15.1|2.0|−3.4|
| shape |−14.0|1.7|−2.1|
| railroads |−14.0|3.2|−2.1|
| sample-1 |−14.1|2.2|−2.1|

These values describe the already mixed exported programs. They do not identify voice-only level, original compressor settings, music gain, SFX gain, narrator identity, exact speech rate, or original stems. The old '+3dBmusic/−6dBSFX' recipe is not established by this measurement and is not a universal new default.

For an original production, preserve supplied narration unless the user authorizes changes; duck music/effects so speech remains clear; prevent clipped peaks; choose a delivery loudness target and measure it on the final mix. Match the quiet/sudden effect's narrative role, not the exact source recording. Use a factual/original script and licensed/original sounds. No automatic music/SFX addition if the user requests only the supplied voice.

## Checks

- Actual font loaded; uppercase source text; every glyph solidwhite with black outline.
- Cues match the approved narration and correct audio version.
- No hidden/out-of-frame/overlapping subtitle groups.
- No scene blur/grade on captions and no subtitle motion introduced by camera transforms.
- Final program duration, fps, audio start/end, integrated loudness and peak measured.
- Whole-program metrics clearly distinguished from isolated stem claims.
