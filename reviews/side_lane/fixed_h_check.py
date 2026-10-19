"""Sidekick probe: independent check of main's fixed-h depth theorem
(experiments/residual_progress/phase_depth/FIXED_H_DEPTH.md, commit 8e2b5eb).

Claim: for every D >= 1 and X with 2^max(D+4,10) | X and X = 10 (mod 3^(D+2)),
N = 3X/128 has h = v3(X-1) = 2. The whole depth-D component of 144N-1 is the
chain y_1..y_(D+3) with sources (-2, +2, +2). For each D, some such X are on
the ladder N = 96*64^k.

Checked here with this lane's own code:
  1. the barrier lemma's finite data:
     - the union of Syracuse orbits of odd 1..33;
     - the full list of (z0, u0, c0) candidates;
     - each c0 > 1 entering a 3x-1 cycle that avoids 1, via the d = -1 map of affine_controls;
  2. the theorem by brute force (full forward exposure of every source) for D = 1..4 at the
     least admissible X;
  3. ladder membership: 2^e = 10 (mod 3^(D+2)) is solvable with 6 | e for D <= 12.
Finite checks only. Standard library. Run without -O.
"""
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / "experiments" / "packet_currents" / "negative_controls")]
from affine_controls import Basins, step  # noqa: E402
from delayed_release_check import isolated_through  # noqa: E402
from depth_probe import v3  # noqa: E402

MAIN_UNION = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 41, 47, 53, 61, 71,
              91, 103, 107, 121, 137, 155, 161, 167, 175, 233, 251, 263, 283, 319, 325, 377, 395,
              425, 433, 445, 479, 577, 593, 719, 911, 1079, 1367, 1619, 2051, 2429, 3077}
MAIN_TABLE = {(155, 16, 5), (167, 18, 13), (175, 18, 5), (233, 24, 7), (251, 27, 19), (263, 27, 7),
              (319, 32, 1), (325, 36, 35), (433, 48, 47), (445, 48, 35), (479, 48, 1), (577, 64, 63),
              (593, 64, 47), (719, 72, 1), (911, 96, 49), (1079, 108, 1), (1367, 144, 73),
              (1619, 162, 1), (2051, 216, 109), (2429, 243, 1), (2429, 256, 131), (3077, 324, 163)}


def barrier():
    union = set()
    for s in range(1, 34, 2):
        x = s
        while True:
            union.add(x)
            if x == 1:
                break
            x = step(1, x)
    assert union == MAIN_UNION
    smooth = sorted({2**a*3**b for a in range(13) for b in range(9) if 2**a*3**b <= 400})
    table = {(z, u, 10*u - z) for z in union for u in smooth if u >= 4 and 9*u < z < 10*u}
    assert table == MAIN_TABLE
    minus = Basins(-1)
    for z, u, c in table:
        if c != 1:
            assert c % 2 and minus(c) in (5, 17)          # 3x-1 cycles {5,7} and {17,...,91}
    return len(table)


def least_X(D):
    power, mod = 1 << max(D + 4, 10), 3**(D + 2)
    X = power
    while X % mod != 10 % mod:
        X += power
    return X


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    rows = barrier()
    brute = []
    for D in (1, 2, 3, 4):
        X = least_X(D)
        assert v3(X - 1) == 2 and (3*X) % 128 == 0 and (3*X//128) % 8 == 0
        assert isolated_through(X, D), (D, X)
        brute.append(dict(D=D, X=X, N=3*X//128))
    ladder = {}
    for D in range(1, 13):
        mod = 3**(D + 2)
        e = next(e for e in range(2*3**(D + 1)) if pow(2, e, mod) == 10 % mod)
        assert e % 6 == 0
        ladder[D] = e
    report = dict(scope="Independent finite checks of main's FIXED_H_DEPTH theorem; its universal "
                  "quantifier rests on main's written proof.", barrier_table_rows=rows,
                  brute_force_isolation=brute, ladder_exponent_mod_2_3_pow=ladder, status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
