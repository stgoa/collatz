"""Bounded exact audit of the complete immediate lower-loop classification."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import random
from types import ModuleType
import lower_loop as M

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def direct(rows):
    answer = Counter()
    for x, c in rows.items():
        value = 3*x+1
        y = value//(value & -value)
        answer[x] += c
        if y != 1:
            answer[y] -= c
    return {x:c for x,c in answer.items() if c and x != 1}


def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def sources():
    pending, seen, paths = [M], set(), {Path(__file__).resolve(), HERE/'LOWER_LOOP_SCOPE.md'}
    while pending:
        module = pending.pop()
        if id(module) in seen:
            continue
        seen.add(id(module))
        name = getattr(module,'__file__',None)
        if not name:
            continue
        p = Path(name).resolve()
        if not p.is_relative_to(ROOT):
            continue
        paths.add(p)
        pending.extend(x for x in vars(module).values() if isinstance(x,ModuleType))
    return {str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)}


def audit():
    cases = []
    for i in range(1500):
        u = 21+72*i
        if M.B.SIGMA.RETURN.returning(u):
            cases.append(u)
    rng = random.Random(751453)
    for bits in (64,128,256):
        group = []
        while len(group)<48:
            u = 21+72*rng.getrandbits(bits)
            if M.B.SIGMA.RETURN.returning(u):
                group.append(u)
        cases.extend(group)
    counts = Counter()
    rows = []
    for u in cases:
        data = M.classify(u)
        counts['nonzero' if data['nonzero'] else 'zero'] += 1
        expected = {}
        for v,c in data['lower_coefficients'].items():
            expected = M.B.combine((1,expected),(-c,{3*v:1,v:-1}))
        assert direct(data['current']) == expected
        if data['nonzero']:
            v = data['target']
            assert v%32==25 and data['nine_parent']==8*v+1
            assert M.B.nine_candidate(v)['status']=='descending'
            plan = data['oriented_plan']
            expected = {3*v:1,v:-1}
            for w,c in plan['coefficients'].items():
                expected = M.B.combine((1,expected),(-c,{3*w:1,w:-1}))
            assert direct(plan['current'])==expected
        else:
            assert data['current']=={} and data['lower_coefficients']=={}
        rows.append([u,data['nonzero'],digest(sorted(data['current'].items())),digest(sorted(data['lower_coefficients'].items()))])
    progression = [M.classify(453+576*i) for i in range(64)]
    assert all(x['nonzero'] for x in progression)
    example=M.classify(453)
    assert example['nine_parent']==201 and example['lower_coefficients']=={5:1,25:1}
    assert len(example['current'])==14
    rejected=0
    for bad in (0,-3,True,5,9,165):
        try:
            M.classify(bad)
        except (ValueError,TypeError):
            rejected+=1
        else:
            raise AssertionError('Invalid returning input accepted')
    return dict(status='PASS',cases=len(cases),classification=dict(counts),progression_boundaries=len(progression),
                rejected=rejected,cases_hash=digest(rows),example=example,sources=sources(),
                scope='Immediate R75 self-loop only; nonzero orientations reuse an already accepted W9 domain.')


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--write-receipt',action='store_true');args=parser.parse_args()
    result=audit();path=HERE/'lower_loop_audit.json'
    serialized=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if args.write_receipt:path.write_text(serialized)
    else:assert json.loads(path.read_text())==json.loads(serialized),'Persisted receipt differs'
    print(json.dumps({k:v for k,v in result.items() if k not in ('example','sources')},sort_keys=True))

if __name__=='__main__':main()
