"""Self-contained recomputation of the odd-h pair interface, its critical bijection and the stored U_128 compilation.

Written at the B10-residual-R25-R39 migration; the legacy scripts in this folder
load ../bridge_normal_form/normal_form.py and ../bounded_run_cycles/bounded_runs.py
(and through it further legacy folders) by their pre-migration paths and no
longer run. Standard library, exact integers, own Syracuse step and own
elementary normal form. Run from the repository root: python3 <this file>.
Exits 1 on any failure; writes nothing.

Checks, against odd_interface_audit.json, compiler128_inputs.json and
compiler128_current.csv in this folder:
  - interface (2): for every odd z < 16384 the explicit current E_z (direct
    child u = z when 3z is canonical, else u = 4z+1) has div E_z = Q(z) - P(u);
    the static label chi joins Q(z)'s endpoints iff z = 3 mod 8; for z != 3 mod 8,
    g(z) = nu(6z+1) is critical, z <= g(z)/3, the inverse returns z, and g(z) is
    in the covered phase (12) iff unit3(z) = 1; classification_count and
    classification_hash;
  - the 5461 critical targets below 65536 and their inverse round trip;
  - the 528 parameter cases w = (2^(2k+3)C+1)/3 (k <= 32, C = 6j+1, j < 16):
    w = 3 mod 8, v2(3w-1) = 2k+3, and the reduction recovers z; parameter_hash;
  - every odd-h reduction w = 3 mod 8 below 32768: div L_w = P(w) - P(u),
    8u < 7w when h >= 7; odd_h_reduction_count, reduction_categories and
    reduction_hash; the 171 prescribed parent clocks k+1+max(ell, A) for w < 2048;
    the 14 expanding examples (h = 3, 5, u > w);
  - the compiler inputs: for M = 64, 128, 512 the index set I_M and the exact
    demonstration inputs (2000-step cap) reproduce input_count and the exact-mode
    input_hash; the stored M = 128 inputs equal the recomputed ones and each has
    divergence Q(z); the stored U_128 current is positive, has divergence
    exactly the sum of [x] over odd 3 <= x <= 127, and matches output_rows and
    output_hash;
  - the four stored delayed-ray seeds (r = 1, 2): x = 19 mod 36, x = 10 mod 27,
    the CRT construction (14)-(15), the repeated word (1,2,1,1,1,1,2,2), every
    prefix state canonical, above N and outside the covered phase, and cutoff_bits.
It does not rebuild the one-sided compilations or the delayed rays with r >= 4
(legacy checker, evidence only).
"""

import csv
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CAP = 2000
WORD = (1, 2, 1, 1, 1, 1, 2, 2)
failures = []


class Reject(Exception):
    pass


def require(ok, message):
    if not ok:
        failures.append(message)


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def v2(n):
    return (n & -n).bit_length() - 1


def S(x):
    if x == 1:
        return 1
    z = 3 * x + 1
    return z >> v2(z)


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


def delta(x):
    return {} if x == 1 else {x: 1}


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


def P(w):
    return combine((1, delta(3 * w)), (-1, delta(w)))


def Q(z):
    return combine((1, delta(6 * z + 1)), (-1, delta(z)))


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
    if not canonical(q) or divergence(current) != combine((1, delta(x)), (-1, delta(q))):
        raise Reject('elementary bridge failed at ' + str(x))
    return q, current


def nu(x):
    return bridge(x)[0]


def prefix(x, length):
    rows = {}
    for _ in range(length):
        if x != 1:
            rows[x] = rows.get(x, 0) + 1
        x = S(x)
    return x, dict(sorted(rows.items()))


def ternary(n):
    k = 0
    while n % 3 == 0:
        n //= 3
        k += 1
    return k, n


def critical(q):
    return canonical(q) and q % 4 == 3 and q % 3 != 2


def critical_index(q):
    return q // 3 if q % 3 == 0 else (q - 1) // 6


def covered(q):
    return critical(q) and (ternary(q)[1] % 3 == 1 if q % 3 == 0 else ternary(q - 1)[1] % 3 == 2)


def chi(x):
    q = nu(x)
    while q % 24 == 9:
        q = (q - 3) // 6 if q % 48 == 9 else q // 3
    return q


def interface(z):
    """Return (kind, child, A, E_z) with div E_z = Q(z) - P(child)."""
    r = v2(3 * z + 1)
    if canonical(3 * z):
        q, current = bridge(6 * z + 1)
        require(q == 3 * z, f'direct bridge at {z}')
        kind, child, length = 'direct', z, r + 1
    else:
        child = 4 * z + 1
        q, rows = bridge(3 * child)
        require(canonical(6 * z + 1) and q == 6 * z + 1, f'F bridge at {z}')
        current = combine((1, combine((1, delta(child)), (-1, delta(z)))), (-1, rows))
        kind, length = 'F', r + 2
    require(divergence(current) == combine((1, Q(z)), (-1, P(child))), f'interface (2) at {z}')
    return kind, child, length, current


def reduction(w):
    h = v2(3 * w - 1)
    k = (h - 3) // 2
    z = 3 ** k * ((3 * w - 1) >> h)
    left, L = prefix(3 * w, k + 1)
    right, R = prefix(w, k + 1)
    require(left == 6 * z + 1 and right == 4 * z + 1, f'prefix ends at {w}')
    local = combine((1, L), (-1, R), (-1, combine((1, delta(right)), (-1, delta(z)))))
    kind, child, length, rows = interface(z)
    current = combine((1, local), (1, rows))
    require(divergence(current) == combine((1, P(w)), (-1, P(child))), f'reduction (4) at {w}')
    if h >= 7:
        require(8 * child < 7 * w, f'h >= 7 shrinking at {w}')
    return dict(h=h, k=k, z=z, child=child, kind=kind, length=length, current=current)


def finite_path(x):
    current = {}
    for _ in range(CAP):
        if x == 1:
            return current
        if x in current:
            raise Reject('demonstration path repeats')
        current[x] = 1
        x = S(x)
    raise Reject('demonstration cap exhausted')


def main():
    receipt = json.loads((HERE / 'odd_interface_audit.json').read_text())

    classification = []
    for z in range(1, 16384, 2):
        kind, child, _, _ = interface(z)
        require((chi(6 * z + 1) == chi(z)) == (z % 8 == 3), f'static label at {z}')
        q = None
        if z % 8 != 3:
            q = nu(6 * z + 1)
            require(critical(q) and 3 * z <= q and critical_index(q) == z
                    and q == (3 * z if canonical(3 * z) else 6 * z + 1), f'critical target of {z}')
            require(covered(q) == (ternary(z)[1] % 3 == 1), f'covered phase of {z}')
        classification.append((z, kind, child, q))
    require(len(classification) == receipt['classification_count'], 'classification_count')
    require(digest(classification) == receipt['classification_hash'], 'classification_hash')

    count = 0
    for q in range(1, 65536, 2):
        if critical(q):
            count += 1
            z = critical_index(q)
            require(z % 2 == 1 and z % 8 != 3 and nu(6 * z + 1) == q, f'critical inverse at {q}')
    require(count == receipt['critical_targets_below65536'] == 5461, 'critical_targets_below65536')

    restrictions = []
    for k in range(33):
        for j in range(16):
            C = 6 * j + 1
            z = 3 ** k * C
            w = (2 ** (2 * k + 3) * C + 1) // 3
            require(3 * w == 2 ** (2 * k + 3) * C + 1 and w % 8 == 3 and w > z
                    and v2(3 * w - 1) == 2 * k + 3 and reduction(w)['z'] == z, f'parameter k={k} C={C}')
            restrictions.append((k, C, w, z))
    require(len(restrictions) == receipt['actual_parameter_cases'], 'actual_parameter_cases')
    require(digest(restrictions) == receipt['parameter_hash'], 'parameter_hash')

    reductions, categories, clocks = [], {}, 0
    for w in range(3, 32768, 8):
        if v2(3 * w - 1) % 2 == 0:
            continue
        row = reduction(w)
        shrinking = row['child'] < w
        key = f"{'high' if row['h'] >= 7 else 'low'}_{row['kind']}_{shrinking}"
        categories[key] = categories.get(key, 0) + 1
        reductions.append((w, row['h'], row['child'], digest(row['current'])))
        if w < 2048:
            u = row['child']
            left, right = 3 * u, S(u)
            for ell in range(CAP):
                if left == right:
                    break
                left, right = S(left), S(right)
            else:
                raise Reject('merger clock cap exhausted')
            length = row['k'] + 1 + max(ell, row['length'])
            require(prefix(3 * w, length)[0] == prefix(w, length + 1)[0], f'parent clock at {w}')
            clocks += 1
    require(len(reductions) == receipt['odd_h_reduction_count'] == 2731, 'odd_h_reduction_count')
    require(dict(sorted(categories.items())) == receipt['reduction_categories'], 'reduction_categories')
    require(digest(reductions) == receipt['reduction_hash'], 'reduction_hash')
    require(clocks == receipt['merger_clock_count'] == 171, 'merger_clock_count')

    expansions = []
    for j in (0, 1, 2, 7, 31, 127, 1023):
        for w, h, child in ((64 * j + 19, 3, 96 * j + 29), (256 * j + 139, 5, 288 * j + 157)):
            row = reduction(w)
            require(row['h'] == h and row['child'] == child > w and row['kind'] == 'F', f'expansion {w}')
            expansions.append([w, h, child])
    require(expansions == receipt['expansion_examples'], 'expansion_examples')

    exact_rows = {row['limit']: row for row in receipt['compilers'] if row['mode'] == 'exact'}
    recomputed128 = None
    for limit in (64, 128, 512):
        needed = sorted(critical_index(q) for q in range(3, limit + 1, 2) if critical(q))
        inputs = {z: combine((1, finite_path(6 * z + 1)), (-1, finite_path(z))) for z in needed}
        require(all(divergence(J) == Q(z) for z, J in inputs.items()), f'inputs divergence M={limit}')
        require(len(inputs) == exact_rows[limit]['input_count'], f'input_count M={limit}')
        require(digest(inputs) == exact_rows[limit]['input_hash'], f'input_hash M={limit}')
        if limit == 128:
            recomputed128 = inputs
    stored = json.loads((HERE / 'compiler128_inputs.json').read_text())
    stored = {int(z): {int(x): c for x, c in J.items()} for z, J in stored.items()}
    require(stored == recomputed128, 'compiler128_inputs.json differs from the recomputed inputs')
    with (HERE / 'compiler128_current.csv').open() as handle:
        current = {int(r['source']): int(r['coefficient']) for r in csv.DictReader(handle)}
    require(all(c > 0 for c in current.values()), 'U_128 current has a nonpositive row')
    require(divergence(current) == {x: 1 for x in range(3, 128, 2)}, 'U_128 current divergence')
    require(len(current) == exact_rows[128]['output_rows'], 'U_128 output_rows')
    require(digest(current) == exact_rows[128]['output_hash'], 'U_128 output_hash')

    seeds = 0
    for row in receipt['delayed_ray_cases']:
        if row['seed'] is None:
            continue
        r, extra = row['repeats'], row['extra_scale']
        modulus = 1 << (11 * r + 6)
        residue = (-9221 * pow(4513, -1, modulus)) % modulus
        residue += modulus * ((10 - residue) * pow(modulus, -1, 27) % 27)
        period = 27 * modulus
        N = 12 * (modulus << (5 + extra))
        x = residue + period * ((N - residue) // period + 1)
        require(str(x) == row['seed'] and N.bit_length() == row['cutoff_bits'], f'delayed seed r={r}')
        require(N < x < 9 * N // 8 and x % 36 == 19 and x % 27 == 10, f'delayed root r={r}')
        states, y = [x], x
        for _ in range(r):
            for valuation in WORD:
                require(v2(3 * y + 1) == valuation, f'delayed word r={r}')
                y = S(y)
                states.append(y)
        require(all(canonical(s) and s > N and not covered(s) for s in states), f'delayed states r={r}')
        seeds += 1
    require(seeds == 4, 'four stored delayed seeds')

    if failures:
        print('FAIL: ' + '; '.join(failures[:10]))
        sys.exit(1)
    print(f'PASS: {len(classification)} Q interfaces; {count} critical targets; {len(restrictions)} parameter cases; '
          f'{len(reductions)} odd-h reductions; {clocks} clocks; U_128 compilation; {seeds} delayed seeds; '
          'all receipt hashes match')


if __name__ == '__main__':
    try:
        main()
    except Reject as error:
        print('FAIL: ' + str(error))
        sys.exit(1)
