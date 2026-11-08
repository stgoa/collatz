import LeanLane.Words

/-!
# Signed endpoints and antiperiodic intercept divisibility

The central theorem of `antiperiodic-intercept-nondivisibility`.
All endpoints and intercepts are integers; the word entries are natural
numbers. The results therefore also cover the positive valuation words
used by the node. No orbit convergence hypothesis is used.
-/

namespace LeanLane.SignedIntercept

open LeanLane.Words

theorem C_nonneg (w : List ℕ) : 0 ≤ C w := by
  induction w with
  | nil => simp [C]
  | cons a w ih =>
    simp only [C]
    positivity

theorem C_pos {w : List ℕ} (hw : w ≠ []) : 0 < C w := by
  cases w with
  | nil => exact False.elim (hw rfl)
  | cons a w =>
    have := C_nonneg w
    simp only [C]
    positivity

/-- An integer endpoint of a word starting at a negative integer is negative.
The proof obtains an integer at each successive cut by cancelling an odd
power of 3 from divisibility by a power of 2. -/
theorem negative_endpoint (w : List ℕ) {x y : ℤ} (hx : x < 0)
    (h : (2 : ℤ) ^ w.sum * y = 3 ^ w.length * x + C w) : y < 0 := by
  induction w generalizing x y with
  | nil =>
    simp only [List.sum_nil, List.length_nil, C, pow_zero, one_mul, add_zero] at h
    exact h.symm ▸ hx
  | cons a w ih =>
    have hp : (0 : ℤ) < 2 ^ a := by positivity
    have hcop : IsCoprime (2 : ℤ) 3 := by
      exact ⟨-1, 1, by norm_num⟩
    have he : 2 ^ a * (2 ^ w.sum * y - C w) =
        (3 : ℤ) ^ w.length * (3 * x + 1) := by
      simp only [List.sum_cons, List.length_cons, C, pow_add, pow_succ] at h
      nlinarith [h]
    have hd : (2 : ℤ) ^ a ∣ 3 ^ w.length * (3 * x + 1) :=
      ⟨2 ^ w.sum * y - C w, he.symm⟩
    obtain ⟨z, hz⟩ := (hcop.pow (m := a) (n := w.length)).dvd_of_dvd_mul_left hd
    have hzneg : z < 0 := by
      have hn : 3 * x + 1 < 0 := by omega
      nlinarith
    have htail : (2 : ℤ) ^ w.sum * y = 3 ^ w.length * z + C w := by
      rw [hz] at he
      have he' : 2 ^ a * (2 ^ w.sum * y - C w) =
          2 ^ a * (3 ^ w.length * z) := by nlinarith [he]
      have := mul_left_cancel₀ (ne_of_gt hp) he'
      linarith
    exact ih hzneg htail

/-- No positive combination of the two endpoint multipliers divides a
nonempty word's intercept. -/
theorem not_dvd_intercept (w : List ℕ) (hw : w ≠ [])
    (s t : ℤ) (hs : 0 < s) (ht : 0 < t) :
    ¬ ((2 : ℤ) ^ w.sum * t + 3 ^ w.length * s) ∣ C w := by
  intro hd
  obtain ⟨k, hk⟩ := hd
  have hc := C_pos hw
  have hp : (0 : ℤ) < 2 ^ w.sum * t + 3 ^ w.length * s := by positivity
  have hkpos : 0 < k := by nlinarith
  have hx : -s * k < 0 := by nlinarith
  have he : (2 : ℤ) ^ w.sum * (t * k) =
      3 ^ w.length * (-s * k) + C w := by rw [hk]; ring
  have hn := negative_endpoint w hx he
  have : 0 < t * k := mul_pos ht hkpos
  omega

theorem not_dvd_power_plus (w : List ℕ) (hw : w ≠ []) (j : ℕ) :
    ¬ ((2 : ℤ) ^ (w.sum + j) + 3 ^ w.length) ∣ C w := by
  have h := not_dvd_intercept w hw 1 (2 ^ j) (by norm_num) (by positivity)
  simpa only [pow_add, mul_one] using h

#print axioms negative_endpoint
#print axioms not_dvd_intercept
#print axioms not_dvd_power_plus

end LeanLane.SignedIntercept
