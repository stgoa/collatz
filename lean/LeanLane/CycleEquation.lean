import LeanLane.RotationPairs

/-!
# The cycle equation, and the exact cancellation of a rotation pair of an actual cycle

Formal companion of the rotation-pair instance in `areas/cycles/results/doubled-word-cancellation-formula/README.md`.

A sequence of states `x : ℕ → ℤ` follows the word `w` under the odd-only `3x+q` map when
`2^(w_i) · x_(i+1) = 3 · x_i + q` for every `i` (letters read cyclically), and it is a cycle when it is
`|w|`-periodic. Then `x_0 · D_w = q · C_w` (the cycle equation), the same for every rotation, `q ∣ D_w` when
`gcd(x_0, q) = 1`, and `C_(R_r w) = x_r · (D_w / q)`. With `doubled-word-cancellation-formula` this gives, for
`w' = R_r w ++ R_s w`, `gcd(C_(w'), D_(w')) = (D_w / q) · gcd(x_r + x_s, q) · gcd(x_r − x_s, 2^(Σw) + 3^|w|)`.
-/

namespace LeanLane
namespace CycleEquation

open LeanLane.Words LeanLane.Doubled LeanLane.RotationPairs

/-- Following a finite word: `2^(Σw) x_|w| = 3^|w| x_0 + q C_w`. -/
theorem follow_word (q : ℤ) : ∀ (w : List ℕ) (x : ℕ → ℤ),
    (∀ i, i < w.length → 2 ^ (w.getD i 0) * x (i + 1) = 3 * x i + q) →
    2 ^ w.sum * x w.length = 3 ^ w.length * x 0 + q * C w := by
  intro w
  induction w with
  | nil => intro x _; simp [C]
  | cons a w ih =>
    intro x hx
    have h0 : 2 ^ a * x 1 = 3 * x 0 + q := by simpa using hx 0 (by simp)
    have h1 := ih (fun i => x (i + 1)) (fun i hi => by
      have := hx (i + 1) (by simp; omega)
      simpa [List.getD_cons_succ] using this)
    simp only [List.sum_cons, List.length_cons, C, pow_add]
    calc 2 ^ a * 2 ^ w.sum * x (w.length + 1)
        = 2 ^ a * (2 ^ w.sum * x (w.length + 1)) := by ring
      _ = 2 ^ a * (3 ^ w.length * x 1 + q * C w) := by rw [h1]
      _ = 3 ^ w.length * (2 ^ a * x 1) + q * (2 ^ a * C w) := by ring
      _ = 3 ^ w.length * (3 * x 0 + q) + q * (2 ^ a * C w) := by rw [h0]
      _ = 3 ^ w.length * 3 * x 0 + q * (3 ^ w.length + 2 ^ a * C w) := by ring

/-- A cycle: the states follow the word cyclically and are `|w|`-periodic. -/
structure IsCycle (q : ℤ) (w : List ℕ) (x : ℕ → ℤ) : Prop where
  step : ∀ i, 2 ^ (w.getD (i % w.length) 0) * x (i + 1) = 3 * x i + q
  periodic : ∀ i, x (i + w.length) = x i

theorem getD_rotate (w : List ℕ) (r i : ℕ) (hi : i < w.length) :
    (w.rotate r).getD i 0 = w.getD ((i + r) % w.length) 0 := by
  rw [List.getD_eq_getElem?_getD, List.getD_eq_getElem?_getD, List.getElem?_rotate hi]

/--  is invariant under rotation. -/
theorem D_rotate (w : List ℕ) (r : ℕ) : D (w.rotate r) = D w := by
  simp [D, (List.rotate_perm w r).sum_eq]

/-- The shifted states follow the rotated word. -/
theorem IsCycle.rotate {q : ℤ} {w : List ℕ} {x : ℕ → ℤ} (h : IsCycle q w x) (r : ℕ) :
    IsCycle q (w.rotate r) (fun i => x (i + r)) where
  step i := by
    show 2 ^ ((w.rotate r).getD (i % (w.rotate r).length) 0) * x (i + 1 + r) = 3 * x (i + r) + q
    have hlen : (w.rotate r).length = w.length := List.length_rotate w r
    rcases Nat.eq_zero_or_pos w.length with h0 | hpos
    · have hnil : w = [] := List.eq_nil_of_length_eq_zero h0
      subst hnil
      have := h.step (i + r)
      simpa [List.rotate_nil, add_right_comm] using this
    · rw [hlen, getD_rotate w r (i % w.length) (Nat.mod_lt _ hpos)]
      have := h.step (i + r)
      rw [show (i % w.length + r) % w.length = (i + r) % w.length from by
        rw [Nat.add_mod, Nat.mod_mod, ← Nat.add_mod]]
      rw [add_right_comm]
      exact this
  periodic i := by
    show x (i + (w.rotate r).length + r) = x (i + r)
    rw [List.length_rotate, add_right_comm, h.periodic]

/-- **The cycle equation**: `x_0 · D_w = q · C_w`. -/
theorem IsCycle.cycle_eq {q : ℤ} {w : List ℕ} {x : ℕ → ℤ} (h : IsCycle q w x) :
    x 0 * D w = q * C w := by
  have hf := follow_word q w x (fun i hi => by
    have := h.step i
    rwa [Nat.mod_eq_of_lt hi] at this)
  have hp : x w.length = x 0 := by simpa using h.periodic 0
  rw [hp] at hf
  unfold D
  linear_combination hf

/-- The cycle equation for every rotation: `x_r · D_w = q · C_(R_r w)`. -/
theorem IsCycle.cycle_eq_rotate {q : ℤ} {w : List ℕ} {x : ℕ → ℤ} (h : IsCycle q w x) (r : ℕ) :
    x r * D w = q * C (w.rotate r) := by
  have := (h.rotate r).cycle_eq
  rw [D_rotate] at this
  simpa using this

/-- When the first state is coprime to `q`, `q` divides `D_w`. -/
theorem IsCycle.q_dvd_D {q : ℤ} {w : List ℕ} {x : ℕ → ℤ} (h : IsCycle q w x) (hcop : Int.gcd (x 0) q = 1) :
    q ∣ D w := by
  have := h.cycle_eq
  exact Int.dvd_of_dvd_mul_right_of_gcd_one ⟨C w, by rw [← this]⟩ (by rwa [Int.gcd_comm])

/-- `C_(R_r w) = x_r · (D_w / q)`. -/
theorem IsCycle.C_rotate_eq {q : ℤ} {w : List ℕ} {x : ℕ → ℤ} (h : IsCycle q w x) (hq : q ≠ 0)
    (hcop : Int.gcd (x 0) q = 1) (r : ℕ) : C (w.rotate r) = x r * (D w / q) := by
  obtain ⟨K, hK⟩ := h.q_dvd_D hcop
  have hc := h.cycle_eq_rotate r
  rw [hK, Int.mul_ediv_cancel_left _ hq]
  rw [hK] at hc
  have : q * C (w.rotate r) = q * (x r * K) := by rw [← hc]; ring
  exact mul_left_cancel₀ hq this

/-- **The exact cancellation of a rotation pair.** For a primitive actual `3x+q` cycle (`q > 0`, states
following `w`, `gcd(x_0, q) = 1`, nonempty word with positive total),
`gcd(C_(R_r w ++ R_s w), D_(R_r w ++ R_s w)) = (D_w/q) · gcd(x_r + x_s, q) · gcd(x_r − x_s, 2^(Σw) + 3^|w|)`. -/
theorem rotation_pair_gcd {q : ℤ} {w : List ℕ} {x : ℕ → ℤ} (h : IsCycle q w x) (hq : 0 < q)
    (hcop : Int.gcd (x 0) q = 1) (hw : 0 < w.sum) (hn : 0 < w.length) (r s : ℕ) :
    (Int.gcd (C (w.rotate r ++ w.rotate s)) (D (w.rotate r ++ w.rotate s)) : ℤ)
      = |D w / q| * Int.gcd (x r + x s) q * Int.gcd (x r - x s) (Phi2 w.sum w.length) := by
  have hlen : (w.rotate s).length = (w.rotate r).length := by simp [List.length_rotate]
  have hsum : ∀ t, (w.rotate t).sum = w.sum := fun t => (List.rotate_perm w t).sum_eq
  have hK : Phi1 ((w.rotate r).sum + 0) (w.rotate r).length = q * (D w / q) := by
    rw [hsum, List.length_rotate, add_zero, Phi1]
    obtain ⟨K, hK⟩ := h.q_dvd_D hcop
    rw [show D w = q * K from hK, Int.mul_ediv_cancel_left _ hq.ne']
    unfold D at hK; linarith [hK]
  have := gcd_D_of_common_factor (w.rotate r) (w.rotate s) 0 (D w / q) q (x r) (x s) hlen
    (by rw [hsum, hsum]; ring) (by rw [hsum]; simpa using hw) (by rw [List.length_rotate]; exact hn) hK
    (h.C_rotate_eq hq.ne' hcop r) (h.C_rotate_eq hq.ne' hcop s)
  simpa [hsum, List.length_rotate] using this

end CycleEquation
end LeanLane

#print axioms LeanLane.CycleEquation.follow_word
#print axioms LeanLane.CycleEquation.D_rotate
#print axioms LeanLane.CycleEquation.IsCycle.rotate
#print axioms LeanLane.CycleEquation.IsCycle.cycle_eq
#print axioms LeanLane.CycleEquation.IsCycle.cycle_eq_rotate
#print axioms LeanLane.CycleEquation.IsCycle.q_dvd_D
#print axioms LeanLane.CycleEquation.IsCycle.C_rotate_eq
#print axioms LeanLane.CycleEquation.rotation_pair_gcd
