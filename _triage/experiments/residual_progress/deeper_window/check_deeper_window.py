"""Replay the complete selective basin and finite original-Q suffix window."""
import argparse
from fractions import Fraction as F
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

import deeper_window as W
import sparse_basin as S

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                    separators=(',', ':')).encode()).hexdigest()


def reject(call, exception=ValueError):
    try:
        call()
    except exception:
        return
    raise AssertionError('expected explicit rejection')


def v2(n):
    assert n != 0
    n = abs(n)
    return (n & -n).bit_length()-1


def nu(x):
    assert type(x) is int and x > 0 and x % 2
    extra = 0
    while x % 8 == 5:
        x = (x-1)//4
        extra += 2
    if x % 4 == 3:
        a = v2(x+1)
        if ((x+1)//2**a) % 4 == pow(3, a, 4):
            x = (x-1)//2
            extra += 1
    return x, extra


def quotient(x):
    assert nu(x)[0] == x
    if x == 1:
        return 1, 0
    a = v2(3*x+1)
    y, extra = nu((3*x+1)//2**a)
    return y, a+extra


def syracuse(x, count):
    for _ in range(count):
        if x != 1:
            x = (3*x+1)//2**v2(3*x+1)
    return x


def positive_magnitude_step(u):
    """Independent sign-converted replay for every stored rational hit arrow."""
    z = 3*u-S.D
    e = v2(z)
    z //= 2**e
    if z <= S.D:
        return z, e
    while z % 8 == 3:
        z = (z+S.D)//4
        e += 2
    if z % 4 == 1:
        a = v2(S.D-z)
        if ((S.D-z)//2**a) % 4 == pow(3, a, 4):
            z = (z+S.D)//2
            e += 1
    return z, e


def family(r, index):
    # Independent solution of the original binary congruence.
    modulus = 2**(19*r)
    offset = (S.D*W.V0+S.B)//2**18
    residue = (-offset*pow(S.D*3**18, -1, modulus)) % modulus
    ell = residue+modulus*index
    v0, q = W.V0+W.VP*ell, W.Q0+W.QP*ell
    current = v0
    for _ in range(r):
        assert v2(S.D*current+S.B) >= 37
        assert (S.A*current+S.B) % S.M == 0
        current = (S.A*current+S.B)//S.M
    return ell, v0, q, 3*current


def audit():
    # All displayed small constants are checked independently as exact fractions.
    C = F(243*2**18-3*S.B, S.D)
    kappa = F(2**27, 3**18)
    assert F(3, 2)**14*kappa == F(8192, 81)
    margin102 = F(70, 81)*C-102*F(243, 32)
    marginhalf = (1-2*kappa)*C-F(3, 2)**19
    assert margin102 == F(21052290557, 3090096) > 0
    assert marginhalf == F(232269104057100257855, 484305580032786432) > 0
    assert S.D+102*(S.T0+12*S.A) == 741545113
    assert 2**21 < F(3**14, 2) < 2**22
    assert [m for m in range(-20, 30) if 1 <= F(2)**m/243 < 102] == list(range(8, 15))
    assert S.A-S.M == S.D and S.ROOT == -W.ROOT

    basin = S.classify()
    assert basin['cap_hits'] == 0
    assert basin['candidates'] == 67992 and basin['canonical_count'] == 33995
    assert len(basin['hits']) == 16 and basin['hits'] == basin['relevant_hits']
    assert all(row[4] for row in basin['hit_details'])
    paths = {row['origin']: row for row in basin['first_hit_paths']}
    first_hit_arrows = 0
    for u, depth, cost in basin['hits']:
        path = paths[u]
        assert path['signed_numerators'][0] == -u
        assert path['signed_numerators'][-1] == S.ROOT
        assert S.ROOT not in path['signed_numerators'][:-1]
        assert len(path['exponents']) == depth and sum(path['exponents']) == cost
        for left, right, e in zip(path['signed_numerators'],
                                  path['signed_numerators'][1:], path['exponents']):
            assert positive_magnitude_step(-left) == (-right, e)
            first_hit_arrows += 1

    full = json.loads((HERE/'full_basin_audit.json').read_text())
    assert full['bound'] == 741545113 and full['candidates'] == 176754119
    assert len(full['hits']) == 1939 and full['cap_hits'] == 0
    full_hits = {u: (d, e) for u, d, e in full['hits']}
    fp = hashlib.sha256()
    for m, u, canonical in S.candidates():
        if not canonical:
            status, d, e = 0, 0, 0
        elif u in full_hits:
            status = 2
            d, e = full_hits[u]
        else:
            status, d, e = 1, 0, 0
        fp.update(S.row_bytes(m, u, status, d, e))
    assert fp.hexdigest() == basin['classification_sha256']
    filtered = []
    for u, d, e in full['hits']:
        if d % 12 != 5:
            continue
        m = e-19*((d-5)//12)
        if 8 <= m <= 14 and 243*(u-S.D) < 2**m*(S.T0+12*S.A):
            filtered.append([u, d, e])
    assert filtered == basin['hits']

    suffixes, all_nodes, pruned_nodes = [], 0, 0
    terminals, successes = [], []
    for hit in basin['hits']:
        data = W.enumerate_suffixes(hit)
        pruned = W.pruned_suffixes(hit)
        assert data['terminal_rows'] == pruned['terminal_rows']
        assert data['successes'] == pruned['successes']
        all_nodes += data['nodes']
        pruned_nodes += pruned['nodes']
        for row in data['terminal_rows']:
            assert row['depth'] <= 14 and row['cost'] <= 21
            assert F(*row['score']) < F(1, 2)
            assert F(*row['slope_ratio']) == F(row['period'], W.QP)
            assert F(*row['slope_ratio']) == F(2)**(data['boundary']['m']+row['cost']-27)*F(3)**(13-row['depth'])
            # Replay the entire affine word independently, including every offset.
            x0, period, exponents = data['boundary']['x0'], data['boundary']['period'], 0
            for kind, index, exponent, b in row['word']:
                assert (2**exponent*x0+b) % 3 == 0 and period % 3 == 0
                x0, period = (2**exponent*x0+b)//3, period*2**exponent//3
                exponents += exponent
                assert index <= 3 and exponent >= 1
            assert (x0, period, exponents) == (row['p0'], row['period'], row['cost'])
            terminals.append(dict(origin=hit[0], **row))
        successes.extend(dict(origin=hit[0], **row) for row in data['successes'])
        suffixes.append(data)
    assert all_nodes == 7036
    assert len(terminals) == 2 and len(successes) == 1
    assert [(row['origin'], row['depth'], row['cost'], row['relation']) for row in terminals] == [
        (952661, 11, 16, '(9Q+5)/8'), (952661, 13, 19, 'Q')]
    assert successes[0]['relation'] == 'Q'
    assert all(row['strict_interval'] is None for row in terminals)

    # Full current-window parameters, exact first-hit affine values and both clocks.
    controls = []
    boundary_instances = terminal_instances = 0
    for r in (0, 1, 2, 4, 8, 16, 128):
        for index in (0, 1, 7):
            ell, v0, q, target = family(r, index)
            assert W.guard(r) == [ell % 2**(19*r), 2**(19*r)]
            assert q == kappa*(3*v0)-F(213949807, 3**17)
            assert 3*v0 > 2*q
            center = S.D*v0+S.B
            assert center % 81 == 0 and center % 243 != 0
            assert center >= 81*2**(19*r+18)
            n0, error = 3*v0, F(243, 32)*2**(7*r)
            assert n0 >= C*2**(7*r)
            assert F(3, 2)**14*(q+1)/(n0+1-error) < 102
            assert n0+1-F(3, 2)**19*2**(7*r) > 2*q
            current, total_cost = q, 0
            for _ in range(18+12*r):
                current, e = quotient(current)
                total_cost += e
            assert current == target and total_cost == 27+19*r
            assert syracuse(q, 23+12*r) == syracuse(target, 5)
            observed = []
            for data in suffixes:
                bd = data['boundary']
                if r < bd['k']:
                    continue
                path = paths[bd['u']]
                vk = v0
                for _ in range(bd['k']):
                    vk = (S.A*vk+S.B)//S.M
                actual = 3*vk
                for j in reversed(range(path['depth'])):
                    exponent = path['exponents'][j]
                    alpha = F(2**exponent, 3)
                    beta = (F(path['signed_numerators'][j])-
                            alpha*path['signed_numerators'][j+1])/S.D
                    previous = alpha*actual+beta
                    assert previous.denominator == 1
                    previous = int(previous)
                    assert quotient(previous) == (actual, exponent)
                    actual = previous
                assert actual == bd['x0']+bd['period']*ell
                assert actual == (2**bd['m']*(center//81)-bd['u'])//S.D
                assert (2**bd['m']*(center//81)-bd['u']) % S.D == 0
                assert actual > q
                boundary_instances += 1
                for row in data['terminal_rows']:
                    p = row['p0']+row['period']*ell
                    y, cost = p, 0
                    for _ in range(row['depth']):
                        y, e = quotient(y)
                        cost += e
                    assert y == actual and cost == row['cost']
                    assert (p == q) == (row['relation'] == 'Q')
                    assert (p > q) == (row['relation'] == '(9Q+5)/8')
                    terminal_instances += 1
                observed.append([bd['u'], digest(hex(actual))])
            controls.append(dict(returns=r, index=index, ell=ell,
                                 quotient_clock=18+12*r, quotient_cost=total_cost,
                                 ordinary_clocks=[23+12*r, 5],
                                 target_digest=digest(hex(target)), boundary_values=observed))

    # Exact original-Q interval and guard boundaries, independent of basin success.
    interval_checks = []
    examples = [(W.Q0, W.QP), (W.Q0-1, W.QP), (W.Q0+1, W.QP),
                (W.Q0-5, W.QP+1), (W.Q0+5, W.QP-1),
                (W.Q0+5, W.QP+1), (W.Q0-5, W.QP-1),
                (-2*W.QP, W.QP), (0, 1), (-10, 3),
                (W.Q0, 1), (W.Q0+1, 1)]
    for p0, period in examples:
        for strict in (False, True):
            interval = W.comparison_interval(p0, period, strict)
            for ell in range(64):
                present = interval is not None and ell >= interval[0] and (interval[1] is None or ell <= interval[1])
                p, q = p0+period*ell, W.Q0+W.QP*ell
                assert present == (p > 0 and (p < q if strict else p <= q))
            for r in (0, 1, 2, 4):
                got = W.first_guarded(interval, r)
                if interval is None:
                    assert got is None
                else:
                    residue, modulus = W.guard(r)
                    expect = interval[0]+(residue-interval[0]) % modulus
                    if interval[1] is not None and expect > interval[1]:
                        expect = None
                    assert got == expect
            interval_checks.append([p0, period, strict, interval])

    bad = [lambda: S.valuation(0), lambda: S.valuation(True),
           lambda: S.normalize(-S.D), lambda: S.normalize(-3*S.D),
           lambda: S.normalize(-899840), lambda: S.normalize(True),
           lambda: S.step(-S.ROOT), lambda: S.classify(max_path=True),
           lambda: W.guard(-1), lambda: W.guard(True),
           lambda: W.boundary([952661, 5, True]), lambda: W.boundary([952661, 4, 8]),
           lambda: W.boundary([952660, 5, 8]), lambda: W.boundary([952663, 5, 8]),
           lambda: W.boundary([952661, 5, 7]), lambda: W.boundary([952661, 5, 15]),
           lambda: W.boundary('not a certificate'),
           lambda: W.comparison_interval(1, 0), lambda: W.comparison_interval(True, 1),
           lambda: W.comparison_interval(1, 1, 1),
           lambda: W.first_guarded([-1, 5], 0), lambda: W.first_guarded([5, 4], 1),
           lambda: W.first_guarded([True, None], 0), lambda: W.enumerate_suffixes([1, 5, 8])]
    for call in bad:
        reject(call)
    cap_tests = [lambda: S.classify(max_path=1), lambda: S.classify(max_states=1),
                 lambda: S.classify(max_bits=1)]
    for call in cap_tests:
        reject(call, RuntimeError)

    files = [Path(__file__).resolve(), HERE/'sparse_basin.py', HERE/'deeper_window.py',
             HERE/'DEEPER_WINDOW.md', HERE/'independent_basin.cpp', HERE/'full_basin_audit.json',
             HERE.parent/'shadow_precision/SHADOW_PRECISION.md',
             HERE.parent/'shadow_precision/shadow_precision.py',
             HERE.parent/'shadow_precision/shadow_precision_audit.json',
             HERE.parent/'shadow_precision/independent_basin.cpp',
             HERE.parent/'phi_exit_control/PHI_EXIT_CONTROL.md',
             HERE.parent/'phi_exit_control/phi_exit_control.py',
             HERE.parent/'phi_exit_control/phi_exit_control_audit.json']
    return dict(status='PASS',
                scope='Complete original-source inverse history classification through12r+19; only Q at12r+18. No all-depth exclusion or terminal-current supply.',
                margins=dict(mu102=str(margin102), whole_half=str(marginhalf)),
                sparse_basin=basin, independent_full_basin=dict(
                    candidates=full['candidates'], hits=len(full['hits']),
                    classification_fingerprint=full['classification_fingerprint'],
                    cap_hits=full['cap_hits'], sparse_outcomes_compared=basin['canonical_count']),
                first_hit_arrows=first_hit_arrows, suffixes=suffixes,
                suffix_nodes=all_nodes, pruned_suffix_nodes=pruned_nodes,
                score_eligible_terminals=terminals, nonstrict_successes=successes,
                positive_families=len(controls), boundary_instances=boundary_instances,
                terminal_instances=terminal_instances, positive_controls=controls,
                interval_checks=interval_checks, invalid_rejections=len(bad),
                explicit_cap_abort_checks=len(cap_tests),
                source_sha256={str(path.relative_to(ROOT)):hashlib.sha256(path.read_bytes()).hexdigest()
                               for path in sorted(files)})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', '--write-receipt', action='store_true')
    parser.add_argument('--cpp', action='store_true')
    args = parser.parse_args()
    result = audit()
    if args.cpp:
        compiler = shutil.which(os.environ.get('CXX', 'c++'))
        if compiler is None:
            raise RuntimeError('C++17 compiler unavailable')
        with tempfile.TemporaryDirectory(prefix='collatz-r92-') as folder:
            executable = Path(folder)/'independent_basin'
            subprocess.run([compiler, '-O2', '-std=c++17', '-Wall', '-Wextra',
                            str(HERE/'independent_basin.cpp'), '-o', str(executable)],
                           check=True, timeout=60)
            independent = json.loads(subprocess.check_output([str(executable)], timeout=120))
            assert independent == json.loads((HERE/'full_basin_audit.json').read_text())
    receipt = HERE/'deeper_window_audit.json'
    if args.write:
        receipt.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    else:
        assert json.loads(receipt.read_text()) == result
    print('PASS R92:', result['sparse_basin']['candidates'], 'odd candidates,',
          result['sparse_basin']['canonical_count'], 'canonical origins,',
          len(result['sparse_basin']['hits']), 'tails,', result['suffix_nodes'],
          'suffix nodes,', len(result['nonstrict_successes']), 'equality history;',
          'C++ PASS' if args.cpp else 'C++ not requested')


if __name__ == '__main__':
    main()
