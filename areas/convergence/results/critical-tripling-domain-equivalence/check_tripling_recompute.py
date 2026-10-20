"""Self-contained recomputation of the critical tripling bijection and the legacy plan receipt.

Written at the B10-residual-R25-R39 migration; the legacy scripts in this folder
load ../bridge_normal_form/normal_form.py (and, for the side-lane probe,
affine_controls and fibre_count_check) by their pre-migration paths and no
longer run. Standard library, exact integers, own Syracuse step and own
elementary normal form. Run from the repository root: python3 <this file>.
Exits 1 on any failure; writes nothing.

Checks, against tripling_audit.json in this folder:
  - the bijection w -> nu(3w) from W = {w = 5 mod 8} u {w = 9 mod 16} onto the
    critical roots C = {q canonical, q = 3 mod 4, q != 2 mod 3}: for every odd
    w < 32768 in W the image is critical, distinct, larger than w, and the stated
    inverse (q/3 or (2q+1)/3) returns w; for every critical q < 32768 the inverse
    lies in W, is smaller than q and maps back to q; the counts (6144, 2731) and
    the receipt hashes critical_domain_hash and critical_inverse_hash;
  - the static and critical local steps for every odd x < 16384: the explicit
    current C has div C = [x] - [v] - P(w) exactly (state 1 killed), v < x,
    3(v - 1) <= 2(q - 1), critical requests lie in W; the receipt's
    local_step_count and local_step_hash;
  - the complete formal plans for every odd x < 2048 in both modes, the
    logarithmic bound 2*3^(r-1) <= 2^(r-1)(x-1) on static plans with r requests,
    formal_plan_count and formal_plan_hash;
  - the 40 compiled examples with capped demonstration pair inputs: each compiled
    current has divergence exactly [x]; actual_compiled_hash, supplied_pair_count,
    supplied_pairs_hash and the two stored final current tables (seeds 27 and 31);
    a plan with absent or zero pair inputs is rejected.
"""

import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
failures = []


class Reject(Exception):
    pass


def require(ok, message):
    if not ok:
        failures.append(message)


def digest(rows):
    return hashlib.sha256(json.dumps(rows, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


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
    t = (x + 1) >> a
    return t % 4 == pow(3, a, 4)


def canonical(x):
    return x % 8 == 1 or (x % 4 == 3 and not selected(x))


def combine(*terms):
    out = {}
    for c, rows in terms:
        for x, value in rows.items():
            if x != 1:
                out[x] = out.get(x, 0) + c * value
    return {x: v for x, v in sorted(out.items()) if v}


def atoms(*terms):
    return combine(*[(c, {x: 1}) for c, x in terms])


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


def bridge(x):
    """Elementary current with div = [x] - [nu(x)]: F-sibling row, then the halving prefixes."""
    base = x
    while base % 8 == 5:
        base = (base - 1) // 4
    partner = selected(base)
    q = (base - 1) // 2 if partner else base
    current = {}
    if x != base:
        current = combine((1, current), (1, {x: 1}), (-1, {base: 1}))
    if partner:
        left, right = base, q
        for _ in range(v2(base + 1)):
            current = combine((1, current), (1, {left: 1}), (-1, {right: 1}))
            left, right = S(left), S(right)
        if left != right:
            raise Reject('halving prefixes do not meet at ' + str(base))
    if not canonical(q) or divergence(current) != atoms((1, x), (-1, q)):
        raise Reject('elementary bridge failed at ' + str(x))
    return q, current


def nu(x):
    return bridge(x)[0]


def in_W(w):
    return w % 8 == 5 or w % 16 == 9


def critical(q):
    return canonical(q) and q % 4 == 3 and q % 3 != 2


def inverse(q):
    return q // 3 if q % 3 == 0 else (2 * q + 1) // 3


def pair_source(w):
    return atoms((1, 3 * w), (-1, w))


def static_step(x):
    q, current = bridge(x)
    if q == 1:
        return q, 1, None, 'elementary', current
    if q % 3 == 0:
        v = w = q // 3
        correction = {}
    elif q % 3 == 1:
        v = w = (2 * q + 1) // 3
        correction = combine((-1, bridge(2 * q + 1)[1]))
    else:
        w, v = (4 * q + 1) // 3, (2 * q - 1) // 3
        if not (selected(w) and nu(w) == v):
            raise Reject('static row 2 at ' + str(x))
        correction = combine((1, atoms((1, q), (-1, 4 * q + 1))), (1, bridge(w)[1]))
    require(0 < v < q and 3 * (v - 1) <= 2 * (q - 1), f'static decrease at {x}')
    current = combine((1, current), (1, correction))
    require(divergence(current) == combine((1, atoms((1, x), (-1, v))), (-1, pair_source(w))),
            f'static boundary at {x}')
    return q, v, w, 'static_' + str(q % 3), current


def critical_step(x):
    q, current = bridge(x)
    if q == 1:
        return q, 1, None, 'elementary', current
    if q % 8 == 1:
        v, w, branch, correction = S(q), None, 'forward_descent', {q: 1}
    elif q % 3 == 2:
        v, w, branch = (2 * q - 1) // 3, None, 'inverse_descent'
        require(S(v) == q, f'inverse arrow at {x}')
        correction = {v: -1}
    else:
        v = w = inverse(q)
        branch = 'critical_pair'
        correction = combine((-1, bridge(3 * w)[1]))
    require(0 < v < q, f'critical decrease at {x}')
    current = combine((1, current), (1, correction))
    expected = atoms((1, x), (-1, v))
    if w is not None:
        expected = combine((1, expected), (-1, pair_source(w)))
    require(divergence(current) == expected, f'critical boundary at {x}')
    return q, v, w, branch, current


def plan(x, mode):
    advance = critical_step if mode == 'critical' else static_step
    start, steps, current, pairs = x, [], {}, []
    while x != 1:
        q, v, w, branch, rows = advance(x)
        if not v < x:
            raise Reject('plan does not decrease at ' + str(x))
        steps.append([x, v, branch])
        current = combine((1, current), (1, rows))
        if w is not None:
            pairs.append(w)
        x = v
    expected = atoms((1, start))
    for w in pairs:
        expected = combine((1, expected), (-1, pair_source(w)))
    require(divergence(current) == expected, f'plan boundary at {start} ({mode})')
    return dict(seed=start, pairs=pairs, steps=steps, current=current)


def compile_plan(data, supplied):
    current = data['current']
    for w in data['pairs']:
        if w not in supplied or divergence(supplied[w]) != pair_source(w):
            raise Reject('missing or incorrect pair input ' + str(w))
        current = combine((1, current), (1, supplied[w]))
    require(divergence(current) == atoms((1, data['seed'])), f"compiled boundary at {data['seed']}")
    return current


def absorption_path(x, cap=10000):
    current = {}
    for _ in range(cap):
        if x == 1:
            return current
        if x in current:
            raise Reject('demonstration path repeats')
        current[x] = 1
        x = S(x)
    raise Reject('demonstration cap exhausted')


def main():
    receipt = json.loads((HERE / 'tripling_audit.json').read_text())
    caps = receipt['caps']

    images = []
    for w in range(1, caps['domain_odd_max'] + 1, 2):
        if in_W(w):
            q = nu(3 * w)
            require(critical(q) and w < q and inverse(q) == w, f'image of {w}')
            images.append([w, q])
    require(len({q for _, q in images}) == len(images), 'images distinct')
    inverses = []
    for q in range(1, caps['critical_odd_max'] + 1, 2):
        if critical(q):
            w = inverse(q)
            require(in_W(w) and w < q and nu(3 * w) == q, f'inverse of {q}')
            inverses.append([q, w])
    require(len(images) == receipt['critical_domain_inputs'] == 6144, 'critical_domain_inputs')
    require(digest(images) == receipt['critical_domain_hash'], 'critical_domain_hash')
    require(len(inverses) == receipt['critical_inverse_inputs'] == 2731, 'critical_inverse_inputs')
    require(digest(inverses) == receipt['critical_inverse_hash'], 'critical_inverse_hash')

    local_rows = []
    for x in range(1, caps['local_odd_max'] + 1, 2):
        for mode, advance in (('static', static_step), ('critical', critical_step)):
            q, v, w, branch, current = advance(x)
            if mode == 'critical' and w is not None:
                require(in_W(w), f'critical request outside W at {x}')
            local_rows.append([mode, x, q, v, w, branch, sorted(current.items())])
    require(len(local_rows) == receipt['local_step_count'], 'local_step_count')
    require(digest(local_rows) == receipt['local_step_hash'], 'local_step_hash')

    plans = []
    for x in range(1, caps['plan_odd_max'] + 1, 2):
        for mode in ('static', 'critical'):
            data = plan(x, mode)
            r = len(data['pairs'])
            if mode == 'static' and r:
                require(2 * 3 ** (r - 1) <= 2 ** (r - 1) * (x - 1), f'logarithmic bound at {x}')
            plans.append([x, mode, data['pairs'], data['steps'], sorted(data['current'].items())])
    require(len(plans) == receipt['formal_plan_count'], 'formal_plan_count')
    require(digest(plans) == receipt['formal_plan_hash'], 'formal_plan_hash')

    pair_inputs, compiled, tables = {}, [], []
    for x in caps['sample_seeds']:
        for mode in ('static', 'critical'):
            data = plan(x, mode)
            for w in data['pairs']:
                if w not in pair_inputs:
                    pair_inputs[w] = combine((1, absorption_path(3 * w)), (-1, absorption_path(w)))
            result = compile_plan(data, pair_inputs)
            compiled.append([x, mode, data['pairs'], len(result),
                             sum(abs(c) for c in result.values()), sorted(result.items())])
            if x in (27, 31) and mode == 'critical':
                tables.append(dict(seed=x, mode=mode, pair_inputs=data['pairs'],
                                   current=[[u, c] for u, c in sorted(result.items())]))
    require(len(compiled) == receipt['actual_compiled_examples'] == 40, 'actual_compiled_examples')
    require(digest(compiled) == receipt['actual_compiled_hash'], 'actual_compiled_hash')
    require(len(pair_inputs) == receipt['supplied_pair_count'] == 34, 'supplied_pair_count')
    require(digest([[w, sorted(c.items())] for w, c in sorted(pair_inputs.items())])
            == receipt['supplied_pairs_hash'], 'supplied_pairs_hash')
    require(tables == receipt['actual_current_tables'], 'actual_current_tables (27, 31)')

    rejecting = plan(27, 'critical')
    for supplied in ({}, {w: {} for w in rejecting['pairs']}):
        try:
            compile_plan(rejecting, supplied)
        except Reject:
            continue
        failures.append('an absent or incorrect pair input was accepted')

    if failures:
        print('FAIL: ' + '; '.join(failures[:10]))
        sys.exit(1)
    print(f'PASS: W-to-critical bijection ({len(images)} images, {len(inverses)} inverses); '
          f'{len(local_rows)} local steps; {len(plans)} plans; {len(compiled)} compiled examples; '
          'all receipt hashes match')


if __name__ == '__main__':
    try:
        main()
    except Reject as error:
        print('FAIL: ' + str(error))
        sys.exit(1)
