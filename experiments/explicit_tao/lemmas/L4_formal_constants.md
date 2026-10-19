# L4, part 0 — the explicit mixing constants that already exist in machine-checked form

**Status: calibration of a machine-checked source. The statements below are
quoted from the pinned Lean library `AxiomMath/CollatzPositiveDensity` @
`3a38bfbb70379e051b51155def1423846fab3a90`, which builds with standard
axioms (lane-3 audit, PR stgoa/collatz#2). Nothing is re-derived here; the
consequence drawn for `C(δ)` is a comparison of orders of magnitude, not a
theorem about Tao's own constants.** Lead supplied by the side lane
(`claude/sidekick`, feed entry after a244490), building on main's
`experiments/phase6/linear_density_audit/lau_scope.md` §3.2.

## The statements (file, Lean name, content)

1. **Primitive Fourier decay** — `CollatzPosDens/FourierDecay/ChPrimitiveDecay.lean`,
   `norm_refLawDft_le_Cstar_div_rpow`: for every `n >= 1` and every unit
   `ξ` of the residue group mod `3^n`,

   ```
   ‖μ̂_n(ξ)‖ <= C_* / n^(10241/4096),      C_* = (160 D_*)^(10241/4096)
   ```

   (`FourierDecay/ChPrimCoeff.lean`, `Cstar_def`). The exponent
   `10241/4096 = 2.50024…` is a polynomial decay rate in the 3-adic level
   `n`, not in a digit count.

2. **The renewal threshold `D_*`** — `CollatzPosDens/Transfer/Dstar.lean`:
   `D_* = max(D_1, D_pt, D_exp, D_bad, D_sc, 1, 2) ∈ ℚ`. The file's own
   implementation note: "`D_exp`, `D_bad` and `D_sc` are numbers with
   thousands of digits, `D_*` is irreducible and is used only through the
   lemmas of this file, never by evaluation." So `C_*` has thousands of
   digits as well.

3. **Mixing lemma** — `CollatzPosDens/Mixing/Mixing.lean`,
   `residueAvg_abs_refDensity_sub_le_of_two_pow_le`: for integers
   `2^80000 <= m <= q`,

   ```
   ⟨ |ρ_q − ρ_m ∘ π_(q,m)| ⟩_q <= 2C / (3 m^(3/2)),
   C = (477/20)·(3200 D_*)^(10241/4096) + 159/10
   ```

   (`Transfer/MixingConst.lean`, `Transfer/X.lean`: `X_* = 3200 D_*`). The
   hypothesis `2^80000 <= m` is a *lower bound on the 3-adic level*: the
   statement says nothing about moduli `3^m` with fewer than `2^80000`
   ternary digits.

4. **Generation threshold** — `Recipe/NValue.lean`,
   `generationThreshold_eq : N_* = 6103914`; `Seed/ZTail.lean` applies the
   central-increment bound only for `n >= N_*`.

5. **Public endpoints** — `Main/Main.lean`: density `c_ch = 1/2^2^2^87640`
   for `N >= X_ch = 2^2^2^2^87640` (the challenge constants).

## What this means for the explicit-Tao target

- In this proof, 3-adic mixing is only available at levels `m >= 2^80000`.
  Any threshold `C(δ)` assembled from these lemmas is therefore at least of
  the order of `3^(2^80000)` — a number with about `10^24000` digits — for
  every `δ`, before the generation count `N_* = 6,103,914` and the
  thousands-of-digits constants are even applied. The verified range is
  `V = 2^68 ≈ 3·10^20`. The gap is not a factor; it is an iterated
  exponential.
- Consequently the machine-checked route contributes exactly one row to
  the `C(δ)` table: `C(δ) = 1` (reaching 1 itself) for
  `δ = 1 − 2^(−2^(2^87640))`, natural density, valid for `N >= X_ch`. It
  contributes nothing for `δ ∈ {0.9, 0.5, 0.1, 0.01}`.
- The AI-generated formal proof optimised for provability, not constants:
  polynomial Fourier decay with a thousands-of-digits coefficient, and a
  level gate of `2^80000`. Tao's own analysis (v7, Remark 1.4) suggests a
  threshold of the form `exp(δ^(−O(1)))` — a single exponential — but with
  an unspecified exponent. **The L4 question is therefore sharpened: what
  does Tao's Proposition 1.17 / §3 actually give, with every constant
  traced, and is its `O(1)` small enough that `exp(δ^(−O(1))) <= 2^68 ≈
  e^47` for some `δ < 1`?** For `δ = 1/2` that requires the exponent
  `O(1)` to satisfy `2^(O(1)) <= 47`, i.e. an exponent below about 5.6;
  for `δ = 0.9`, `(10/9)^(O(1)) <= 47`, i.e. an exponent below about 36.
  Those are the numbers the next units must beat or fail against.

## d-control

All quoted statements are about the 3-adic reference laws of the `3x+1`
renewal process; their `3x+5` analogues would have to be restated (the
reference density changes with the additive constant), so this calibration
makes no transfer claim. The only d-specific step of the programme remains
L7 (the verified range); the mixing constants are d-blind in kind, as
expected of an averaging estimate.

## Receipt

The quoted statements were read from the local clone of the pinned commit
used for the lane-3 build (`~/lean-audit/src/CollatzPositiveDensity`), file
hashes in `lean/audit/receipts/pinned_source_hashes.txt` on
`claude/lean-audit`; the four theorems depending on them are machine-checked
there with axioms `[propext, Classical.choice, Quot.sound]`.
