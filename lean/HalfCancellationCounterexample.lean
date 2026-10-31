import Mathlib

/-!
# The half-cancellation bound fails at four mismatches: the explicit word, machine-checked

Formal companion of `areas/cycles/results/half-cancellation-counterexample-rotation-pair/README.md`.
For the word `w = (1,1,1,1,6,1,5,1,1,2,1,5,1,1,2,1,1,1,1,6)` (length 20, total 40):
`C_w = 655517108785`, `D_w = 2^40 − 3^20 = 1096024843375`, `gcd(C_w, D_w) = 4947635 = 5·(2^20 − 3^10)`,
`gcd(C_w, D_w)^2 > 2^40`, the rotation by 5 differs from `w` in exactly four positions, every nonidentity
rotation differs in at least four, and `w` is primitive. Definitions of `C` and `D` as in `CycleSpectrum.lean`.
-/

namespace LeanLane
namespace HalfCancellationCounterexample

/-- `C_z`: `C_[] = 0`, `C_(a :: z) = 3^|z| + 2^a C_z`. -/
def C : List ℕ → ℤ
  | [] => 0
  | a :: z => 3 ^ z.length + 2 ^ a * C z

/-- `D_z = 2^{Σz} − 3^{|z|}`. -/
def D (z : List ℕ) : ℤ := 2 ^ z.sum - 3 ^ z.length

/-- The number of positions in which `z` differs from its rotation by `h`. -/
def mismatches (z : List ℕ) (h : ℕ) : ℕ :=
  (List.range z.length).countP fun i => z.getD i 0 ≠ z.getD ((i + h) % z.length) 0

/-- The counterexample word `a·b·b·a`, `a = (1,1,1,1,6)`, `b = (1,5,1,1,2)`. -/
def w : List ℕ := [1, 1, 1, 1, 6, 1, 5, 1, 1, 2, 1, 5, 1, 1, 2, 1, 1, 1, 1, 6]

theorem w_length : w.length = 20 := by decide

theorem w_sum : w.sum = 40 := by decide

theorem w_C : C w = 655517108785 := by norm_num [C, w]

theorem w_D : D w = 1096024843375 := by norm_num [D, w]

theorem w_D_factor : D w = (2 ^ 20 - 3 ^ 10) * (2 ^ 20 + 3 ^ 10) := by rw [w_D]; norm_num

theorem w_gcd : Int.gcd (C w) (D w) = 4947635 := by rw [w_C, w_D]; norm_num

theorem w_gcd_factor : (4947635 : ℤ) = 5 * (2 ^ 20 - 3 ^ 10) := by norm_num

/-- The half bound fails: `G^2 > 2^A`. -/
theorem w_violates_half_bound : (2 : ℤ) ^ w.sum < (Int.gcd (C w) (D w) : ℤ) ^ 2 := by
  rw [w_gcd, w_sum]; norm_num

/-- The rotation by 5 has exactly four mismatches ... -/
theorem w_mismatches_five : mismatches w 5 = 4 := by decide

/-- ... and no nonidentity rotation has fewer: `ρ(w) = 4`. -/
theorem w_rotation_distance : ∀ h < 20, 0 < h → 4 ≤ mismatches w h := by decide

/-- `w` is primitive: no proper period. -/
theorem w_primitive : ∀ p < 20, 0 < p → 20 % p = 0 → 0 < mismatches w p := by decide

/-- `D_w > 0`. -/
theorem w_D_pos : 0 < D w := by rw [w_D]; norm_num

end HalfCancellationCounterexample
end LeanLane

#print axioms LeanLane.HalfCancellationCounterexample.w_C
#print axioms LeanLane.HalfCancellationCounterexample.w_D
#print axioms LeanLane.HalfCancellationCounterexample.w_D_factor
#print axioms LeanLane.HalfCancellationCounterexample.w_gcd
#print axioms LeanLane.HalfCancellationCounterexample.w_gcd_factor
#print axioms LeanLane.HalfCancellationCounterexample.w_violates_half_bound
#print axioms LeanLane.HalfCancellationCounterexample.w_mismatches_five
#print axioms LeanLane.HalfCancellationCounterexample.w_rotation_distance
#print axioms LeanLane.HalfCancellationCounterexample.w_primitive
#print axioms LeanLane.HalfCancellationCounterexample.w_D_pos
