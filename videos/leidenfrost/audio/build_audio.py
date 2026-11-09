"""Original synthetic dialogue/SFX. Run with PYTHONPATH=/tmp/leidenfrost-deps.
Requires kokoro-onnx 0.6.1, numpy, scipy, soundfile; ffmpeg/ffprobe;
Kokoro v1.0 ONNX and voices-v1.0.bin in /tmp/leidenfrost-models.
ASR alignment is a separate reviewed pass; see align_captions.py.
"""
from pathlib import Path
import json, subprocess, os, re
os.environ.setdefault('OMP_NUM_THREADS','2')
import numpy as np
import soundfile as sf
from scipy.signal import resample_poly, butter, sosfilt
from kokoro_onnx import Kokoro
P=Path(__file__).resolve().parent
MODEL=Path(os.environ.get('KOKORO_MODELS','/tmp/leidenfrost-models'))
SR=48000
LINES=[
 dict(speaker='Mia',voice='af_heart',start=.35,slotEnd=3,text='Wait. Why is that water skating?',speed=.95),
 dict(speaker='Leo',voice='am_michael',start=3.15,slotEnd=6,text='It is like a tiny hovercraft.',speed=.98),
 dict(speaker='Leo',voice='am_michael',start=6.12,slotEnd=12,text='The hot pan turns the bottom of the drop into steam. The rest floats on it.',speed=.96),
 dict(speaker='Leo',voice='am_michael',start=12.15,slotEnd=15,text='That is the Leidenfrost effect.',speed=.98)]
def run(args):
 return subprocess.run(args,check=True,capture_output=True,text=True)
def main():
 k=Kokoro(str(MODEL/'kokoro-v1.0.onnx'),str(MODEL/'voices-v1.0.bin'))
 speech=np.zeros(SR*15)
 for i,line in enumerate(LINES):
  # Explicit pronunciation respelling is only an input to TTS; transcript remains exact.
  spoken=line['text'].replace('Leidenfrost','Lye-den-frost')
  data,rate=k.create(spoken,voice=line['voice'],speed=line['speed'],lang='en-us')
  raw=P/f'line{i+1}-raw.wav'; sf.write(raw,data,rate)
  available=line['slotEnd']-line['start']-.12
  duration=len(data)/rate
  tempo=max(1.,duration/available)
  out=P/f'line{i+1}.wav'
  run(['ffmpeg','-v','error','-y','-i',str(raw),'-af',f'atempo={tempo},highpass=f=65,afade=t=in:d=0.008,areverse,afade=t=in:d=0.015,areverse','-ar',str(SR),str(out)])
  data,rate=sf.read(out); duration=len(data)/rate
  # Normalize voice RMS per line for intelligible matching between speakers.
  active=data[np.abs(data)>.012]
  rms=np.sqrt(np.mean(active**2)) if len(active) else .1
  data*=.105/rms
  sf.write(out,data,SR,subtype='PCM_24')
  start=round(line['start']*SR); speech[start:start+len(data)]+=data
  line.update(duration=round(duration,6),end=round(line['start']+duration,6),atempo=tempo)
 sf.write(P/'dialogue.wav',speech,SR,subtype='PCM_24')
 # Original seeded procedural sound design, no reference audio.
 rng=np.random.default_rng(83017); sfx=np.zeros(SR*15)
 def add(t,x):
  s=round(t*SR); sfx[s:s+len(x)]+=x[:len(sfx)-s]
 t=np.arange(int(.19*SR))/SR
 zipfx=(np.sin(2*np.pi*(1500*t+3900*t*t))*np.exp(-t*30)+rng.normal(0,.27,len(t))*np.exp(-t*35))*.03
 add(.55,zipfx)
 for start in [.78,1.7,2.55,3.9,5.25,10.75]:
  t=np.arange(int(.45*SR))/SR
  noise=sosfilt(butter(2,[1700,6000],btype='bandpass',fs=SR,output='sos'),rng.normal(size=len(t)))
  add(start,noise*np.sin(np.pi*t/.45)**2*.009)
 t=np.arange(SR*6)/SR
 steam=sosfilt(butter(2,[3000,9500],btype='bandpass',fs=SR,output='sos'),rng.normal(size=len(t)))
 add(6,steam*np.minimum(1,t/.35)*np.minimum(1,(6-t)/.35)*.0035)
 sf.write(P/'sfx.wav',sfx,SR,subtype='PCM_24')
 mix=np.stack([speech+sfx*.95,speech+sfx*1.05],axis=1)
 sf.write(P/'mix-unmastered.wav',mix,SR,subtype='PCM_24')
 args=['ffmpeg','-hide_banner','-i',str(P/'mix-unmastered.wav'),'-af','loudnorm=I=-15:TP=-1.5:LRA=8:print_format=json','-f','null','-']
 result=run(args); measure=json.JSONDecoder().raw_decode(result.stderr[result.stderr.rfind('{'):])[0]
 filt='loudnorm=I=-15:TP=-1.5:LRA=8:linear=true:'+':'.join(f'{a}={measure[b]}' for a,b in [('measured_I','input_i'),('measured_LRA','input_lra'),('measured_TP','input_tp'),('measured_thresh','input_thresh'),('offset','target_offset')])
 run(['ffmpeg','-v','error','-y','-i',str(P/'mix-unmastered.wav'),'-af',filt,'-ar',str(SR),'-ac','2','-t','15','-c:a','pcm_s24le',str(P/'audio.wav')])
 run(['ffmpeg','-v','error','-y','-i',str(P/'audio.wav'),'-c:a','libmp3lame','-b:a','192k',str(P/'audio.mp3')])
 final=run(['ffmpeg','-hide_banner','-i',str(P/'audio.wav'),'-af','loudnorm=I=-15:TP=-1.5:LRA=8:print_format=json','-f','null','-'])
 measured=json.JSONDecoder().raw_decode(final.stderr[final.stderr.rfind('{'):])[0]
 verification=dict(durationSeconds=15,sampleRate=SR,channels=2,dialogue=LINES,integratedLUFS=float(measured['input_i']),truePeakDBTP=float(measured['input_tp']),effects='Original seeded procedural landing zip, glide wisps and quiet steam; no music.',source='Authorized synthetic original dialogue; Kokoro ONNX v1.0; af_heart (female), am_michael (male).',pronunciation='Leidenfrost synthesized with input Lye-den-frost; approved transcript preserved.',alignment='See captions.json and alignment-verification.json. ASR timestamps have model uncertainty.')
 (P/'verification.json').write_text(json.dumps(verification,indent=2)+'\n')
 print(json.dumps(verification,indent=2))
if __name__=='__main__': main()
