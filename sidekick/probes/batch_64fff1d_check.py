"""Sidekick probe: independent checks of concrete identities in main commit 64fff1d.

R30 (second_return/SHRINKING_PAIRS.md):
  - for w = 3 (mod 8) with h = v2(3w-1) = 2k+2 even and z = 3^k(3w-1)/2^h:
    S^k(3w) = 4z+1 and S^(k+1)(w) = 2z+1;
  - z = 101 (mod 128) gives w' = (3z+1)/16 = 3 (mod 8) and 0 < w' < w/4;
  - Mersenne mergers S^(a+3r+3)(2^a-1) = S^(a+3r+3)(2^(a-1)-1) for the stated
    classes a = 199 (mod 256) (r = 1) and a = 2887 (mod 65536) (r = 2), and the
    a = 39 example with merger time a + 8.
R31 (bounded_run_cycles/BOUNDED_RUN_GROWTH.md):
  - 4513*27 + 9221 = 2^17 and 4513*Psi(x) + 9221 = (6561/2048)(4513x + 9221),
    with Psi(x) = (6561x + 9221)/2048;
  - x = -9221/4513 (mod 2^(11r+6)) forces r complete words (1,2,1,1,1,1,2,2),
    checked by direct Syracuse steps for r <= 6.
R32 (merger_scope/MERGER_SCOPE.md):
  - for a = 1 (mod 18), a >= 19, N = 12*2^(a-5), z = 2^a-1, p = (4z-1)/3, q = 4p+1:
    A_N(p) = +1, A_N(q) = -1 and S(p) = S(q) = z, by this lane's point evaluator.
Standard library. Run without -O.
"""
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / "collatz_research_20261017" / "negative_controls")]
from affine_controls import step, valuation  # noqa: E402
from progress_measures_audit import point_value  # noqa: E402


def iterate(x, k):
    for _ in range(k):
        x = step(1, x)
    return x


def v2(n):
    return (n & -n).bit_length() - 1


def r30():
    pairs = 0
    for w in range(3, 2**18, 8):
        h = v2(3*w - 1)
        if h % 2 or h < 4:
            continue
        k = (h - 2)//2
        z = 3**k*(3*w - 1) >> h
        assert iterate(3*w, k) == 4*z + 1 and iterate(w, k + 1) == 2*z + 1, w
        if z % 128 == 101:
            w2 = (3*z + 1)//16
            assert (3*z + 1) % 16 == 0 and w2 % 8 == 3 and 0 < 4*w2 < w, w
        pairs += 1
    mersenne = []
    for a, r in ((199, 1), (455, 1), (2887, 2)):
        x, q = 2**a - 1, 2**(a - 1) - 1
        t = a + 3*r + 3
        assert iterate(x, t) == iterate(q, t), a
        mersenne.append(dict(a=a, r=r, merge_steps=t))
    assert iterate(2**39 - 1, 47) == iterate(2**38 - 1, 47)
    mersenne.append(dict(a=39, merge_steps=47))
    return pairs, mersenne


def r31():
    assert 4513*27 + 9221 == 2**17
    for x in (27, 12345, 2**40 + 7):
        assert 4513*(6561*x + 9221) + 9221*2048 == 6561*(4513*x + 9221)
    word = [1, 2, 1, 1, 1, 1, 2, 2]
    for r in range(1, 7):
        mod = 2**(11*r + 6)
        x = (-9221*pow(4513, -1, mod)) % mod
        y = x
        for _ in range(r):
            for a in word:
                assert valuation(1, y) == a, (r, y)
                y = step(1, y)
    return 6


def r32():
    rows = []
    for a in (19, 37, 55):
        N = 12*2**(a - 5)
        z = 2**a - 1
        p = (4*z - 1)//3
        q = 4*p + 1
        A = lambda y: point_value(1, 64*N, y) - point_value(1, N, y)
        assert A(p) == 1 and A(q) == -1 and step(1, p) == z == step(1, q), a
        rows.append(dict(a=a, N=N))
    return rows


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    pairs, mersenne = r30()
    report = dict(scope="Independent finite checks of concrete identities in main commit 64fff1d.",
                  r30_pairs_checked=pairs, r30_mersenne=mersenne, r31_repeated_words_r_max=r31(),
                  r32_cancellation=r32(), status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
