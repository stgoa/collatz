"""Bounded exact checks for the two-identity signed-frontier compiler."""
import argparse
import hashlib
import json
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from types import ModuleType
import frontier_normal_form as M

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
spec = spec_from_file_location('frontier_debt', HERE.parent/'arithmetic_progress/valuation_debt.py')
DEBT = module_from_spec(spec)
spec.loader.exec_module(DEBT)


def rows(data):
    return [[x, c] for x, c in sorted(data.items())]


def digest(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def advance(x, length):
    for _ in range(length):
        x = M.step(x)
    return x


def reject(action):
    try:
        action()
    except ValueError:
        return
    raise AssertionError('Expected rejection')


def finite_pair(w):
    def history(x):
        current = {}
        while x != 1:
            if x in current or len(current) >= 10000 or x.bit_length() > 4096:
                raise RuntimeError('Designated supplied input exceeded finite caps')
            current[x] = 1
            x = M.step(x)
        return current
    current = M.combine((1, history(3*w)), (-1, history(w)))
    assert M.divergence(current) == M.pair(w)
    return current


def source_hashes():
    # module_from_spec imports need not appear in sys.modules.
    queue, seen, paths = [M, DEBT], set(), {Path(__file__).resolve()}
    while queue:
        module = queue.pop()
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
        queue.extend(x for x in vars(module).values() if isinstance(x, ModuleType))
    return {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(paths)}


def audit():
    branch_cases = []
    for label, residue, period in (('I', 93, 512), ('II', 1285, 2048)):
        for index in range(256):
            w = residue+period*index
            data = M.bridge(w)
            assert data['label'] == label
            u = data['child']
            assert DEBT.RANK.rho(u) < DEBT.RANK.rho(w)
            for multiplier, (left, right) in zip((1, 3), data['ordinary_clocks_lower_upper']):
                assert advance(multiplier*w, left) == advance(multiplier*u, right)
            branch_cases.append([w, u, label, digest(rows(data['current']))])
    singleton_cases = []
    for w in range(5, 32768, 8):
        data = M.normalize_pair(w)
        left, right = data['common_padded_clocks']
        assert all(advance(m*w, left) == advance(m*data['terminal'], right) for m in (1, 3))
        again = M.normalize({data['terminal']: 1})
        assert again['current'] == {} and again['coefficients'] == {data['terminal']: 1}
        singleton_cases.append([w, data['terminal'], len(data['chain'])])
    word_cases = []
    for length in (1, 2, 3, 4, 8, 16, 32):
        for pattern in (('I',), ('II',), ('I', 'II'), ('II', 'I')):
            labels = [pattern[i % len(pattern)] for i in range(length)]
            family = M.inverse_word(labels)
            normal = M.normalize_pair(family['seed'])
            assert len(normal['chain']) >= length
            assert [x['label'] for x in normal['chain'][:length]] == labels[::-1]
            left, right = normal['common_padded_clocks']
            assert all(advance(m*family['seed'], left) == advance(m*normal['terminal'], right)
                       for m in (1, 3))
            word_cases.append(dict(family=family, terminal=normal['terminal'], clocks=[left, right],
                                   current_hash=digest(rows(normal['current']))))
    vectors = []
    for index in range(128):
        w, b, terminal = 93+512*index, 1285+2048*index, 5+8*index
        u, a = M.bridge(w)['child'], M.bridge(b)['child']
        source = M.combine((2, {w: 1}), (-2, {u: 1}), (-3, {b: 1}), (3, {a: 1}),
                           ((index % 5)-2, {terminal: 1}))
        data = M.normalize(source)
        again = M.normalize(data['coefficients'])
        assert again['current'] == {} and again['coefficients'] == data['coefficients']
        assert M.potential(data['coefficients']) <= M.potential(source)
        vectors.append([rows(source), rows(data['coefficients']), digest(rows(data['current']))])
    resets = []
    for H in (26, 27, 40, 64, 128, 256):
        for index in (0, 1):
            old = DEBT.obstruction(H, index)
            w, u, a, b = (old[x] for x in ('seed', 'leading', 'small_positive', 'small_negative'))
            normalized = M.normalize(old['coefficients'])
            assert normalized['coefficients'] == {u: 1}
            assert normalized['current'] == M.combine((-1, M.bridge(b)['current']))
            assert M.combine((1, old['current']), (1, normalized['current'])) == M.bridge(w)['current']
            resets.append(dict(H=H, index=index, seed=w, child=u, positive_helper=a, negative_helper=b,
                               old_coefficients=rows(old['coefficients']),
                               old_current_hash=digest(rows(old['current'])),
                               simplified_current=rows(M.bridge(w)['current'])))
    barriers = []
    for count in (1, 2, 4):
        for index in (0, 1):
            family = DEBT.MIXED.family(count, index)
            old = DEBT.MIXED.repeated_plan(family['seed'], count)
            data = M.normalize(old['coefficients'])
            w, v = old['seed'], old['leading']
            assert M.bridge(w) is None and M.bridge(v) is None
            assert data['coefficients'][v] == 1
            assert all(x < v for x in data['coefficients'] if x != v)
            assert M.potential(data['coefficients']) >= v > w
            barriers.append(dict(seed=w, leading=v, repetitions=count,
                                 normalized_coefficients=rows(data['coefficients']),
                                 potential=M.potential(data['coefficients'])))
    fixture = M.normalize({93: 2, 13: -2, 1285: -3, 45: 3})
    assert fixture['coefficients'] == {}
    closed = M.compile_frontier(fixture, {})
    residual = M.normalize({93: 2, 1285: -3, 5: -2})
    supplied = {w: finite_pair(w) for w in residual['coefficients']}
    completed = M.compile_frontier(residual, supplied)
    reject(lambda: M.compile_frontier(residual, {}))
    bad = dict(supplied)
    bad[next(iter(bad))] = {}
    reject(lambda: M.compile_frontier(residual, bad))
    invalid = [lambda: M.bridge(1), lambda: M.bridge(-3), lambda: M.normalize({5: 0.5}),
               lambda: M.inverse_word(['III']), lambda: M.inverse_word(['I'], -1)]
    for action in invalid:
        reject(action)
    return json.loads(json.dumps(dict(
        status='PASS', scope='Two specified pair identities only; terminal pair currents remain mandatory',
        branch_cases=len(branch_cases), branch_hash=digest(branch_cases),
        singleton_cases=len(singleton_cases), singleton_hash=digest(singleton_cases),
        mixed_word_families=word_cases, signed_vectors=len(vectors), signed_vector_hash=digest(vectors),
        full_R69_resets=resets, retained_R67_leading_requests=barriers,
        closed_without_inputs=dict(original=rows(fixture['original']), current=rows(closed)),
        supplied_conversion=dict(original=rows(residual['original']), normalization_current=rows(residual['current']),
                                 terminal_requests=rows(residual['coefficients']),
                                 supplied={str(w): rows(c) for w, c in sorted(supplied.items())},
                                 current=rows(completed), current_rows=len(completed)),
        rejections=len(invalid)+2, caps=dict(supplied_arrows=10000, supplied_bits=4096),
        sources=source_hashes())))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    result = audit()
    path = HERE/'frontier_normal_form_audit.json'
    if args.write:
        path.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    else:
        assert json.loads(path.read_text()) == result
    print('PASS: signed-frontier normalization; '
          f"{result['branch_cases']} bridges; {result['singleton_cases']} singleton normalizations; "
          f"{len(result['mixed_word_families'])} mixed words; {result['signed_vectors']} signed vectors; "
          f"{len(result['full_R69_resets'])} full reset compressions; "
          f"{len(result['retained_R67_leading_requests'])} scoped retained leaders; "
          'one input-free and one supplied-current conversion')
