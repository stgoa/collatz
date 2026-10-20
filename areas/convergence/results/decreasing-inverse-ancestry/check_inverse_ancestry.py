"""Bounded independent checks for complete decreasing inverse ancestry."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
from fractions import Fraction as F
import inverse_ancestry as I

HERE = Path(__file__).resolve().parent


def digest(current):
    return hashlib.sha256(''.join(f'{x},{c}\n' for x,c in sorted(current.items())).encode()).hexdigest()


def prefix(seed, length):
    states, valuations = [seed], []
    for _ in range(length):
        x = states[-1]
        valuations.append(I.NORMAL.valuation2(3*x+1))
        states.append(I.step(x))
    return states, valuations


def lower_current(sources, cap=5000):
    return I.RUN.H.LOCAL.FORCING.absorption_current(sources, cap=cap)


def run():
    canonical = 0
    for q in range(1, 16384, 2):
        if not I.NORMAL.canonical(q):
            continue
        data = I.ancestry(q)
        point, rays = I.NORMAL.predecessor_families(q)
        smaller = [x for x in rays+(() if point is None else (point,)) if x < q]
        assert smaller == ([(2*q-1)//3] if q % 3 == 2 else [])
        assert data['minimum'] <= q
        assert I.ancestry(data['minimum'])['minimum'] == data['minimum']
        assert q in I.canonical_class(data['minimum'])
        canonical += 1
    for h in range(1,129):
        t = 1 if h % 2 == 0 else 7
        p = 2**(h+1)*t-1
        q = 2*3**h*t-1
        data = I.ancestry(q)
        assert data['depth'] == h and data['minimum'] == p

    branch_cases = even_cases = 0
    for x in range(3, 16384, 4):
        if I.RUN.H.selected(x):
            continue
        a,t,d,w = I.RUN.parameters(x)
        normalization = I.NORMAL.normalization(I.RUN.target(x))
        q, k = normalization['minimum'], normalization['F_exponent']
        depth = I.valuation3(q+1)
        if d % 2 == 0:
            assert k == 0 and depth == 0
            even_cases += 1
        else:
            b = d//2
            V = 3**(a+b)*t-3**(b+1)+2**d*(2**(2*k+1)+1)
            assert depth == I.valuation3(V)-1
            e = I.valuation3(2*k+1)
            if e != b:
                assert depth == min(e,b)
        branch_cases += 1

    small_family = []
    for j in range(32):
        x = 19199+65536*j
        data = I.bridge(x)
        q, p = (6561*x+3745)//8192, (2187*x-117)//4096
        assert data['old_target'] == q and data['target'] == p
        left, lv = prefix(x,9)
        right, rv = prefix(p,2)
        assert lv == [1]*7+[2,6] and rv == [1,2] and left[-1] == right[-1]
        small_family.append(dict(root=x,target=p,old_target=q,rows=len(data['current']),
                                 sha256=digest(data['current'])))

    family_cases = []
    for h in range(2,8):
        family = I.large_return_family(h)
        for weight in (1,2):
            witness = I.ray_witness(h,weight)
            x,N = witness['root'],witness['N']
            data = I.bridge(x)
            a,b,k = family['a'],family['b'],family['k']
            assert I.RUN.parameters(x)[:3] == (a,(x+1)//2**a,family['d'])
            assert data['ancestry']['depth'] == h
            assert data['target'] == family['slope']*x+family['intercept'] < N < x < data['old_target']
            left,lv = prefix(x,a+b)
            right,rv = prefix(data['target'],h+1)
            assert lv == [1]*(a-1)+[2]*b+[2*k+4]
            assert rv == [1]*h+[2] and left[-1] == right[-1]
            assert sum(lv)+1 == family['modulus'].bit_length()-1
            count = I.source_count(N,family['residue'],family['modulus'])
            family_cases.append(dict(h=h,weight=weight,a=a,d=family['d'],k=k,
                                     binary_bits=family['modulus'].bit_length()-1,
                                     root_bits=x.bit_length(),source_count=count,
                                     bridge_rows=len(data['current']),sha256=digest(data['current'])))

    masses, conversions = [], []
    for N in (8,32,96,384,1536,6144,24576,65536):
        profile = I.selected_profile(N)
        old = I.RUN.normalized_profile(N)
        mass = I.mass_formula(N)
        assert mass == sum(profile.values()) and old.keys() <= profile.keys()
        extras = {x:c for x,c in profile.items() if x not in old}
        masses.append(dict(N=N,old_mass=sum(old.values()),new_mass=mass,
                           extra_roots=[[x,c] for x,c in extras.items()],
                           profile_sha256=digest(profile)))
        if N in (96,384,1536):
            supplied = lower_current(dict.fromkeys(range(3,N+1,2),1))
            result = I.certify(N,supplied)
            assert result['selected'] == profile
            assert I.divergence(result['current']) == profile
            assert all(c>0 for c in result['current'].values())
            conversions.append(dict(N=N,source_mass=mass,rows=len(result['current']),
                                    sha256=digest(result['current'])))

    witnesses = [(65536,84735,1),
                 (I.ray_witness(2,2)['N'],I.ray_witness(2,2)['root'],2)]
    stored, actual = {}, []
    for N,x,weight in witnesses:
        data = I.bridge(x)
        p = data['target']
        assert I.RUN.H.TRANSFER.residual_coefficient(N,x) == weight
        assert p < N < x < 3*N//2 and data['old_target'] > N
        supplied = lower_current({p:1})
        result = I.certify_single(x,supplied,weight)
        assert I.divergence(result['current']) == {x:weight}
        assert all(c>0 for c in result['current'].values())
        name = 'root84735_current.csv' if x == 84735 else 'large_h2_weight2_current.csv'
        stored[name] = result['current']
        actual.append(dict(N=N,root=x,weight=weight,target=p,old_target=data['old_target'],
                           input_rows=len(supplied),bridge_rows=len(data['current']),
                           output_rows=len(result['current']),sha256=digest(result['current'])))

    for j in range(33):
        u,q = 27+131072*j,91+419904*j
        states,vals = prefix(u,8)
        assert states[-1] == q and all(I.NORMAL.canonical(x) for x in states)
        assert I.ancestry(q)['minimum'] == q > u
    assert I.ancestry(I.NORMAL.quotient_step(7))['minimum'] == 7
    assert I.ancestry(I.NORMAL.quotient_step(17))['minimum'] == 1
    receipt = dict(status='PASS',scope='Complete local inverse normalizer and partial R26 extension; universal coverage open',
                   canonical_targets=dict(bound_exclusive=16384,cases=canonical),
                   long_inverse_depths=[1,128],branch_cases=branch_cases,even_branch_cases=even_cases,
                   small_cylinder=small_family,large_return_families=family_cases,
                   exact_profile_counts=masses,full_profile_conversions=conversions,
                   actual_new_root_conversions=actual,input_search_cap=5000,
                   nongreedy_ancestor_counterfamily_cases=33,
                   new_targets_contained_in_R29_saturation=True,convergence_proved=False)
    return receipt,stored


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-receipt',action='store_true')
    args=parser.parse_args()
    receipt,currents=run()
    path=HERE/'inverse_ancestry_audit.json'
    if args.write_receipt:
        path.write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
        for name,current in currents.items():
            with (HERE/name).open('w',newline='') as out:
                writer=csv.writer(out,lineterminator='\n')
                writer.writerow(('state','current'))
                writer.writerows(sorted(current.items()))
    else:
        assert json.loads(path.read_text()) == receipt
        for name,current in currents.items():
            with (HERE/name).open(newline='') as source:
                assert {int(r['state']):int(r['current']) for r in csv.DictReader(source)} == current
    print(f"PASS: {receipt['canonical_targets']['cases']} canonical targets, "
          f"{receipt['branch_cases']} return branches, {len(receipt['large_return_families'])} large-return families, "
          f"{len(receipt['exact_profile_counts'])} exact profile counts, two new-root currents")


if __name__ == '__main__':
    main()
