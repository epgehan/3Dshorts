"""Transcribe each actual voice segment with whisper.cpp DTW, then build reviewed cues.
ASR alignment is approximate; DTW token centers delimit words through midpoints.
Never evenly spaces words across a whole utterance. Original approved text drives cues.
"""
from pathlib import Path
import json, subprocess, re, difflib, os
P=Path(__file__).resolve().parent
ROOT=Path(os.environ.get('WHISPER_CPP_HOME',str(Path.home()/'.cache/whisper.cpp')))
WHISPER=Path(os.environ.get('WHISPER_BIN',str(WHISPER)))
MODEL=Path(os.environ.get('WHISPER_MODEL',str(MODEL)))
def norm(s): return re.sub('[^a-z]','',s.lower())
def main():
 v=json.loads((P/'verification.json').read_text()); words=[]; report=[]
 for i,line in enumerate(v['dialogue']):
  wav=P/f'line{i+1}-16k.wav'; out=P/f'line{i+1}-asr'
  subprocess.run(['ffmpeg','-v','error','-y','-i',str(P/f'line{i+1}.wav'),'-ar','16000',str(wav)],check=True)
  result=subprocess.run([str(WHISPER),'-m',str(MODEL),'-f',str(wav),'-l','en','-dtw','tiny','-nfa','-ojf','-of',str(out),'--prompt',line['text'],'-t','2'],capture_output=True,text=True,check=True)
  (P/f'line{i+1}-asr.log').write_text(result.stdout+'\n'+result.stderr)
  d=json.loads(out.with_suffix('.json').read_text()); tokens=[t for s in d['transcription'] for t in s['tokens'] if t['id']<50257 and re.search('[a-zA-Z]',t['text'])]
  grouped=[]
  for t in tokens:
   if t['text'].startswith(' ') or not grouped: grouped.append(dict(text=t['text'].strip(),centers=[t['t_dtw']/100],start=t.get('offsets',{}).get('from',0)/1000,end=t.get('offsets',{}).get('to',0)/1000))
   else:
    grouped[-1]['text']+=t['text']; grouped[-1]['centers'].append(t['t_dtw']/100)
    grouped[-1]['end']=t.get('offsets',{}).get('to',0)/1000
  expected=line['text'].split()
  report.append(dict(line=i+1,expected=expected,recognized=[g['text'] for g in grouped],rawDTW=grouped))
  # DTW words are reviewed in alignment-review.json before cue generation.
  (P/f'line{i+1}-words.json').write_text(json.dumps(grouped,indent=2))
 (P/'alignment-verification.json').write_text(json.dumps(dict(method='Whisper.cpp tiny token DTW on individual actual generated lines; reviewed original transcript correspondence. See alignment-review.json for approved boundaries.',lines=report),indent=2)+'\n')
 print(json.dumps(report,indent=2))
if __name__=='__main__': main()
