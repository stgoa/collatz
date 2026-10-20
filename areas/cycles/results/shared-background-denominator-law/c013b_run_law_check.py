"""Independent check of the Lean lane's C013 OVERLAP_THEORY.md sections 1-2 unit (claude/lean-lane 9a81b08).

On every actual 3x+q cycle found by iteration (any order; q in 1, 5, 7, 11, 13, 17, 19, 23, 29, 61, 233,
1201), listed from its minimum, for every nonidentity rotation h and every maximal agreeing run (i, t)
(a_(i+j) = a_(i+j+h) for j < t, maximal on both sides; t = 0 included), with z_j = n_(j+h) - n_j and
E = sum of the run's letters:
  z even and nonzero (primitive cycles); 2^E z_(i+t) = 3^t z_i (run law);
  k := z_(i+t)/(2*3^t) is an integer with z_i = 2^(E+1) k, k != 0;
  diameter: 2 max(2^E, 3^t) <= H - n_0;
  (7): 6 D max(2^E, 3^t) < m q 2^A (2^(B+1) - 1), with the actual B.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from s1a_integer_cycle_check import cycles, step  # noqa: E402


def main():
    n_cyc = n_runs = 0
    slack = []
    for q, N in [(1, 2001), (5, 40001), (7, 40001), (11, 20001), (13, 40001), (17, 20001),
                 (19, 20001), (23, 20001), (29, 20001), (61, 40001), (233, 20001), (1201, 8001)]:
        for cyc in cycles(q, N):
            m = len(cyc)
            if m < 2:
                continue
            i0 = cyc.index(min(cyc))
            n = cyc[i0:] + cyc[:i0]
            a = [step(x, q)[1] for x in n]
            A = sum(a)
            D = 2**A - 3**m
            L, H = n[0], max(n)
            B = 0
            while H >= 2**(B + 1) * L:
                B += 1
            for h in range(1, m):
                z = [n[(j + h) % m] - n[j] for j in range(m)]
                assert all(x % 2 == 0 and x != 0 for x in z)
                agree = [a[j] == a[(j + h) % m] for j in range(m)]
                if all(agree):
                    continue  # cannot happen for a primitive cycle and h != 0
                # maximal runs: start where previous position disagrees
                for i in range(m):
                    if agree[(i - 1) % m]:
                        continue
                    t = 0
                    while agree[(i + t) % m]:
                        t += 1
                    E = sum(a[(i + j) % m] for j in range(t))
                    zs, ze = z[i], z[(i + t) % m]
                    assert 2**E * ze == 3**t * zs
                    assert ze % (2 * 3**t) == 0
                    k = ze // (2 * 3**t)
                    assert zs == 2**(E + 1) * k and k != 0
                    M = max(2**E, 3**t)
                    assert 2 * M <= H - L
                    lhs, rhs = 6 * D * M, m * q * 2**A * (2**(B + 1) - 1)
                    assert lhs < rhs
                    slack.append(rhs / lhs)
                    n_runs += 1
            n_cyc += 1
    out = {"probe": "c013b_run_law_check", "lean": "claude/lean-lane 9a81b08",
           "cycles_m_ge_2": n_cyc, "maximal_agreeing_runs": n_runs,
           "slack_rhs_over_lhs_of_(7)": {"min": round(min(slack), 2), "max": round(max(slack), 1)},
           "result": "PASS"}
    js = json.dumps(out, indent=1)
    print(js)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as f:
            f.write(js + "\n")


if __name__ == "__main__":
    main()
