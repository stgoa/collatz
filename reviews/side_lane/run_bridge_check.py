"""Sidekick probe: independent check of main's R26 run bridges (commit 541101a,
complementary_bridge/RUN_BLOCK_BRIDGES.md).

For a complementary root x = 2^a t - 1 (not selected), put d = v2(3^(a-1) t - 1) and
w = (3^(a-1) t - 1)/2^d. The return is f(x) = 3^((d-1)/2) w if d is odd, and
f(x) = 2*3^(d/2) w + 1 if d is even.

Checked here:
  (1) for every complementary x < 200000, the orbits of x and f(x) share a state
      before 1, or both enter 1 through F-siblings of the absorbing class. The
      steps on each side are recorded.
  (2) R26 coverage: with this lane's own normal form nu (fibre_count_check), the
      R_N mass certified by nu(f(x)) <= N is computed at three cutoffs.
Standard library. Run without -O.
"""
from collections import Counter
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / "experiments" / "packet_currents" / "negative_controls")]
from affine_controls import step  # noqa: E402
from fibre_count_check import nu, selected  # noqa: E402
from residual_vs_induction import R  # noqa: E402


def v2(n):
    return (n & -n).bit_length() - 1


def ret(x):
    a = v2(x + 1)
    t = (x + 1) >> a
    z = 3**(a - 1)*t - 1
    d = v2(z)
    w = z >> d
    return 3**((d - 1)//2)*w if d % 2 else 2*3**(d//2)*w + 1


def orbit(x):
    out = []
    while x != 1:
        out.append(x)
        x = step(1, x)
    return out


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    sides, via_one, max_x = Counter(), 0, 0
    for x in range(7, 200000, 4):
        if selected(x):
            continue
        ox = {u: i for i, u in reversed(list(enumerate(orbit(x))))}
        hit = next(((ox[u], j) for j, u in enumerate(orbit(ret(x))) if u in ox), None)
        if hit is None:
            last_x, last_f = orbit(x)[-1], orbit(ret(x))[-1]
            assert nu(last_x) == 1 and nu(last_f) == 1, x     # both enter 1 through F-siblings of 1
            via_one += 1
        else:
            sides[hit[1]] += 1
            max_x = max(max_x, hit[0])
    coverage = []
    for N in (6144, 49152, 98304):
        comp = {x: c for x, c in R(N).items() if not selected(x)}
        cert = sum(c for x, c in comp.items() if nu(ret(x)) <= N)
        coverage.append(dict(N=N, complementary_mass=sum(comp.values()), certified=cert,
                             remaining=sum(comp.values()) - cert,
                             remaining_over_N=round((sum(comp.values()) - cert)/N, 5)))
    assert coverage[0]["certified"] == 146 and coverage[0]["remaining"] == 123     # main's N=6144 figures
    report = dict(scope="Independent finite checks of main's R26 bridges and coverage.",
                  bridges=dict(roots_below=200000, f_side_steps=dict(sides), max_x_side_steps=max_x,
                               via_absorbing_class_only=via_one), coverage=coverage, status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
