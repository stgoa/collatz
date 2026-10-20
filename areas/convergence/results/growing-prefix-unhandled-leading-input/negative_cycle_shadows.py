"""Sidekick probe: R53/R54 growing blocks are 2-adic shadows of the negative 3x+1 cycles.

1. On negative odd integers (|x| <= 4000), the quotient map T = nu o S (nu extended to
   negatives: F^-1 on x=5 mod 8, halving on selected x != -1) has exactly three cycles:
   {-1}, {-5,-7}, {-17,-25,-37,-55,-21,-31,-23}. R54's Psi and R53's G fix -17 and -5.
   R54's 'negative shadow' column is this 7-cycle.
2. Negative W5 indices w whose critical image nu(3w) lies on a cycle (|w| <= 4000): only
   w = -3 (q = -5) and w = -11 (q = -17); 3445 = -11 mod 3456 (R54's phase).
3. Measurement: main's continued dispatcher (seven rules + R52 + R53, commit 8764158) and
   R51's sigma dispatcher on the returning row w = 3 mod 9, for w at exact 2-adic depth K
   near -3 or -11, against generic selected w = 3 mod 9.
Standard library. Run without -O.
"""
from collections import Counter
from pathlib import Path
import json
import random
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path[:0] = [str(HERE), str(ROOT / "experiments/residual_progress/phase_rank"),
                str(ROOT / "experiments/residual_progress/continued_rules")]
from fibre_count_check import selected  # noqa: E402
import sigma_rank as SIG  # noqa: E402
import continued_rules as CONT  # noqa: E402


def S(x):
    z = 3*x + 1
    return z//(z & -z)


def nu_z(x):
    while True:
        if x % 8 == 5 and x != 1:
            x = (x - 1)//4
        elif x != -1 and selected(x):
            x = (x - 1)//2
        else:
            return x


def T(x):
    return nu_z(S(x))


def cycle_of(x):
    seen = []
    while x not in seen:
        seen.append(x)
        x = T(x)
    c = seen[seen.index(x):]
    i = c.index(max(c))
    return tuple(c[i:] + c[:i])


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    cycles = sorted({cycle_of(x) for x in range(-1, -4001, -2)}, key=len)
    assert cycles == [(-1,), (-5, -7), (-17, -25, -37, -55, -21, -31, -23)], cycles
    assert (2187*(-17) + 2363)//2048 == -17 and (9*(-5) + 5)//8 == -5
    on_cycle = {w: nu_z(3*w) for w in range(-3, -4001, -8) if any(nu_z(3*w) in c for c in cycles)}
    assert on_cycle == {-3: -5, -11: -17} and 3445 % 3456 == (-11) % 3456
    rng = random.Random(5)

    def accept(ws):
        cont = Counter(CONT.one_step(w) is not None for w in ws)[True]
        sig = Counter(SIG.one_step(w) is not None for w in ws)[True]
        return dict(samples=len(ws), continued_accepts=cont, sigma_accepts=sig)

    rows = {}
    ws = []
    while len(ws) < 200:
        w = rng.randrange(2**39, 2**40)//8*8 + 5
        if w % 9 == 3 and selected(3*w):
            ws.append(w)
    rows["generic selected, w=3 mod 9"] = accept(ws)
    for c in (-3, -11):
        for K in (12, 16, 20, 28):
            ws = []
            while len(ws) < 200:
                w = c + 2**K*rng.randrange(2**12, 2**13)
                if (w - c) % 2**(K + 1) and w % 9 == 3:
                    ws.append(w)
            assert all(selected(3*w) for w in ws)
            rows["w=%d mod 2^%d exactly, w=3 mod 9" % (c, K)] = accept(ws)
    report = dict(scope="Negative T-cycles behind R53/R54, and dispatcher acceptance on the returning row "
                        "near the two cycle-anchored W5 indices (measurement).",
                  negative_T_cycles=[list(c) for c in cycles], w5_indices_on_cycles=on_cycle,
                  returning_row_acceptance=rows, status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
