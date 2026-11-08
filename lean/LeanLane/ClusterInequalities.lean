import LeanLane.Words

/-!
# The three clustered-arc gap systems

These are real algebraic inequalities. The three systems are the explicit
gap witnesses obtained after the profile analysis; this module does not
formalize that analysis, a logarithmic estimate, or a cycle exclusion.
-/

namespace LeanLane.ClusterInequalities

/-- First ordering: the first, third and last gap witnesses. -/
def FirstSystem (a c u v ε : ℝ) : Prop :=
  v - c * u ≤ (3 / 8 : ℝ) * (v - (c - 1) * u) + ε ∧
  1 - a * u - v ≤ (3 / 8 : ℝ) * (a / (a + c) - (a - 1) * u) + ε ∧
  a * u ≤ 3 / (8 * (a + c)) + ε

/-- Second ordering: the first and last gap witnesses. -/
def SecondSystem (a c u v ε : ℝ) : Prop :=
  v - c * u ≤ (3 / 8 : ℝ) * (v - (c - 1) * u) + ε ∧
  1 - v ≤ 3 / (8 * (a + c)) + ε

/-- Third ordering: the first gap witness. -/
def ThirdSystem (a u ε : ℝ) : Prop :=
  1 - a * u ≤ (3 / 8 : ℝ) * (1 - (a - 1) * u) + ε

theorem scaled_error_le {a c ε : ℝ} (ha : 1 ≤ a) (hc : 1 ≤ c)
    (hε : ε ≤ 1 / (104 * (a + c))) : (a + c) * ε ≤ 1 / 104 := by
  have hr : 0 < 104 * (a + c) := by positivity
  have h := (le_div_iff₀ hr).mp hε
  nlinarith only [h]

theorem residual_pos {a c : ℝ} (ha : 1 ≤ a) (hc : 1 ≤ c) :
    0 < (5 / 8 : ℝ) * a ^ 2 + a * c - (15 / 64 : ℝ) * a -
      (3 / 8 : ℝ) * c - 117 / 320 -
      ((129 / 40 : ℝ) * a + c + 39 / 40) / 104 := by
  have hab : 0 ≤ (a - 1) * (c - 1) :=
    mul_nonneg (sub_nonneg.mpr ha) (sub_nonneg.mpr hc)
  nlinarith only [ha, hc, sq_nonneg (a - 1), hab]

/-- The first system already forces the margin without a clustering assumption. -/
theorem first_order {a c u v ε : ℝ} (ha : 1 ≤ a) (hc : 1 ≤ c)
    (hw : FirstSystem a c u v ε) : 1 / (104 * (a + c)) < ε := by
  rcases hw with ⟨hfirst, hmiddle, hlast⟩
  have ha0 : 0 < a := by linarith
  have hr : 0 < a + c := by linarith
  have hrne : a + c ≠ 0 := ne_of_gt hr
  have hcancel : (a + c) * (a / (a + c)) = a := by field_simp
  have hcancel3 : (a + c) * (3 / (8 * (a + c))) = (3 / 8 : ℝ) := by
    field_simp
  have h1 : (5 / 8 : ℝ) * v - ((5 / 8 : ℝ) * c + 3 / 8) * u - ε ≤ 0 := by
    nlinarith only [hfirst]
  have h2 : (a + c) - (a + c) * v -
      (a + c) * ((5 / 8 : ℝ) * a + 3 / 8) * u -
      (3 / 8 : ℝ) * a - (a + c) * ε ≤ 0 := by
    have h := mul_le_mul_of_nonneg_left hmiddle hr.le
    nlinarith only [h, hcancel]
  have h3 : a * (a + c) * u - (3 / 8 : ℝ) - (a + c) * ε ≤ 0 := by
    have h := mul_le_mul_of_nonneg_left hlast hr.le
    nlinarith only [h, hcancel3]
  have hT : 0 ≤ (5 / 8 : ℝ) * a + c + 39 / 40 := by linarith
  have hweight : 0 ≤ (8 / 5 : ℝ) * a * (a + c) := by positivity
  have hw1 := mul_nonpos_of_nonneg_of_nonpos hweight h1
  have hw2 := mul_nonpos_of_nonneg_of_nonpos ha0.le h2
  have hw3 := mul_nonpos_of_nonneg_of_nonpos hT h3
  have hsum : (5 / 8 : ℝ) * a ^ 2 + a * c - (15 / 64 : ℝ) * a -
      (3 / 8 : ℝ) * c - 117 / 320 ≤
      (a + c) * ((129 / 40 : ℝ) * a + c + 39 / 40) * ε := by
    nlinarith only [hw1, hw2, hw3]
  by_contra hnot
  have he := scaled_error_le ha hc (le_of_not_gt hnot)
  have hcoef : 0 ≤ (129 / 40 : ℝ) * a + c + 39 / 40 := by linarith
  have hupper := mul_le_mul_of_nonneg_left he hcoef
  have hpositive := residual_pos ha hc
  nlinarith only [hsum, hupper, hpositive]

theorem second_order {a c u v ε : ℝ} (ha : 1 ≤ a) (hc : 1 ≤ c)
    (hcluster : (a + c) * u < 1) (hw : SecondSystem a c u v ε) :
    1 / (104 * (a + c)) < ε := by
  rcases hw with ⟨hfirst, hlast⟩
  have hr : 0 < a + c := by linarith
  have hrne : a + c ≠ 0 := ne_of_gt hr
  have hcancel : (a + c) * (3 / (8 * (a + c))) = (3 / 8 : ℝ) := by
    field_simp
  have h1 : (5 / 8 : ℝ) * v - ((5 / 8 : ℝ) * c + 3 / 8) * u - ε ≤ 0 := by
    nlinarith only [hfirst]
  have h2 : (a + c) - (a + c) * v - (3 / 8 : ℝ) - (a + c) * ε ≤ 0 := by
    have h := mul_le_mul_of_nonneg_left hlast hr.le
    nlinarith only [h, hcancel]
  have hweight : 0 ≤ (8 / 5 : ℝ) * (a + c) := by positivity
  have hw1 := mul_nonpos_of_nonneg_of_nonpos hweight h1
  have hsum : a - (39 / 40 : ℝ) - (13 / 5 : ℝ) * (a + c) * ε +
      (c + 3 / 5) * (1 - (a + c) * u) ≤ 0 := by
    nlinarith only [hw1, h2]
  have hpositive : 0 < (c + (3 / 5 : ℝ)) * (1 - (a + c) * u) := by
    apply mul_pos
    · linarith
    · linarith
  by_contra hnot
  have he := scaled_error_le ha hc (le_of_not_gt hnot)
  nlinarith only [ha, he, hsum, hpositive]

theorem third_order {a c u ε : ℝ} (ha : 1 ≤ a) (hc : 1 ≤ c)
    (hcluster : (a + c) * u < 1) (hw : ThirdSystem a u ε) :
    1 / (104 * (a + c)) < ε := by
  have hr : 0 < a + c := by linarith
  have h1 : (5 / 8 : ℝ) - ((5 / 8 : ℝ) * a + 3 / 8) * u - ε ≤ 0 := by
    dsimp [ThirdSystem] at hw
    nlinarith only [hw]
  have hw1 := mul_nonpos_of_nonneg_of_nonpos hr.le h1
  have hsum : (5 / 8 : ℝ) * c - 3 / 8 - (a + c) * ε +
      ((5 / 8 : ℝ) * a + 3 / 8) * (1 - (a + c) * u) ≤ 0 := by
    nlinarith only [hw1]
  have hpositive : 0 < ((5 / 8 : ℝ) * a + 3 / 8) * (1 - (a + c) * u) := by
    apply mul_pos
    · linarith
    · linarith
  by_contra hnot
  have he := scaled_error_le ha hc (le_of_not_gt hnot)
  nlinarith only [hc, he, hsum, hpositive]

/-- Complete algebraic obstruction for the three gap systems. -/
theorem three_order_obstruction {a c u v ε : ℝ} (ha : 1 ≤ a) (hc : 1 ≤ c)
    (hcluster : (a + c) * u < 1)
    (hw : FirstSystem a c u v ε ∨ SecondSystem a c u v ε ∨ ThirdSystem a u ε) :
    1 / (104 * (a + c)) < ε := by
  rcases hw with hfirst | hsecond | hthird
  · exact first_order ha hc hfirst
  · exact second_order ha hc hcluster hsecond
  · exact third_order ha hc hcluster hthird

end LeanLane.ClusterInequalities

#print axioms LeanLane.ClusterInequalities.scaled_error_le
#print axioms LeanLane.ClusterInequalities.residual_pos
#print axioms LeanLane.ClusterInequalities.first_order
#print axioms LeanLane.ClusterInequalities.second_order
#print axioms LeanLane.ClusterInequalities.third_order
#print axioms LeanLane.ClusterInequalities.three_order_obstruction
