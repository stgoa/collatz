import LeanLane.ThirdPeriod

/-! Full balanced third-period classification on the shared valuation-word definitions.
The majority and placement reductions are proved here; the unaligned arithmetic is
imported from `ThirdPeriod`, and the aligned arithmetic is rederived below. -/

namespace LeanLane.AlignedThirdPeriod

open Words ThirdPeriod RationalCycle CycleEquation

theorem equal_intercepts_of_dvd {U V : List ℕ}
    (hU : Positive U) (hV : Positive V)
    (hlen : V.length = U.length) (hsum : V.sum = U.sum)
    (hdiv : D (U ++ U ++ V) ∣ C (U ++ U ++ V)) : C U = C V := by
  let P : ℤ := 3 ^ U.length
  let Z : ℤ := 2 ^ U.sum
  let Φ := P ^ 2 + P * Z + Z ^ 2
  have hP : 0 < P := by dsimp [P]; positivity
  have hZ : 0 < Z := by dsimp [Z]; positivity
  have hΦ : 0 < Φ := by dsimp [Φ]; positivity
  have hPZ : P * Z < Φ := by dsimp [Φ]; nlinarith
  have hfac : D (U ++ U ++ V) = (Z - P) * Φ := by
    simp only [D, List.sum_append, List.length_append, hsum, hlen, pow_add]
    dsimp [Φ, P, Z]
    ring
  have hΦC : Φ ∣ C (U ++ U ++ V) :=
    dvd_trans ⟨Z - P, by rw [hfac]; ring⟩ hdiv
  have hformula : C (U ++ U ++ V) - Φ * C U = Z ^ 2 * (C V - C U) := by
    simp only [C_append, List.sum_append, hlen, pow_add]
    dsimp [Φ, P, Z]
    ring
  have hc : IsCoprime (3 : ℤ) 2 := ⟨1, -1, by norm_num⟩
  have hcop : IsCoprime P Z := hc.pow
  have hcopΦ := coprime_cyclotomic hcop
  have hdifference : Φ ∣ C V - C U := by
    apply (hcopΦ.pow_right (n := 2)).dvd_of_dvd_mul_left
    rw [← hformula]
    exact dvd_sub hΦC (dvd_mul_right _ _)
  have hboundU := intercept_bound hU
  have hboundV := intercept_bound hV
  rw [hlen, hsum] at hboundV
  have htwo : (1 : ℤ) ≤ 2 ^ U.length := one_le_pow₀ (by norm_num)
  have hCU : C U < Φ := by
    have hle := mul_le_mul_of_nonneg_right htwo (C_nonneg U)
    have : C U < P * Z := by dsimp [P, Z]; nlinarith
    exact lt_trans this hPZ
  have hCV : C V < Φ := by
    have hle := mul_le_mul_of_nonneg_right htwo (C_nonneg V)
    have : C V < P * Z := by dsimp [P, Z]; nlinarith
    exact lt_trans this hPZ
  obtain ⟨t, ht⟩ := hdifference
  have htzero : t = 0 := by
    by_contra htzero
    have htcase : t ≤ -1 ∨ 1 ≤ t := by omega
    rcases htcase with htlo | hthi
    · have hmul := mul_le_mul_of_nonneg_left htlo hΦ.le
      nlinarith [C_nonneg U, C_nonneg V]
    · have hmul := mul_le_mul_of_nonneg_left hthi hΦ.le
      nlinarith [C_nonneg U, C_nonneg V]
  rw [htzero, mul_zero] at ht
  omega

theorem balanced_edit_difference (u v z : List ℕ) (a b d : ℕ) :
    C (block u (a + d) ++ block v b ++ z) -
      C (block u a ++ block v (b + d) ++ z) =
      3 ^ z.length * 2 ^ (block u a).sum * (2 ^ d - 1) * C (block v b) := by
  simp only [block, C_append, C, List.length_nil, pow_zero, mul_zero, add_zero,
    List.length_append, List.length_singleton, List.sum_append, List.sum_singleton,
    pow_add, pow_succ]
  ring

theorem balanced_edit_intercepts_ne (u v z : List ℕ) (a b d : ℕ) (hd : 0 < d) :
    C (block u (a + d) ++ block v b ++ z) ≠
      C (block u a ++ block v (b + d) ++ z) := by
  have hk : (0 : ℤ) < 2 ^ d - 1 := by
    have hp := (pow_lt_pow_iff_right₀ (by norm_num : (1 : ℤ) < 2)).mpr hd
    norm_num only [pow_zero] at hp
    omega
  have hC : 0 < C (block v b) := C_pos _ (by simp [block])
  have hdiff : 0 < C (block u (a + d) ++ block v b ++ z) -
      C (block u a ++ block v (b + d) ++ z) := by
    rw [balanced_edit_difference]
    positivity
  omega

theorem aligned_discriminant_not_dvd {u v z : List ℕ} {a b d : ℕ}
    (hu : Positive u) (hv : Positive v) (hz : Positive z)
    (ha : 0 < a) (hb : 0 < b) (hd : 0 < d) :
    let U := block u a ++ block v (b + d) ++ z
    let V := block u (a + d) ++ block v b ++ z
    ¬ D (U ++ U ++ V) ∣ C (U ++ U ++ V) := by
  intro U V hdiv
  have hU : Positive U := positive_append
    (positive_append (block_positive hu ha) (block_positive hv (by omega))) hz
  have hV : Positive V := positive_append
    (positive_append (block_positive hu (by omega)) (block_positive hv hb)) hz
  have heq := equal_intercepts_of_dvd hU hV (by simp [U, V, block])
    (by simp [U, V, block]; omega) hdiv
  exact balanced_edit_intercepts_ne u v z a b d hd heq.symm

theorem aligned_positive_addend_control :
    ∃ x : ℕ → ℤ, IsCycle 32039 ([2,3] ++ [2,3] ++ [3,2]) x ∧ (∀ i, 0 < x i) := by
  have hnonempty : ([2,3] ++ [2,3] ++ [3,2] : List ℕ) ≠ [] := by decide
  have hD : 0 < D ([2,3] ++ [2,3] ++ [3,2]) := by norm_num [D]
  obtain ⟨hc, _, _, hp, _, _⟩ := reduced_cycle ([2,3] ++ [2,3] ++ [3,2]) hnonempty hD
  refine ⟨_, ?_, hp⟩
  convert hc using 1
  norm_num [D, C]

theorem aligned_control_intercepts :
    C [2,3] = 7 ∧ C [3,2] = 11 ∧ C ([2,3] ++ [2,3] ++ [3,2]) = 13847 ∧
      D ([2,3] ++ [2,3] ++ [3,2]) = 32039 := by norm_num [C, D]

theorem C_odd {z : List ℕ} (hz : z ≠ []) (hpos : ∀ a ∈ z, 1 ≤ a) : Odd (C z) :=
  odd_C_of_positive hz (fun a ha => by have := hpos a ha; omega)

/-- The existing equal-total intercept injectivity argument, on the shared word definitions. -/
theorem C_injective : ∀ (u v : List ℕ), (∀ a ∈ u, 1 ≤ a) → (∀ a ∈ v, 1 ≤ a) →
    u.length = v.length → u.sum = v.sum → C u = C v → u = v
  | [], v, _, _, hl, _, _ => (List.length_eq_zero_iff.mp hl.symm).symm
  | a :: u, [], _, _, hl, _, _ => absurd hl (by simp)
  | a :: u, b :: v, hu, hv, hl, hs, hC => by
    have hu' : ∀ x ∈ u, 1 ≤ x := fun x hx => hu x (List.mem_cons_of_mem _ hx)
    have hv' : ∀ x ∈ v, 1 ≤ x := fun x hx => hv x (List.mem_cons_of_mem _ hx)
    simp only [List.length_cons, List.sum_cons] at hl hs
    have hlen : u.length = v.length := by omega
    simp only [C] at hC
    rw [← hlen] at hC
    have hC' : (2 : ℤ) ^ a * C u = 2 ^ b * C v := add_left_cancel hC
    rcases eq_or_ne u [] with rfl | hu0
    · have hv0 : v = [] := List.length_eq_zero_iff.mp hlen.symm
      subst hv0
      simp only [List.sum_nil, add_zero] at hs
      rw [hs]
    · have hv0 : v ≠ [] := fun h => hu0 (List.length_eq_zero_iff.mp (hlen.trans (by simp [h])))
      have hou := C_odd hu0 hu'
      have hov := C_odd hv0 hv'
      have hab : a = b := by
        by_contra hne
        rcases Nat.lt_or_gt_of_ne hne with hlt | hgt
        · have e : (2 : ℤ) ^ b = 2 ^ a * 2 ^ (b - a) := by
            rw [← pow_add, Nat.add_sub_cancel' hlt.le]
          rw [e, mul_assoc] at hC'
          have h := mul_left_cancel₀ (by positivity : (2 : ℤ) ^ a ≠ 0) hC'
          have heven : Even (C u) := by
            rw [h]
            exact (even_two.pow_of_ne_zero (by omega)).mul_right _
          exact (Int.not_even_iff_odd.mpr hou) heven
        · have e : (2 : ℤ) ^ a = 2 ^ b * 2 ^ (a - b) := by
            rw [← pow_add, Nat.add_sub_cancel' hgt.le]
          rw [e, mul_assoc] at hC'
          have h := mul_left_cancel₀ (by positivity : (2 : ℤ) ^ b ≠ 0) hC'.symm
          have heven : Even (C v) := by
            rw [h]
            exact (even_two.pow_of_ne_zero (by omega)).mul_right _
          exact (Int.not_even_iff_odd.mpr hov) heven
      subst hab
      have hCuv : C u = C v := mul_left_cancel₀ (by positivity : (2 : ℤ) ^ a ≠ 0) hC'
      have := C_injective u v hu' hv' hlen (by omega) hCuv
      rw [this]

theorem no_equal_total_cycle {U V : List ℕ} {x : ℕ → ℤ}
    (hU : Positive U) (hV : Positive V)
    (hlen : V.length = U.length) (hsum : V.sum = U.sum) (hne : U ≠ V)
    (hc : IsCycle 1 (U ++ U ++ V) x) : False := by
  have hdiv : D (U ++ U ++ V) ∣ C (U ++ U ++ V) := by
    refine ⟨x 0, ?_⟩
    simpa only [one_mul, mul_comm] using hc.cycle_eq.symm
  have hC := equal_intercepts_of_dvd hU hV hlen hsum hdiv
  exact hne (C_injective U V (fun a ha => by have := hU a ha; omega)
    (fun a ha => by have := hV a ha; omega) hlen.symm hsum.symm hC)

end LeanLane.AlignedThirdPeriod

namespace LeanLane.BalancedThirdPeriod

open Words ThirdPeriod CycleEquation RationalCycle Finset

def edge (a b : ℕ) : ℕ := if a ≠ b then 1 else 0

def triangleCount (a b c : ℕ) : ℕ := edge a b + edge b c + edge c a

def majority3 (a b c : ℕ) : ℕ := if a = b then a else if a = c then a else b

def majorityTemplate (w : List ℕ) (g : ℕ) : List ℕ :=
  (List.range g).map fun i => majority3 (w.getD i 0) (w.getD (i + g) 0) (w.getD (i + 2*g) 0)

theorem majority_length (w : List ℕ) (g : ℕ) : (majorityTemplate w g).length = g := by
  simp [majorityTemplate]

theorem count_range (p : ℕ → Bool) (n : ℕ) :
    (List.range n).countP p = ∑ i ∈ Finset.range n, if p i then 1 else 0 := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [List.range_succ, List.countP_append, Finset.sum_range_succ, ih]
    simp only [List.countP_cons, List.countP_nil, Nat.zero_add]

theorem three_sum_blocks (f : ℕ → ℕ) (g : ℕ) :
    (∑ i ∈ Finset.range (3*g), f i) =
      ∑ i ∈ Finset.range g, (f i + f (i+g) + f (i+2*g)) := by
  rw [show 3*g = (g+g)+g by omega, Finset.sum_range_add, Finset.sum_range_add]
  simp only [Finset.sum_add_distrib]
  congr 1
  · congr 1
    apply Finset.sum_congr rfl
    intro i hi
    congr 1
    omega
  · apply Finset.sum_congr rfl
    intro i hi
    congr 1
    omega

theorem mismatches_column_sum {w : List ℕ} {g : ℕ} (_hg : 0 < g)
    (hlen : w.length = 3*g) :
    mismatches w g = ∑ i ∈ Finset.range g,
      triangleCount (w.getD i 0) (w.getD (i+g) 0) (w.getD (i+2*g) 0) := by
  unfold mismatches
  rw [count_range, hlen, three_sum_blocks]
  apply Finset.sum_congr rfl
  intro i hi
  have hi : i < g := Finset.mem_range.mp hi
  have h1 : (i+g) % (3*g) = i+g := Nat.mod_eq_of_lt (by omega)
  have h2 : (i+g+g) % (3*g) = i+2*g := by rw [Nat.mod_eq_of_lt (by omega)]; omega
  have h3 : (i+2*g+g) % (3*g) = i := by
    rw [show i+2*g+g = i+3*g by omega, Nat.add_mod_right]
    exact Nat.mod_eq_of_lt (by omega)
  simp only [h1, h2, h3, decide_eq_true_eq, triangleCount, edge]

theorem triangle_values (a b c : ℕ) :
    triangleCount a b c = 0 ∨ triangleCount a b c = 2 ∨ triangleCount a b c = 3 := by
  by_cases hab : a = b <;> by_cases hbc : b = c <;> by_cases hca : c = a <;>
    simp_all [triangleCount, edge]

theorem triangle_nonzero_lower (a b c : ℕ) (h : triangleCount a b c ≠ 0) :
    2 ≤ triangleCount a b c := by
  rcases triangle_values a b c with h0 | h2 | h3 <;> omega

theorem triangle_upper (a b c : ℕ) : triangleCount a b c ≤ 3 := by
  rcases triangle_values a b c with h0 | h2 | h3 <;> omega

theorem triangle_majority_deviations (a b c : ℕ) (h : triangleCount a b c ≤ 2) :
    triangleCount a b c = 2 *
      (edge a (majority3 a b c) + edge b (majority3 a b c) + edge c (majority3 a b c)) := by
  by_cases hab : a = b
  · subst b
    by_cases hac : a = c
    · subst c
      simp [triangleCount, edge, majority3]
    · simp [triangleCount, edge, majority3, hac, Ne.symm hac]
  · by_cases hac : a = c
    · subst c
      simp [triangleCount, edge, majority3, hab, Ne.symm hab]
    · by_cases hbc : b = c
      · subst c
        simp [triangleCount, edge, majority3, hab, Ne.symm hab]
      · simp [triangleCount, edge, hab, hbc, Ne.symm hac] at h

theorem count_four_bounds (f : ℕ → ℕ) (g : ℕ)
    (hvalues : ∀ i ∈ Finset.range g, f i = 0 ∨ f i = 2 ∨ f i = 3)
    (hsum : ∑ i ∈ Finset.range g, f i = 4) :
    ((Finset.range g).filter fun i => f i ≠ 0).card = 2 ∧
      ∀ i ∈ Finset.range g, f i ≤ 2 := by
  let K := (Finset.range g).filter fun i => f i ≠ 0
  have hsumK : ∑ i ∈ K, f i = 4 := by
    dsimp [K]
    rw [Finset.sum_filter_ne_zero]
    exact hsum
  have hlower : ∀ i ∈ K, 2 ≤ f i := by
    intro i hi
    have hi' := Finset.mem_filter.mp hi
    rcases hvalues i hi'.1 with h0 | h2 | h3 <;> omega
  have hupper : ∀ i ∈ K, f i ≤ 3 := by
    intro i hi
    rcases hvalues i (Finset.mem_filter.mp hi).1 with h0 | h2 | h3 <;> omega
  have hlo : K.card * 2 ≤ 4 := by
    calc K.card * 2 = ∑ i ∈ K, 2 := by simp
      _ ≤ ∑ i ∈ K, f i := Finset.sum_le_sum hlower
      _ = 4 := hsumK
  have hup : 4 ≤ K.card * 3 := by
    calc 4 = ∑ i ∈ K, f i := hsumK.symm
      _ ≤ ∑ i ∈ K, 3 := Finset.sum_le_sum hupper
      _ = K.card * 3 := by simp
  have hcard : K.card = 2 := by omega
  obtain ⟨i, j, hij, hK⟩ := Finset.card_eq_two.mp hcard
  have hiK : i ∈ K := by rw [hK]; simp
  have hjK : j ∈ K := by rw [hK]; simp
  have hsumij : f i + f j = 4 := by simpa [hK, hij] using hsumK
  have hi2 : f i = 2 := by have := hlower i hiK; have := hlower j hjK; omega
  have hj2 : f j = 2 := by have := hlower i hiK; have := hlower j hjK; omega
  refine ⟨hcard, ?_⟩
  intro n hn
  by_cases hfn : f n = 0
  · omega
  · have hnK : n ∈ K := Finset.mem_filter.mpr ⟨hn, hfn⟩
    rw [hK] at hnK
    simp only [Finset.mem_insert, Finset.mem_singleton] at hnK
    rcases hnK with rfl | rfl <;> omega

theorem column_bounds {w : List ℕ} {g : ℕ} (hg : 0 < g)
    (hlen : w.length = 3*g) (hmis : mismatches w g = 4) :
    ∀ i ∈ Finset.range g,
      triangleCount (w.getD i 0) (w.getD (i+g) 0) (w.getD (i+2*g) 0) ≤ 2 := by
  apply (count_four_bounds _ g (fun i hi => triangle_values _ _ _) ?_).2
  rw [← mismatches_column_sum hg hlen]
  exact hmis

theorem majority_getD (w : List ℕ) (g i : ℕ) (hi : i < g) :
    (majorityTemplate w g).getD i 0 =
      majority3 (w.getD i 0) (w.getD (i+g) 0) (w.getD (i+2*g) 0) := by
  rw [List.getD_eq_getElem _ _ (by simpa [majority_length] using hi)]
  simp [majorityTemplate]

theorem getD_positive {w : List ℕ} (hw : Positive w) {i : ℕ} (hi : i < w.length) :
    0 < w.getD i 0 := by
  rw [List.getD_eq_getElem _ _ hi]
  exact hw _ (List.getElem_mem hi)

theorem majority_positive {w : List ℕ} {g : ℕ}
    (hw : Positive w) (hlen : w.length = 3*g) : Positive (majorityTemplate w g) := by
  intro a ha
  obtain ⟨i, hi, rfl⟩ := List.mem_map.mp ha
  have hi : i < g := List.mem_range.mp hi
  have h1 : 0 < w.getD i 0 := getD_positive hw (by omega)
  have h2 : 0 < w.getD (i+g) 0 := getD_positive hw (by omega)
  unfold majority3
  split_ifs <;> assumption

def deviation (w : List ℕ) (g i : ℕ) : ℕ :=
  edge (w.getD i 0) ((majorityTemplate w g).getD (i % g) 0)

theorem two_deviations {w : List ℕ} {g : ℕ} (hg : 0 < g)
    (hlen : w.length = 3*g) (hmis : mismatches w g = 4) :
    (∑ i ∈ Finset.range (3*g), deviation w g i) = 2 := by
  have hc := column_bounds hg hlen hmis
  have htwice : 2 * (∑ i ∈ Finset.range (3*g), deviation w g i) = 4 := by
    rw [three_sum_blocks, Finset.mul_sum]
    rw [← hmis, mismatches_column_sum hg hlen]
    apply Finset.sum_congr rfl
    intro i hi
    have hi' : i < g := Finset.mem_range.mp hi
    have h0 : i % g = i := Nat.mod_eq_of_lt hi'
    have h1 : (i+g) % g = i := by simp [h0]
    have h2 : (i+2*g) % g = i := by
      simp [Nat.add_mod, h0]
    simp only [deviation, h0, h1, h2, majority_getD w g i hi']
    exact (triangle_majority_deviations _ _ _ (hc i hi)).symm
  omega

theorem exceptional_positions {w : List ℕ} {g : ℕ} (hg : 0 < g)
    (hlen : w.length = 3*g) (hmis : mismatches w g = 4) :
    ∃ p n : ℕ, p < 3*g ∧ n < 3*g ∧ p ≠ n ∧
      w.getD p 0 ≠ (majorityTemplate w g).getD (p%g) 0 ∧
      w.getD n 0 ≠ (majorityTemplate w g).getD (n%g) 0 ∧
      ∀ i < 3*g, i ≠ p → i ≠ n →
        w.getD i 0 = (majorityTemplate w g).getD (i%g) 0 := by
  let E := (Finset.range (3*g)).filter fun i =>
    w.getD i 0 ≠ (majorityTemplate w g).getD (i%g) 0
  have hcard : E.card = 2 := by
    simpa only [E, deviation, edge, Finset.sum_boole, Nat.cast_id] using
      two_deviations hg hlen hmis
  obtain ⟨p, n, hpn, hE⟩ := Finset.card_eq_two.mp hcard
  have hp : p ∈ E := by rw [hE]; simp
  have hn : n ∈ E := by rw [hE]; simp
  have hp' := Finset.mem_filter.mp hp
  have hn' := Finset.mem_filter.mp hn
  refine ⟨p, n, Finset.mem_range.mp hp'.1, Finset.mem_range.mp hn'.1,
    hpn, hp'.2, hn'.2, ?_⟩
  intro i hi hip hin
  by_contra hne
  have hiE : i ∈ E := Finset.mem_filter.mpr ⟨Finset.mem_range.mpr hi, hne⟩
  rw [hE] at hiE
  simp only [Finset.mem_insert, Finset.mem_singleton] at hiE
  tauto

theorem three_residue_cases {g i : ℕ} (_hg : 0 < g) (hi : i < 3*g) :
    i = i%g ∨ i = i%g+g ∨ i = i%g+2*g := by
  by_cases hi0 : i < g
  · left
    exact (Nat.mod_eq_of_lt hi0).symm
  · by_cases hi1 : i < 2*g
    · right; left
      have hm : i%g = i-g := by
        rw [Nat.mod_eq_sub_mod (by omega), Nat.mod_eq_of_lt (by omega)]
      omega
    · right; right
      have hm : i%g = i-g-g := by
        rw [Nat.mod_eq_sub_mod (by omega), Nat.mod_eq_sub_mod (by omega),
          Nat.mod_eq_of_lt (by omega)]
      omega

theorem exceptional_columns_distinct {w : List ℕ} {g p n : ℕ}
    (hg : 0 < g) (hlen : w.length = 3*g) (hmis : mismatches w g = 4)
    (hp : p < 3*g) (hn : n < 3*g) (hpn : p ≠ n)
    (hpne : w.getD p 0 ≠ (majorityTemplate w g).getD (p%g) 0)
    (hnne : w.getD n 0 ≠ (majorityTemplate w g).getD (n%g) 0) : p%g ≠ n%g := by
  intro hmod
  let i := p%g
  have hi : i < g := Nat.mod_lt p hg
  have hc := column_bounds hg hlen hmis i (Finset.mem_range.mpr hi)
  have hdev := triangle_majority_deviations
    (w.getD i 0) (w.getD (i+g) 0) (w.getD (i+2*g) 0) hc
  have hpedge : edge (w.getD p 0)
      (majority3 (w.getD i 0) (w.getD (i+g) 0) (w.getD (i+2*g) 0)) = 1 := by
    rw [← majority_getD w g i hi]
    exact ite_eq_left hpne
  have hnedge : edge (w.getD n 0)
      (majority3 (w.getD i 0) (w.getD (i+g) 0) (w.getD (i+2*g) 0)) = 1 := by
    rw [← majority_getD w g i hi]
    change edge (w.getD n 0) ((majorityTemplate w g).getD (p%g) 0) = 1
    rw [hmod]
    exact ite_eq_left hnne
  have hpcases := three_residue_cases hg hp
  have hncases := three_residue_cases hg hn
  rw [← hmod] at hncases
  change p = i ∨ p = i+g ∨ p = i+2*g at hpcases
  change n = i ∨ n = i+g ∨ n = i+2*g at hncases
  rcases hpcases with hp' | hp' | hp' <;>
    rcases hncases with hn' | hn' | hn'
  all_goals rw [hp'] at hpedge hpn
  all_goals rw [hn'] at hnedge hpn
  all_goals omega

theorem sum_periodic_template (U : List ℕ) :
    (∑ i ∈ Finset.range (3*U.length), U.getD (i%U.length) 0) = 3*U.sum := by
  rw [three_sum_blocks]
  calc (∑ i ∈ Finset.range U.length,
      (U.getD (i%U.length) 0 + U.getD ((i+U.length)%U.length) 0 +
        U.getD ((i+2*U.length)%U.length) 0)) =
      ∑ i ∈ Finset.range U.length, 3*U.getD i 0 := by
        apply Finset.sum_congr rfl
        intro i hi
        have hi' : i < U.length := Finset.mem_range.mp hi
        simp [Nat.add_mod, Nat.mod_eq_of_lt hi']
        omega
    _ = 3*U.sum := by rw [← Finset.mul_sum, CycleInequality.sum_getD]

theorem paired_values_of_sum (f b : ℕ → ℕ) (N p n : ℕ)
    (hp : p < N) (hn : n < N) (hpn : p ≠ n)
    (hsum : (∑ i ∈ Finset.range N, f i) = ∑ i ∈ Finset.range N, b i)
    (hother : ∀ i < N, i ≠ p → i ≠ n → f i = b i) :
    f p + f n = b p + b n := by
  have hpoint : ∀ i ∈ Finset.range N,
      f i + (if i=p then b p else 0) + (if i=n then b n else 0) =
      b i + (if i=p then f p else 0) + (if i=n then f n else 0) := by
    intro i hi
    by_cases hip : i=p
    · subst i
      simp [hpn, Nat.add_comm]
    · by_cases hin : i=n
      · subst i
        simp [Ne.symm hpn, Nat.add_comm]
      · simp [hip, hin, hother i (Finset.mem_range.mp hi) hip hin]
  have htotal := Finset.sum_congr rfl hpoint
  simp only [Finset.sum_add_distrib] at htotal
  simp only [Finset.sum_ite_eq', Finset.mem_range, hp, hn, ite_true] at htotal
  omega

structure BalancedPair (w U : List ℕ) (p n d : ℕ) : Prop where
  length_eq : w.length = 3*U.length
  positive_lt : p < w.length
  negative_lt : n < w.length
  distinct_columns : p%U.length ≠ n%U.length
  delta_pos : 0 < d
  increase : w.getD p 0 = U.getD (p%U.length) 0 + d
  decrease : w.getD n 0 + d = U.getD (n%U.length) 0
  unchanged : ∀ i < w.length, i ≠ p → i ≠ n → w.getD i 0 = U.getD (i%U.length) 0

theorem balanced_pair_of_mismatches {w : List ℕ} {g : ℕ}
    (hg : 0 < g) (hlen : w.length = 3*g) (hmis : mismatches w g = 4)
    (hbal : w.sum = 3*(majorityTemplate w g).sum) :
    ∃ p n d : ℕ, BalancedPair w (majorityTemplate w g) p n d := by
  let U := majorityTemplate w g
  have hUlen : U.length = g := majority_length w g
  change ∃ p n d : ℕ, BalancedPair w U p n d
  obtain ⟨p,n,hp,hn,hpn,hpne,hnne,hother⟩ := exceptional_positions hg hlen hmis
  have hcols := exceptional_columns_distinct hg hlen hmis hp hn hpn hpne hnne
  have hsumf : (∑ i ∈ Finset.range (3*g), w.getD i 0) = w.sum := by
    rw [← hlen]
    exact CycleInequality.sum_getD w
  have hsumb : (∑ i ∈ Finset.range (3*g), U.getD (i%g) 0) = 3*U.sum := by
    simpa only [hUlen] using sum_periodic_template U
  have hpair := paired_values_of_sum (fun i => w.getD i 0) (fun i => U.getD (i%g) 0)
    (3*g) p n hp hn hpn (by rw [hsumf, hsumb]; exact hbal) hother
  by_cases hup : U.getD (p%g) 0 < w.getD p 0
  · refine ⟨p,n,w.getD p 0-U.getD (p%g) 0, ?_⟩
    constructor
    · simpa only [hUlen] using hlen
    · omega
    · omega
    · simpa only [hUlen] using hcols
    · omega
    · simpa only [hUlen] using (show w.getD p 0 = U.getD (p%g) 0 +
        (w.getD p 0-U.getD (p%g) 0) by omega)
    · simpa only [hUlen] using (show w.getD n 0 +
        (w.getD p 0-U.getD (p%g) 0) = U.getD (n%g) 0 by omega)
    · simpa only [hUlen, hlen] using hother
  · have hdown : w.getD p 0 < U.getD (p%g) 0 := by change w.getD p 0 ≠ U.getD (p%g) 0 at hpne; omega
    refine ⟨n,p,U.getD (p%g) 0-w.getD p 0, ?_⟩
    constructor
    · simpa only [hUlen] using hlen
    · omega
    · omega
    · simpa only [hUlen] using hcols.symm
    · omega
    · simpa only [hUlen] using (show w.getD n 0 = U.getD (n%g) 0 +
        (U.getD (p%g) 0-w.getD p 0) by omega)
    · simpa only [hUlen] using (show w.getD p 0 +
        (U.getD (p%g) 0-w.getD p 0) = U.getD (p%g) 0 by omega)
    · intro i hi hin hip
      simpa only [hUlen] using hother i (by omega) hip hin

def backIndex (m R p : ℕ) : ℕ := if R ≤ p then p-R else p+m-R

theorem backIndex_lt {m R p : ℕ} (hR : R < m) (hp : p < m) : backIndex m R p < m := by
  unfold backIndex
  split_ifs <;> omega

theorem rotated_index_iff {m R p i : ℕ} (hR : R < m) (hp : p < m) (hi : i < m) :
    (i+R)%m = p ↔ i = backIndex m R p := by
  unfold backIndex
  split_ifs with hRp
  all_goals by_cases hsum : i+R < m
  all_goals first
    | rw [Nat.mod_eq_of_lt hsum]; omega
    | rw [Nat.mod_eq_sub_mod (by omega), Nat.mod_eq_of_lt (by omega)]; omega

theorem backIndex_inverse {m R p : ℕ} (hR : R < m) (hp : p < m) :
    (backIndex m R p + R)%m = p :=
  (rotated_index_iff hR hp (backIndex_lt hR hp)).mpr rfl

theorem rotate_template_getD (U : List ℕ) (R i : ℕ) (hg : 0 < U.length) :
    (U.rotate R).getD (i%U.length) 0 = U.getD ((i+R)%U.length) 0 := by
  rw [getD_rotate U R (i%U.length) (Nat.mod_lt i hg)]
  congr 1
  simp [Nat.add_mod]

theorem triple_mod (i g : ℕ) : (i%(3*g))%g = i%g := by
  exact Nat.mod_mod_of_dvd i (dvd_mul_left g 3)

theorem BalancedPair.rotate {w U : List ℕ} {p n d R : ℕ}
    (h : BalancedPair w U p n d) (hR : R < w.length) :
    BalancedPair (w.rotate R) (U.rotate R)
      (backIndex w.length R p) (backIndex w.length R n) d := by
  have hg : 0 < U.length := by have := h.positive_lt; have := h.length_eq; omega
  have hp := backIndex_lt hR h.positive_lt
  have hn := backIndex_lt hR h.negative_lt
  have hip := backIndex_inverse hR h.positive_lt
  have hin := backIndex_inverse hR h.negative_lt
  have hpmod : (backIndex w.length R p+R)%U.length = p%U.length := by
    calc _ = ((backIndex w.length R p+R)%w.length)%U.length := by
          rw [h.length_eq, triple_mod]
      _ = p%U.length := by rw [hip]
  have hnmod : (backIndex w.length R n+R)%U.length = n%U.length := by
    calc _ = ((backIndex w.length R n+R)%w.length)%U.length := by
          rw [h.length_eq, triple_mod]
      _ = n%U.length := by rw [hin]
  constructor
  · simpa only [List.length_rotate] using h.length_eq
  · simpa only [List.length_rotate] using hp
  · simpa only [List.length_rotate] using hn
  · simp only [List.length_rotate]
    intro heq
    apply h.distinct_columns
    rw [← hpmod, ← hnmod]
    simp only [Nat.add_mod, Nat.mod_mod, heq]
  · exact h.delta_pos
  · simp only [List.length_rotate]
    rw [getD_rotate w R _ hp, hip, rotate_template_getD U R _ hg, hpmod]
    exact h.increase
  · simp only [List.length_rotate]
    rw [getD_rotate w R _ hn, hin, rotate_template_getD U R _ hg, hnmod]
    exact h.decrease
  · intro i hi hip' hin'
    have hi' : i < w.length := by simpa only [List.length_rotate] using hi
    rw [getD_rotate w R i hi']
    rw [h.unchanged ((i+R)%w.length) (Nat.mod_lt _ (by omega))
      (fun heq => hip' ((rotated_index_iff hR h.positive_lt hi').mp heq))
      (fun heq => hin' ((rotated_index_iff hR h.negative_lt hi').mp heq))]
    simp only [List.length_rotate]
    rw [rotate_template_getD U R i hg, h.length_eq, triple_mod]


theorem list_eq_of_getD_eq {A B : List ℕ} (hlen : A.length = B.length)
    (heq : ∀ i, i < A.length → A.getD i 0 = B.getD i 0) : A = B := by
  apply List.ext_getElem hlen
  intro i hi hi'
  simpa only [List.getD_eq_getElem A 0 hi, List.getD_eq_getElem B 0 hi'] using heq i hi

theorem getD_take (w : List ℕ) (g i : ℕ) (hi : i < g) :
    (w.take g).getD i 0 = w.getD i 0 := by
  simp only [List.getD_eq_getElem?_getD, List.getElem?_take_of_lt hi]

theorem triple_getD (U : List ℕ) (i : ℕ) (hi : i < 3*U.length) :
    (U ++ U ++ U).getD i 0 = U.getD (i%U.length) 0 := by
  by_cases h1 : i < U.length
  · rw [List.getD_append _ _ _ _ (by simp; omega), List.getD_append _ _ _ _ h1,
      Nat.mod_eq_of_lt h1]
  · by_cases h2 : i < 2*U.length
    · rw [List.getD_append _ _ _ _ (by simp; omega),
        List.getD_append_right _ _ _ _ (by omega),
        Nat.mod_eq_sub_mod (by omega), Nat.mod_eq_of_lt (by omega)]
    · rw [List.getD_append_right _ _ _ _ (by simp; omega)]
      simp only [List.length_append]
      rw [Nat.mod_eq_sub_mod (by omega), Nat.mod_eq_sub_mod (by omega),
        Nat.mod_eq_of_lt (by omega)]
      congr 1
      omega

theorem getD_set (w : List ℕ) (i j v : ℕ) (hj : j < w.length) :
    (w.set j v).getD i 0 = if j = i then v else w.getD i 0 := by
  simp only [List.getD_eq_getElem?_getD, List.getElem?_set, hj, ite_true]
  split <;> simp_all

theorem positive_rotate {w : List ℕ} (hw : Positive w) (R : ℕ) : Positive (w.rotate R) :=
  fun a ha => hw a (List.mem_rotate.mp ha)

theorem aligned_decomposition {w U : List ℕ} {p n d : ℕ}
    (h : BalancedPair w U p n d) (hp : p < U.length) (hn : n < U.length) :
    w = w.take U.length ++ U ++ U := by
  have ht : (w.take U.length).length = U.length := by
    rw [List.length_take]; have := h.length_eq; omega
  apply list_eq_of_getD_eq (by simp only [List.length_append, ht]; have := h.length_eq; omega)
  intro i hi
  by_cases hi1 : i < U.length
  · rw [List.getD_append _ _ _ _ (by simp only [List.length_append, ht]; omega),
      List.getD_append _ _ _ _ (by omega), getD_take w U.length i hi1]
  · rw [h.unchanged i hi (by omega) (by omega)]
    have heq : (w.take U.length ++ U ++ U).getD i 0 = (U ++ U ++ U).getD i 0 := by
      rw [List.append_assoc, List.append_assoc,
        List.getD_append_right (w.take U.length) (U ++ U) 0 i (by omega),
        List.getD_append_right U (U ++ U) 0 i (by omega), ht]
    rw [heq, triple_getD U i (by rw [←h.length_eq]; exact hi)]

theorem no_aligned_pair_cycle {w U : List ℕ} {p n d : ℕ} {x : ℕ → ℤ}
    (h : BalancedPair w U p n d) (hw : Positive w) (hU : Positive U)
    (hbal : w.sum = 3*U.sum) (hp : p < U.length) (hn : n < U.length)
    (hc : IsCycle 1 w x) : False := by
  let V := w.take U.length
  have ht : V.length = U.length := by
    dsimp [V]; rw [List.length_take]; have := h.length_eq; omega
  have hv : Positive V := fun a ha => hw a (List.mem_of_mem_take ha)
  have hdecomp : w = V ++ U ++ U := aligned_decomposition h hp hn
  have hsum : V.sum = U.sum := by rw [hdecomp] at hbal; simp only [List.sum_append] at hbal; omega
  have hne : U ≠ V := by
    intro heq
    have hinc := h.increase
    rw [Nat.mod_eq_of_lt hp] at hinc
    have hget : V.getD p 0 = w.getD p 0 := getD_take w U.length p hp
    rw [←heq] at hget
    have := h.delta_pos
    omega
  have hcr := hc.rotate V.length
  have hrot : w.rotate V.length = U ++ U ++ V := by
    rw [hdecomp, List.append_assoc, List.rotate_append_length_eq]
  rw [hrot] at hcr
  exact AlignedThirdPeriod.no_equal_total_cycle hU hv ht hsum hne hcr


theorem set_at_join (u v : List ℕ) (a b : ℕ) :
    (u ++ a::v).set u.length b = u ++ b::v := by
  rw [List.set_append_right _ _ (le_refl _)]
  simp

theorem word_as_updates (u v : List ℕ) (a b d : ℕ) :
    let U := block u a ++ block v (b+d)
    word u v a b d = ((U ++ U ++ U).set u.length (a+d)).set (2*U.length-1) b := by
  intro U
  have hfirst : (U ++ U ++ U).set u.length (a+d) =
      block u (a+d) ++ block v (b+d) ++ block u a ++ block v (b+d) ++
        block u a ++ block v (b+d) := by
    dsimp [U, block]
    simp only [List.append_assoc, List.cons_append]
    rw [set_at_join]
  let H := block u (a+d) ++ block v (b+d) ++ block u a ++ v
  let tail := block u a ++ block v (b+d)
  have hmiddle : block u (a+d) ++ block v (b+d) ++ block u a ++ block v (b+d) ++
        block u a ++ block v (b+d) = H ++ (b+d)::tail := by
    simp [H, tail, block, List.append_assoc]
  have hH : H.length = 2*U.length-1 := by simp [H, U, block]; omega
  rw [hfirst, hmiddle, ←hH, set_at_join]
  simp [word, H, tail, block, List.append_assoc]

theorem BalancedPair.as_updates {w U : List ℕ} {p n d : ℕ}
    (h : BalancedPair w U p n d) :
    w = ((U ++ U ++ U).set p (w.getD p 0)).set n (w.getD n 0) := by
  have hp : p < (U ++ U ++ U).length := by simp only [List.length_append]; have := h.positive_lt; have := h.length_eq; omega
  have hn : n < ((U ++ U ++ U).set p (w.getD p 0)).length := by
    simp only [List.length_set, List.length_append]; have := h.negative_lt; have := h.length_eq; omega
  apply list_eq_of_getD_eq (by simp only [List.length_set, List.length_append]; have := h.length_eq; omega)
  intro i hi
  rw [getD_set _ i n _ hn, getD_set _ i p _ hp]
  by_cases hin : n=i
  · subst i; simp
  · by_cases hip : p=i
    · subst i; simp [hin]
    · simp only [hin, hip, ite_false]
      rw [h.unchanged i hi (Ne.symm hip) (Ne.symm hin),
        triple_getD U i (by rw [←h.length_eq]; exact hi)]

theorem getD_last_block (u : List ℕ) (a : ℕ) : (block u a).getD u.length 0 = a := by
  rw [block, List.getD_append_right _ _ _ _ (le_refl _)]
  simp

theorem split_positive_block {U : List ℕ} (hU : Positive U) (hU0 : U ≠ []) :
    ∃ u a, Positive u ∧ 0<a ∧ U = block u a := by
  refine ⟨U.dropLast,U.getLast hU0,?_,hU _ (List.getLast_mem hU0),?_⟩
  · exact fun a ha => hU a (List.dropLast_subset U ha)
  · exact (List.dropLast_concat_getLast hU0).symm

theorem reconstruct_unaligned {w U : List ℕ} {l d : ℕ}
    (h : BalancedPair w U (l-1) (2*U.length-1) d)
    (hw : Positive w) (hU : Positive U) (hl : 0<l) (hlg : l<U.length) :
    ∃ u v a b, Positive u ∧ Positive v ∧ 0<a ∧ 0<b ∧ w = word u v a b d := by
  have htake : (U.take l).length = l := by simp [List.length_take, le_of_lt hlg]
  have hdrop : (U.drop l).length = U.length-l := List.length_drop
  obtain ⟨u,a,hu,ha,hA⟩ := split_positive_block
    (fun k hk => hU k (List.mem_of_mem_take hk)) (by intro he; rw [he] at htake; simp at htake; omega)
  obtain ⟨v,B,hv,hBpos,hB⟩ := split_positive_block
    (fun k hk => hU k (List.mem_of_mem_drop hk)) (by intro he; rw [he] at hdrop; simp at hdrop; omega)
  have hUeq : U = block u a ++ block v B := by rw [←hA, ←hB]; exact (List.take_append_drop l U).symm
  have hul : u.length+1=l := by rw [hA] at htake; simpa [block] using htake
  have hlenU : U.length = u.length+v.length+2 := by simp [hUeq, block]; omega
  have hlast : U.getD ((2*U.length-1)%U.length) 0 = B := by
    have hm : (2*U.length-1)%U.length=U.length-1 := by
      rw [Nat.mod_eq_sub_mod (by omega), Nat.mod_eq_of_lt (by omega)]
      omega
    rw [hm, hUeq, List.getD_append_right _ _ _ _ (by simp [block])]
    have hi : (block u a ++ block v B).length-1-(block u a).length=v.length := by simp [block]; omega
    rw [hi, getD_last_block]
  let b := w.getD (2*U.length-1) 0
  have hb : 0<b := getD_positive hw h.negative_lt
  have hBd : B=b+d := by have := h.decrease; rw [hlast] at this; exact this.symm
  have hplus : w.getD (l-1) 0=a+d := by
    have hi : l-1=u.length := by omega
    have hup : U.getD ((l-1)%U.length) 0=a := by
      rw [Nat.mod_eq_of_lt (by omega), hi, hUeq,
        List.getD_append _ _ _ _ (by simp [block]), getD_last_block]
    rw [h.increase, hup]
  refine ⟨u,v,a,b,hu,hv,ha,hb,?_⟩
  have hminus : w.getD (2*U.length-1) 0 = b := rfl
  rw [h.as_updates, hplus, hminus]
  have hi : l-1=u.length := by omega
  rw [hi, hUeq, hBd]
  exact (word_as_updates u v a b d).symm


theorem unaligned_cut {g j : ℕ} (hg : 0<g) (hj1 : g<j) (hj2 : j<2*g) :
    ∃ R l, R<3*g ∧ 0<l ∧ l<g ∧ backIndex (3*g) R 0=l-1 ∧
      backIndex (3*g) R j=2*g-1 := by
  refine ⟨if j+g+1=3*g then 0 else j+g+1, 2*g-j, ?_⟩
  split_ifs with heq
  · simp only [backIndex, Nat.zero_le, ite_true, Nat.sub_zero]
    omega
  · have hr : j+g+1<3*g := by omega
    have hz : ¬j+g+1≤0 := by omega
    have hj : ¬j+g+1≤j := by omega
    simp only [backIndex, hz, hj, ite_false]
    omega

theorem no_middle_pair_cycle {w U : List ℕ} {j d : ℕ} {x : ℕ → ℤ}
    (h : BalancedPair w U 0 j d) (hw : Positive w) (hU : Positive U)
    (hj1 : U.length<j) (hj2 : j<2*U.length)
    (hc : IsCycle 1 w x) (hx : ∀ i, 0<x i) (ho : ∀ i, Odd (x i)) : False := by
  obtain ⟨R,l,hR,hl,hlg,hp,hn⟩ := unaligned_cut (by omega : 0<U.length) hj1 hj2
  have hr := h.rotate (by rw [h.length_eq]; exact hR)
  rw [h.length_eq, hp, hn] at hr
  have hlgr : l<(U.rotate R).length := by simpa using hlg
  obtain ⟨u,v,a,b,hu,hv,ha,hb,heq⟩ := reconstruct_unaligned
    (by simpa only [List.length_rotate] using hr)
    (positive_rotate hw R) (positive_rotate hU R) hl hlgr
  have hc' := hc.rotate R
  rw [heq] at hc'
  exact ThirdPeriod.no_positive_odd_cycle hu hv ha hb h.delta_pos hc'
    (fun i => hx (i+R)) (fun i => ho (i+R))

theorem no_balanced_pair_cycle {w U : List ℕ} {p n d : ℕ} {x : ℕ → ℤ}
    (h : BalancedPair w U p n d) (hw : Positive w) (hU : Positive U)
    (hbal : w.sum=3*U.sum) (hc : IsCycle 1 w x)
    (hx : ∀ i, 0<x i) (ho : ∀ i, Odd (x i)) : False := by
  let W := w.rotate p
  let V := U.rotate p
  let j := backIndex w.length p n
  have hpair : BalancedPair W V 0 j d := by
    simpa only [W, V, j, backIndex, le_refl, ite_true, Nat.sub_self] using h.rotate h.positive_lt
  have hW : Positive W := positive_rotate hw p
  have hV : Positive V := positive_rotate hU p
  have hbalance : W.sum=3*V.sum := by
    dsimp [W,V]; rw [(List.rotate_perm w p).sum_eq, (List.rotate_perm U p).sum_eq]; exact hbal
  have hc' : IsCycle 1 W (fun i => x (i+p)) := hc.rotate p
  have hg : 0<V.length := by have := hpair.positive_lt; have := hpair.length_eq; omega
  have hj : j<3*V.length := by have := hpair.negative_lt; rwa [hpair.length_eq] at this
  have hne : j%V.length≠0 := by simpa using hpair.distinct_columns.symm
  have hj0 : 0<j := by
    by_contra hzero
    have hjz : j=0 := by omega
    simp [hjz] at hne
  have hjg : j≠V.length := by intro heq; simp [heq] at hne
  have hj2g : j≠2*V.length := by intro heq; simp [heq] at hne
  by_cases hj1 : j<V.length
  · exact no_aligned_pair_cycle hpair hW hV hbalance hg hj1 hc'
  · by_cases hj2 : j<2*V.length
    · exact no_middle_pair_cycle hpair hW hV (by omega) hj2 hc'
        (fun i => hx (i+p)) (fun i => ho (i+p))
    · have hR : j<W.length := hpair.negative_lt
      have hr := hpair.rotate hR
      have hp : backIndex W.length j 0=W.length-j := by simp [backIndex, Nat.not_le.mpr hj0]
      have hn : backIndex W.length j j=0 := by simp [backIndex]
      rw [hp,hn] at hr
      have hpbound : W.length-j<(V.rotate j).length := by
        have he := hpair.length_eq
        have hvlen : (V.rotate j).length=V.length := List.length_rotate V j
        rw [hvlen]
        omega
      have hnbound : 0<(V.rotate j).length := by simpa using hg
      have hbalance' : (W.rotate j).sum=3*(V.rotate j).sum := by
        rw [(List.rotate_perm W j).sum_eq, (List.rotate_perm V j).sum_eq]; exact hbalance
      exact no_aligned_pair_cycle hr (positive_rotate hW j) (positive_rotate hV j)
        hbalance' hpbound hnbound (hc'.rotate j)

/-- The full balanced third-period obstruction, before any placement is assumed. -/
theorem no_positive_odd_cycle {w : List ℕ} {g : ℕ} {x : ℕ → ℤ}
    (hw : Positive w) (hlen : w.length=3*g) (hmis : mismatches w g=4)
    (hbal : w.sum=3*(majorityTemplate w g).sum)
    (hc : IsCycle 1 w x) (hx : ∀ i, 0<x i) (ho : ∀ i, Odd (x i)) : False := by
  have hg : 0<g := by
    by_contra hz
    have hgz : g=0 := by omega
    have hwz : w=[] := List.length_eq_zero_iff.mp (by omega)
    subst w
    simp [mismatches] at hmis
  obtain ⟨p,n,d,hpair⟩ := balanced_pair_of_mismatches hg hlen hmis hbal
  exact no_balanced_pair_cycle hpair hw (majority_positive hw hlen) hbal hc hx ho

/-- The denominator-one exclusion for intrinsically balanced words of length `3g`. -/
theorem discriminant_not_dvd_intercept {w : List ℕ} {g : ℕ}
    (hw : Positive w) (hlen : w.length=3*g) (hmis : mismatches w g=4)
    (hbal : w.sum=3*(majorityTemplate w g).sum) (hD : 0<D w) : ¬ D w ∣ C w := by
  intro hdiv
  have hw0 : w≠[] := by intro he; simp [he,mismatches] at hmis
  obtain ⟨x,hc,hx,ho⟩ := integral_cycle_of_dvd hw0 hw hD hdiv
  exact no_positive_odd_cycle hw hlen hmis hbal hc hx ho


/-- Both placements occur in actual positive-addend cycles and satisfy the intrinsic hypotheses. -/
theorem balanced_control_words :
    mismatches [2,3,2,3,3,2] 2=4 ∧ majorityTemplate [2,3,2,3,3,2] 2=[2,3] ∧
    ([2,3,2,3,3,2] : List ℕ).sum=3*([2,3] : List ℕ).sum ∧
    mismatches [3,3,2,2,2,3] 2=4 ∧ majorityTemplate [3,3,2,2,2,3] 2=[2,3] ∧
    ([3,3,2,2,2,3] : List ℕ).sum=3*([2,3] : List ℕ).sum := by decide

theorem balanced_positive_addend_controls :
    (∃ x : ℕ → ℤ, IsCycle 32039 [2,3,2,3,3,2] x ∧ (∀ i, 0<x i)) ∧
    (∃ x : ℕ → ℤ, IsCycle 32039 [3,3,2,2,2,3] x ∧ (∀ i, 0<x i)) := by
  constructor
  · exact AlignedThirdPeriod.aligned_positive_addend_control
  · exact ThirdPeriod.positive_addend_control

end LeanLane.BalancedThirdPeriod

#print axioms LeanLane.AlignedThirdPeriod.equal_intercepts_of_dvd
#print axioms LeanLane.AlignedThirdPeriod.balanced_edit_difference
#print axioms LeanLane.AlignedThirdPeriod.balanced_edit_intercepts_ne
#print axioms LeanLane.AlignedThirdPeriod.aligned_discriminant_not_dvd
#print axioms LeanLane.AlignedThirdPeriod.aligned_positive_addend_control
#print axioms LeanLane.AlignedThirdPeriod.aligned_control_intercepts
#print axioms LeanLane.AlignedThirdPeriod.C_odd
#print axioms LeanLane.AlignedThirdPeriod.C_injective
#print axioms LeanLane.AlignedThirdPeriod.no_equal_total_cycle
#print axioms LeanLane.BalancedThirdPeriod.majority_length
#print axioms LeanLane.BalancedThirdPeriod.count_range
#print axioms LeanLane.BalancedThirdPeriod.three_sum_blocks
#print axioms LeanLane.BalancedThirdPeriod.mismatches_column_sum
#print axioms LeanLane.BalancedThirdPeriod.triangle_values
#print axioms LeanLane.BalancedThirdPeriod.triangle_nonzero_lower
#print axioms LeanLane.BalancedThirdPeriod.triangle_upper
#print axioms LeanLane.BalancedThirdPeriod.triangle_majority_deviations
#print axioms LeanLane.BalancedThirdPeriod.count_four_bounds
#print axioms LeanLane.BalancedThirdPeriod.column_bounds
#print axioms LeanLane.BalancedThirdPeriod.majority_getD
#print axioms LeanLane.BalancedThirdPeriod.getD_positive
#print axioms LeanLane.BalancedThirdPeriod.majority_positive
#print axioms LeanLane.BalancedThirdPeriod.two_deviations
#print axioms LeanLane.BalancedThirdPeriod.exceptional_positions
#print axioms LeanLane.BalancedThirdPeriod.three_residue_cases
#print axioms LeanLane.BalancedThirdPeriod.exceptional_columns_distinct
#print axioms LeanLane.BalancedThirdPeriod.sum_periodic_template
#print axioms LeanLane.BalancedThirdPeriod.paired_values_of_sum
#print axioms LeanLane.BalancedThirdPeriod.balanced_pair_of_mismatches
#print axioms LeanLane.BalancedThirdPeriod.backIndex_lt
#print axioms LeanLane.BalancedThirdPeriod.rotated_index_iff
#print axioms LeanLane.BalancedThirdPeriod.backIndex_inverse
#print axioms LeanLane.BalancedThirdPeriod.rotate_template_getD
#print axioms LeanLane.BalancedThirdPeriod.triple_mod
#print axioms LeanLane.BalancedThirdPeriod.BalancedPair.rotate
#print axioms LeanLane.BalancedThirdPeriod.list_eq_of_getD_eq
#print axioms LeanLane.BalancedThirdPeriod.getD_take
#print axioms LeanLane.BalancedThirdPeriod.triple_getD
#print axioms LeanLane.BalancedThirdPeriod.getD_set
#print axioms LeanLane.BalancedThirdPeriod.positive_rotate
#print axioms LeanLane.BalancedThirdPeriod.aligned_decomposition
#print axioms LeanLane.BalancedThirdPeriod.no_aligned_pair_cycle
#print axioms LeanLane.BalancedThirdPeriod.set_at_join
#print axioms LeanLane.BalancedThirdPeriod.word_as_updates
#print axioms LeanLane.BalancedThirdPeriod.BalancedPair.as_updates
#print axioms LeanLane.BalancedThirdPeriod.getD_last_block
#print axioms LeanLane.BalancedThirdPeriod.split_positive_block
#print axioms LeanLane.BalancedThirdPeriod.reconstruct_unaligned
#print axioms LeanLane.BalancedThirdPeriod.unaligned_cut
#print axioms LeanLane.BalancedThirdPeriod.no_middle_pair_cycle
#print axioms LeanLane.BalancedThirdPeriod.no_balanced_pair_cycle
#print axioms LeanLane.BalancedThirdPeriod.no_positive_odd_cycle
#print axioms LeanLane.BalancedThirdPeriod.discriminant_not_dvd_intercept
#print axioms LeanLane.BalancedThirdPeriod.balanced_control_words
#print axioms LeanLane.BalancedThirdPeriod.balanced_positive_addend_controls
