# Review of annular-root-collapse-contraction

## What I checked

- Read the node, the band table of [`disjoint-annular-recursion`](../disjoint-annular-recursion/README.md), the three evidence scripts and the control node [`progress-measures-control-3x-61`](../progress-measures-control-3x-61.md).
- Certificates: none are listed in this node. The evidence scripts were re-run from scratch copies of their folders: `exposure-potential-boundary-flux/check_duality.py` PASS, exit 0, 0.7 s (its `independent_collapse_check` at `N = 8, 16, 24, 96, 112, 128, 144, 168, 512`); `locally-collatz-like-control-barrier/progress_measures_audit.py` PASS, exit 0, 2.6 s, receipt byte-identical (68 cutoffs `N ≤ 4096`, `c_80000 = 0`, the `3x+61` ratios 0.863, 0.8553, 0.8489, 0.853); the legacy `check_arithmetic_reductions.py` replayed through `tools/legacy_replay.py` PASS, 9 s, every file unchanged.
- **Algebra, re-derived.** `3(4x+1) + 1 = 4(3x+1)`, so `S(F(x)) = S(x)`; `x ≡ 5 (mod 8)` iff `x = 4z + 1` with `z` odd, so roots have first valuation 1 (`x ≡ 3 mod 4`) or 2 (`x ≡ 1 mod 8`); `PRμ = Pμ` because every chain point has the root's successor and the chain of 1 is killed by `P` in any case; hence `(I − P)(μ − Rμ) = μ − Rμ`. Norm identity: a state `y > 1` with `3 ∤ y` has exactly one root among its predecessors, `(2y−1)/3` if `y ≡ 2 (mod 3)` and `(4y−1)/3` if `y ≡ 1 (mod 3)`, odd in both cases; the only root whose successor is 1 is 1 itself, which `R` discards. So `r ↦ S(r)` is a bijection from roots `≠ 1` onto `{y > 1 : 3 ∤ y}` with `(Rμ)(r) = (Pμ)(S(r))`, and the two norms agree.
- **Entry profiles, re-derived.** For `x` in band `j`, `F(x) = 4x + 1` is odd and `2^(j+3)Q` is even, so `F(x)` is in band `j + 2`; entries in bands 0, 1 are all odd states there (the `F`-preimage is below `Q`), entries in bands 2–5 are the states `≢ 5 (mod 8)` (the preimage `(x−1)/4` would lie strictly inside band `j − 2`). I recomputed `g_j(r) = Σ_k f_(j+2k)(F^k r mod 18)`: all 54 table entries agree. Absolute sums 14, 14 per period 18, and 36, 36, 24, 12 per period 72 (each odd residue mod 18 has exactly three of its four lifts mod 72 not `≡ 5 (mod 8)`, so bands 2–5 give three times the row sums 12, 12, 8, 4). Band `j` holds `2^j·N/8` full periods (its boundaries `2^j·9N/4` are multiples of 18, and of 72 for `j ≥ 2`, because `8 | N`), giving `N·(7/4, 7/2, 9/2, 9, 12, 12)`, total `171N/4`; `171/198 = 19/22`. The chain of 1 has exactly three annular points (entry `e < 4Q`, then `4e + 1`, `16e + 5 < 64Q`, `64e + 21 > 64Q`), so `|c_N| ≤ 3` from rows 0–1.
- **Independent code** at the 131 cutoffs `8 | N ≤ 1024` and `2048, 4096, 6144`: `PRA_N = PA_N`, the identity, `‖RA_N‖₁ = ‖PA_N‖₁ = 171N/4 − |c_N|`, `|c_N| ≤ 3`, `22‖RA_N‖₁ ≤ 19‖A_N‖₁`, `R(RA_N) = RA_N`, and `(RA_N)(p) = 2` at exactly the `2N` states `p ≡ 35 (mod 36)` in `(32Q, 64Q)`, each its own root with `F(p) > 64Q`. `c_80000 = 0`: the chain points 349525, 1398101, 5592405 carry coefficients 1, −1, 0.
- **Survivors, re-derived.** `p ≡ 35 (mod 36)` gives `p ≡ 17 (mod 18)` (row-5 value 2) and `p ≡ 3 (mod 4)` (a root); `(32Q, 64Q) = (72N, 144N)` has both endpoints `≡ 0 (mod 36)`, so it holds exactly `2N` such states.
- **Remarks' numbers.** `‖P^k A_96‖₁ = 4752, 4103, 3533, 3124` for `k = 0, …, 3` reproduced; the `3x+61` one-pass ratios 0.849–0.863 reproduced by the PR1 audit.
- **Controls (`d`-uniformity).** With `F_d(x) = 4x + d` and absorbing set `{1, d}`, `P_d R_d = P_d` and `‖R_d μ‖₁ = ‖P_d μ‖₁` held on 200 random finite measures for each of `d = 5` and `d = 13`. The algebraic half is `d`-uniform and carries no information about `3x+1`; the constant `19/22` is the band arithmetic of `A_N`, and the node's own remark that `3x+61` gives 0.849–0.863 is the right caution.
- Informational: scanning `c_N` by the chain alone over `8 | N ≤ 200000`, the correction vanishes first at `N = 9712, 9720, …` (10923 of the 25000 cutoffs), so `N = 80000` is one of many; at none of the 131 cutoffs tested with the full annulus is `c_N = 0` (values `−3, −2, −1, 1, 2, 3` occur 21, 43, 11, 2, 53, 1 times).

## What I did not check

- The statements quoted from [`root-transport-normal-form`](../root-transport-normal-form/README.md) in the Remarks (beyond `R² = R`, which is immediate).
- `c_N` at cutoffs beyond 6144 with the full annulus (the chain evaluation covers them).

## Findings

1. (imprecision) The Statement names the chain root `ρ(x)`; `ρ` is the rotation distance in `conventions/NOTATION.md` and the rank `ν(3w)` elsewhere in this area. Notation only.
2. (gap, supplied) "Different roots have different successors ... hence `‖Rμ‖₁ = ‖Pμ‖₁`" also needs that multiples of 3 have no predecessor, that every `y > 1` with `3 ∤ y` has a root among its predecessors, and that 1 is the only root whose successor is 1, so that discarding it matches `P` killing at 1. All three hold (above).
3. (imprecision) "positive mass at least `4N`" is far from sharp. Since `Σ RA_N = −c_N`, the residual's positive mass is `(171N/4 − |c_N| − c_N)/2 ≈ 171N/8` (131328 at `N = 6144`, i.e. `21.4N`), about 86% of the original positive mass `99N/4`: the pass removes only `27N/8 + O(1)` of positive mass. This strengthens "cannot be iterated".
4. (imprecision) The ratio `19/22` is attained only when `c_N = 0`, which does not happen at any cutoff `≤ 6144` tested; the claim's `≤` and "the correction can vanish" are both correct as written.

## Verdict

HOLDS

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
