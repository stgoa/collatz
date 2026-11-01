# Review of growth-norm-transport-barrier

## What I checked

- Read the node, [`fixed-factor-stopping-explicit-constants`](../fixed-factor-stopping-explicit-constants/README.md) (S.1, the parity lemma and the bound `(8/7)(16807/18432)^m`) and [`arbitrary-target-linear-transport-barrier`](../arbitrary-target-linear-transport-barrier/README.md), and both main-lane checkers.
- **Theorem 1, line by line.** An arrow `n → y > 1` half-descends iff `(2^a − 6)y ≥ 1` iff `a ≥ 3`; integrality forces `y ≡ 5 (mod 6)` for odd `a` and `y ≡ 1 (mod 6)` for even `a`; `n ≤ X` iff `y ≤ Z/2^a`, `Z = 3X + 1`; pairing `a = 2b + 1, 2b + 2` gives (2), and `Σ_(b≥1) (Z/(2·4^b))^α = Z^α 8^(−α)/(1 − 4^(−α))`. Smallest sources `13 → 5` (`a = 3`) and `37 → 7` (`a = 4`), so `Z/X ≤ 40/13` for `X ≥ 13`. Constants: `(3/8)^(4/5) = 0.4563 < 1/2` (`3^4 < 2^7`), `4^(−4/5) = 0.3299 < 1/3` (`3^5 < 4^4`), `K_1(4/5) = 0.6809 < 3/4`, `(3/4)(40/39) = 10/13`. Independent brute force: identity (2) exact for a random 40-element set and every `X ≤ 6000`; for 30 random finite target sets and `α ∈ {0.8, 0.9, 0.99}`, the largest observed `sup_(X ≤ 40000) Q(A)(X)/X^α` divided by the exact `||A||_α` was 0.4656 (theorem: `< 10/13 = 0.7692`).
- **Theorem 2, line by line.** `y ≡ 5d (mod 18)` makes `8y − d ≡ 0 (mod 3)`, `32y − d ≡ 0 (mod 3)`, `32y − 7d ≡ 0 (mod 9)`, `64y − 5d ≡ 0 (mod 9)`; `3n_23 + d = 4n_3` and `3n_15 + d = 2n_5` give the exact words; the six inequalities (7); the counts (8); `N_d(X)/(||A|| X^α) → K(α)`; the integer inequalities (9) (`3^7·5^8 = 854296875 > 2^29 = 536870912`, `2187 > 2048`, `4782969 > 3125000`, `3^22 > 2^34`) and `2/5 + 1/8 + 5/16 + 1/6 = 241/240`. Independent code: for `d ∈ {1, 5, 7, 13, 61}` and every `y ≡ 5d (mod 18)` with `5d < y < 60000` (3316 to 3333 targets per `d`), the four sources are odd, distinct, exceed 1, follow exactly `(3), (5), (2,3), (1,5)` and first half-descend to `y` at times 1, 1, 2, 2. The count (5) is exact for every `X ≤ 30000` at `α ∈ {1/2, 4/5, 7/8}`, `d ∈ {1, 5}`, with `A(X)/X^α ≤ 18^(−α)` at every jump and tending to it. `K(7/8) = 1.05922`; `K(α) = 1` at `α ≈ 0.91619`; `K(1) = 57/64`.
- **Theorem 3, line by line.** Prefix-freeness of first-crossing words and disjointness of their cylinders (weight `2^(−A_l)` with the extra bit); the feed from S.1: "more than `3m` ones in the first `5m` positions" is `Bin(5m − 1, 1/2) ≥ 3m`, the complete word before the first 1 at position `j ≥ t` has `r ≤ 3m` letters and total `j`, slope `≤ (27/32)^m < 1/4` since `4·27^9 < 32^9`; the intercept recursion `b_(w,a) = 3b_w + 2^(A_l)`; the congruence (14) by unwinding one arrow (`2^a y ≡ d (mod 3)` and the previous word's condition); `3^(K−l)` compatible odd residues modulo `2·3^K`; the identity `3^(−l) s_l^α = 2^(−A_l) s_l^(α−1)` and the strict inequality from `s_l < 1/2`; `y < n/2` iff `n > d b_w/(2^(A_l−1) − 3^l)`; earlier states `> n/2 > 1`; (16) and the limit `W(c) > 1`. Independent DP for the code mass: `p_48 = 0.9798150915`, `p_80 = 0.9962448385`, `p_90 = 0.9977166792`, `p_120 = 0.9994477`; `2^(1−19/20) p_48 > 1` and `2^(1−99/100) p_80 > 1` hold in exact integers; at `B = 90` the exact binomial tail is below `(8/7)(16807/18432)^m` and `1 − δ_m − 2^(−L) ≤ p_90` for `m = 9..15`, `L = 91 − 5m`. Independent inverse-word check: all 118 first-crossing words with total `≤ 10`, `d ∈ {1, 5, 7, 13, 61}`: `n_w(y)` is an odd integer that follows exactly `w` and first half-descends at step `l` whenever `y > 1` satisfies (14) and the thresholds (590 cases).
- **Certificates.** `python3 tools/run_certificates.py --node growth-norm-transport-barrier`: `check_growth_norm.py` PASS (0 s), `check_all_exponents.py` PASS (0 s), `p6_003_growth_norm_check.py` PASS (1 s); exit 0; wall 1.2 s (second run 1.5 s). Both main-lane checkers compare exact receipts, fail closed on unknown flags and use no bare `assert`.
- **Controls.** Theorems 2 and 3 are stated for every `d` coprime to 6 and my checks include `d = 5, 7, 13, 61`; the targets are arbitrary sets, so the actual `3x+d` cycles are not in tension with any claim. Theorem 1 is claimed for `d = 1` only, as the Remarks say.

## What I did not check

- The literature matches (Borovkov–Pfeifer, Tao) beyond their contextual role.
- The side-lane probe's internals beyond its passing run.
- Finiteness of `||G_d(A)||_α` for the constructed sets (left open by the node).

## Findings

1. Theorem 2 is stated for `0 < α ≤ 7/8`; the four-word witness in fact expands for every `α` below `α_0 ≈ 0.91619` where `K(α_0) = 1`, and `K(0.95) = 0.954 < 1`, so Theorem 3 is needed only above `α_0`. The stated range is a safe sub-range, not the exact one. Imprecision.
2. §4, "Restore the affine intercept": the two lower bounds on the representative `c` give `n_w(y) > 2` and `y < n/2`; the exclusion of the target 1 is only added afterwards ("by further increasing `c` take `y > 1`"). It is needed: with `y = 1` the formulas give valid first-half paths into the excluded state (for `d = 1`, `w = (4)`: `n = 5 → 1`). My own check tripped on exactly this before I added `y > 1`. Imprecision in the order of the argument, not a gap.
3. Theorem 1's proof uses `A_5 + A_1 ≤ A`; elements of `A` divisible by 3 have no sources at all, so the inequality is loose but correct. Remark.
4. `p6_003_growth_norm_check.py` is listed both as a certificate and as the side lane's `reviewed_by` link; that entry is finite-only, as its scope says. Remark.

## Verdict

HOLDS.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
