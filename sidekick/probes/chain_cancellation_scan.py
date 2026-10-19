"""Sidekick probe (Q3): how often can main's isolated chain block be cancelled at zero cost?

Setting, from main's DELAYED_RELEASE.md (commit 65093c4):
  - X has v3(X-1) = h and 2^max(h+5,10) | X;
  - N = 3X/128, with chain sources y1 = 3X/2-1 (-2), y2 = 9X/4-1 (+2), y3 = 27X/8-1 (+2);
  - U = (X-1)/3^h.

A zero-cost cancellation is a set of negative annular sources whose forward paths
enter {y1, y2, y3} with total coefficient <= -2. Then the five-or-more-source submeasure
has an everywhere nonpositive current (traffic along the chain stays <= 0).

The search runs backwards from y1, y2, y3. It covers every inverse branch that a
source below 144N can reach within L forward steps; heights are capped at
(3/2)^m * 144N. It records annular sources with this lane's own point evaluator.
Calibration: on main's two delayed-release classes it recovers exactly v (distance 5)
and u (distance 7). Finite, bounded search only: absence within depth L is not
absence at any depth. Standard library. Run without -O.
"""
from collections import Counter
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / "collatz_research_20261017" / "negative_controls")]
from affine_controls import step, valuation  # noqa: E402
from progress_measures_audit import point_value  # noqa: E402
from delayed_release_check import family_X, parameters  # noqa: E402


def predecessors(y, cap):
    if y % 3 == 0:
        return
    p = (2 if y % 3 == 2 else 4)*y
    while p <= 3*cap + 1:
        if (p - 1)//3 > 1:
            yield (p - 1)//3
        p <<= 2


def chain_ancestors(X, L):
    """Annular sources within forward distance L of {y1,y2,y3}: {state: (coef, distance)}."""
    N = 3*X//128
    Q, top = 9*N//4, 144*N
    chain = [3*X//2 - 1, 9*X//4 - 1, 27*X//8 - 1]
    caps = [int(1.5**m*top) + 1 for m in range(L + 1)]
    found, seen, frontier = {}, set(chain), [(y, 0) for y in chain]
    while frontier:
        nxt = []
        for y, k in frontier:
            if k < L:
                for x in predecessors(y, caps[L - k - 1]):
                    if x not in seen:
                        seen.add(x)
                        if Q < x < 64*Q and x % 3:
                            c = point_value(1, 64*N, x) - point_value(1, N, x)
                            if c:
                                found[x] = (c, k + 1)
                        nxt.append((x, k + 1))
        frontier = nxt
    return found


def first_cancel(found):
    total = 0
    for k, mass in sorted((k, -c) for c, k in found.values() if c < 0):
        total += mass
        if total >= 2:
            return k
    return None


def word(x, X):
    chain = {3*X//2 - 1: "y1", 9*X//4 - 1: "y2", 27*X//8 - 1: "y3"}
    w = []
    while x not in chain and len(w) < 64:
        w.append(valuation(1, x))
        x = step(1, x)
    return "".join(map(str, w)) + "->" + chain.get(x, "?")


def representative(h, U, j):
    r = parameters(h)[0]
    M, b = 3**(h + r + 4), max(h + 5, 10)
    return (1 << b)*((1 + 3**h*U)*pow(1 << b, -1, M) % M) + j*(1 << b)*M


def scan(h, L, reps):
    r = parameters(h)[0]
    status, depths, uniform = Counter(), Counter(), []
    for U in range(3**(r + 4)):
        if U % 3 == 0:
            continue
        res = [first_cancel(chain_ancestors(representative(h, U, j), L)) for j in range(reps)]
        kind = "all" if None not in res else ("none" if set(res) == {None} else "mixed")
        status[kind] += 1
        if kind == "all":
            uniform.append(U)
            depths[max(res)] += 1
    return dict(h=h, r=r, classes_mod=3**(r + 4), admissible=2*3**(r + 3), depth_L=L,
                representatives=reps, cancel_in_all_reps=status["all"], mixed=status["mixed"],
                never=status["none"], uniform_classes=uniform,
                worst_depth_histogram={str(k): v for k, v in sorted(depths.items())})


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    for V in (47, 155):                                    # calibration on main's families
        r, Xs = family_X(2, V, count=1)
        found = chain_ancestors(Xs[0], 12)
        assert sorted((k, c) for c, k in found.values()) == [(5, -1), (7, -1)]
    rows = [scan(2, 16, 4), scan(3, 16, 2)]
    examples = {}
    for U in (124, 610, 691):                              # depth-7 classes outside main's families
        X = representative(2, U, 0)
        found = chain_ancestors(X, 9)
        examples[str(U)] = sorted([k, c, word(x, X)] for x, (c, k) in found.items() if c < 0)
    report = dict(scope="Bounded backward search from main's isolated chain; finite data, no proof.",
                  calibration="recovers main's delayed-release v (5) and u (7) exactly",
                  scans=rows, new_depth7_examples_h2=examples, status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in report.items()}, indent=1, sort_keys=True)[:3000])


if __name__ == "__main__":
    main()
