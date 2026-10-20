"""Cross-model audit of two claims added on main in commit 8d62dcc.

  * R5 (five rays): the grid N = a 2^b, a in {12,14,16,18,21}, b >= 3, has the
    exact cutoffs, upper targets and comparison values used in its maximum
    principle, and the contraction constant is below 89/90;
  * R6 (annular recursion): for 8 | N, Pi_(64N) = Pi_N + A_N, eta_(64N) = eta_N,
    with the stated supports, band table modulo 18 and exact norms.

Every packet here comes from affine_controls.py, which was written
independently of both right_aligned_packets.py and main's checkers. The
negative controls are also run on the five-ray grid. Finite checks only.
Standard library only. Run without -O.
"""
from fractions import Fraction
from pathlib import Path
import json
import sys

from affine_controls import Basins, cutoffs, packets, pairing, prefix_tables

RAYS = (12, 14, 16, 18, 21)
BANDS = {  # main's table: j -> residue mod 18 -> coefficient
    0: {1: 1, 5: 0, 7: 1, 11: 0, 13: -2, 17: 0},
    1: {1: 2, 5: 1, 7: -1, 11: 1, 13: -1, 17: -2},
    2: {1: 3, 5: -1, 7: -3, 11: 2, 13: 0, 17: -1},
    3: {1: 1, 5: -3, 7: -2, 11: 3, 13: 1, 17: 0},
    4: {1: -1, 5: -2, 7: -1, 11: 1, 13: 2, 17: 1},
    5: {1: 0, 5: -1, 7: 0, 11: -1, 13: 0, 17: 2},
}


def check_five_rays(bmax):
    """Exponents of F(a_i 2^b) = 2^((5b+i)/3) are tracked as integers 5b+i."""
    for b in range(3, bmax + 1):
        for i, a in enumerate(RAYS):
            M = a << b
            n0, n1, n2 = cutoffs(1, M)
            assert M % 8 == 0 and (n0, n1, n2) == (M//4 - 1, 3*M//2, 3*M//4)
            s, j = divmod(i + 3, 5)
            target = RAYS[j] << (b + s)
            assert 2*target >= 3*M and n1 <= target and n2 <= target//2
            assert (5*(b + s) + j) - (5*b + i) == 3            # F(M') = 2 F(M)
            assert RAYS[i] << (b - 2) == M//4 and n0 < M//4    # F(M/4) = 2^(-10/3) F(M)
            for point, exponent in ((M//4, b - 2), (target//2, b + s - 1)):
                assert exponent >= 3 or point < 96
    # 2^-10/3 < 1/10 and 2^-5/3 < 1/3 from 2^10 > 10^3, 2^5 > 3^3
    assert 2**10 > 10**3 and 2**5 > 3**3
    assert Fraction(1, 10) + Fraction(2, 3)*(1 + Fraction(1, 3)) == Fraction(89, 90)
    return bmax


def check_annular(N):
    assert N % 8 == 0
    Q = 9*N//4
    small, eta, _ = packets(1, N)
    big, eta_big, _ = packets(1, 64*N)
    assert eta_big == eta and all(1 < y < Q for y in small)
    A = dict(big)
    for y, c in small.items():
        A[y] = A.get(y, 0) - c
    A = {y: c for y, c in A.items() if c}
    assert all(Q < y < 64*Q for y in A)
    for j in range(6):
        lo, hi = Q << j, Q << (j + 1)
        total = 0
        for y in range(lo + 1, hi, 2):
            want = 0 if y % 3 == 0 else BANDS[j][y % 18]
            assert A.get(y, 0) == want, (N, j, y)
            total += want
        assert total == 0
    assert sum(A.values()) == 0 and sum(y*c for y, c in A.items()) == 63*Q
    assert sum(map(abs, A.values()))*2 == 99*N
    assert sum(c for c in A.values() if c > 0)*4 == 99*N
    assert len(A)*8 == 267*N
    return len(A)


def controls_on_grid(d, nmax):
    basins = Basins(d)
    top = 3*cutoffs(d, nmax)[1] + 3*abs(d) + 16
    by_res, total = prefix_tables(basins, top)
    grid = sorted(a << b for a in RAYS for b in range(3, 40) if (a << b) <= nmax)
    failing = [M for M in grid if pairing(d, basins, by_res, total, M)[0] > 0]
    return dict(grid_points=len(grid), failing=len(failing), failing_cutoffs=failing[:12])


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    report = dict(scope="Independent finite checks of main's R5 arithmetic and R6 identities; "
                  "neither result supplies universal currents.")
    report["five_rays"] = dict(exponents_b=[3, check_five_rays(400)], status="PASS")
    cases = list(range(8, 513, 8)) + [768, 1024, 2048, 4096]
    sizes = {N: check_annular(N) for N in cases}
    report["annular"] = dict(N=cases[:1] + [cases[-1]], cases=len(cases),
                             largest_expanded_cutoff=64*cases[-1], status="PASS")
    report["controls_on_five_ray_grid"] = {str(d): controls_on_grid(d, 20000) for d in (-1, 61)}
    report["status"] = "PASS"
    path = Path(__file__).with_name("main_claims_audit.json")
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
