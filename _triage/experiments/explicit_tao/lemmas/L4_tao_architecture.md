# L4, part 1 — Tao's architecture at the verified scale: a scoped barrier

**Status.** Facts (i)–(vii) below are quoted from Tao, *Almost all orbits of
the Collatz map attain almost bounded values*, arXiv 1909.03562v7, read in
the arXiv HTML rendering on 2026-10-18 (equation numbers as printed there;
a model-assisted read, cross-checked by the side lane's independent trace,
`claude/sidekick` feed). The window computation is a **finite certificate**
(`../check_L4_window.py`, receipt `../receipts/L4_window_receipt.json`).
The conclusion for the programme is a **scoped barrier**: the named method
"Tao's argument with its printed parameter choices, with constants made
explicit" cannot produce any `C(δ) <= 2^68`. The further judgement that
re-optimising the parameters inside the same architecture cannot either is
a **candidate**, argued below but not proved. No statement about Tao's
theorem being wrong or improvable is made; this is about the quantitative
shape of the proof.

## What the paper actually fixes

- (i) Theorem 1.3 / 1.6: for any `f → ∞`, `Col_min(N) < f(N)` (resp.
  `Syr_min(N) < f(N)` on odd `N`) for log-almost all `N`.
- (ii) Remark 1.4: "our arguments give a constant of the form
  `C_δ << exp(δ^(−O(1)))`", details deferred to Theorem 3.1, which gives
  `P(Syr_min <= N_0) >= 1 − O(1/log^c N_0)` with `c` an unspecified absolute
  constant. Section 2: "`c>0` denotes various small constants that are
  allowed to vary from line to line, or even within the same line." No
  numerical value of `c` appears anywhere.
- (iii) Proposition 1.11 (first-passage stabilisation) with `α := 1.001`:
  `P(T_x(N_y) = +∞) << x^(−c)` and
  `d_TV(Pass_x(N_(x^α)), Pass_x(N_(x^(α²)))) << log^(−c) x`.
- (iv) Section 5 parameters: `n_0` with `2^(n_0) ≍ x^(0.1)` (5.1);
  `m_0 = ⌊(α−1)/100 · log x⌋` (5.2); the first-passage window
  `I_y = [log(y/x)/log(4/3) + log^(0.8) x, log(y^α/x)/log(4/3) − log^(0.8) x]`
  (5.9); the mass window `exp(±log^(0.7) x)(4/3)^(m_0) x` (5.10); the
  deviation event `|a_[1,n] − 2n| < log^(0.6) x` (5.11); the union bound
  `P(a⃗^(n_0)(N_y) ∉ 𝒜^(n_0)) << log^(−10) x` (5.12), proved from a
  Chernoff bound `<< exp(−c log^(0.2) x)`; `P(T_x(N_y) ∈ I_y) = 1 −
  O(log^(−c) x)` (5.16); target error `O(log^(−c) x)` in (5.7)/(5.20).
- (v) Propositions 1.14 and 1.17: `O_A(m^(−A))` and `O_A(n^(−A))` "for any
  fixed `A > 0`"; Remark 1.15 only *predicts* `exp(−cm)`.
- (vi) Section 6: `C_A` "sufficiently large depending on `A`"; the good
  event requires `|a_[i,j] − 2(j−i)| <= C_A(√((j−i) log n) + log n)`;
  the paper concludes "by taking `A′` large enough".
- (vii) Section 7: `0 < ε < 1/100` "sufficiently small absolute constant
  to be chosen later"; white factor `exp(−ε³)`; triangles separated by at
  least `(1/10) log(1/ε)`; decay `n^(−A)` for every `A`.

## The window computation (finite certificate)

With `y = x^α`, `I_y` is nonempty iff

```
((α²−1) − (α−1)) · log x / log(4/3) > 2 (log x)^0.8
  ⇔ (log x)^0.2 > 2 log(4/3) / (α(α−1))
  ⇔ log x > (2 log(4/3) / (α(α−1)))^5.
```

With the paper's `α = 1.001` the threshold is `log x > 6.3 × 10^13`, i.e.
`x > 2^(9.1 × 10^13)`. At the verified range `x = 2^68` (`log x = 47.1`):
`I_y = [22.0, −21.5]`, empty; `m_0 = 0` (it is `>= 1` only for
`log x >= 10^5`); `n_0 ≈ 6.8`; the windows `log^(0.6/0.7/0.8) x` are
`10.1 / 14.8 / 21.8`, while the number of Syracuse steps between the scales
`x` and `x^α` is `(α−1) log x / log(4/3) = 0.16`. For the window to be
nonempty at `x = 2^68` one would need `α ≈ 1.22` (receipt:
`alpha_needed_for_nonempty_window_at_2^68 = 1.219`), far from the paper's
`α = 1.001`; whether the Section 5 estimates survive such an `α` is not
examined here, and the `m_0 = 0` obstruction is independent of it. The checker brackets the
threshold exactly (empty at `0.999·thr`, nonempty at `1.001·thr`).

## Consequence for the target

- **As written, the method is vacuous below `log x ≈ 6 × 10^13`.** Every
  `C(δ)` that Tao's architecture with its printed choices can certify is
  therefore at least `exp(6 × 10^13)`, for every `δ < 1`, before any
  constant `c`, `C_A` or `ε` is even traced. The verified range is `e^47`.
  Making the constants explicit cannot change this: the obstruction is in
  the choice of the auxiliary scales as powers of `log x`, not in the
  implied constants. This settles the question posed in part 0: the
  exponent in `exp(δ^(−O(1)))` is irrelevant at the verified scale.
- **Re-optimising inside the architecture (candidate, not proved).** The
  exponents `0.6, 0.7, 0.8, 0.1`, the divisor `100` in `m_0`, and `α` are
  all free choices made for asymptotics. Shrinking them runs into the
  reason they were chosen: the Chernoff window must dominate the
  fluctuation of `a_[1,n]` over the `(α²−1) log x / log(4/3)` steps between
  the scales, the 3-adic level `m_0` must be large enough that the
  `m^(−A)` mixing bound is small with a `C_A`-sized deviation allowance,
  and `log^(−c) x` errors must be summable over the chain of scales
  `x, x^α, x^(α²), …` down to the target. At `log x = 47` there are
  fewer than 200 Syracuse steps between any two scales of interest and a
  deviation allowance of order `C_A(√(n log n) + log n)` already exceeds
  `2n` for moderate `C_A`. My assessment is that no choice of these
  parameters brings the vacuity threshold below `log x ~ 10^3`, i.e.
  `x ~ 2^1500`, and probably not below `10^5`; the side lane's independent
  estimate is `log x` of order `10^12` for the union bound (5.12) as
  written. Either way the target `2^68` is out of reach by orders of
  magnitude in the exponent. A proof of this candidate would need to
  formalise "the architecture" as a parametrised family; that is not
  attempted.
- **What survives.** L2/L3 (explicit one-round descent) are correct and
  explicit; the equivalence "Collatz ⇔ `B` has logarithmic density 0 ⇔
  log-almost all orbits dip below the verified range" (STATE.md) stands and
  is the sharpest honest statement of what is missing; and the d-specific
  step of any such proof has been identified as the verified range itself.
  What does not survive is the hope that an explicit version of the
  existing almost-all theorem meets the verified range: an argument that
  works at a *fixed* scale would have to be structurally different —
  finite-scale mixing with no `log x`-sized auxiliary windows — and no
  such argument is known.

## d-control

The architecture facts are d-blind (the same proof scheme applies to
`3x+5`, with the same vacuity thresholds); the only d-specific input of the
programme remains L7. This note makes no transfer claim beyond that.
