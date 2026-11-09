#!/usr/bin/env python3
"""Validate this documentation/tooling package, not a newly rendered short."""
from pathlib import Path
import ast,json,re,hashlib
import yaml
root=Path(__file__).resolve().parents[1];issues=[];counts={'json':0,'markdown':0,'python':0,'local_markdown_links':0}
for f in root.rglob('*'):
 if not f.is_file() or any(x in {'.git','.venv','node_modules','__pycache__','.private-study'} for x in f.relative_to(root).parts):continue
 if f.relative_to(root).parts[0]!='videos' and f.suffix.lower() in {'.mp4','.mov','.mkv','.webm','.avi','.mp3','.wav','.jpg','.jpeg','.png','.webp','.zip'}:issues.append('Reference/media artifact must not be in published package: '+str(f.relative_to(root)))
 if f.suffix=='.json':json.loads(f.read_text());counts['json']+=1
 if f.suffix=='.py':ast.parse(f.read_text(),filename=str(f));counts['python']+=1
 if f.suffix=='.md':
  text=f.read_text();counts['markdown']+=1
  if '/tmp/clip-scout-study' in text or '/workspace/' in text:issues.append('Nonportable private path: '+str(f.relative_to(root)))
  for target in re.findall(r'\]\(([^\n)]+)\)',text):
   target=target.strip().strip('<>')
   if re.match(r'^[a-z]+:',target,re.I) or target.startswith('#'):continue
   path=target.split('#',1)[0]
   if path and not (f.parent/path).exists():issues.append(f'Broken link: {f.relative_to(root)} -> {target}')
   counts['local_markdown_links']+=1
text=(root/'SKILL.md').read_text();front=yaml.safe_load(text.split('---',2)[1]);assert front['name']=='cartoon-3d-short-v2' and front['description'];assert 'ALL CAPS' in text and 'Arial' in text and 'white only' in text
assert 'Copyright (c) 2026 Mr omi' in (root/'LICENSE').read_text()
inv=json.loads((root/'analysis/metrics/inventory.json').read_text());assert len(inv['videos'])==7;assert sum(v['decoded_frames'] for v in inv['videos'])==12488;assert sum(v['private_sheets'] for v in inv['videos'])==212
for v in inv['videos']:assert v['native_fps']=='30/1' and (v['width'],v['height'])==(360,640)
verification=json.loads((root/'analysis/verification.json').read_text());assert verification['status']=='passed' and verification['total_frames']==12488
manifest=json.loads((root/'analysis/baseline-manifest.json').read_text())
for file,digest in manifest['files'].items():assert hashlib.sha256((root/file).read_bytes()).hexdigest()==digest,file
assert not issues,'\n'.join(issues)
print(json.dumps({'status':'passed','scope':'skill/documentation/scripts/source-study package, not a newly rendered episode','counts':counts,'videos':7,'native_frames':12488,'private_contact_sheets_generated':212,'inherited_bridge_files_verified':len(manifest['files'])},indent=2))
