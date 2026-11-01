# Review of valuation-debt-reset-obstruction

## What I checked

- Certificate [`check_legacy_replay.py`](check_legacy_replay.py) via `python3 tools/run_certificates.py --node valuation-debt-reset-obstruction`: PASS, exit 0, 42 s wall (the node says about 37 s).
- Definitions from [`elementary-bridge-quotient-normal-form`](../elementary-bridge-quotient-normal-form/README.md) (`F(x) = 4x + 1`, selected and complementary climbers, the canonical set `B`, `ν`), [`critical-image-rank-composition`](../critical-image-rank-composition/README.md) (`ρ(w) = ν(3w)`, equal to `3w` for canonical `3w` and to `(3w − 1)/2` for selected `3w`; request bound `(9s + 5)/8`), [`returning-forward-interface`](../returning-forward-interface/README.md) (`E_return`, `3w = 2^a t − 1`, `t ≡ 3^a (mod 4)`, `2^a t ≡ 10 (mod 27)`, interface (4), accepted `a = 3` inputs with noncanonical `r`) and [`mixed-rank-growing-blocks`](../mixed-rank-growing-blocks/README.md) (cylinder `w ≡ 40529845 (mod 2^26)`, `u = (2187w + 1209)/1024`, `v = (243u + 17)/512`).
- Section 1. `D = 7153 = 3^12 − 2^19`; (3) as identities of affine maps (intercepts `7153·1209 + 656187·1024 = 2187·311195 = 680 583 465` and `7153·17 + 311195·512 = 243·656187 = 159 453 441`); `H_E(u) = H − 10`, `H_W(v) = H − 19`; the ratios `3^7/2^20` and `3^5/2^18` of `K`; `v = (3^12 w + 311195)/2^19`; `40529845 ≡ −311195·7153^(−1) (mod 2^26)`.
- Section 2, for `H = 26, …, 40, 64, 128` and indices 0, 1, 7 of the CRT progression (period `81·2^(H+1)`): `v2(L_W(u)) = H`, `u ≡ 5 (mod 8)`, `u ≡ 4 (mod 9)` (so `u ∉ E`), `3u` complementary, hence canonical and `ρ(u) = 3u`; `w = (64u + 5)/9` is an integer with `w ≡ 3 (mod 9)`, `w ≡ 5 (mod 8)`; `3w + 1 = 8t` with `t = (8u + 1)/3` odd, `t ≡ 3 (mod 4)` (selected) and `8t ≡ 10 (mod 27)`, so `w ∈ E_return` with `a = 3`; `q = ρ(w) = (3w − 1)/2 = (32u + 1)/3 > 3u`; `r = (9t − 1)/2 = 12u + 1 = F(3u)`, `r ≡ 5 (mod 8)` with `v2(r + 1) = 1`, so `r` is noncanonical and the plan lies in R44's accepted `a = 3` subdomain; the word `(1, 2)` carries `q` to `r`; `S(r) = S(3u)` and `ν(r) = 3u`, so `S^3(q) = S(3u)` and `T^2(q) = 3u`. Bounds (9): `z = ν(w) ≤ (w − 1)/4 = (16u − 1)/9`, `(9z + 5)/8 ≤ 2u + 1/2 < 3u`, and `(9u + 5)/8 < 3u`.
- (9a) step by step. `u ≡ 5 (mod 16)` and `m = (u − 5)/16 ≡ 11 (mod 16)` is complementary, so `ν(u) = m`; `m ≡ 2 (mod 3)` and `(2m − 1)/3 = 3a` with `a = (u − 13)/72 ∈ W5`, `9 | a`. `z_0 = (w − 1)/4 = (16u − 1)/9 ≡ 7 (mod 8)` is selected with exponent 3, so `z = ν(w) = (z_0 − 1)/2 = (8u − 5)/9`, complementary and `≡ 2 (mod 3)`; `(2z − 1)/3 = (16u − 19)/27 = (3b − 1)/2` with `b = (32u − 11)/81 ∈ W5` and `3b` selected. Writing `u = 648c + 13`: `a = 9c`, `b = 256c + 5`, `c ≡ 101 (mod 128)`; `b = F(64c + 1)` with `64c + 1 ≡ 1 (mod 8)`; `S(64c + 1) = 48c + 1 ≡ 1 (mod 8)` and `S(48c + 1) = 36c + 1 = F(a)`, both steps of valuation 2; `ν(36c + 1) = ν(a)`. Hence `A_u = {a:1} + A_a`, `A_z = {b:1} + A_b`, `A_b = A_a`, and the frontier is `P(u) + P(a) − P(b)`, with `ρ(u) = 3u`, `ρ(a) ≤ 3a` and `ρ(b) = (16u − 19)/27` all below `q`.
- (10)–(11). `9L_E(w) = 64L_W(u) − 13 975 032` as an identity in `u`, `v2(13 975 032) = 3`, so `H_E(w) = 3` while `H_W(u) = H`; `K(u)/K(w) > 9·2^(H−9)`. The stored parents `61 849 410 141` (`H = 26`) and `1 008 756 393 712 221` (`H = 40`) are the least members.
- Section 3, the theorem. Fixed `H = 26` and `w → ∞` along the progression: the first edge forces `α_E ≤ α_W`, the second `α_W ≤ α_E`. With `α` common and `H → ∞`: `β_E ≤ β_W` and `β_W ≤ β_E`. The block ratio `(3^12/2^19)^α·2^(−19β)` is at least 1 for `β ≤ 0` because `3^12 > 2^19` and `α ≥ 0`, so strict block decrease needs `β > 0`; then (14) gives `Φ(u)/Φ(w) > (C_W/C_E)(9/64)^α·2^(β(H−3)) → ∞`, using `L_W(u)/L_E(w) = 9L_W(u)/(64L_W(u) − 13975032) > 9/64`. Both centres in both phases: `v2(B_E − B_W) = 5`, so the inactive orders are 5 at `w, u, v` (as `H − 19 ≥ 7`), and `(H, 5)` at the child and `(3, 3)` at the parent of the reset family; bounded factors only.
- Section 4. `g(θ) = (64θ + 5)/9 = −6 626 905/21 459` for `θ = −311 195/7153`, and `3(21459w + 6626905) = 64L_W(u)` exactly, so the pulled-back order is `H + 6`.
- All of the above runs in `recompute_debt.py` (review lane's scratch folder) with my own `ν`, `S`, `F` and climber tests; every assertion holds. I read `valuation_debt.py` and `check_valuation_debt.py`: they assert the same identities and recompute the plans through the legacy R44 and R43 modules.
- Controls. The claim concerns potentials on specified dependency edges of `3x+1` plan compilers; it is a statement about explicit linear forms and is independent of whether Collatz holds, so no actual `3x+d` cycle bears on it. Not applicable.

## What I did not check

- The R44 forward plan and the R43 bound themselves (both reviewed on 2026-10-31 by this lane in separate sessions); I used their statements.
- The 35 rational-power illustrations, the nine rejections and the two stored conversions (180 and 235 rows) beyond the certificate's replay.
- The forward reference to the R73 joint normaliser at the end of section 2, which is not a premise.

## Findings

1. (remark) The hypothesis `α_p ≥ 0` is essential and is stated: with `α < 0` the block ratio (13) can fall below 1 for `β ≤ 0`, and (14) then stays bounded.
2. (typo, not changed) The legacy text lost many spaces in migration ("coefficient+1", "u5mod8", "w3mod9 with selected3w", "a3", "modulo2^26", "H512", "parent61849410141, child8697573301 at H26 uses3 supplied pairs and180 output rows"); every such token was decoded against the Statement and the receipt and is consistent.
3. (remark) Claim 2 says "valid R44 exponent-three plan"; validity here is R44's own test (`a = 3`, `r` noncanonical), which I verified, not an assumption.

## Verdict

HOLDS.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
