import LeanLane.SaturatedAutomaton

/-!
# `LeanLane.SaturatedConnectivity`: every automaton is strongly connected

Formal companion of `areas/invariants/results/saturated-residue-automata-uniform-connectivity`.

For `M'` coprime to 6 and any `v`, the automaton `Step M' v` of `LeanLane.SaturatedAutomaton` is strongly
connected. The proof uses only two families of its arrows on the states `(x, η) ∈ ZMod M' × ZMod (3^v)`:

* the scaling arrow with `s = 1`: `(x, η) → (4x + 1, 4η + 1)`;
* the inverse arrow with `j = 2`: `(x, η) → (x', η')` whenever `4x = 3x' + 1` and `4η = 3η' + 1`.

A set `C` of states closed under both is everything (`closed_eq_univ`):

1. translating the second coordinate by elements killed by `3^k` stays in `C` at a suitable state, by induction
   on `k`: each inverse arrow frees one more 3-adic digit (`P_inv`), and one of `η, 4η + 1, 4(4η + 1) + 1` is
   always the source of an inverse arrow (`good_cases`);
2. at `k = v` a whole fibre `{x} × ZMod (3^v)` lies in `C`; the set `X` of such `x` is closed under
   `x ↦ 4x + 1` and `x ↦ (4x − 1)/3`, hence, being finite, under their inverses (`mem_of_map_mem`), hence under
   `x ↦ 3x + 1` and `x ↦ 3x + 2`, hence under `x ↦ x + 1`.

With `LeanLane.SaturatedAutomaton.saturated_dense_of_automaton` this gives `saturated_dense_all`: a nonempty
saturated set of the Collatz map meets every residue class modulo every positive integer.
-/

namespace LeanLane
namespace SaturatedConnectivity

open LeanLane.SaturatedDensity LeanLane.SaturatedScaling LeanLane.SaturatedAutomaton

/-- A subset of a finite type that is mapped into itself by an injective map contains every preimage of its
elements. -/
theorem mem_of_map_mem {α : Type*} [Finite α] (X : Set α) (f : α → α) (hf : Function.Injective f)
    (hX : ∀ x ∈ X, f x ∈ X) {x : α} (h : f x ∈ X) : x ∈ X := by
  let g : X → X := fun y => ⟨f y.1, hX y.1 y.2⟩
  have hg : Function.Injective g := by
    intro y y' hyy'
    apply Subtype.ext
    apply hf
    exact congrArg Subtype.val hyy'
  obtain ⟨⟨y, hy⟩, hy'⟩ := Finite.surjective_of_injective hg ⟨f x, h⟩
  have hfy : f y = f x := congrArg Subtype.val hy'
  rwa [← hf hfy]

/-- A residue coprime to the modulus has an inverse. -/
theorem exists_inv (a n : ℕ) (h : Nat.Coprime a n) : ∃ b : ZMod n, (a : ZMod n) * b = 1 := by
  have hu : IsUnit ((a : ℕ) : ZMod n) := (ZMod.isUnit_iff_coprime a n).mpr h
  exact isUnit_iff_exists_inv.mp hu

theorem three_pow_mod_four (n : ℕ) : 3 ^ n % 4 = 1 ∨ 3 ^ n % 4 = 3 := by
  induction n with
  | zero => left; norm_num
  | succ n ih =>
    rw [pow_succ]
    rcases ih with h | h
    · right; omega
    · left; omega

variable {M' v : ℕ}

/-- Closure of a set of states under the scaling arrow with `s = 1` and the inverse arrow with `j = 2`. -/
structure Closed (C : Set (ZMod M' × ZMod (3 ^ v))) : Prop where
  sig : ∀ p ∈ C, (4 * p.1 + 1, 4 * p.2 + 1) ∈ C
  inv : ∀ p ∈ C, ∀ q : ZMod M' × ZMod (3 ^ v), 4 * p.1 = 3 * q.1 + 1 → 4 * p.2 = 3 * q.2 + 1 → q ∈ C

/-- `P k C p`: `C` contains every translate of `p` by an element of the second coordinate killed by `3^k`. -/
def P (k : ℕ) (C : Set (ZMod M' × ZMod (3 ^ v))) (p : ZMod M' × ZMod (3 ^ v)) : Prop :=
  ∀ κ : ZMod (3 ^ v), 3 ^ k * κ = 0 → (p.1, p.2 + κ) ∈ C

theorem P_sig {C : Set (ZMod M' × ZMod (3 ^ v))} (hC : Closed C) {j2 : ZMod (3 ^ v)} (hj2 : 4 * j2 = 1)
    {k : ℕ} {p : ZMod M' × ZMod (3 ^ v)} (hp : P k C p) : P k C (4 * p.1 + 1, 4 * p.2 + 1) := by
  intro κ hκ
  have h1 : (3 : ZMod (3 ^ v)) ^ k * (j2 * κ) = 0 := by rw [mul_left_comm, hκ, mul_zero]
  have h2 : (4 * p.1 + 1, 4 * (p.2 + j2 * κ) + 1) ∈ C := hC.sig _ (hp _ h1)
  have e : (4 : ZMod (3 ^ v)) * (p.2 + j2 * κ) + 1 = 4 * p.2 + 1 + κ := by linear_combination κ * hj2
  rw [e] at h2
  exact h2

theorem P_inv {C : Set (ZMod M' × ZMod (3 ^ v))} (hC : Closed C) {j2 : ZMod (3 ^ v)} (hj2 : 4 * j2 = 1)
    {k : ℕ} {p q : ZMod M' × ZMod (3 ^ v)} (hp : P k C p) (h1 : 4 * p.1 = 3 * q.1 + 1)
    (h2 : 4 * p.2 = 3 * q.2 + 1) : P (k + 1) C q := by
  intro κ hκ
  have hk : (3 : ZMod (3 ^ v)) ^ k * (j2 * (3 * κ)) = 0 := by
    have e : (3 : ZMod (3 ^ v)) ^ k * (j2 * (3 * κ)) = j2 * (3 ^ (k + 1) * κ) := by ring
    rw [e, hκ, mul_zero]
  have hmem : (p.1, p.2 + j2 * (3 * κ)) ∈ C := hp _ hk
  refine hC.inv _ hmem (q.1, q.2 + κ) h1 ?_
  show 4 * (p.2 + j2 * (3 * κ)) = 3 * (q.2 + κ) + 1
  linear_combination h2 + 3 * κ * hj2

/-- `η ≡ 1 (mod 3)`, stated as: `η` is the source of an inverse arrow. -/
def Good (η : ZMod (3 ^ v)) : Prop := ∃ q : ZMod (3 ^ v), 4 * η = 3 * q + 1

theorem good_natCast (n : ℕ) (h : n % 3 = 1) : Good (v := v) (n : ZMod (3 ^ v)) := by
  refine ⟨((4 * n - 1) / 3 : ℕ), ?_⟩
  have e : 4 * n = 3 * ((4 * n - 1) / 3) + 1 := by omega
  have h' := congrArg (Nat.cast : ℕ → ZMod (3 ^ v)) e
  push_cast at h'
  exact h'

theorem good_cases (η : ZMod (3 ^ v)) : Good η ∨ Good (4 * η + 1) ∨ Good (4 * (4 * η + 1) + 1) := by
  have hη : ((η.val : ℕ) : ZMod (3 ^ v)) = η := ZMod.natCast_zmod_val η
  rcases (by omega : η.val % 3 = 0 ∨ η.val % 3 = 1 ∨ η.val % 3 = 2) with h | h | h
  · right; left
    have h' := good_natCast (v := v) (4 * η.val + 1) (by omega)
    push_cast at h'
    rwa [hη] at h'
  · left
    have h' := good_natCast (v := v) η.val h
    rwa [hη] at h'
  · right; right
    have h' := good_natCast (v := v) (4 * (4 * η.val + 1) + 1) (by omega)
    push_cast at h'
    rwa [hη] at h'

theorem exists_P {C : Set (ZMod M' × ZMod (3 ^ v))} (hC : Closed C) (hne : C.Nonempty)
    {j2 : ZMod (3 ^ v)} (hj2 : 4 * j2 = 1) {i3 : ZMod M'} (hi3 : 3 * i3 = 1) (k : ℕ) :
    ∃ p, P k C p := by
  induction k with
  | zero =>
    obtain ⟨a, ha⟩ := hne
    refine ⟨a, ?_⟩
    intro κ hκ
    rw [pow_zero, one_mul] at hκ
    subst hκ
    simpa using ha
  | succ k ih =>
    obtain ⟨p, hp⟩ := ih
    have hp1 := P_sig hC hj2 hp
    have hp2 := P_sig hC hj2 hp1
    have key : ∀ p' : ZMod M' × ZMod (3 ^ v), P k C p' → Good p'.2 → ∃ q, P (k + 1) C q := by
      rintro p' hp' ⟨q2, hq2⟩
      refine ⟨(i3 * (4 * p'.1 - 1), q2), P_inv hC hj2 hp' ?_ hq2⟩
      show 4 * p'.1 = 3 * (i3 * (4 * p'.1 - 1)) + 1
      linear_combination (-(4 * p'.1 - 1)) * hi3
    rcases good_cases p.2 with h | h | h
    · exact key p hp h
    · exact key _ hp1 h
    · exact key _ hp2 h

/-- A nonempty set of states closed under the two families of arrows is everything. -/
theorem closed_eq_univ [NeZero M'] (hM6 : Nat.Coprime M' 6) {C : Set (ZMod M' × ZMod (3 ^ v))}
    (hC : Closed C) (hne : C.Nonempty) : ∀ p, p ∈ C := by
  have h2M : Nat.Coprime 2 M' := Nat.Coprime.coprime_dvd_left (by norm_num : 2 ∣ 6) hM6.symm
  have h3M : Nat.Coprime 3 M' := Nat.Coprime.coprime_dvd_left (by norm_num : 3 ∣ 6) hM6.symm
  have h4M : Nat.Coprime 4 M' := by simpa using Nat.Coprime.pow_left 2 h2M
  obtain ⟨j2, hj2⟩ := exists_inv 4 (3 ^ v) (Nat.Coprime.pow_right v (by decide))
  obtain ⟨j1, hj1⟩ := exists_inv 4 M' h4M
  obtain ⟨i3, hi3⟩ := exists_inv 3 M' h3M
  push_cast at hj2 hj1 hi3
  obtain ⟨p0, hp0⟩ := exists_P hC hne hj2 hi3 v
  have h3v : (3 : ZMod (3 ^ v)) ^ v = 0 := by
    have h := ZMod.natCast_self (3 ^ v)
    push_cast at h
    exact h
  let X : Set (ZMod M') := {x | ∀ η, (x, η) ∈ C}
  have hx0 : p0.1 ∈ X := by
    intro η
    have h := hp0 (η - p0.2) (by rw [h3v, zero_mul])
    simpa using h
  have hX1 : ∀ x ∈ X, 4 * x + 1 ∈ X := by
    intro x hx η
    have h : (4 * x + 1, 4 * (j2 * (η - 1)) + 1) ∈ C := hC.sig _ (hx (j2 * (η - 1)))
    have e : (4 : ZMod (3 ^ v)) * (j2 * (η - 1)) + 1 = η := by linear_combination (η - 1) * hj2
    rw [e] at h
    exact h
  have hX2 : ∀ x ∈ X, ∀ x', 4 * x = 3 * x' + 1 → x' ∈ X := by
    intro x hx x' hxx' η'
    refine hC.inv _ (hx (j2 * (3 * η' + 1))) (x', η') hxx' ?_
    show 4 * (j2 * (3 * η' + 1)) = 3 * η' + 1
    linear_combination (3 * η' + 1) * hj2
  -- closure under `y ↦ (3y + 1)/4`, the inverse of `x ↦ (4x - 1)/3`
  have hX3 : ∀ y ∈ X, j1 * (3 * y + 1) ∈ X := by
    intro y hy
    have hinj : Function.Injective (fun x : ZMod M' => i3 * (4 * x - 1)) := by
      apply Function.LeftInverse.injective (g := fun y : ZMod M' => j1 * (3 * y + 1))
      intro x
      show j1 * (3 * (i3 * (4 * x - 1)) + 1) = x
      linear_combination x * hj1 + j1 * (4 * x - 1) * hi3
    have hcl : ∀ x ∈ X, (fun x : ZMod M' => i3 * (4 * x - 1)) x ∈ X := by
      intro x hx
      refine hX2 x hx _ ?_
      show 4 * x = 3 * (i3 * (4 * x - 1)) + 1
      linear_combination (-(4 * x - 1)) * hi3
    apply mem_of_map_mem X _ hinj hcl
    show i3 * (4 * (j1 * (3 * y + 1)) - 1) ∈ X
    have e : i3 * (4 * (j1 * (3 * y + 1)) - 1) = y := by
      linear_combination y * hi3 + i3 * (3 * y + 1) * hj1
    rw [e]
    exact hy
  have hXp : ∀ x ∈ X, 3 * x + 1 ∈ X := by
    intro x hx
    have h := hX3 _ (hX1 x hx)
    have e : j1 * (3 * (4 * x + 1) + 1) = 3 * x + 1 := by linear_combination (3 * x + 1) * hj1
    rw [e] at h
    exact h
  have hXq : ∀ x ∈ X, 3 * x + 2 ∈ X := by
    intro x hx
    have h := hX1 _ (hX3 x hx)
    have e : 4 * (j1 * (3 * x + 1)) + 1 = 3 * x + 2 := by linear_combination (3 * x + 1) * hj1
    rw [e] at h
    exact h
  have hXt : ∀ t ∈ X, t + 1 ∈ X := by
    intro t ht
    have hinj : Function.Injective (fun x : ZMod M' => 3 * x + 1) := by
      apply Function.LeftInverse.injective (g := fun y : ZMod M' => i3 * (y - 1))
      intro x
      show i3 * (3 * x + 1 - 1) = x
      linear_combination x * hi3
    have hy : i3 * (t - 1) ∈ X := by
      apply mem_of_map_mem X _ hinj hXp
      show 3 * (i3 * (t - 1)) + 1 ∈ X
      have e : 3 * (i3 * (t - 1)) + 1 = t := by linear_combination (t - 1) * hi3
      rw [e]
      exact ht
    have h := hXq _ hy
    have e : 3 * (i3 * (t - 1)) + 2 = t + 1 := by linear_combination (t - 1) * hi3
    rw [e] at h
    exact h
  have hall : ∀ n : ℕ, p0.1 + (n : ZMod M') ∈ X := by
    intro n
    induction n with
    | zero => simpa using hx0
    | succ n ih =>
      have h := hXt _ ih
      push_cast
      rw [← add_assoc]
      exact h
  intro p
  have h := hall (p.1 - p0.1).val
  rw [ZMod.natCast_zmod_val] at h
  have e : p0.1 + (p.1 - p0.1) = p.1 := by ring
  rw [e] at h
  exact h p.2

/-- The sparse edge relation: the scaling arrow with `s = 1` and the inverse arrow with `j = 2`. -/
def E (a b : ZMod M' × ZMod (3 ^ v)) : Prop :=
  b = (4 * a.1 + 1, 4 * a.2 + 1) ∨ (4 * a.1 = 3 * b.1 + 1 ∧ 4 * a.2 = 3 * b.2 + 1)

theorem E_connected [NeZero M'] (hM6 : Nat.Coprime M' 6) (a b : ZMod M' × ZMod (3 ^ v)) :
    Relation.ReflTransGen E a b := by
  have hC : Closed {c : ZMod M' × ZMod (3 ^ v) | Relation.ReflTransGen E a c} := by
    constructor
    · intro p hp
      exact Relation.ReflTransGen.tail hp (Or.inl rfl)
    · intro p hp q h1 h2
      exact Relation.ReflTransGen.tail hp (Or.inr ⟨h1, h2⟩)
  exact closed_eq_univ hM6 hC ⟨a, Relation.ReflTransGen.refl⟩ b

/-- Every sparse edge is an arrow of the automaton. -/
theorem step_of_E {a b : ZMod M' × ZMod (3 ^ v)} (h : E a b) : Step M' v a b := by
  obtain ⟨a1, a2⟩ := a
  obtain ⟨b1, b2⟩ := b
  rcases h with h | ⟨h1, h2⟩
  · obtain ⟨rfl, rfl⟩ := Prod.mk.inj h
    have hs := Step.scale (M' := M') (v := v) 1 le_rfl a1 a2
    have hc : cst 1 = 1 := by norm_num [cst]
    rw [hc] at hs
    simpa using hs
  · have h1' : 4 * a1 = 3 * b1 + 1 := h1
    have h2' : 4 * a2 = 3 * b2 + 1 := h2
    obtain ⟨j2, hj2⟩ := exists_inv 4 (3 ^ v) (Nat.Coprime.pow_right v (by decide))
    push_cast at hj2
    have h3v : (3 : ZMod (3 ^ v)) ^ v = 0 := by
      have h := ZMod.natCast_self (3 ^ v)
      push_cast at h
      exact h
    have hβc : ((b2.val : ℕ) : ZMod (3 ^ v)) = b2 := ZMod.natCast_zmod_val b2
    generalize b2.val = β at hβc
    have ht := three_pow_mod_four (v + 1)
    have hpow : 3 ^ (v + 1) = 3 * 3 ^ v := by ring
    obtain ⟨s, hs⟩ : ∃ s, (3 * β + 1 + 3 ^ (v + 1) * s) % 4 = 0 := by
      generalize 3 ^ (v + 1) = t at ht ⊢
      rcases ht with ht | ht
      · rcases (by omega : (3 * β + 1) % 4 = 0 ∨ (3 * β + 1) % 4 = 1 ∨ (3 * β + 1) % 4 = 2
            ∨ (3 * β + 1) % 4 = 3) with h0 | h0 | h0 | h0
        · exact ⟨0, by omega⟩
        · exact ⟨3, by omega⟩
        · exact ⟨2, by omega⟩
        · exact ⟨1, by omega⟩
      · rcases (by omega : (3 * β + 1) % 4 = 0 ∨ (3 * β + 1) % 4 = 1 ∨ (3 * β + 1) % 4 = 2
            ∨ (3 * β + 1) % 4 = 3) with h0 | h0 | h0 | h0
        · exact ⟨0, by omega⟩
        · exact ⟨1, by omega⟩
        · exact ⟨2, by omega⟩
        · exact ⟨3, by omega⟩
    obtain ⟨zc, hz4⟩ : ∃ zc, 4 * zc = 3 * β + 1 + 3 ^ (v + 1) * s :=
      ⟨(3 * β + 1 + 3 ^ (v + 1) * s) / 4, Nat.mul_div_cancel' (Nat.dvd_of_mod_eq_zero hs)⟩
    have hsplit : 3 ^ (v + 1) * s = 3 * (3 ^ v * s) := by rw [hpow]; ring
    have hquot : (2 ^ 2 * zc - 1) / 3 = β + 3 ^ v * s := by
      have h4 : 2 ^ 2 * zc = 3 * (β + 3 ^ v * s) + 1 := by
        have : 2 ^ 2 * zc = 4 * zc := by norm_num
        rw [this, hz4, hsplit]; ring
      omega
    have hleg : 2 ^ 2 * zc % 3 = 1 := by
      have h4 : 2 ^ 2 * zc = 3 * (β + 3 ^ v * s) + 1 := by
        have : 2 ^ 2 * zc = 4 * zc := by norm_num
        rw [this, hz4, hsplit]; ring
      omega
    have hzc : ((zc : ℕ) : ZMod (3 ^ v)) = a2 := by
      have hc := congrArg (Nat.cast : ℕ → ZMod (3 ^ v)) hz4
      push_cast at hc
      have h3 : (3 : ZMod (3 ^ v)) ^ (v + 1) = 0 := by rw [pow_succ, h3v, zero_mul]
      rw [hβc, h3, zero_mul, add_zero] at hc
      linear_combination j2 * hc - j2 * h2' - ((zc : ZMod (3 ^ v)) - a2) * hj2
    have hx' : (3 : ZMod M') * b1 = 2 ^ 2 * a1 - 1 := by linear_combination (-1 : ZMod M') * h1'
    have hstep := Step.inv (M' := M') (v := v) 2 (by norm_num) a1 b1 a2 zc hzc hleg hx'
    have hq : (((2 ^ 2 * zc - 1) / 3 : ℕ) : ZMod (3 ^ v)) = b2 := by
      rw [hquot]
      push_cast
      rw [hβc, h3v, zero_mul, add_zero]
    rw [hq] at hstep
    exact hstep

/-- **Uniform connectivity.** For `M'` coprime to 6 the automaton `Step M' v` is strongly connected. -/
theorem step_connected (M' v : ℕ) [NeZero M'] (hM6 : Nat.Coprime M' 6) :
    ∀ σ σ' : ZMod M' × ZMod (3 ^ v), Relation.ReflTransGen (Step M' v) σ σ' := by
  intro a b
  have h := E_connected hM6 a b
  induction h with
  | refl => exact Relation.ReflTransGen.refl
  | tail _ hbc ih => exact Relation.ReflTransGen.tail ih (step_of_E hbc)

/-- **A nonempty saturated set meets every residue class modulo every positive integer.** -/
theorem saturated_dense_all {B : Set ℕ} (hB : Saturated B) (hne : B.Nonempty) (M r : ℕ) (hM : 0 < M) :
    ∃ x ∈ B, x ≡ r [MOD M] := by
  obtain ⟨k, m1, h2m1, rfl⟩ := Nat.exists_eq_pow_mul_and_not_dvd hM.ne' 2 (by norm_num)
  have hm1 : m1 ≠ 0 := fun h => h2m1 (h ▸ dvd_zero 2)
  obtain ⟨b, M', h3M', rfl⟩ := Nat.exists_eq_pow_mul_and_not_dvd hm1 3 (by norm_num)
  have hM' : M' ≠ 0 := fun h => h3M' (h ▸ dvd_zero 3)
  have hM'pos : 0 < M' := Nat.pos_of_ne_zero hM'
  have h2M' : ¬ 2 ∣ M' := fun h => h2m1 (Dvd.dvd.mul_left h _)
  have c2 : Nat.Coprime M' 2 := ((Nat.Prime.coprime_iff_not_dvd Nat.prime_two).mpr h2M').symm
  have c3 : Nat.Coprime M' 3 := ((Nat.Prime.coprime_iff_not_dvd Nat.prime_three).mpr h3M').symm
  have hM6 : Nat.Coprime M' 6 := by simpa using Nat.Coprime.mul_right c2 c3
  have h4M : Nat.Coprime 4 M' := by simpa using Nat.Coprime.pow_left 2 c2.symm
  have hφ : 0 < Nat.totient M' := Nat.totient_pos.mpr hM'pos
  obtain ⟨e, u, h3u, hφu⟩ := Nat.exists_eq_pow_mul_and_not_dvd hφ.ne' 3 (by norm_num)
  have hu : 0 < u := Nat.pos_of_ne_zero (fun h => h3u (h ▸ dvd_zero 3))
  have hper : 4 ^ (3 ^ (e + 1) * u) ≡ 1 [MOD M'] := by
    have h1 : 4 ^ Nat.totient M' ≡ 1 [MOD M'] := Nat.ModEq.pow_totient h4M
    have h2 : (4 ^ Nat.totient M') ^ 3 ≡ 1 ^ 3 [MOD M'] := Nat.ModEq.pow 3 h1
    have e3 : 3 ^ (e + 1) * u = Nat.totient M' * 3 := by rw [hφu]; ring
    rw [e3, pow_mul]
    simpa using h2
  have : NeZero M' := ⟨hM'⟩
  obtain ⟨x, hx, hxr⟩ := saturated_dense_of_automaton hB hne M' (e + 1) u hM'pos hM6 (by omega) hu h3u hper
    (step_connected M' (e + 1) hM6) k b r
  refine ⟨x, hx, ?_⟩
  rw [← mul_assoc]
  exact hxr

end SaturatedConnectivity
end LeanLane

#print axioms LeanLane.SaturatedConnectivity.mem_of_map_mem
#print axioms LeanLane.SaturatedConnectivity.closed_eq_univ
#print axioms LeanLane.SaturatedConnectivity.step_connected
#print axioms LeanLane.SaturatedConnectivity.saturated_dense_all
