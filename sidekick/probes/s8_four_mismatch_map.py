"""S8: does S7's size/sign/witness method reach s = 4? (Map: no.)

We build actual valuation words w of period m with exactly four mismatches under a rotation h, of the
'single huge letter + one 2-arc' shape (one h-chain with arcs [V][1^a][2^b][1^c], g = gcd(h, m) = 1),
and evaluate every inequality the S7 method uses, on the *maximal admissible profile*
    y_k = ell + sum_(i<k) (log2 3 - a_i + eps)      (the excess-tracked ceiling from the minimum),
i.e. the most favourable heights a hypothetical q = 1 cycle with this word could have:
  (1) end witnesses   1 + t log2 3 < y_z,  z = e or e + h by the sign of delta on the run,
  (2) start witnesses E + 1 < y_z',  z' = s or s + h by the same sign,
  (3) ones-run witnesses (comparison with the fixed point -1): a run of r ones ending at e needs
      1 + r log2 3 < y_e (n_e + 1 = 2 * 3^r * u),
  (4) the total A = ceil(m log2 3) and V >= 2.
Signs are read off the model profile (delta_i > 0 iff y_(i+h) > y_i). If every inequality holds
with margin, the S7 method cannot exclude s = 4: excluding these words needs arithmetic.
ell = log2 L is set to its worst case ell*(m) = 172 + 342 log2 m - log2 3 (above the S7 threshold, m = 1e6
and 4e6), and scanned over 71, 200, 1000, 3000 at m = 1e6 to see how the verdict depends on the L-bound.
"""
import json
import math
import sys
from pathlib import Path

LOG2_3 = math.log2(3)


def build_word(m, h, a, b):
    """Chain x + k h (x = m - 1): k = 0 -> V, 1..a -> 1, a+1..a+b -> 2, rest -> 1. Returns letters."""
    assert math.gcd(h, m) == 1
    x = m - 1
    word = [1] * m
    for k in range(a + 1, a + b + 1):
        word[(x + k * h) % m] = 2
    A = math.ceil(m * LOG2_3)
    V = A - (m - 1 - b) - 2 * b
    word[x] = V
    return word, V, A


def mismatches(w, h):
    m = len(w)
    return [i for i in range(m) if w[i] != w[(i + h) % m]]


def evaluate(w, h, ell, eps):
    m = len(w)
    y = [ell]
    for i in range(m - 1):
        y.append(y[-1] + LOG2_3 - w[i] + eps)
    # the minimum must be at index 0 and the word must close: y_m = ell + m log2 3 - A + m eps ~ ell
    M = mismatches(w, h)
    sgn = lambda i: y[(i + h) % m] > y[i]
    res = {"s": len(M), "min_at_0": min(y) == y[0], "end": [], "start": [], "ones": []}
    Ms = sorted(M)
    for k, e in enumerate(Ms):
        prev = Ms[k - 1]
        t = (e - prev - 1) % m
        start = (prev + 1) % m
        pos_run = sgn(e)                       # sign of delta on this run (constant in the model)
        z = (e + h) % m if pos_run else e
        res["end"].append(y[z] - (1 + t * LOG2_3))
        E = sum(w[(start + u) % m] for u in range(t))
        zs = (start + h) % m if pos_run else start
        res["start"].append(y[zs] - (E + 1))
    # ones-runs: maximal runs of 1s ending at a letter >= 2 at position e (the run ends at e)
    i = 0
    while i < m:
        if w[i] == 1:
            j = i
            while j < m and w[j] == 1:
                j += 1
            r = j - i
            e = j % m
            res["ones"].append(y[e] - (1 + r * LOG2_3))
            i = j
        else:
            i += 1
    res["min_end"] = min(res["end"])
    res["min_start"] = min(res["start"])
    res["min_ones"] = min(res["ones"]) if res["ones"] else None
    return res


def targeted(m, ell, eps, hf, p1win, p2win, bfs, span=60):
    """Place the two inner mismatches P1 = x + a h, P2 = x + (a+b) h in the windows where the continuous
    witness LP is feasible (p1 in (1-h, 1), p2 in (0, h); see the S8 note), with b ~ bf * m / ell 2s so
    that the ones-run constraint can hold near the minimum; h/m badly approximable so the 2s spread evenly."""
    h = int(hf * m)
    while math.gcd(h, m) != 1:
        h += 1
    hinv = pow(h, -1, m)
    x = m - 1
    best = None
    for bf in bfs:
        b0 = max(1, int(bf * m / ell))
        for b in range(b0, b0 + span):
            for k in range(7):
                P1 = int((p1win[0] + k * (p1win[1] - p1win[0]) / 6) * m)
                P2f = ((P1 + b * h) % m) / m
                if not (p2win[0] <= P2f <= p2win[1]):
                    continue
                a = ((P1 - x) * hinv) % m
                if a < 1 or a + b >= m - 1:
                    continue
                w, V, A = build_word(m, h, a, b)
                if V < 2 or len(mismatches(w, h)) != 4:
                    continue
                r = evaluate(w, h, ell, eps)
                if not r["min_at_0"]:
                    continue
                mg = min(r["min_end"], r["min_start"], r["min_ones"])
                if best is None or mg > best["margin"]:
                    best = {"m": m, "ell": round(ell, 1), "h": h, "h_over_m": round(h / m, 4), "a": a, "b": b,
                            "V": V, "P1": round(P1 / m, 3), "P2": round(P2f, 3), "margin": round(mg, 1),
                            "min_end": round(r["min_end"], 1), "min_start": round(r["min_start"], 1),
                            "min_ones": round(r["min_ones"], 1)}
                if best["margin"] > 50:
                    return best
    return best


def main():
    eps = math.log1p(1 / (3 * 2**71)) / math.log(2)
    hf = math.sqrt(2) - 1
    out = {"above_threshold": [], "ell_scan_m1e6": []}
    for m in (1_000_003, 4_000_037):
        ell = 172 + 342 * math.log2(m) - LOG2_3
        r = targeted(m, ell, eps, hf, (0.64, 0.92), (0.2, 0.243), (1.6, 2, 3))
        out["above_threshold"].append(r)
        print("ell = ell*:", r)
    m = 1_000_003
    for ell in (71.0, 200.0, 1000.0, 3000.0):
        r = targeted(m, ell, eps, hf, (0.64, 0.92), (0.2, 0.243), (1.6, 2, 3), span=15)
        out["ell_scan_m1e6"].append(r)
        print("ell =", ell, ":", r)
    ok = all(r is not None and r["margin"] > 0 for r in out["above_threshold"])
    out["s4_survives_all_size_constraints_at_ell_star"] = ok
    Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=1))
    print("four-mismatch words meet every size constraint at ell = ell*:", ok)
    return 0


if __name__ == "__main__":
    sys.exit(main())
