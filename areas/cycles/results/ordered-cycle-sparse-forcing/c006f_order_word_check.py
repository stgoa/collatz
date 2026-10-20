"""Independent check of Lean C006-f (claude/lean-lane e5e979a) and the separation question.

Ordered actual 3x+q cycles: the normalised word from the minimum is mech(A, m, 0) and gcd(A, m) = 1.
Unordered actual cycles (rank rotation or image order fails): how many still have a mechanical
normalised word (any phase / phase 0)? C005 section 4 says a mechanical c-word can coexist with
inversions, so the word statement does not characterise the ordered class.
"""
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from s1a_integer_cycle_check import cycles, step  # noqa: E402
from c006e_cc_check import heights, mech  # noqa: E402


def classify(cyc, q):
    i0 = cyc.index(min(cyc))
    n = cyc[i0:] + cyc[:i0]
    m = len(n)
    if m < 2:
        return None
    a = [step(x, q)[1] for x in n]
    A = sum(a)
    h = heights(n)
    B = max(h)
    c = [a[j] + h[(j + 1) % m] - h[j] for j in range(m)]
    Z = [2**(B - t) * x for t, x in zip(h, n)]
    order = sorted(range(m), key=lambda i: Z[i])
    rank = {i: r for r, i in enumerate(order)}
    s = (rank[1] - rank[0]) % m
    rot_ok = all((rank[(i + 1) % m] - rank[i]) % m == s for i in range(m))
    F = [3 * Z[i] + 2**(B - h[i]) * q for i in range(m)]
    img_ok = all(F[order[r + 1]] > F[order[r]] for r in range(m - 1))
    ordered = rot_ok and img_ok
    mech0 = c == mech(A, m, 0)
    mech_any = any(c == mech(A, m, l) for l in range(m)) or any(
        c[i:] + c[:i] == mech(A, m, 0) for i in range(m))
    return ordered, mech0, mech_any, math.gcd(A, m), (q, n[0], m, B)


def main():
    stats = {"ordered": 0, "ordered_mech0": 0, "unordered": 0, "unordered_mech0": 0,
             "unordered_mech_any_rotation_or_phase": 0}
    examples = []
    for q, N in [(5, 40001), (7, 40001), (13, 40001), (61, 40001), (11, 20001), (17, 20001),
                 (19, 20001), (23, 20001), (29, 20001), (233, 20001), (1201, 8001)]:
        for cyc in cycles(q, N):
            r = classify(cyc, q)
            if r is None:
                continue
            ordered, mech0, mech_any, g, info = r
            if ordered:
                stats["ordered"] += 1
                assert mech0 and g == 1
                stats["ordered_mech0"] += 1
            else:
                stats["unordered"] += 1
                stats["unordered_mech0"] += mech0
                stats["unordered_mech_any_rotation_or_phase"] += mech_any
                if mech0 and len(examples) < 5:
                    examples.append(info)
    out = {"probe": "c006f_order_word_check", "lean": "claude/lean-lane e5e979a", **stats,
           "unordered_with_mech0_examples_(q,min,m,B)": examples, "result": "PASS"}
    js = json.dumps(out, indent=1)
    print(js)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as f:
            f.write(js + "\n")


if __name__ == "__main__":
    main()
