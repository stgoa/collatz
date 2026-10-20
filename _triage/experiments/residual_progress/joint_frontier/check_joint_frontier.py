"""Bounded replay of complete local interfaces and unfinished frontiers."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import joint_frontier as J

HERE = Path(__file__).resolve().parent


def digest(rows):
    value = '\n'.join(f'{x:x}:{c}' for x, c in sorted(rows.items()))
    return hashlib.sha256(value.encode()).hexdigest()


def word(x, n):
    out = []
    for _ in range(n):
        assert x > 1
        out.append(J.v2(3*x+1))
        x = J.step(x)
    return out


def audit():
    interface_counts = {'3mod8': 0, '7mod8': 0}
    for v in range(3, 32768, 4):
        data = J.interface(v)
        assert word(18*v+3, 2) == data['upper_word']
        assert word(v, 2) == data['lower_word']
        if v % 16 == 3:
            assert data['lower'] < v
        else:
            assert data['lower'] > v
        interface_counts[data['kind']] += 1
    for v in range(3, 65536, 32):
        data = J.shadow_frontier(v)
        assert word(18*v+3, data['upper_clock']) == data['upper_word']
        assert word(v, 2) == data['lower_word']
        assert data['frontier'] % 27 == 22
        assert 3*data['u'] <= v
    parameterized = []
    for h in range(2, 17):
        residue = 4*pow(2**h, -1, 9) % 9
        if residue % 2 == 0:
            residue += 9
        for index in (0, 1, 7):
            u = residue+18*index
            v = (2**(h+3)*u-5)//9
            data = J.shadow_frontier(v)
            assert (data['h'], data['u']) == (h, u)
            assert word(18*v+3, data['upper_clock']) == data['upper_word']
            parameterized.append(dict(h=h, u=u, v=v, frontier=data['frontier']))
    expanding = []
    for r in (0, 1, 2, 4, 8, 9, 16, 27, 32, 54, 128):
        data = J.expanding_family(r)
        assert word(18*data['v']+3, data['upper_clock']) == data['upper_word']
        assert data['residual'] == {data['frontier']: 1}
        assert data['frontier'] % 3 == 1  # R34 eta has h=0.
        expanding.append(dict(r=r, v=data['v'], frontier=data['frontier'],
                              clock=data['upper_clock'], rows=len(data['current']),
                              sha256=digest(data['current'])))
    embedded = []
    for r in (0, 9, 18, 27, 54):
        data = J.embedded_family(r)
        assert word(data['root'], data['clock']) == data['upper_word']
        assert word(data['lower'], 4) == data['lower_word']
        assert J.divergence(data['lower_current']) == {data['lower']: 1}
        assert J.combine((1, data['current']), (1, data['lower_current'])) == data['upper_current']
        embedded.append(dict(r=r, root=data['root'], lower=data['lower'],
                             frontier=data['frontier'], clock=data['clock']))
    actual, saved = [], {}
    for r in (27, 54, 81, 108):
        data = J.required_ray_family(r)
        assert word(data['root'], data['clock']) == data['upper_word']
        assert data['residual'] == {data['frontier']: 1}
        assert J.divergence(data['upper_current']) == {data['root']: 1, data['frontier']: -1}
        actual.append(dict(r=r, N=data['N'], root=data['root'], weight=data['weight'],
                           lower=data['lower'], frontier=data['frontier'], clock=data['clock'],
                           rows=len(data['current']), sha256=digest(data['current'])))
        if r == 27:
            saved['frontier'] = data['current']
            saved['lower'] = data['lower_current']
    result = dict(status='PASS', scope='Complete local interface; unresolved positive frontiers retained',
                  two_arrow_inputs=8192, interface_classes=interface_counts,
                  complete_block_inputs=2048, parameterized_cases=parameterized,
                  expansion_family=expanding, d4_embeddings=embedded, required_ray_sources=actual)
    return result, saved


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write-receipt', action='store_true')
    args = parser.parse_args()
    result, saved = audit()
    receipt = HERE/'joint_frontier_audit.json'
    if args.write_receipt:
        receipt.write_text(json.dumps(result, indent=2)+'\n')
        for name, rows in saved.items():
            with (HERE/f'actual_r27_{name}_current.csv').open('w', newline='') as out:
                writer = csv.writer(out, lineterminator='\n')
                writer.writerow(('state', 'current'))
                writer.writerows(sorted(rows.items()))
    else:
        assert json.loads(receipt.read_text()) == result
        for name, rows in saved.items():
            with (HERE/f'actual_r27_{name}_current.csv').open() as source:
                stored = {int(row['state']): int(row['current']) for row in csv.DictReader(source)}
            assert stored == rows
    print('PASS: 8192 complete interfaces; 2048 blocks; 45 parameter cases; '
          '11 expansion cases; five d4 embeddings; four full-weight ray sources')


if __name__ == '__main__':
    main()
