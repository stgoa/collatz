# Review of no-finite-affine-valuation-rank

## What I checked

- Certificate [`check_legacy_replay.py`](check_legacy_replay.py) via `python3 tools/run_certificates.py --node no-finite-affine-valuation-rank`: PASS, exit 0, 15 s wall (the node says about 13 s).
- Definitions as in the review of [`valuation-debt-reset-obstruction`](../valuation-debt-reset-obstruction/README.md) (R25 normal form, R43 rank and bound, R44 returning row, R67 cylinder) and the phases `E`, `W`.
- Section 2. (4) and (5) as affine identities; `v2(u − θ_E) = H − 10`, `v2(v − θ_W) = H − 19`. The stabilisation lemma: from `f(x) = f(θ) + a(x − θ)`, the order is `v2(f(θ))` once `v2(x − θ) + v2(a) > v2(f(θ))`, and `v2(x − θ) + v2(a)` if `f(θ) = 0`. At fixed exact `H` beyond the threshold, `w → ∞` along the progression leaves every valuation factor fixed while the heights grow linearly, so the first edge forces `α_E ≤ α_W` and the second `α_W ≤ α_E`. With `α` common and `H → ∞`, the exponents `(b_E − b_W)H` and `(b_W − b_E)H` force `b_E = b_W = b`. In (8), all off-centre orders agree at `w` and `v` once stabilised and the `θ_W` forms lose exactly 19, so `Φ_W(v)/Φ_W(w) = (h_W(v)/h_W(w))^α·2^(−19b)`; `v > w`, `h_W` increasing and `α ≥ 0` make this at least 1 for `b ≤ 0`, hence `b > 0`.
- Section 3, by hand and in `recompute_centres.py` (review lane's scratch folder, own normal form) for `L = 1, 4, …, 22`, `H = 26, 27, 40`, indices 0 and 2. `a` is the least integer with `6·4^L(2/3)^a ≤ 4` (`a = 5, 15, 25, 35, 46, 56, 66, 77`), `a > 3`, `8/3 < λ ≤ 4`, `a ≥ 3L + 2`; `κ = λ/9 − 1/3 + (2/3)^a/3 ∈ (−1/27, 1)`; `d_L = (2p + 1)/9 ∈ Z` because `4^L ≡ 4 (mod 9)`. The CRT member `u` has `v2(L_W(u)) = H`, `u ≡ 5 (mod 8)`, `u ≡ 40529845 (mod 2^26)`, `3u` complementary (canonical, not selected), so `ρ(u) = 3u` and `u ∈ W`. `r = F^L(3u) = 3pu + (p − 1)/3 ≡ 5 (mod 8)`, `2r + 1 = 3(2pu + d_L)`, `v3(2r + 1) = a − 1`; `t = (2r + 1)/3^(a−1)` is odd with `t ≡ 3^a (mod 4)`, `t ≡ τ (mod 27)`, `2^a t ≡ 10 (mod 27)`; `w = (2^a t − 1)/3 = λu + κ` is an integer with `w ≡ 3 (mod 9)`, `w ≡ 5 (mod 8)` and `3w` selected with exponent `a`, so `w ∈ E_return`; `2u < w ≤ 4u` (the upper bound from `κ < 1` and integrality); `q = ρ(w) = (3w − 1)/2 > 3u`; `(9w + 11)/32 < 3u` and `(9u + 5)/8 < 3u`, so `P(u)` is the unique highest request with coefficient +1 (`A_r = {u:1} + A_u` because `ν(r) = 3u`); the word `1^(a−2), 2` carries `q` to `r` with exactly these valuations; `S(r) = S(3u)`, giving the clocks `(a, 1)`.
- Section 4. (21): `γ_L = λθ_W + κ` equals the displayed fraction. (22): `v2(den(γ_L)·w − num(γ_L)) = H + a + 2L + 1` at every tested member, as `v2(λ) = a + 2L + 1` and both reduced denominators are odd. (23), for `L ≡ 4 (mod 9)`: `p ≡ 13 (mod 27)`, `3 | d_L`, `K_L ≡ 2 (mod 3)`, numerator of ternary order exactly 1 against denominator order `a`, so the reduced denominator has order `a − 1`; the 24 poles `L = 4, 13, …, 211` are pairwise distinct with that order. (24), for `L ≥ 13`: `|T_L| < 3^(2L+15)`, `v3(T_L) ≤ 2L + 14 < a`, `v3(den γ_L) = a + 1 − v3(T_L) ≥ L − 11` (tested at `L = 13, 16, 19, 22`). `a` strictly increases with `L` because `λ_(L+1)(a_L) = 4λ_L(a_L) > 32/3 > 4`.
- Section 5. With `b > 0` and a fixed `L ≡ 4 (mod 9)` whose `γ_L` is not a centre of the finitely many `E` forms, along `H → ∞` the `E` orders at `w → γ_L` and the off-centre `W` orders at `u → θ_W` stabilise, the `θ_W` forms contribute `bH + O(1)`, and the height ratio tends to `(c_W/(c_E λ))^α`, so `Φ_W(u)/Φ_E(w) → ∞`, violating requirement 3 on a child of coefficient +1. The least members grow because `Du + B_W ≡ 2^H (mod 2^(H+1))` with positivity forces `u ≥ (2^H − B_W)/D`.
- I read `finite_centres.py` and `check_finite_centres.py`: `parameters`, `family` and `comparison` assert the same facts (through the legacy R44 and R43 modules); my checks mirror them with independent code.
- Controls. Not applicable, as for R69: a statement about explicit affine forms along `3x+1` plan edges, independent of the truth of Collatz.

## What I did not check

- The R44 `descending` status beyond the direct comparison `3u < q` and the bounds (19); the certificate asserts it through the legacy module.
- The three finite-list pole examples (`H = 512, 768, 1024`) and the two stored conversions (158 and 211 rows) beyond the replay.

## Findings

1. (imprecision) Requirement 3 quantifies over every `L ≡ 1 (mod 3)`, whereas the proof uses one `L ≡ 4 (mod 9)` chosen after the finite list, with `H → ∞`. The theorem is correct as stated and slightly weaker than what is proved (nonincrease on the `L ≡ 4 (mod 9)` families alone suffices). No change.
2. (remark) The hypotheses `α_p ≥ 0` and `c_p > 0` are both used (in (8) and in the height limit of section 5) and both stated. The statement's exclusions are exact: a potential whose valuation forms depend on the other endpoint, or on history, is outside the class.
3. (typo, not changed) Lost spaces in the legacy text ("Section1", "coefficient+1", "L211", "H512,768,1024", "parent189106655349"); decoded against the receipt.

## Verdict

HOLDS.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
