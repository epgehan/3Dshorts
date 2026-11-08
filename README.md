# 3Dshorts — Cartoon3DShort v2

An improved, evidence-based successor to `cartoon-3d-short`, combining the user's character/background guide, the MIT-licensed baseline, and detailed study of seven supplied videos.

**Current subtitle default: ALL CAPS · Arial · white only · black outline.**

## Start here

- [Active reusable skill](SKILL.md)
- [Detailed production instruction guide](references/PRODUCTION_GUIDE.md)
- [Seven-video findings and changes from the old skill](references/SEVEN_VIDEO_STUDY.md)
- [Character report](references/reports/characters.md)
- [Lighting](references/reports/lighting.md), [camera](references/reports/camera.md), [motion](references/reports/motion.md), [depth](references/reports/depth.md), [materials](references/reports/textures.md), [outlines](references/reports/outlines.md), [grade](references/reports/grade.md)
- [Captions/audio specification](references/CAPTIONS_AND_AUDIO.md)
- [Acceptance checklist](references/ACCEPTANCE_CHECKLIST.md)

## What was actually studied

All seven sources are native360 × 640 at30 fps. **12,488 frames** were decoded, measured and exported locally, with212 consecutive-frame contact sheets covering every frame. Topic reviewers inspected all whole-duration overview sheets plus named native frames and consecutive-frame motion windows. All-frame computation is exhaustive; human visual inspection is targeted and explicitly documented rather than falsely described as12,488individual manual reviews.

See [inventory and per-frame metrics](analysis/metrics/), [coverage verification](analysis/verification.json), and [methods/limits](references/MEASUREMENT_METHODS.md). Source videos, frame images, sheets and audio remain private and are excluded from Git. They can be recreated locally using the scripts and your original uploads.

## Install the actual skill

A clone alone does not register a skill with your coding tool. Clone this repository, then run its installer:

```bash
git clone https://github.com/epgehan/3Dshorts.git
cd 3Dshorts
python scripts/install_skill.py --tool codex
```

This copies the package to `~/.agents/skills/cartoon-3d-short-v2/`. For Claude Code:

```bash
python scripts/install_skill.py --tool claude
```

That installs to `~/.claude/skills/cartoon-3d-short-v2/`. `--scope project --project /path/to/your/project` uses a project-local discovery directory instead. Paths also work under Windows with your Python installation (`py` can replace `python`). Existing destination folders are preserved; the installer refuses to overwrite them. Restart/reload your coding tool and confirm the new skill appears. Filesystem installation and current-session discovery are separate checks.

Then ask: **“Use cartoon-3d-short-v2 to make an original short about …”** The skill first records your brief, then creates look probes before a whole episode.

## Reproduce the private30 fps study

Python3.10+, FFmpeg/FFprobe and the analysis dependencies are required. Use a local virtual environment:

```bash
python -m venv .venv
# Activate .venv using your platform's normal command.
python -m pip install -r requirements-analysis.txt
```

Create an untracked `inputs.local.json` containing local file locations, for example:

```json
[
  {"slug":"mirror","path":"C:/your/videos/How-a-Mirror-SnapYT.App.mp4"},
  {"slug":"knight","path":"C:/your/videos/This-Knight-Found-SnapYT.App.mp4"}
]
```

For this exact seven-video study include all slugs from the inventory. Run:

```bash
python scripts/analyze_references.py --inputs inputs.local.json --private-output .private-study --metrics-output analysis/metrics
python scripts/verify_study.py --metrics analysis/metrics --private-output .private-study --report analysis/verification.json
python scripts/build_private_viewer.py --metrics analysis/metrics --private-output .private-study
python -m http.server 8841 --bind 127.0.0.1 --directory .private-study
```

Open `http://127.0.0.1:8841/`. Select a video, step one frame with left/right arrows or30 frames withShift+arrow, play at30/15/5/1fps, and open the current60-frame contact sheet. Inspect native source files for final pixel judgments: the convenient JPEG frame collection adds a small quality93encoding. Allow disk space for every exported frame. The analyzer rejects non30 fps inputs instead of silently interpolating them.

## Production scaffolding and honest verification

`templates/bridge/` contains the attributed baseline renderer as an adaptation reference, not a new ready-to-render episode. It needs compatible Remotion/Three.js dependencies, assets, a registered composition and rewritten story/cast/timing. `templates/captions/` contains the new white-only Arial overlay and requires an actual supplied Arial Bold font asset. See the template READMEs.

The new study supports multiple lighting recipes, protected pale faces, character front/back variants, held poses, short expressive changes, hard cuts/dissolves/POV inserts and shot-specific camera moves. It does not establish original physical light intensities, exact lenses/eases/rigs or a single immutable shader preset.

No new matching short has been rendered yet. Package checks and source-frame analysis are not a production look-match pass. An original episode still needs probes, narration alignment, contact/motion checks, a final render and visual acceptance.

## Attribution

See [upstream notes](UPSTREAM.md) and [MIT license](LICENSE). Private reference pixels are not distributed by this repository.

For a partial rerun use `--only <slug>`; existing other-video summaries remain in the inventory. Existing frame collections are protected by default. Pass `--overwrite` explicitly to replace only the selected inputs’ generated frame/sheet JPEGs, or choose a fresh private output folder.
