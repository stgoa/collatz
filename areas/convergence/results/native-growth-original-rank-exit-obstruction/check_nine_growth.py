"""Independent bounded replay of exact native growth/current identities."""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from types import ModuleType
import nine_growth as M

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def step(x):
    if x == 1:
        return 1
    n = 3*x+1
    while n % 2 == 0:
        n //= 2
    return n


def v2(n):
    count = 0
    while n % 2 == 0:
        count += 1
        n //= 2
    return count


def direct_divergence(rows):
    result = Counter()
    for x, c in rows.items():
        assert x > 1 and x % 2 and isinstance(c, int) and c
        result[x] += c
        y = step(x)
        if y != 1:
            result[y] -= c
    return {x: c for x, c in result.items() if x != 1 and c}


def boundary(plan):
    expected = Counter({3*plan['seed']: 1, plan['seed']: -1})
    for u, c in plan['coefficients'].items():
        expected[3*u] -= c
        expected[u] += c
    expected = {x: c for x, c in expected.items() if x != 1 and c}
    assert direct_divergence(plan['current']) == expected


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def sources():
    pending, seen = [M], set()
    paths = {Path(__file__).resolve(), HERE/'NATIVE_NINE_GROWTH.md'}
    while pending:
        module = pending.pop()
        if id(module) in seen:
            continue
        seen.add(id(module))
        filename = getattr(module, '__file__', None)
        if not filename:
            continue
        path = Path(filename).resolve()
        if not path.is_relative_to(ROOT):
            continue
        paths.add(path)
        pending.extend(x for x in vars(module).values() if isinstance(x, ModuleType))
    return {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(paths)}


def lift_log(target, depth):
    """Unique log base64 in1+9Z modulo3^depth; tiny exact digit lift only."""
    value, period = 0, 1
    assert target % 9 == 1
    for precision in range(3, depth+1):
        modulus = 3**precision
        choices = [value+k*period for k in range(3)
                   if pow(64, value+k*period, modulus) == target % modulus]
        assert len(choices) == 1
        value = choices[0]
        period *= 3
    return value


def audit():
    records = []
    cylinders = 0
    for r in range(41):
        residue, modulus = M.cylinder(r)
        assert modulus == 2**(13+9*r)
        for offset in (0, 1, 7):
            b = residue+offset*modulus
            x = b
            for _ in range(r):
                assert x % 8192 == 905
                assert (729*x+223) % 512 == 0
                x = (729*x+223)//512
            assert x % 8192 == 905 and x == M.affine_iterate(b, r)
            assert v2(217*b+223) >= 13+9*r
            cylinders += 1
    phases = 0
    for h in range(13, 22):
        for offset in range(24):
            b = M.exact_family(0, h, offset)
            result = M.exit_phase(b)
            assert result['order'] == h
            row = M.native_step(b)
            assert row['target'] % 8192 != 905
            direct = 3*b
            for valuation in (1, 2, 1, 1, 1, 2):
                assert v2(3*direct+1) == valuation
                direct = step(direct)
            assert direct == 6*row['target']+1
            assert direct_divergence(row['current']) == {3*b: 1, 3*row['target']: -1}
            records.append(['phase', b, h, result['d'], result['canonical_upper']])
            phases += 1
    exits, undos, returns = 0, 0, 0
    fixtures = []
    for r in range(9):
        for offset in range(3):
            b = M.exact_family(r, 17, offset)
            x, count = b, 0
            while True:
                y = (729*x+223)//512
                if y % 8192 != 905:
                    break
                count += 1
                x = y
            assert count == r == M.return_count(b)
            assert v2(217*x+223) == 17
            plan = M.exit_plan(b)
            boundary(plan)
            z = plan['target']
            assert (3*z < 3*b) == (r == 0)
            assert plan['coefficients'][z] == 1
            assert all(M.B.rho(u) < 3*z for u in plan['coefficients'] if u != z)
            left, right = 3*b, 3*z
            for _ in range(6*r+12):
                left = step(left)
            for _ in range(4):
                right = step(right)
            assert left == right
            # The last exit has quotient time6r+8; it is not its ordinary left clock.
            x = 3*b
            for _ in range(6*r+8):
                x = M.N.quotient_step(x)
            assert x == 3*z
            exits += 1
            if r:
                returned = M.return_composition(b)
                boundary(returned)
                returns += 1
            for ray in (4, 8):
                restored = M.standard_inverse_undo(b, ray)
                boundary(restored)
                undos += 1
            records.append(['exit', b, r, z, digest(sorted(plan['current'].items())),
                            sorted(plan['coefficients'].items())])
            if offset == 0 and r in (1, 2):
                fixtures.append(plan)
    bounds = 0
    for index in range(512):
        w = 9+16*index
        local = M.B.nine_candidate(w)
        if local['status'] == 'descending':
            bound = Fraction(81*w+23, 32)
            assert all(M.B.rho(u) <= bound for u in local['coefficients'])
            bounds += 1
    # The fixed-point contraction is exact on its own restricted operation set.
    for initial in (27, 2715, 100001):
        value = Fraction(initial)
        for k in range(1, 25):
            value = (27*value+23)/32
            assert value == Fraction(23, 5)+Fraction(27, 32)**k*(initial-Fraction(23, 5))
    logs = []
    for s in (1, 2):
        depth = 6*s+4
        modulus = 3**depth
        for denominator in (3268, 8272):
            target = 217*pow(denominator, -1, modulus) % modulus
            L = lift_log(target, depth)
            logs.append([s, denominator, L])
    assert logs == [[1, 3268, 6069], [1, 8272, 740],
                    [2, 3268, 2466444], [2, 8272, 2028089]]
    bad = [lambda: M.order(1), lambda: M.order(True), lambda: M.order(-905),
           lambda: M.cylinder(-1), lambda: M.cylinder(True),
           lambda: M.exact_family(1, 12), lambda: M.exact_family(1, 22),
           lambda: M.exact_family(1, 17, -1), lambda: M.native_step(9),
           lambda: M.growth_plan(905, 0),
           lambda: M.growth_plan(M.exact_family(0), 2),
           lambda: M.exit_plan(M.exact_family(0, 18)),
           lambda: M.exit_phase(M.exact_family(1)),
           lambda: M.return_composition(M.exact_family(0)),
           lambda: M.standard_inverse_undo(M.exact_family(0), 16),
           lambda: M.affine_iterate(1, 1)]
    rejected = 0
    for call in bad:
        try:
            call()
        except (ValueError, TypeError):
            rejected += 1
        else:
            raise AssertionError('Invalid input accepted')
    return dict(status='PASS', cylinders=cylinders, binary_exit_cases=phases,
                full_H17_comparisons=exits, full_R40_R75_return_equalities=returns,
                full_inverse_undos=undos, nonblocked_bound_cases=bounds,
                modular_candidates=logs, rejected=rejected,
                record_hash=digest(records), fixtures=fixtures, source_hashes=sources(),
                scope='Finite exact implementation audit; written proof supplies universal guarded identities. No new accepted rule or universal stopping theorem.')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write-receipt', action='store_true')
    args = parser.parse_args()
    result = audit()
    data = json.dumps(result, indent=2, sort_keys=True)+'\n'
    path = HERE/'nine_growth_audit.json'
    if args.write_receipt:
        path.write_text(data)
    else:
        assert json.loads(path.read_text()) == json.loads(data), 'Stored receipt differs'
    print('PASS: native W9 guarded growth; '+json.dumps(
        {k: v for k, v in result.items() if k not in ('fixtures', 'source_hashes')}, sort_keys=True))


if __name__ == '__main__':
    main()
