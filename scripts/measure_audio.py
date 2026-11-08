#!/usr/bin/env python3
"""Measure complete-program loudness; does not infer isolated voice/music stems."""
import argparse,json,re,subprocess
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--inputs',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();out=[]
for row in json.loads(a.inputs.read_text()):
 r=subprocess.run(['ffmpeg','-hide_banner','-nostats','-i',row['path'],'-vn','-af','ebur128=peak=true','-f','null','-'],capture_output=True,text=True,check=True);summary=r.stderr.rsplit('Summary:',1)[-1]
 def get(pattern):
  m=re.search(pattern,summary);return float(m.group(1)) if m else None
 out.append({'slug':row['slug'],'integrated_lufs':get(r'I:\s+(-?[\d.]+) LUFS'),'loudness_range_lu':get(r'LRA:\s+([\d.]+) LU'),'true_peak_dbfs':get(r'Peak:\s+(-?[\d.]+) dBFS'),'method':'FFmpegEBUR128 complete mixed program, no stem separation'})
a.output.write_text(json.dumps({'measurements':out,'limits':'Mixed-program measurements do not recover narration loudness, speech rate, music/SFX gains or original mix settings.'},indent=2)+'\n');print(json.dumps(out,indent=2))
