"""Sidekick probe: independent checks of main's R33, R34 and R36 (commit 1603bf3).

R33: the mixed shrinking recognizer is rebuilt from its stated rules, with this lane's own
     normal form nu. Its acceptance fraction among w = 3 (mod 8) in [2^(k-1), 2^k) is
     compared with the stated exact cylinder measure 32/157.
R34: checks eta(q) = 2^h(q+1)/3^h - 1 (h = v3(q+1)) with S^h(eta(q)) = q;
     the cylinder x = 19199 (mod 65536) with q = (6561x+3745)/8192, p = (2187x-117)/4096
     and S^9(x) = S^2(p); and the N = 65536 example root 84735.
R36: Mersenne mergers S^t(2^a-1) = S^t(2^(a-1)-1) at a = 1699 (t = a+4) and a = 659
     (t = a+5).
Standard library. Run without -O.
"""
from fractions import Fraction
from pathlib import Path
import json
import random
import sys

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / "experiments" / "packet_currents" / "negative_controls")]
from affine_controls import step  # noqa: E402
from fibre_count_check import nu  # noqa: E402


def v2(n):
    return (n & -n).bit_length() - 1


def v3(n):
    k = 0
    while n % 3 == 0:
        n, k = n//3, k + 1
    return k


def iterate(x, k):
    for _ in range(k):
        x = step(1, x)
    return x


def accepted(w):
    while True:
        assert w % 8 == 3 and w > 0
        h = v2(3*w - 1)
        if h % 2:
            k = (h - 3)//2
            z = 3**k*((3*w - 1) >> h)
            if z % 8 != 3:
                return False
            child = z
        else:
            k = h//2 - 1
            z = 3**k*((3*w - 1) >> h)
            if nu(z) == z:
                return True
            if z % 64 == 29:
                child = (3*z + 1)//8
            elif z % 128 == 101:
                child = (3*z + 1)//16
            else:
                return False
        assert 0 < 2*child < w and child % 8 == 3
        w = child


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    target = float(Fraction(32, 157))
    fractions = {}
    for k in (16, 20, 22):
        ws = range((1 << (k - 1)) + 3, 1 << k, 8)
        fractions[k] = sum(map(accepted, ws))/len(ws)
    rng = random.Random(33)
    big = [rng.randrange(2**99, 2**100)//8*8 + 3 for _ in range(200000)]
    fractions[100] = sum(map(accepted, big))/len(big)
    # R34
    for q in range(3, 20000, 2):
        h = v3(q + 1)
        eta = (2**h*(q + 1))//3**h - 1
        assert 2**h*(q + 1) % 3**h == 0 and iterate(eta, h) == q
    for x in (19199, 19199 + 65536, 19199 + 7*65536):
        q, p = (6561*x + 3745)//8192, (2187*x - 117)//4096
        assert (6561*x + 3745) % 8192 == 0 and (2187*x - 117) % 4096 == 0
        assert iterate(x, 9) == iterate(p, 2)
    x = 84735
    assert x % 65536 == 19199 and (6561*x + 3745)//8192 == 67865 and (2187*x - 117)//4096 == 45243
    # R36
    for a, t in ((1699, 1699 + 4), (659, 659 + 5)):
        assert iterate(2**a - 1, t) == iterate(2**(a - 1) - 1, t), a
    report = dict(scope="Independent checks of main's R33/R34/R36 (commit 1603bf3); finite data.",
                  r33_acceptance_fraction=fractions, r33_stated=target,
                  r34="eta chains for odd q < 20000; cylinder 19199 mod 65536; root 84735",
                  r36="Mersenne mergers at a = 1699 (t = a+4) and a = 659 (t = a+5)", status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
