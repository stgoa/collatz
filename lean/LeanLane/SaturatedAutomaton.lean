import LeanLane.SaturatedScaling

/-!
# `LeanLane.SaturatedAutomaton`: the finite-automaton reduction for the residue-class question

Formal companion of Theorem 1 of `areas/invariants/results/saturated-sets-residue-classes-finite-automaton`.

For `M'` coprime to 6 and `v ≥ 1` such that `4^(3^v · u) ≡ 1 (mod M')` for some `u ≥ 1` prime to 3, the state of an
odd `z` is `(z mod M', z mod 3^v)`. The automaton `Step` has scaling arrows `(x, η) → (4^s x + c_s, 4^s η + c_s)`
with `c_s = (4^s − 1)/3`, and inverse arrows `(x, η) → ((2^j x − 1)/3, ((2^j z' − 1)/3) mod 3^v)` for every lift `z'`
of `η` to a class modulo `3^(v+1)` with `2^j z' ≡ 1 (mod 3)`. If the automaton is strongly connected, every nonempty
saturated set meets every residue class modulo `2^k · 3^b · M'`.
-/

namespace LeanLane
namespace SaturatedAutomaton

open LeanLane.SaturatedDensity LeanLane.SaturatedScaling

/-- The constant of the scaling move, `(4^s − 1)/3`, as a natural number. -/
def cst (s : ℕ) : ℕ := (4 ^ s - 1) / 3

theorem three_cst (s : ℕ) : 3 * cst s + 1 = 4 ^ s := by
  unfold cst
  have h := four_pow_mod_three s
  have : 1 ≤ 4 ^ s := Nat.one_le_pow _ _ (by norm_num)
  omega

theorem scale_eq (s z : ℕ) : scale s z = 4 ^ s * z + cst s := by
  have h1 := three_scale_add_one s z
  have h2 := three_cst s
  nlinarith [h1, h2]

/-- The state of an odd integer. -/
def state (M' v : ℕ) (z : ℕ) : ZMod M' × ZMod (3 ^ v) := ((z : ZMod M'), (z : ZMod (3 ^ v)))

/-- The arrows of the automaton. -/
inductive Step (M' v : ℕ) : ZMod M' × ZMod (3 ^ v) → ZMod M' × ZMod (3 ^ v) → Prop
  | scale (s : ℕ) (hs : 1 ≤ s) (x : ZMod M') (η : ZMod (3 ^ v)) :
      Step M' v (x, η) (4 ^ s * x + (cst s : ZMod M'), 4 ^ s * η + (cst s : ZMod (3 ^ v)))
  | inv (j : ℕ) (hj : 1 ≤ j) (x x' : ZMod M') (η : ZMod (3 ^ v)) (zc : ℕ) (hzc : (zc : ZMod (3 ^ v)) = η)
      (hleg : 2 ^ j * zc % 3 = 1) (hx' : (3 : ZMod M') * x' = 2 ^ j * x - 1) :
      Step M' v (x, η) (x', (((2 ^ j * zc - 1) / 3 : ℕ) : ZMod (3 ^ v)))

/-- `4^s ≡ 1 (mod 3^(v+1))` forces `3^v ∣ s`. -/
theorem three_pow_dvd_of_four_pow_modEq (v s : ℕ) (h : 4 ^ s ≡ 1 [MOD 3 ^ (v + 1)]) : 3 ^ v ∣ s := by
  by_contra hnd
  -- write s = 3^a * c with a < v and 3 ∤ c
  obtain ⟨a, c, hs, hc3, hav⟩ : ∃ a c, s = 3 ^ a * c ∧ ¬ 3 ∣ c ∧ a < v := by
    have hs0 : s ≠ 0 := by rintro rfl; exact hnd (dvd_zero _)
    set a := (Nat.factorization s) 3 with ha
    refine ⟨a, s / 3 ^ a, ?_, ?_, ?_⟩
    · exact (Nat.ordProj_mul_ordCompl_eq_self s 3).symm
    · exact Nat.not_dvd_ordCompl Nat.prime_three hs0
    · by_contra hge
      push_neg at hge
      exact hnd (dvd_trans (pow_dvd_pow 3 hge) (Nat.ordProj_dvd s 3))
  obtain ⟨m, hm⟩ := four_pow_three_pow_mul a c
  -- 4^s = 1 + c 3^(a+1) + m 3^(a+2); modulo 3^(a+2) this is 1 iff 3 ∣ c
  have hmod : 4 ^ s ≡ 1 [MOD 3 ^ (a + 2)] :=
    Nat.ModEq.of_dvd (pow_dvd_pow 3 (by omega)) h
  rw [Nat.ModEq.comm, Nat.modEq_iff_dvd] at hmod
  push_cast at hmod
  rw [hs, hm] at hmod
  have h2 : (3 : ℤ) ^ (a + 2) ∣ (c : ℤ) * 3 ^ (a + 1) + m * 3 ^ (a + 2) := by
    have e : (1 : ℤ) + c * 3 ^ (a + 1) + m * 3 ^ (a + 2) - 1 = c * 3 ^ (a + 1) + m * 3 ^ (a + 2) := by ring
    rw [e] at hmod; exact hmod
  have h3 : (3 : ℤ) ^ (a + 2) ∣ (c : ℤ) * 3 ^ (a + 1) := (dvd_add_left (dvd_mul_left _ _)).mp h2
  have h4 : (3 : ℤ) * 3 ^ (a + 1) ∣ (c : ℤ) * 3 ^ (a + 1) := by rw [← pow_succ']; exact h3
  have h5 : (3 : ℤ) ∣ (c : ℤ) := (mul_dvd_mul_iff_right (by positivity : (3 : ℤ) ^ (a + 1) ≠ 0)).mp h4
  exact hc3 (by exact_mod_cast h5)

/-- Free steering beyond `3^(v+1)`: for `4^(3^v u) ≡ 1 (mod M')` with `3 ∤ u`, any `τ ≡ 1 (mod 3)` with
`τ ≡ 3z + 1 (mod 3^(v+1))` is reached modulo `3^(B+1)` by a scaling trivial modulo `M'`. -/
theorem exists_free_exponent' (M' v u : ℕ) (hu : 0 < u) (h3u : ¬ 3 ∣ u) (hper : 4 ^ (3 ^ v * u) ≡ 1 [MOD M'])
    (z : ℕ) (Bexp τ : ℕ) (hB : v ≤ Bexp) (hτ : τ % 3 = 1) (hτv : τ ≡ 3 * z + 1 [MOD 3 ^ (v + 1)]) :
    ∃ s, 1 ≤ s ∧ 4 ^ s ≡ 1 [MOD M'] ∧ 4 ^ s * (3 * z + 1) ≡ τ [MOD 3 ^ (Bexp + 1)] := by
  -- a power of two does the 3-adic job
  have hy : ¬ (3 : ℤ) ∣ ((3 * z + 1 : ℕ) : ℤ) := by push_cast; omega
  have hη : ¬ (3 : ℤ) ∣ (τ : ℤ) := by omega
  obtain ⟨j, hj, hdvd⟩ := two_pow_mul_surj ((3 * z + 1 : ℕ) : ℤ) (τ : ℤ) hy hη Bexp
  have hmod : τ ≡ 2 ^ j * (3 * z + 1) [MOD 3 ^ (Bexp + 1)] := by
    rw [Nat.modEq_iff_dvd]; push_cast at hdvd ⊢; exact hdvd
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
  -- 4^s₀ ≡ 1 modulo 3^(v+1), hence 3^v ∣ s₀
  have h4v : 4 ^ s₀ ≡ 1 [MOD 3 ^ (v + 1)] := by
    have h1 : 4 ^ s₀ * (3 * z + 1) ≡ τ [MOD 3 ^ (v + 1)] :=
      Nat.ModEq.of_dvd (pow_dvd_pow 3 (by omega)) h4s₀
    have h2 : 4 ^ s₀ * (3 * z + 1) ≡ 1 * (3 * z + 1) [MOD 3 ^ (v + 1)] := by
      rw [one_mul]; exact h1.trans hτv
    exact Nat.ModEq.cancel_right_of_coprime (by
      have : Nat.Coprime (3 * z + 1) 3 := by
        rw [Nat.coprime_comm, Nat.Prime.coprime_iff_not_dvd Nat.prime_three]; omega
      exact (Nat.Coprime.pow_right _ this).symm.gcd_eq_one) h2
  obtain ⟨t, ht⟩ := three_pow_dvd_of_four_pow_modEq v s₀ h4v
  -- Chinese remainder: t' ≡ t (mod 3^(B-v)), t' ≡ 0 (mod u)
  have hcop : Nat.Coprime (3 ^ (Bexp - v)) u := by
    apply Nat.Coprime.pow_left
    exact (Nat.Prime.coprime_iff_not_dvd Nat.prime_three).mpr h3u
  obtain ⟨k, hk1, hk2⟩ := Nat.chineseRemainder hcop t 0
  set t' := k + 3 ^ (Bexp - v) * u with ht'
  refine ⟨3 ^ v * t', ?_, ?_, ?_⟩
  · have : 0 < 3 ^ v * t' := by positivity
    omega
  · -- 4^(3^v t') ≡ 1 mod M': 3^v u ∣ 3^v t'
    have hu' : u ∣ t' := by
      have : u ∣ k := Nat.modEq_zero_iff_dvd.mp hk2
      exact dvd_add this (dvd_mul_left u _)
    obtain ⟨q, hq⟩ := hu'
    rw [hq, ← mul_assoc, pow_mul]
    simpa using hper.pow q
  · -- 4^(3^v t') ≡ 4^(3^v t) = 4^s₀ modulo 3^(B+1)
    have hexp : t' ≡ t [MOD 3 ^ (Bexp - v)] := by
      have : t' ≡ k + 0 [MOD 3 ^ (Bexp - v)] :=
        Nat.ModEq.add_left k (Nat.modEq_zero_iff_dvd.mpr (dvd_mul_right _ _))
      simpa using this.trans hk1
    have hbase : (4 ^ 3 ^ v) ^ (3 ^ (Bexp - v)) ≡ 1 [MOD 3 ^ (Bexp + 1)] := by
      rw [← pow_mul, ← pow_add, Nat.add_sub_cancel' hB]
      exact four_pow_three_pow_modEq Bexp
    have h4 := pow_modEq_of_exp_modEq hbase (by positivity) hexp
    rw [← pow_mul, ← pow_mul, ← ht] at h4
    exact (h4.mul_right _).trans h4s₀


/-! ## Realisation of the arrows and the theorem -/

theorem natCast_modEq_iff' {a b n : ℕ} : (a : ZMod n) = (b : ZMod n) ↔ a ≡ b [MOD n] :=
  ZMod.natCast_eq_natCast_iff a b n

variable {B : Set ℕ} (hB : Saturated B)
include hB

/-- Every arrow of the automaton from the state of an odd element of `B` is realised by an odd element of `B`. -/
theorem exists_step (M' v u : ℕ) [NeZero M'] (hM6 : Nat.Coprime M' 6) (hv : 1 ≤ v) (hu : 0 < u) (h3u : ¬ 3 ∣ u)
    (hper : 4 ^ (3 ^ v * u) ≡ 1 [MOD M']) {z : ℕ} (hz : z ∈ B) (hodd : z % 2 = 1)
    {σ' : ZMod M' × ZMod (3 ^ v)} (hstep : Step M' v (state M' v z) σ') :
    ∃ z' ∈ B, z' % 2 = 1 ∧ state M' v z' = σ' := by
  have h3unit := three_isUnit M' hM6
  generalize hσ : state M' v z = σ at hstep
  cases hstep with
  | scale s hs x η =>
    refine ⟨scale s z, scale_mem hB hz hodd s, scale_odd s z hodd, ?_⟩
    simp only [state, Prod.mk.injEq] at hσ
    obtain ⟨hx, hη⟩ := hσ
    simp only [state, scale_eq, Prod.mk.injEq]
    push_cast
    rw [hx, hη]
    exact ⟨rfl, rfl⟩
  | inv j hj x x' η zc hzc hleg hx' =>
    simp only [state, Prod.mk.injEq] at hσ
    obtain ⟨hx, hη⟩ := hσ
    -- zc ≡ z modulo 3^v
    have hzcz : zc ≡ z [MOD 3 ^ v] := natCast_modEq_iff'.mp (hzc.trans hη.symm)
    -- steer z modulo 3^(v+1) to the class of zc, keeping its class modulo M'
    have hτv : 3 * zc + 1 ≡ 3 * z + 1 [MOD 3 ^ (v + 1)] := by
      rw [pow_succ']; exact Nat.ModEq.add_right 1 (Nat.ModEq.mul_left' 3 hzcz)
    obtain ⟨s, hs1, hsM, hs3⟩ :=
      exists_free_exponent' M' v u hu h3u hper z (v + 1) (3 * zc + 1) (by omega) (by omega) hτv
    set z₁ := scale s z with hz₁def
    have hz₁ : z₁ ∈ B := scale_mem hB hz hodd s
    have hodd₁ : z₁ % 2 = 1 := scale_odd s z hodd
    have hz₁zc : z₁ ≡ zc [MOD 3 ^ (v + 1)] := by
      have h := three_scale_add_one s z
      have h1 : 3 * z₁ + 1 ≡ 3 * zc + 1 [MOD 3 ^ (v + 2)] := by rw [hz₁def, h]; exact hs3
      have h2 : 3 * z₁ ≡ 3 * zc [MOD 3 * 3 ^ (v + 1)] := by
        rw [← pow_succ']; exact Nat.ModEq.add_right_cancel' 1 h1
      exact Nat.ModEq.mul_left_cancel' (by norm_num) h2
    have hz₁M : (z₁ : ZMod M') = (z : ZMod M') := by
      have h := three_scale_add_one s z
      have hc : ((3 * z₁ + 1 : ℕ) : ZMod M') = ((4 ^ s * (3 * z + 1) : ℕ) : ZMod M') := by rw [hz₁def, h]
      push_cast at hc
      rw [four_pow_s_cast M' hsM, one_mul] at hc
      have : (3 : ZMod M') * (z₁ : ZMod M') = 3 * (z : ZMod M') := by linear_combination hc
      exact h3unit.mul_left_cancel this
    -- the inverse step is legal
    have hleg₁ : 2 ^ j * z₁ % 3 = 1 := by
      have h3 : z₁ ≡ zc [MOD 3] := Nat.ModEq.of_dvd (dvd_pow_self 3 (Nat.succ_ne_zero v)) hz₁zc
      have := Nat.ModEq.mul_left (2 ^ j) h3
      unfold Nat.ModEq at this
      rw [this]; exact hleg
    refine ⟨inv j z₁, inv_mem hB hz₁ j hj hleg₁, inv_odd j z₁ hleg₁ hj, ?_⟩
    simp only [state, Prod.mk.injEq]
    constructor
    · -- class modulo M'
      have h := three_inv_add_one j z₁ hleg₁
      have hc : ((3 * inv j z₁ + 1 : ℕ) : ZMod M') = ((2 ^ j * z₁ : ℕ) : ZMod M') := by rw [h]
      push_cast at hc
      rw [hz₁M, hx] at hc
      have : (3 : ZMod M') * (inv j z₁ : ZMod M') = 3 * x' := by linear_combination hc - hx'
      exact h3unit.mul_left_cancel this
    · -- class modulo 3^v
      apply natCast_modEq_iff'.mpr
      have ha : 3 ∣ 2 ^ j * z₁ - 1 := by omega
      have hb : 3 ∣ 2 ^ j * zc - 1 := by omega
      have h1 : 2 ^ j * z₁ - 1 ≡ 2 ^ j * zc - 1 [MOD 3 ^ (v + 1)] := by
        have := Nat.ModEq.mul_left (2 ^ j) hz₁zc
        have hpos : 1 ≤ 2 ^ j * z₁ := by omega
        have hpos' : 1 ≤ 2 ^ j * zc := by omega
        exact (Nat.ModEq.add_right_cancel' 1 (by
          rw [Nat.sub_add_cancel hpos, Nat.sub_add_cancel hpos']; exact this))
      have h2 : 3 * ((2 ^ j * z₁ - 1) / 3) ≡ 3 * ((2 ^ j * zc - 1) / 3) [MOD 3 * 3 ^ v] := by
        rw [Nat.mul_div_cancel' ha, Nat.mul_div_cancel' hb, ← pow_succ']; exact h1
      exact Nat.ModEq.mul_left_cancel' (by norm_num) h2

/-- The base case from strong connectivity: an element of `B` in every class modulo `3^b M'`. -/
theorem exists_modEq_of_connected (hne : B.Nonempty) (M' v u : ℕ) [NeZero M'] (hM6 : Nat.Coprime M' 6) (hv : 1 ≤ v)
    (hu : 0 < u) (h3u : ¬ 3 ∣ u) (hper : 4 ^ (3 ^ v * u) ≡ 1 [MOD M'])
    (hconn : ∀ σ σ' : ZMod M' × ZMod (3 ^ v), Relation.ReflTransGen (Step M' v) σ σ') (b ε : ℕ) :
    ∃ x ∈ B, x ≡ ε [MOD 3 ^ b * M'] := by
  have h3unit := three_isUnit M' hM6
  obtain ⟨x₀, hx₀, hodd₀⟩ := exists_odd hB hne
  have reach : ∀ σ', Relation.ReflTransGen (Step M' v) (state M' v x₀) σ' →
      ∃ z ∈ B, z % 2 = 1 ∧ state M' v z = σ' := by
    intro σ' h
    induction h with
    | refl => exact ⟨x₀, hx₀, hodd₀, rfl⟩
    | tail _ hstep ih =>
      obtain ⟨z, hz, hodd, hst⟩ := ih
      rw [← hst] at hstep
      exact exists_step hB M' v u hM6 hv hu h3u hper hz hodd hstep
  obtain ⟨z, hz, hodd, hst⟩ := reach ((ε : ZMod M'), (ε : ZMod (3 ^ v))) (hconn _ _)
  simp only [state, Prod.mk.injEq] at hst
  obtain ⟨hzM, hz3⟩ := hst
  have hzε : z ≡ ε [MOD 3 ^ v] := natCast_modEq_iff'.mp hz3
  set Bexp := max b v with hBexp
  have hτv : 3 * ε + 1 ≡ 3 * z + 1 [MOD 3 ^ (v + 1)] := by
    rw [pow_succ']; exact Nat.ModEq.add_right 1 (Nat.ModEq.mul_left' 3 hzε.symm)
  obtain ⟨s, hs1, hsM, hs3⟩ :=
    exists_free_exponent' M' v u hu h3u hper z Bexp (3 * ε + 1) (le_max_right _ _) (by omega) hτv
  refine ⟨scale s z, scale_mem hB hz hodd s, ?_⟩
  have hcop : Nat.Coprime (3 ^ b) M' :=
    Nat.Coprime.pow_left _ (Nat.Coprime.coprime_dvd_left (by norm_num : 3 ∣ 6) hM6.symm)
  apply (Nat.modEq_and_modEq_iff_modEq_mul hcop).1
  constructor
  · have h := three_scale_add_one s z
    have h1 : 3 * scale s z + 1 ≡ 3 * ε + 1 [MOD 3 ^ (Bexp + 1)] := by rw [h]; exact hs3
    have h2 : 3 * scale s z ≡ 3 * ε [MOD 3 * 3 ^ Bexp] := by
      rw [← pow_succ']; exact Nat.ModEq.add_right_cancel' 1 h1
    have h3 : scale s z ≡ ε [MOD 3 ^ Bexp] := Nat.ModEq.mul_left_cancel' (by norm_num) h2
    exact Nat.ModEq.of_dvd (pow_dvd_pow 3 (le_max_left _ _)) h3
  · rw [← natCast_modEq_iff']
    have h := three_scale_add_one s z
    have hc : ((3 * scale s z + 1 : ℕ) : ZMod M') = ((4 ^ s * (3 * z + 1) : ℕ) : ZMod M') := by rw [h]
    push_cast at hc
    rw [four_pow_s_cast M' hsM, one_mul, hzM] at hc
    have : (3 : ZMod M') * (scale s z : ZMod M') = 3 * (ε : ZMod M') := by linear_combination hc
    exact h3unit.mul_left_cancel this

/-- **Theorem 1 of the node.** If the automaton of `(M', v)` is strongly connected, a nonempty saturated set meets
every residue class modulo `2^k · 3^b · M'`. -/
theorem saturated_dense_of_automaton (hne : B.Nonempty) (M' v u : ℕ) (hM' : 0 < M') (hM6 : Nat.Coprime M' 6)
    (hv : 1 ≤ v) (hu : 0 < u) (h3u : ¬ 3 ∣ u) (hper : 4 ^ (3 ^ v * u) ≡ 1 [MOD M'])
    (hconn : ∀ σ σ' : ZMod M' × ZMod (3 ^ v), Relation.ReflTransGen (Step M' v) σ σ')
    (k b r : ℕ) : ∃ x ∈ B, x ≡ r [MOD 2 ^ k * 3 ^ b * M'] := by
  have : NeZero M' := ⟨by omega⟩
  have hM'odd : M' % 2 = 1 := by
    have h : Nat.Coprime 2 M' := Nat.Coprime.coprime_dvd_left (by norm_num : 2 ∣ 6) hM6.symm
    rcases Nat.even_or_odd M' with he | ho
    · exfalso
      have := Nat.Coprime.eq_one_of_dvd h (even_iff_two_dvd.mp he)
      omega
    · exact Nat.odd_iff.mp ho
  have hbase := exists_modEq_of_connected hB hne M' v u hM6 hv hu h3u hper hconn
  obtain ⟨x, hx, h2, h3⟩ := exists_modEq_pow_mul hB M' hM'odd hbase k b r r
  refine ⟨x, hx, ?_⟩
  have hcop : Nat.Coprime (2 ^ k) (3 ^ b * M') := by
    apply Nat.Coprime.pow_left
    apply Nat.Coprime.mul_right
    · exact Nat.Coprime.pow_right _ (by decide)
    · exact Nat.Coprime.coprime_dvd_left (by norm_num : 2 ∣ 6) hM6.symm
  rw [mul_assoc]
  exact (Nat.modEq_and_modEq_iff_modEq_mul hcop).1 ⟨h2, h3⟩

end SaturatedAutomaton
end LeanLane

#print axioms LeanLane.SaturatedAutomaton.three_pow_dvd_of_four_pow_modEq
#print axioms LeanLane.SaturatedAutomaton.exists_free_exponent'
#print axioms LeanLane.SaturatedAutomaton.exists_step
#print axioms LeanLane.SaturatedAutomaton.saturated_dense_of_automaton
