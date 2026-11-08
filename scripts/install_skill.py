#!/usr/bin/env python3
"""Install this repository as a filesystem-discoverable skill without private media."""
from pathlib import Path
import argparse,shutil
p=argparse.ArgumentParser();p.add_argument('--tool',choices=['codex','claude'],default='codex');p.add_argument('--scope',choices=['user','project'],default='user');p.add_argument('--project',type=Path,default=Path.cwd());p.add_argument('--destination',type=Path,help='Explicit destination for testing/custom installs; must not already exist.');a=p.parse_args();source=Path(__file__).resolve().parents[1];base=Path.home() if a.scope=='user' else a.project.resolve();target=a.destination.resolve() if a.destination else base/('.agents' if a.tool=='codex' else '.claude')/'skills'/'cartoon-3d-short-v2'
if target.exists():raise SystemExit('Destination exists; preserve it or choose a new destination before installing: '+str(target))
if target==source or source in target.parents:raise SystemExit('Install outside the source repository to avoid recursive copying.')
ignore=shutil.ignore_patterns('.git','.venv','.private-study','private','reference-videos','frames','sheets','node_modules','__pycache__','*.pyc','*.mp4','*.mov','*.mkv','*.webm','*.avi','*.mp3','*.wav','*.jpg','*.jpeg','*.png','*.webp','*.zip','inputs.local.json','inputs.*.private.json')
shutil.copytree(source,target,ignore=ignore);assert (target/'SKILL.md').is_file();print('Skill files installed at '+str(target));print('Restart/reload your coding tool, then check its skill list. A copied directory is not proof the running session has reloaded it.')
