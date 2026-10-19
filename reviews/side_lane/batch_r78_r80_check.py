"""Sidekick probe: independent checks of R78's six-arrow native prefix, R79's return count, and
R80's high-history family and anchor (main 3b0c8a5), with this branch's own step/nu/selected.

R78: b = 905 mod 8192, t = (27b+13)/128 = 191 mod 1728, c = (27t-1)/4. From n = 3b the six ordinary
     arrows have valuations (1,2,1,1,1,2) and end at r = (81t-1)/2, which is selected, nu(r) = 3c.
     (Then c = U(b) = (729b+223)/512.)
R79: Y(b) = 217b + 223 has Y(U b) = (729/512) Y(b); the number of consecutive complete returns
     U^s(b) in G = {905 mod 8192} equals floor((v2(Y(b)) - 13)/9).
R80: q = 11547 + 2^17 3^D t, b = q/3, p = 11391 + 2^36 3^(D-12) t, y = (3q+1)/2 (D >= 12):
     b < p < q < y; p, q, y canonical; p's thirteen arrows (1^6,2,2,1^4,2) end at F^2(y) = 24q+13;
     every state after p exceeds q, with peak 32q+17; S^2(q) = S^14(p) = (9q+5)/8 > q.
     Anchor: 11547 has no smaller canonical ancestor at any depth (forward closure of all canonical
     states below it).
Standard library. Run without -O.
"""
from pathlib import Path
import json
import random
import sys

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / "collatz_research_20261017" / "negative_controls")]
from affine_controls import step, valuation  # noqa: E402
from fibre_count_check import nu, selected  # noqa: E402


def v2(n):
    return (n & -n).bit_length() - 1


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    rng = random.Random(78)
    U = lambda b: (729*b + 223)//512
    for _ in range(2000):
        b = 905 + 8192*rng.randrange(0, 2**30)
        assert (27*b + 13) % 128 == 0
        t = (27*b + 13)//128
        assert t % 1728 == 191 and (27*t - 1) % 4 == 0
        c = (27*t - 1)//4
        x = 3*b
        for a in (1, 2, 1, 1, 1, 2):
            assert valuation(1, x) == a
            x = step(1, x)
        assert x == (81*t - 1)//2 and selected(x) and nu(x) == 3*c and c == U(b)
    returns = 0
    for _ in range(3000):
        b = 905 + 8192*rng.randrange(0, 2**40)
        if rng.random() < 0.5:   # bias toward deeper Y valuations
            k = rng.randrange(1, 6)
            mod = 2**(13 + 9*k)
            # solve 217 b + 223 = 0 mod 2^(13+9k) together with b = 905 mod 8192
            base = (-223*pow(217, -1, mod)) % mod
            if base % 8192 != 905:
                continue
            b = base + mod*rng.randrange(1, 2**8)
        Y = 217*b + 223
        assert 512*(217*U(b) + 223) == 729*Y if (729*b + 223) % 512 == 0 else True
        s, x = 0, b
        while x % 8192 == 905 and (729*x + 223) % 512 == 0 and U(x) % 8192 == 905:
            x, s = U(x), s + 1
        assert s == (v2(Y) - 13)//9, (b, s, v2(Y))
        returns += 1
    fam = 0
    for D in range(12, 17):
        for t in range(0, 6):
            q = 11547 + 2**17*3**D*t
            b, p, y = q//3, 11391 + 2**36*3**(D - 12)*t, (3*q + 1)//2
            assert q % 3 == 0 and b < p < q < y and all(nu(z) == z for z in (p, q, y))
            x, states = p, []
            for a in (1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2):
                assert valuation(1, x) == a
                x = step(1, x)
                states.append(x)
            assert x == 24*q + 13 == 16*y + 5 and all(z > q for z in states) and max(states) == 32*q + 17
            assert step(1, step(1, q)) == step(1, x) == (9*q + 5)//8 > q
            fam += 1
    V, anchor_free = {1}, None
    for q in range(3, 11548, 2):
        if nu(q) != q:
            continue
        if q == 11547:
            anchor_free = q not in V
            break
        x = q
        while x not in V:
            V.add(x)
            x = nu(step(1, x))
    assert anchor_free is True
    report = dict(scope="Independent checks of R78 prefix, R79 return count, R80 family and anchor (main 3b0c8a5).",
                  r78_inputs=2000, r79_return_cases=returns, r80_family_cases=fam, r80_anchor_no_smaller_ancestor=True,
                  status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
