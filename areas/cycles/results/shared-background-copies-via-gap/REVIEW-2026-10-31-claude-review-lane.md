# Review of shared-background-copies-via-gap

## What I checked

- Certificate: `python3 tools/run_certificates.py --node shared-background-copies-via-gap` from the repository root: PASS, exit 0, 0.4 s wall (the tool prints 0 s). The script rewrites `s11_c013_gap.json`; the working tree was unchanged afterwards, so the receipt was reproduced byte-identically.
- Where `η` enters C013 ([`shared-background-denominator-law`](../shared-background-denominator-law/README.md), `OVERLAP_CONTROLS.md` §§3–4). Re-derived (3) + (6) + (8) ⇒ (9) ⇒ (10) (using `θ ≥ 2`, `u ≥ 2^n`, `α < θu`, `e ≥ 2`), and (10) ⇒ (12) ⇒ (13): at `q = 1`, (10) reads `n(e − 1) < d + 2Te + e(d + 1)·log₂r + log₂(1/η)`; dividing by `e − 1 ≥ 1` with `e/(e − 1) ≤ 2`, `1/(e − 1) ≤ 1` and `d ≤ r − 2` gives `n < r + 4T + 2(r − 1)·log₂r + log₂(1/η)`. The bound `η` appears only as `log₂(1/η)`, so substituting EXT-1 (`η ≥ 2^(−172)·m^(−341)`) is exactly (13′). Numerically, `RHS(12)/(e − 1) ≤ RHS(13)` on 1,843,160 grid cases (`r ≤ 60`, `2 ≤ e ≤ r`, `r ≤ T ≤ 300`, four values of the last term), minimum slack 2. EXT-1's hypotheses (`0 < m`, `3^m < 2^A`) hold for any displayed word with `D > 0`, a repetition of the primitive cycle included, so C013's extra hypothesis `A < 2m` (needed only for Matveev) is not needed.
- The relaxation `T ≤ H·r ⇒ m/r − 1 < r(1 + 4H) + 2(r − 1)·log₂r + 172 + 341·log₂m`: the admissible set is an up-set in `r` (checked for `r < 2,000`), and the threshold is nondecreasing in `m`, so the figures at `m = 1.375·10^11` bound every larger period.
- The table, recomputed exactly by bisection (my script). `λ_gap = 172 + 341·log₂m = 8,101.44 / 12,789.22 / 17,163.66`; `λ_Matveev = (6·10^8/ln 2)·(1 + ln 2m) = 1.542·10^10 / 2.367·10^10 / 3.136·10^10`, matching C011's (1) and C013's (13). Exact smallest admissible `r` for `H = 1, 2, 4, 8`: `m = 10^7`: 507, 479, 434, 374 (equal to the receipt), Matveev 2. `m = 1.375·10^11`: 60,961 / 58,005 / 53,171 / 46,254 (receipt 60,985 / 58,036 / 53,192 / 46,267, 0.03–0.05 % high), Matveev 6 (equal). `m = 10^15`: 4,507,809 / 4,339,542 / 4,052,050 / 3,613,740 (receipt 0.01–0.1 % high); Matveev 31,884 / 31,884 / 31,884 / 31,883 (receipt 31,897).
- Use of the sources against their records. EXT-1 is used exactly as [`musson-collatz-gap-all`](../../../../sources/musson-collatz-gap-all.md) records it (`k ↦ m`, `L ↦ A`, `2^A ≤ 2^172·m^341·(2^A − 3^m)`), only to bound `η`. The period bound is used exactly as [`hercher-2023-cycle-length`](../../../../sources/hercher-2023-cycle-length.md) records it (`m > 1.375·10^11`, with [`barina-2025-convergence-2-71`](../../../../sources/barina-2025-convergence-2-71.md)), only to choose the row of the table.
- Controls (my script, odd seeds `≤ 20,000`; cycle counts 6, 2, 10, 3 for `3x+5, 7, 13, 61`, equal to the corpus). Every rotation, every representation `(U, a_0, …, U, a_(r−1))` with `r ≥ 2` and nonconstant markers: 133 representations, all with empty `U` (the periods 2, 3, 5, 15, 17, 41 carry no nonempty shared background). The general-`q` form of (12) and (13), with `+ log₂q` and the exact `η`, holds with at least 24 bits of slack. Over the whole corpus ([`actual-cycles-3x-d-corpus`](../actual-cycles-3x-d-corpus/README.md), 333 parameters): 387 representations with nonempty `U` and nonconstant markers (4 with a nontrivial polynomial gcd), the general-`q` (12) and (13) hold in all, minimum slack 22 bits; EXT-1 holds on every control `(A, m)`. No actual cycle is excluded: the claim is `q = 1` only, and at general `q` the same chain carries `+ log₂q`.

## What I did not check

- C013's algebra beyond (3) + (6) + (8) ⇒ (13): the exact factor extraction (2), the resultant bound (7) and the Fourier part are the reviewed node's; I took (7) as given, as the node itself does.
- EXT-1's proof (replayed elsewhere), and Hercher's and Barina's computations.
- The "Pattern" remark (C006 and the C002 non-import).

## Findings

1. Statement table and receipt: values above 1,000 are the stepped search's first admissible point (0.1 % steps) and overstate the exact smallest admissible `r` by up to 0.1 % (exact values above). The rounded text "about 61,000 … about 46,000", "`r ≥ 6`" and "`r ≥ 2`" are right; the Matveev entry "31,897" at `m = 10^15` is exactly 31,884 (`H ≤ 4`) or 31,883 (`H = 8`). The node discloses the step. Severity: imprecision.
2. Notation: `H` is the marker-average bound here but the cycle maximum in [`conventions/NOTATION.md`](../../../../conventions/NOTATION.md) §2; the node defines its use, but another letter would avoid the clash. Severity: imprecision.
3. Claim: "nontrivial" and C013's `A < 2m` are not needed for (13′), which only needs `D > 0` and nonconstant markers; harmless. Severity: imprecision.

## Verdict

HOLDS. Certificate passed. No correction applied.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
