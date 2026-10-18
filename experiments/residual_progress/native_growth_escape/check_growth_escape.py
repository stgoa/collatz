"""Portable exact replay: all-r descriptors, full large fixture, all-ray failure."""
import argparse
import base64
from collections import Counter
import hashlib
import json
from pathlib import Path
from types import ModuleType
import zlib
import growth_escape as M

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ARROW_CAP, BIT_CAP = 50000, 25000


def step(x):
    n = 3*x+1
    e = (n & -n).bit_length()-1
    return n >> e, e


def direct_divergence(rows):
    out = Counter()
    for x, c in rows.items():
        assert type(x) is int and x > 1 and x % 2 and type(c) is int and c
        y, _ = step(x)
        out[x] += c
        if y != 1:
            out[y] -= c
    return {x: c for x, c in out.items() if x != 1 and c}


def table_hash(rows):
    out = hashlib.sha256()
    for x, c in sorted(rows.items()):
        out.update((format(x, 'x')+':'+str(c)+'\n').encode())
    return out.hexdigest()


def digest(x):
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def encode_word(word):
    raw = ','.join(map(str, word)).encode()
    return dict(codec='base64-zlib-comma-separated-positive-integers', length=len(word),
                sha256=hashlib.sha256(raw).hexdigest(),
                value=base64.b64encode(zlib.compress(raw, 9)).decode())


def decode_word(data):
    raw = zlib.decompress(base64.b64decode(data['value']))
    assert len(raw) < 10*ARROW_CAP
    assert hashlib.sha256(raw).hexdigest() == data['sha256']
    word = [] if not raw else list(map(int, raw.decode().split(',')))
    assert len(word) == data['length'] <= ARROW_CAP
    assert all(0 < a <= BIT_CAP for a in word)
    return word


def supply(x, stored=None):
    """Generation searches only this capped fixture; replay checks stored edges."""
    source, rows, word = x, {}, []
    if stored is not None:
        assert stored['source_hex'] == format(source, 'x')
        prescribed = decode_word(stored['valuation_word'])
    else:
        prescribed = None
    while x != 1:
        if len(word) >= ARROW_CAP or x.bit_length() > BIT_CAP or x in rows:
            raise RuntimeError('Designated finite absorption supply exceeded its caps')
        rows[x] = 1
        x, e = step(x)
        if prescribed is not None:
            assert len(word) < len(prescribed) and prescribed[len(word)] == e
        word.append(e)
    if prescribed is not None:
        assert word == prescribed
    assert direct_divergence(rows) == {source: 1}
    record = dict(source_hex=format(source, 'x'), source_bits=source.bit_length(),
                  valuation_word=encode_word(word), current_rows=len(rows),
                  current_hash=table_hash(rows))
    if stored is not None:
        assert record == stored
    return rows, record


def reject(call):
    try:
        call()
    except (ValueError, TypeError):
        return
    raise AssertionError('Invalid request was accepted')


def sources():
    pending, seen = [M], set()
    paths = {Path(__file__).resolve(), HERE/'NATIVE_GROWTH_ESCAPE.md'}
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


def audit(stored=None):
    descriptors = []
    phases = 0
    for r in list(range(17))+[24, 32, 64]:
        data = M.family_spec(r)
        s, d, L, h = (data[k] for k in ('s', 'forced_precision', 'ray_index', 'point_depth'))
        assert (8272*pow(64, L, 3**d)-217) % 3**d == 0
        assert 0 < L < 3**(d-2) and h == 11*L+8*s
        assert h >= 6*s+2 and 2*9 <= 18**s and 131072 < 177147
        b = data['binary_residue']
        c = M.G.affine_iterate(b, s)
        assert c % 1024 == 137 and M.G.order(b) == 9*r+17
        upper = M.path(3*b, 6*r+12, data['upper_word'])
        assert sum(data['upper_word']) == 9*r+18
        assert upper['endpoint'] == (2187*c+925)//512 > 3*b
        for precision in range(1, 9):
            beta = M.beta_mod(data, precision)
            modulus = 3**precision
            residue = -beta*pow(pow(2, 6*L, modulus), -1, modulus) % modulus
            assert (pow(2, 6*L, modulus)*residue+beta) % modulus == 0
            if precision > 1:
                assert beta % (modulus//3) == M.beta_mod(data, precision-1)
            phases += 1
        descriptors.append({k: v for k, v in data.items() if k != 'upper_word'})
    assert descriptors[0]['ray_index'] == 740 and descriptors[0]['point_depth'] == 8148
    assert descriptors[1]['ray_index'] == 2028089 and descriptors[1]['point_depth'] == 22308995
    exact_cells = []
    for unit in (1, 2):
        for index in (0, 1):
            cell = M.family(0, unit, index)
            checked = M.ray_parameters(cell['seed'], 1, cell['ray_index'])
            assert checked['point_depth'] == 8148 and checked['endpoint'] < cell['seed']
            exact_cells.append([unit, index, format(cell['seed'], 'x')])

    # Exact all-L failure includes full signed coefficients for every feasible ray.
    b = 96797577
    failure = M.exhaustive_decision(b)
    assert failure['status'] == 'exhausted'
    assert failure['point_bound'] == 27 and failure['lifted_bound'] == 16498700317341
    assert [x['ratio'] for x in failure['bounds']] == [18683, 9341]
    assert [(x['ray'], x['L'], x['depth']) for x in failure['cases']] == [
        (0, 0, 1), (0, 1, 0), (0, 2, 0), (1, 0, 0), (1, 1, 0), (1, 2, 2)]
    failure_tables = []
    for case in failure['cases']:
        plan = M.critical_comparison(b, case['ray'], case['L'])
        expected = Counter({3*b: 1, b: -1})
        for w, a in plan['coefficients'].items():
            expected[3*w] -= a
            expected[w] += a
        assert direct_divergence(plan['current']) == {x: c for x, c in expected.items() if x != 1 and c}
        assert any(M.B.rho(w) >= 3*b for w in plan['coefficients'])
        failure_tables.append(dict(ray=case['ray'], L=case['L'],
                                   current=sorted(plan['current'].items()),
                                   coefficients=sorted(plan['coefficients'].items())))
    failure_supplies = []
    failure_paths = {}
    for i, x in enumerate((b, 3*b)):
        old = None if stored is None else stored['failure_absorption'][i]
        rows, record = supply(x, old)
        failure_paths[x] = rows
        failure_supplies.append(record)
    failure_pair = M.combine((1, failure_paths[3*b]), (-1, failure_paths[b]))
    assert direct_divergence(failure_pair) == {3*b: 1, b: -1}

    # Materialize the all-r theorem only at its moderate r0 representative.
    comparison = M.family_comparison(0)
    b, p = comparison['seed'], comparison['endpoint']
    assert comparison['point_depth'] == 8148 and p < b < 3*b < comparison['meeting']
    assert direct_divergence(comparison['current']) == {3*b: 1, p: -1}
    assert comparison['ordinary_clocks'] == [12, 8153]
    upper, lower = 3*b, p
    upper_rows, lower_rows = Counter(), Counter()
    for e in comparison['upper_word']:
        upper_rows[upper] += 1
        upper, actual = step(upper)
        assert actual == e
    for e in comparison['lower_word']:
        lower_rows[lower] += 1
        lower, actual = step(lower)
        assert actual == e
    assert upper == lower == comparison['meeting']
    expected = upper_rows.copy(); expected.subtract(lower_rows)
    assert {x: c for x, c in expected.items() if c} == comparison['current']
    supplied, supplied_records = {}, []
    for i, x in enumerate((p, b)):
        old = None if stored is None else stored['large_fixture']['supplied_absorption'][i]
        rows, record = supply(x, old)
        supplied[x] = rows
        supplied_records.append(record)
    compiled = M.compile_absorptions(comparison, supplied)
    assert direct_divergence(compiled) == {3*b: 1, b: -1}
    fixture = dict(returns=0, ray=1, ray_index=740, point_depth=8148,
                   original_seed_hex=format(b, 'x'), smaller_seed_hex=format(p, 'x'),
                   meeting_hex=format(comparison['meeting'], 'x'),
                   seed_bits=[b.bit_length(), p.bit_length()],
                   ordinary_clocks=comparison['ordinary_clocks'],
                   upper_word=comparison['upper_word'], lower_word=encode_word(comparison['lower_word']),
                   comparison_rows=len(comparison['current']), comparison_hash=table_hash(comparison['current']),
                   supplied_absorption=supplied_records,
                   compiled_rows=len(compiled), compiled_hash=table_hash(compiled))

    invalid = [lambda: M.entry(905), lambda: M.entry(True),
               lambda: M.family_spec(-1), lambda: M.family_spec(True),
               lambda: M.family(1), lambda: M.family(0, 3), lambda: M.family(0, 1, -1),
               lambda: M.ternary_log(2, 4), lambda: M.ternary_log(1, 1),
               lambda: M.beta_mod(descriptors[0], 0),
               lambda: M.ray_parameters(96797577, True, 0),
               lambda: M.ray_parameters(96797577, 0, -1),
               lambda: M.ray_parameters(96797577, 0, 10001),
               lambda: M.inverse_bridge(M.ray_parameters(96797577, 0, 0), max_steps=0),
               lambda: M.exhaustive_decision(M.G.exact_family(0)),
               lambda: M.critical_comparison(b, 1, 740),
               lambda: M.compile_absorptions(comparison, {}),
               lambda: M.compile_absorptions(comparison, {**supplied, p: {}}),
               lambda: M.compile_absorptions(comparison, {**supplied, p: {3: True}}),
               lambda: M.compile_absorptions(dict(comparison, current={3: True}), supplied),
               lambda: M.compile_absorptions(dict(comparison, status='unresolved'), supplied)]
    for call in invalid:
        reject(call)
    capped = M.exhaustive_decision(96797577, max_rays=1)
    assert capped['status'] == 'capped'
    return dict(status='PASS', scope='All-r conditional CRT subfamilies; complete two-ray/point decision only; universal supply open.',
                caps=dict(absorption_arrows=ARROW_CAP, absorption_bits=BIT_CAP,
                          family_point_materialization=10000),
                symbolic_descriptors=descriptors, modular_phase_checks=phases,
                exact_terminal_unit_cells=len(exact_cells), exact_cell_hash=digest(exact_cells),
                complete_failure=failure, failure_current_tables=failure_tables,
                failure_absorption=failure_supplies, failure_pair_rows=len(failure_pair),
                failure_pair_hash=table_hash(failure_pair), large_fixture=fixture,
                rejections=len(invalid), capped_decisions=1, source_hashes=sources())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write-receipt', action='store_true')
    args = parser.parse_args()
    path = HERE/'growth_escape_audit.json'
    stored = None if args.write_receipt else json.loads(path.read_text())
    result = audit(stored)
    serialized = json.dumps(result, indent=2, sort_keys=True)+'\n'
    if args.write_receipt:
        path.write_text(serialized)
    else:
        assert stored == json.loads(serialized), 'Stored receipt differs'
    print('PASS: native H17 growth escape; '+json.dumps(dict(
        symbolic_depths=len(result['symbolic_descriptors']), modular_phases=result['modular_phase_checks'],
        full_failure_rays=len(result['complete_failure']['cases']),
        large_comparison_rows=result['large_fixture']['comparison_rows'],
        supplied_lengths=[x['current_rows'] for x in result['large_fixture']['supplied_absorption']],
        compiled_rows=result['large_fixture']['compiled_rows'], rejections=result['rejections'],
        capped_decisions=result['capped_decisions']), sort_keys=True))


if __name__ == '__main__':
    main()
