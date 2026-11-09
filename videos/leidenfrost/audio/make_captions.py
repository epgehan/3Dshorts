"""Regenerate captions from actual generated audio's reviewed ASR/DTW word evidence."""
from pathlib import Path
import json,re
P=Path(__file__).resolve().parent
# Word groups are phrase choices, not independent onset estimates.
GROUPS=[[[0],[1,2,3],[4,5]],[[0,1,2],[3,4,5]],[[0,1,2],[3,4,5],[6,7,8],[9,10],[11,12],[13,14,15]],[[0,1,2],[3],[4]]]
def norm(s): return re.sub('[^a-z]','',s.lower())
def main():
 v=json.loads((P/'verification.json').read_text()); words=[]; cues=[]; review=[]
 for i,line in enumerate(v['dialogue']):
  observed=json.loads((P/f'line{i+1}-words.json').read_text()); expected=line['text'].split()
  assert [norm(w) for w in expected]==[norm(x['text']) for x in observed], (expected,observed)
  # Neighboring DTW centers bracket boundaries. First onset uses ASR offset.
  # The isolated WAIT and the sentence break after STEAM retain real pauses.
  bounds=[max(0,observed[0]['start'])]
  for a,b in zip(observed,observed[1:]): bounds.append((a['centers'][-1]+b['centers'][0])/2)
  bounds.append(line['duration'])
  local=[]
  for j,text in enumerate(expected):
   start=max(0,bounds[j]); end=min(line['duration'],bounds[j+1])
   if i==0 and j==0: end=min(end,observed[j]['centers'][-1]+.15)
   if i==0 and j==1: start=max(start,observed[j]['start'])
   if i==2 and j==10: end=min(end,observed[j]['centers'][-1]+.15)
   if i==2 and j==11: start=max(start,observed[j]['start'])
   assert end>start,(i,j,start,end)
   w=dict(text=text,start=round(line['start']+start,4),end=round(line['start']+end,4),speaker=line['speaker'])
   words.append(w);local.append(w)
  for group in GROUPS[i]:
   cues.append(dict(startFrame=round(local[group[0]]['start']*30),endFrame=round(local[group[-1]]['end']*30),text=' '.join(local[j]['text'] for j in group).upper()))
  review.append(dict(line=i+1,recognizedExact=True,words=local))
 assert all(a['endFrame']<=b['startFrame'] for a,b in zip(cues,cues[1:]))
 result=dict(fps=30,durationFrames=450,style=dict(fontFamily='Arial',fontWeight='bold',fill='#ffffff',stroke='#000000',case='ALL CAPS'),rounding='Round each absolute second boundary once to nearest 30fps frame; intervals are half-open [startFrame,endFrame).',timingMethod='Whisper.cpp tiny token DTW on each actual voice stem; adjacent token centers bracket word boundaries, with onset offsets and sentence pauses retained. Approximate model alignment, not manually auditioned word onsets.',cues=cues,words=words)
 (P.parent/'captions.json').write_text(json.dumps(result,indent=2)+'\n')
 (P/'alignment-review.json').write_text(json.dumps(dict(method=result['timingMethod'],review='All four recognized word sequences exactly match the approved original transcript. Group boundaries inspected against DTW tokens and actual segment durations; no uniformly spaced word estimates. Word boundaries remain approximate, especially function words.',lines=review),indent=2)+'\n')
 print(json.dumps(cues,indent=2))
if __name__=='__main__':main()
