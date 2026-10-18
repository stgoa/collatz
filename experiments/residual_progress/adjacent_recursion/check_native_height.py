"""Bounded implementation audit for the complete native-height separation."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import native_height as M

HERE=Path(__file__).resolve().parent


def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def absorb(seed,step_cap=10000,bit_cap=512):
    x,current=seed,{}
    for _ in range(step_cap+1):
        if x==1:
            assert M.divergence(current)==M.atoms((1,seed))
            return current
        if x in current or len(current)>=step_cap or x.bit_length()>bit_cap:
            raise RuntimeError('Unresolved capped fixture discovery')
        current[x]=1;x=M.NORMAL.step(x)
    raise AssertionError('Unreachable')


def words(depth):
    frontier=[(31,[])];result=[]
    for _ in range(depth):
        new=[]
        for target,word in frontier:
            for kind in M.C.BASES[target%3]:
                for index in ((0,) if kind=='point' else (0,1)):
                    x,_,_=M.C.inverse_step(target,kind,index)
                    child=word+[(kind,index)]
                    new.append((x,child));result.append(child)
        frontier=new
    return result


def audit():
    anchor=M.verify_anchor()
    for origin in anchor['quotient_edges']:
        x=origin
        for _ in range(6):
            if x==1:break
            x=anchor['quotient_edges'][x]
        assert x==1
    assert 2**62>3**39
    inverse=[]
    for depth in (3,4,5):
        q=M.family(depth)['q']
        for word in words(depth):
            data=M.shadow_word(q,word)
            inverse.append([depth,data['word'],data['rows'][-1]])
    large_rays=[]
    for index in (8,32,128):
        q=M.family(16)['q'];target=31;word=[]
        for i in range(8):
            kind='ray0' if i%2==0 else 'ray1'
            target,_,_=M.C.inverse_step(target,kind,index)
            word.append((kind,index))
        data=M.shadow_word(q,word)
        large_rays.append(data)

    binary=[];undo=[]
    for a in range(2,17):
        t3=(5*pow(2,-a,27))%27
        t0=t3+27*(((-3**a-t3)*pow(27,-1,4))%4)
        for index in range(8):
            t=t0+108*index;q=2**a*t-1
            data=M.paired_run(q)
            assert data['a']==a
            binary.append([q,a,data['lower'],data['upper'],digest(data['current'])])
            old=M.transported_undo((2*q+1)//3)
            undo.append([old['seed'],digest(old['current']),sorted(old['coefficients'].items())])

    family=[]
    for depth in list(range(3,25))+[64,128]:
        for index in (1,2):
            data=M.family(depth,index);plan=M.forward_plan(data['q'])
            y=plan['negative']['endpoint'];n=plan['height']
            assert y==23+2*3**(depth+35)*index
            assert 8*n-(9*y+5)==4+2*3**(depth-2)*index*(2**62-3**39)
            family.append(dict(parameters=data,requests=sorted(plan['coefficients'].items()),
                               rows=len(plan['current']),current_hash=digest(plan['current'])))

    examples=[];cache={}
    for q in (31,M.family(3)['q']):
        plan=M.forward_plan(q);supplied={}
        for u in plan['coefficients']:
            if u not in cache:
                cache[u]=M.combine((1,absorb(3*u)),(-1,absorb(u)))
            supplied[u]=cache[u]
        current=M.compile_plan(plan,supplied)
        assert M.divergence(current)==M.ADJ.adjacent_source(q)
        examples.append(dict(plan=plan,supplied=supplied,current=current,rows=len(current)))

    first=examples[-1]['plan']
    assert first['coefficients']
    bad=dict(first,height=first['height']+1)
    rejections=0
    for action in (lambda:M.family(2),lambda:M.family(3,0),
                   lambda:M.forward_plan(139),
                   lambda:M.shadow_word(139,[('ray0',0)]*8),
                   lambda:M.shadow_word(M.family(3)['q'],[('point',0)]),
                   lambda:M.validate_plan(bad),
                   lambda:M.compile_plan(first,{}),
                   lambda:M.compile_plan(first,{u:{} for u in first['coefficients']}),
                   lambda:absorb(3,step_cap=0)):
        try:action()
        except (ValueError,RuntimeError):rejections+=1
        else:raise AssertionError('Malformed or missing premise accepted')
    return dict(status='PASS',scope='All-ray native-height separation on varying seeds; conditional forward currents only',
                anchor=anchor,inverse_word_cases=len(inverse),inverse_hash=digest(inverse),
                ray_index_samples=large_rays,paired_run_cases=len(binary),paired_run_hash=digest(binary),
                exact_transport_undos=len(undo),transport_undo_hash=digest(undo),
                family_cases=family,stored_conversions=examples,distinct_supplied_pairs=len(cache),
                rejections=rejections,caps=dict(fixture_steps=10000,fixture_bits=512,tree_depth=5,tree_ray_indices=[0,1]),
                source_hashes={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                               for name in ('native_height.py','check_native_height.py')})


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--write-receipt',action='store_true')
    args=parser.parse_args();result=json.loads(json.dumps(audit(),sort_keys=True))
    path=HERE/'native_height_audit.json'
    if args.write_receipt:path.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    else:assert json.loads(path.read_text())==result,'Receipt differs; inspect before regenerating'
    print('PASS: adjacent native-height inverse barrier, fixed forward current and exact returning undo')


if __name__=='__main__':main()
