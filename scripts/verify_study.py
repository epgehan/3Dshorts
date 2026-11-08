#!/usr/bin/env python3
"""Verify native-frame coverage, cadence, metric records, and optional private exports."""
from pathlib import Path
import argparse,csv,json,math
from PIL import Image
p=argparse.ArgumentParser();p.add_argument('--metrics',type=Path,required=True);p.add_argument('--private-output',type=Path);p.add_argument('--report',type=Path);a=p.parse_args();inv=json.loads((a.metrics/'inventory.json').read_text());report={'videos':[]};total=0
for v in inv['videos']:
 rows=list(csv.DictReader((a.metrics/(v['slug']+'.frames.csv')).open()));assert len(rows)==v['decoded_frames'];last=-1.;exported=0
 for i,r in enumerate(rows):
  assert int(r['frame'])==i;pts=float(r['pts_seconds']);assert pts>last;last=pts
  assert abs(pts-float(v['first_pts'])-i/30)<.00001;assert len(r['decoded_rgb_sha256'])==64
  assert all(math.isfinite(float(r[k])) for k in ['y_mean','y_p05','y_median','y_p95','delta_visual_top'])
  assert 0<=float(r['y_p05'])<=float(r['y_median'])<=float(r['y_p95'])<=1
  if a.private_output:
   f=a.private_output/v['slug']/r['image'];assert f.is_file()
   with Image.open(f) as im:assert im.size==(v['width'],v['height'])
   exported+=1
 assert abs(v['video_duration']-len(rows)/30)<.0001;total+=len(rows);report['videos'].append({'slug':v['slug'],'frames':len(rows),'native_fps':30,'cadence':'passed','coverage':'passed','private_exports_verified':exported})
assert total==inv['total_frames'];report.update(total_frames=total,status='passed',source_resolution_note='360x640 source;30fps study adds no genuine higher-resolution detail.');text=json.dumps(report,indent=2)+'\n'
if a.report:a.report.write_text(text)
print(text)
