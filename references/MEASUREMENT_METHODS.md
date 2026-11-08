# Measurement methods and confidence

## Inputs and cadence

Seven user-supplied MP4s were inspected. Every native video stream is360 × 640 at30/1fps. The study decoded and exported all12,488video frames; no interpolation or duplication was added to make a synthetic30 fps stream. Video duration is frame_count/30. Container/audio duration can be a few dozen milliseconds longer and is listed separately. Zero-based frame indexf corresponds tof/30seconds because source video PTS begin at0; the CSV also retains native best-effort PTS.

Inventory includes source-fileSHA-256, frame counts, video/container durations, cadence maximum error and software versions. `analysis/verification.json` validates the recorded frame sequence and all private exported image headers. The study is reproducible using the original local files, which are not committed.

## Full-frame metrics

`analyze_references.py` decodes each frame using OpenCV. It measures source RGB before making the inspection JPEG. Each CSV record contains index, PTS,30 fps timecode, private relative image name, luma percentiles, mean saturation, dark-pixel proxy, half-resolution Laplacian variance, upper/lower grayscale frame differences, upper HSV histogram distance, optional tracked affine fit and decoded-RGB hash.

- The full-source RGB hash identifies that decoder's frame pixels, not an uploaded PNG or the source compressed packet.
- JPEG quality93 exports preserve360 × 640 dimensions but introduce another small lossy encoding. Visual inspection and manually sampled patches on those exports inherit that limit.
- The top72%mask excludes most subtitles, not all possible typography. The lower-region difference is not a definitive caption detector.
- HSV saturation and gamma-encodedY' describe rendered pixels. They do not recover materials, light intensity, scene-linear luminance, contrast preference or stylistic quality.
- Laplacian variance mixes texture, edges, compression and blur. It is not a calibrated depth-of-field radius.
- The16×16×16RGB palette bins are whole-program pixel distributions. They mix all scenes and do not identify a semantic face/sky/wall palette.

## Motion and edits

Features are tracked at180×320 inside the upper72%, then fitted to a partial affine transform with RANSAC. CSV translation is at the affine image origin in that half-resolution coordinate system. Camera report displacement values instead transform an explicitly named image point into native360px coordinates. This is image motion, not camera meters, field of view, a physical dolly path or original easing curves. A tracked fit can follow a moving foreground object rather than the set. Reject low-inlier or ambiguous fits and examine native frames.

Adjacent image/histogram thresholds generate candidate discontinuities. They miss many dissolves and can trigger on effects or rapid foreground travel. The33automatic candidates across all 7files are NOT33shots and must not be reported as a complete edit list. Human-reviewed camera/motion reports distinguish cuts, blends, occluder transitions, inserts and continuous travel. Their onset/end bounds are visual estimates; compressed low-opacity blends do not reveal exact alpha keys.

## Human review coverage

All seven whole-duration overview sheets were visually reviewed by topic reviewers. Each sheet samples an opening, approximately3s-spaced frames and the final frame. The frame collections and contact sheets cover every native frame. Reviewers additionally inspected named native frames and consecutive30 fps windows; each report lists its coverage. Motion review alone reports17full60-frame sheets (1,020 frames); camera and character/depth reviews include additional windows. Some review windows overlap. Do not add reviewer counts together and claim every unique frame was human-reviewed. Computational coverage is exhaustive; human semantic inspection is targeted and documented.

No claim of exhaustive manual examination, recovered rigs, original software identification, physical light/lens recovery, or exact pixel reproduction is supported. The deliverable is a source-backed production guide with calibrated limits.

## Reproduce

1. Install Python dependencies from `requirements-analysis.txt` in a local environment, and install FFmpeg/FFprobe.
2. Make an untracked input list: `[{"slug":"mirror","path":"/your/local/video.mp4"}, ...]` with the seven slugs used in the inventory.
3. Run `python scripts/analyze_references.py --inputs inputs.local.json --private-output .private-study --metrics-output analysis/metrics`.
4. Run `python scripts/verify_study.py --metrics analysis/metrics --private-output .private-study --report analysis/verification.json`.
5. Run `python scripts/build_private_viewer.py --metrics analysis/metrics --private-output .private-study`, then serve `.private-study` locally to inspect every frame and contact sheet.

The analyzer intentionally rejects a non30 fps source rather than quietly changing its cadence. Adapt the study explicitly for other frame rates and document the conversion if needed. Keep reference pixels, source narration and private input paths out of Git.

For a partial rerun use `--only <slug>`; existing other-video summaries remain in the inventory. Existing frame collections are protected by default. Pass `--overwrite` explicitly to replace only the selected inputs’ generated frame/sheet JPEGs, or choose a fresh private output folder.
