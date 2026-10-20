"""Self-contained recomputation of the coupled C(v) recursion and the A-entry d=4 bridges.

Written at the B10-residual-R25-R39 migration; the legacy scripts in this folder
load ../pair_one/pair_one.py (and through it the R33, R30, R26, R25 and R23
modules) by their pre-migration paths and no longer run. Standard library, exact
integers, own Syracuse step and own elementary normal form. Run from the
repository root: python3 <this file>. Exits 1 on any failure; writes nothing.

Checks, against even_pair_audit.json and the two stored weight-2 current tables
in this folder:
  - the 57 joint cylinders (depth 0..16, 32, 64; three representatives each):
    the cylinder recursion (5), the recognizer's depth and terminal class
    v = 39 mod 8192, the terminal words (2,2,3,6) and (1,1,2,1,4,1),
    S^(r+5)(18v+3) = S^(r+7)(v), and the explicit current for C(v) (local currents
    of divergence C(parent) - C(child), plus the terminal prefixes) has divergence
    [18v+3] - [v]; parameter_bits, clock, rows and sha256 of every receipt row;
    the half modulus 4096 loses the left terminal word (v = 4135);
  - the A-entry original cylinders (11) for a = 2, 5, 8, 32 and joint depth
    1, 2, 8, 32: exact a and d = 4, w = 17 mod 128 with an accepted joint child,
    w = 2 mod 3, S^(a+1)(x) = 18w+1, S^(a-1)(q) = w, the equal clock
    S^(a+r+7)(x) = S^(a+r+7)(q), the old return 9w > x for a >= 5; bits and clock
    of the receipt's A rows;
  - the six A-entry actual sources (a = 5, 8, 32; weights 1, 2): the required-ray
    cutoff, the root, its residual weight, the lower seed and the equal clock;
    for the six B-entry sources, the stored root has weight, d = 4,
    w = 105 mod 256 and the stated equal clock (the B cylinder is not rebuilt);
  - the twelve A-entry fixed-cylinder counts: explicit enumeration equals the CRT
    floor count and |mass - 25N/(72L)| <= 6;
  - both stored weight-2 conversions: branch_A/B_weight2_current.csv are
    positive, have divergence exactly 2[root], and match rows and sha256.
It does not rebuild the B entry, the split-catalogue success set or the 8192
paired nonacceptances, which need the R33 recognizer (legacy checker, evidence
only).
"""

import csv
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
failures = []


class Reject(Exception):
    pass


def require(ok, message):
    if not ok:
        failures.append(message)


def digest(rows):
    return hashlib.sha256('\n'.join(f'{x:x}:{c}' for x, c in sorted(rows.items())).encode()).hexdigest()


def v2(n):
    return (n & -n).bit_length() - 1


def S(x):
    if x == 1:
        return 1
    z = 3 * x + 1
    return z >> v2(z)


def iterate(x, k):
    for _ in range(k):
        x = S(x)
    return x


def valuations(x, length):
    word = []
    for _ in range(length):
        word.append(v2(3 * x + 1))
        x = S(x)
    return word


def selected(x):
    if x % 4 != 3:
        return False
    a = v2(x + 1)
    return ((x + 1) >> a) % 4 == pow(3, a, 4)


def canonical(x):
    return x % 8 == 1 or (x % 4 == 3 and not selected(x))


def combine(*terms):
    out = {}
    for c, rows in terms:
        for x, value in rows.items():
            out[x] = out.get(x, 0) + c * value
    return {x: v for x, v in sorted(out.items()) if x != 1 and v}


def divergence(current):
    out = {}
    for x, c in current.items():
        if x == 1 or not c:
            continue
        out[x] = out.get(x, 0) + c
        y = S(x)
        if y != 1:
            out[y] = out.get(y, 0) - c
    return {x: v for x, v in sorted(out.items()) if v}


def path_rows(x, length):
    rows = {}
    for _ in range(length):
        if x != 1:
            rows[x] = rows.get(x, 0) + 1
        x = S(x)
    return x, rows


def bridge(x):
    """Elementary current with div = [x] - [nu(x)]: F-sibling row, then the halving prefixes."""
    base = x
    while base % 8 == 5:
        base = (base - 1) // 4
    partner = selected(base)
    q = (base - 1) // 2 if partner else base
    current = {}
    if x != base:
        current = combine((1, {x: 1}), (-1, {base: 1}))
    if partner:
        left, right = base, q
        for _ in range(v2(base + 1)):
            current = combine((1, current), (1, {left: 1}), (-1, {right: 1}))
            left, right = S(left), S(right)
        if left != right:
            raise Reject('halving prefixes do not meet at ' + str(base))
    if not canonical(q) or divergence(current) != combine((1, {x: 1}), (-1, {q: 1})):
        raise Reject('elementary bridge failed at ' + str(x))
    return q, current


def joint_plan(v):
    layers = []
    while True:
        if v % 8192 == 39:
            return True, layers, v
        if v % 32 != 19:
            return False, layers, v
        child = (3 * v - 1) // 8
        if not (0 < child < v and child % 4 == 3):
            raise Reject('joint child at ' + str(v))
        layers.append((v, child))
        v = child


def joint_current(v):
    accepted, layers, end = joint_plan(v)
    if not accepted:
        raise Reject('joint pair unresolved at ' + str(v))
    left, L = path_rows(18 * end + 3, 5)
    right, R = path_rows(end, 7)
    require(left == right, f'terminal merger at {end}')
    result = combine((1, L), (-1, R))
    for parent, child in reversed(layers):
        large = 18 * child + 3
        partner = 2 * large + 1
        fchild = 4 * child + 1
        require(S(18 * parent + 3) == partner and S(parent) == fchild and canonical(large),
                f'coupled rewrite (4) at {parent}')
        q, rows = bridge(partner)
        require(q == large, f'selected partner of {large}')
        local = combine((1, {18 * parent + 3: 1}), (1, rows), (-1, {parent: 1}),
                        (-1, {fchild: 1}), (1, {child: 1}))
        require(divergence(local) == combine((1, {18 * parent + 3: 1, child: 1}), (-1, {parent: 1, large: 1})),
                f'local current L_v at {parent}')
        result = combine((1, local), (1, result))
    require(divergence(result) == combine((1, {18 * v + 3: 1}), (-1, {v: 1})), f'C({v}) current')
    return len(layers), end, result


def joint_cylinder(depth):
    residue, modulus = 39, 8192
    for _ in range(depth):
        modulus *= 8
        residue = (8 * residue + 1) * pow(3, -1, modulus) % modulus
    return residue, modulus


def a_cylinder(a, depth):
    r, m = joint_cylinder(depth)
    r, m = (16 * r + 3) * pow(3, -1, 16 * m) % (16 * m), 16 * m
    t = (16 * r + 1) * pow(3 ** (a - 1), -1, 16 * m) % (16 * m)
    return 2 ** a * t - 1, 2 ** a * 16 * m


def parameters(x):
    a = v2(x + 1)
    t = (x + 1) >> a
    z = 3 ** (a - 1) * t - 1
    d = v2(z)
    return a, t, d, z >> d


def weight(N, x):
    if not N < x < Fraction(3 * N, 2):
        return 0
    if x % 12 == 3 or (x % 12 == 7 and 8 * x > 9 * N):
        return 1
    if x % 36 in (7, 19) and 8 * x < 9 * N:
        return 2
    return 0


def crt_mass(N, r, m):
    rows = ((1, N, 3 * N // 2, 3, 3), (1, 9 * N // 8, 3 * N // 2, 7, 3),
            (2, N, 9 * N // 8, 7, 9), (2, N, 9 * N // 8, 19, 9))
    total = 0
    for wt, low, high, source, odd in rows:
        index = (source - r) * pow(m, -1, odd) % odd
        first, period = r + m * index, m * odd
        total += wt * max(0, (high - 1 - first) // period - (low - first) // period)
    return total


def check_root(x, lower, clock, a, entry, label):
    a_x, t, d, w = parameters(x)
    require(selected(x) is False and a_x == a and d == 4 and w % 3 == 2 and lower == (x - 1) // 2,
            f'{label}: parameters')
    require(iterate(x, a + 1) == 18 * w + 1 and iterate(lower, a - 1) == w, f'{label}: prefixes (7)')
    require(iterate(x, clock) == iterate(lower, clock), f'{label}: equal clock')
    if a >= 5:
        require(9 * w > x, f'{label}: old return exceeds x')
    if entry == 'A':
        require(w % 128 == 17, f'{label}: A entry class')
        accepted, layers, _ = joint_plan(3 * (w - 1) // 16)
        require(accepted and clock == a + len(layers) + 7, f'{label}: A joint child and clock')
    else:
        require(w % 256 == 105, f'{label}: B entry class')


def main():
    receipt = json.loads((HERE / 'even_pair_audit.json').read_text())

    joint = []
    for depth in list(range(17)) + [32, 64]:
        r, m = joint_cylinder(depth)
        require(m == 2 ** (13 + 3 * depth), f'cylinder modulus depth {depth}')
        for index in (0, 1, 7):
            v = r + m * index
            layers, end, current = joint_current(v)
            clock = layers + 5
            require(layers == depth and end % 8192 == 39, f'joint depth {depth}')
            require(iterate(18 * v + 3, clock) == iterate(v, clock + 2), f'joint clock depth {depth}')
            require(valuations(18 * end + 3, 4) == [2, 2, 3, 6] and valuations(end, 6) == [1, 1, 2, 1, 4, 1],
                    f'terminal words depth {depth}')
            joint.append(dict(depth=depth, index=index, parameter_bits=v.bit_length(),
                              clock=clock, rows=len(current), sha256=digest(current)))
    require(joint == receipt['joint_cylinders'], 'joint_cylinders rows')
    require(valuations(18 * (39 + 4096) + 3, 4) != [2, 2, 3, 6], 'half modulus keeps the word')

    rows = [row for row in receipt['original_cylinders'] if row['kind'] == 'A']
    mine = []
    for a in (2, 5, 8, 32):
        for depth in (1, 2, 8, 32):
            r, m = a_cylinder(a, depth)
            for index in (0, 1):
                x = r + m * index
                clock = a + depth + 7
                check_root(x, (x - 1) // 2, clock, a, 'A', f'A cylinder a={a} depth={depth}')
                mine.append((a, depth, index, x.bit_length(), clock))
    require(mine == [(row['a'], row['depth'], row['index'], row['bits'], row['clock']) for row in rows],
            'A original cylinder rows')

    for row in receipt['actual_sources']:
        a, entry, wt = row['a'], row['kind'], row['weight']
        if entry == 'A':
            r, m = a_cylinder(a, 1)
            N = 12 * 2 ** (m.bit_length() - 1 + 4)
            odd, source = (3, 3) if wt == 1 else (9, 7)
            index = (source - r) * pow(m, -1, odd) % odd
            first, period = r + m * index, m * odd
            low = 9 * N // 8 if wt == 1 else N
            x = first + period * ((low - first) // period + 1)
            require((N, x) == (row['N'], row['root']), f'A source a={a} weight={wt}')
        require(weight(row['N'], row['root']) == wt and row['lower'] < row['N'] < row['root'],
                f'{entry} source a={a} weight={wt}: residual weight')
        check_root(row['root'], row['lower'], row['clock'], a, entry, f'{entry} source a={a} weight={wt}')

    for row in receipt['fixed_cylinder_counts']:
        if row['kind'] != 'A':
            continue
        r, m = a_cylinder(row['a'], 1)
        N = row['N']
        direct = sum(weight(N, x) for x in range(r + m * ((N - r) // m + 1), 3 * N // 2, m))
        require(direct == crt_mass(N, r, m) == row['mass'], f"fixed count a={row['a']} N={N}")
        require(abs(direct - Fraction(25 * N, 72 * m)) <= 6, f"count bound a={row['a']} N={N}")

    for row in receipt['supplied_conversions']:
        with (HERE / f"branch_{row['kind']}_weight2_current.csv").open() as handle:
            current = {int(r['state']): int(r['current']) for r in csv.DictReader(handle)}
        require(all(c > 0 for c in current.values()), f"conversion {row['kind']}: positivity")
        require(divergence(current) == {row['root']: 2}, f"conversion {row['kind']}: divergence")
        require(len(current) == row['rows'] and digest(current) == row['sha256'], f"conversion {row['kind']}: hash")
        require(weight(row['N'], row['root']) == 2 and row['lower'] == (row['root'] - 1) // 2,
                f"conversion {row['kind']}: weight-2 source")

    if failures:
        print('FAIL: ' + '; '.join(failures[:10]))
        sys.exit(1)
    print(f'PASS: {len(joint)} joint cylinders with current hashes; {len(mine)} A original cylinders; '
          '12 actual sources; 12 A fixed counts; two weight-2 conversions')


if __name__ == '__main__':
    try:
        main()
    except Reject as error:
        print('FAIL: ' + str(error))
        sys.exit(1)
