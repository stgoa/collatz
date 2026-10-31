# Review of base-inverse-phases-increasing-pairs

Independent review of [`README.md`](README.md) (legacy R45), its certificate and every displayed statement, against the definitions of [`elementary-bridge-quotient-normal-form`](../elementary-bridge-quotient-normal-form/README.md), [`critical-tripling-domain-equivalence`](../critical-tripling-domain-equivalence/README.md), [`critical-nine-elimination`](../critical-nine-elimination/README.md), [`decreasing-w5-phase-inverse-barrier`](../decreasing-w5-phase-inverse-barrier/README.md) and [`critical-image-rank-composition`](../critical-image-rank-composition/README.md). Every number below comes from my own scripts (own `S`, `selected`, `canonical`, `ν`, `ρ`, own R25 bridge currents, own R37 planner with the R40 request recursion; nothing imported from the legacy libraries) or from a derivation written out here.

## What I checked

- **Certificate.** `python3 tools/run_certificates.py --node base-inverse-phases-increasing-pairs`: PASS, exit 0, 9 s (real 8.9 s): legacy replay of `check_inverse_phases.py`, receipt and the `w = 1613` fixture unchanged.
- **Domain.** For `w ∈ W5`, `3w ≡ 7 (mod 8)` is an F-root with `a = v2(3w+1) ≥ 3`, so `ρ(w) = 3w` exactly when `3w` is complementary: the node's `B` is `{w ∈ W5 : ρ(w) = 3w}`, and `q = 3w` is complementary canonical.
- **Section 1.** `3(8w+1)+1 = 4(6w+1)` and `3(16w+1)+1 = 4(12w+1)`, so `S(b) = 2q+1` (the selected partner of `q`, `ν = q`) for `k = 4` and `S(b) = F(q)` for `k = 8`; both `b ≡ 1 (mod 8)`. With `p = 2^(h+1)C − 1`: `S^j(p) = 2^(h+1−j)·3^j·C − 1` for `j ≤ h`, each step of valuation exactly 1, ending at `2·3^h C − 1 = b`; the odd part `3^j C ≡ 3^(j+h) ≡ −3^(h+1−j) (mod 4)` (as `C ≡ 3^h (mod 4)` because `kw+1 ≡ 1 (mod 4)`), so every intermediate state and `p` itself are complementary canonical and `T^(h+1)(p) = q` as quotient steps. `C` is coprime to 3, so `p ≡ 0` or `1 (mod 3)`; `v ∈ W9` iff the exponent `h+1` is 2 and `3 | p`. `4w+1 ≡ w+1` and `8w+1 ≡ 2w+1 (mod 3)` give "only one ray has `h > 0`". Ordinary clocks `(h+2, 1)` and `(h+a+2, a+1)` verified by iteration.
- **Section 2.** `p < 3w ⟺ (3^(h+1) − k·2^(h+1))·C > 3 − k`; the coefficient is `7, 5, −17, …` for `k = 4` and `23, 37, 47, 13, −217, …` for `k = 8`, so the thresholds are `h ≥ 3` and `h ≥ 5`; the closest case `(k, h) = (8, 4)` would need `13w < 49`, impossible for `w ≥ 5`. The index table: coefficients `3^(h+1) − k·2^(h+1)` (row `p ≡ 0`) and `3^(h+1) − k·2^(h+2)` (row `p ≡ 1`) give thresholds 3, 5, 5, 6, and never equal `3 − k`, so `v = w` never occurs. `G`: `4^(−1) ≡ 7 (mod 27)` gives `w ≡ 20`; `8·91 ≡ −1 (mod 243)` gives `w ≡ 91`. The 17 classes: `47 (mod 81)` (`h = 3`, `C ≡ 1 mod 3`), `101 (mod 243)` (`h = 4`, `C ≡ 2`), `182 (mod 243)` (`h ≥ 5`), `577 (mod 729)` (`h = 5`, `C ≡ 1`), `91 (mod 729)` (`h ≥ 6`); all inside `G`, which has 30 classes modulo 729. Exhaustively for all 16,384 `w ∈ B` below `2^18` (10,923 positive-`h` plans): rank decrease iff `w ∈ G`, index decrease iff `w mod 729` is one of the 17 classes, every item above.
- **Section 3.** `div(A − N_(3v) − N_w) = [q] − [p] − [3v] + [p] − [w] + [z] = P(w) − P(v) − [v] + [z]`, checked with my own bridge currents for every `w ∈ B` below `2^16` with `h ≥ 1`. Bounds: `(9v+5)/8 ≤ (3p+4)/4 < p` for `p > 4`, and `(9z+5)/8 ≤ (9w+11)/32 < 3w`.
- **Section 4 at the request level.** With my own planner (R37 steps; W9 requests replaced by `requests(3z) − requests(z)` or `requests(6z+1) − requests(2z+1)` from R40 (5), (7)), the complete plan `P(v)`-part `+ H_v − H_z` for all 2,731 positive-`h` cases below `2^16`: 168 rank-decreasing (every request of rank `< 3w`; 74 with `v > w`), 911 exact tautologies `{w: 1}`, 1,652 failures with `v` the unique largest-rank request, coefficient `+1`, all others of rank `< p`. The totals 2,731 and 911 agree with the receipt. The zero-current identity (10) re-derived by hand for both rays: `k = 4` uses `C = (4w+1)/3 ≡ 7 (mod 32)` canonical, the R40 row `d = 4` with `z_0 = w`, and `H_(3w) = P(w) + H_w`; `k = 8` uses `C ≡ 35 (mod 64)` selected, `d = 5`, `S(ν(C)) = w` and `H_C = e_C + e_(F(w)) − e_w + H_w`; in both the currents cancel to `−N_w + H_w − H_z = 0` with the single request `P(w)`.
- **Examples.** `w = 1613`: `k = 4`, `h = 3`, `C = 239`, `p = 3823`, `v = 2549 > w`, ranks `4839 → 3823`. `w = 17101`: `k = 8`, `h = 5`, `C = 563`, `p = 36031`, `v = 24021`, ranks `51303 → 36031`.
- **Controls.** The base-ray identities are `3x+1` arithmetic: `S_d(8w+1) = 6w+1` fails for every `w ≡ 5 (mod 8)` below 2000 for `d = 5` and `d = 13`. The node claims nothing for other `d`; its Collatz-equivalence is through R37 and R43, whose control failures are recorded there.

## What I did not check

- The compiled fixture current for `w = 1613` beyond the replay (I checked request vectors and the local boundary (7), not the full compiled current with the R40 and R41 currents).
- The proofs of R37, R40, R41 and R43 beyond re-implementing what this node uses (all four are `reviewed`).
- The three dependents (`two-inverse-phases-intermediate-increase`, `nonselected-multiples-inverse-interface`, `native-growth-original-rank-exit-obstruction`); they use the base-ray parameters and the boundary `[3w] − [p]`, which I verified.

## Findings

1. **Notation (imprecision).** The letter `B` names `{w ∈ W5 : 3w not selected}` here, while R25, a dependency, uses `B` for the canonical set. The Statement defines it, so the text is readable; no change.
2. **Section 3, "where p ≥ 7" (imprecision).** The inequality `(3p+4)/4 < p` needs only `p > 4`; on the rank-decreasing rows `p = 2^(h+1)C − 1 ≥ 15`, and on every positive-`h` row `p ≥ 27` (`k = 4`: `C = (4w+1)/3 ≥ 7`). No change.
3. **Section 2, "no small exceptions" (imprecision, verified).** The only case where the sign of `(3^(h+1) − k·2^(h+1))·C − (3 − k)` depends on the size of `w` is `(k, h) = (8, 4)`, where `p < 3w` would need `13w < 49`; it is excluded only because `w ≥ 5`. The text says "below these thresholds `p > 3w`" without naming this case. No change.

## Verdict

HOLDS. No correction; the certificate passed; the status is raised to `reviewed`.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
