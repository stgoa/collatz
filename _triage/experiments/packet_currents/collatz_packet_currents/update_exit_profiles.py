from pathlib import Path
from collections import defaultdict
import json,csv
from certificate import step,source_packets,construct_current
ROOT=Path(__file__).resolve().parent

def exit_profiles(J):
    tags={}
    for source in J:
        path=[];seen=set();y=source
        while y in J and y not in tags:
            if y in seen:raise ValueError('Current graph cycle requires separate handling')
            seen.add(y);path.append(y);y=step(y)[0]
        root,depth=tags[y] if y in tags else (y,0)
        for y in reversed(path):depth+=1;tags[y]=(root,depth)
    profiles=defaultdict(lambda:defaultdict(int))
    for y,w in J.items():
        root,depth=tags[y];profiles[root][depth]+=w
    upper=lower=0;data=[]
    for root,r in profiles.items():
        partial=U=L=0
        for d in sorted(r):partial+=r[d];U=max(U,partial);L=min(L,partial)
        upper+=U;lower+=L
        data.append(dict(exit=root,level_coefficients=[[d,r[d]]for d in sorted(r) if r[d]],uniform_lower=L,uniform_upper=U))
    assert upper<=sum(c for c in J.values() if c>0)
    assert lower>=sum(c for c in J.values() if c<0)
    return lower,upper,sorted(data,key=lambda r:r['exit'])

if __name__=='__main__':
    old=json.loads((ROOT/'certificate_results.json').read_text())
    out=[]
    for row in old['table']:
        N,d=row['N'],row['depth']
        if N in (4096,262144):
            J={int(r['state']):int(r['weight'])for r in csv.DictReader(open(ROOT/f'data/current_{N}.csv'))}
        else:
            pi,*_=source_packets(N,d);J,_=construct_current(pi)
        lower,upper,profiles=exit_profiles(J)
        new={**row,'exit_count':len(profiles),'exit_profile_upper':upper,'exit_profile_lower':lower,'exit_upper_over_N':upper/N}
        out.append(new)
        if N in (4096,262144):(ROOT/f'data/exit_profiles_{N}.json').write_text(json.dumps(profiles,separators=(',',':'))+'\n')
        print(json.dumps({k:new[k]for k in ['N','depth','exit_count','exit_profile_upper','exit_profile_lower','exit_upper_over_N']}))
    (ROOT/'exit_profile_results.json').write_text(json.dumps(out,indent=2)+'\n')
