"""Exact arithmetic and scoped controls for the two-defect first-block theorem."""
from fractions import Fraction as F
from hashlib import sha256
import json
from math import gcd
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def valuation(value, prime=2):
    require(value != 0, 'valuation of zero')
    value = abs(value)
    result = 0
    while value % prime == 0:
        result += 1
        value //= prime
    return result


def intercept(word):
    result = total = 0
    for letter in word:
        require(letter >= 1, 'positive letter')
        result = 3 * result + 2**total
        total += letter
    return result


def trace(start, addend, word):
    states = [start]
    for letter in word:
        require(states[-1] != 0 and states[-1] % 2 == 1, 'nonzero odd input')
        raw = 3 * states[-1] + addend
        require(raw != 0 and valuation(raw) == letter, 'exact signed arrow')
        states.append(raw // 2**letter)
    require(states[-1] != 0 and states[-1] % 2 == 1, 'odd endpoint')
    return states


def cylinder_start(word):
    total = sum(word)
    modulus = 2**(total + 1)
    start = (2**total - intercept(word)) * pow(3**len(word), -1, modulus) % modulus
    require(start > 0 and start % 2 == 1, 'positive cylinder representative')
    return start


def log_interval(value, terms=80):
    z = F(value - 1, value + 1)
    low = 2 * sum((z**(2*j + 1) / (2*j + 1) for j in range(terms)), F(0))
    tail = 2 * z**(2*terms + 1) / ((2*terms + 1) * (1 - z*z))
    return low, low + tail


def prefix_checks():
    excesses = tuple(range(1, 7)) + (12, 27, 64)
    count = terminal = arrows = eligible_padic = 0
    branches = {'one': 0, 'U1': 0, 'U2': 0}
    for n in range(1, 6):
        for ell in range(1, 6):
            for w in range(6):
                for e in excesses:
                    for f in excesses:
                        A = (1,)*(n-1) + (e+1,) + (1,)*(ell-1) + (f+1,) + (1,)*w
                        a = len(A)
                        C = intercept(A)
                        ratio = F(C, 3**a)
                        U1 = 2**e * F(2, 3)**n
                        U2 = 2**(e+f) * F(2, 3)**(n+ell)
                        formula = (1 + (2**e-1)*F(2, 3)**n
                                   + 2**e*(2**f-1)*F(2, 3)**(n+ell)
                                   - 2**(e+f)*F(2, 3)**a)
                        require(ratio == formula, 'two-defect intercept identity')
                        for raise_last in (1, 3):
                            modified = A[:-1] + (A[-1]+raise_last,)
                            x = cylinder_start(modified)
                            states = trace(x, 1, modified)
                            ordinary_end = F(3**a*x + C, 2**sum(A))
                            require(ordinary_end == 2**raise_last * states[-1]
                                    and ordinary_end.denominator == 1
                                    and ordinary_end % 2 == 0, 'ordinary even output')
                            # K is chosen only for the local prefix inequality.
                            # No complete signed join or corresponding B is asserted.
                            K = 2 + 2*x/ratio
                            require(x < (K-1)*ratio and K > 1, 'chosen local enclosure')
                            if w == 0:
                                reduced = A[:-1] + (1,)
                                require(sum(letter > 1 for letter in reduced) == 1,
                                        'one-defect terminal reduction')
                                require(intercept(reduced) == C, 'last valuation absent from intercept')
                                reduced_end = F(3**a*x+C, 2**sum(reduced))
                                require(reduced_end == 2**f*ordinary_end
                                        and reduced_end % 2 == 0, 'reduced prefix ends even')
                                require(trace(x, 1, reduced[:-1]) == states[:-1],
                                        'terminal reduction preserves actual prefix')
                                terminal += 1
                            else:
                                y1, y2 = states[n], states[n+ell]
                                t0, t1, t2 = x+1, y1+1, y2+1
                                require(t0 % 2**n == 0 and t1 % 2**ell == 0,
                                        'initial and middle divisibilities')
                                t, s = t0 // 2**n, t1 // 2**ell
                                require(t >= 1 and s >= 1 and t % 2 == s % 2 == 1,
                                        'positive odd quotients')
                                require(3**n*t + 2**e - 1 == 2**(e+ell)*s,
                                        'exact earlier congruence')
                                require(3**ell*s == 2**f*y2+1, 'exact p-adic identity')
                                require(valuation(t2) == w and 2**w <= t2,
                                        'terminal-run valuation')
                                require(t1 == 1 + F(F(3, 2)**n*t0-1, 2**e),
                                        'first shifted recurrence')
                                require(t2 == 1 + F(F(3, 2)**ell*t1-1, 2**f),
                                        'second shifted recurrence')
                                require(t0 < K*(1+U1+U2), 'discarded negative intercept terms')
                                require(t1 <= F(3, 2)**n*t0
                                        and t2 <= F(3, 2)**ell*t1, 'convex shifted growth')
                                if 1 >= max(U1, U2):
                                    require(t0 < 3*K, 'one-dominant branch')
                                    branches['one'] += 1
                                elif U1 >= U2:
                                    require(t1 == t0/U1+1-F(1, 2**e), 'U1 expression')
                                    require(t1 < 4*K and 3**n < 3*K*2**e,
                                            'U1-dominant branch')
                                    branches['U1'] += 1
                                else:
                                    require(t2 == t0/U2 + (1-F(1, 2**e))*U1/U2
                                            + 1-F(1, 2**f), 'U2 expression')
                                    require(t2 < 5*K and y2 < 4*K, 'controlled second endpoint')
                                    require(3**(n+ell) < 3*K*2**(e+f+ell),
                                            'retained middle-run loss')
                                    require(valuation(2**f*y2+1, 3) >= ell,
                                            'p-adic divisibility')
                                    require(y2 % 2 == 1 and y2 % 3 != 0, 'p-adic units')
                                    eligible_padic += int(y2 >= 35)
                                    branches['U2'] += 1
                            count += 1
                            arrows += a
    require(count == 24300 and terminal == 4050, 'prefix coverage')
    require(all(branches.values()) and sum(branches.values()) + terminal == count,
            'all branches exercised')
    return {'scope': 'Actual finite integer prefixes with chosen local K; not complete signed joins.',
            'n_range': [1, 5], 'ell_range': [1, 5], 'w_range': [0, 5],
            'excesses': list(excesses), 'terminal_raises': [1, 3],
            'prefixes': count, 'exact_modified_arrows': arrows,
            'terminal_reductions': terminal, 'dominant_branches': branches,
            'U2_prefixes_with_padic_height_at_least_35': eligible_padic}


def constants_and_gap():
    low2, high2 = log_interval(2)
    low3, high3 = log_interval(3)
    require(F(1, 2) < low2 < high2 < 1, 'ln2 bounds')
    require(1 < low3 < high3 < F(11, 10), 'ln3 bounds')
    require(2**3 < 3**2 and 3**5 < 2**8 and 5**5 < 2**12,
            'alpha and log5 rational bounds')
    alpha_high = F(8, 5)
    require(1+alpha_high+alpha_high**2 < 6
            and (1+alpha_high+alpha_high**2)*(1+alpha_high) < 15,
            'one-dominant a bound')
    require(F(2, 3)+1+alpha_high < 4 and 3+2*alpha_high < 7,
            'U1-dominant a bound')
    require(1+alpha_high < 3
            and 1+alpha_high+alpha_high*(1+F(12, 5)) < 9,
            'U2-dominant weighted a bound')
    require((6*alpha_high+1)/F(2, 5) < 27
            and (15*alpha_high+1)/F(2, 5) < 63, 'one-dominant m bound')
    require((4*alpha_high+1)/F(2, 5) < 19
            and (11*alpha_high+1)/F(2, 5) < 47, 'U1-dominant m bound')
    require(F(1)/F(2, 5) == F(5, 2)
            and F(4)/F(2, 5) == 10 and F(10)/F(2, 5) == 25,
            'U2-dominant m bound')
    # Chim's theorem is cited, not proved here. These are exact overestimates
    # after substituting its rational field and p=3 parameters.
    chim_bracket = F(3, 2)*F(11, 10)+F(97, 20)
    coefficient = 13950*chim_bracket
    maximum_third_term = 180*chim_bracket*F(11, 10)
    require(chim_bracket == F(13, 2) and coefficient == 90675 < 100000,
            'Chim coefficient envelope')
    require(1000*high3 < 1100 and maximum_third_term == 1287 < 1300,
            'Chim H envelope')
    require(F(1217, 25)/low2 < 98 and F(8, 5)/2+1 < 2, 'LMN specialization')
    # R has positive coefficients, and thus R(j+1)/R(j) <= ((j+1)/j)^3.
    polynomial = [250000*1152686+23904, 250000*765874+15876,
                  250000*128086+2646, 250000*98]
    require(all(value > 0 for value in polynomial), 'positive cubic coefficients')
    k = 48
    H = 1+98*(k+3)**2
    R = 250000*(k+1301)*(H+3)+27*H+63
    require(sum(value*k**i for i, value in enumerate(polynomial)) == R,
            'cutoff polynomial expansion')
    require(R == 85965706382336 < 2**k and 49**3 < 2*48**3, 'all-large-length cutoff')
    lo, hi = low3/high2, high3/low2
    left, right = lo, hi
    pm2, pm1, qm2, qm1 = 0, 1, 1, 0
    convergents = []
    coefficients = []
    for _ in range(100):
        al, ah = left.__floor__(), right.__floor__()
        require(al == ah, 'ambiguous continued-fraction coefficient')
        pp, qq = al*pm1+pm2, al*qm1+qm2
        coefficients.append(al)
        convergents.append((pp, qq))
        if qq > 2**48:
            break
        left, right = 1/(right-al), 1/(left-al)
        pm2, pm1, qm2, qm1 = pm1, pp, qm1, qq
    else:
        raise RuntimeError('continued-fraction guard')
    p, q = convergents[-2]
    pnext, qnext = convergents[-1]
    require((p, q) == (83130157078217, 52449289519716), 'lower bracket')
    require((pnext, qnext) == (683381996816440, 431166034846567), 'upper bracket')
    require(F(p, q) < lo < hi < F(pnext, qnext), 'opposite bracket signs')
    require(pnext*q-p*qnext == 1 and q <= 2**48 < qnext, 'unimodular gap coverage')
    gap = q*lo-p
    require(gap > F(1, 2**62), 'positive gap power')
    # The manuscript's integer-coordinate sign argument covers every
    # 0<m<qnext, not a sampled set and not only m>=q.
    eta_bits = 64
    final = 250000*(48+1300)*(eta_bits+3)+27*eta_bits+63
    require(final == 22579001791, 'final half-length bound')
    period_path = ROOT / 'areas/cycles/results/cycle-length-lower-bound-from-convergents/cycle_length_convergents.json'
    period_data = json.loads(period_path.read_text())
    period = int(period_data['V3']['2^71']['least_m'])
    require(period == 72057431991 and 2*final == 45158003582 < period,
            'full odd-length comparison')
    return {'atanh_terms': 80, 'ln2_bounds': [str(low2), str(high2)],
            'ln3_bounds': [str(low3), str(high3)],
            'Chim_coefficient_upper': int(coefficient),
            'Chim_H_constant_upper': int(maximum_third_term),
            'half_length_cutoff': 2**48, 'cutoff_polynomial': polynomial,
            'dyadic_upper_at_48': R, 'continued_fraction_terms': coefficients,
            'lower_convergent': {'p': p, 'q': q},
            'upper_convergent': {'p': pnext, 'q': qnext},
            'positive_gap_lower': str(gap), 'gap_bits': 62, 'eta_bits': eta_bits,
            'final_half_length_upper': final, 'final_full_odd_length_upper': 2*final,
            'replayed_period_lower_bound': period,
            'period_receipt_sha256': sha256(period_path.read_bytes()).hexdigest(),
            'external_inputs': ['LMN', 'Chim Theorem 2.1', 'Barina through the replayed period theorem']}


def genuine_controls():
    path = ROOT / 'areas/cycles/results/bounded-unequal-half-defect-exclusion/check_bounded_halves.json'
    selected = [row for row in json.loads(path.read_text())['joins']
                if row['order'] == 'LH' and sum(letter > 1 for letter in row['A']) <= 2]
    require(len(selected) == 6, 'genuine join coverage')
    rows = []
    for row in selected:
        J, r, h = row['J'], row['r'], row['h']
        A, B = tuple(row['A']), tuple(row['B'])
        M, N = 2**r, 2**J
        z = trace(-h, M-1, A)[-1]
        require(z > 0 and trace(z, N-1, B)[-1] == h, 'signed join')
        require(J > r >= 1 and B[-1] > J, 'normal-form boundary hypotheses')
        u, v = list(A+B), list(A+B)
        u[len(A)-1] += J-r
        u[-1] -= J
        v[-1] += r
        word = u+v
        a, b = len(A), len(B)
        m, S = a+b, sum(A)+sum(B)
        require(len(word) == 2*m and sum(word) == 2*S and min(word) >= 1,
                'full word clock and total')
        C, D = intercept(word), 2**(2*S)-3**(2*m)
        require(D > 0, 'positive denominator')
        q, x = D//gcd(C, D), F(C, D)
        X = q*x
        require(X.denominator == 1 and X > 0, 'integer reduced state')
        states = trace(X.numerator, q, word)
        require(states[-1] == X and min(states) > 0, 'positive reduced cycle')
        require(F(states[m], q) == M*x+h and x == F(row['canonical_state']),
                'canonical half closure')
        lam = F(3**m, 2**S)
        eta = 1-lam
        kappa = (lam+F(1, M))/eta
        require(x < kappa*F(intercept(A), 3**a), 'normalized rational enclosure')
        ordinary_end = F(3**a*X.numerator+q*intercept(A), 2**sum(A))
        require(ordinary_end == 2**(J-r)*states[a] and ordinary_end % 2 == 0,
                'q-scaled ordinary even terminal')
        require(q > 1, 'control retains denominator greater than one')
        rows.append({'J': J, 'r': r, 'h': h, 'interface': z,
                     'A': list(A), 'B': list(B), 'defects_in_A': sum(v > 1 for v in A),
                     'half_length': m, 'full_odd_length': 2*m, 'half_total': S,
                     'normalized_state': str(x), 'denominator': q,
                     'actual_minimum': min(states), 'failed_hypothesis': 'q=1'})
    require(sum(row['defects_in_A'] == 2 for row in rows) == 1, 'two-defect genuine control')
    return {'source_receipt_sha256': sha256(path.read_bytes()).hexdigest(),
            'count': len(rows), 'records': rows,
            'scope': 'Complete genuine joins; normalized rational states are not treated as q=1 integers.'}


def separated_prefix_control():
    A = (2, 1, 1, 3, 1, 1, 1, 1)
    modified = A[:-1]+(2,)
    positive = trace(73, 1, modified)
    signed = trace(-73, 2047, A)
    ordinary_end = F(3**len(A)*73+intercept(A), 2**sum(A))
    K_threshold = 1+F(73*3**len(A), intercept(A))
    require(ordinary_end == 242 and positive[-1] == 121 and signed[-1] == 16421,
            'separate prefix endpoints')
    require(K_threshold == F(495616, 16663), 'local enclosure threshold')
    return {'A': list(A), 'positive_modified_trace': positive, 'signed_first_trace': signed,
            'signed_addend': 2047, 'r': 11, 'h': 73, 'interface': 16421,
            'ordinary_even_terminal': 242, 'local_K_threshold': str(K_threshold),
            'scope': 'An exact positive prefix and first signed segment only; no B or complete join is claimed.'}


def standard_controls():
    path = ROOT / 'areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json'
    rows = []
    for fixture in json.loads(path.read_text())['cycles']:
        d, states, word = fixture['d'], fixture['states'], fixture['valuations']
        require(trace(states[0], d, word) == states+[states[0]], 'standard cycle arrows')
        C, D = intercept(word), 2**sum(word)-3**len(word)
        q = D//gcd(C, D)
        require(D > 0 and F(C, D) == F(states[0], d), 'standard cycle identity')
        require(q > 1 and d % q == 0, 'standard denominator')
        rows.append({'addend': d, 'odd_period': len(word), 'denominator': q,
                     'failed_hypothesis': 'q=1'})
    require(len(rows) == 11 and {row['addend'] for row in rows} == {5, 7, 13, 61},
            'all standard addends')
    return {'fixture_sha256': sha256(path.read_bytes()).hexdigest(),
            'count': len(rows), 'records': rows}


def main():
    require(sys.argv[1:] in ([], ['--write-receipt']), 'usage: script [--write-receipt]')
    receipt = {'schema': 'two-defect-first-block-v1',
               'finite_prefixes': prefix_checks(), 'arithmetic': constants_and_gap(),
               'genuine_joins': genuine_controls(),
               'separate_prefix_control': separated_prefix_control(),
               'standard_cycles': standard_controls()}
    target = HERE / 'check_two_defects.json'
    encoded = json.dumps(receipt, indent=2, sort_keys=True)+'\n'
    if sys.argv[1:]:
        target.write_text(encoded)
    else:
        require(target.read_text() == encoded, 'receipt mismatch; regenerate explicitly')
    print(json.dumps({'status': 'passed', 'finite_prefixes': receipt['finite_prefixes']['prefixes'],
                      'genuine_joins': receipt['genuine_joins']['count'],
                      'standard_cycles': receipt['standard_cycles']['count'],
                      'full_odd_length_upper': receipt['arithmetic']['final_full_odd_length_upper']},
                     sort_keys=True))


if __name__ == '__main__':
    main()
