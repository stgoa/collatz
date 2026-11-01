import LeanLane.SaturatedDensity

/-!
# `LeanLane.SaturatedScaling`: saturated sets meet every class modulo `2^k 3^b M'` when `3 ∤ ord_{M'}(2)`

Formal companion of `areas/invariants/results/saturated-sets-residue-classes-order-of-two-prime-to-three`.
The scaling move `scale s z = (4^s (3z+1) - 1)/3` (forward step, `2s` doublings, one inverse step) and the inverse
move `inv j z = (2^j z - 1)/3`, their legality, the free steering of the 3-adic class, the translation by `2/3`
modulo `M'`, and the theorem `saturated_dense_of_order_prime_to_three`.
-/

namespace LeanLane
namespace SaturatedScaling

open LeanLane.SaturatedDensity

/-- The scaling move. -/
def scale (s z : ℕ) : ℕ := (4 ^ s * (3 * z + 1) - 1) / 3

/-- The inverse move. -/
def inv (j z : ℕ) : ℕ := (2 ^ j * z - 1) / 3

theorem four_pow_mod_three (s : ℕ) : 4 ^ s % 3 = 1 := by
  induction s with
  | zero => rfl
  | succ s ih => rw [pow_succ, Nat.mul_mod, ih]

theorem three_scale_add_one (s z : ℕ) : 3 * scale s z + 1 = 4 ^ s * (3 * z + 1) := by
  unfold scale
  have h := four_pow_mod_three s
  have hX : (4 ^ s * (3 * z + 1)) % 3 = 1 := by rw [Nat.mul_mod, h]; omega
  have hpos : 1 ≤ 4 ^ s * (3 * z + 1) := Nat.one_le_iff_ne_zero.mpr (by positivity)
  omega

theorem three_inv_add_one (j z : ℕ) (h : 2 ^ j * z % 3 = 1) : 3 * inv j z + 1 = 2 ^ j * z := by
  unfold inv
  have hpos : 1 ≤ 2 ^ j * z := by
    rcases Nat.eq_zero_or_pos (2 ^ j * z) with h0 | h0
    · rw [h0] at h; omega
    · exact h0
  omega

variable {B : Set ℕ} (hB : Saturated B)
include hB

theorem scale_mem {z : ℕ} (hz : z ∈ B) (hodd : z % 2 = 1) (s : ℕ) : scale s z ∈ B := by
  have h1 : 3 * z + 1 ∈ B := mem_forward hB hz hodd
  have h2 : 2 ^ (2 * s) * (3 * z + 1) ∈ B := mem_pow_double hB h1 (2 * s)
  have h4 : (4 : ℕ) ^ s = 2 ^ (2 * s) := by rw [pow_mul]; norm_num
  have hX6 : 4 ^ s * (3 * z + 1) % 6 = 4 := by
    have hm3 : (4 ^ s * (3 * z + 1)) % 3 = 1 := by rw [Nat.mul_mod, four_pow_mod_three]; omega
    have hm2 : (4 ^ s * (3 * z + 1)) % 2 = 0 := by
      have : (3 * z + 1) % 2 = 0 := by omega
      rw [Nat.mul_mod, this]; simp
    omega
  have := mem_inverse hB (h4 ▸ h2) hX6
  simpa [scale] using this

omit hB in
theorem scale_odd (s z : ℕ) (hodd : z % 2 = 1) : scale s z % 2 = 1 := by
  have h := three_scale_add_one s z
  have : (4 ^ s * (3 * z + 1)) % 2 = 0 := by
    have : (3 * z + 1) % 2 = 0 := by omega
    rw [Nat.mul_mod, this]; simp
  omega

theorem inv_mem {z : ℕ} (hz : z ∈ B) (j : ℕ) (hj : 1 ≤ j) (h3 : 2 ^ j * z % 3 = 1) : inv j z ∈ B := by
  have hX : 2 ^ j * z ∈ B := mem_pow_double hB hz j
  have hX6 : 2 ^ j * z % 6 = 4 := by
    have h2 : 2 ^ j * z % 2 = 0 := by
      obtain ⟨j', rfl⟩ : ∃ j', j = j' + 1 := ⟨j - 1, by omega⟩
      rw [pow_succ, show 2 ^ j' * 2 * z = 2 * (2 ^ j' * z) by ring]; exact Nat.mul_mod_right 2 _
    omega
  exact mem_inverse hB hX hX6

omit hB in
theorem inv_odd (j z : ℕ) (h3 : 2 ^ j * z % 3 = 1) (hj : 1 ≤ j) : inv j z % 2 = 1 := by
  have h := three_inv_add_one j z h3
  have h2 : 2 ^ j * z % 2 = 0 := by
    obtain ⟨j', rfl⟩ : ∃ j', j = j' + 1 := ⟨j - 1, by omega⟩
    rw [pow_succ, show 2 ^ j' * 2 * z = 2 * (2 ^ j' * z) by ring]; exact Nat.mul_mod_right 2 _
  omega

omit hB

/-- `a^n ≡ 1` and `k ≡ k'` modulo `n` give `a^k ≡ a^k'`. -/
theorem pow_modEq_of_exp_modEq {a n m k k' : ℕ} (h1 : a ^ n ≡ 1 [MOD m]) (hn : 0 < n) (h : k ≡ k' [MOD n]) :
    a ^ k ≡ a ^ k' [MOD m] := by
  have key : ∀ t, a ^ t ≡ a ^ (t % n) [MOD m] := by
    intro t
    conv_lhs => rw [← Nat.div_add_mod t n, pow_add, pow_mul]
    have := (h1.pow (t / n)).mul_right (a ^ (t % n))
    simpa using this
  have hk := key k
  have hk' := key k'
  unfold Nat.ModEq at h
  rw [h] at hk
  exact hk.trans hk'.symm

/-- `4^(3^B) ≡ 1 (mod 3^(B+1))`. -/
theorem four_pow_three_pow_modEq (Bexp : ℕ) : 4 ^ (3 ^ Bexp) ≡ 1 [MOD 3 ^ (Bexp + 1)] := by
  obtain ⟨m, hm⟩ := four_pow_three_pow Bexp
  rw [Nat.ModEq.comm, Nat.modEq_iff_dvd]
  push_cast
  rw [hm]
  exact ⟨1 + 3 * m, by ring⟩

/-- Free steering: when `4^T ≡ 1 (mod M')` with `3 ∤ T`, a scaling exponent `s ≥ 1` exists that is trivial modulo `M'`
and sends `3z + 1` to any prescribed class `τ ≡ 1 (mod 3)` modulo `3^(B+1)`. -/
theorem exists_free_exponent (M' T : ℕ) (hT : 0 < T) (h3T : ¬ 3 ∣ T) (hTpow : 4 ^ T ≡ 1 [MOD M'])
    (z : ℕ) (Bexp τ : ℕ) (hτ : τ % 3 = 1) :
    ∃ s, 1 ≤ s ∧ 4 ^ s ≡ 1 [MOD M'] ∧ 4 ^ s * (3 * z + 1) ≡ τ [MOD 3 ^ (Bexp + 1)] := by
  -- a power of two does the 3-adic job
  have hy : ¬ (3 : ℤ) ∣ ((3 * z + 1 : ℕ) : ℤ) := by push_cast; omega
  have hη : ¬ (3 : ℤ) ∣ (τ : ℤ) := by omega
  obtain ⟨j, hj, hdvd⟩ := two_pow_mul_surj ((3 * z + 1 : ℕ) : ℤ) (τ : ℤ) hy hη Bexp
  have hmod : τ ≡ 2 ^ j * (3 * z + 1) [MOD 3 ^ (Bexp + 1)] := by
    rw [Nat.modEq_iff_dvd]; push_cast at hdvd ⊢; exact hdvd
  -- j is even
  have hmod3 : τ ≡ 2 ^ j * (3 * z + 1) [MOD 3] := Nat.ModEq.of_dvd (dvd_pow_self 3 (Nat.succ_ne_zero Bexp)) hmod
  have hjeven : j % 2 = 0 := by
    by_contra hodd
    have hodd' : j % 2 = 1 := by omega
    have h2j : 2 ^ j % 3 = 2 := by
      conv_lhs => rw [← Nat.div_add_mod j 2, pow_add, pow_mul, hodd']
      rw [Nat.mul_mod, Nat.pow_mod]; norm_num
    unfold Nat.ModEq at hmod3
    rw [Nat.mul_mod, h2j] at hmod3
    omega
  obtain ⟨s₀, hs₀⟩ : ∃ s₀, j = 2 * s₀ := ⟨j / 2, by omega⟩
  have h4s₀ : 4 ^ s₀ * (3 * z + 1) ≡ τ [MOD 3 ^ (Bexp + 1)] := by
    have : (4 : ℕ) ^ s₀ = 2 ^ j := by rw [hs₀, pow_mul]; norm_num
    rw [this]; exact hmod.symm
  -- Chinese remainder: s ≡ s₀ (mod 3^B), s ≡ 0 (mod T)
  have hcop : Nat.Coprime (3 ^ Bexp) T := by
    apply Nat.Coprime.pow_left
    exact (Nat.Prime.coprime_iff_not_dvd Nat.prime_three).mpr h3T
  obtain ⟨k, hk1, hk2⟩ := Nat.chineseRemainder hcop s₀ 0
  refine ⟨k + 3 ^ Bexp * T, by have : 0 < 3 ^ Bexp * T := by positivity
                               omega, ?_, ?_⟩
  · -- 4^s ≡ 1 mod M': T divides s
    have hTdvd : T ∣ k + 3 ^ Bexp * T := by
      have : T ∣ k := (Nat.modEq_zero_iff_dvd.mp hk2)
      exact dvd_add this (dvd_mul_left T _)
    obtain ⟨q, hq⟩ := hTdvd
    rw [hq, pow_mul]
    simpa using hTpow.pow q
  · -- 4^s ≡ 4^s₀ mod 3^(B+1)
    have hexp : k + 3 ^ Bexp * T ≡ s₀ [MOD 3 ^ Bexp] := by
      have : k + 3 ^ Bexp * T ≡ k + 0 [MOD 3 ^ Bexp] :=
        Nat.ModEq.add_left k (Nat.modEq_zero_iff_dvd.mpr (dvd_mul_right _ _))
      simpa using this.trans hk1
    have h4 := pow_modEq_of_exp_modEq (four_pow_three_pow_modEq Bexp) (by positivity) hexp
    exact (h4.mul_right _).trans h4s₀


/-! ## Modulo `M'`: parity fixes, inverse steps, scalings, the translation, every class -/

section Modular

variable (M' : ℕ) [NeZero M'] (hM6 : Nat.Coprime M' 6)
variable (T : ℕ) (hT : 0 < T) (h3T : ¬ 3 ∣ T) (hTpow : 4 ^ T ≡ 1 [MOD M'])
include hM6

theorem two_isUnit : IsUnit (2 : ZMod M') := by
  have h : Nat.Coprime 2 M' := Nat.Coprime.coprime_dvd_left (by norm_num : 2 ∣ 6) hM6.symm
  have := (ZMod.isUnit_iff_coprime 2 M').mpr h
  simpa using this

theorem three_isUnit : IsUnit (3 : ZMod M') := by
  have h : Nat.Coprime 3 M' := Nat.Coprime.coprime_dvd_left (by norm_num : 3 ∣ 6) hM6.symm
  have := (ZMod.isUnit_iff_coprime 3 M').mpr h
  simpa using this

omit hM6

theorem four_pow_s_cast {s : ℕ} (hs : 4 ^ s ≡ 1 [MOD M']) : ((4 : ZMod M')) ^ s = 1 := by
  have := (ZMod.natCast_eq_natCast_iff _ _ _).mpr hs
  simpa using this

include hTpow

theorem four_pow_T_cast : ((4 : ZMod M')) ^ T = 1 := by
  have := (ZMod.natCast_eq_natCast_iff _ _ _).mpr hTpow
  simpa using this

omit hTpow
include hB hM6

/-- A scaling step and its effect modulo `M'`. -/
theorem exists_scale_step {z : ℕ} (hz : z ∈ B) (hodd : z % 2 = 1) (s : ℕ) :
    ∃ z' ∈ B, z' % 2 = 1 ∧ (3 : ZMod M') * z' + 1 = 4 ^ s * (3 * z + 1) := by
  refine ⟨scale s z, scale_mem hB hz hodd s, scale_odd s z hodd, ?_⟩
  have h := three_scale_add_one s z
  have hc : ((3 * scale s z + 1 : ℕ) : ZMod M') = ((4 ^ s * (3 * z + 1) : ℕ) : ZMod M') := by rw [h]
  push_cast at hc
  exact hc

include hT h3T hTpow

/-- A parity fix: a scaling that is the identity modulo `M'` and makes the element `≡ 2 (mod 3)`. -/
theorem exists_parity_fix {z : ℕ} (hz : z ∈ B) (hodd : z % 2 = 1) :
    ∃ z' ∈ B, z' % 2 = 1 ∧ z' % 3 = 2 ∧ (z' : ZMod M') = (z : ZMod M') := by
  obtain ⟨s, hs1, hsM, hs9⟩ := exists_free_exponent M' T hT h3T hTpow z 1 7 (by norm_num)
  refine ⟨scale s z, scale_mem hB hz hodd s, scale_odd s z hodd, ?_, ?_⟩
  · have h := three_scale_add_one s z
    have : (3 * scale s z + 1) % 9 = 7 := by
      rw [h]; unfold Nat.ModEq at hs9; simpa using hs9
    omega
  · have h := three_scale_add_one s z
    have hc : ((3 * scale s z + 1 : ℕ) : ZMod M') = ((4 ^ s * (3 * z + 1) : ℕ) : ZMod M') := by rw [h]
    push_cast at hc
    rw [four_pow_s_cast M' hsM, one_mul] at hc
    have h3 : (3 : ZMod M') * (scale s z : ZMod M') = 3 * (z : ZMod M') := by linear_combination hc
    exact (three_isUnit M' hM6).mul_left_cancel h3

/-- An inverse step (after a parity fix) and its effect modulo `M'`: `3 z' = 2 z − 1`. -/
theorem exists_inv_step {z : ℕ} (hz : z ∈ B) (hodd : z % 2 = 1) :
    ∃ z' ∈ B, z' % 2 = 1 ∧ (3 : ZMod M') * z' = 2 * z - 1 := by
  obtain ⟨z₁, hz₁, hodd₁, h3₁, hc₁⟩ := exists_parity_fix hB M' hM6 T hT h3T hTpow hz hodd
  have hleg : 2 ^ 1 * z₁ % 3 = 1 := by omega
  refine ⟨inv 1 z₁, inv_mem hB hz₁ 1 le_rfl hleg, inv_odd 1 z₁ hleg le_rfl, ?_⟩
  have h := three_inv_add_one 1 z₁ hleg
  have hc : ((3 * inv 1 z₁ + 1 : ℕ) : ZMod M') = ((2 ^ 1 * z₁ : ℕ) : ZMod M') := by rw [h]
  push_cast at hc
  rw [hc₁] at hc
  linear_combination hc

/-- `n` inverse steps: `3^n (z' + 1) = 2^n (z + 1)` modulo `M'`. -/
theorem exists_inv_iter {z : ℕ} (hz : z ∈ B) (hodd : z % 2 = 1) (n : ℕ) :
    ∃ z' ∈ B, z' % 2 = 1 ∧ (3 : ZMod M') ^ n * (z' + 1) = 2 ^ n * (z + 1) := by
  induction n with
  | zero => exact ⟨z, hz, hodd, by simp⟩
  | succ n ih =>
    obtain ⟨z', hz', hodd', heq⟩ := ih
    obtain ⟨z'', hz'', hodd'', heq''⟩ := exists_inv_step hB M' hM6 T hT h3T hTpow hz' hodd'
    refine ⟨z'', hz'', hodd'', ?_⟩
    rw [pow_succ, pow_succ]
    linear_combination (3 : ZMod M') ^ n * heq'' + 2 * heq

/-- The translation: an odd element with `3 z' = 3 z + 2` modulo `M'`. -/
theorem exists_translate {z : ℕ} (hz : z ∈ B) (hodd : z % 2 = 1) :
    ∃ z' ∈ B, z' % 2 = 1 ∧ (3 : ZMod M') * z' = 3 * z + 2 := by
  have h2 := two_isUnit M' hM6
  have h3 := three_isUnit M' hM6
  have h4T := four_pow_T_cast M' T hTpow
  -- an exponent N with 2^N = 3^N in ZMod M'
  have h2cop : Nat.Coprime 2 M' := Nat.Coprime.coprime_dvd_left (by norm_num : 2 ∣ 6) hM6.symm
  have h3cop : Nat.Coprime 3 M' := Nat.Coprime.coprime_dvd_left (by norm_num : 3 ∣ 6) hM6.symm
  set u2 := ZMod.unitOfCoprime 2 h2cop with hu2
  set u3 := ZMod.unitOfCoprime 3 h3cop with hu3
  set N := orderOf u2 * orderOf u3 with hN
  have hNpos : 0 < N := Nat.mul_pos (orderOf_pos u2) (orderOf_pos u3)
  have h2N : (2 : ZMod M') ^ N = 1 := by
    have : u2 ^ N = 1 := by rw [hN, pow_mul, pow_orderOf_eq_one, one_pow]
    have := congrArg Units.val this
    simpa [hu2, ZMod.coe_unitOfCoprime] using this
  have h3N : (3 : ZMod M') ^ N = 1 := by
    have : u3 ^ N = 1 := by rw [hN, mul_comm, pow_mul, pow_orderOf_eq_one, one_pow]
    have := congrArg Units.val this
    simpa [hu3, ZMod.coe_unitOfCoprime] using this
  obtain ⟨N', hN'⟩ : ∃ N', N = N' + 1 := ⟨N - 1, by omega⟩
  -- step 1: scale by T - 1
  obtain ⟨z₁, hz₁, hodd₁, heq₁⟩ := exists_scale_step hB M' hM6 hz hodd (T - 1)
  have hz₁' : (4 : ZMod M') * (z₁ : ZMod M') = z - 1 := by
    have h4 : (4 : ZMod M') * (4 ^ (T - 1)) = 1 := by
      rw [← pow_succ', Nat.sub_add_cancel hT, h4T]
    have : (3 : ZMod M') * (4 * z₁) = 3 * (z - 1) := by
      linear_combination 4 * heq₁ + (3 * (z : ZMod M') + 1) * h4
    exact h3.mul_left_cancel this
  -- step 2: N - 1 inverse steps
  obtain ⟨z₂, hz₂, hodd₂, heq₂⟩ := exists_inv_iter hB M' hM6 T hT h3T hTpow hz₁ hodd₁ N'
  have hz₂' : (2 : ZMod M') * z₂ = 3 * z₁ + 1 := by
    have hu : IsUnit ((2 : ZMod M') ^ N') := h2.pow N'
    have : (2 : ZMod M') ^ N' * (2 * z₂) = 2 ^ N' * (3 * z₁ + 1) := by
      have e1 : (3 : ZMod M') ^ N * (z₂ + 1) = 3 * 2 ^ N' * (z₁ + 1) := by
        rw [hN', pow_succ]; linear_combination 3 * heq₂
      rw [h3N] at e1
      have e2 : (2 : ZMod M') ^ N' * 2 = 1 := by rw [← pow_succ, ← hN', h2N]
      linear_combination ((z₂ : ZMod M') + 1) * e2 + e1
    exact hu.mul_left_cancel this
  -- step 3: scale by 1
  obtain ⟨z₃, hz₃, hodd₃, heq₃⟩ := exists_scale_step hB M' hM6 hz₂ hodd₂ 1
  have hz₃' : (z₃ : ZMod M') = 4 * z₂ + 1 := by
    have : (3 : ZMod M') * z₃ = 3 * (4 * z₂ + 1) := by linear_combination heq₃
    exact h3.mul_left_cancel this
  -- step 4: one inverse step
  obtain ⟨z₄, hz₄, hodd₄, heq₄⟩ := exists_inv_step hB M' hM6 T hT h3T hTpow hz₃ hodd₃
  refine ⟨z₄, hz₄, hodd₄, ?_⟩
  -- 3 z₄ = 2 z₃ - 1 = 8 z₂ + 1 = 4 (3 z₁ + 1) + 1 = 3 z + 2
  have h4z₁ : (4 : ZMod M') * (3 * z₁ + 1) = 3 * z + 1 := by linear_combination 3 * hz₁'
  linear_combination heq₄ + 2 * hz₃' + 4 * hz₂' + h4z₁

/-- Every class modulo `M'` contains an odd element of `B`. -/
theorem exists_class (hne : B.Nonempty) (ρ : ZMod M') : ∃ z ∈ B, z % 2 = 1 ∧ (z : ZMod M') = ρ := by
  obtain ⟨z₀, hz₀, hodd₀⟩ := exists_odd hB hne
  have h2 := two_isUnit M' hM6
  have h3 := three_isUnit M' hM6
  -- t translations give 3 z_t = 3 z₀ + 2 t
  have iter : ∀ t : ℕ, ∃ z ∈ B, z % 2 = 1 ∧ (3 : ZMod M') * z = 3 * z₀ + 2 * t := by
    intro t
    induction t with
    | zero => exact ⟨z₀, hz₀, hodd₀, by simp⟩
    | succ t ih =>
      obtain ⟨z, hz, hodd, heq⟩ := ih
      obtain ⟨z', hz', hodd', heq'⟩ := exists_translate hB M' hM6 T hT h3T hTpow hz hodd
      refine ⟨z', hz', hodd', ?_⟩
      push_cast
      linear_combination heq' + heq
  set t : ℕ := ((3 * (ρ - z₀) : ZMod M') * (2 : ZMod M')⁻¹).val with ht
  obtain ⟨z, hz, hodd, heq⟩ := iter t
  refine ⟨z, hz, hodd, ?_⟩
  have htc : (t : ZMod M') = (3 * (ρ - z₀)) * (2 : ZMod M')⁻¹ := by rw [ht, ZMod.natCast_zmod_val]
  have h2inv : (2 : ZMod M') * (2 : ZMod M')⁻¹ = 1 := ZMod.mul_inv_of_unit _ h2
  have : (3 : ZMod M') * z = 3 * ρ := by
    rw [heq, htc]
    linear_combination (3 * (ρ - (z₀ : ZMod M'))) * h2inv
  exact h3.mul_left_cancel this

/-- The base case: an element of `B` in every class modulo `3^b M'`. -/
theorem exists_modEq_three_pow_mul (hne : B.Nonempty) (b ε : ℕ) : ∃ x ∈ B, x ≡ ε [MOD 3 ^ b * M'] := by
  have h3 := three_isUnit M' hM6
  obtain ⟨z, hz, hodd, hρ⟩ := exists_class hB M' hM6 T hT h3T hTpow hne (ε : ZMod M')
  obtain ⟨s, hs1, hsM, hs3⟩ := exists_free_exponent M' T hT h3T hTpow z b (1 + 3 * ε) (by omega)
  refine ⟨scale s z, scale_mem hB hz hodd s, ?_⟩
  have hcop : Nat.Coprime (3 ^ b) M' :=
    Nat.Coprime.pow_left _ (Nat.Coprime.coprime_dvd_left (by norm_num : 3 ∣ 6) hM6.symm)
  apply (Nat.modEq_and_modEq_iff_modEq_mul hcop).1
  constructor
  · -- modulo 3^b
    have h := three_scale_add_one s z
    have h1 : 3 * scale s z + 1 ≡ 3 * ε + 1 [MOD 3 ^ (b + 1)] := by
      rw [h]; convert hs3 using 1; ring
    have h2 : 3 * scale s z ≡ 3 * ε [MOD 3 * 3 ^ b] := by
      rw [← pow_succ']; exact Nat.ModEq.add_right_cancel' 1 h1
    exact Nat.ModEq.mul_left_cancel' (by norm_num) h2
  · -- modulo M'
    rw [← ZMod.natCast_eq_natCast_iff]
    have h := three_scale_add_one s z
    have hc : ((3 * scale s z + 1 : ℕ) : ZMod M') = ((4 ^ s * (3 * z + 1) : ℕ) : ZMod M') := by rw [h]
    push_cast at hc
    rw [four_pow_s_cast M' hsM, one_mul, hρ] at hc
    have : (3 : ZMod M') * (scale s z : ZMod M') = 3 * (ε : ZMod M') := by linear_combination hc
    exact h3.mul_left_cancel this

end Modular

/-! ## The 2-adic lift with an odd modulus `3^b M'` -/

section Lift

variable (M' : ℕ) (hM'odd : M' % 2 = 1)
include hB hM'odd

theorem exists_modEq_pow_mul (hbase : ∀ b ε : ℕ, ∃ x ∈ B, x ≡ ε [MOD 3 ^ b * M']) :
    ∀ k b r ε : ℕ, ∃ x ∈ B, x ≡ r [MOD 2 ^ k] ∧ x ≡ ε [MOD 3 ^ b * M'] := by
  intro k
  induction k with
  | zero =>
    intro b r ε
    obtain ⟨x, hx, hmod⟩ := hbase b ε
    exact ⟨x, hx, by simp [Nat.modEq_one], hmod⟩
  | succ k ih =>
    intro b r ε
    have hodd3 : (3 ^ b * M') % 2 = 1 := by
      have : (3 ^ b) % 2 = 1 := Nat.odd_iff.mp (Odd.pow (by decide))
      rw [Nat.mul_mod, this, hM'odd]
    have hodd3' : (3 ^ (b + 1) * M') % 2 = 1 := by
      have : (3 ^ (b + 1)) % 2 = 1 := Nat.odd_iff.mp (Odd.pow (by decide))
      rw [Nat.mul_mod, this, hM'odd]
    by_cases hr : r % 2 = 0
    · obtain ⟨y, hy, hy2, hy3⟩ := ih b (r / 2) (ε * ((3 ^ b * M' + 1) / 2))
      refine ⟨2 * y, mem_double hB hy, ?_, ?_⟩
      · have := Nat.ModEq.mul_left' 2 hy2
        rw [pow_succ']; convert this using 2; omega
      · have := Nat.ModEq.mul_left 2 hy3
        refine this.trans ?_
        have h2 : 2 * (ε * ((3 ^ b * M' + 1) / 2)) = ε + ε * (3 ^ b * M') := by
          generalize 3 ^ b * M' = m at hodd3 ⊢
          have : 2 * ((m + 1) / 2) = m + 1 := by omega
          calc 2 * (ε * ((m + 1) / 2)) = ε * (2 * ((m + 1) / 2)) := by ring
            _ = ε * (m + 1) := by rw [this]
            _ = ε + ε * m := by ring
        rw [h2]; exact Nat.add_mul_mod_self_right ε ε (3 ^ b * M')
    · obtain ⟨y, hy, hy2, hy3⟩ :=
        ih (b + 1) ((3 * r + 1) / 2) ((1 + 3 * ε) * ((3 ^ (b + 1) * M' + 1) / 2))
      set X := 2 * y with hXdef
      have hX : X ∈ B := mem_double hB hy
      have hX2 : X ≡ 3 * r + 1 [MOD 2 ^ (k + 1)] := by
        have := Nat.ModEq.mul_left' 2 hy2
        rw [pow_succ']; convert this using 2; omega
      have hX3 : X ≡ 1 + 3 * ε [MOD 3 ^ (b + 1) * M'] := by
        have := Nat.ModEq.mul_left 2 hy3
        refine this.trans ?_
        have h2 : 2 * ((1 + 3 * ε) * ((3 ^ (b + 1) * M' + 1) / 2)) =
            (1 + 3 * ε) + (1 + 3 * ε) * (3 ^ (b + 1) * M') := by
          generalize 3 ^ (b + 1) * M' = m at hodd3' ⊢
          have : 2 * ((m + 1) / 2) = m + 1 := by omega
          calc 2 * ((1 + 3 * ε) * ((m + 1) / 2)) = (1 + 3 * ε) * (2 * ((m + 1) / 2)) := by ring
            _ = (1 + 3 * ε) * (m + 1) := by rw [this]
            _ = (1 + 3 * ε) + (1 + 3 * ε) * m := by ring
        rw [h2]; exact Nat.add_mul_mod_self_right _ _ _
      have hmod3 : X ≡ 1 + 3 * ε [MOD 3] :=
        Nat.ModEq.of_dvd (dvd_mul_of_dvd_left (dvd_pow_self 3 (Nat.succ_ne_zero b)) M') hX3
      have hX3' : X % 3 = 1 := by unfold Nat.ModEq at hmod3; omega
      have hXeven : X % 2 = 0 := by omega
      have hX6 : X % 6 = 4 := by omega
      refine ⟨(X - 1) / 3, mem_inverse hB hX hX6, ?_, ?_⟩
      · have h3x : 3 * ((X - 1) / 3) + 1 = X := by omega
        have h1 : 3 * ((X - 1) / 3) + 1 ≡ 3 * r + 1 [MOD 2 ^ (k + 1)] := by rw [h3x]; exact hX2
        have h2 : 3 * ((X - 1) / 3) ≡ 3 * r [MOD 2 ^ (k + 1)] := Nat.ModEq.add_right_cancel' 1 h1
        exact Nat.ModEq.cancel_left_of_coprime (Nat.Coprime.pow_left _ (by decide : Nat.Coprime 2 3)) h2
      · have h3x : 3 * ((X - 1) / 3) + 1 = X := by omega
        have h1 : 3 * ((X - 1) / 3) + 1 ≡ 3 * ε + 1 [MOD 3 ^ (b + 1) * M'] := by
          rw [h3x]; convert hX3 using 1; ring
        have h2 : 3 * ((X - 1) / 3) ≡ 3 * ε [MOD 3 * (3 ^ b * M')] := by
          rw [← mul_assoc, ← pow_succ']; exact Nat.ModEq.add_right_cancel' 1 h1
        exact Nat.ModEq.mul_left_cancel' (by norm_num) h2

end Lift

include hB

/-- **Theorem.** If `M'` is coprime to 6 and `2^T ≡ 1 (mod M')` for some `T ≥ 1` not divisible by 3 (that is,
`3 ∤ ord_{M'}(2)`), then a nonempty saturated set meets every residue class modulo `2^k · 3^b · M'`. -/
theorem saturated_dense_of_order_prime_to_three (hne : B.Nonempty) (M' : ℕ) (hM' : 0 < M')
    (hM6 : Nat.Coprime M' 6) (T : ℕ) (hT : 0 < T) (h3T : ¬ 3 ∣ T) (hTpow : 2 ^ T ≡ 1 [MOD M'])
    (k b r : ℕ) : ∃ x ∈ B, x ≡ r [MOD 2 ^ k * 3 ^ b * M'] := by
  have : NeZero M' := ⟨by omega⟩
  have h4T : 4 ^ T ≡ 1 [MOD M'] := by
    have := hTpow.pow 2
    rw [← pow_mul, mul_comm, pow_mul] at this
    simpa using this
  have hM'odd : M' % 2 = 1 := by
    have h : Nat.Coprime 2 M' := Nat.Coprime.coprime_dvd_left (by norm_num : 2 ∣ 6) hM6.symm
    rcases Nat.even_or_odd M' with he | ho
    · exfalso
      have := Nat.Coprime.eq_one_of_dvd h (even_iff_two_dvd.mp he)
      omega
    · exact Nat.odd_iff.mp ho
  have hbase := exists_modEq_three_pow_mul hB M' hM6 T hT h3T h4T hne
  obtain ⟨x, hx, h2, h3⟩ := exists_modEq_pow_mul hB M' hM'odd hbase k b r r
  refine ⟨x, hx, ?_⟩
  have hcop : Nat.Coprime (2 ^ k) (3 ^ b * M') := by
    apply Nat.Coprime.pow_left
    apply Nat.Coprime.mul_right
    · exact Nat.Coprime.pow_right _ (by decide)
    · exact Nat.Coprime.coprime_dvd_left (by norm_num : 2 ∣ 6) hM6.symm
  rw [mul_assoc]
  exact (Nat.modEq_and_modEq_iff_modEq_mul hcop).1 ⟨h2, h3⟩

end SaturatedScaling
end LeanLane

#print axioms LeanLane.SaturatedScaling.exists_free_exponent
#print axioms LeanLane.SaturatedScaling.exists_translate
#print axioms LeanLane.SaturatedScaling.saturated_dense_of_order_prime_to_three
