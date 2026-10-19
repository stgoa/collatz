"""Sidekick probe (Q6): can merging with the excursions of absorbed seeds fire while high?

F_N is the union of Syracuse orbits of odd seeds <= N. The probe measures:
  - the density of F_N among odd numbers in height bands [H N, 2H N);
  - for every root of main's R17 residual R_N, the first step at which its orbit
    meets F_N, compared with its first step below N.
Finite data at N = 49152; no termination claim. Standard library. Run without -O.
"""
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / "experiments" / "packet_currents" / "negative_controls")]
from affine_controls import step  # noqa: E402
from residual_vs_induction import R  # noqa: E402


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    N = 49152
    F = set()
    for s in range(1, N + 1, 2):
        x = s
        while x not in F:
            F.add(x)
            if x == 1:
                break
            x = step(1, x)
    density = {}
    for k in range(0, 11):
        H = 2**k
        count = sum(1 for y in F if H*N <= y < 2*H*N)
        density[str(H)] = dict(density=count/(H*N/2), times_H2=count/(H*N/2)*H*H)
    rows = []
    for x in sorted(R(N)):
        y, j, td, tm, hm = x, 0, None, None, None
        while td is None:
            y, j = step(1, y), j + 1
            if tm is None and y in F:
                tm, hm = j, y/N
            if y <= N:
                td = j
        rows.append((x, td, tm, hm))
    desc, merge = sorted(r[1] for r in rows), sorted(r[2] for r in rows)
    pick = lambda v, p: v[int(p*(len(v) - 1))]
    slow = sorted(rows, key=lambda r: -r[1])[:6]
    report = dict(scope="Finite data at N=49152; no termination claim.", N=N, F_size=len(F),
                  F_max_over_N=max(F)/N, density_by_height=density, roots=len(rows),
                  descent_median_p99_max=[pick(desc, .5), pick(desc, .99), desc[-1]],
                  merge_median_p99_max=[pick(merge, .5), pick(merge, .99), merge[-1]],
                  merge_before_descent_fraction=sum(r[2] < r[1] for r in rows)/len(rows),
                  slowest=[dict(x=r[0], descent=r[1], merge=r[2], merge_height_over_N=round(r[3], 3))
                           for r in slow], status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in report.items() if k != "density_by_height"}, indent=1))


if __name__ == "__main__":
    main()
