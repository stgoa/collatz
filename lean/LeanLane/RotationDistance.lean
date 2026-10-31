import LeanLane.CycleEquation

/-!
# No rotation differs from a word in exactly one position

For a word `w` and a shift `h`, `mismatches w h` (from `LeanLane.Words`) counts the positions `j < |w|` with
`w_j ≠ w_(j+h)` (indices modulo `|w|`). The signed differences `w_(j+h) − w_j` sum to zero over a full period,
because the rotated word is a permutation of the word; a single nonzero term is therefore impossible. Hence a
word that differs from one of its rotations differs from it in at least two positions, and a primitive word has
rotation distance `ρ(w) ≥ 2`.
-/

namespace LeanLane
namespace RotationDistance

open LeanLane.Words LeanLane.CycleEquation

/-- The signed difference between the rotated word and the word at position `j`. -/
def diff (w : List ℕ) (h j : ℕ) : ℤ := ((w.rotate h).getD j 0 : ℤ) - (w.getD j 0 : ℤ)

theorem map_range_getD (l : List ℕ) :
    (List.range l.length).map (fun j => (l.getD j 0 : ℤ)) = l.map (Nat.cast : ℕ → ℤ) := by
  apply List.ext_getElem (by simp)
  intro j h1 h2
  have hj : j < l.length := by simpa using h2
  simp [List.getElem_map, List.getElem_range, List.getD_eq_getElem?_getD, List.getElem?_eq_getElem hj]

/-- The differences sum to zero over a period. -/
theorem sum_diff (w : List ℕ) (h : ℕ) : ((List.range w.length).map (diff w h)).sum = 0 := by
  have hsplit : (List.range w.length).map (diff w h)
      = (List.range w.length).map (fun j => ((w.rotate h).getD j 0 : ℤ) + (-1) * (w.getD j 0 : ℤ)) := by
    simp [diff, sub_eq_add_neg]
  have h1 : (List.range w.length).map (fun j => ((w.rotate h).getD j 0 : ℤ))
      = (w.rotate h).map (Nat.cast : ℕ → ℤ) := by
    rw [← List.length_rotate w h]; exact map_range_getD (w.rotate h)
  rw [hsplit, List.sum_map_add, List.sum_map_mul_left, h1, map_range_getD, ← Nat.cast_list_sum, ← Nat.cast_list_sum,
    (List.rotate_perm w h).sum_eq]
  ring

/-- `mismatches` counts the nonzero differences. -/
theorem mismatches_eq_countP_diff (w : List ℕ) (h : ℕ) :
    mismatches w h = (List.range w.length).countP (fun j => decide (diff w h j ≠ 0)) := by
  unfold mismatches
  apply List.countP_congr
  intro j hj
  have hj' : j < w.length := List.mem_range.mp hj
  unfold diff
  rw [getD_rotate w h j hj']
  simp only [decide_eq_true_eq, ne_eq, sub_eq_zero, Nat.cast_inj]
  exact ⟨fun hne heq => hne heq.symm, fun hne heq => hne heq.symm⟩

/-- **No rotation has exactly one mismatch.** -/
theorem mismatches_ne_one (w : List ℕ) (h : ℕ) : mismatches w h ≠ 1 := by
  intro hone
  rw [mismatches_eq_countP_diff, List.countP_eq_length_filter] at hone
  obtain ⟨i, hi⟩ := List.length_eq_one_iff.mp hone
  have hmem : ∀ j, j ∈ (List.range w.length).filter (fun j => decide (diff w h j ≠ 0)) ↔ j = i := by
    intro j; rw [hi]; simp
  have hi_mis : diff w h i ≠ 0 := by
    have := (List.mem_filter.mp ((hmem i).mpr rfl)).2
    simpa using this
  have hi_lt : i < w.length := List.mem_range.mp (List.mem_filter.mp ((hmem i).mpr rfl)).1
  have hothers : ∀ j, j ∈ Finset.range w.length → j ≠ i → diff w h j = 0 := by
    intro j hj hne
    by_contra hdj
    have : j ∈ (List.range w.length).filter (fun j => decide (diff w h j ≠ 0)) :=
      List.mem_filter.mpr ⟨List.mem_range.mpr (Finset.mem_range.mp hj), by simpa using hdj⟩
    exact hne ((hmem j).mp this)
  have hsum : ∑ j ∈ Finset.range w.length, diff w h j = diff w h i :=
    Finset.sum_eq_single i hothers (fun hnot => absurd (Finset.mem_range.mpr hi_lt) hnot)
  have hzero : ∑ j ∈ Finset.range w.length, diff w h j = 0 := by
    have hconv : ∑ j ∈ Finset.range w.length, diff w h j = ((List.range w.length).map (diff w h)).sum := rfl
    rw [hconv]; exact sum_diff w h
  exact hi_mis (hsum ▸ hzero)

/-- Every rotation that is not the word itself differs from it in at least two positions. -/
theorem two_le_mismatches_of_ne (w : List ℕ) (h : ℕ) (hne : w.rotate h ≠ w) (hh : h < w.length) :
    2 ≤ mismatches w h := by
  have h0 : mismatches w h ≠ 0 := by
    intro hz
    apply hne
    rw [mismatches_eq_countP_diff, List.countP_eq_zero] at hz
    apply List.ext_getElem (List.length_rotate w h)
    intro j hj1 hj2
    have := hz j (List.mem_range.mpr hj2)
    simp only [decide_eq_true_eq, not_not] at this
    unfold diff at this
    have heq : (w.rotate h).getD j 0 = w.getD j 0 := by exact_mod_cast sub_eq_zero.mp this
    simpa [List.getD_eq_getElem?_getD, List.getElem?_eq_getElem hj1, List.getElem?_eq_getElem hj2] using heq
  have h1 := mismatches_ne_one w h
  omega

end RotationDistance
end LeanLane

#print axioms LeanLane.RotationDistance.sum_diff
#print axioms LeanLane.RotationDistance.mismatches_ne_one
#print axioms LeanLane.RotationDistance.two_le_mismatches_of_ne
