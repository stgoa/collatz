import Mathlib

/-!
# Two markers on a constant background: `gcd(C, D) = 4^n − 3^n` and denominator `4^n + 3^n`

Formal companion of `areas/cycles/results/two-marker-constant-background-exact-denominator/README.md`.
`w_n = (1, 2^(n−1), 3, 2^(n−1))`, written with `n = k + 1`: `marker k = (1 :: 2^k) ++ (3 :: 2^k)`.
Definitions of `C` and `D` as in `CycleSpectrum.lean`.
-/

namespace LeanLane
namespace TwoMarker

/-- `C_z`: `C_[] = 0`, `C_(a :: z) = 3^|z| + 2^a C_z`. -/
def C : List ℕ → ℤ
  | [] => 0
  | a :: z => 3 ^ z.length + 2 ^ a * C z

/-- `D_z = 2^{Σz} − 3^{|z|}`. -/
def D (z : List ℕ) : ℤ := 2 ^ z.sum - 3 ^ z.length

theorem C_append (u v : List ℕ) : C (u ++ v) = 3 ^ v.length * C u + 2 ^ u.sum * C v := by
  induction u with
  | nil => simp [C]
  | cons a u ih =>
    simp only [List.cons_append, C, List.length_append, List.sum_cons, ih]
    ring

/-- `k` twos. -/
def rep2 (k : ℕ) : List ℕ := List.replicate k 2

@[simp] theorem rep2_length (k : ℕ) : (rep2 k).length = k := by simp [rep2]

@[simp] theorem rep2_sum (k : ℕ) : (rep2 k).sum = 2 * k := by simp [rep2, mul_comm]

/-- `C_(2^k) = 4^k − 3^k`. -/
theorem C_rep2 (k : ℕ) : C (rep2 k) = 4 ^ k - 3 ^ k := by
  induction k with
  | zero => simp [rep2, C]
  | succ k ih =>
    rw [rep2, List.replicate_succ, C, ← rep2, rep2_length, ih]
    ring

/-- The two-marker word `w_(k+1) = (1, 2^k, 3, 2^k)`. -/
def marker (k : ℕ) : List ℕ := (1 :: rep2 k) ++ (3 :: rep2 k)

theorem marker_length (k : ℕ) : (marker k).length = 2 * (k + 1) := by
  simp [marker]; ring

theorem marker_sum (k : ℕ) : (marker k).sum = 4 * (k + 1) := by
  simp [marker]; ring

/-- The closed form of the intercept, `C = 3^(2n−1) + 2·3^(n−1)(4^n − 3^n) + 4^(n+1)(4^(n−1) − 3^(n−1))`, `n = k + 1`. -/
theorem marker_C (k : ℕ) :
    C (marker k) = 3 ^ (2 * k + 1) + 2 * 3 ^ k * (4 ^ (k + 1) - 3 ^ (k + 1))
      + 4 ^ (k + 2) * (4 ^ k - 3 ^ k) := by
  have hsum : (2 : ℤ) ^ (1 :: rep2 k).sum = 2 * 4 ^ k := by
    rw [List.sum_cons, rep2_sum, pow_add, pow_mul]; norm_num
  rw [marker, C_append, hsum]
  simp only [C, rep2_length, C_rep2, List.length_cons]
  ring

/-- `C` factors through `P = 4^n − 3^n`: `C = P·(4^n + 3^(n−1))`. -/
theorem marker_C_factor (k : ℕ) :
    C (marker k) = (4 ^ (k + 1) - 3 ^ (k + 1)) * (4 ^ (k + 1) + 3 ^ k) := by
  rw [marker_C]; ring

/-- `D = 16^n − 9^n = (4^n − 3^n)(4^n + 3^n)`. -/
theorem marker_D (k : ℕ) :
    D (marker k) = (4 ^ (k + 1) - 3 ^ (k + 1)) * (4 ^ (k + 1) + 3 ^ (k + 1)) := by
  rw [D, marker_sum, marker_length]
  have h4 : (2 : ℤ) ^ (4 * (k + 1)) = (4 ^ (k + 1)) ^ 2 := by
    rw [← pow_mul, show (4 : ℤ) = 2 ^ 2 by norm_num, ← pow_mul]; ring_nf
  have h3 : (3 : ℤ) ^ (2 * (k + 1)) = (3 ^ (k + 1)) ^ 2 := by rw [← pow_mul]; ring_nf
  rw [h4, h3]; ring

theorem P_pos (k : ℕ) : 0 < (4 : ℤ) ^ (k + 1) - 3 ^ (k + 1) := by
  have : (3 : ℤ) ^ (k + 1) < 4 ^ (k + 1) := by gcongr; norm_num
  linarith

theorem gcd_two_eq_one_of_odd {Φ : ℤ} (h : Odd Φ) : Int.gcd 2 Φ = 1 := by
  obtain ⟨m, hm⟩ := h
  rw [← Int.isCoprime_iff_gcd_eq_one]
  exact ⟨-m, 1, by rw [hm]; ring⟩

theorem gcd_pow_mul_left {b Φ : ℤ} (h : Int.gcd b Φ = 1) (t : ℕ) (X : ℤ) :
    Int.gcd (b ^ t * X) Φ = Int.gcd X Φ := by
  induction t with
  | zero => simp
  | succ t ih =>
    rw [pow_succ, mul_comm (b ^ t) b, mul_assoc, Int.gcd_mul_right_left_of_gcd_eq_one h, ih]

/-- `K = 4^n + 3^(n−1)` is coprime to `Q = 4^n + 3^n`. -/
theorem gcd_K_Q (k : ℕ) :
    Int.gcd ((4 : ℤ) ^ (k + 1) + 3 ^ k) (4 ^ (k + 1) + 3 ^ (k + 1)) = 1 := by
  have hQ : (4 : ℤ) ^ (k + 1) + 3 ^ (k + 1) = 2 * 3 ^ k + (4 ^ (k + 1) + 3 ^ k) * 1 := by ring
  rw [hQ, Int.gcd_add_mul_left_right, Int.gcd_comm]
  have hodd : Odd ((4 : ℤ) ^ (k + 1) + 3 ^ k) := by
    have h4 : Even ((4 : ℤ) ^ (k + 1)) := (Int.even_pow.mpr ⟨by decide, Nat.succ_ne_zero k⟩)
    exact h4.add_odd (Odd.pow ⟨1, by norm_num⟩)
  rw [Int.gcd_mul_right_left_of_gcd_eq_one (gcd_two_eq_one_of_odd hodd)]
  have h3 : Int.gcd 3 ((4 : ℤ) ^ (k + 1) + 3 ^ k) = 1 := by
    rw [← Int.isCoprime_iff_gcd_eq_one, Int.prime_three.coprime_iff_not_dvd]
    intro h
    have h3k : (3 : ℤ) ∣ 3 ^ k * 1 := by
      rcases k with _ | k
      · exfalso
        -- `k = 0`: `K = 4 + 1 = 5`, and `3 ∤ 5`.
        norm_num at h
      · exact ⟨3 ^ k, by ring⟩
    have : (3 : ℤ) ∣ 4 ^ (k + 1) := by
      have := (dvd_add_left (by simpa using h3k : (3 : ℤ) ∣ 3 ^ k)).mp h
      exact this
    exact absurd (Int.prime_three.dvd_of_dvd_pow this) (by norm_num)
  simpa using gcd_pow_mul_left h3 k 1

/-- **The cancellation is exactly `P = 4^n − 3^n`.** -/
theorem marker_gcd (k : ℕ) :
    (Int.gcd (C (marker k)) (D (marker k)) : ℤ) = 4 ^ (k + 1) - 3 ^ (k + 1) := by
  rw [marker_C_factor, marker_D, Int.gcd_mul_left, gcd_K_Q, mul_one]
  exact Int.natAbs_of_nonneg (P_pos k).le

/-- **The reduced denominator is exactly `Q = 4^n + 3^n`.** -/
theorem marker_den (k : ℕ) :
    D (marker k) / (Int.gcd (C (marker k)) (D (marker k)) : ℤ) = 4 ^ (k + 1) + 3 ^ (k + 1) := by
  rw [marker_gcd, marker_D]
  exact Int.mul_ediv_cancel_left _ (P_pos k).ne'

/-- The reduced numerator (the cycle minimum) is `K = 4^n + 3^(n−1)`: `19` for `n = 2`, `73` for `n = 3`. -/
theorem marker_num (k : ℕ) :
    C (marker k) / (Int.gcd (C (marker k)) (D (marker k)) : ℤ) = 4 ^ (k + 1) + 3 ^ k := by
  rw [marker_gcd, marker_C_factor]
  exact Int.mul_ediv_cancel_left _ (P_pos k).ne'

/-! ### The rotation by `n` and primitivity -/

/-- The number of positions in which `z` differs from its rotation by `h`. -/
def mism (z : List ℕ) (h : ℕ) : ℕ :=
  (List.zipWith (fun a b => if a = b then 0 else 1) z (z.rotate h)).sum

theorem marker_rotate (k : ℕ) : (marker k).rotate (k + 1) = (3 :: rep2 k) ++ (1 :: rep2 k) := by
  have h : (1 :: rep2 k).length = k + 1 := by simp
  rw [marker, ← h, List.rotate_append_length_eq]

/-- The rotation by `n` differs from `w_n` in exactly two positions (the `1` and the `3`). -/
theorem marker_mism (k : ℕ) : mism (marker k) (k + 1) = 2 := by
  rw [mism, marker_rotate, marker, List.zipWith_append (by simp), List.sum_append]
  simp [rep2]

theorem marker_getElem?_ne_one (k p : ℕ) (hp : 0 < p) (hlt : p < 2 * (k + 1)) :
    (marker k)[p]? ≠ some 1 := by
  rcases Nat.lt_or_ge p (k + 1) with h | h
  · rw [marker, List.getElem?_append_left (by simp; omega)]
    obtain ⟨p', rfl⟩ : ∃ p', p = p' + 1 := ⟨p - 1, by omega⟩
    rw [List.getElem?_cons_succ, rep2, List.getElem?_replicate_of_lt (by omega)]
    decide
  · rw [marker, List.getElem?_append_right (by simp; omega)]
    simp only [List.length_cons, rep2_length]
    rcases Nat.lt_or_ge (k + 1) p with h2 | h2
    · obtain ⟨q, hq⟩ : ∃ q, p - (k + 1) = q + 1 := ⟨p - (k + 1) - 1, by omega⟩
      rw [hq, List.getElem?_cons_succ, rep2, List.getElem?_replicate_of_lt (by omega)]
      decide
    · have h0 : p - (k + 1) = 0 := by omega
      rw [h0]
      simp

/-- `w_n` is primitive: no rotation by `0 < p < 2n` fixes it. -/
theorem marker_primitive (k p : ℕ) (hp : 0 < p) (hlt : p < 2 * (k + 1)) :
    (marker k).rotate p ≠ marker k := by
  intro heq
  have hlen : p < (marker k).length := by rw [marker_length]; exact hlt
  have h0 : ((marker k).rotate p)[0]? = (marker k)[p]? := by
    rw [List.getElem?_rotate (by rw [marker_length]; omega), zero_add, Nat.mod_eq_of_lt hlen]
  rw [heq] at h0
  have h1 : (marker k)[0]? = some 1 := by simp [marker]
  exact marker_getElem?_ne_one k p hp hlt (by rw [← h0]; exact h1)

/-! ### The arcs between the mismatches, and the two worked cycles -/

/-- Both arcs between the mismatches, `(2^(n−1), 3)` and `(2^(n−1), 1)`, have intercept `4^n − 3^n`
(an intercept does not depend on its last letter). -/
theorem arc_C (k x : ℕ) : C (rep2 k ++ [x]) = 4 ^ (k + 1) - 3 ^ (k + 1) := by
  have h : (2 : ℤ) ^ (rep2 k).sum = 4 ^ k := by rw [rep2_sum, pow_mul]; norm_num
  rw [C_append, C_rep2, h]
  simp [C]
  ring

/-- The odd part and 2-adic valuation of `n`, computed with fuel `f ≥ log₂ n`. -/
def oddPart : ℕ → ℕ → ℕ × ℕ
  | 0, n => (n, 0)
  | f + 1, n => if n % 2 = 0 ∧ n ≠ 0 then ((oddPart f (n / 2)).1, (oddPart f (n / 2)).2 + 1) else (n, 0)

/-- One odd-only `3x+q` step: the next odd state and the valuation. -/
def step (q x : ℕ) : ℕ × ℕ := oddPart (3 * x + q) (3 * x + q)

/-- `r` steps of the odd-only `3x+q` map from `x`: the states and the valuation word. -/
def trajectory (q x : ℕ) : ℕ → List ℕ × List ℕ
  | 0 => ([], [])
  | r + 1 =>
    let s := step q x
    let t := trajectory q s.1 r
    (x :: t.1, s.2 :: t.2)

/-- `n = 2`: the reduced cycle `19 → 41 → 37 → 17 → 19` of `3x+25`, with valuation word `w_2 = (1, 2, 3, 2)`. -/
theorem cycle_n2 : trajectory 25 19 4 = ([19, 41, 37, 17], marker 1) ∧ (step 25 17).1 = 19 := by decide

/-- `n = 3`: the reduced cycle `73 → 155 → 139 → 127 → 59 → 67 → 73` of `3x+91`, word `w_3 = (1, 2, 2, 3, 2, 2)`. -/
theorem cycle_n3 : trajectory 91 73 6 = ([73, 155, 139, 127, 59, 67], marker 2) ∧ (step 91 67).1 = 73 := by
  decide

/-- The reduced numerator and denominator at `n = 2` and `n = 3` are the minima and moduli of those cycles. -/
theorem reduced_n2 : (4 : ℤ) ^ (1 + 1) + 3 ^ 1 = 19 ∧ (4 : ℤ) ^ (1 + 1) + 3 ^ (1 + 1) = 25 := by norm_num

theorem reduced_n3 : (4 : ℤ) ^ (2 + 1) + 3 ^ 2 = 73 ∧ (4 : ℤ) ^ (2 + 1) + 3 ^ (2 + 1) = 91 := by norm_num

end TwoMarker
end LeanLane

#print axioms LeanLane.TwoMarker.marker_C
#print axioms LeanLane.TwoMarker.marker_C_factor
#print axioms LeanLane.TwoMarker.marker_D
#print axioms LeanLane.TwoMarker.marker_gcd
#print axioms LeanLane.TwoMarker.marker_den
#print axioms LeanLane.TwoMarker.marker_num
#print axioms LeanLane.TwoMarker.marker_mism
#print axioms LeanLane.TwoMarker.marker_primitive
#print axioms LeanLane.TwoMarker.marker_rotate
#print axioms LeanLane.TwoMarker.arc_C
#print axioms LeanLane.TwoMarker.cycle_n2
#print axioms LeanLane.TwoMarker.cycle_n3
#print axioms LeanLane.TwoMarker.reduced_n2
#print axioms LeanLane.TwoMarker.reduced_n3
