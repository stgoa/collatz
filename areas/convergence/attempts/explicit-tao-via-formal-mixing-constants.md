---
id: explicit-tao-via-formal-mixing-constants
kind: attempt
title: Reading explicit mixing constants for Tao's argument off the machine-checked positive-density library
status: reviewed
claim: >
  Tried (explicit-Tao lane, legacy L4 part 0): take the explicit Syracuse mixing constants that the audited Lean
  library AxiomMath/CollatzPositiveDensity at 3a38bfbb proves inside its own chain, instead of re-deriving Tao's. The
  library proves primitive Fourier decay ||mu_n(xi)|| <= C_*/n^(10241/4096) with C_* = (160 D_*)^(10241/4096) and
  D_* a rational with thousands of digits, and its mixing lemma only for 3-adic levels 2^80000 <= m <= q (generation
  threshold N_* = 6103914). Verdict, an order-of-magnitude comparison and not a theorem about Tao's constants: any
  threshold C(delta) assembled from these lemmas is at least of the order of 3^(2^80000) for every delta, hopeless
  against the verified range; the machine-checked route contributes only the row C = 1 (reaching 1) at natural
  density 1 - 2^(-2^(2^87640)) for N >= 2^2^2^2^87640.
authors:
  - Claude explicit-Tao lane (Opus)
created: 2026-10-18
depends_on: [lau-density-formal-replay]
assumes: [lau-2026-positive-density, tao-2019-almost-all]
reviewed_by:
  - by: Claude Lean lane (Fable)
    date: 2026-10-18
    scope: "Side-lane feed 2026-10-18 19:44, CONFIRMED at claude/explicit-tao a00a6c1 as a calibration: the quoted Lean statements agree with the main lane's independently written lau_scope.md section 3.2 (now in lau-density-formal-replay): the Fourier decay C_* n^(-10241/4096) with C_* = (160 D_*)^(10241/4096), mixing only for 2^80000 <= m <= q, N_* = 6103914 and the challenge constants; the order of magnitude checks out (3^(2^80000) has about 10^24082 digits); the conclusion that this route adds only the trivial row follows. The lead itself came from the side lane (feed 19:39)"
aliases: [TAO-L4-b]
tags: [convergence, explicit-tao, mixing, lean, external-library, calibration, explicit-constants]
---

# Reading explicit mixing constants for Tao's argument off the machine-checked positive-density library

## Idea

The explicit-Tao programme ([`explicit-tao-almost-all-constants`](explicit-tao-almost-all-constants.md)) needed explicit constants for the mixing of the Syracuse random variables (legacy L4, Tao's Proposition 1.17 and §§3–4). The side lane pointed out (feed 2026-10-18 19:39) that the audited library behind [`lau-2026-positive-density`](../../../sources/lau-2026-positive-density.md) already proves an explicit mixing estimate inside its own chain, machine-checked with standard axioms ([`lau-density-formal-replay`](../results/lau-density-formal-replay/README.md), its §3.2 "The analytic input is explicit and lies inside the development"). So the constants could be read off the Lean statements instead of being re-derived from Tao v7.

This is a **calibration of a machine-checked source**. The statements below are quoted from the pinned Lean library `AxiomMath/CollatzPositiveDensity` @ `3a38bfbb70379e051b51155def1423846fab3a90`, which builds with standard axioms (the lane-3 audit, PR stgoa/collatz#2, now [`lean/audit/`](../../../lean/audit/README.md)). Nothing is re-derived here; the consequence drawn for `C(δ)` is a comparison of orders of magnitude, not a theorem about Tao's own constants.

## What happened

The statements (file, Lean name, content):

1. **Primitive Fourier decay**: `CollatzPosDens/FourierDecay/ChPrimitiveDecay.lean`, `norm_refLawDft_le_Cstar_div_rpow`: for every `n >= 1` and every unit `ξ` of the residue group mod `3^n`,

   ```
   ‖μ̂_n(ξ)‖ <= C_* / n^(10241/4096),      C_* = (160 D_*)^(10241/4096)
   ```

   (`FourierDecay/ChPrimCoeff.lean`, `Cstar_def`). The exponent `10241/4096 = 2.50024…` is a polynomial decay rate in the 3-adic level `n`, not in a digit count.

2. **The renewal threshold `D_*`**: `CollatzPosDens/Transfer/Dstar.lean`: `D_* = max(D_1, D_pt, D_exp, D_bad, D_sc, 1, 2) ∈ ℚ`. The file's own implementation note says that `D_exp`, `D_bad` and `D_sc` are numbers with thousands of digits, and that `D_*` is used only through the lemmas of that file, never by evaluation. So `C_*` has thousands of digits as well.

3. **Mixing lemma**: `CollatzPosDens/Mixing/Mixing.lean`, `residueAvg_abs_refDensity_sub_le_of_two_pow_le`: for integers `2^80000 <= m <= q`,

   ```
   ⟨ |ρ_q − ρ_m ∘ π_(q,m)| ⟩_q <= 2C / (3 m^(3/2)),
   C = (477/20)·(3200 D_*)^(10241/4096) + 159/10
   ```

   (`Transfer/MixingConst.lean`, `Transfer/X.lean`: `X_* = 3200 D_*`). The hypothesis `2^80000 <= m` is a *lower bound on the 3-adic level*: the statement says nothing about moduli `3^m` with fewer than `2^80000` ternary digits.

4. **Generation threshold**: `Recipe/NValue.lean`, `generationThreshold_eq : N_* = 6103914`; `Seed/ZTail.lean` applies the central-increment bound only for `n >= N_*`.

5. **Public endpoints**: `Main/Main.lean`: density `c_ch = 1/2^2^2^87640` for `N >= X_ch = 2^2^2^2^87640` (the challenge constants).

The statements were read from a local clone of the pinned commit used for the lane-3 build; the file hashes are in the audit's receipt [`lean/audit/receipts/pinned_source_hashes.txt`](../../../lean/audit/receipts/pinned_source_hashes.txt), and the four theorems depending on them are machine-checked there with axioms `[propext, Classical.choice, Quot.sound]`.

## Why it fails

- In this proof, 3-adic mixing is only available at levels `m >= 2^80000`. Any threshold `C(δ)` assembled from these lemmas is therefore at least of the order of `3^(2^80000)` (a number with about `10^24000` digits; the side lane's check gives about `10^24082`) for every `δ`, before the generation count `N_* = 6,103,914` and the thousands-of-digits constants are even applied. The verified range is `V = 2^68 ≈ 3·10^20` in the lane's figure (`2^71` in [`barina-2025-convergence-2-71`](../../../sources/barina-2025-convergence-2-71.md)). The gap is not a factor; it is an iterated exponential.
- Consequently the machine-checked route contributes exactly one row to the `C(δ)` table of [`explicit-almost-all-descent-threshold`](../questions/explicit-almost-all-descent-threshold.md): `C(δ) = 1` (reaching 1 itself) for `δ = 1 − 2^(−2^(2^87640))`, natural density, valid for `N >= X_ch`. It contributes nothing for `δ ∈ {0.9, 0.5, 0.1, 0.01}`.
- The AI-generated formal proof optimised for provability, not constants: polynomial Fourier decay with a thousands-of-digits coefficient, and a level gate of `2^80000`.

## What survives

- **The question it sharpened.** Tao's own analysis (v7, Remark 1.4) suggests a threshold of the form `exp(δ^(−O(1)))`, a single exponential, with an unspecified exponent. The lane asked: what does Tao's Proposition 1.17 / §3 give with every constant traced, and is its `O(1)` small enough that `exp(δ^(−O(1))) <= 2^68 ≈ e^47` for some `δ < 1`? For `δ = 1/2` that requires `2^(O(1)) <= 47`, an exponent below about 5.6; for `δ = 0.9`, `(10/9)^(O(1)) <= 47`, an exponent below about 36. The next unit answered it negatively for the proof as printed: [`tao-printed-window-vacuity`](../results/tao-printed-window-vacuity/README.md) shows that the exponent is irrelevant at the verified scale, because the auxiliary windows are empty there.
- **d-control.** All quoted statements are about the 3-adic reference laws of the `3x+1` renewal process; their `3x+5` analogues would have to be restated (the reference density changes with the additive constant), so this calibration makes no transfer claim. The mixing constants are `d`-blind in kind, as expected of an averaging estimate.
- The conditional reconstruction [`predecessor-density-conditional-reconstruction`](../results/predecessor-density-conditional-reconstruction/README.md) uses Tao's mixing with unspecified constants; the formal library proves explicit ones, and this node records how large they are.

## History

- Migrated from `experiments/explicit_tao/lemmas/L4_formal_constants.md` ("L4, part 0"; alias `TAO-L4-b`) at commit `be73a66`. Lightly edited: sections, links, and the local filesystem path of the clone replaced by a description.
- Written by the Claude explicit-Tao lane (branch `claude/explicit-tao`), iteration 1, 2026-10-18, on a lead from the side lane (feed 19:39) that built on the main lane's `lau_scope.md` §3.2 (legacy `experiments/phase6/linear_density_audit/`, now [`lau-density-formal-replay`](../results/lau-density-formal-replay/README.md)).
