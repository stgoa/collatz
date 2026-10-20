"""Capped arithmetic checks of joint and d=4 current constructions."""
import argparse
import csv
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path
import even_pairs as E

HERE = Path(__file__).resolve().parent


def digest(rows):
    text = '\n'.join(f'{x:x}:{c}' for x, c in sorted(rows.items()))
    return hashlib.sha256(text.encode()).hexdigest()


def valuations(x, length):
    word = []
    for _ in range(length):
        word.append(E.NORMAL.valuation2(3*x+1))
        x = E.step(x)
    return word


def check_clock(x, data):
    left = E.prefix(x, data['clock'])[0]
    right = E.prefix(data['lower'], data['clock'])[0]
    assert left[-1] == right[-1]


def split_accepts(w):
    """Precisely the two-call catalogue audited in the proof note."""
    def accepts(v):
        if v % 8 == 3:
            return E.MIXED.plan(v)['accepted']
        if v % 8 == 1:
            row = E.ONE.reduction(v)
            return row['kind'] != 'unresolved' and E.MIXED.plan(row['child'])['accepted']
        return False
    return E.NORMAL.canonical(9*w) and accepts(w) and accepts(3*w)


def audit():
    joint = []
    for depth in list(range(17))+[32, 64]:
        r, m = E.joint_cylinder(depth)
        for index in (0, 1, 7):
            v = r+m*index
            data = E.joint_current(v)
            assert len(data['plan']['layers']) == depth
            assert E.prefix(18*v+3, data['clock'])[0][-1] == E.prefix(v, data['clock']+2)[0][-1]
            terminal = data['plan']['terminal']
            assert valuations(18*terminal+3, 4) == [2, 2, 3, 6]
            assert valuations(terminal, 6) == [1, 1, 2, 1, 4, 1]
            joint.append(dict(depth=depth, index=index, parameter_bits=v.bit_length(),
                              clock=data['clock'], rows=len(data['current']),
                              sha256=digest(data['current'])))
    # Half the stated modulus loses the last exact valuation bit.
    assert valuations(18*(39+4096)+3, 4) != [2, 2, 3, 6]
    split = dict(inputs=8192, accepted=0)
    for w in range(1, 16384, 2):
        expected = w % 256 == 105 and E.MIXED.plan((9*w-1)//16)['accepted']
        actual = split_accepts(w)
        assert actual == expected
        split['accepted'] += actual
    for v in range(3, 65536, 8):
        assert not (E.MIXED.plan(v)['accepted'] and E.MIXED.plan(6*v+1)['accepted'])
    symbols = (('O', 1), ('E1', 1), ('E2', 1))
    words = [word for depth in range(4) for word in itertools.product(symbols, repeat=depth)]
    words += [tuple(symbols[i % 3] for i in range(depth)) for depth in (8, 16, 32, 64)]
    cylinders = []
    for a in (2, 5, 8, 32):
        families = [('A', (), depth) for depth in (1, 2, 8, 32)]
        families += [('B', word, 1) for word in words]
        for kind, word, depth in families:
            r, m = E.cylinder(a, kind, word=word, depth=depth)
            for index in (0, 1):
                x = r+m*index
                data = E.bridge(x)
                check_clock(x, data)
                assert data['a'] == a
                assert E.RUN.parameters(x)[2] == 4
                assert data['w'] % 3 == 2
                assert data['old_normalized_return'] % 3 == 0
                if a >= 5:
                    assert data['old_normalized_return'] > x
                cylinders.append(dict(a=a, kind=kind, depth=depth if kind == 'A' else len(word),
                                      index=index, bits=x.bit_length(), clock=data['clock'],
                                      rows=len(data['current']), sha256=digest(data['current'])))
    actual = []
    for a, kind, weight in itertools.product((5, 8, 32), ('A', 'B'), (1, 2)):
        witness = E.actual_source(a, kind, weight)
        data = witness['data']
        check_clock(witness['root'], data)
        assert data['old_normalized_return'] > witness['root'] > witness['N'] > data['lower']
        actual.append(dict(a=a, kind=kind, weight=weight, N=witness['N'],
                           root=witness['root'], lower=data['lower'], clock=data['clock']))
    counts = []
    for a, kind in itertools.product((2, 5, 8), ('A', 'B')):
        r, m = E.cylinder(a, kind)
        for scale in (1, 2, 7, 24):
            N = m*scale
            direct = sum(E.RUN.H.TRANSFER.residual_coefficient(N, x)
                         for x in range(r+m*((N-r)//m+1), 3*N//2, m))
            exact = E.weighted_count(N, a, kind)
            assert exact == direct
            leading = Fraction(25*N, 72*m)
            assert abs(exact-leading) <= 6
            counts.append(dict(a=a, kind=kind, N=N, mass=exact))
    cap = 10000
    conversions, saved = [], {}
    for kind in ('A', 'B'):
        witness = E.actual_source(5, kind, 2)
        x, data = witness['root'], witness['data']
        lower = E.RUN.H.LOCAL.FORCING.absorption_current({data['lower']: 1}, cap=cap)
        out = E.from_supplied_lower(x, lower, weight=2)
        one = E.from_supplied_lower(x, lower, weight=1)
        assert out['current'] == {u: 2*c for u, c in one['current'].items()}
        assert all(c > 0 for c in out['current'].values())
        conversions.append(dict(kind=kind, N=witness['N'], root=x, weight=2,
                                lower=data['lower'], discovery_cap=cap,
                                input_rows=len(lower), rows=len(out['current']),
                                sha256=digest(out['current'])))
        saved[kind] = out['current']
    return dict(status='PASS', scope='Partial d=4 half-seed bridges; universal even-return completion open',
                joint_cylinders=joint, split_catalogue=split, paired_nonacceptance_inputs=8192,
                original_cylinders=cylinders, actual_sources=actual, fixed_cylinder_counts=counts,
                supplied_conversions=conversions), saved


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write-receipt', action='store_true')
    args = parser.parse_args()
    result, saved = audit()
    receipt = HERE/'even_pair_audit.json'
    if args.write_receipt:
        receipt.write_text(json.dumps(result, indent=2)+'\n')
        for kind, current in saved.items():
            with (HERE/f'branch_{kind}_weight2_current.csv').open('w', newline='') as out:
                writer = csv.writer(out, lineterminator='\n')
                writer.writerow(('state', 'current'))
                writer.writerows(sorted(current.items()))
    else:
        assert json.loads(receipt.read_text()) == result
        for kind, current in saved.items():
            with (HERE/f'branch_{kind}_weight2_current.csv').open() as source:
                stored = {int(r['state']): int(r['current']) for r in csv.DictReader(source)}
            assert stored == current
    print(f"PASS: {len(result['joint_cylinders'])} joint cylinders; 8192 split inputs; "
          f"{len(result['original_cylinders'])} original cylinders; 12 actual sources; "
          '24 exact counts; two weight2 conversions')


if __name__ == '__main__':
    main()
