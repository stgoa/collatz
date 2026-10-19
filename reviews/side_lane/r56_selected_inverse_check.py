"""Sidekick probe: independent check of R56's two selected inverse words (main, selected_inverse/).

Domain: w = 205 mod 216 with 3w selected; q = (3w-1)/2, v = (16w-13)/27 (v = -7 mod 128), p = 3v.
For k in {4, 8}: b = 2kv+1, h = v3(kv+1), C = (kv+1)/3^h, r = 2^(h+1) C - 1. The ordinary word
from r to q is 1^h,2,1,1,4 (k = 4) or 1^h,2,3,2,2 (k = 8), and
    32 * 3^h * (r - q) = (k 2^(h+6) - 3^(h+4)) v + 2^(h+6) - 55 * 3^h,
so r < q iff h >= 3 (k = 4), iff h >= 5 (k = 8).
Checked with this branch's own step/selected on inputs built with prescribed h = 0..9 for each k
(CRT on v), plus 2000 random domain members. Standard library. Run without -O.
"""
from pathlib import Path
import json
import random
import sys

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / "collatz_research_20261017" / "negative_controls")]
from affine_controls import step, valuation  # noqa: E402
from fibre_count_check import selected  # noqa: E402


def v3(n):
    h = 0
    while n % 3 == 0:
        n //= 3
        h += 1
    return h


def check(w, k, tally):
    q, v = (3*w - 1)//2, (16*w - 13)//27
    assert (16*w - 13) % 27 == 0 and v % 128 == 121 and 32*q == 81*v + 23
    h = v3(k*v + 1)
    C = (k*v + 1)//3**h
    r = 2**(h + 1)*C - 1
    word = [1]*h + ([2, 1, 1, 4] if k == 4 else [2, 3, 2, 2])
    x = r
    for a in word:
        assert valuation(1, x) == a
        x = step(1, x)
    assert x == q
    lhs = 32*3**h*(r - q)
    rhs = (k*2**(h + 6) - 3**(h + 4))*v + 2**(h + 6) - 55*3**h
    assert lhs == rhs
    assert (r < q) == (h >= (3 if k == 4 else 5))
    tally[(k, min(h, 9), r < q)] = tally.get((k, min(h, 9), r < q), 0) + 1


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    rng = random.Random(56)
    tally = {}
    for k in (4, 8):
        for h in range(0, 10):
            made = 0
            while made < 40:
                m3 = 3**(h + 1)
                # v = -7 mod 128 and k v + 1 = 0 mod 3^h exactly
                t = rng.randrange(0, m3)
                v = (121 + 128*rng.randrange(1, 2**30))
                v -= v % m3
                v += t
                while v % 128 != 121:
                    v += m3
                if v3(k*v + 1) != h or v < 121:
                    continue
                w = (27*v + 13)//16
                if w % 216 != 205 or not selected(3*w):
                    continue
                check(w, k, tally)
                made += 1
    rand = 0
    while rand < 2000:
        w = 205 + 216*rng.randrange(0, 2**40)
        if selected(3*w):
            for k in (4, 8):
                check(w, k, tally)
            rand += 1
    report = dict(scope="Independent check of R56's two inverse words, identity (2) and thresholds (3).",
                  cases=sum(tally.values()), by_k_h_accept={"k%d h%d %s" % (k, h, "r<q" if a else "r>=q"): c
                                                            for (k, h, a), c in sorted(tally.items())},
                  status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(dict(cases=report["cases"], status="PASS")))


if __name__ == "__main__":
    main()
