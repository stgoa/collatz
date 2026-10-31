import LeanLane.RationalCycle

/-!
# The general rotation identity and the gcd of a rotation difference

Formal companion of identity (3) of `areas/cycles/results/two-defect-cancellation-bound.md`:
for every `r`, `2^(P_r) · C_(R_r w) = 3^r · C_w + D_w · C_(w_<r)` where `P_r` is the `r`-th prefix sum and
`w_<r` the prefix of length `r`; hence, with `g = gcd(C_w, D_w)` and `q = D_w / g`,
`gcd(D_w, C_(R_r w) − C_w) = g · gcd(q, 2^(P_r) − 3^r)` for `r ≤ |w|`.
-/

namespace LeanLane
namespace RotationIdentity

open LeanLane.Words LeanLane.Doubled LeanLane.CycleEquation LeanLane.RationalCycle

/-- `C_(z ++ [a]) = 3 · C_z + 2^(Σz)`: appending a letter. -/
theorem C_append_singleton (z : List ℕ) (a : ℕ) : C (z ++ [a]) = 3 * C z + 2 ^ z.sum := by
  rw [C_append]; simp [C]

/-- **The general rotation identity**: `2^(Σ take r w) · C_(R_r w) = 3^r · C_w + D_w · C_(take r w)` for `r ≤ |w|`. -/
theorem rotation_identity_general (w : List ℕ) : ∀ r, r ≤ w.length →
    2 ^ (w.take r).sum * C (w.rotate r) = 3 ^ r * C w + D w * C (w.take r) := by
  intro r
  induction r with
  | zero => intro _; simp [C]
  | succ r ih =>
    intro hr
    have hr' : r ≤ w.length := Nat.le_of_succ_le hr
    have hlt : r < w.length := hr
    have hw' : w.rotate r ≠ [] := by
      intro h
      have := congrArg List.length h
      rw [List.length_rotate, List.length_nil] at this
      omega
    -- one more rotation step from `R_r w`
    have hstep := rotation_identity' (w.rotate r) hw'
    rw [List.rotate_rotate, D_rotate] at hstep
    have hget : (w.rotate r).getD 0 0 = w.getD r 0 := by
      rw [getD_rotate w r 0 (List.length_pos_of_ne_nil (by intro h; subst h; simp at hlt))]
      simp [Nat.mod_eq_of_lt hlt]
    rw [hget] at hstep
    -- the prefix of length r+1 and its sum
    have htake : w.take (r + 1) = w.take r ++ [w.getD r 0] := by
      rw [List.take_succ, List.getD_eq_getElem?_getD]
      cases h : w[r]? with
      | none => exact absurd hlt (Nat.not_lt.mpr (List.getElem?_eq_none_iff.mp h))
      | some a => simp
    have hsum : (w.take (r + 1)).sum = (w.take r).sum + w.getD r 0 := by
      rw [htake, List.sum_append, List.sum_singleton]
    rw [hsum, pow_add, htake, C_append_singleton]
    have ih' := ih hr'
    calc 2 ^ (w.take r).sum * 2 ^ (w.getD r 0) * C (w.rotate (r + 1))
        = 2 ^ (w.take r).sum * (2 ^ (w.getD r 0) * C (w.rotate (r + 1))) := by ring
      _ = 2 ^ (w.take r).sum * (3 * C (w.rotate r) + D w) := by rw [hstep]
      _ = 3 * (2 ^ (w.take r).sum * C (w.rotate r)) + 2 ^ (w.take r).sum * D w := by ring
      _ = 3 * (3 ^ r * C w + D w * C (w.take r)) + 2 ^ (w.take r).sum * D w := by rw [ih']
      _ = 3 ^ (r + 1) * C w + D w * (3 * C (w.take r) + 2 ^ (w.take r).sum) := by ring

/-- **Identity (3)**: `gcd(D_w, C_(R_r w) − C_w) = g · gcd(q, 2^(P_r) − 3^r)` with `g = gcd(C_w, D_w)`, `q = D_w/g`,
for `r ≤ |w|` and `D_w` odd (any positive word has `D_w` odd). -/
theorem gcd_rotation_difference (w : List ℕ) (r : ℕ) (hr : r ≤ w.length) (hodd : Odd (D w))
    (hD : D w ≠ 0) :
    (Int.gcd (D w) (C (w.rotate r) - C w) : ℤ)
      = Int.gcd (C w) (D w) * Int.gcd (D w / Int.gcd (C w) (D w)) (2 ^ (w.take r).sum - 3 ^ r) := by
  set g : ℤ := (Int.gcd (C w) (D w) : ℤ) with hg
  have hid := rotation_identity_general w r hr
  have hgpos : 0 < g := by
    rw [hg]; exact_mod_cast Int.gcd_pos_of_ne_zero_right _ hD
  obtain ⟨c, hc⟩ : g ∣ C w := Int.gcd_dvd_left _ _
  obtain ⟨q, hq⟩ : g ∣ D w := Int.gcd_dvd_right _ _
  have hc' : c = C w / g := by rw [hc, Int.mul_ediv_cancel_left _ hgpos.ne']
  have hq' : q = D w / g := by rw [hq, Int.mul_ediv_cancel_left _ hgpos.ne']
  have hcop : Int.gcd c q = 1 := by
    rw [hc', hq']
    exact Int.gcd_div_gcd_div_gcd (Int.gcd_pos_of_ne_zero_right (C w) hD)
  -- `2^P · (C_(R_r w) − C_w) = (3^r − 2^P) C_w + D_w · C_(take r w)`
  have key : 2 ^ (w.take r).sum * (C (w.rotate r) - C w)
      = (3 ^ r - 2 ^ (w.take r).sum) * C w + D w * C (w.take r) := by linear_combination hid
  -- the power of two is a unit modulo the odd `D_w`
  have h2 : Int.gcd (D w) (2 ^ (w.take r).sum * (C (w.rotate r) - C w)) = Int.gcd (D w) (C (w.rotate r) - C w) := by
    rw [Int.gcd_comm, gcd_two_pow_mul_left hodd, Int.gcd_comm]
  rw [← h2, key, Int.gcd_comm, Int.gcd_add_mul_left_left, hc, hq]
  -- gcd((3^r − 2^P)·g·c, g·q) = g · gcd((3^r − 2^P)·c, q) = g · gcd(3^r − 2^P, q)
  have h3 : (3 ^ r - 2 ^ (w.take r).sum) * (g * c) = g * ((3 ^ r - 2 ^ (w.take r).sum) * c) := by ring
  rw [h3, Int.gcd_mul_left, Int.gcd_mul_left_left_of_gcd_eq_one hcop, Int.mul_ediv_cancel_left _ hgpos.ne',
    Nat.cast_mul, Int.natCast_natAbs, abs_of_pos hgpos, Int.gcd_comm q,
    ← neg_sub (2 ^ (w.take r).sum) (3 ^ r), Int.neg_gcd]

end RotationIdentity
end LeanLane

#print axioms LeanLane.RotationIdentity.rotation_identity_general
#print axioms LeanLane.RotationIdentity.gcd_rotation_difference
