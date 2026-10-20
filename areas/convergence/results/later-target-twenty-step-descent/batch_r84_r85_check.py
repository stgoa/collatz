"""Sidekick probe: independent checks of R84's prefix and sharp descent and R85's clock barrier
(main 355c173), with this branch's own step/nu (no main code).

R84: q = 11547 + 3*2^19*k: the first thirteen ordinary valuations are (1,2,1,1,1,1,1,2,2,1,1,2,2),
     the raw endpoint is R = 70237 + 2*3^14*k, and 4(R-1) < 25(q-1). On k = 9954 mod 16384 the first
     quotient step with T^n(q) < q is exactly n = 20.
R85: q canonical, 3^D | q, first J ordinary arrows of valuation 1 with canonical states,
     y_a = (3/2)^a (q+1) - 1. For every a <= J the only canonical origin p <= q with T^i(p) = y_a for
     some i <= D + a is p = q (at i = a). Checked by brute force over all canonical p <= q for
     small instances built from R85's construction.
Standard library. Run without -O.
"""
from pathlib import Path
import json
import random
import sys

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / "experiments" / "packet_currents" / "negative_controls")]
from affine_controls import step, valuation  # noqa: E402
from fibre_count_check import nu  # noqa: E402


def T(x):
    return nu(step(1, x))


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    rng = random.Random(84)
    word = (1, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 2, 2)
    for _ in range(3000):
        k = rng.randrange(0, 2**40)
        q = 11547 + 3*2**19*k
        x = q
        for a in word:
            assert valuation(1, x) == a
            x = step(1, x)
        R = 70237 + 2*3**14*k
        assert x == R and 4*(R - 1) < 25*(q - 1)
    sharp = 0
    for _ in range(300):
        k = 9954 + 16384*rng.randrange(0, 2**30)
        q = 11547 + 3*2**19*k
        x, n = q, 0
        while True:
            x, n = T(x), n + 1
            if x < q:
                break
        assert n == 20, (k, n)
        sharp += 1
    cases = 0
    for D in (1, 2, 3):
        for J in (1, 2, 3, 4):
            found, tries = 0, 0
            while found < 2 and tries < 20000:
                tries += 1
                H = rng.randrange(max(J + 1, 3), max(J + 1, 3) + 4)
                u = rng.randrange(1, 400)
                if u % 2 == 0 or u % 4 != (-pow(3, H, 4)) % 4:
                    continue
                q = 2**H*u - 1
                if q % 3**D or nu(q) != q or q > 120000:
                    continue
                ys, x, ok = [], q, True
                for a in range(1, J + 1):
                    if valuation(1, x) != 1:
                        ok = False
                        break
                    x = step(1, x)
                    if nu(x) != x:
                        ok = False
                        break
                    assert x == (3**a*(q + 1))//2**a - 1
                    ys.append(x)
                if not ok:
                    continue
                for a, y in enumerate(ys, start=1):
                    hits = []
                    for p in range(3, q + 1, 2):
                        if nu(p) != p:
                            continue
                        z = p
                        for i in range(1, D + a + 1):
                            z = T(z)
                            if z == y:
                                hits.append((p, i))
                                break
                    assert hits == [(q, a)], (q, D, J, a, hits[:5])
                found += 1
                cases += 1
    report = dict(scope="Independent checks of R84 prefix/sharp descent and R85 clock barrier (main 355c173).",
                  r84_prefix_cases=3000, r84_sharp_cases=sharp, r85_brute_force_instances=cases, status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
