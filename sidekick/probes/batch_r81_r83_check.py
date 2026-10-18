"""Sidekick probe: independent checks of R81's same-word merger cells and R83's parameters
(main 1d58f50), with this branch's own odd-only step (no main code).

R81 (cell theorem): if q0 follows ordinary word alpha (length a, total A) and p0 follows beta
(length b, total B) and S^a(q0) = S^b(p0), then the same-word mergers are exactly
q = q0 + M k, p = p0 + P k with M = 2^(A+1) 3^max(b-a,0), P = 2^(B+1) 3^max(a-b,0).
Checked: (i) R80's cell q = 11547 + 16*3^12 k, p = 11391 + 2^23 k with words (1,2) and
(1^6,2,2,1^4,2,6), k = 0..3000 and 300 random large k; (ii) 400 random small anchor pairs with
meeting words: every lift k = 0..40 keeps both words and the meeting; halving the 2-part or
dividing the 3-part of M (with the matching P) breaks some lift (minimality).
R83: for s = 1, 2 the unique 0 < L < 3^(6s+2) with 64^L = 217/8272 mod 3^(6s+4) is 740 and
2028089, and h = 11L + 8s gives 8148 and 22308995.
Standard library. Run without -O.
"""
from pathlib import Path
import json
import random
import sys

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / "collatz_research_20261017" / "negative_controls")]
from affine_controls import step, valuation  # noqa: E402


def follows(x, word):
    for v in word:
        if x <= 1 or valuation(1, x) != v:
            return None
        x = step(1, x)
    return x


def word_of(x, n):
    w = []
    for _ in range(n):
        w.append(valuation(1, x))
        x = step(1, x)
    return w


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    rng = random.Random(81)
    alpha, beta = (1, 2), (1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 6)
    ks = list(range(0, 3001)) + [rng.randrange(1, 2**60) for _ in range(300)]
    for k in ks:
        q, p = 11547 + 16*3**12*k, 11391 + 2**23*k
        assert q - p == 156 + 114448*k and p < q
        mq, mp = follows(q, alpha), follows(p, beta)
        assert mq is not None and mq == mp
    cells = 0
    while cells < 400:
        a, b = rng.randrange(1, 5), rng.randrange(1, 7)
        q0 = rng.randrange(3, 2**14) | 1
        alpha = word_of(q0, a)
        target, states = q0, []
        for _ in range(a):
            target = step(1, target)
            states.append(target)
        if min(states) <= 1:
            continue   # the anchor's prefix must avoid the absorbing state
        # find p0 != q0 reaching target in exactly b steps by a random inverse walk
        p0, ok = target, True
        for _ in range(b):
            cands = [((2**v)*p0 - 1)//3 for v in range(1, 9) if ((2**v)*p0 - 1) % 3 == 0 and ((2**v)*p0 - 1)//3 % 2 == 1]
            cands = [c for c in cands if c > 1]
            if not cands:
                ok = False
                break
            p0 = rng.choice(cands)
        if not ok or p0 == q0:
            continue
        beta = word_of(p0, b)
        A, B = sum(alpha), sum(beta)
        M = 2**(A + 1)*3**max(b - a, 0)
        P = 2**(B + 1)*3**max(a - b, 0)
        for k in range(0, 41):
            mq, mp = follows(q0 + M*k, alpha), follows(p0 + P*k, beta)
            assert mq is not None and mq == mp, (q0, p0, k)
        # minimality: a strictly smaller common period fails for some lift
        for M2, P2 in ((M//2, P//2),) + (((M//3, P//3),) if M % 3 == 0 and P % 3 == 0 else ()):
            broke = False
            for k in range(1, 41):
                mq, mp = follows(q0 + M2*k, alpha), follows(p0 + P2*k, beta)
                if mq is None or mq != mp:
                    broke = True
                    break
            assert broke
        cells += 1
    params = {}
    for s, (L_claim, h_claim) in ((1, (740, 8148)), (2, (2028089, 22308995))):
        mod = 3**(6*s + 4)
        target = 217*pow(8272, -1, mod) % mod
        sols = [L for L in range(1, 3**(6*s + 2)) if pow(64, L, mod) == target] if s == 1 else None
        if s == 1:
            assert sols == [L_claim]
        else:
            assert pow(64, L_claim, mod) == target and 0 < L_claim < 3**(6*s + 2)
            # uniqueness: 64 has order 3^(6s+2) modulo 3^(6s+4)
            assert pow(64, 3**(6*s + 2), mod) == 1 and pow(64, 3**(6*s + 1), mod) != 1
        assert 11*L_claim + 8*s == h_claim
        params[s] = dict(L=L_claim, h=h_claim)
    report = dict(scope="Independent checks of R81 merger cells and R83 (L, h) parameters (main 1d58f50).",
                  r80_cell_lifts=len(ks), random_cells=cells, r83_parameters=params, status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
