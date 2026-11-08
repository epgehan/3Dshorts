#!/usr/bin/env python3
"""Decode every native frame; keep reference pixels private, publish measurements only."""
from pathlib import Path
import argparse, csv, hashlib, json, subprocess, math, time, re
from fractions import Fraction
import cv2
import numpy as np
from PIL import Image, ImageDraw

def probe(path):
    return json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(path)]))

def pts_list(path):
    data=json.loads(subprocess.check_output(['ffprobe','-v','error','-select_streams','v:0','-show_frames','-show_entries','frame=best_effort_timestamp_time','-of','json',str(path)]))
    return [float(f['best_effort_timestamp_time']) for f in data['frames']]

def tc(frame, fps=30):
    n=frame; return f'{n//(fps*3600):02d}:{n//(fps*60)%60:02d}:{n//fps%60:02d}:{n%fps:02d}'

def sheet(files, output, columns=6, thumb=(120,214), heading=''):
    if not files:return
    tw,th=thumb;rows=math.ceil(len(files)/columns);im=Image.new('RGB',(columns*tw,rows*(th+18)+30),'#171925');draw=ImageDraw.Draw(im);draw.text((6,6),heading,fill='white')
    for i,f in enumerate(files):
        x=(i%columns)*tw;y=(i//columns)*(th+18)+30
        with Image.open(f) as pic:im.paste(pic.resize((tw,th)),(x,y))
        idx=int(f.stem);draw.text((x+2,y+th+2),f'f{idx:05d} {idx/30:.3f}s',fill='white')
    im.save(output,quality=90)

def affine(prev,gray):
    mask=np.zeros_like(prev);mask[10:int(prev.shape[0]*.72),8:-8]=255
    p=cv2.goodFeaturesToTrack(prev,maxCorners=110,qualityLevel=.025,minDistance=7,mask=mask)
    if p is None or len(p)<10:return None
    q,status,err=cv2.calcOpticalFlowPyrLK(prev,gray,p,None,winSize=(17,17),maxLevel=2)
    if q is None:return None
    valid=status.ravel()==1; a=p[valid].reshape(-1,2);b=q[valid].reshape(-1,2)
    if len(a)<10:return None
    M,inliers=cv2.estimateAffinePartial2D(a,b,method=cv2.RANSAC,ransacReprojThreshold=1.6,maxIters=500)
    if M is None:return None
    return [float(M[0,2]),float(M[1,2]),float(np.hypot(M[0,0],M[1,0])),float(np.degrees(np.arctan2(M[1,0],M[0,0]))),float(inliers.mean()),len(a)]

def analyze(path,slug,out,private,overwrite=False):
    assert re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]{0,63}',slug),'Use a simple unique source ID, not a path.'
    cv2.setNumThreads(1);meta=probe(path);v=next(s for s in meta['streams'] if s['codec_type']=='video');fps=float(Fraction(v['avg_frame_rate']));assert abs(fps-30)<1e-5,'This study expects native30fps; do not silently interpolate.'
    points=pts_list(path);n_expected=len(points);folder=private/slug;frames=folder/'frames';sheets=folder/'sheets';frames.mkdir(parents=True,exist_ok=True);sheets.mkdir(exist_ok=True)
    existing=list(frames.glob('*.jpg'))+list(sheets.glob('*.jpg'))
    if existing and not overwrite:raise RuntimeError(f'Private exports already exist for {slug}; choose a fresh output or explicitly pass --overwrite.')
    if overwrite:
        for old in existing:
            if old.parent==frames and old.stem.isdigit():old.unlink()
            elif old.parent==sheets and old.name.startswith('frames-'):old.unlink()
        for old in folder.glob('cuts-*.jpg'):old.unlink()
    cap=cv2.VideoCapture(str(path));rows=[];previous=None;prev_hist=None;prev_small=None;cuts=[];all_hist=np.zeros((16,16,16),dtype=np.int64);index=0;started=time.monotonic()
    columns=['frame','pts_seconds','timecode_30fps','image','y_mean','y_p05','y_median','y_p95','saturation_mean','ink_fraction_proxy','laplacian_variance','delta_visual_top','delta_caption_bottom','hist_distance_top','flow_dx_halfres','flow_dy_halfres','flow_scale','flow_rotation_deg','flow_inlier_ratio','flow_track_count','decoded_rgb_sha256']
    while True:
        ok,bgr=cap.read()
        if not ok:break
        assert index<n_expected;rgb=cv2.cvtColor(bgr,cv2.COLOR_BGR2RGB);small=cv2.resize(bgr,(180,320),interpolation=cv2.INTER_AREA);gray=cv2.cvtColor(small,cv2.COLOR_BGR2GRAY);hsv=cv2.cvtColor(small,cv2.COLOR_BGR2HSV)
        # Whole-frame display-referred Rec.709 luma proxy; not linear luminance or lighting energy.
        f=rgb.astype(np.float32)/255;y=f[:,:,0]*.2126+f[:,:,1]*.7152+f[:,:,2]*.0722;percent=np.percentile(y,[5,50,95])
        quant=(rgb[::4,::4]//16).reshape(-1,3);np.add.at(all_hist,(quant[:,0],quant[:,1],quant[:,2]),1)
        hist=cv2.calcHist([hsv[:230]],[0,1],None,[24,16],[0,180,0,256]);cv2.normalize(hist,hist)
        top=bottom=hd=0.;motion=None
        if previous is not None:
            diff=cv2.absdiff(gray,previous).astype(np.float32)/255;top=float(diff[:230].mean());bottom=float(diff[230:].mean());hd=float(cv2.compareHist(prev_hist,hist,cv2.HISTCMP_BHATTACHARYYA));motion=affine(previous,gray)
            # Candidates only: flashes, fast object movement and dissolves can trigger these.
            if (top>.13 and hd>.20) or hd>.56:cuts.append({'frame':index,'time':points[index],'top_delta':top,'hist_distance':hd,'kind':'candidate_requires_visual_review'})
        file=frames/f'{index:06d}.jpg';assert cv2.imwrite(str(file),bgr,[cv2.IMWRITE_JPEG_QUALITY,93])
        rec=[index,round(points[index],6),tc(index),f'frames/{index:06d}.jpg',float(y.mean()),*map(float,percent),float(hsv[:,:,1].mean()/255),float((y<.12).mean()),float(cv2.Laplacian(gray,cv2.CV_64F).var()),top,bottom,hd]
        rec.extend(motion if motion else ['','','','','','']);rec.append(hashlib.sha256(rgb.tobytes()).hexdigest());rows.append(rec)
        previous=gray;prev_hist=hist;prev_small=small;index+=1
    cap.release();assert index==n_expected,(index,n_expected);assert index==int(v['nb_frames'])
    out.mkdir(parents=True,exist_ok=True)
    with (out/f'{slug}.frames.csv').open('w',newline='') as f:
        writer=csv.writer(f,lineterminator="\n");writer.writerow(columns);writer.writerows(rows)
    # Collapse clusters to the largest visual discontinuity in an8-frame neighborhood.
    groups=[]
    for c in cuts:
        if groups and c['frame']-groups[-1][-1]['frame']<=8:groups[-1].append(c)
        else:groups.append([c])
    boundaries=[max(g,key=lambda c:c['top_delta']+c['hist_distance']) for g in groups]
    # Private contact sheets cover ALL decoded frames,60 consecutive frames per sheet.
    for start in range(0,index,60):
        files=[frames/f'{i:06d}.jpg' for i in range(start,min(start+60,index))];sheet(files,sheets/f'frames-{start:06d}-{min(start+59,index-1):06d}.jpg',columns=10,thumb=(90,160),heading=f'{slug}: every native frame, {start/30:.2f}s onward')
    sampled=sorted(set([0,index-1,*range(30,index,90)]));sheet([frames/f'{i:06d}.jpg' for i in sampled],folder/'overview.jpg',heading=f'{slug}: overview;3s sampling')
    keyframes=sorted(set([0,index-1,*[c['frame'] for c in boundaries],*[min(index-1,c['frame']+12) for c in boundaries]]))
    for start in range(0,len(keyframes),24):sheet([frames/f'{i:06d}.jpg' for i in keyframes[start:start+24]],folder/f'cuts-{start//24:02d}.jpg',heading=f'{slug}: candidate transitions /12frames later')
    array=np.asarray([r[4:14] for r in rows],dtype=float);palette=[]
    for flat in np.argsort(all_hist.ravel())[-12:][::-1]:
        ix=np.unravel_index(flat,all_hist.shape);palette.append({'rgb_bin_center':[int(x*16+8) for x in ix],'pixel_fraction':float(all_hist[ix]/all_hist.sum())})
    measured={'file':path.name,'slug':slug,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'width':v['width'],'height':v['height'],'native_fps':v['avg_frame_rate'],'decoded_frames':index,'video_duration':float(v['duration']),'container_duration':float(meta['format']['duration']),'first_pts':points[0],'last_pts':points[-1],'cadence_max_error_seconds':float(np.max(np.abs(np.diff(points)-1/30))),'full_decode_passed':True,'all_frames_exported':True,'frame_collection_format':'native-sizeJPEGquality93; metrics calculated on decoded sourceRGB before JPEG','private_sheets':math.ceil(index/60),'candidate_transition_count':len(boundaries),'candidate_transitions':boundaries,'metric_summary':{name:{'p05':float(np.percentile(array[:,j],5)),'median':float(np.median(array[:,j])),'p95':float(np.percentile(array[:,j],95))} for j,name in enumerate(columns[4:14])},'rgb_palette_bins':palette,'decode_analysis_seconds':round(time.monotonic()-started,2),'software':{'opencv':cv2.__version__,'numpy':np.__version__},'limits':['Compressed360x640source, no genuine higher-resolution detail recoverable.','Transition candidates and affine feature motion are observations, not authoritative cuts or physical camera parameters.','Caption region mask is coarse; y<72% excludes most but not necessarily all text.','Automatic ink, sharpness and brightness proxies mix subject, set, captions and compression; do not treat as material or lighting measurements.']}
    (out/f'{slug}.summary.json').write_text(json.dumps(measured,indent=2)+'\n');print(json.dumps({'slug':slug,'frames':index,'candidates':len(boundaries),'seconds':measured['decode_analysis_seconds']}),flush=True);return measured

def main():
    a=argparse.ArgumentParser();a.add_argument('--inputs',type=Path,required=True);a.add_argument('--private-output',type=Path,required=True);a.add_argument('--metrics-output',type=Path,required=True);a.add_argument('--only');a.add_argument('--overwrite',action='store_true',help='Replace only generated frame/sheet JPEGs for selected input IDs.');args=a.parse_args();inputs=json.loads(args.inputs.read_text());assert isinstance(inputs,list) and inputs;assert len({x['slug'] for x in inputs})==len(inputs),'Duplicate source IDs';results=[]
    for item in inputs:
        if args.only and item['slug']!=args.only:continue
        results.append(analyze(Path(item['path']),item['slug'],args.metrics_output,args.private_output,args.overwrite))
    by_slug={x['slug']:x for x in results}
    for item in inputs:
        prior=args.metrics_output/f"{item['slug']}.summary.json"
        if item['slug'] not in by_slug and prior.is_file():by_slug[item['slug']]=json.loads(prior.read_text())
    ordered=[by_slug[x['slug']] for x in inputs if x['slug'] in by_slug]
    (args.metrics_output/'inventory.json').write_text(json.dumps({'videos':ordered,'total_frames':sum(x['decoded_frames'] for x in ordered)},indent=2)+'\n')
if __name__=='__main__':main()
