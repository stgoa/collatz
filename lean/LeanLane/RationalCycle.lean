import LeanLane.CycleEquation

/-!
# Every word with `D_w > 0` is the valuation word of an actual `3x+den(w)` cycle

Formal companion of the converse half of the cycle equation in
`areas/cycles/results/doubled-word-cancellation-formula/README.md` (NOTATION.md §2).

The rotation identity `2^(a_0) · C_(R_1 w) = 3 · C_w + D_w` shows that the odd common divisors of `C_w` and `D_w`
divide every rotated intercept; so with `G = gcd(C_w, D_w)` and `q = D_w / G` the integers `x_i = C_(R_i w) / G`
follow `w` under `3x+q`, are `|w|`-periodic, positive, and `gcd(x_0, q) = 1`: the reduced cycle of `w`.
-/

namespace LeanLane
namespace RationalCycle

open LeanLane.Words LeanLane.Doubled LeanLane.CycleEquation

/-- The rotation identity: `2^(a) · C_(w' ++ [a]) = 3 · C_(a :: w') + D_(a :: w')`. -/
theorem rotation_identity (a : ℕ) (w' : List ℕ) :
    2 ^ a * C (w' ++ [a]) = 3 * C (a :: w') + D (a :: w') := by
  rw [C_append, D]
  simp only [C, List.length_cons, List.length_nil, List.sum_cons, pow_add, pow_one, mul_zero, add_zero]
  ring

theorem rotate_one_cons (a : ℕ) (w' : List ℕ) : (a :: w').rotate 1 = w' ++ [a] := by
  simp [List.rotate_cons_succ]

/-- `2^(w_0) · C_(R_1 w) = 3 · C_w + D_w` for nonempty `w`. -/
theorem rotation_identity' (w : List ℕ) (hw : w ≠ []) :
    2 ^ (w.getD 0 0) * C (w.rotate 1) = 3 * C w + D w := by
  obtain ⟨a, w', rfl⟩ := List.exists_cons_of_ne_nil hw
  rw [rotate_one_cons]
  simpa using rotation_identity a w'

/-- `D` is rotation invariant (restated). -/
theorem D_rotate' (w : List ℕ) (r : ℕ) : D (w.rotate r) = D w := D_rotate w r

/-- An odd common divisor of `C_w` and `D_w` divides `C_(R_1 w)`. -/
theorem dvd_C_rotate_one {w : List ℕ} (hw : w ≠ []) {g : ℤ} (hodd : Odd g) (hC : g ∣ C w) (hD : g ∣ D w) :
    g ∣ C (w.rotate 1) := by
  have h := rotation_identity' w hw
  have h2 : g ∣ 2 ^ (w.getD 0 0) * C (w.rotate 1) := by
    rw [h]; exact dvd_add (dvd_mul_of_dvd_right hC 3) hD
  have hcop : Int.gcd (2 ^ (w.getD 0 0)) g = 1 := by
    have := gcd_pow_mul_left (b := 2) (Φ := g) (gcd_two_eq_one_of_odd hodd) (w.getD 0 0) 1
    simpa using this
  exact Int.dvd_of_dvd_mul_right_of_gcd_one h2 (by rwa [Int.gcd_comm])

/-- An odd common divisor of `C_w` and `D_w` divides every rotated intercept. -/
theorem dvd_C_rotate {w : List ℕ} (hw : w ≠ []) {g : ℤ} (hodd : Odd g) (hC : g ∣ C w) (hD : g ∣ D w) :
    ∀ r, g ∣ C (w.rotate r) := by
  intro r
  induction r with
  | zero => simpa using hC
  | succ r ih =>
    have hw' : w.rotate r ≠ [] := by
      intro h; apply hw; simpa using congrArg List.length h
    have := dvd_C_rotate_one hw' hodd ih (by rwa [D_rotate])
    rwa [List.rotate_rotate] at this

/-- `D_w` is odd and `C_w > 0` for a nonempty word with positive total. -/
theorem odd_D {w : List ℕ} (hS : 0 < w.sum) : Odd (D w) := by
  unfold D
  exact (Int.even_pow.mpr ⟨even_two, hS.ne'⟩).sub_odd (Odd.pow ⟨1, by norm_num⟩)

theorem C_nonneg : ∀ (w : List ℕ), 0 ≤ C w
  | [] => by simp [C]
  | a :: w' => by
    simp only [C]
    have h1 : (0 : ℤ) ≤ 3 ^ w'.length := by positivity
    have h2 : (0 : ℤ) ≤ 2 ^ a * C w' := mul_nonneg (by positivity) (C_nonneg w')
    linarith

theorem C_pos : ∀ (w : List ℕ), w ≠ [] → 0 < C w
  | [], h => absurd rfl h
  | a :: w', _ => by
    simp only [C]
    have h1 : (0 : ℤ) < 3 ^ w'.length := by positivity
    have h2 : (0 : ℤ) ≤ 2 ^ a * C w' := mul_nonneg (by positivity) (C_nonneg w')
    linarith

/-- **The reduced cycle of a word.** For `w ≠ []` with `D_w > 0`, `G = gcd(C_w, D_w)` and `q = D_w / G`, the
integers `x_i = C_(R_i w) / G` form a cycle of `3x+q` along `w` with `x_0 = C_w / G`, `gcd(x_0, q) = 1`, all
states positive, and `G · x_i = C_(R_i w)` exactly. -/
theorem reduced_cycle (w : List ℕ) (hw : w ≠ []) (hD : 0 < D w) :
    IsCycle (D w / Int.gcd (C w) (D w)) w (fun i => C (w.rotate i) / Int.gcd (C w) (D w))
    ∧ (fun i => C (w.rotate i) / Int.gcd (C w) (D w)) 0 = C w / Int.gcd (C w) (D w)
    ∧ Int.gcd (C w / Int.gcd (C w) (D w)) (D w / Int.gcd (C w) (D w)) = 1
    ∧ (∀ i, 0 < C (w.rotate i) / Int.gcd (C w) (D w))
    ∧ (∀ i, (Int.gcd (C w) (D w) : ℤ) * (C (w.rotate i) / Int.gcd (C w) (D w)) = C (w.rotate i))
    ∧ 0 < D w / Int.gcd (C w) (D w) := by
  set G : ℤ := (Int.gcd (C w) (D w) : ℤ) with hG
  set q : ℤ := D w / G with hq
  set x : ℕ → ℤ := fun i => C (w.rotate i) / G with hx
  have hS : 0 < w.sum := by
    by_contra h0
    have : w.sum = 0 := by omega
    have hn : 1 ≤ w.length := List.length_pos_of_ne_nil hw
    have : D w ≤ 0 := by
      unfold D; rw [this, pow_zero]
      have : (1 : ℤ) ≤ 3 ^ w.length := one_le_pow₀ (by norm_num)
      linarith
    linarith
  have hGpos : 0 < G := by
    rw [hG]
    have : 0 < Int.gcd (C w) (D w) := Int.gcd_pos_of_ne_zero_right _ hD.ne'
    exact_mod_cast this
  have hG0 : G ≠ 0 := hGpos.ne'
  have hGodd : Odd G := by
    have hGD : G ∣ D w := Int.gcd_dvd_right _ _
    rcases Int.even_or_odd G with he | ho
    · exfalso
      have : Even (D w) := he.trans_dvd hGD
      exact (Int.not_even_iff_odd.mpr (odd_D hS)) this
    · exact ho
  have hall : ∀ i, G ∣ C (w.rotate i) := dvd_C_rotate hw hGodd (Int.gcd_dvd_left _ _) (Int.gcd_dvd_right _ _)
  have hexact : ∀ i, G * x i = C (w.rotate i) := fun i => Int.mul_ediv_cancel' (hall i)
  have hDq : G * q = D w := Int.mul_ediv_cancel' (Int.gcd_dvd_right _ _)
  refine ⟨⟨?_, ?_⟩, ?_, ?_, ?_, hexact, ?_⟩
  · -- the step relation
    intro i
    have hw' : w.rotate i ≠ [] := by
      intro h; apply hw; simpa using congrArg List.length h
    have hid := rotation_identity' (w.rotate i) hw'
    rw [List.rotate_rotate, D_rotate] at hid
    have hget : (w.rotate i).getD 0 0 = w.getD (i % w.length) 0 := by
      rw [getD_rotate w i 0 (List.length_pos_of_ne_nil hw)]; simp
    rw [hget] at hid
    -- multiply the target by `G`
    apply mul_left_cancel₀ hG0
    rw [show i + 1 = 1 + i from add_comm _ _] at hid
    calc G * (2 ^ (w.getD (i % w.length) 0) * x (i + 1))
        = 2 ^ (w.getD (i % w.length) 0) * (G * x (i + 1)) := by ring
      _ = 2 ^ (w.getD (i % w.length) 0) * C (w.rotate (1 + i)) := by rw [hexact, add_comm]
      _ = 3 * C (w.rotate i) + D w := hid
      _ = 3 * (G * x i) + G * q := by rw [hexact, hDq]
      _ = G * (3 * x i + q) := by ring
  · -- periodicity
    intro i
    show C (w.rotate (i + w.length)) / G = C (w.rotate i) / G
    rw [add_comm, ← List.rotate_rotate, List.rotate_length]
  · simp only [hx, List.rotate_zero]
  · -- coprimality of x 0 and q
    exact Int.gcd_div_gcd_div_gcd (Int.gcd_pos_of_ne_zero_right _ hD.ne')
  · intro i
    have hw' : w.rotate i ≠ [] := by
      intro h; apply hw; simpa using congrArg List.length h
    have hCpos := C_pos _ hw'
    have := hexact i
    nlinarith [this, hCpos, hGpos]
  · have : 0 < G * q := by rw [hDq]; exact hD
    exact pos_of_mul_pos_right this hGpos.le

end RationalCycle
end LeanLane

#print axioms LeanLane.RationalCycle.rotation_identity
#print axioms LeanLane.RationalCycle.dvd_C_rotate
#print axioms LeanLane.RationalCycle.reduced_cycle
