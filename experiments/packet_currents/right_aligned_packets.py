"""Finite checks for the right-aligned depth-one Collatz packet reduction.

This verifies finite identities, not the universal current-existence conjecture.
Standard library only. Run without -O.
"""
from collections import defaultdict
from pathlib import Path
import json

CORE = {5, 7, 11, 13}
CORE_TAU = {5: 1, 7: 5, 11: 4, 13: 2}


def clean(mu):
    return {x: c for x, c in mu.items() if c}


def step(x):
    assert x > 0 and x % 2
    z = 3*x + 1
    return z // (z & -z)


def initial(N):
    n1, n2 = (3*N + 1)//2, (3*N + 1)//4
    return {x: 3*int(x % 3 == 2) - 1
            + (3*int(x % 3 == 1) - 1 if x <= n2 else 0)
            for x in range(3, n1 + 1, 2)}


def push(mu):
    out = defaultdict(int)
    for x, c in mu.items():
        y = step(x)
        if y > 1:
            out[y] += c
    return clean(out)


def right_packets(N, materialize=True):
    """Return packet measure and fixed-core remainder; O(log N) core-only mode."""
    assert N >= 8
    b = (N - 1).bit_length()
    packet, eta = defaultdict(int), defaultdict(int)
    triples = 0
    for a in range(1, b + 1):
        power = 1 << a
        period = 2*power
        if a % 2:
            q, e, first = (5*power - 1)//3, 5, 0
        else:
            q, e, first = (power - 1)//3, 1, 1
        assert 3*q + 1 == power*e
        for cutoff, target in (((3*N + 1)//2, 2), ((3*N + 1)//4, 1)):
            last = (cutoff - q)//period
            size = max(0, last - first + 1)
            leftover = size % 3
            for t in range(first, first + leftover):
                x, y = q + period*t, e + 6*t
                assert 1 < x <= cutoff and y in CORE
                eta[y] += 3*int(x % 3 == target) - 1
            triples += size//3
            if materialize:
                for t in range(first + leftover, first + size, 3):
                    total = 0
                    for j in range(3):
                        x, y = q + period*(t+j), e + 6*(t+j)
                        c = 3*int(x % 3 == target) - 1
                        assert 1 < x <= cutoff and y > 1
                        packet[y] += c
                        total += c
                    assert total == 0
    return clean(packet), clean(eta), triples


def audit(N):
    packet, eta, triples = right_packets(N)
    expected = push(initial(N))
    combined = defaultdict(int, packet)
    for x, c in eta.items():
        combined[x] += c
    assert clean(combined) == expected
    assert sum(packet.values()) == 0
    assert set(eta) <= CORE
    assert sum(abs(c) for c in eta.values()) <= 6*(N-1).bit_length()
    return dict(N=N, packet_atoms=len(packet), raw_triples=triples,
                core_remainder=eta, core_norm=sum(abs(c) for c in eta.values()))


def main():
    for x, expected in CORE_TAU.items():
        y, t = x, 0
        while y > 1:
            y, t = step(y), t + 1
        assert t == expected
    for x in range(1, 16, 2):
        y = x
        for _ in range(10):
            if y == 1:
                break
            y = step(y)
        assert y == 1
    for N in range(8, 2049):
        audit(N)
    selected = [audit(N) for N in (4096, 10001, 262144)]
    mu, _, _ = right_packets(32)
    work = 0
    for _ in range(39):
        work += sum(mu.values())
        mu = push(mu)
    assert work == 57
    periodic = {
        0: {5: 2, 7: -1}, 1: {5: -1, 7: 1, 13: -1},
        2: {5: -1, 13: -2}, 3: {5: -1, 7: -1},
        4: {5: -1, 7: -2, 13: 2}, 5: {5: 2, 7: -3, 13: 1},
    }
    for b in range(3, 1001):
        _, eta, _ = right_packets(1 << b, materialize=False)
        assert eta == periodic[b % 6]
        for L in range(7):
            correction = -1 + sum(c*min(L, CORE_TAU[x]) for x, c in eta.items())
            assert -12 <= correction <= 1
    # Exact rational inequality used in the maximum principle:
    # 1/sqrt(2) < 5/7, and 1/8 + 245/384 + 343/1536 = 505/512 < 1.
    assert 7**2 < 2*5**2
    assert 192 + 980 + 343 == 1515
    assert 1515*512 == 505*1536
    result = dict(status="PASS", consecutive_cutoffs=[8, 2048],
                  selected=selected, dyadic_exponents=[3, 1000],
                  all_horizon_dyadic_correction=[-12, 1],
                  positive_work_witness=dict(N=32, L=39, H=work),
                  universal_current_existence_proved=False)
    path = Path(__file__).with_name("right_aligned_audit.json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
