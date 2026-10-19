"""Sidekick probe: independent checks for main's R40/R41 batch (commit 4a45eb0).

R37 planner, as restated in CRITICAL_NINE_ELIMINATION.md section 2 and rebuilt from the text:
  q = nu(x); stop if q = 1; if q = 1 (mod 8), step to S(q) < q; if q = 2 (mod 3), go to
  (2q-1)/3 < q; otherwise request u = q/3 (q = 0 mod 3) or (2q+1)/3 (q = 1 mod 3) and
  continue from u.
  Checked: termination; requests lie in W5 u W9 and strictly decrease; u <= (2x+1)/3;
  every index in I_(3z) u I_z is <= (3z+1)/2 (the "sharper tripling bound").
R41: every odd q = 4 (mod 9) has ancestor p = 2^h(2q+1)/3^h - 1, h = v3(2q+1), with exact
  valuation word 1^(h-1),2 to q, and p < q.
R41 barrier: for canonical q > 1 with q = 1 (mod 3^D), every y with T^j(y) = q for
  1 <= j <= D, where T = nu o S, is larger than q, and the least such y is (4q-1)/3. Brute
  force over y < 2*10^6.
Standard library. Run without -O.
"""
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / "collatz_research_20261017" / "negative_controls")]
from affine_controls import step, valuation  # noqa: E402
from fibre_count_check import nu  # noqa: E402


def v3(n):
    k = 0
    while n % 3 == 0:
        n, k = n//3, k + 1
    return k


def plan(x):
    requests = []
    while True:
        q = nu(x)
        if q == 1:
            return requests
        if q % 8 == 1:
            nxt = step(1, q)
            assert nxt < q
        elif q % 3 == 2:
            nxt = (2*q - 1)//3
            assert step(1, nxt) == q and nxt < q
        else:
            nxt = q//3 if q % 3 == 0 else (2*q + 1)//3
            requests.append(nxt)
        x = nxt


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    W = lambda u: u % 8 == 5 or u % 16 == 9
    n_plans = 0
    for x in range(3, 200000, 2):
        I = plan(x)
        assert all(W(u) for u in I) and all(a > b for a, b in zip(I, I[1:]))
        assert all(3*u <= 2*x + 1 for u in I)
        n_plans += 1
    for z in range(1, 60000, 2):
        assert all(2*u <= 3*z + 1 for u in plan(3*z) + plan(z)), z
    for q in range(13, 10**6, 18):                          # odd q = 4 (mod 9)
        h = v3(2*q + 1)
        p = 2**h*(2*q + 1)//3**h - 1
        assert h >= 2 and p < q
        y = p
        for a in [1]*(h - 1) + [2]:
            assert valuation(1, y) == a
            y = step(1, y)
        assert y == q
    T = lambda y: nu(step(1, y))
    H = 2*10**6
    Tmap = {y: T(y) for y in range(3, H, 2)}
    barrier = []
    for D in (2, 3):
        for q in [q for q in range(3, 4000, 2) if q % 3**D == 1 and nu(q) == q][:40]:
            level, preds = {q}, set()
            for _ in range(D):
                level = {y for y, t in Tmap.items() if t in level and y != 1}
                preds |= level
            if preds:
                assert min(preds) > q and min(preds) == (4*q - 1)//3, (D, q, min(preds))
            barrier.append(q)
    report = dict(scope="Independent finite checks for main's R40/R41 batch (commit 4a45eb0).",
                  planner_inputs=n_plans, tripling_bound_z_below=60000,
                  r41_identity_q_below=10**6, r41_barrier_q_checked=len(barrier),
                  r41_barrier_search_bound=H, status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
