"""Sidekick probe: independent checks of main's C009 (experiments/cycle_spectrum/C009, main ec48fbd).

(1) The ordered q13 cycle 283 -> 431 -> 653 -> 493 -> 373 -> 283 (raw 3x+13): exact arrows, ordered with rank shift 3 on
    five ranks; deleting the height-one state 653 and keeping first returns gives successor ranks (2,0,3,1), not a
    circular shift.
(2) One-point deletion theorem: for a circular shift x -> x + s (mod m) with gcd(s, m) = 1, deleting one rank and
    taking first returns gives a circular shift on m-1 ranks iff s = 1 or s = m-1. Exhaustive for 3 <= m <= 40.
(3) The ordered q83 cycle with minimum 157 has the excursion 277 -> 457 -> 727 -> 283 with 32*283 = 27*277 + 83*19
    (slope 27/32 < 1, yet it rises by 6).
(4) The q = 1 open paths 7 -> 11 -> 17 -> 13 and 19 -> 29 -> 11 are exact Collatz odd-step paths.
Standard library. Run without -O.
"""
from fractions import Fraction as Fr
from math import gcd
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def v2(n):
    return (n & -n).bit_length() - 1


def step(x, q):
    y = 3 * x + q
    return y >> v2(y), v2(y)


def ordered_shift(ns):
    m, L = len(ns), min(ns)
    h = [((n // L).bit_length() - 1) for n in ns]
    z = [Fr(n, 2**hi) for n, hi in zip(ns, h)]
    order = sorted(range(m), key=lambda i: z[i])
    rank = {i: r for r, i in enumerate(order)}
    shifts = {(rank[(i + 1) % m] - rank[i]) % m for i in range(m)}
    return (next(iter(shifts)) if len(shifts) == 1 else None), h


def part1():
    cyc = [283, 431, 653, 493, 373]
    for a, b in zip(cyc, cyc[1:] + cyc[:1]):
        assert step(a, 13)[0] == b
    s, h = ordered_shift(cyc)
    assert s == 3 and h.count(1) == 1 and h[2] == 1
    core = [x for x, hi in zip(cyc, h) if hi == 0]           # minimum band, cyclic order 283, 431, 493, 373
    srt = sorted(core)
    rk = {x: srt.index(x) for x in core}
    succ = {core[i]: core[(i + 1) % len(core)] for i in range(len(core))}
    ranks = tuple(rk[succ[x]] for x in srt)
    assert ranks == (2, 0, 3, 1)
    disp = {(rk[succ[x]] - rk[x]) % 4 for x in core}
    assert len(disp) > 1
    return {"rank_shift": s, "core_successor_ranks": list(ranks)}


def induced_is_circular(m, s, deleted):
    keep = [r for r in range(m) if r != deleted]
    pos = {r: i for i, r in enumerate(keep)}
    def nxt(r):
        r = (r + s) % m
        while r == deleted:
            r = (r + s) % m
        return r
    disp = {(pos[nxt(r)] - pos[r]) % (m - 1) for r in keep}
    return len(disp) == 1


def part2():
    cases = 0
    for m in range(3, 41):
        for s in range(1, m):
            if gcd(s, m) != 1:
                continue
            for d in range(m):
                circ = induced_is_circular(m, s, d)
                assert circ == (s in (1, m - 1)), (m, s, d)
                cases += 1
    return {"cases": cases}


def part3():
    path = [277, 457, 727, 283]
    vals = []
    for a, b in zip(path, path[1:]):
        nxt, e = step(a, 83)
        assert nxt == b
        vals.append(e)
    assert 32 * 283 == 27 * 277 + 83 * 19 and sum(vals) == 5
    x, cyc = 157, []
    while True:
        cyc.append(x)
        x = step(x, 83)[0]
        if x == 157:
            break
    assert all(p in cyc for p in path)
    s, _ = ordered_shift(cyc)
    assert s is not None
    return {"valuations": vals, "cycle_period": len(cyc), "ordered_shift": s}


def part4():
    for path in ([7, 11, 17, 13], [19, 29, 11]):
        for a, b in zip(path, path[1:]):
            assert step(a, 1)[0] == b
    return {"open_paths_exact": True}


def main():
    out = {"probe": "c009_excursion_check", "main": "ec48fbd", "q13_cycle": part1(), "deletion_theorem": part2(),
           "q83_excursion": part3(), "q1_open_paths": part4(), "result": "PASS"}
    (HERE / "c009_excursion_check.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
