"""Exact controls for the two-order half-defect minimum window.

The README supplies the unbounded proof. Raw inequalities retain the true
positive addend on actual reduced cycles; fixed q1 constants are checked
algebraically, not imposed on controls with a small normalized minimum.
The declared dependency supplies placement and the 259*log(minimum) closure.
Standard library only; default receipt verification, --write-receipt to regenerate.
"""
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from math import gcd
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
FIXTURES = ROOT / "areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json"
DEPENDENCY = HERE.parent / "half-defect-imbalance-growth/README.md"


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def intercept(word):
    C = total = 0
    for letter in word:
        C = 3*C+2**total
        total += letter
    return C


def raise_last(word, extra):
    return word[:-1]+(word[-1]+extra,)


def actual(A, B, p, q, scale=1):
    word = A+B+raise_last(A, p)+raise_last(B, q)
    D = 2**sum(word)-3**len(word)
    if D <= 0:
        return None
    C = intercept(word)
    g = gcd(C, D)
    require(scale > 0 and scale % 2, "positive odd scaling")
    d, state = scale*(D//g), scale*(C//g)
    states = []
    for letter in word:
        require(state > 0 and state % 2, 'positive odd actual state')
        states.append(state)
        raw = 3*state+d
        require((raw & -raw).bit_length()-1 == letter, 'exact actual arrow valuation')
        state = raw >> letter
    require(state == states[0] and len(set(states)) == len(states), 'primitive exact closure')
    return d, states, word


def check(A, B, p, q, scale=1):
    require(p != q and p > 0 and q > 0 and A and B, "unequal positive defects and nonempty blocks")
    cycle = actual(A, B, p, q, scale)
    if cycle is None:
        return []
    d, states, word = cycle
    a, b = len(A), len(B)
    N = a+b
    Q, S = 2**sum(A), 2**sum(B)
    x, z, y, t = states[0], states[a], states[N], states[N+a]
    require((y-x) % Q == 0 and (z-t) % S == 0, 'actual paired quotients')
    H, J = (y-x)//Q, (z-t)//S
    require(H > 0 and H % 2 and J % 2, 'odd nonzero paired differences')
    if p < q and J > 0:
        return []
    M = min(states)
    gamma = F(3*M+d, 2*M)
    r0 = F(y, x)
    r = F(t, z) if p < q else F(z, t)
    require(r > 1 and r0 > 1, 'chosen paired orders')
    rho = F(3**N, Q*S)
    require(r0 < F(2**(p+q), 1)/rho, 'untruncated first ratio bound')
    require(r < F(2**(q if p < q else p), 1)/rho, 'second ratio bound')
    records = []
    for index, state in enumerate(states):
        if state != M:
            continue
        if p < q and index < a:
            i, c = index, a-index
            prefix, suffix = sum(A[:i]), sum(A[i:])
            eA, eB, eD = sum(A)-a, sum(B)-b, suffix-c
            require(M*r0 > 3**i*2**suffix, 'A retained prefix cylinder')
            require(M*r*gamma**c > 2**(sum(B)+eD), 'A retained suffix and B excess')
            require(states[N+i]-M == 3**i*2**suffix*H, 'exact paired difference at minimum')
            require(2**prefix >= 3**i and (i == 0 or 2**prefix > 3**i),
                    'A minimum prefix has contracting slope')
            require(2**eD*z <= gamma**c*M, 'A exact suffix growth bound')
            record = {'case': 'A', 'offset': i, 'prefix_excess': prefix-i,
                      'suffix_excess': eD, 'other_excess': eB, 'smaller_defect': p,
                      'suffix_base_word': list(A[i:]), 'suffix_extra_defect': 0}
        elif p > q and index >= N+a:
            j, c = index-(N+a), 2*N-index
            prefix, suffix = sum(B[:j]), sum(B[j:])
            eA, e0, e1 = sum(A)-a, prefix-j, suffix-c
            require(M*r > 3**j*2**suffix, 'D retained prefix cylinder')
            require(M*r0*gamma**c > 2**(sum(A)+q+e1), 'D retained terminal-q factor')
            require(r0 < 2**q*r, 'D ordinary B ratio contraction')
            require(M*r*gamma**c > 2**(sum(A)+e1), 'D reduced suffix growth inequality')
            require(2**prefix >= 3**j and (j == 0 or 2**prefix > 3**j),
                    'D minimum prefix has contracting slope')
            require(2**(q+e1)*x <= gamma**c*M, 'D exact terminal-q suffix growth bound')
            require(states[a+j]-M == 3**j*2**suffix*J, 'exact D paired difference at minimum')
            record = {'case': 'D', 'offset': j, 'prefix_excess': e0,
                      'suffix_excess': e1, 'other_excess': eA, 'smaller_defect': q,
                      'suffix_base_word': list(B[j:]), 'suffix_extra_defect': q,
                      'changed_B_slope': str(F(3**b, 2**(sum(B)+q)))}
        else:
            continue
        record.update(A=list(A), B=list(B), p=p, q=q, addend=d, minimum=M,
                      normalized_minimum=str(F(M, d)), full_word=list(word),
                      states=states, boundaries=[x, z, y, t], gamma=str(gamma), r0=str(r0), r=str(r),
                      paired_H=H, paired_J=J)
        records.append(record)
    return records


def combine(first, second, weight):
    return {key: weight*first.get(key, 0)+second.get(key, 0)
            for key in first.keys() | second.keys()
            if weight*first.get(key, 0)+second.get(key, 0) != 0}


def constants():
    require(3**10000 > 2**15849 and 393217**200 < 2**3717, 'replayed fixed rational bounds')
    K, A0 = F(317, 200), F(15849, 10000)
    c0, eps = 2*K-A0-1, K-A0
    cA, cD = 1-eps-K*c0, 1-(K+1)*eps
    D0, B0 = K*A0-1, K-1-cA
    firstA = {'ell': F(1), 'N': c0, 'a': F(-1), 'i': -(A0-1),
              'eD': F(-1), 'eA': F(-1), 'eB': F(-1)}
    secondA = {'ell': F(1), 'N': eps-1, 'a': K, 'i': -(K-1),
               'eD': F(-1), 'eB': F(-1), 'Delta': F(1, 2)}
    combinedA = combine(firstA, secondA, K)
    require(combinedA ==
            {'ell': K+1, 'N': -cA, 'i': -D0, 'eA': -K,
             'eB': -(K+1), 'eD': -(K+1), 'Delta': F(1, 2)},
            'exact case-A elimination of the first block length')
    firstD = {'ell': F(1), 'N': eps, 'b': F(-1), 'j': -(A0-1),
              'e1': F(-1), 'Delta': F(1, 2)}
    secondD = {'ell': F(1), 'N': eps-1, 'b': K, 'j': -(K-1),
               'eA': F(-1), 'e1': F(-1), 'Delta': F(1, 2)}
    combinedD = combine(firstD, secondD, K)
    require(combinedD ==
            {'ell': K+1, 'N': -cD, 'j': -D0, 'eA': F(-1),
             'e1': -(K+1), 'Delta': (K+1)/2},
            'exact case-D elimination of the second block length')
    require(K*K-1-cD == B0, 'same post-budget N coefficient')
    budgetA = {'N': K-1, 'eA': F(-1), 'eB': F(-1), 'p': F(-1), 'Delta': F(-1, 2)}
    budgetD = {'N': K-1, 'eA': F(-1), 'e0': F(-1), 'e1': F(-1),
               'q': F(-1), 'Delta': F(-1, 2)}
    require(combine(combinedA, budgetA, F(1)) ==
            {'N': B0, 'ell': K+1, 'i': -D0, 'eA': -(K+1),
             'eB': -(K+2), 'eD': -(K+1), 'p': F(-1)},
            'complete post-budget case-A coefficient identity')
    require(combine(budgetD, combinedD, K+1) ==
            {'N': B0, 'ell': K+1, 'j': -D0, 'eA': -(K+2),
             'e0': -(K+1), 'e1': -2*(K+1), 'q': -(K+1)},
            'complete post-budget case-D coefficient identity')
    I0 = D0+(K+1)*(A0-1)
    rhs = B0+(K+1)/259
    density = rhs/(K+1)
    position = rhs/I0
    require(cA == F(145033, 2000000) and cD == F(1999483, 2000000), 'original constants retained')
    require(density == F(270636453, 1339030000) < F(203, 1000), 'exact excess consequence')
    require(I0 == F(3024033, 1000000), 'prefix-return coefficient')
    require(position == F(90212151, 522149698) < F(173, 1000), 'exact position consequence')
    require(B0 == F(1024967, 2000000) and D0 == F(3024133, 2000000), 'common retained coefficients')
    require(rhs == F(270636453, 518000000), 'generic closure right side')
    suffix = rhs/(2*(K+1))
    require(suffix == F(270636453, 2678060000), 'retained suffix-excess bound')
    require(F(173,1000)-position == F(59873377,261074849000), 'strict rounded offset margin')
    # The same density bound is already implied by the old case-A inequalities
    # if their exact first-ratio term -(eA+eB) is retained.
    require(rhs-(K+1)*F(203, 1000) < 0, 'old density-only consequence is not new')
    return {'cA': str(cA), 'cD': str(cD), 'D0': str(D0), 'B0': str(B0),
            'I0': str(I0), 'after_generic_closure_rhs': str(rhs),
            'K': str(K), 'A0': str(A0), 'generic_closure_coefficient': 259,
            'common_weights': {'other_excess': str(K+2), 'prefix_excess': str(K+1),
                               'suffix_excess': str(2*(K+1)),
                               'smaller_defect_case_A': '1', 'smaller_defect_case_D': str(K+1)},
            'suffix_excess_coefficient': str(suffix),
            'total_excess_coefficient': str(density), 'minimum_offset_coefficient': str(position),
            'excess_slack_to_203_over_1000': str(F(203, 1000)-density),
            'offset_slack_to_173_over_1000': str(F(173, 1000)-position)}


def shared_fixtures():
    data = json.loads(FIXTURES.read_text())
    arrows = 0
    for cycle in data['cycles']:
        word, states, d = cycle['valuations'], cycle['states'], cycle['d']
        require(len(word) == len(states) > 0 and d > 0 and d % 2, 'fixture dimensions')
        for i, (letter, value) in enumerate(zip(word, states)):
            raw = 3*value+d
            require(value > 0 and value % 2 and letter > 0, 'fixture odd positive state')
            require((raw & -raw).bit_length()-1 == letter, 'fixture exact valuation')
            require(raw == 2**letter*states[(i+1)%len(states)], 'fixture arrow')
            arrows += 1
    require(len(data['cycles']) == 11 and {c['d'] for c in data['cycles']} == {5,7,13,61},
            'eleven standard actual-addend controls')
    return {'cycles': len(data['cycles']), 'arrows': arrows,
            'addends': sorted({c['d'] for c in data['cycles']}),
            'fixture_sha256': sha256(FIXTURES.read_bytes()).hexdigest()}


def actual_controls():
    words = [v for length in range(1, 4) for v in product(range(1, 4), repeat=length)]
    counts = Counter()
    digest = sha256()
    examples = {}
    for A in words:
        for B in words:
            for p, q in product(range(1, 6), repeat=2):
                if p == q:
                    continue
                for row in check(A, B, p, q):
                    case = row['case']
                    counts[case] += 1
                    counts['arrows'] += len(row['full_word'])
                    counts['interior_minima'] += row['offset'] > 0
                    counts['opposite_parity'] += (p+q) % 2
                    counts['fixed_K_applicable'] += row['minimum'] >= row['addend']*2**17
                    counts['positive_suffix_excess'] += row['suffix_excess'] > 0
                    counts['positive_other_excess'] += row['other_excess'] > 0
                    examples.setdefault(case, row)
                    if row['offset'] > 0:
                        examples.setdefault(case+'_interior', row)
                    digest.update((json.dumps(row, sort_keys=True)+'\n').encode())
    require({'A','D','A_interior','D_interior'} <= examples.keys(), 'both orders and interior minima exercised')
    special = []
    for A, B, p, q in [((1,), (3,1,1,1), 5, 1),
                       ((1,), (3,1,1,1,1,1), 7, 1)]:
        rows = check(A, B, p, q)
        require(len(rows) == 1 and rows[0]['case'] == 'D' and rows[0]['offset'] == 1,
                'genuine D interior-minimum control')
        special.extend(rows)
    require([row['addend'] for row in special] == [989527,62325895], 'two retained true addends')
    require(F(special[0]['changed_B_slope']) == F(81,128) < 1 <
            F(special[1]['changed_B_slope']) == F(729,512), 'both changed-B slope signs')
    window = check((1,1), (2,1,1), 3, 1)
    require(len(window) == 1, 'window boundary control exists')
    window = window[0]
    require(window['addend'] == 499 and window['minimum'] == 8545 and window['offset'] == 1,
            'actual addend499 minimum control')
    require(window['states'] == [9925,15137,22955,17341,26261,39641,59711,11227,8545,13067],
            'complete displayed addend499 cycle')
    require(1000*window['offset'] > 173*(len(window['A'])+len(window['B'])),
            'the q1 offset window is not imposed on other addends')
    require(F(window['normalized_minimum']) < 2**17, 'fixed-K hypothesis fails in countercontrol')
    scaled = check((1,1), (2,1,1), 3, 1, scale=3)
    require(len(scaled) == 1 and scaled[0]['addend'] == 1497 and
            scaled[0]['normalized_minimum'] == window['normalized_minimum'],
            'odd-scaled actual addend including a factor of three')
    require(scaled[0]['states'] == [3*state for state in window['states']],
            'complete scaled addend1497 cycle')
    return {'block_lengths': [1,3], 'block_letters': [1,3], 'unequal_defects': [1,5],
            'counts': dict(sorted(counts.items())), 'actual_control_digest': digest.hexdigest(),
            'examples': examples, 'interior_B_controls': special,
            'other_addend_window_countercontrol': window, 'scaled_window_control': scaled[0],
            'scope': 'Exact raw inequalities at genuine minima; no finite absence or q1 cutoff is inferred from the grid.'}


def main():
    require(sys.argv[1:] in ([], ['--write-receipt']), 'usage: check_minimum_window.py [--write-receipt]')
    output = {'schema': 'half-defect-minimum-window-v1',
              'source_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
              'dependency_id': 'half-defect-imbalance-growth',
              'dependency_statement_sha256': sha256(DEPENDENCY.read_bytes()).hexdigest(),
              'constants': constants(), 'actual_controls': actual_controls(),
              'shared_fixtures': shared_fixtures()}
    encoded = json.dumps(output, sort_keys=True, indent=2)+'\n'
    destination = HERE/'check_minimum_window.json'
    if sys.argv[1:]:
        destination.write_text(encoded)
    else:
        require(destination.read_text() == encoded, 'receipt mismatch; inspect before regenerating')
    print(json.dumps({'status': 'PASS', 'counts': output['actual_controls']['counts'],
                      'minimum_offset_coefficient': output['constants']['minimum_offset_coefficient'],
                      'standard_fixtures': output['shared_fixtures']['cycles']}, sort_keys=True))


if __name__ == '__main__':
    main()
