# Review of prefix-rule-cylinder-rate-barrier

## What I checked

- Read the node, [`halving-coalescence-return`](../halving-coalescence-return/README.md) (the halving identity), [`absorbed-fibre-uniform-counts`](../absorbed-fibre-uniform-counts/README.md), the cutoff set `G_5` of [`five-ray-current-criterion`](../five-ray-current-criterion/README.md), the checker and the receipt.
- **Rates recomputed independently** (40-digit decimal arithmetic, my own code): `c = log₂3 = 1.5849625007…`, `ρ = c^c/(2^c (c − 1)^(c − 1)) = 0.94650457683258419880…`, `β = ρ^(1/c) = 0.96590655323343772360…`; the entropy form `exp[−q log q − (1 − q) log(1 − q)]/2`, `q = 1/c`, agrees with `ρ^(1/c)` to `4·10^(−40)`, and I re-derived that identity by hand. The Markov bracket `e^(θc)/(2e^θ − 1)` is minimised at `e^θ = c/(2(c − 1)) = 1.35476 > 1` with minimum `ρ` (checked against `θ* ± 0.01`); the Chernoff bracket `(1 + z)/(2 z^q)` at `z = q/(1 − q) = 1.70951` equals `β`. The claim's 15-digit decimals are correctly rounded.
- **§3.1–3.4 re-derived.** `E e^(θ L_n) = [e^(θc)/(2e^θ − 1)]^n` for the geometric letter law and `L_j = cj − A_j`; conditioning on `a_1 = 1` costs a factor 2; the cycle-lemma rotation after a minimum of the partial increment sums (all rotated partial sums nonnegative, including the wrapped part; at most `n` preimages); `a_1 = 1` forced by `1 < c < 2`; Stirling gives `c log c − (c − 1) log(c − 1) − c log 2 = log ρ`. Bit clock: a surviving last completed prefix with `k` letters and last success at `t` has `k ≥ qt − b/c`; the Chernoff bound with `z > 1`; `Σ_t β^t 2^(−(L−t)) ≤ C β^L` because `β > 1/2`; the lower bound `binom(L − 1, j − 1)/j` with `j = ⌈L/c⌉` at rate `β`.
- **§4.** `x ≡ 47 (mod 64)` has exact word `(1, 1, 1, 2)` and `S^4(x) = (81x + 65)/32` (2000 members); slope `81/32 > 2`; no D or M test fires along the prefix; the valuation-1 run from `r = 0` is eligible but closed by a 2, so H cannot fire; appended zero-barrier words keep the global slope `≥ 81/32 > 4/3`, so no later D, M or H acceptance is possible.
- **§5.** `x ≡ 3 (mod 16)` is selected (`a = 2`, `t ≡ 1 (mod 4)`) with second valuation `≥ 3` (500 members), giving `3/4` at `m = 4` under partial closing. The table recomputed by my own state-merging dynamic program and, for `2 ≤ m ≤ 14`, by direct enumeration of the residues `x ≡ 3 (mod 4)` modulo `2^m` for all four variants (DP equals enumeration): `m = 4`: `1, 1, 1, 3/4`; `m = 8`: `19/32, 35/64, 1/2, 25/64`; `m = 16`: `4057/16384, 867/4096, 2555/16384, 2431/16384`; `m = 64` and `128`: all twelve printed decimals reproduced; `m = 96` (D): `0.002140830523`. The four 96-to-128-bit fitted factors for `K = 1, 4, 16, 64` reproduce to all ten digits (`0.9546098033, 0.9565378898, 0.9572643214, 0.9580886202`). Odd-step rows `p_1..p_8` match the receipt (D+M+H: `681/4096` at `n = 8`).
- **Approach to the rates (illustration, not proof).** `p_n/ρ^n` for D decreases like a power, 0.062 (`n = 50`) to 0.0039 (`n = 400`); `u_m/β^m` from 0.041 (`m = 128`) to 0.0022 (`m = 1024`), with 64-bit ratio roots `0.9577 → 0.9649` against `β = 0.9659`; consistent with exponential rates exactly `ρ`, `β` and polynomial prefactors. The Markov bound `p_n ≤ 2 e^(θ* b) ρ^n = 2.3887 ρ^n` (`b = c − 1`) holds for all `n ≤ 400` (largest ratio 1.057). With the shell `K = 4`, `p_400/ρ^400 = 0.0136`, the same rate.
- **§6.** For `a ∈ {6, 10, 14, 18, 22}`: `S^a(2^a − 1) = S^a(2^(a−1) − 1) = (3^a − 1)/8`, the prefix states are `3^j 2^(a−j) − 1` and exceed `x`, `x ≡ 3 (mod 12)`, `N < x < 3N/2`, `q < N`, `z > N`, `z/N = 9.6, 48.7, 246, 1247` for `a = 10..22`. `N = 12·2^(a−4) ∈ G_5` exactly when `a − 4 ≥ 3`.
- **Certificate.** `python3 tools/run_certificates.py --node prefix-rule-cylinder-rate-barrier`: PASS, exit 0, wall 3.6 s (two runs).
- **Controls.** The node is about `3x+1` cylinder measures and slope tests and claims nothing about cycles; nothing in it would exclude the actual `3x+d` cycles.

## What I did not check

- §7's audit of the side lane's excursion experiment (I agree with its five "does not follow" items but did not rerun `coalescence_check.py` or `excursion_merge_probe.py`).
- The source hashes recorded in `external_review.json`.
- The 32- and 96-bit rows of the other three variants beyond the D row at 96 bits.

## Findings

1. §6, "`a ≥ 10`": the construction works for every `a ≡ 2 (mod 4)`, `a ≥ 6` (checked at `a = 6`: `N = 48`, `x = 63`, `q = 31`, `z = 91`); the restriction only ensures that `N = 12·2^(a−4)` is a five-ray cutoff (`b = a − 4 ≥ 3`, hence `a ≥ 7`, hence `a ≥ 10` in the class). The text does not say why. Imprecision.
2. §3.3 bounds the bit-clock survival using only the constraint at the last completed prefix and drops the condition that position `t` is a success; both only enlarge the bound, as stated. Correct. No issue.
3. Statement 1's "exact rates" are rates: the three recognizers differ by constant factors (`p_8 = 131/512, 111/512, 681/4096`), which §2 says explicitly, and the escape prefix contributes a factor `1/16` and a clock shift of 4 without changing the limits. Correct. No issue.
4. The side lane's `reviewed_by` link points to its probe in another node (`../halving-coalescence-return/coalescence_check.py`), finite-only as its scope says. Remark.

## Verdict

HOLDS.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
