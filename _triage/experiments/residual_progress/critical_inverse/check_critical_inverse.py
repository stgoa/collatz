"""Bounded verification of the exact phase, composition loop and inverse barrier."""
import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
import critical_inverse as C

HERE = Path(__file__).resolve().parent


def digest(rows):
    return hashlib.sha256(json.dumps(rows, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def finite_absorption(seed, cap=10000):
    """Discovery only for explicitly bounded demonstration inputs."""
    rows, x = {}, seed
    for _ in range(cap+1):
        if x == 1:
            assert C.divergence(rows) == C.atoms((1, seed))
            return rows
        if x in rows or len(rows) == cap or x.bit_length() > 512:
            raise RuntimeError('Unresolved finite input discovery: '+str(seed))
        rows[x] = 1
        x = C.NORMAL.step(x)
    raise AssertionError('Unreachable')


def audit():
    phases = []
    for q in range(13, 32768, 18):
        data = C.phase_bridge(q)
        phases.append([q,data['lower'],data['h'],sorted(data['current'].items())])
    long_phases = []
    for h in list(range(2,17))+[32,64,128]:
        # 3^h*C0=3 modulo4 makes q odd; C0 not0 modulo3 fixes h.
        C0 = 7 if h % 2 == 0 else 1
        q = (3**h*C0-1)//2
        data = C.phase_bridge(q)
        assert data['h'] == h
        long_phases.append([h,q,data['lower'],digest(data['current'])])

    absorption = []
    for seed in range(1, 2048, 2):
        data = C.absorption_five_plan(seed)
        absorption.append([seed,sorted(data['coefficients'].items()),digest(data['current'])])

    plans, counts, good_samples = [], Counter(), []
    for w in range(5, 32768, 8):
        if not C.eligible(w):
            continue
        data = C.phase_pair_plan(w)
        counts[data['status']] += 1
        plans.append([w,data['status'],data['parameters']['h'],
                      data['parameters']['pair_child'],sorted(data['coefficients'].items()),
                      digest(data['current'])])
        if data['status'] == 'descending' and len(good_samples) < 24:
            good_samples.append(w)
    loops = []
    for j in (0,1,2,7,31,127,1023,65535):
        w = 21+2304*j
        data = C.phase_pair_plan(w)
        assert data['status'] == 'self_dependency' and data['coefficients'][w] == 1
        assert C.NORMAL.valuation2(3*w+1) == 6
        loops.append([j,w,data['parameters']['pair_child'],digest(data['current'])])
    first = C.phase_pair_plan(21)
    assert first['current'] == {} and first['coefficients'] == {21:1}
    try:
        C.compile_phase_plan(first,{})
    except ValueError:
        pass
    else:
        raise AssertionError('A self-dependent plan was accepted')

    supplied, examples, tables = {}, [], []
    for w in good_samples:
        data = C.phase_pair_plan(w)
        for u in data['coefficients']:
            if u not in supplied:
                supplied[u] = C.combine((1,finite_absorption(3*u)),(-1,finite_absorption(u)))
        current = C.compile_phase_plan(data,supplied)
        assert C.divergence(current) == C.T.pair_source(w)
        examples.append([w,[[u,c] for u,c in sorted(data['coefficients'].items())],
                         len(current),digest(current)])
        if w in (69,117):
            tables.append(dict(w=w,current=[[x,c] for x,c in sorted(current.items())]))
    assert len(tables) == 2

    affine_rows = []
    for residue,kinds in C.BASES.items():
        for kind in kinds:
            indices = (0,) if kind == 'point' else tuple(range(9))+(32,128,1024)
            for index in indices:
                a,b = C.inverse_affine(residue,kind,index)
                affine_rows.append([residue,kind,index,[a.numerator,a.denominator],
                                    [b.numerator,b.denominator]])

    # Exhaust every branch of a finite ray truncation, then separately check all
    # small possible origins by forward evaluation. The proof covers all rays.
    inverse_rows = []
    for D in range(1,6):
        q = C.critical_witness(D)['target']
        def visit(shadow,word):
            if word:
                row = C.inverse_lift(q,word)
                inverse_rows.append([D,row])
            if len(word) == D:
                return
            for kind in C.BASES[shadow % 3]:
                for index in ((0,) if kind == 'point' else (0,1)):
                    child,_,_ = C.inverse_step(shadow,kind,index)
                    visit(child,word+[(kind,index)])
        visit(1,[])

    direct = []
    for D in range(1,7):
        q = C.critical_witness(D)['target']
        quotient_origins = ordinary_origins = 0
        for p in range(1,q+1,2):
            x = p
            for _ in range(D):
                x = C.NORMAL.step(x)
                assert x != q
            ordinary_origins += 1
            if C.NORMAL.canonical(p):
                x = p
                for _ in range(D):
                    x = C.NORMAL.quotient_step(x)
                    assert x != q
                quotient_origins += 1
        direct.append(dict(D=D,q=q,ordinary_origins=ordinary_origins,
                           canonical_origins=quotient_origins))

    witnesses, long_words = [], []
    for D in (1,2,3,4,8,16,32,64,128):
        for index in (0,1,7):
            witness = C.critical_witness(D,index)
            q,shadow,word = witness['target'],1,[]
            for depth in range(D):
                if shadow % 3 == 2 and depth % 2:
                    kind,index0 = 'point',0
                else:
                    kind,index0 = ('ray0' if depth % 2 else 'ray1'), depth % 3
                shadow,_,_ = C.inverse_step(shadow,kind,index0)
                word.append((kind,index0))
            row = C.inverse_lift(q,word)
            spine = C.inverse_lift(q,[('ray0',0)]*D)
            assert all(r['shadow'] == 1 for r in spine['states'])
            witnesses.append(witness)
            long_words.append([D,index,digest(row),digest(spine)])

    return dict(status='PASS',scope='Whole conditional W5 phase; exact self-loop; exhaustive bounded inverse theorem',
                phase_count=len(phases),phase_hash=digest(phases),long_phase_examples=long_phases,
                absorption_five_plans=len(absorption),absorption_hash=digest(absorption),
                eligible_pair_plans=len(plans),plan_categories=dict(sorted(counts.items())),plan_hash=digest(plans),
                returning_family_examples=loops,actual_pair_examples=examples,actual_pair_tables=tables,
                supplied_pair_count=len(supplied),
                inverse_affine_samples=len(affine_rows),inverse_affine_hash=digest(affine_rows),
                finite_inverse_words=len(inverse_rows),finite_inverse_hash=digest(inverse_rows),
                independent_forward_exhaustions=direct,crt_family_samples=witnesses,long_inverse_words=long_words,
                caps=dict(phase_target_max=32767,absorption_seed_max=2047,phase_pair_max=32767,
                          supplied_pair_examples=24,input_discovery_steps=10000,input_discovery_bits=512,
                          truncated_inverse_depth_max=5,truncated_ray_index_max=1,
                          independent_forward_depth_max=6,long_depth_max=128,
                          affine_ray_indices=list(range(9))+[32,128,1024]),
                source_hashes={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                               for name in ['critical_inverse.py','check_critical_inverse.py']})


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write-receipt',action='store_true')
    args = parser.parse_args()
    result = audit()
    path = HERE/'critical_inverse_audit.json'
    if args.write_receipt:
        path.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    else:
        assert json.loads(path.read_text()) == result,'Receipt differs; inspect before regenerating'
    print('PASS: whole critical inverse phase, decreasing W5 plans, exact returning family, and complete inverse-word checks')


if __name__ == '__main__':
    main()
