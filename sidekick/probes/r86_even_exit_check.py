"""Sidekick probe: independent check of R86's even-exit raw-target cone (main 2a37f31).

R86: H >= 3, q = 2^H t - 1 divisible by 3 (t odd), 3^(H-1) t - 1 = 4^b u with u odd, b >= 1, and
n = 3^b u = 1 mod 8. Then f = 2n + 1 is selected, nu(f) = n, the raw target is y = S(n) = (3n+1)/4, the
ordinary prefix of length H+b+1 from q and one arrow from y meet (S^(H+b+1)(q) = S(y)), and
    y < q  iff  3^(H+b) < 2^(H+2b+2)   (no small-source exception).
Checked with this branch's own step/nu/selected on inputs built by CRT for H = 3..14, b = 1..8.
Standard library. Run without -O.
"""
from pathlib import Path
import json
import random
import sys

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / "collatz_research_20261017" / "negative_controls")]
from affine_controls import step  # noqa: E402
from fibre_count_check import nu, selected  # noqa: E402


def Sn(x, n):
    for _ in range(n):
        x = step(1, x)
    return x


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    rng = random.Random(86)
    cases, inside, outside = 0, 0, 0
    for H in range(3, 15):
        for b in range(1, 9):
            made, tries = 0, 0
            while made < 12 and tries < 20000:
                tries += 1
                m8, m3 = 8, 3**(H - 1)
                r8 = pow(3, -b, 8)                       # n = 3^b u = 1 mod 8
                r3 = (-pow(4**b, -1, m3)) % m3            # 4^b u + 1 = 0 mod 3^(H-1)
                u0 = (r8*m3*pow(m3, -1, m8) + r3*m8*pow(m8, -1, m3)) % (m8*m3)
                u = u0 + m8*m3*rng.randrange(0, 2**(10 + 2*H))
                if u % 2 == 0 or u == 0:
                    continue
                t = (4**b*u + 1)//3**(H - 1)
                q = 2**H*t - 1
                if q % 3 or t % 2 == 0:
                    continue
                n = 3**b*u
                assert n % 8 == 1 and 3**(H - 1)*t - 1 == 4**b*u
                f = 2*n + 1
                assert selected(f) and nu(f) == n
                y = (3*n + 1)//4
                assert step(1, n) == y and Sn(q, H + b + 1) == step(1, y)
                predicted = 3**(H + b) < 2**(H + 2*b + 2)
                assert (y < q) == predicted, (H, b, u, y < q)
                inside += predicted
                outside += not predicted
                made += 1
                cases += 1
    report = dict(scope="Independent check of R86's raw-target cone and its exact inequality (main 2a37f31).",
                  cases=cases, inside_cone=inside, outside_cone=outside, status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
