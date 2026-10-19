"""Sidekick probe: independent checks of R75's E_return translation arithmetic and R77's
same-seed complexity bounds (main e9effe1), with this branch's own step/selected (no main code).

R75: for u in E_return (u = 5 mod 8, u = 3 mod 9, 3u selected): q = (3u-1)/2, n = (4u-3)/3 = sigma(u),
     b = n/3 is in W9 (b = 9 mod 16), and the ordinary path n -> q has valuations (1, 2), with
     rho(b) = 3b = n < q.
R77: K = 311195/7153, Lambda = 3^24/2^37. V(w) + K = (3^12/2^19)(w + K) and R(w) + K <= Lambda(w + K)
     for w > 0, so w_j + K <= Lambda^j (w_0 + K). Spacing: a length-L factor repeated at i < j forces
     w_j = w_i mod 2^(26 + e) with e >= 19L (checked on random legal trajectories built from R74's
     domains). Threshold floor(2^1305/3^768 - K) = 260028359941009900571662033 (exact). Fixed-word
     copy count floor((v2((a - 2^e)w + c) - 26)/e) checked against direct iteration for V, R, VR, RV, VVR.
Standard library. Run without -O.
"""
from fractions import Fraction
from pathlib import Path
import json
import random
import sys

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / "collatz_research_20261017" / "negative_controls")]
from affine_controls import step, valuation  # noqa: E402
from fibre_count_check import selected  # noqa: E402

VC, RC = (3**12, 311195, 19), (3**24, 328537586155, 37)
G = 40529845
DOM = {"V": (2218391138229, 45), "R": (8515171531530858421, 63)}


def v2(n):
    return (n & -n).bit_length() - 1


def compose(word):
    A, C, E = 1, 0, 0
    for sym in word:
        a, c, e = VC if sym == "V" else RC
        A, C, E = a*A, a*C + c*2**E, E + e
    return A, C, E


def legal(x, sym):
    r, m = DOM[sym]
    return x % 2**m == r


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    rng = random.Random(77)
    e_ret = 0
    while e_ret < 3000:
        u = rng.randrange(1, 2**40)*72 + rng.choice([21, 45])  # u = 5 mod 8 and 3 mod 9 candidates
        if u % 8 != 5 or u % 9 != 3 or not selected(3*u):
            continue
        q, n = (3*u - 1)//2, (4*u - 3)//3
        assert (4*u - 3) % 3 == 0 and n % 3 == 0
        b = n//3
        assert b % 16 == 9 and valuation(1, n) == 1 and valuation(1, step(1, n)) == 2
        assert step(1, step(1, n)) == q and 3*b == n < q
        e_ret += 1
    K = Fraction(311195, 7153)
    Lam = Fraction(3**24, 2**37)
    assert 3**12 - 2**19 == 7153
    for w in (1, 10**6, 10**30):
        Vw = Fraction(3**12*w + 311195, 2**19)
        Rw = Fraction(3**24*w + 328537586155, 2**37)
        assert Vw + K == Fraction(3**12, 2**19)*(w + K) and Rw + K <= Lam*(w + K)
    thr = (2**1305 - 3**768*K)/3**768
    assert thr.numerator//thr.denominator == 260028359941009900571662033
    spacing_pairs = 0
    for _ in range(150):
        word = [rng.choice("VR") for _ in range(rng.randrange(6, 14))]
        A, C, E = compose(word)
        mod = 2**(26 + E)
        w0 = ((2**E*G - C)*pow(A, -1, mod)) % mod
        traj, x = [w0], w0
        for sym in word:
            assert legal(x, sym)
            a, c, e = VC if sym == "V" else RC
            x = (a*x + c) >> e
            traj.append(x)
        for L in (1, 2, 3):
            seen = {}
            for i in range(len(word) - L + 1):
                f = tuple(word[i:i + L])
                if f in seen:
                    j0 = seen[f]
                    e = compose(f)[2]
                    assert (traj[i] - traj[j0]) % 2**(26 + e) == 0 and e >= 19*L
                    assert traj[i] + K <= Lam**i*(traj[0] + K)
                    spacing_pairs += 1
                else:
                    seen[f] = i
    copies = 0
    for word in (["V"], ["R"], ["V", "R"], ["R", "V"], ["V", "V", "R"]):
        a, c, e = compose(word)
        for t in range(40):
            k = rng.randrange(0, 4)
            A, C, E = compose(word*(k + 1))
            mod = 2**(26 + E)
            w = ((2**E*G - C)*pow(A, -1, mod)) % mod + mod*rng.randrange(1, 2**6)
            predicted = (v2((a - 2**e)*w + c) - 26)//e
            x, n_copies = w, 0
            while True:
                y, ok = x, True
                for sym in word:
                    if not legal(y, sym):
                        ok = False
                        break
                    aa, cc, ee = VC if sym == "V" else RC
                    y = (aa*y + cc) >> ee
                if not ok or y % 2**26 != G:
                    break
                x, n_copies = y, n_copies + 1
            assert n_copies == predicted, (word, k, n_copies, predicted)
            copies += 1
    report = dict(scope="Independent checks of R75 E_return arithmetic and R77 complexity bounds (main e9effe1).",
                  r75_e_return_inputs=e_ret, r77_spacing_repeats=spacing_pairs, r77_copy_count_cases=copies,
                  r77_threshold="260028359941009900571662033", status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
