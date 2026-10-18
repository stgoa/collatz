"""Check the saved finite cycle witnesses from the independently reviewed feed.

This does not repeat external random experiments or fetch external source.
The inspected, pinned reproductions are documented in the adjacent receipt.
"""
import json
from pathlib import Path


def step(x, d):
    if x == 1 or (d > 1 and x == d):
        return x
    y = 3*x+d
    assert y > 0
    return y // (y & -y)


def check_orbit(data, start, d):
    prefix, cycle = data['prefix'], data['cycle']
    assert cycle
    states = prefix+cycle
    assert (prefix[0] == start if prefix else start in cycle)
    assert len(states) == len(set(states))
    assert all(x > 0 and x % 2 == 1 for x in states)
    for x, y in zip(prefix, prefix[1:]):
        assert step(x, d) == y
    # Saved cycles are rotated to their least state, not to the entry state.
    if prefix:
        assert step(prefix[-1], d) in cycle
    for x, y in zip(cycle, cycle[1:]):
        assert step(x, d) == y
    assert step(cycle[-1], d) == cycle[0]
    return set(cycle)


def main():
    data = json.loads((Path(__file__).with_name('pair_domain_external_review.json')).read_text())
    assert data['external_commit'] == 'dbb0dea5930ec667b70b5dfcbb595e5d566451b0'
    assert data['status'] == 'PASS' and not data['external_branch_modified']
    assert all(r['published_receipt_matches'] for r in data['unmodified_probe_reproductions'].values())
    witnesses = data['independent_control_witnesses']
    assert [(r['d'], r['w']) for r in witnesses] == [(-1, 3), (-1, 11), (13, 19), (61, 235)]
    for row in witnesses:
        d, w = row['d'], row['w']
        left = check_orbit(row['w_orbit'], w, d)
        right = check_orbit(row['triple_orbit'], 3*w, d)
        absorbers = {1, d} if d > 1 else {1}
        assert left.isdisjoint(right)
        # One endpoint enters a nonabsorbing cycle, the other an absorber.
        # Its basin indicator is invariant on every unkilled arrow.
        if right.isdisjoint(absorbers):
            assert left <= absorbers
            pairing = 1
        else:
            assert right <= absorbers and left.isdisjoint(absorbers)
            pairing = -1
        assert pairing == row['cycle_indicator_pairing'] != 0
    latest = json.loads((Path(__file__).with_name('side_lane_review_1a2dfc5.json')).read_text())
    assert latest['source_commit'] == '1a2dfc5710c5e17a4f42355a3dce2d6984b2b09b'
    assert latest['status'] == 'PASS' and latest['unmodified_probe_reproduced']
    assert not latest['external_branch_modified']
    witnesses = latest['independent_W5_control_witnesses']
    assert [(r['d'], r['w']) for r in witnesses] == [(-1, 5), (13, 53), (61, 133)]
    for row in witnesses:
        d, w = row['d'], row['w']
        assert w % 8 == 5
        left = check_orbit(row['w_orbit'], w, d)
        right = check_orbit(row['triple_orbit'], 3*w, d)
        absorbers = {1, d} if d > 1 else {1}
        assert left.isdisjoint(right)
        if right.isdisjoint(absorbers):
            assert left <= absorbers
            pairing = 1
        else:
            assert right <= absorbers and left.isdisjoint(absorbers)
            pairing = -1
        assert pairing == row['cycle_indicator_pairing'] != 0
    print('PASS: seven exact control pairs, including three W5 witnesses, with nonzero invariant pairings')


if __name__ == '__main__':
    main()
