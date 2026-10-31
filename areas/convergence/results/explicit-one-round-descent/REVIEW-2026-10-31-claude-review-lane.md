# Review of explicit-one-round-descent

## What I checked

- Read the node and [`explicit-valuation-large-deviations`](../explicit-valuation-large-deviations/README.md) (L1, L2, L2′ and the receipt), the shared checker `check_L2.py` and the side-lane probe `fable_L2_check.py`.
- Certificates: none are listed in this node. The evidence certificate `explicit-valuation-large-deviations/check_L2.py` (its checks 3–5 are this node's), re-run from a scratch copy of its folder: PASS, exit 0, 6.7 s, receipt byte-identical; `fable_L2_check.py`: PASS, exit 0, 3.7 s, receipt byte-identical.
- **(5), re-derived.** Induction: `S_d^(n+1)(N) = (3S_d^n(N) + d)/2^(a_(n+1))` gives `S_d^n(N) = (3^n N + dC_w)/2^A` with `C_w = Σ_(j<n) 3^(n−1−j) 2^(A_j)`. Every later letter is `≥ 1`, so `A − A_j ≥ n − j` and `C_w/2^A ≤ Σ_(j<n) 3^(n−1−j) 2^(−(n−j)) = (1/2) Σ_(i<n) (3/2)^i = (3/2)^n − 1`, with equality exactly for the all-ones word (`C_w = 3^n − 2^n`, `A = n`). Independent code: formula and bound on 20000 random odd `N < 2^64`, `n ≤ 40`, `d ∈ {1, 5, 7, 13, 61}`; equality at `N = 2^(n+1) − 1` for `n ≤ 29`.
- **(6).** `A > θn` gives `3^n/2^A < (3/2^θ)^n`, and `C_w/2^A < (3/2)^n`. Checked on 58730 random `(N, n, θ)` cases off the exceptional set, `d ∈ {1, 5, 13, 61}`, `θ ∈ {1.6, 1.7, 1.8, 1.9}`: no violation.
- **The exceptional set's count, recomputed three ways** at `X = 2^20`, `n ∈ {6, 8, 10}`, `θ ∈ {1.6, 1.7, 1.8}`, `d ∈ {1, 5}`: brute force over all odd `N ≤ X`; the exact cylinder formula `Σ_(A=n)^(⌊θn⌋) C(A−1, n−1)·X/2^(A+1)` (exact because `2^(⌊θn⌋+1) | X`); and the receipt. All three agree: 133120, 197632, 197632 (`n = 6`), 101632, 152320, 207232 (`n = 8`), 119144, 164904, 213524 (`n = 10`), identical for `d = 1` and `d = 5` because the word law does not depend on `d`. Each is below the bound (4), `(X/2)exp(−nI(θ)) + C(⌊θn⌋, n)` = 387243, 447131, 490617; 350437, 425045, 482611; 324310, 421244, 512804, and no descent violation occurs off the exceptional set. The exceptional fraction of the odd `N` is 0.19–0.41 against the Chernoff factor `exp(−nI)` of 0.60–0.94.
- **Trade-off numbers of the Remarks.** `θ = 1.6`: factor 0.9896, `κ_max = 0.655`, exponents 0.0477 and 0.990; `θ = 1.8`: 0.8615, 0.561, 0.0090, 0.879. The additive-term condition `(θ−1)κ < 1 + κ log₂(3/2^θ)` reads 0.393 < 0.990 and 0.448 < 0.879.
- **Controls.** On all eleven raw `3x+d` cycles of `cycle_fixtures.json` (`d = 5, 7, 13, 61`), at every cycle state with `n = m, 2m, 3m` and `θ ∈ {1.6, 1.7, 1.8, 1.9}` such that `A_n > θn` (201 cases), (6) holds. A cycle state has `S^m(N) = N`, so (6) needs `N(1 − (3/2^θ)^m) < d(3/2)^m`: the additive term `d(3/2)^n` is what accommodates the actual cycles, and none is excluded.
- The History's correction record: the word `(10, 1)` has `C_w = 3 + 2^10 = 1027 > 3^2`.

## What I did not check

- L2 and L2′ themselves (another node, status `written`); I used (4) as stated and verified only that the recomputed counts respect it.
- The asymptotic reading of the trade-off table (`κ_max` from `C(θn, n) ≈ 2^(θnH(1/θ))`) beyond recomputing its numbers.

## Findings

1. (imprecision, corrected) The claim said "any odd `d`". The `3x+d` step scales `0 < C_w/2^A ≤ (3/2)^n − 1` by `d`, which needs `d > 0`. For negative `d` the inequality (6) as written is false: `d = −1`, `N = 3`, `n = 3`, `θ = 1.6` has word `(3, 1, 1)`, `A = 5 > 4.8`, `S^3(3) = 1`, but `N(3/2^θ)^n + d(3/2)^n = −0.467`. (For `d < 0` the additive term is negative and (6) holds without it; the count (4) is unaffected.) Correction applied: "any positive odd `d`" in the claim, in the Statement paragraph "For `3x+d`" and in the Remark "d-control". This is the repository's reading of `3x+d` in any case.
2. (imprecision, Remark only) With `n = ⌊κ log₂ X⌋` one has `exp(−nI) ≥ X^(−κI/ln 2)`, so the quoted exceptional fraction "`≤ X^(−κI(θ)/ln 2) + 2C(⌊θn⌋, n)/X`" holds up to the factor `e^(I(θ)) ≤ 1.089` for `θ ≥ 1.5`, or exactly with `n ≥ κ log₂ X`. Not part of the claim.
3. (imprecision) At `X = 2^20` the boundary term `C(⌊θn⌋, n)` of (4) plays no role: the count is exactly `(X/2)·P(A_n ≤ θn)` because `X` is a multiple of every cylinder modulus. Check 4 of `check_L2.py` therefore exercises the Chernoff slack only; no finite check in either node exercises the boundary term. Correct as stated; a note on what the certificate shows.

## Verdict

HOLDS WITH CORRECTIONS

- "any odd `d`" → "any positive odd `d`" (claim; Statement, paragraph "For `3x+d`"; Remarks, "d-control"). Applied; the proof already uses `d > 0`.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
