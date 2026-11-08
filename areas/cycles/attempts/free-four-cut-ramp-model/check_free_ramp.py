"""Exact countercontrols for the free four-cut finite-horizon ramp attempt.

The controls are circle configurations, not cycle words. Actual-cycle
checks retain the true addend and verify only the surviving ramp/run laws.
No search solver, floating-point arithmetic, or absence census is used.
"""
from fractions import Fraction as F
from hashlib import sha256
import json
from math import gcd
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
R = F(3, 8)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def ramp(x):
    x %= 1
    return x if x else F(1)


def rotation_rows(h, base, horizon):
    output = []
    for j in range(1, horizon+1):
        raw = [(c-i*h) % 1 for c in base for i in range(j)]
        cuts = sorted(set(raw))
        witnesses = []
        for index, end in enumerate(cuts):
            previous = cuts[index-1]
            gap = (end-previous) % 1
            paired = max(ramp(end), ramp(end+j*h))
            require(gap > 0 and paired > 0, 'positive circular gap and witness')
            witnesses.append(dict(end=str(end), previous=str(previous), gap=str(gap),
                                  partner=str((end+j*h) % 1), paired_height=str(paired),
                                  deficit=str(gap-R*paired)))
        output.append(dict(j=j, raw_count=len(raw), distinct_count=len(cuts),
                           maximum_deficit=str(max(F(row['deficit']) for row in witnesses)),
                           minimum_coefficient=str(max(F(row['gap'])/F(row['paired_height'])
                                                       for row in witnesses)),
                           witnesses=witnesses))
    return output


def geometry_controls():
    controls = [
        ('order18', F(7, 18), list(map(F, ['2/9', '61/128', '799/1152', '383/384'])),
         F(-7, 9216), F(155, 9216), F(94, 253)),
        ('order14751', F(5734, 14751), list(map(F, ['0', '3283/14751', '2347/4917', '932/1341'])),
         F(-11, 10728), F(235, 14751), F(1216, 3283)),
    ]
    output = {}
    for name, h, base, expected, failure, coefficient in controls:
        require(0 < h < F(1, 2) and h.denominator > 17, 'nonidentity first17 shifts')
        require(len(set(base)) == 4 and all(0 <= c < 1 for c in base), 'four distinct cuts')
        require(not any((b-a) % 1 == h for a in base for b in base),
                'no prescribed anchored h-separated pair')
        rows = rotation_rows(h, base, 18)
        maximum = max(F(row['maximum_deficit']) for row in rows[:17])
        require(maximum == expected < 0, 'strict zero-error survival through17')
        require(F(rows[17]['maximum_deficit']) == failure > 0, 'first failure18')
        required_coefficient = max(F(row['minimum_coefficient']) for row in rows[:17])
        require(required_coefficient == coefficient > F(37, 100), 'sharper coefficients remain open')
        output[name] = dict(h=str(h), rotation_order=h.denominator, cuts=list(map(str, base)),
                            maximum_through17=str(maximum), first_failing_rotation=18,
                            eighteenth_is_identity=(18*h).denominator == 1,
                            minimum_coefficient_through17=str(coefficient), rotations=rows)
    require(output['order18']['eighteenth_is_identity'], 'small-control identity caveat')
    require(not output['order14751']['eighteenth_is_identity'], 'large-order failure is nonidentity')
    require(any(row['distinct_count'] < row['raw_count']
                for row in output['order14751']['rotations']), 'coincidence/dedup control')
    require(3**2 > 2**3 and 3**5 < 2**8, 'elementary alpha interval')
    require(3**63 < 2**100, 'actual ramp coefficient is below37/100')
    return output


def actual_controls():
    fixture = ROOT/'areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json'
    raw = fixture.read_bytes()
    rows = json.loads(raw)['cycles']
    arrows = ramp_checks = run_checks = 0
    for row in rows:
        q, states, word = row['d'], row['states'], row['valuations']
        require(q in (5, 7, 13, 61), 'true fixture addend')
        m = len(word)
        minimum_index = states.index(min(states))
        states = states[minimum_index:]+states[:minimum_index]
        word = word[minimum_index:]+word[:minimum_index]
        L, E = states[0], sum(word)
        require(len(set(states)) == m, 'primitive fixture states')
        for i, a in enumerate(word):
            require(a >= 1 and states[i] > 0 and states[i] % 2, 'positive odd exact state')
            require(3*states[i]+q == 2**a*states[(i+1) % m], 'true-addend arrow')
            require(states[i]*2**i*3**m <= L*3**i*2**E,
                    'universal ramp in exact integer powers')
            arrows += 1
            ramp_checks += 1
        for h in range(1, m):
            base = {i for i in range(m) if word[i] != word[(i+h) % m]}
            require(base, 'nonidentity primitive valuation rotation')
            order = m//gcd(h, m)
            for j in range(1, min(17, order-1)+1):
                cutset = sorted({(c-i*h) % m for c in base for i in range(j)})
                for index, end in enumerate(cutset):
                    previous = cutset[index-1]
                    length = (end-previous) % m-1
                    start = (previous+1) % m
                    require(all(word[(start+k) % m] == word[(start+k+j*h) % m]
                                for k in range(length)), 'raw union refines actual mismatches')
                    A = sum(word[(start+k) % m] for k in range(length))
                    first_difference = states[(start+j*h) % m]-states[start]
                    last_difference = states[(end+j*h) % m]-states[end]
                    require(first_difference and first_difference % 2**(A+1) == 0,
                            'nonzero odd-pair integrality')
                    require(last_difference == 2*3**length*(first_difference//2**(A+1)),
                            'exact agreeing-run difference')
                    require(max(states[end], states[(end+j*h) % m]) > 2*3**length,
                            'actual end-witness clock')
                    run_checks += 1
    require(len(rows) == 11 and arrows == 106, 'all shared standard fixtures')
    return dict(cycles=len(rows), arrows=arrows, ramp_checks=ramp_checks,
                refined_agreement_runs=run_checks, fixture_sha256=sha256(raw).hexdigest(),
                scope='True 3x+q addends retained. These checks do not impose the q=1 error bound.')


def main():
    require(sys.argv[1:] in ([], ['--write-receipt']), 'usage: checker [--write-receipt]')
    result = dict(schema='free-four-cut-ramp-model-v1', geometry_controls=geometry_controls(),
                  actual_cycle_controls=actual_controls(),
                  scope='Exact finite circle countercontrols and surviving identities; no cycle counterexample or general method limit.')
    encoded = json.dumps(result, sort_keys=True, indent=2)+'\n'
    destination = HERE/'check_free_ramp.json'
    if sys.argv[1:]:
        destination.write_text(encoded)
    else:
        require(destination.read_text() == encoded, 'receipt mismatch; inspect before regenerating')
    print(json.dumps(dict(status='passed', geometric_controls=2, rotations_per_control=18,
                         actual_cycles=result['actual_cycle_controls']['cycles'],
                         actual_arrows=result['actual_cycle_controls']['arrows'],
                         refined_runs=result['actual_cycle_controls']['refined_agreement_runs']), sort_keys=True))


if __name__ == '__main__':
    main()
