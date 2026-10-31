# Review of binary-residue-projection-information-loss

Independent review of the node [`README.md`](README.md) (moved from the single file `binary-residue-projection-information-loss.md` at this review; seven relative links inside it repointed, and the inbound links in `reflected-negative-annulus-control.md`, `exposure-potential-boundary-flux/README.md` and the questions `uniform-aggregate-exposure-depth`, `five-ray-annular-current-supply`, `annular-component-progress-lemma` repaired). Scratch script: `review-work/binary-residue-projection-information-loss/check_projection.py` (outside the repository).

## What I checked

- **Definitions.** `A_N`, `Q = 9N/4`, the six bands `2^j Q < y < 2^(j+1) Q` and the `6 × 6` coefficient table are those of [`disjoint-annular-recursion`](../disjoint-annular-recursion/README.md) (status `reviewed`, independently re-derived in this wave); `A_N` is supported on odd `y` not divisible by 3 and depends on `y mod 18` in each band. I took the table as given.
- **Row sums.** By hand, each row of the table sums to zero on `{1, 7, 13}` (the class `1 mod 6`) and on `{5, 11, 17}` (the class `5 mod 6`): rows `(1,1,−2 | 0,0,0)`, `(2,−1,−1 | 1,1,−2)`, `(3,−3,0 | −1,2,−1)`, `(1,−2,1 | −3,3,0)`, `(−1,−1,2 | −2,1,1)`, `(0,0,0 | −1,−1,2)`. So the proof's premise holds, and every whole row sums to zero too.
- **Periods.** `lcm(18, 2^K) = lcm(18, 3·2^K) = 9·2^K` for `K ≥ 1`. In one period, the integers `y ≡ r (mod 2^K)` with `r` odd number 9 and have residues `r, r + 2^K, …` modulo 9 running through all classes (2 is invertible mod 9), so they meet every odd residue mod 18 exactly once; those with `y ≡ r (mod 3·2^K)` number 3 and lie in the three odd residues mod 18 of the class `r mod 6`. Checked by code for `K = 1, …, 8` and every odd `r`.
- **Hypothesis use.** `2^(K+2) | N` is exactly what makes `Q = 9N/4` a multiple of `9·2^K`; then the integers `2^j Q + 1, …, 2^(j+1) Q` of band `j` (the even endpoint carries no mass) form `2^j Q / (9·2^K)` complete periods, so each band-wise projection is a sum of complete-period sums, each zero. For `K ≥ 1` the hypothesis implies `8 | N`, as `A_N` requires.
- **Independent computation.** Built `A_N` from the table and summed it band by band on every residue class mod `2^K` and mod `3·2^K`: zero in all 42 cases `K = 1, …, 7`, `N ∈ 2^(K+2)·{1, 3, 5, 7, 9, 21}` (exit 0, 1.2 s). When the hypothesis fails (`8 | N` but `2^(K+2) ∤ N`, e.g. `N = 8, K = 2`) some band-residue sums are nonzero in all 18 cases tried, so the hypothesis is not vacuous.
- **Five rays.** `N = a·2^r·64^k` has `v₂(N) ≥ 3 + 6k`, so for fixed `K` every cutoff with `k ≥ (K − 1)/6` satisfies the hypothesis, as the claim says.
- **Evidence.** `python3 areas/convergence/results/exposure-potential-boundary-flux/check_duality.py` (a certificate of that node, listed here as evidence): exit 0, 0.77 s; its projection cases are `N = 12·2^max(3,K)`, `K = 1, …, 8`, all of which satisfy `2^(K+2) | N`.
- **Certificates:** none listed for this node.
- **Controls.** Not applicable: the annulus `A_N` and its `×64` recursion are specific to `3x+1` (the shift `q_(a+6) = 64 q_a + 21`; [`disjoint-annular-recursion`](../disjoint-annular-recursion/README.md), Remarks), and the node claims nothing `d`-uniform and nothing about cycles or words.

## What I did not check

- The derivation of the table itself (taken from the reviewed dependency).
- The remarks on negative-cycle shadowing and on [`unbounded-exposure-depth-necessary`](../unbounded-exposure-depth-necessary/README.md); they are cross-references, not part of the theorem.

## Findings

1. **Proof, "a fixed odd binary residue visits every odd residue modulo 18 exactly once, so the coefficients sum to zero" (imprecision).** The conclusion uses the zero sum of the *whole* row (nine odd residues, three of them multiples of 3 with coefficient 0), not only the two three-term sums quoted in the previous sentence. Both are true; the sentence just does not say which one it uses.
2. **Statement (imprecision).** The theorem also needs `A_N` to vanish at even `y` and at multiples of 3 (true by the dependency); the proof mentions it only for the endpoints. No effect on the claim.

## Verdict

**HOLDS.** The identity is correct exactly as scoped (band by band, moduli `2^K` and `3·2^K`, hypothesis `2^(K+2) | N`), and the information-loss reading in the claim follows from it. No corrections to the claim.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
