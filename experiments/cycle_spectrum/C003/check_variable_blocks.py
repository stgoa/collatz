#!/usr/bin/env python3
"""C003 bounded all-rotation tests of variable-block denominator proposals.

The proposed inequalities are observations unless separately proved.
All arithmetic uses the raw odd recurrence, including at state1.
"""

import argparse
from collections import Counter
from functools import lru_cache
from hashlib import sha256
from itertools import product
import json
from math import gcd
from pathlib import Path
import sys

if sys.flags.optimize:
    raise SystemExit("FAIL: optimized Python is not supported for certificate replay")

HERE = Path(__file__).resolve().parent
ACTUAL = HERE.parent / "C001/actual_cycles.json"
SCANNER = HERE.parent / "C001/scan_cycles.py"
BASELINE = "e14a4e361bd01d93fc48eaa4f2684300dad194e9"
MAX_BASE_LENGTH = 3
MAX_VALUATION = 4
MAX_REPETITION = 6
SLOPE_INTEGER_LIMIT = 32
SLOPE_REPETITION_LIMIT = 12


def require(test, message):
    if not test:
        raise ValueError(message)


def raw_step(n, d):
    require(type(n) is int and n > 0 and n % 2 and type(d) is int
            and d > 0 and gcd(d,6) == 1, 'invalid positive raw odd state/parameter')
    z = 3*n+d
    a = (z & -z).bit_length()-1
    return z >> a, a


@lru_cache(maxsize=None)
def divisors(n):
    return tuple(k for k in range(1, n+1) if n % k == 0)


def prefix_powers(word):
    """All repetition exponents of every nonempty prefix, using its least period."""
    pi, answer = [0]*len(word), [None]
    for i in range(len(word)):
        if i:
            j = pi[i-1]
            while j and word[i] != word[j]:
                j = pi[j-1]
            if word[i] == word[j]:
                j += 1
            pi[i] = j
        length = i+1
        period = length-pi[i]
        answer.append(divisors(length//period) if length % period == 0 else (1,))
    return answer


def direct(word):
    require(word and all(type(a) is int and a >= 1 for a in word), 'invalid valuation word')
    c = A = 0
    for a in word:
        c = 3*c+2**A
        A += a
    return c, 2**A-3**len(word), A


def contracting_checks(cu,du,au,mu,cv,dv,av,mv,k,ell,den,counts):
    """Exact finite checks of the separate written contracting-block theorem.

    The parameter used is the reduced denominator, not a possibly larger
    parameter of a scaled realization. All comparisons are integer products.
    """
    K = du*cv-dv*cu
    if not (du > 0 and dv > 0 and K):
        return
    q,s = 2**au,2**av
    M = max(mu,mv)
    Fnum,Fden = 3**M*(3**M+1),2**M
    require(cu*2**mu < du*3**mu*(3**mu+1), 'u fixed-point bound failed')
    require(cv*2**mv < dv*3**mv*(3**mv+1), 'v fixed-point bound failed')
    require(den*abs(K) > max(q**k*dv,s**ell*du), 'strict denominator-commutator bound failed')
    counts['contracting_commutator_checks'] += 1
    for side,Q,t in [('u',q,k),('v',s,ell)]:
        require(Q**(t-1)*Fden < den*Fnum, 'contracting lattice-height inequality failed')
        counts['contracting_lattice_height_checks'] += 1
        if Q == max(q,s) and t >= 3:
            require(den > 2**M*Q**(t-3), 'maximum-power variable-block bound failed')
            counts['maximum_power_uniform_checks'] += 1
    if k >= 3 and ell >= 3:
        require(den > 2**M, 'maximum-length uniform bound failed')
        counts['both_ge3_maximum_length_checks'] += 1


def universal_coefficient_check(cu,du,au,mu,cv,dv,av,mv,counts):
    bu,bv = 2**(au-mu)*3**mu,2**(av-mv)*3**mv
    require(cu < bu and cv < bv and abs(du) < bu and abs(dv) < bv,
            'universal block coefficient bound failed')
    require(abs(du*cv-dv*cu) < 2*bu*bv, 'universal commutator bound failed')
    counts['universal_commutator_upper_checks'] += 1


def proportional_check(cu,du,au,mu,cv,dv,av,mv,k,ell,C,D,counts):
    K = du*cv-dv*cu
    if D <= 0 or not K or au*mv != av*mu:
        return
    R = gcd(au,mu)
    a,b = au//R,mu//R
    require(av % a == 0 and mv % b == 0 and av//a == mv//b,
            'common primitive slope failed')
    S = av//a
    U,V = 2**a,3**b
    e,h,L = gcd(R,S),gcd(R*k,S*ell),R*k+S*ell
    He,Hh = U**e-V**e,U**h-V**h
    require(U > V and K % He == 0,'positive proportional factor failed')
    g = gcd(C,D)
    require(((K//He)*Hh) % g == 0,'proportional cancellation divisor failed')
    require((D//g)*abs(K) > U**(L-h)*He,
            'exact proportional denominator refinement failed')
    counts['proportional_exact_denominator_checks'] += 1


def slope_integer_grid():
    """Finite evidence for the separate all-integer written lemma, not S-units."""
    count,equalities,worst = 0,[],None
    digest = sha256()
    for R in range(1,SLOPE_INTEGER_LIMIT+1):
        for S in range(1,SLOPE_INTEGER_LIMIT+1):
            if gcd(R,S) != 1:
                continue
            for k in range(2,SLOPE_REPETITION_LIMIT+1):
                for ell in range(2,SLOPE_REPETITION_LIMIT+1):
                    L,H = R*k+S*ell,gcd(R*k,S*ell)
                    gap = 5*(L-H+1)-7*(R+S)
                    require(gap >= 0,'uniform coprime-slope integer lemma failed')
                    count += 1
                    row = dict(R=R,S=S,k=k,ell=ell,L=L,H=H,gap=gap)
                    if gap == 0:
                        equalities.append(row)
                    if worst is None or gap < worst['gap']:
                        worst = row
                    digest.update(json.dumps(row,sort_keys=True,separators=(',',':')).encode()+b'\n')
    require(any(row['R']==2 and row['S']==3 and row['k']==3 and row['ell']==2
                for row in equalities),'named sharp equality missing')
    return dict(domain=dict(R_S=[1,SLOPE_INTEGER_LIMIT],coprime=True,
                            k_ell=[2,SLOPE_REPETITION_LIMIT]),
                inequality='5*(L-H+1)>=7*(R+S), L=R*k+S*ell,H=gcd(R*k,S*ell)',
                cases=count,equalities=equalities,smallest_gap=worst,
                verification_sha256=digest.hexdigest(),
                scope='Exact bounded integer checks only; the universal lemma requires its written proof and the S-unit asymptotic input is not numerically verified.')


def empty_all_size_probe():
    require(2**8 > 3**5,'rational diagnostic exponent comparison failed')
    return dict(eligible=0,counterexample_count=0,counterexamples=[],worst_exact_ratio=None,
                comparison='den^16 < 2^(5*A), i.e. den < 2^((5/16)*A)',
                scope='Diagnostic for unequal slopes,K!=0,k,ell>=2,positive D; absence of finite counterexamples proves no all-size inequality. The exponent5/16 is below log_3(2)/2 because2^8>3^5.')


def all_size_probe(probe,u,k,v,ell,K,den,A,extra=None):
    if not K or k < 2 or ell < 2 or sum(u)*len(v) == sum(v)*len(u):
        return
    numerator,denominator = den**16,2**(5*A)
    probe['eligible'] += 1
    previous = probe['worst_exact_ratio']
    better = previous is None or numerator*previous['ratio_denominator'] < previous['ratio_numerator']*denominator
    failure = numerator < denominator
    if better or failure:
        row = dict(u=list(u),k=k,v=list(v),ell=ell,K=K,denominator=den,A=A,
                   ratio_numerator=numerator,ratio_denominator=denominator)
        if extra:
            row.update(extra)
        if better:
            probe['worst_exact_ratio'] = row
        if failure:
            probe['counterexample_count'] += 1
            probe['counterexamples'].append(row)


def candidate_record(d, states, word, rotation, cut, k, ell, u, v, cu, du, cv, dv, g, den, gu, gv):
    return dict(actual_parameter=d, rotation=rotation, source=states[rotation],
                canonical_minimum=states[0], cut=cut, u=list(u), k=k, v=list(v), ell=ell,
                C_u=cu, D_u=du, C_v=cv, D_v=dv, K=du*cv-dv*cu,
                cancellation=g, denominator=den, G_u=gu, G_v=gv,
                common_geometric_gcd=gcd(gu,gv),
                proposed_power_bound=2**max(len(u),len(v)))


def scan_actual():
    source = json.loads(ACTUAL.read_text())
    require(source['sources']['scanner_sha256'] == sha256(SCANNER.read_bytes()).hexdigest(),
            'source scanner hash mismatch')
    cycles = source['cycles']
    require(len(cycles) == 2459, 'unexpected source-cycle count')
    counts, groups = Counter(), Counter()
    failures, geometric_examples, eligible_examples, mixed_examples = [], [], [], []
    worst = None
    all_size = empty_all_size_probe()
    digest = sha256()
    for cycle in cycles:
        d, states, original = cycle['d'], cycle['states'], tuple(cycle['word'])
        require(states[0] == min(states) and len(states) == len(set(states)) == len(original),
                'source cycle must be canonical and simple')
        for i, n in enumerate(states):
            require(raw_step(n,d) == (states[(i+1)%len(states)],original[i]), 'source arrow failed')
            counts['source_arrows'] += 1
        c0,D,A0 = direct(original)
        require(D > 0 and d*c0 == states[0]*D, 'source fixed point failed')
        g, den = gcd(c0,D), D//gcd(c0,D)
        require(cycle['reduced_denominator'] == den, 'source denominator mismatch')
        m = len(original)
        p3 = [3**j for j in range(m+1)]
        for rotation in range(m):
            word = original[rotation:]+original[:rotation]
            counts['rotations'] += 1
            prefix, suffix = prefix_powers(word), prefix_powers(word[::-1])
            Cs, As = [0], [0]
            for a in word:
                Cs.append(3*Cs[-1]+2**As[-1])
                As.append(As[-1]+a)
            C = Cs[-1]
            require(d*C == states[rotation]*D and gcd(C,D) == g, 'rotation coefficient failed')
            if m <= 12:
                for length in range(1,m+1):
                    brute = tuple(k for k in divisors(length)
                                  if word[:length] == word[:length//k]*k)
                    require(prefix[length] == brute, 'prefix period enumeration is incomplete')
                    counts['small_prefix_completeness_checks'] += 1
            for cut in range(1,m):
                counts['baseline_cuts'] += 1
                for k in prefix[cut]:
                    mu = cut//k
                    cu, au = Cs[mu], As[mu]
                    du = 2**au-p3[mu]
                    gu = (2**As[cut]-p3[cut])//du
                    for ell in suffix[m-cut]:
                        mv = (m-cut)//ell
                        av = As[cut+mv]-As[cut]
                        cv = (Cs[cut+mv]-p3[mv]*Cs[cut]) >> As[cut]
                        dv = 2**av-p3[mv]
                        gv = (2**(A0-As[cut])-p3[m-cut])//dv
                        K = du*cv-dv*cu
                        require(du*C-cu*D == 2**As[cut]*K*gv, 'first elimination failed')
                        require(dv*C-cv*D == -p3[m-cut]*K*gu, 'second elimination failed')
                        require(K == 0 or (K*gcd(gu,gv)) % g == 0, 'gcd divisor failed')
                        relation = 'proportional' if au*mv == av*mu else 'unequal'
                        both_contract = du > 0 and dv > 0
                        universal_coefficient_check(cu,du,au,mu,cv,dv,av,mv,counts)
                        proportional_check(cu,du,au,mu,cv,dv,av,mv,k,ell,C,D,counts)
                        contracting_checks(cu,du,au,mu,cv,dv,av,mv,k,ell,den,counts)
                        counts['decompositions'] += 1
                        counts['K_zero'] += int(K == 0)
                        for threshold in (1,2,3):
                            if k >= threshold and ell >= threshold:
                                group = f'k_ell_ge{threshold}|{relation}|'+(
                                    'both_contracting' if both_contract else 'has_expanding_block')
                                groups[group] += 1
                        digest.update(json.dumps([d,states[0],rotation,cut,k,ell,mu,mv,K,g,gu,gv],
                                                 separators=(',',':')).encode()+b'\n')
                        if k >= 2 and ell >= 2:
                            all_size_probe(all_size,word[:mu],k,word[cut:cut+mv],ell,K,den,A0,
                                dict(actual_parameter=d,canonical_minimum=states[0],rotation=rotation))
                        if k >= 3 and ell >= 3 and not both_contract:
                            mixed_examples.append(candidate_record(d,states,word,rotation,cut,k,ell,
                                word[:mu],word[cut:cut+mv],cu,du,cv,dv,g,den,gu,gv))
                        if K and both_contract and k >= 2 and ell >= 2:
                            counts['both_contracting_nonzeroK_ge2'] += 1
                            for name,factor in [('minimum',min(gu,gv)),('maximum',max(gu,gv)),
                                                ('gcd',gcd(gu,gv))]:
                                counts[f'den_not_above_geometric_{name}'] += int(den <= factor)
                            if den <= min(gu,gv) and len(geometric_examples) < 8:
                                geometric_examples.append(candidate_record(d,states,word,rotation,cut,k,ell,
                                    word[:mu],word[cut:cut+mv],cu,du,cv,dv,g,den,gu,gv))
                        if not (K and both_contract and k >= 3 and ell >= 3):
                            continue
                        counts['proposed_uniform_eligible'] += 1
                        bound = 2**max(mu,mv)
                        record = candidate_record(d,states,word,rotation,cut,k,ell,
                                                  word[:mu],word[cut:cut+mv],cu,du,cv,dv,g,den,gu,gv)
                        if len(eligible_examples) < 12:
                            eligible_examples.append(record)
                        if worst is None or den*worst['proposed_power_bound'] < worst['denominator']*bound:
                            worst = record
                        if den <= bound:
                            counts['proposed_uniform_failures'] += 1
                            failures.append(record)
    require(counts['rotations'] == 36912 and counts['baseline_cuts'] == 1637490,
            'all-rotation domain count mismatch')
    failures.sort(key=lambda row:(row['denominator'],row['actual_parameter'],row['canonical_minimum'],
                                  row['rotation'],row['cut'],row['k'],row['ell']))
    return dict(source_cycles=2459, source_parameters=len({x['d'] for x in cycles}),
                counts=dict(sorted(counts.items())), groups=dict(sorted(groups.items())),
                decomposition_sha256=digest.hexdigest(), proposed_uniform_counterexamples=failures,
                eligible_examples=eligible_examples, worst_power_ratio=worst,
                both_ge3_mixed_direction_examples=mixed_examples,
                all_size_exponent_diagnostic=all_size,
                geometric_comparison_examples=geometric_examples,
                scope='Every rotation and every exact power decomposition; rotations and scaled repeats are not distinct primitive cycles.')


def generated_grid():
    """All declared finite words; actual integer cycles verified arrow by arrow."""
    bases = [tuple(w) for length in range(1,MAX_BASE_LENGTH+1)
             for w in product(range(1,MAX_VALUATION+1),repeat=length)]
    data = {w:direct(w) for w in bases}
    counts,groups = Counter(),Counter()
    digest = sha256()
    parameters = set()
    worst = None
    all_size = empty_all_size_probe()
    expanding_failures = []
    geometric_failures = []
    for u in bases:
        cu,du,au = data[u]
        q,p,mu = 2**au,3**len(u),len(u)
        for v in bases:
            cv,dv,av = data[v]
            s,r,mv = 2**av,3**len(v),len(v)
            K = du*cv-dv*cu
            relation = 'proportional' if au*mv == av*mu else 'unequal'
            both_contract = du > 0 and dv > 0
            for k in range(1,MAX_REPETITION+1):
                gu = (q**k-p**k)//du
                for ell in range(1,MAX_REPETITION+1):
                    gv = (s**ell-r**ell)//dv
                    C = r**ell*cu*gu+q**k*cv*gv
                    D = q**k*s**ell-p**k*r**ell
                    require(D != 0,'impossible equal pure two/three powers')
                    word = u*k+v*ell
                    dc,dd,da = direct(word)
                    require((dc,dd,da) == (C,D,k*au+ell*av), 'direct word coefficient mismatch')
                    g = gcd(C,D)
                    require(gcd(g,6) == 1, 'cancellation not coprime to6')
                    require(du*C-cu*D == q**k*K*gv, 'generated first elimination failed')
                    require(dv*C-cv*D == -r**ell*K*gu, 'generated second elimination failed')
                    require(not K or (K*gcd(gu,gv)) % g == 0, 'generated gcd divisor failed')
                    universal_coefficient_check(cu,du,au,mu,cv,dv,av,mv,counts)
                    proportional_check(cu,du,au,mu,cv,dv,av,mv,k,ell,C,D,counts)
                    counts['words'] += 1
                    if D < 0:
                        counts['negative_D'] += 1
                        digest.update(json.dumps([u,v,k,ell,C,D,g],separators=(',',':')).encode()+b'\n')
                        continue
                    counts['positive_D'] += 1
                    den,initial = D//g,C//g
                    parameters.add(den)
                    n = initial
                    states = []
                    for a in word:
                        states.append(n)
                        require(gcd(n,den) == 1,'generated state not reduced')
                        n,actual = raw_step(n,den)
                        require(actual == a,'generated exact valuation failed')
                        counts['actual_arrows'] += 1
                    require(n == initial,'generated cycle does not close')
                    primitive_length = len(word)//max(prefix_powers(word)[-1])
                    require(len(set(states)) == primitive_length,'generated primitive period mismatch')
                    counts['primitive_displayed_words'] += int(primitive_length == len(word))
                    counts['proper_power_words'] += int(primitive_length < len(word))
                    counts['K_zero_positive'] += int(K == 0)
                    all_size_probe(all_size,u,k,v,ell,K,den,k*au+ell*av)
                    if not K:
                        require(du > 0 and dv > 0 and du*C == cu*D,
                                'positive common-fixed-point control failed')
                    contracting_checks(cu,du,au,mu,cv,dv,av,mv,k,ell,den,counts)
                    for threshold in (1,2,3):
                        if k >= threshold and ell >= threshold:
                            groups[f'k_ell_ge{threshold}|{relation}|'+(
                                'both_contracting' if both_contract else 'has_expanding_block')
                                + ('|K0' if not K else '|K_nonzero')] += 1
                    record = None
                    if K and k >= 3 and ell >= 3:
                        record = dict(u=list(u),k=k,v=list(v),ell=ell,C_u=cu,D_u=du,
                                      C_v=cv,D_v=dv,K=K,denominator=den,
                                      numerator=initial,cancellation=g,minimum=min(states),
                                      maximum_length_bound=2**max(mu,mv),
                                      G_u=gu,G_v=gv)
                        if both_contract:
                            if worst is None or den*worst['maximum_length_bound'] < worst['denominator']*2**max(mu,mv):
                                worst = record
                        elif den <= 2**max(mu,mv):
                            expanding_failures.append(record)
                    if K and both_contract and k >= 2 and ell >= 2:
                        for name,factor in [('minimum',min(gu,gv)),('maximum',max(gu,gv)),
                                            ('gcd',gcd(gu,gv))]:
                            counts[f'den_not_above_geometric_{name}'] += int(den <= factor)
                        if den <= min(gu,gv) and len(geometric_failures) < 8:
                            if record is None:
                                record = dict(u=list(u),k=k,v=list(v),ell=ell,denominator=den,
                                              G_u=gu,G_v=gv,C_u=cu,D_u=du,C_v=cv,D_v=dv,K=K)
                            geometric_failures.append(record)
                    digest.update(json.dumps([u,v,k,ell,C,D,g,den,primitive_length],
                                             separators=(',',':')).encode()+b'\n')
    expanding_failures.sort(key=lambda row:(row['denominator'],len(row['u'])+len(row['v']),
        row['k']+row['ell'],row['u'],row['v'],row['k'],row['ell']))
    return dict(domain=dict(base_lengths=[1,MAX_BASE_LENGTH],valuations=[1,MAX_VALUATION],
                            exponents=[1,MAX_REPETITION],ordered_base_pairs=len(bases)**2),
                counts=dict(sorted(counts.items())),groups=dict(sorted(groups.items())),
                distinct_positive_parameters=len(parameters),verification_sha256=digest.hexdigest(),
                worst_contracting_maximum_length_ratio=worst,
                all_size_exponent_diagnostic=all_size,
                mixed_direction_maximum_length_counterexamples=expanding_failures[:12],
                mixed_direction_maximum_length_counterexample_count=len(expanding_failures),
                geometric_comparison_examples=geometric_failures,
                scope='Each positive word is realized at its reduced denominator and every raw arrow checked; proper powers are retained as controls.')


def report():
    return dict(schema='C003-variable-blocks-v1', status='finite observations', baseline_commit=BASELINE,
                clock='raw odd-only recurrence; state1 is not absorbed',
                proposal='Written contracting theorem: den>2^max(len(u),len(v)) when K!=0 and both exponents>=3; stronger maximum-Q exponent and lattice-height inequalities checked too.',
                limits='Finite evidence for the separate written theorem; no universal inference from absence of a counterexample; expanding blocks excluded.',
                source_sha256={'check_variable_blocks.py':sha256(Path(__file__).read_bytes()).hexdigest(),
                               'C001/actual_cycles.json':sha256(ACTUAL.read_bytes()).hexdigest(),
                               'C001/scan_cycles.py':sha256(SCANNER.read_bytes()).hexdigest()},
                actual_cycles=scan_actual(),generated=generated_grid(),
                coprime_slope_integer_lemma=slope_integer_grid())


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write',action='store_true')
    parser.add_argument('--receipt',type=Path,default=HERE/'variable_blocks_audit.json')
    args=parser.parse_args()
    try:
        result=json.loads(json.dumps(report()))
        if args.write:
            args.receipt.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
        else:
            require(result==json.loads(args.receipt.read_text()),'saved receipt mismatch')
    except (OSError,ValueError,KeyError,TypeError) as error:
        print(f'FAIL: {error}',file=sys.stderr)
        return 1
    print(json.dumps({'status':'PASS','counts':result['actual_cycles']['counts'],
                      'groups':result['actual_cycles']['groups'],
                      'generated_counts':result['generated']['counts'],
                      'generated_worst':result['generated']['worst_contracting_maximum_length_ratio'],
                      'mixed_failures':result['generated']['mixed_direction_maximum_length_counterexample_count']},sort_keys=True))
    return 0


if __name__=='__main__':
    raise SystemExit(main())
