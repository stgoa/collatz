"""Sidekick probe: exact section counts for main's V005 sparse control (experiments/viewpoints/V005/literature.md,
main 85a07c2): f = indicator of A = {6^e : e in E}, E = {2^j : j >= 0}. Main claims G_2(f;D) <= 5D+3 and
G_3(f;D) <= 3D+3 (cumulative counts of distinct entire sections n -> f(p^a n + r), 0 <= a <= D, 0 <= r < p^a), so f
has finite 2- and 3-dimension in the sense of Bell (2009, Definitions 4-5) while not being eventually periodic,
contradicting Conjecture 3.4 of that survey as printed.

Exact method (no prefix truncation). v_p(6^e) = e, so for depth a: the zero-offset section is the infinite set
{6^e/p^a : e in E, e >= a}; these are pairwise distinct for distinct a (their least elements differ in p- or
q-adic valuation). Every nonzero-offset section is empty or a singleton {floor(6^e/p^a)} with e < a, because distinct
e give distinct valuations and hence distinct nonzero residues mod p^a. So
G_p(f;D) = (D+1) + [D >= 1] + #{floor(6^e/p^a) : e in E, e < a <= D}, counted as distinct singletons
(the empty section is the zero sequence; singleton {0} is delta_0). Computed exactly with integers.
Standard library. Run without -O.
"""
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def G(p, D):
    E = [2**j for j in range(0, 12) if 2**j < max(D, 2)]
    singles = set()
    for a in range(1, D + 1):
        for e in E:
            if e < a:
                singles.add(6**e // p**a)
    return (D + 1) + (1 if D >= 1 else 0) + len(singles)


def main():
    rows, worst = [], {2: 0.0, 3: 0.0}
    for D in list(range(0, 41)) + [64, 100, 128, 200, 256, 400, 512, 1000]:
        g2, g3 = G(2, D), G(3, D)
        assert g2 <= 5*D + 3 and g3 <= 3*D + 3, (D, g2, g3)
        if D >= 1:
            worst[2] = max(worst[2], (g2 - 3) / D)
            worst[3] = max(worst[3], (g3 - 3) / D)
        rows.append([D, g2, g3])
    out = {"probe": "v005_sparse_growth_check", "main": "85a07c2", "rows_D_G2_G3": rows,
           "max_slope_(G-3)/D": {"base2": round(worst[2], 3), "base3": round(worst[3], 3)},
           "slope_at_D=1000": {"base2": round((G(2, 1000) - 3) / 1000, 3), "base3": round((G(3, 1000) - 3) / 1000, 3)},
           "result": "PASS"}
    (HERE / "v005_sparse_growth_check.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps({k: v for k, v in out.items() if k != "rows_D_G2_G3"}, indent=1))
    print("D, G2, G3 at D = 8, 16, 32, 64, 128, 256, 512, 1000:",
          [r for r in rows if r[0] in (8, 16, 32, 64, 128, 256, 512, 1000)])


if __name__ == "__main__":
    main()
