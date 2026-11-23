import LeanLane.Words

/-!
# `LeanLane.HalfPeriodSUnit`: the algebraic core of the half-period S-unit approximation law

Formal companion of sections 2, 3 and 8 of
`areas/cycles/results/half-period-s-unit-approximation-law/README.md`.

A cycle of the odd-only `3x+d` map with valuation word `A B A[p] B[q]` has states `x, z, y, t` before its four
blocks. With `a, b` the lengths of `A, B`, `sA, sB` their totals and `CA, CB` their intercepts, the block
equations are the four fields of `Blocks`. Everything here is integer algebra on those four equations.

* `exists_h`, `exists_j`: the paired quotients `h`, `j` exist, with `y - x = 2^sA h`, `2^p t - z = 3^a h`,
  `z - t = 2^sB j`, `y - 2^q x = 3^b j`.
* `h_pos`: `h > 0` for positive states and `p, q ≥ 1`.
* `intercept_identity` and `p_lt_q_of_j_neg`: identity (3) of the node, and `j < 0` implies `p < q`.
* `identity_I`, `identity_II`: the two exact identities (4) and (5).
* `theta_I_lt`, `theta_II_lt`: the bounds (6).
* `isolated`: the approximation step of section 8, in integer form.

The gap estimate of the node (which uses EXT-1, logarithms and the placement of the minimum) is not formalised.
-/

namespace LeanLane
namespace HalfPeriodSUnit

/-- The four block equations of a `3x+d` cycle with word `A B A[p] B[q]`. -/
structure Blocks (a b sA sB p q : ℕ) (d CA CB x z y t : ℤ) : Prop where
  eA : 2 ^ sA * z = 3 ^ a * x + d * CA
  eB : 2 ^ sB * y = 3 ^ b * z + d * CB
  eAp : 2 ^ (sA + p) * t = 3 ^ a * y + d * CA
  eBq : 2 ^ (sB + q) * x = 3 ^ b * t + d * CB

variable {a b sA sB p q : ℕ} {d CA CB x z y t : ℤ}

private theorem coprime_three_two (m n : ℕ) : IsCoprime ((3 : ℤ) ^ m) ((2 : ℤ) ^ n) :=
  IsCoprime.pow ⟨1, -1, by norm_num⟩

private theorem two_le_two_pow {n : ℕ} (hn : 1 ≤ n) : (2 : ℤ) ≤ 2 ^ n := by
  calc (2 : ℤ) = 2 ^ 1 := by norm_num
    _ ≤ 2 ^ n := pow_le_pow_right₀ (by norm_num) hn

/-- The paired quotient `h`: `y - x = 2^sA h` and `2^p t - z = 3^a h`. -/
theorem exists_h (hb : Blocks a b sA sB p q d CA CB x z y t) :
    ∃ h : ℤ, y - x = 2 ^ sA * h ∧ 2 ^ p * t - z = 3 ^ a * h := by
  have key : (2 : ℤ) ^ sA * (2 ^ p * t - z) = 3 ^ a * (y - x) := by
    linear_combination hb.eAp - hb.eA
  have hdvd : (3 : ℤ) ^ a ∣ 2 ^ p * t - z :=
    (coprime_three_two a sA).dvd_of_dvd_mul_left ⟨y - x, key⟩
  obtain ⟨h, hh⟩ := hdvd
  refine ⟨h, ?_, hh⟩
  have h3 : (3 : ℤ) ^ a ≠ 0 := by positivity
  have : (3 : ℤ) ^ a * (y - x) = 3 ^ a * (2 ^ sA * h) := by rw [← key, hh]; ring
  exact mul_left_cancel₀ h3 this

/-- The paired quotient `j`: `z - t = 2^sB j` and `y - 2^q x = 3^b j`. -/
theorem exists_j (hb : Blocks a b sA sB p q d CA CB x z y t) :
    ∃ j : ℤ, z - t = 2 ^ sB * j ∧ y - 2 ^ q * x = 3 ^ b * j := by
  have key : (2 : ℤ) ^ sB * (y - 2 ^ q * x) = 3 ^ b * (z - t) := by
    linear_combination hb.eB - hb.eBq
  have hdvd : (3 : ℤ) ^ b ∣ y - 2 ^ q * x :=
    (coprime_three_two b sB).dvd_of_dvd_mul_left ⟨z - t, key⟩
  obtain ⟨j, hj⟩ := hdvd
  refine ⟨j, ?_, hj⟩
  have h3 : (3 : ℤ) ^ b ≠ 0 := by positivity
  have : (3 : ℤ) ^ b * (z - t) = 3 ^ b * (2 ^ sB * j) := by rw [← key, hj]; ring
  exact mul_left_cancel₀ h3 this

/-- `h` is positive for positive states and `p, q ≥ 1`. -/
theorem h_pos {h j : ℤ} (hx : 0 < x) (ht : 0 < t) (hp : 1 ≤ p) (hq : 1 ≤ q)
    (hh1 : y - x = 2 ^ sA * h) (hh2 : 2 ^ p * t - z = 3 ^ a * h)
    (hj1 : z - t = 2 ^ sB * j) (hj2 : y - 2 ^ q * x = 3 ^ b * j) : 0 < h := by
  by_contra hneg
  rw [not_lt] at hneg
  have e2 : (2 : ℤ) ≤ 2 ^ q := two_le_two_pow hq
  have e3 : (2 : ℤ) ≤ 2 ^ p := two_le_two_pow hp
  have h1 : y - x ≤ 0 := by
    rw [hh1]; exact mul_nonpos_of_nonneg_of_nonpos (by positivity) hneg
  have h2 : 2 ^ p * t - z ≤ 0 := by
    rw [hh2]; exact mul_nonpos_of_nonneg_of_nonpos (by positivity) hneg
  have h3 : y - 2 ^ q * x < 0 := by nlinarith
  have hjneg : j < 0 := by
    by_contra hc
    rw [not_lt] at hc
    have : (0 : ℤ) ≤ 3 ^ b * j := mul_nonneg (by positivity) hc
    linarith
  have h4 : z - t < 0 := by
    rw [hj1]; exact mul_neg_of_pos_of_neg (by positivity) hjneg
  nlinarith

/-- Identity (3) of the node: the intercept of `A` in terms of `h` and `j`. -/
theorem intercept_identity (hb : Blocks a b sA sB p q d CA CB x z y t) {h j : ℤ}
    (hh1 : y - x = 2 ^ sA * h) (hh2 : 2 ^ p * t - z = 3 ^ a * h)
    (hj1 : z - t = 2 ^ sB * j) (hj2 : y - 2 ^ q * x = 3 ^ b * j) :
    (2 ^ p - 1) * (2 ^ q - 1) * (d * CA)
      = 3 ^ a * 2 ^ sA * (2 ^ q - 2 ^ p) * h
        + (2 ^ (sA + sB + p) * (2 ^ q - 1) + 3 ^ (a + b) * (2 ^ p - 1)) * j := by
  linear_combination (-((2 : ℤ) ^ p - 1) * (2 ^ q - 1)) * hb.eA
    + (2 : ℤ) ^ sA * (2 ^ q - 1) * (hh2 + 2 ^ p * hj1)
    - (3 : ℤ) ^ a * (2 ^ p - 1) * (hh1 - hj2)

/-- `j < 0` forces `p < q`. -/
theorem p_lt_q_of_j_neg (hb : Blocks a b sA sB p q d CA CB x z y t) {h j : ℤ}
    (hh1 : y - x = 2 ^ sA * h) (hh2 : 2 ^ p * t - z = 3 ^ a * h)
    (hj1 : z - t = 2 ^ sB * j) (hj2 : y - 2 ^ q * x = 3 ^ b * j)
    (hCA : 0 < d * CA) (hh : 0 < h) (hj : j < 0) (hp : 1 ≤ p) (hq : 1 ≤ q) : p < q := by
  by_contra hle
  rw [not_lt] at hle
  have hid := intercept_identity hb hh1 hh2 hj1 hj2
  have e2 : (2 : ℤ) ≤ 2 ^ q := two_le_two_pow hq
  have e3 : (2 : ℤ) ≤ 2 ^ p := two_le_two_pow hp
  have hpq : (2 : ℤ) ^ q ≤ 2 ^ p := pow_le_pow_right₀ (by norm_num) hle
  have hlhs : 0 < (2 ^ p - 1) * (2 ^ q - 1) * (d * CA) :=
    mul_pos (mul_pos (by linarith) (by linarith)) hCA
  have hfirst : (3 : ℤ) ^ a * 2 ^ sA * (2 ^ q - 2 ^ p) * h ≤ 0 := by
    have h32 : (0 : ℤ) ≤ 3 ^ a * 2 ^ sA := by positivity
    have : (3 : ℤ) ^ a * 2 ^ sA * (2 ^ q - 2 ^ p) ≤ 0 :=
      mul_nonpos_of_nonneg_of_nonpos h32 (by linarith)
    exact mul_nonpos_of_nonpos_of_nonneg this hh.le
  have hbr : (0 : ℤ) < 2 ^ (sA + sB + p) * (2 ^ q - 1) + 3 ^ (a + b) * (2 ^ p - 1) := by
    have h1 : (0 : ℤ) < 2 ^ (sA + sB + p) * (2 ^ q - 1) := mul_pos (by positivity) (by linarith)
    have h2 : (0 : ℤ) < 3 ^ (a + b) * (2 ^ p - 1) := mul_pos (by positivity) (by linarith)
    linarith
  have hsecond : (2 ^ (sA + sB + p) * (2 ^ q - 1) + 3 ^ (a + b) * (2 ^ p - 1)) * j < 0 :=
    mul_neg_of_pos_of_neg hbr hj
  linarith

/-- Identity (4): `3^N h = 2^(sB+p+q) x - 2^sB y - (2^p - 1) d C_B`, with `N = a + b`. -/
theorem identity_I (hb : Blocks a b sA sB p q d CA CB x z y t) {h : ℤ}
    (hh2 : 2 ^ p * t - z = 3 ^ a * h) :
    3 ^ (a + b) * h = 2 ^ (sB + p + q) * x - 2 ^ sB * y - (2 ^ p - 1) * (d * CB) := by
  linear_combination (-(3 : ℤ) ^ b) * hh2 - (2 : ℤ) ^ p * hb.eBq + hb.eB

/-- Identity (5): `2^(sA+p) t = 3^N j + 3^a 2^q x + d C_A`, with `N = a + b`. -/
theorem identity_II (hb : Blocks a b sA sB p q d CA CB x z y t) {j : ℤ}
    (hj2 : y - 2 ^ q * x = 3 ^ b * j) :
    2 ^ (sA + p) * t = 3 ^ (a + b) * j + 3 ^ a * 2 ^ q * x + d * CA := by
  linear_combination hb.eAp + (3 : ℤ) ^ a * hj2

/-- The first bound of (6): `2^sB y + (2^p - 1) d C_B < 2^(sB+p) y`. -/
theorem theta_I_lt (hb : Blocks a b sA sB p q d CA CB x z y t) (hz : 0 < z) (hp : 1 ≤ p) :
    2 ^ sB * y + (2 ^ p - 1) * (d * CB) < 2 ^ (sB + p) * y := by
  have e3 : (2 : ℤ) ≤ 2 ^ p := two_le_two_pow hp
  have hlt : d * CB < 2 ^ sB * y := by
    have : (0 : ℤ) < 3 ^ b * z := mul_pos (by positivity) hz
    linarith [hb.eB]
  have : (2 ^ p - 1) * (d * CB) < (2 ^ p - 1) * (2 ^ sB * y) :=
    mul_lt_mul_of_pos_left hlt (by linarith)
  rw [pow_add]
  nlinarith

/-- The second bound of (6): `3^a 2^q x + d C_A < 2^(sA+q) z`. -/
theorem theta_II_lt (hb : Blocks a b sA sB p q d CA CB x z y t) (hCA : 0 < d * CA) (hq : 1 ≤ q) :
    3 ^ a * 2 ^ q * x + d * CA < 2 ^ (sA + q) * z := by
  have e2 : (2 : ℤ) ≤ 2 ^ q := two_le_two_pow hq
  have : 2 ^ (sA + q) * z = 2 ^ q * (3 ^ a * x + d * CA) := by
    rw [← hb.eA]; ring
  rw [this]
  nlinarith

/-- The approximation step of section 8 in integer form. If `0 < Θ = 2^c U - 3^N V` and a fraction `P'/Q'`
different from `V/U` is at least as close to `2^c/3^N` as `V/U`, then `3^N ≤ 2 Θ Q'`. -/
theorem isolated (c N : ℕ) {U V P' Q' Θ : ℤ} (hU : 0 < U)
    (hΘ : Θ = 2 ^ c * U - 3 ^ N * V) (hne : P' * U ≠ V * Q')
    (hclose : |2 ^ c * Q' - 3 ^ N * P'| * U ≤ Θ * Q') : (3 : ℤ) ^ N ≤ 2 * Θ * Q' := by
  have hkey : (3 : ℤ) ^ N * (P' * U - V * Q') = Q' * Θ - U * (2 ^ c * Q' - 3 ^ N * P') := by
    rw [hΘ]; ring
  have hone : (1 : ℤ) ≤ |P' * U - V * Q'| := by
    have : P' * U - V * Q' ≠ 0 := sub_ne_zero.mpr hne
    exact Int.one_le_abs this
  have h3 : (0 : ℤ) < 3 ^ N := by positivity
  have habs : (3 : ℤ) ^ N * |P' * U - V * Q'| = |Q' * Θ - U * (2 ^ c * Q' - 3 ^ N * P')| := by
    rw [← hkey, abs_mul, abs_of_pos h3]
  have htri : |Q' * Θ - U * (2 ^ c * Q' - 3 ^ N * P')|
      ≤ |Q' * Θ| + |U * (2 ^ c * Q' - 3 ^ N * P')| := abs_sub _ _
  have hΘnn : 0 ≤ Θ * Q' := le_trans (mul_nonneg (abs_nonneg _) hU.le) hclose
  have hb1 : |Q' * Θ| = Θ * Q' := by rw [mul_comm, abs_of_nonneg hΘnn]
  have hb2 : |U * (2 ^ c * Q' - 3 ^ N * P')| = |2 ^ c * Q' - 3 ^ N * P'| * U := by
    rw [abs_mul, abs_of_pos hU, mul_comm]
  have hle : (3 : ℤ) ^ N ≤ 3 ^ N * |P' * U - V * Q'| := by nlinarith
  linarith

end HalfPeriodSUnit
end LeanLane

#print axioms LeanLane.HalfPeriodSUnit.exists_h
#print axioms LeanLane.HalfPeriodSUnit.exists_j
#print axioms LeanLane.HalfPeriodSUnit.h_pos
#print axioms LeanLane.HalfPeriodSUnit.intercept_identity
#print axioms LeanLane.HalfPeriodSUnit.p_lt_q_of_j_neg
#print axioms LeanLane.HalfPeriodSUnit.identity_I
#print axioms LeanLane.HalfPeriodSUnit.identity_II
#print axioms LeanLane.HalfPeriodSUnit.theta_I_lt
#print axioms LeanLane.HalfPeriodSUnit.theta_II_lt
#print axioms LeanLane.HalfPeriodSUnit.isolated
