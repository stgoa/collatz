# Review of finite-rational-cone-integer-certificate

Independent review (wave 7). Definitions were followed into [`right-aligned-fixed-core-remainder`](../right-aligned-fixed-core-remainder/README.md), [`five-ray-current-criterion`](../five-ray-current-criterion/README.md) and [`orbit-component-current-criterion`](../orbit-component-current-criterion/README.md). Every number below comes from my scratch code (outside the repository) or from the node's proof.

## What I checked

- **Certificates.** `python3 tools/run_certificates.py --node finite-rational-cone-integer-certificate`: PASS, exit 0, 7.0 s wall (`check_cone_recompute.py` 1 s; `check_legacy_replay.py` about 6 s, replaying `check_finite_cone.py` unchanged with every file byte-identical).
- **§1 lemma, re-derived.** A weak component `C` of the graph is closed under the current arrows, so `Σ_C (I − P)J = 0` and `Σ_C μ = Σ_C Z ≤ ‖Z⁺‖₁ < 1` for `C` not containing 1; an integer below 1 is `≤ 0`, and Theorem 1 of [`orbit-component-current-criterion`](../orbit-component-current-criterion/README.md) routes the integer coefficients. If `μ ≥ 0`, a nonabsorbing component with a nonzero source would have `Σ_C μ ≥ 1`. The component of 1 is an in-tree: every vertex has out-degree at most 1 and 1 has out-degree 0 (currents are measures on `X ∖ {1}`), so `#edges = #vertices − #sinks ≥ #vertices − 1` forces exactly one sink and no directed cycle; every vertex follows its arrows to 1. Both sharpness examples checked.
- **§2, re-derived.** `N_(k−10) = N_k/4`; `N_(k+3) ≥ 3N_k/2` with equality for `i = 0, 1, 2` and ratios `28/27`, `32/31.5` for `i = 3, 4`; `N_(k−2) = N_(k+3)/2`; the lower indices 5–14 have cutoffs at most 84. `λ(35/27) = 162742333796706147551/162889462677744140625 < 1` exactly; `r^5 > 2`; `a_i/r^i ≤ 12`, giving (1); (2) gives the block of `5(B − 3)` cutoffs with maximum `21·2^(B−1)`, and `p = 5 log₂(35/27) = 1.87198`, `p/(p−1) = 2.14682`.
- **§3, re-derived.** `Af ≤ λf` for `f_k = r^k` (omitted boundary columns only drop nonnegative terms), so `(I − A)^(−1) ≥ 0`. Expanding `e_(k*) = Σ_k w_k (e_k − A_k·)` is exactly (4); `T = h_(k*)` for `h = Ah + b`; the maximum principle for `g_k = h_k/r^k` gives `g_k ≤ λ·max g`, hence `T ≤ r^(k*) max_(ℓ>K) (N_ℓ/2 − 1)/r^ℓ < 6 r^(k*) (2/r^5)^B`.
- **§4, re-derived.** `ν_N = 3P(U_N − U_(N/4)) − U_(3N/2) − U_(3N/4)` for `8 | N` (valuation partition of the sources) and `P ν_N = Π_N + η_N` give (6); the target inequalities give `W_k ≥ 0` and (7). In the compiler theorem `Z = Σ (w_k/3)ζ_k − Σ (w_k/3)W_k + Σ_(ℓ>K) c_ℓ U_(N_ℓ)` with `w, c ≥ 0`, so `Z⁺ ≤ Σ_(ℓ>K) c_ℓ U_(N_ℓ)` pointwise and `‖Z⁺‖₁ ≤ T`; `U_g` is a nonnegative integer measure, so §1 applies.
- **Independent computation** (scratch script `recompute_r11.py`, own Gauss–Jordan over `Q`). For `m = 97`: `k* = 16`, `g = 112`; (2) selects `B = 10` and fails at `B = 9` (`6r^16(2/r^5)^9 ≥ 1`). Exact masses: `T(B = 8) = 122276046150/95104814731 ≈ 1.2856977`; `T(B = 9) = 31562113241597/46422343855805 ≈ 0.6798906` (30 cutoffs, maximum 5376); `T(B = 10) = 94871593415091/257308134588959 ≈ 0.3687081` (35 cutoffs, maximum 10752); for `m = 1001`, `B = 17` and `T = 29363305156616253425422658574417/44497622481390807869839145155909`. All agree with the claim and with `finite_cone_audit.json`. The maximum-principle bound holds for each plan. Identity (4) was verified as an identity of actual measures on odd integers (not only of coefficients) for `B = 8, 9, 10`; identity (6) in the form `D_N − (I − P)K_N = P ν_N` at `N = 96, 112, 128, 192, 2688, 5376`; every odd seed `≤ 84` and the core `5, 7, 11, 13` reach 1.
- **Lemma on random graphs.** 3000 random functional graphs on at most 7 vertices with random currents in `(1/3)Z`: 1285 instances satisfied `‖Z⁺‖₁ < 1` (183 with `μ ≥ 0`); in all of them every nonabsorbing component had mass `≤ 0`, and for `μ ≥ 0` every source lay in the component of 1 and reached 1 along current arrows.
- **Controls.** The lemma's strict threshold is exactly what the controls fail: for `3x+5`, `μ = δ_19` on the actual cycle `19 → 31 → 49` has `J = 0`, `Z = μ`, `‖Z⁺‖₁ = 1`, and no current exists. The compiler's hypotheses (supplied `Π_(N_k)` currents at every block cutoff) are not available for `3x+61` at its failing cutoffs ([`locally-collatz-like-control-barrier`](../locally-collatz-like-control-barrier/README.md)).

## What I did not check

- The right-aligned decomposition itself (R2, reviewed) and the 216000-case integer-gap audit, beyond re-running it in the replay.
- The demonstration [`actual-graph-current-compiler`](../actual-graph-current-compiler/README.md).
- Sharpness of the exponent `p/(p − 1)`; only the derivation.

## Findings

1. §1 proof (imprecision): "A finite functional graph component containing the sink 1 has no other sink or directed cycle" is correct but unargued; it needs the edge count above and the fact that 1 carries no current row.
2. §2 (imprecision): the lower cutoffs 28, 36, 42 and 84 are not divisible by 8. Harmless: only their counting measures enter (4); every packet cutoff `N_k`, `k ≥ 15`, is divisible by 8.
3. Claim and §5 (imprecision): the bound (2) selects `B = 10`, while the stated exact certificate uses `B = 9`; both are correct and both are stated, but a reader should note that "the 30 starting cutoffs through 5376" come from the exact solve, not from (2).
4. Legacy text (typo): commands and the "`../forcing/`" reference name pre-migration paths; documented under Certificates.

No error found.

## Verdict

HOLDS.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
