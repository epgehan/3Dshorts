# Study evidence and validation

- [Full inventory](metrics/inventory.json):7source hashes, native video metadata, all-frame measurements, video/container durations and explicitly tentative transition candidates.
- `metrics/*.frames.csv`: one record for every decoded source frame; see [measurement methods](../references/MEASUREMENT_METHODS.md) for units, masks, limitations and interpretation.
- `metrics/*.summary.json`: individual source summaries and binned aggregate pixel statistics.
- [Coverage verification](verification.json):12,488ordered native frames and all private JPEG export headers checked.
- [Audio metrics](audio-metrics.json): FFmpegEBUR128 of complete mixed exports; no isolated-stem inference.
- [Viewer QA](viewer-verification.json):7 videos, single-frame/30frame stepping, final-frame seek and playback tested in Chromium.
- [Tooling tests](tooling-tests.json): synthetic30 fps decode, non30 fps rejection, repeat-run/inventory safeguards and installer privacy/overwrite checks.
- [Baseline code hashes](baseline-manifest.json):13 unchanged MIT-attributed bridge files.

No reference image/video/audio files or absolute private input locations are in this folder. The CSV's relative `frames/...jpg` labels address the separately generated private study collection, not committed public files. Human topic reports document sampled visual coverage; the all-frame diagnostics are exhaustive computation, not proof everyframe was human-inspected.
