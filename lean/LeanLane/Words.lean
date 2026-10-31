import Mathlib

/-!
# `LeanLane.Words`: shared definitions for valuation words

The definitions of `CycleSpectrum.lean` (`C`, `D`) for the standalone files that import this module, the two
factors `Φ₁ = 2^S − 3^n`, `Φ₂ = 2^S + 3^n` of `D` for a doubled word, and the parity and gcd facts about them.
Nothing here is a result of its own; the results live in the files that import it.
-/

namespace LeanLane
namespace Words

/-- `C_z`: `C_[] = 0`, `C_(a :: z) = 3^|z| + 2^a C_z`. -/
def C : List ℕ → ℤ
  | [] => 0
  | a :: z => 3 ^ z.length + 2 ^ a * C z

/-- `D_z = 2^{Σz} − 3^{|z|}`. -/
def D (z : List ℕ) : ℤ := 2 ^ z.sum - 3 ^ z.length

/-- `Φ₁ = 2^S − 3^n`. -/
def Phi1 (S n : ℕ) : ℤ := 2 ^ S - 3 ^ n

/-- `Φ₂ = 2^S + 3^n`. -/
def Phi2 (S n : ℕ) : ℤ := 2 ^ S + 3 ^ n

/-- The number of positions in which `z` differs from its rotation by `h` (indices modulo the length). -/
def mismatches (z : List ℕ) (h : ℕ) : ℕ :=
  (List.range z.length).countP fun i => z.getD i 0 ≠ z.getD ((i + h) % z.length) 0

theorem C_append (u v : List ℕ) : C (u ++ v) = 3 ^ v.length * C u + 2 ^ u.sum * C v := by
  induction u with
  | nil => simp [C]
  | cons a u ih =>
    simp only [List.cons_append, C, List.length_append, List.sum_cons, ih]
    ring

theorem odd_Phi1 (S n : ℕ) (hS : 0 < S) : Odd (Phi1 S n) := by
  unfold Phi1
  exact (Int.even_pow.mpr ⟨even_two, hS.ne'⟩).sub_odd (Odd.pow ⟨1, by norm_num⟩)

theorem odd_Phi2 (S n : ℕ) (hS : 0 < S) : Odd (Phi2 S n) := by
  unfold Phi2
  exact (Int.even_pow.mpr ⟨even_two, hS.ne'⟩).add_odd (Odd.pow ⟨1, by norm_num⟩)

theorem Phi2_pos (S n : ℕ) : 0 < Phi2 S n := by
  unfold Phi2; positivity

theorem Phi1_ne_zero (S n : ℕ) (hS : 0 < S) : Phi1 S n ≠ 0 := by
  obtain ⟨k, hk⟩ := odd_Phi1 S n hS
  intro h0
  rw [h0] at hk
  omega

theorem Phi1_cast_ne_zero (S n : ℕ) (hS : 0 < S) : ((Phi1 S n : ℤ) : ℚ) ≠ 0 :=
  Int.cast_ne_zero.mpr (Phi1_ne_zero S n hS)

theorem Phi2_cast_ne_zero (S n : ℕ) : ((Phi2 S n : ℤ) : ℚ) ≠ 0 := by
  exact_mod_cast (Phi2_pos S n).ne'

theorem gcd_two_eq_one_of_odd {Φ : ℤ} (h : Odd Φ) : Int.gcd 2 Φ = 1 := by
  obtain ⟨k, hk⟩ := h
  rw [← Int.isCoprime_iff_gcd_eq_one]
  exact ⟨-k, 1, by rw [hk]; ring⟩

/-- A power of a unit modulo `Φ` can be cancelled from a gcd. -/
theorem gcd_pow_mul_left {b Φ : ℤ} (h : Int.gcd b Φ = 1) (t : ℕ) (X : ℤ) :
    Int.gcd (b ^ t * X) Φ = Int.gcd X Φ := by
  induction t with
  | zero => simp
  | succ t ih =>
    rw [pow_succ, mul_comm (b ^ t) b, mul_assoc, Int.gcd_mul_right_left_of_gcd_eq_one h, ih]

theorem gcd_two_pow_mul_left {Φ : ℤ} (h : Odd Φ) (t : ℕ) (X : ℤ) :
    Int.gcd (2 ^ t * X) Φ = Int.gcd X Φ :=
  gcd_pow_mul_left (gcd_two_eq_one_of_odd h) t X

theorem not_three_dvd_Phi1 (S n : ℕ) (hn : 0 < n) : ¬ (3 : ℤ) ∣ Phi1 S n := by
  intro h
  have h3n : (3 : ℤ) ∣ 3 ^ n := dvd_pow_self 3 hn.ne'
  have h2 : (3 : ℤ) ∣ 2 ^ S := by
    have := dvd_add h h3n
    unfold Phi1 at this
    simpa using this
  exact absurd (Int.prime_three.dvd_of_dvd_pow h2) (by norm_num)

theorem not_three_dvd_Phi2 (S n : ℕ) (hn : 0 < n) : ¬ (3 : ℤ) ∣ Phi2 S n := by
  intro h
  have h3n : (3 : ℤ) ∣ 3 ^ n := dvd_pow_self 3 hn.ne'
  unfold Phi2 at h
  exact absurd (Int.prime_three.dvd_of_dvd_pow ((dvd_add_left h3n).mp h)) (by norm_num)

theorem gcd_three_Phi1 (S n : ℕ) (hn : 0 < n) : Int.gcd 3 (Phi1 S n) = 1 := by
  rw [← Int.isCoprime_iff_gcd_eq_one]
  exact (Int.prime_three.coprime_iff_not_dvd).mpr (not_three_dvd_Phi1 S n hn)

end Words
end LeanLane
