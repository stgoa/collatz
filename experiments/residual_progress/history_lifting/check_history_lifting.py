"""Independent bounded replay of complete fixed-word history lifting."""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from types import ModuleType
import history_lifting as M

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SECOND = M.load('history_lift_second', 'returning_continuation/returning_continuation.py')


def rows(data):
    return [[x, c] for x, c in sorted(data.items())]


def digest(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def direct_prefix(x, word):
    out = Counter()
    for a in word:
        y = 3*x+1
        actual = (y & -y).bit_length()-1
        if actual != a:
            return None
        if x != 1:
            out[x] += 1
        x = y>>actual
    return x, dict(out)


def direct_divergence(current):
    out = Counter()
    for x, c in current.items():
        assert type(x) is int and x > 1 and x % 2 and type(c) is int and c
        y = 3*x+1
        y //= y & -y
        out[x] += c
        if y != 1:
            out[y] -= c
    return {x: c for x, c in out.items() if c}


def check(plan):
    expected = {3*plan['seed']: 1, plan['seed']: -1}
    for v, c in plan['coefficients'].items():
        expected = M.combine((1, expected), (-c, {3*v: 1, v: -1}))
    assert direct_divergence(plan['current']) == expected
    M.BASIS.validate(plan)


def rejected(action):
    try:
        action()
    except ValueError:
        return
    raise AssertionError('Expected rejection')


def supplied_pair(w):
    def path(x):
        out = {}
        while x != 1:
            if x in out or len(out) >= 10000 or x.bit_length() > 4096:
                raise RuntimeError('Designated fixture exceeded finite discovery caps')
            out[x] = 1
            y = 3*x+1
            x = y//(y & -y)
        return out
    current = M.combine((1, path(3*w)), (-1, path(w)))
    assert direct_divergence(current) == {3*w: 1, w: -1}
    return current


def demo(plan, stored=None):
    supply = ({v: supplied_pair(v) for v in plan['coefficients']} if stored is None else
              {int(v): dict(c) for v, c in stored['supplied'].items()})
    assert set(supply) == set(plan['coefficients'])
    for v, c in supply.items():
        assert direct_divergence(c) == {3*v: 1, v: -1}
    current = M.compile_plan(plan, supply)
    assert direct_divergence(current) == {3*plan['seed']: 1, plan['seed']: -1}
    rejected(lambda: M.compile_plan(plan, {}))
    bad = dict(supply);bad[next(iter(bad))] = {}
    rejected(lambda: M.compile_plan(plan, bad))
    bad = dict(supply);bad[next(iter(bad))] = {3: True}
    rejected(lambda: M.compile_plan(plan, bad))
    return dict(seed=plan['seed'], rank=plan['rank'], plan_current=rows(plan['current']),
                coefficients=rows(plan['coefficients']), current=rows(current),
                current_rows=len(current), current_hash=digest(rows(current)),
                supplied={str(v): rows(c) for v, c in sorted(supply.items())})


def sources():
    pending, seen = [M, SECOND], set()
    paths = {Path(__file__).resolve(), HERE/'HISTORY_LIFTING.md'}
    while pending:
        module = pending.pop()
        if id(module) in seen:
            continue
        seen.add(id(module))
        file = getattr(module, '__file__', None)
        if not file:
            continue
        path = Path(file).resolve()
        if not path.is_relative_to(ROOT):
            continue
        paths.add(path)
        pending.extend(v for v in vars(module).values() if isinstance(v, ModuleType))
    return {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)}


def audit(stored=None):
    specs = [M.NATIVE,
        M.make_spec(739, 725, (1,8), (7,2)),
        M.make_spec(725, 739, (7,2), (1,8)),
        M.make_spec(21, 19, (6,), (1,3,1,2,3,4)),
        M.make_spec(13, 3, (3,), (1,)),
        M.make_spec(3, 5, (1,4), (4,)),
        M.make_spec(5, 3, (), (1,)),
        M.make_spec(3, 5, (1,), ()),
        M.make_spec(13, 13, (3,), (3,))]
    # Reanchoring must retain the complete cell, including its negative indices.
    for spec in list(specs):
        lifted = M.lift(spec, 3)
        specs.append(M.make_spec(lifted['q'],lifted['p'],spec['upper_word'],spec['lower_word']))
    generic = []
    membership = []
    for spec in specs:
        lam = Fraction(*spec['slope']);delta = Fraction(*spec['intercept'])
        allowed = spec['smaller_indices']
        for k in range(-4,9):
            q,p = spec['q0']+spec['q_period']*k,spec['p0']+spec['p_period']*k
            interval = (not allowed['empty'] and k >= allowed['minimum'] and
                        (allowed['maximum'] is None or k <= allowed['maximum']))
            assert interval == (min(q,p)>0 and p<q)
            if min(q,p)<=0:
                rejected(lambda:M.lift(spec,k))
                continue
            data = M.lift(spec,k)
            left,right = direct_prefix(q,spec['upper_word']),direct_prefix(p,spec['lower_word'])
            assert left is not None and right is not None and left[0]==right[0]
            assert direct_divergence(data['current']) == M.atoms((1,q),(-1,p))
            assert p == lam*q+delta and data==M.recover(spec,q)
            generic.append([q,p,k,data['smaller'],digest(rows(data['current']))])
        step=2**(spec['upper_affine']['total']+1)
        ternary=spec['q_period']//step
        # Offset necessity is checked independently through the affine equations.
        for j in sorted(set(range(32))|{ternary-1,ternary,ternary+1,2*ternary}):
            q=spec['q0']+step*j;p=lam*q+delta
            valid=p.denominator==1 and p>0
            if valid:
                p=p.numerator
                left,right=direct_prefix(q,spec['upper_word']),direct_prefix(p,spec['lower_word'])
                valid=left is not None and right is not None and left[0]==right[0]
            assert valid==(j%ternary==0)
            if valid:assert M.recover(spec,q)['p']==p
            else:rejected(lambda:M.recover(spec,q))
            membership.append([spec['q0'],j,valid])
    assert specs[1]['slope']==[1,1] and specs[1]['uniformly_smaller_for_nonnegative_indices']
    assert specs[3]['slope']==[256,243] and specs[3]['smaller_indices']==dict(minimum=0,maximum=0,empty=False)

    indices=set(range(128))|{512*j for j in range(32)}|{3072+4096*j for j in range(32)}
    indices|={2**64+3,2**128+3,512*2**128,3072+4096*2**128}
    native,phases,old=[],[],[]
    for k in sorted(indices):
        plan=M.native_plan(k);check(plan)
        data=plan['parameters'];q,p=data['q'],data['p']
        assert q-p==156+114448*k
        assert max(map(M.rho,plan['coefficients']),default=0)<q
        x=q
        for _ in range(1):x=M.N.quotient_step(x)
        y=p
        for _ in range(13):y=M.N.quotient_step(y)
        assert x==y==data['quotient_meeting']
        phase=M.blocked_phase(k)
        local=M.BASIS.nine_candidate(data['seed'])
        assert phase['blocked']==(local['status']!='descending')
        native.append([k,rows(plan['coefficients']),digest(rows(plan['current']))])
        phases.append(phase)
        if k%512==0:
            fdata=M.old_failure_phase(k)
            if fdata['genuine_old_higher_request']:
                u,v=fdata['returning'],fdata['leading']
                a,b=SECOND.OLD.forward_plan(u),SECOND.continuation_plan(u)
                assert a['status']==b['status']=='unresolved'
                assert a['coefficients'][v]==b['coefficients'][v]==1
                assert M.rho(v)>M.rho(u)>q
            if k%4096==3072:
                assert fdata['genuine_old_higher_request'] and k%8192!=0
            old.append(fdata)
    demos=[demo(M.native_plan(k),None if stored is None else stored['demonstrations'][i])
           for i,k in enumerate((0,1,3072))]
    bad_spec=dict(M.NATIVE,q_period=M.NATIVE['q_period']//2)
    invalid=[lambda:M.make_spec(True,3,(1,),(1,)),
         lambda:M.make_spec(13,3,(True,),(1,)),
         lambda:M.make_spec(13,3,(1,),(1,)),
         lambda:M.make_spec(13,5,(3,),(4,)),
         lambda:M.affine((0,)),lambda:M.prefix(-3,(1,)),
         lambda:M.lift(bad_spec,0),lambda:M.lift(M.NATIVE,True),
         lambda:M.lift(M.NATIVE,-1),lambda:M.recover(M.NATIVE,11549),
         lambda:M.recover(M.NATIVE,True),lambda:M.native_plan(-1),
         lambda:M.native_plan(True),lambda:M.critical_plan(9,M.NATIVE,0),
         lambda:M.critical_plan(3849,specs[3],1),
         lambda:M.critical_plan(3849,M.make_spec(11547,46189,(1,),(3,)),0),
         lambda:M.old_failure_phase(1),lambda:M.old_failure_phase(True)]
    for action in invalid:rejected(action)
    plan=M.native_plan(0)
    bad=dict(plan,current={**plan['current'],3:True})
    rejected(lambda:M.compile_plan(bad,{}))
    return dict(status='PASS',scope='Exact fixed-word cells and conditional original-rank supply; no universal hitting',
                specifications=specs,generic_lifts=len(generic),generic_hash=digest(generic),
                membership_cases=len(membership),membership_hash=digest(membership),
                native_cases=len(native),native_hash=digest(native),blocked_phases=phases,
                old_failure_phases=old,demonstrations=demos,rejections=len(invalid)+1,
                caps=dict(fixture_arrows=10000,fixture_bits=4096),source_hashes=sources())


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true')
    args=parser.parse_args();path=HERE/'history_lifting_audit.json'
    stored=None if args.write else json.loads(path.read_text())
    result=audit(stored);text=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if args.write:path.write_text(text)
    else:assert text==path.read_text(),'Receipt mismatch; investigate before regenerating'
    print('PASS: fixed-word lifting; %d specs,%d lifts,%d exact-membership cases,%d native plans,%d supplied outputs' %
          (len(result['specifications']),result['generic_lifts'],result['membership_cases'],
           result['native_cases'],len(result['demonstrations'])))


if __name__=='__main__':main()
