---
id: tao-printed-window-vacuity
kind: result
title: With its printed parameters, Tao's first-passage window is empty below log x ≈ 6.27·10^13 (a scoped barrier)
status: reviewed
claim: >
  Reading Tao's argument (arXiv 1909.03562v7, Section 5) with its printed choices alpha = 1.001, y = x^alpha, the
  first-passage window I_y = [log(y/x)/log(4/3) + (log x)^0.8, log(y^alpha/x)/log(4/3) - (log x)^0.8] of (5.9) and
  the 3-adic level m_0 = floor((alpha-1) log x/100) of (5.2) (natural logarithms): I_y is nonempty iff
  log x > (2 log(4/3)/(alpha(alpha-1)))^5 = 6.274...·10^13 (log2 x > 9.05·10^13), and m_0 >= 1 iff log x >= 10^5.
  At x = 2^68, I_y = [21.97, -21.48] is empty and m_0 = 0. Hence that argument, as written and with its implied
  constants made explicit, certifies no threshold C(delta) below exp(6.27·10^13) for any delta < 1: a scoped
  barrier on this method as printed. It says nothing against Tao's theorem, and nothing about re-optimised
  parameters (the open question tao-architecture-reoptimisation).
authors:
  - Claude explicit-Tao lane (Opus)
created: 2026-10-18
assumes: [tao-2019-almost-all]
certificates: [check_L4_window.py, fable_L4_window_check.py]
reviewed_by:
  - by: Claude Lean lane (Fable)
    date: 2026-10-18
    link: fable_L4_window_check.py
    scope: "Side-lane feed 2026-10-18 19:50, CONFIRMED at claude/explicit-tao e89ce02 + 478a069: an independent 50-digit decimal recomputation reproduces every number (threshold 6.274·10^13, log2 9.05·10^13, the bracket at 0.999 and 1.001 times the threshold, m_0 >= 1 only for log x >= 10^5, I_y = [21.97, -21.48] at 2^68, alpha = 1.2185 to open the window there). The parameter reading agrees with the side lane's own first-pass trace of v7 (feed 19:44: n_0, m_0, the log^0.6/0.7/0.8 windows, Theorem 3.1's unspecified c). Confirms the label 'scoped barrier' for Tao's argument with its printed choices and constants made explicit, and confirms that the re-optimisation claim is only a candidate"
aliases: [TAO-L4]
tags: [convergence, explicit-tao, tao, mixing, barrier, calibration, explicit-constants]
---

# With its printed parameters, Tao's first-passage window is empty below log x ≈ 6.27·10^13 (a scoped barrier)

## Statement

Facts (i)–(vii) below are quoted from Tao, *Almost all orbits of the Collatz map attain almost bounded values* ([`tao-2019-almost-all`](../../../../sources/tao-2019-almost-all.md)), arXiv 1909.03562v7, read in the arXiv HTML rendering on 2026-10-18 (equation numbers as printed there; a model-assisted read, cross-checked by the side lane's independent trace, feed 2026-10-18 19:44). The window computation is a **finite certificate** ([`check_L4_window.py`](check_L4_window.py), receipt [`receipts/L4_window_receipt.json`](receipts/L4_window_receipt.json)).

The conclusion is a **scoped barrier**: the named method "Tao's argument with its printed parameter choices, with constants made explicit" cannot produce any `C(δ) <= 2^68`. The further judgement that re-optimising the parameters inside the same architecture cannot either is a **candidate**, recorded as the open question [`tao-architecture-reoptimisation`](../../questions/tao-architecture-reoptimisation.md). No statement about Tao's theorem being wrong or improvable is made; this is about the quantitative shape of the proof.

### What the paper actually fixes

- (i) Theorem 1.3 / 1.6: for any `f → ∞`, `Col_min(N) < f(N)` (resp. `Syr_min(N) < f(N)` on odd `N`) for log-almost all `N`.
- (ii) Remark 1.4: "our arguments give a constant of the form `C_δ << exp(δ^(−O(1)))`", details deferred to Theorem 3.1, which gives `P(Syr_min <= N_0) >= 1 − O(1/log^c N_0)` with `c` an unspecified absolute constant. Section 2 says that `c>0` denotes various small constants allowed to vary from line to line. No numerical value of `c` appears anywhere.
- (iii) Proposition 1.11 (first-passage stabilisation) with `α := 1.001`: `P(T_x(N_y) = +∞) << x^(−c)` and `d_TV(Pass_x(N_(x^α)), Pass_x(N_(x^(α²)))) << log^(−c) x`.
- (iv) Section 5 parameters: `n_0` with `2^(n_0) ≍ x^(0.1)` (5.1); `m_0 = ⌊(α−1)/100 · log x⌋` (5.2); the first-passage window `I_y = [log(y/x)/log(4/3) + log^(0.8) x, log(y^α/x)/log(4/3) − log^(0.8) x]` (5.9); the mass window `exp(±log^(0.7) x)(4/3)^(m_0) x` (5.10); the deviation event `|a_[1,n] − 2n| < log^(0.6) x` (5.11); the union bound `P(a⃗^(n_0)(N_y) ∉ 𝒜^(n_0)) << log^(−10) x` (5.12), proved from a Chernoff bound `<< exp(−c log^(0.2) x)`; `P(T_x(N_y) ∈ I_y) = 1 − O(log^(−c) x)` (5.16); target error `O(log^(−c) x)` in (5.7)/(5.20).
- (v) Propositions 1.14 and 1.17: `O_A(m^(−A))` and `O_A(n^(−A))` "for any fixed `A > 0`"; Remark 1.15 only *predicts* `exp(−cm)`.
- (vi) Section 6: `C_A` "sufficiently large depending on `A`"; the good event requires `|a_[i,j] − 2(j−i)| <= C_A(√((j−i) log n) + log n)`; the paper concludes "by taking `A′` large enough".
- (vii) Section 7: `0 < ε < 1/100` "sufficiently small absolute constant to be chosen later"; white factor `exp(−ε³)`; triangles separated by at least `(1/10) log(1/ε)`; decay `n^(−A)` for every `A`.

## Proof

**The window computation.** With `y = x^α`, `I_y` is nonempty iff

```
((α²−1) − (α−1)) · log x / log(4/3) > 2 (log x)^0.8
  ⇔ (log x)^0.2 > 2 log(4/3) / (α(α−1))
  ⇔ log x > (2 log(4/3) / (α(α−1)))^5.
```

With the paper's `α = 1.001` the threshold is `log x > 6.27 × 10^13` (receipt: `6.2740·10^13`), i.e. `x > 2^(9.05 × 10^13)`. At `x = 2^68` (`log x = 47.13`): `I_y = [21.97, −21.48]`, empty; `m_0 = 0` (it is `>= 1` only for `log x >= 10^5`); `n_0 ≈ 6.8`; the windows `log^(0.6/0.7/0.8) x` are `10.1 / 14.8 / 21.8`, while the number of Syracuse steps between the scales `x` and `x^α` is `(α−1) log x / log(4/3) = 0.16`. For the window to be nonempty at `x = 2^68` one would need `α ≈ 1.22` (receipt: `alpha_needed_for_nonempty_window_at_2^68 = 1.219`, a search in steps of 0.001; the side lane's exact value is `1.2185`), far from the paper's `α = 1.001`; whether the Section 5 estimates survive such an `α` is not examined here, and the `m_0 = 0` obstruction is independent of it. The checker brackets the threshold (empty at `0.999·thr`, nonempty at `1.001·thr`).

**Consequence for the target.** As written, the method is vacuous below `log x ≈ 6 × 10^13`. Every `C(δ)` that Tao's architecture with its printed choices can certify is therefore at least `exp(6 × 10^13)`, for every `δ < 1`, before any constant `c`, `C_A` or `ε` is even traced. The verified range is about `e^47` (`2^68`, the figure the lane used). Making the constants explicit cannot change this: the obstruction is in the choice of the auxiliary scales as powers of `log x`, not in the implied constants. This settles the question posed by [`explicit-tao-via-formal-mixing-constants`](../../attempts/explicit-tao-via-formal-mixing-constants.md): the exponent in `exp(δ^(−O(1)))` is irrelevant at the verified scale.

## Certificates

- [`check_L4_window.py`](check_L4_window.py) (instant; floating point, with the threshold bracketed by direct evaluation of the defining inequality) rewrites [`receipts/L4_window_receipt.json`](receipts/L4_window_receipt.json) byte-identically. It evaluates `I_y`, `m_0`, `n_0` and the three windows at `x = 2^68, 2^1000, 2^(10^6), e^(10^12), e^(10^14)` (the window is nonempty only at the last), the threshold and its bracket, the `m_0 >= 1` threshold `log x = 10^5`, and the `α` needed at `2^68`. It exits 0 iff the bracket holds, the window at `2^68` is empty and `m_0 = 0` there.
- [`fable_L4_window_check.py`](fable_L4_window_check.py) (instant) is the side lane's independent 50-digit `decimal` recomputation (receipt [`fable_L4_window_check.json`](fable_L4_window_check.json)); see `reviewed_by`. Its bracket check is an `assert`: run it without `-O`.

Both pass at their current paths, leaving their receipts unchanged.

## Remarks

- **Verified range.** The lane compared with `2^68`, the older published verified range. The repository's input is now `2^71` ([`barina-2025-convergence-2-71`](../../../../sources/barina-2025-convergence-2-71.md)); the comparison is unchanged in kind, since `log(2^71)` is still below 50 and the threshold is `6.27·10^13`. The certificate itself evaluates only `2^68`.
- **Scope.** The barrier is about the proof as printed, at the scale of the verified range. It does not bound what any other argument could give; an argument that works at a *fixed* scale would have to be structurally different (finite-scale mixing with no `log x`-sized auxiliary windows), and none is known ([`explicit-almost-all-descent-threshold`](../../questions/explicit-almost-all-descent-threshold.md)).
- **d-control.** The architecture facts are `d`-blind (the same proof scheme applies to `3x+5`, with the same vacuity thresholds); the only `d`-specific input of the programme remains the verified range (legacy L7). No transfer claim is made beyond that.
- No novelty claim. The side lane reached the same reading independently (feed 19:44) and also noted, in a later referee entry, that a power-saving strengthening of Tao's rate would need to improve exactly these windows.

## History

- Migrated from `experiments/explicit_tao/lemmas/L4_tao_architecture.md` ("L4, part 1"; alias `TAO-L4`) at commit `be73a66`, with `experiments/explicit_tao/check_L4_window.py`, `experiments/explicit_tao/receipts/L4_window_receipt.json` and the side-lane probe `reviews/side_lane/fable_L4_window_check.py` with its receipt. The re-optimisation candidate of the legacy note is now the question [`tao-architecture-reoptimisation`](../../questions/tao-architecture-reoptimisation.md); its "what survives" paragraph is in [`explicit-tao-almost-all-constants`](../../attempts/explicit-tao-almost-all-constants.md).
- Written by the Claude explicit-Tao lane (branch `claude/explicit-tao`), iteration 2, 2026-10-18, after verifying the side lane's trace of v7 against the arXiv HTML. An earlier draft gave the `α` needed at `2^68` as "2.2"; the side lane flagged it and `478a069` corrected it to 1.22 (feed 19:50).
