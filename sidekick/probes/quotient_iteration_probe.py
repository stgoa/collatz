"""Sidekick probe: does iterating main's normalized return (the quotient map
q -> nu(S(q)) of R25/R26, commit 541101a) change how slow roots descend?

Parts:
  (1) 2-adic random model: 60000 random 200-bit odd starts. Records the mean
      one-step drift and the probability of staying >= start for n steps,
      under raw Syracuse S and under the quotient nu(S(.)).
  (2) actual R26 remainder at N = 98304: steps to reach <= N under S, and under
      the quotient started from nu(f(x)).
Finite data; no termination claim. Standard library. Run without -O.
"""
from pathlib import Path
import json
import math
import random
import sys

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / "collatz_research_20261017" / "negative_controls")]
from affine_controls import step  # noqa: E402
from fibre_count_check import nu, selected  # noqa: E402
from residual_vs_induction import R  # noqa: E402
from run_bridge_check import ret  # noqa: E402


def model(T, rng, samples=60000, nmax=30):
    drift, stay = 0.0, [0]*(nmax + 1)
    for _ in range(samples):
        x0 = rng.randrange(2**199, 2**200) | 1
        x = x0
        for n in range(1, nmax + 1):
            y = T(x)
            if n == 1:
                drift += math.log2(y/x)
            x = y
            if x < x0:
                break
            stay[n] += 1
    return dict(drift_bits_per_step=round(drift/samples, 4),
                stay_5=stay[5]/samples, stay_15=stay[15]/samples, stay_30=stay[30]/samples,
                decay_per_step_15_30=round((stay[30]/stay[15])**(1/15), 4))


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    S = lambda x: step(1, x)
    Q = lambda x: nu(step(1, x))
    models = dict(raw=model(S, random.Random(2026)), quotient=model(Q, random.Random(2026)))
    N = 98304
    rem = [x for x, c in R(N).items() if not selected(x) and nu(ret(x)) > N]

    def steps(x, T):
        n = 0
        while x > N:
            x, n = T(x), n + 1
        return n
    raw = sorted(steps(x, S) for x in rem)
    quo = sorted(steps(nu(ret(x)), Q) for x in rem)
    pick = lambda v, p: v[int(p*(len(v) - 1))]
    report = dict(scope="Finite data and random-model estimates; no termination claim.",
                  model=models, N=N, remaining_roots=len(rem),
                  raw_steps_median_p90_max=[pick(raw, .5), pick(raw, .9), raw[-1]],
                  quotient_steps_median_p90_max=[pick(quo, .5), pick(quo, .9), quo[-1]],
                  status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
