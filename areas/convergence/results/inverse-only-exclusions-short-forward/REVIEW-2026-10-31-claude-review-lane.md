# Review of inverse-only-exclusions-short-forward

Independent review (Claude review lane, Fable 5.1), a different lane from the main lane that wrote the node (R49) and from the side lane whose probe is stored here. Every number below comes from my own code or from the node's proof.

## What I checked

- **Certificate.** `python3 tools/run_certificates.py --node inverse-only-exclusions-short-forward`: `check_legacy_replay.py` PASS, exit 0, 8 s (it replays `check_inverse_scope.py` and `r49_ancestor_free.py` in the rebuilt legacy layout; both receipts reproduced unchanged).
- **Definitions.** Re-read the inputs the argument uses: `ν`, the canonical set, `T = νS` and the complete inverse branches of [`elementary-bridge-quotient-normal-form`](../elementary-bridge-quotient-normal-form/README.md); the affine inverse table and the shadow argument of [`decreasing-w5-phase-inverse-barrier`](../decreasing-w5-phase-inverse-barrier/README.md) §4; the `W5`-only plan `H_s` and its bound `(9s+5)/8` of [`critical-image-rank-composition`](../critical-image-rank-composition/README.md); the `a = 3` classification of [`forward-blocks-low-exponent-tests`](../forward-blocks-low-exponent-tests/README.md). All four are `reviewed`.
- **Section 1 (scope theorem).** Re-derived: `Q` `T`-forward-closed and `q ∉ Q` give `T^d(p) = q ⇒ p ∉ Q` directly, and `S^d(x) = q ⇒ ν(x) ∉ Q` through `ν(S^d(x)) = T^d(ν(x))` and `ν(q) = q`. The finite certificate (every canonical `p < b` in `Q`, `Q` closed, `b ∉ Q`) excludes every depth; the ordinary version uses `ν(p) ≤ p`.
- **Section 2 (anchors), with my own `S`, `ν`, `T`.** `Q_<39` has 43 states, maximum 1025; `Q_<135` has 68 states, maximum 1457; both equal the stored edge tables in `anchor_certificates.json` exactly, are `T`-closed, contain every canonical state below `b`, and exclude `b`. `39` and `135` are complementary canonical, `3 | b`, `b/3 ∈ W5`, `3·(b/3)` nonselected, so `ρ(13) = 39`, `ρ(45) = 135`. Descents `39 → 59 → 89 → 33` and `135 → 203 → 305 → 57`: the first two arrows are ordinary valuation-1 arrows between canonical states, the third normalises (`S(89) = 67`, selected, `ν = 33`; `S(305) = 229 ≡ 5 (mod 8)`, `ν = 57`); the first three vertices lie outside `Q_<b`, the last inside. Stored lower currents (54 and 114 rows): nonnegative, divergence `Σ [p]` over odd `3 ≤ p < b`; stored pair currents (9 and 11 rows): divergence `P(13)`, resp. `P(45)`. Brute force below `2^18`: every canonical ancestor of 39 and of 135 is larger (smallest: 105 at depth 1 for 39, 361 at depth 1 for 135).
- **Section 3 (infinitude).** `r_k = (16·64^k − 7)/9` is canonical with `T(r_k) = 1` for `k = 0, …, 59`, and `r_(k+1) = 64 r_k + 49`. The least-origin argument re-derived: `m(q)` exists (depth 0 allowed), is inverse-minimal and absorbed; finitely many minima would give a finite absorbed canonical set.
- **Section 4 (lifts).** Rebuilt the inverse table from R25's branches (point `(2y−1)/3` at `y ≡ 2`, rays `(4F^k(b)−1)/3`, `b ∈ {y, 2y+1}`, `k ≡ 1 − b (mod 3)`): the base rows are those of R41's table, `α − β ≥ 1` with equality only at the point, and `α_j − β_j = 64^j(α − β − 7/9) + 7/9` under `p → 64p + 49`. Re-derived (6) and (7): `G_i = α_i G_(i−1) + (α_i − β_i − 1)/(b+1)`, `G_0 = 0`, first step a ray (since `b ≢ 2 (mod 3)`), hence `λ_i > (c_i+1)/(b+1) ≥ 1` and `p_i = λ_i(q−b) + c_i > q`. Checked on 288 random inverse words (all three branch kinds, ray indices 0–2) at 48 family members (`b = 39`, `D = 2..5`; `b = 135`, `D = 4..7`; `t = 1..6`): residues agree before each step, every shadow is a canonical ancestor `≥ b` outside `Q_<b`, (7) holds, `λ_i > 1`, `p_i > q`. Brute force for the members below `3·10^5`: no odd `p ≤ q` reaches `q` within `D` quotient or `D` ordinary steps. Family properties (8): `q` canonical, `v3(q) = 1` resp. `3`, `w ≡ 13 (mod 256)` resp. `45 (mod 128)` with `v3(w) = 2`, `3w` nonselected, `v3(q − b) = D` when `3 ∤ t`.
- **Section 5 (forward escape).** 1304 members of the two cylinders (all below 60000 and 600 random members up to `2^38`): the first two arrows have valuation 1 between canonical states, `S^3(q) = y = (27q+19)/16`; row one: `y` selected with `v2(y+1) = 2`, `r = (27q+3)/32`; row two: `y ≡ 5 (mod 8)`, `r ≤ (27q+3)/64`; `r = T^3(q)`; (10) `r < q`, `9r + 5 < 8q`. R48 parameters at `a = 3`: `d = v2(9t − 1) = 2` with selected endpoint `f = y`, resp. `d = 3` with `F(f) = y`, so both cylinders are accepted by R48's `a = 3` test. The plan (11) built with my own `W5`-only `H` for all 234 members below 20000: divergence `P(w) − Σ (A_r − A_z)(u) P(u)`, every request in `W5` with `ρ(u) < q`, `ρ(u) ≤ (9r+5)/8` on the upper side, `4z < w`.
- **Census (Remarks).** Own recount: among the 499,998 canonical `q` with `1 < q < 2·10^6`, 242,468 (48.49%) have no smaller canonical ancestor; shares `0.8848`, `0.5700`, `0` by `q mod 3`; the first twenty agree with the probe's receipt.
- **Controls.** The scope theorem is a statement about forward-closed sets and holds for any map. For `3x+5` the cycle minimum 19 has the smaller origin 11 (`11 → 19 → 31 → 49 → 19`), so the finite-exclusion hypothesis fails there and nothing about the `3x+d` cycles is excluded; the node makes no absorption claim.

Scratch work: `rederive_r49.py` in my review folder (own primitives; my `W5`-only absorption plan written from R37/R40/R41 in an earlier wave).

## What I did not check

- The legacy scripts' internals beyond the replay (`inverse_scope.py`, its discovery caps and hashes).
- Ray indices above 2 in the sampled shadow words; the written argument covers all indices through (8), which I re-derived.
- The statement "contained in R48" beyond R48's `a = 3` parameters (R48 itself is reviewed).

## Findings

1. Remarks, census (imprecision). "Of the 499,998 canonical states below `2·10^6`" counts canonical `q > 1`; `q = 1` is trivially ancestor-free. Including it gives 499,999 and 242,469, with the percentages unchanged to four digits.
2. Statement 4 (information, no change). The lifts are depth-limited by construction, as the node says: the member `q = 4647` (`b = 39`, `D = 2`, `t = 2`) has the smaller canonical ancestor 2175 at depth 7 `> D`. Only the two anchors are permanently inverse-minimal.
3. Section 5 (imprecision). "The run parameter there is `d = v2(9t−1)` … 2 in the first cylinder and 3 in the second": correct, but the acceptance by R48 in the first cylinder uses the *selected even endpoint* clause of R48's `a = 3` test, not even `d ≥ 6`; the second uses odd `d`. Worth saying, since it is the reason the containment holds.

## Verdict

HOLDS.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
