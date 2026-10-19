import Mathlib

/-!
# Cycle denominators of repeated valuation words (main's C001 `REPETITION_SPECTRUM.md` §§1–2)

Lane: `claude/lean-lane`. Prose source: `experiments/cycle_spectrum/C001/REPETITION_SPECTRUM.md`
on main (the first batch of the cycle-spectrum goal, `docs/CYCLE_SPECTRUM_BRIEF.md`).

Setting. A valuation word is a list `z = [a₀, …, a_{m−1}]` of exponents; its affine
composition is `F_z(x) = (3^m x + C_z)/2^{Σz}` with `F_a(x) = (3x+1)/2^a` applied left to
right, so `C_(a :: z) = 3^|z| + 2^a C_z` and `D_z = 2^{Σz} − 3^{|z|}`. For blocks `u, v` and
`w_k = u^k v`, with `Q = 2^{Σu}`, `P = 3^{|u|}`, `S = 2^{Σv}`, `R = 3^{|v|}`,
`G_k = Σ_{i<k} Q^{k−1−i} P^i` and `K = D_u C_v − D_v C_u`.

Verified in this file (all with the standard axioms; everything is in `ℤ`, so negative
`D` is allowed — the prose's positivity `D_k > 0` is only needed to read `C/D` as a cycle):

* `C_append`, `C_rep`, `G_mul`: concatenation and repetition formulas
  (`C_{uv} = R C_u + Q C_v`, `C_{u^k} = C_u G_k`, `(Q − P) G_k = Q^k − P^k`);
* `C_w`, `D_w`: main's (1), (2);
* `commutator`: main's (3), `D_u C_k − C_u D_k = Q^k K`;
* `gcd_dvd_K`: main's (4), `gcd(C_k, D_k) ∣ K` for every `k` (no coprimality premise);
  `gcd_le_natAbs_K`: hence `gcd(C_k, D_k) ≤ |K|` when `K ≠ 0`, main's (5);
* `gcd_eq_gcd_K`: main's (6), `gcd(C_k, D_k) = gcd(D_k, K)` when `D_u`, `D_v` are coprime;
* `D_odd`, `D_not_three_dvd`: `D_z` is odd and prime to `3` for nonempty positive words;
* the worked examples: `(1,1,3)`, `(2)` with `K = −14`; the `d = 485` word `(3,1,5)` with
  `gcd(C,D) = 1 ≠ 5 = gcd(D,K)` (the counterexample to dropping the coprimality premise);
  and the exact law `7 ∣ D((1,1,3)^k 2) ↔ k ≡ 3 (mod 6)` behind main's spectrum formula
  `den((1,1,3)^k 2) = (4·32^k − 3·27^k)/(7 if k ≡ 3 mod 6 else 1)`.

Not formalised: the periodicity statement (9), the two-sided bound (7), the `K = 0`
characterisation, and the perturbed mechanical family of §3. Nothing here concerns
convergence; Collatz remains open.
-/

namespace LeanLane
namespace Cyc

/-- `C_z`: `C_[] = 0`, `C_(a :: z) = 3^|z| + 2^a C_z`. -/
def C : List ℕ → ℤ
  | [] => 0
  | a :: z => 3 ^ z.length + 2 ^ a * C z

/-- `D_z = 2^{Σz} − 3^{|z|}`. -/
def D (z : List ℕ) : ℤ := 2 ^ z.sum - 3 ^ z.length

/-- `u^k`. -/
def rep (u : List ℕ) : ℕ → List ℕ
  | 0 => []
  | k + 1 => u ++ rep u k

/-- `G_k`, as the recurrence `G_0 = 0`, `G_{k+1} = Q G_k + P^k`. -/
def G (Q P : ℤ) : ℕ → ℤ
  | 0 => 0
  | k + 1 => Q * G Q P k + P ^ k

/-! ### Concatenation and repetition -/

theorem C_append (u v : List ℕ) : C (u ++ v) = 3 ^ v.length * C u + 2 ^ u.sum * C v := by
  induction u with
  | nil => simp [C]
  | cons a u ih =>
    simp only [List.cons_append, C, List.length_append, List.sum_cons, ih]
    ring

theorem rep_length (u : List ℕ) (k : ℕ) : (rep u k).length = k * u.length := by
  induction k with
  | zero => simp [rep]
  | succ k ih =>
    simp only [rep, List.length_append, ih]
    ring

theorem rep_sum (u : List ℕ) (k : ℕ) : (rep u k).sum = k * u.sum := by
  induction k with
  | zero => simp [rep]
  | succ k ih =>
    simp only [rep, List.sum_append, ih]
    ring

theorem G_mul (Q P : ℤ) (k : ℕ) : (Q - P) * G Q P k = Q ^ k - P ^ k := by
  induction k with
  | zero => simp [G]
  | succ k ih =>
    simp only [G]
    linear_combination Q * ih

theorem C_rep (u : List ℕ) (k : ℕ) : C (rep u k) = C u * G (2 ^ u.sum) (3 ^ u.length) k := by
  induction k with
  | zero => simp [rep, C, G]
  | succ k ih =>
    rw [rep, C_append, ih, rep_length, G, pow_mul']
    ring

/-! ### The word `u^k v` -/

section
variable (u v : List ℕ) (k : ℕ)

/-- Main's (1): `C_k = R C_u G_k + Q^k C_v`. -/
theorem C_w : C (rep u k ++ v) =
    3 ^ v.length * (C u * G (2 ^ u.sum) (3 ^ u.length) k) + (2 ^ u.sum) ^ k * C v := by
  rw [C_append, C_rep, rep_sum, pow_mul']

/-- Main's (2): `D_k = S Q^k − R P^k`. -/
theorem D_w : D (rep u k ++ v) =
    2 ^ v.sum * (2 ^ u.sum) ^ k - 3 ^ v.length * (3 ^ u.length) ^ k := by
  rw [D, List.sum_append, List.length_append, rep_sum, rep_length, pow_add, pow_add, pow_mul',
    pow_mul']
  ring

/-- Main's (3): `D_u C_k − C_u D_k = Q^k K`. -/
theorem commutator :
    D u * C (rep u k ++ v) - C u * D (rep u k ++ v)
      = (2 ^ u.sum) ^ k * (D u * C v - D v * C u) := by
  rw [C_w, D_w]
  have hG := G_mul (2 ^ u.sum) (3 ^ u.length) k
  simp only [D] at hG ⊢
  linear_combination (3 ^ v.length * C u) * hG

end

/-! ### Parity and the gcd bound -/

theorem one_le_sum_of_ne_nil {v : List ℕ} (hv0 : v ≠ []) (hv : ∀ a ∈ v, 1 ≤ a) : 1 ≤ v.sum := by
  cases v with
  | nil => exact absurd rfl hv0
  | cons a v =>
    have := hv a (List.mem_cons_self ..)
    simp only [List.sum_cons]
    omega

theorem D_odd {z : List ℕ} (hz : 1 ≤ z.sum) : ¬ (2 : ℤ) ∣ D z := by
  intro h
  have h2 : (2 : ℤ) ∣ 2 ^ z.sum := dvd_pow_self 2 (by omega)
  have h3 : (2 : ℤ) ∣ 3 ^ z.length := (dvd_sub_right h2).mp h
  exact (by decide : ¬ (2 : ℤ) ∣ 3) (Int.prime_two.dvd_of_dvd_pow h3)

theorem D_not_three_dvd {z : List ℕ} (hz : 1 ≤ z.length) : ¬ (3 : ℤ) ∣ D z := by
  intro h
  have h3 : (3 : ℤ) ∣ 3 ^ z.length := dvd_pow_self 3 (by omega)
  have h2 : (3 : ℤ) ∣ 2 ^ z.sum := (dvd_sub_left h3).mp h
  exact (by decide : ¬ (3 : ℤ) ∣ 2) (Int.prime_three.dvd_of_dvd_pow h2)

/-- **Main's (4).** For every `k`, `gcd(C_k, D_k)` divides `K = D_u C_v − D_v C_u`
(no coprimality premise). -/
theorem gcd_dvd_K (u v : List ℕ) (k : ℕ) (hv : ∀ a ∈ v, 1 ≤ a) (hv0 : v ≠ []) :
    ((Int.gcd (C (rep u k ++ v)) (D (rep u k ++ v)) : ℕ) : ℤ) ∣ D u * C v - D v * C u := by
  have hgC : ((Int.gcd (C (rep u k ++ v)) (D (rep u k ++ v)) : ℕ) : ℤ) ∣ C (rep u k ++ v) :=
    Int.gcd_dvd_left _ _
  have hgD : ((Int.gcd (C (rep u k ++ v)) (D (rep u k ++ v)) : ℕ) : ℤ) ∣ D (rep u k ++ v) :=
    Int.gcd_dvd_right _ _
  set g : ℕ := Int.gcd (C (rep u k ++ v)) (D (rep u k ++ v)) with hg
  have hdvd : (g : ℤ) ∣ (2 ^ u.sum) ^ k * (D u * C v - D v * C u) := by
    rw [← commutator]
    exact dvd_sub (dvd_mul_of_dvd_right hgC _) (dvd_mul_of_dvd_right hgD _)
  have hsum : 1 ≤ (rep u k ++ v).sum := by
    rw [List.sum_append]
    have := one_le_sum_of_ne_nil hv0 hv
    omega
  have hodd : ¬ (2 : ℤ) ∣ (g : ℤ) := fun h2 => D_odd hsum (h2.trans hgD)
  have hodd' : ¬ 2 ∣ g := fun h2 => hodd (by exact_mod_cast h2)
  have hcopN : Nat.Coprime g ((2 ^ u.sum) ^ k) :=
    Nat.Coprime.pow_right _ (Nat.Coprime.pow_right _
      ((Nat.Prime.coprime_iff_not_dvd Nat.prime_two).mpr hodd').symm)
  have hcop : IsCoprime (g : ℤ) (((2 : ℤ) ^ u.sum) ^ k) := by
    have := Nat.isCoprime_iff_coprime.mpr hcopN
    exact_mod_cast this
  exact hcop.dvd_of_dvd_mul_left hdvd

/-- **Main's (5).** When `K ≠ 0`, the cancellation is at most `|K|`, uniformly in `k`. -/
theorem gcd_le_natAbs_K (u v : List ℕ) (k : ℕ) (hv : ∀ a ∈ v, 1 ≤ a) (hv0 : v ≠ [])
    (hK : D u * C v - D v * C u ≠ 0) :
    Int.gcd (C (rep u k ++ v)) (D (rep u k ++ v)) ≤ (D u * C v - D v * C u).natAbs :=
  Nat.le_of_dvd (Int.natAbs_pos.mpr hK) (Int.natAbs_dvd_natAbs.mpr (gcd_dvd_K u v k hv hv0))

/-- **Main's (6).** If `D_u` and `D_v` are coprime, `gcd(C_k, D_k) = gcd(D_k, K)`. -/
theorem gcd_eq_gcd_K (u v : List ℕ) (k : ℕ) (hv : ∀ a ∈ v, 1 ≤ a) (hv0 : v ≠ [])
    (hcop : IsCoprime (D u) (D v)) :
    Int.gcd (C (rep u k ++ v)) (D (rep u k ++ v))
      = Int.gcd (D (rep u k ++ v)) (D u * C v - D v * C u) := by
  have hgD : ((Int.gcd (C (rep u k ++ v)) (D (rep u k ++ v)) : ℕ) : ℤ) ∣ D (rep u k ++ v) :=
    Int.gcd_dvd_right _ _
  have hHD : ((Int.gcd (D (rep u k ++ v)) (D u * C v - D v * C u) : ℕ) : ℤ) ∣
      D (rep u k ++ v) := Int.gcd_dvd_left _ _
  have hHK : ((Int.gcd (D (rep u k ++ v)) (D u * C v - D v * C u) : ℕ) : ℤ) ∣
      D u * C v - D v * C u := Int.gcd_dvd_right _ _
  set g : ℕ := Int.gcd (C (rep u k ++ v)) (D (rep u k ++ v)) with hg
  set H : ℕ := Int.gcd (D (rep u k ++ v)) (D u * C v - D v * C u) with hH
  -- `g ∣ H`
  have hgH : g ∣ H := Int.dvd_gcd hgD (gcd_dvd_K u v k hv hv0)
  -- `H` is coprime to `D_u`
  have hlen : 1 ≤ (rep u k ++ v).length := by
    rw [List.length_append]
    have : 1 ≤ v.length := List.length_pos_of_ne_nil hv0
    omega
  have hcopH : IsCoprime (H : ℤ) (D u) := by
    rw [Int.isCoprime_iff_gcd_eq_one]
    have h1 : ((Int.gcd (H : ℤ) (D u) : ℕ) : ℤ) ∣ (H : ℤ) := Int.gcd_dvd_left _ _
    have h2 : ((Int.gcd (H : ℤ) (D u) : ℕ) : ℤ) ∣ D u := Int.gcd_dvd_right _ _
    set h : ℕ := Int.gcd (H : ℤ) (D u) with hh
    have hQP : (3 : ℤ) ^ u.length ≡ 2 ^ u.sum [ZMOD h] := Int.modEq_iff_dvd.mpr h2
    have hDw : D (rep u k ++ v) ≡ D v * (3 ^ u.length) ^ k [ZMOD h] := by
      rw [D_w]
      have e1 := ((hQP.pow k).mul_left ((2 : ℤ) ^ v.sum)).symm
      have e2 := e1.sub_right ((3 : ℤ) ^ v.length * (3 ^ u.length) ^ k)
      calc 2 ^ v.sum * (2 ^ u.sum) ^ k - 3 ^ v.length * (3 ^ u.length) ^ k
          ≡ 2 ^ v.sum * (3 ^ u.length) ^ k - 3 ^ v.length * (3 ^ u.length) ^ k [ZMOD h] := e2
        _ = D v * (3 ^ u.length) ^ k := by simp only [D]; ring
    have hDw' : (h : ℤ) ∣ D (rep u k ++ v) := h1.trans hHD
    have h3 : (h : ℤ) ∣ D v * (3 ^ u.length) ^ k := (dvd_sub_left hDw').mp hDw.dvd
    have hnot3 : ¬ 3 ∣ h := fun h3' =>
      D_not_three_dvd hlen ((by exact_mod_cast h3' : (3 : ℤ) ∣ (h : ℤ)).trans hDw')
    have hcop3N : Nat.Coprime h ((3 ^ u.length) ^ k) :=
      Nat.Coprime.pow_right _ (Nat.Coprime.pow_right _
        ((Nat.Prime.coprime_iff_not_dvd Nat.prime_three).mpr hnot3).symm)
    have hcop3 : IsCoprime (h : ℤ) (((3 : ℤ) ^ u.length) ^ k) := by
      have := Nat.isCoprime_iff_coprime.mpr hcop3N
      exact_mod_cast this
    have hDv : (h : ℤ) ∣ D v := hcop3.dvd_of_dvd_mul_right h3
    have hunit : IsUnit (h : ℤ) := hcop.isUnit_of_dvd' h2 hDv
    rcases Int.isUnit_iff.mp hunit with h1' | h1'
    · exact_mod_cast h1'
    · omega
  -- `H ∣ C_k`, hence `H ∣ g`
  have hHC : (H : ℤ) ∣ C (rep u k ++ v) := by
    have e : D u * C (rep u k ++ v)
        = C u * D (rep u k ++ v) + (2 ^ u.sum) ^ k * (D u * C v - D v * C u) := by
      have := commutator u v k
      linear_combination this
    have hdvd : (H : ℤ) ∣ D u * C (rep u k ++ v) := by
      rw [e]
      exact dvd_add (dvd_mul_of_dvd_right hHD _) (dvd_mul_of_dvd_right hHK _)
    exact hcopH.dvd_of_dvd_mul_left hdvd
  have hHg : H ∣ g := Int.dvd_gcd hHC hHD
  exact Nat.dvd_antisymm hgH hHg

/-! ### Worked examples -/

example : C [1, 1, 3] = 19 ∧ D [1, 1, 3] = 5 := by norm_num [C, D]

example : C [2] = 1 ∧ D [2] = 1 := by norm_num [C, D]

/-- `K = −14` for `u = (1,1,3)`, `v = (2)`. -/
example : D [1, 1, 3] * C [2] - D [2] * C [1, 1, 3] = -14 := by norm_num [C, D]

example : C [3, 1, 5] = 49 ∧ D [3, 1, 5] = 485 := by norm_num [C, D]

/-- The `d = 485` counterexample to dropping `gcd(D_u, D_v) = 1`: for `u = (3)`, `v = (1,5)`
(`K = −30`), `gcd(C_w, D_w) = 1` while `gcd(D_w, K) = 5`. -/
example : Int.gcd (C [3, 1, 5]) (D [3, 1, 5]) = 1 ∧
    Int.gcd (D [3, 1, 5]) (D [3] * C [1, 5] - D [1, 5] * C [3]) = 5 := by
  norm_num [C, D]

theorem D_example (k : ℕ) : D (rep [1, 1, 3] k ++ [2]) = 4 * 32 ^ k - 3 * 27 ^ k := by
  rw [D_w]
  norm_num

/-- The exact residue law behind main's spectrum formula for `(1,1,3)^k (2)`:
`7 ∣ D_k ↔ k ≡ 3 (mod 6)`. -/
theorem seven_dvd_D_example (k : ℕ) :
    (7 : ℤ) ∣ D (rep [1, 1, 3] k ++ [2]) ↔ k % 6 = 3 := by
  rw [D_example]
  have hk : k = 6 * (k / 6) + k % 6 := (Nat.div_add_mod k 6).symm
  have h32 : (32 : ℤ) ^ k ≡ 32 ^ (k % 6) [ZMOD 7] := by
    conv_lhs => rw [hk]
    rw [pow_add, pow_mul]
    have : (32 : ℤ) ^ 6 ≡ 1 [ZMOD 7] := by decide
    calc ((32 : ℤ) ^ 6) ^ (k / 6) * 32 ^ (k % 6)
        ≡ 1 ^ (k / 6) * 32 ^ (k % 6) [ZMOD 7] := (this.pow _).mul_right _
      _ = 32 ^ (k % 6) := by ring
  have h27 : (27 : ℤ) ^ k ≡ 27 ^ (k % 6) [ZMOD 7] := by
    conv_lhs => rw [hk]
    rw [pow_add, pow_mul]
    have : (27 : ℤ) ^ 6 ≡ 1 [ZMOD 7] := by decide
    calc ((27 : ℤ) ^ 6) ^ (k / 6) * 27 ^ (k % 6)
        ≡ 1 ^ (k / 6) * 27 ^ (k % 6) [ZMOD 7] := (this.pow _).mul_right _
      _ = 27 ^ (k % 6) := by ring
  have hmod : 4 * (32 : ℤ) ^ k - 3 * 27 ^ k ≡ 4 * 32 ^ (k % 6) - 3 * 27 ^ (k % 6) [ZMOD 7] :=
    (h32.mul_left 4).sub (h27.mul_left 3)
  rw [Int.dvd_iff_emod_eq_zero, hmod]
  have hr : k % 6 < 6 := Nat.mod_lt _ (by norm_num)
  generalize k % 6 = r at hr ⊢
  interval_cases r <;> decide

/-- Main's (6) applies to this example (`gcd(D_u, D_v) = gcd(5, 1) = 1`):
`gcd(C_k, D_k) = gcd(D_k, −14)` for every `k`. -/
theorem gcd_example (k : ℕ) :
    Int.gcd (C (rep [1, 1, 3] k ++ [2])) (D (rep [1, 1, 3] k ++ [2]))
      = Int.gcd (D (rep [1, 1, 3] k ++ [2])) (-14) := by
  have h := gcd_eq_gcd_K [1, 1, 3] [2] k (by decide) (by decide)
    (by norm_num [D, Int.isCoprime_iff_gcd_eq_one])
  rwa [show D [1, 1, 3] * C [2] - D [2] * C [1, 1, 3] = -14 by norm_num [C, D]] at h

/-! ### Main's (7): the two-sided bound without a coprimality premise -/

/-- The cancellation factor is coprime to `6`. -/
theorem gcd_coprime_six (u v : List ℕ) (k : ℕ) (hv : ∀ a ∈ v, 1 ≤ a) (hv0 : v ≠ []) :
    Nat.Coprime (Int.gcd (C (rep u k ++ v)) (D (rep u k ++ v))) 6 := by
  have hgD : ((Int.gcd (C (rep u k ++ v)) (D (rep u k ++ v)) : ℕ) : ℤ) ∣ D (rep u k ++ v) :=
    Int.gcd_dvd_right _ _
  set g : ℕ := Int.gcd (C (rep u k ++ v)) (D (rep u k ++ v)) with hg
  have hsum : 1 ≤ (rep u k ++ v).sum := by
    rw [List.sum_append]
    have := one_le_sum_of_ne_nil hv0 hv
    omega
  have hlen : 1 ≤ (rep u k ++ v).length := by
    rw [List.length_append]
    have : 1 ≤ v.length := List.length_pos_of_ne_nil hv0
    omega
  have h2 : ¬ 2 ∣ g := fun h =>
    D_odd hsum ((by exact_mod_cast h : (2 : ℤ) ∣ (g : ℤ)).trans hgD)
  have h3 : ¬ 3 ∣ g := fun h =>
    D_not_three_dvd hlen ((by exact_mod_cast h : (3 : ℤ) ∣ (g : ℤ)).trans hgD)
  show Nat.Coprime g (2 * 3)
  exact Nat.Coprime.mul_right ((Nat.Prime.coprime_iff_not_dvd Nat.prime_two).mpr h2).symm
    ((Nat.Prime.coprime_iff_not_dvd Nat.prime_three).mpr h3).symm

/-- **Main's (7).** With `H = gcd(D_k, K)` and `e = gcd(H, |D_u|)`:
`H/e ∣ gcd(C_k, D_k) ∣ H`, with no coprimality premise. -/
theorem gcd_two_sided (u v : List ℕ) (k : ℕ) (hv : ∀ a ∈ v, 1 ≤ a) (hv0 : v ≠ []) :
    Int.gcd (D (rep u k ++ v)) (D u * C v - D v * C u)
        / Nat.gcd (Int.gcd (D (rep u k ++ v)) (D u * C v - D v * C u)) (D u).natAbs
      ∣ Int.gcd (C (rep u k ++ v)) (D (rep u k ++ v)) ∧
    Int.gcd (C (rep u k ++ v)) (D (rep u k ++ v))
      ∣ Int.gcd (D (rep u k ++ v)) (D u * C v - D v * C u) := by
  have hHD : ((Int.gcd (D (rep u k ++ v)) (D u * C v - D v * C u) : ℕ) : ℤ) ∣
      D (rep u k ++ v) := Int.gcd_dvd_left _ _
  have hHK : ((Int.gcd (D (rep u k ++ v)) (D u * C v - D v * C u) : ℕ) : ℤ) ∣
      D u * C v - D v * C u := Int.gcd_dvd_right _ _
  set H : ℕ := Int.gcd (D (rep u k ++ v)) (D u * C v - D v * C u) with hH
  refine ⟨?_, Int.dvd_gcd (Int.gcd_dvd_right _ _) (gcd_dvd_K u v k hv hv0)⟩
  have hdvd : (H : ℤ) ∣ D u * C (rep u k ++ v) := by
    have e : D u * C (rep u k ++ v)
        = C u * D (rep u k ++ v) + (2 ^ u.sum) ^ k * (D u * C v - D v * C u) := by
      have := commutator u v k
      linear_combination this
    rw [e]
    exact dvd_add (dvd_mul_of_dvd_right hHD _) (dvd_mul_of_dvd_right hHK _)
  have hdvdN : H ∣ (D u).natAbs * (C (rep u k ++ v)).natAbs := by
    rw [← Int.natAbs_mul]
    exact Int.natCast_dvd.mp hdvd
  set e : ℕ := Nat.gcd H (D u).natAbs with he
  have hsum : 1 ≤ (rep u k ++ v).sum := by
    rw [List.sum_append]
    have := one_le_sum_of_ne_nil hv0 hv
    omega
  have hDw0 : D (rep u k ++ v) ≠ 0 := fun h0 => D_odd hsum (h0 ▸ dvd_zero 2)
  have hH0 : 0 < H := Int.gcd_pos_of_ne_zero_left _ hDw0
  have he0 : 0 < e := Nat.gcd_pos_of_pos_left _ hH0
  have heH : e ∣ H := Nat.gcd_dvd_left _ _
  have heD : e ∣ (D u).natAbs := Nat.gcd_dvd_right _ _
  have hcop : Nat.Coprime (H / e) ((D u).natAbs / e) := Nat.coprime_div_gcd_div_gcd he0
  have hdiv : H / e ∣ (D u).natAbs / e * (C (rep u k ++ v)).natAbs := by
    apply Nat.dvd_of_mul_dvd_mul_left he0
    rw [Nat.mul_div_cancel' heH, ← mul_assoc, Nat.mul_div_cancel' heD]
    exact hdvdN
  have h1 : H / e ∣ (C (rep u k ++ v)).natAbs := hcop.dvd_of_dvd_mul_left hdiv
  have h2 : H / e ∣ (D (rep u k ++ v)).natAbs :=
    (Nat.div_dvd_of_dvd heH).trans (Int.natCast_dvd.mp hHD)
  exact Nat.dvd_gcd h1 h2

/-! ### Main's (9): the cancellation factor is periodic in `k` -/

/-- Cancelling a nonzero factor `a` presented through `|a|`. -/
theorem dvd_of_mul_natAbs_dvd {n : ℕ} {a X : ℤ} (ha : a ≠ 0)
    (h : ((n * a.natAbs : ℕ) : ℤ) ∣ a * X) : (n : ℤ) ∣ X := by
  have h' : n * a.natAbs ∣ a.natAbs * X.natAbs := by
    rw [← Int.natAbs_mul]
    exact Int.natCast_dvd.mp h
  rw [mul_comm] at h'
  exact Int.natCast_dvd.mpr (Nat.dvd_of_mul_dvd_mul_left (Int.natAbs_pos.mpr ha) h')

/-- **Main's (9).** Write `|K| = 2^a 3^b K₀`. If `Q^T ≡ P^T ≡ 1 (mod K₀|D_u|)`, then the
cancellation factor has period `T`: `gcd(C_{k+T}, D_{k+T}) = gcd(C_k, D_k)` for every `k`. -/
theorem gcd_periodic (u v : List ℕ) (hu : ∀ a ∈ u, 1 ≤ a) (hu0 : u ≠ [])
    (hv : ∀ a ∈ v, 1 ≤ a) (hv0 : v ≠ []) (a b K₀ : ℕ)
    (hK : (D u * C v - D v * C u).natAbs = 2 ^ a * 3 ^ b * K₀) (T : ℕ)
    (hQ : (2 ^ u.sum) ^ T ≡ 1 [MOD K₀ * (D u).natAbs])
    (hP : (3 ^ u.length) ^ T ≡ 1 [MOD K₀ * (D u).natAbs]) (k : ℕ) :
    Int.gcd (C (rep u (k + T) ++ v)) (D (rep u (k + T) ++ v))
      = Int.gcd (C (rep u k ++ v)) (D (rep u k ++ v)) := by
  have hDu : D u ≠ 0 := fun h0 => D_odd (one_le_sum_of_ne_nil hu0 hu) (h0 ▸ dvd_zero 2)
  -- the two congruences, in `ℤ`
  have hQZ : ((K₀ * (D u).natAbs : ℕ) : ℤ) ∣ ((2 : ℤ) ^ u.sum) ^ T - 1 := by
    have := hQ.symm.dvd
    exact_mod_cast this
  have hPZ : ((K₀ * (D u).natAbs : ℕ) : ℤ) ∣ ((3 : ℤ) ^ u.length) ^ T - 1 := by
    have := hP.symm.dvd
    exact_mod_cast this
  have hK₀L : (K₀ : ℤ) ∣ ((K₀ * (D u).natAbs : ℕ) : ℤ) := by
    push_cast
    exact dvd_mul_right _ _
  have hK₀Q : (K₀ : ℤ) ∣ ((2 : ℤ) ^ u.sum) ^ T - 1 := hK₀L.trans hQZ
  have hK₀P : (K₀ : ℤ) ∣ ((3 : ℤ) ^ u.length) ^ T - 1 := hK₀L.trans hPZ
  -- `K₀ ∣ G_{k+T} − G_k`
  have hGdiff : D u * (G (2 ^ u.sum) (3 ^ u.length) (k + T) - G (2 ^ u.sum) (3 ^ u.length) k)
      = (2 ^ u.sum) ^ k * (((2 : ℤ) ^ u.sum) ^ T - 1)
        - (3 ^ u.length) ^ k * (((3 : ℤ) ^ u.length) ^ T - 1) := by
    have h1 := G_mul (2 ^ u.sum) (3 ^ u.length) (k + T)
    have h2 := G_mul (2 ^ u.sum) (3 ^ u.length) k
    simp only [D]
    linear_combination h1 - h2
  have hK₀G : (K₀ : ℤ) ∣ G (2 ^ u.sum) (3 ^ u.length) (k + T) - G (2 ^ u.sum) (3 ^ u.length) k := by
    apply dvd_of_mul_natAbs_dvd hDu
    rw [hGdiff]
    exact dvd_sub (dvd_mul_of_dvd_right hQZ _) (dvd_mul_of_dvd_right hPZ _)
  -- `C` and `D` are periodic modulo `K₀`
  have hC : (K₀ : ℤ) ∣ C (rep u (k + T) ++ v) - C (rep u k ++ v) := by
    rw [C_w, C_w]
    have e : (3 ^ v.length * (C u * G (2 ^ u.sum) (3 ^ u.length) (k + T))
          + (2 ^ u.sum) ^ (k + T) * C v)
        - (3 ^ v.length * (C u * G (2 ^ u.sum) (3 ^ u.length) k) + (2 ^ u.sum) ^ k * C v)
        = 3 ^ v.length * C u
            * (G (2 ^ u.sum) (3 ^ u.length) (k + T) - G (2 ^ u.sum) (3 ^ u.length) k)
          + (2 ^ u.sum) ^ k * (((2 : ℤ) ^ u.sum) ^ T - 1) * C v := by ring
    rw [e]
    exact dvd_add (dvd_mul_of_dvd_right hK₀G _)
      (dvd_mul_of_dvd_left (dvd_mul_of_dvd_right hK₀Q _) _)
  have hD : (K₀ : ℤ) ∣ D (rep u (k + T) ++ v) - D (rep u k ++ v) := by
    rw [D_w, D_w]
    have e : (2 ^ v.sum * (2 ^ u.sum) ^ (k + T) - 3 ^ v.length * (3 ^ u.length) ^ (k + T))
        - (2 ^ v.sum * (2 ^ u.sum) ^ k - 3 ^ v.length * (3 ^ u.length) ^ k)
        = 2 ^ v.sum * (2 ^ u.sum) ^ k * (((2 : ℤ) ^ u.sum) ^ T - 1)
          - 3 ^ v.length * (3 ^ u.length) ^ k * (((3 : ℤ) ^ u.length) ^ T - 1) := by ring
    rw [e]
    exact dvd_sub (dvd_mul_of_dvd_right hK₀Q _) (dvd_mul_of_dvd_right hK₀P _)
  -- both cancellation factors divide `K₀`
  have hg_dvd : ∀ j, Int.gcd (C (rep u j ++ v)) (D (rep u j ++ v)) ∣ K₀ := by
    intro j
    have h1 : Int.gcd (C (rep u j ++ v)) (D (rep u j ++ v)) ∣ 2 ^ a * 3 ^ b * K₀ := by
      rw [← hK]
      exact Int.natCast_dvd.mp (gcd_dvd_K u v j hv hv0)
    have h6 := gcd_coprime_six u v j hv hv0
    have hcop : Nat.Coprime (Int.gcd (C (rep u j ++ v)) (D (rep u j ++ v))) (2 ^ a * 3 ^ b) :=
      Nat.Coprime.mul_right (Nat.Coprime.pow_right _ (h6.coprime_dvd_right (by norm_num)))
        (Nat.Coprime.pow_right _ (h6.coprime_dvd_right (by norm_num)))
    exact hcop.dvd_of_dvd_mul_left h1
  have hgT := hg_dvd (k + T)
  have hgk := hg_dvd k
  apply Nat.dvd_antisymm
  · apply Int.dvd_gcd
    · have h1 : ((Int.gcd (C (rep u (k + T) ++ v)) (D (rep u (k + T) ++ v)) : ℕ) : ℤ) ∣
          C (rep u (k + T) ++ v) := Int.gcd_dvd_left _ _
      have h2 := (Int.natCast_dvd_natCast.mpr hgT).trans hC
      exact (dvd_sub_right h1).mp h2
    · have h1 : ((Int.gcd (C (rep u (k + T) ++ v)) (D (rep u (k + T) ++ v)) : ℕ) : ℤ) ∣
          D (rep u (k + T) ++ v) := Int.gcd_dvd_right _ _
      have h2 := (Int.natCast_dvd_natCast.mpr hgT).trans hD
      exact (dvd_sub_right h1).mp h2
  · apply Int.dvd_gcd
    · have h1 : ((Int.gcd (C (rep u k ++ v)) (D (rep u k ++ v)) : ℕ) : ℤ) ∣
          C (rep u k ++ v) := Int.gcd_dvd_left _ _
      have h2 := (Int.natCast_dvd_natCast.mpr hgk).trans hC
      exact (dvd_sub_left h1).mp h2
    · have h1 : ((Int.gcd (C (rep u k ++ v)) (D (rep u k ++ v)) : ℕ) : ℤ) ∣
          D (rep u k ++ v) := Int.gcd_dvd_right _ _
      have h2 := (Int.natCast_dvd_natCast.mpr hgk).trans hD
      exact (dvd_sub_left h1).mp h2

/-- **Main's (9) with the explicit period `φ(K₀|D_u|)`**, for `K₀` coprime to `6`. -/
theorem gcd_periodic_totient (u v : List ℕ) (hu : ∀ a ∈ u, 1 ≤ a) (hu0 : u ≠ [])
    (hv : ∀ a ∈ v, 1 ≤ a) (hv0 : v ≠ []) (a b K₀ : ℕ)
    (hK : (D u * C v - D v * C u).natAbs = 2 ^ a * 3 ^ b * K₀) (hK₀ : Nat.Coprime K₀ 6)
    (k : ℕ) :
    Int.gcd (C (rep u (k + Nat.totient (K₀ * (D u).natAbs)) ++ v))
        (D (rep u (k + Nat.totient (K₀ * (D u).natAbs)) ++ v))
      = Int.gcd (C (rep u k ++ v)) (D (rep u k ++ v)) := by
  have hodd := D_odd (one_le_sum_of_ne_nil hu0 hu)
  have hnot3 := D_not_three_dvd (List.length_pos_of_ne_nil hu0)
  have h2 : ¬ 2 ∣ (D u).natAbs := fun h => hodd (by exact_mod_cast Int.natCast_dvd.mpr h)
  have h3 : ¬ 3 ∣ (D u).natAbs := fun h => hnot3 (by exact_mod_cast Int.natCast_dvd.mpr h)
  apply gcd_periodic u v hu hu0 hv hv0 a b K₀ hK
  · apply Nat.ModEq.pow_totient
    apply Nat.Coprime.pow_left
    exact Nat.Coprime.mul_right (hK₀.coprime_dvd_right (by norm_num)).symm
      ((Nat.Prime.coprime_iff_not_dvd Nat.prime_two).mpr h2)
  · apply Nat.ModEq.pow_totient
    apply Nat.Coprime.pow_left
    exact Nat.Coprime.mul_right (hK₀.coprime_dvd_right (by norm_num)).symm
      ((Nat.Prime.coprime_iff_not_dvd Nat.prime_three).mpr h3)

/-! ### Two growing blocks `u^k v^ℓ` (main's C002 `PROPORTIONAL.md` §§1–2) -/

/-- The cancellation factor of any word with positive sum and length is coprime to `6`. -/
theorem gcd_coprime_six' (w : List ℕ) (hsum : 1 ≤ w.sum) (hlen : 1 ≤ w.length) :
    Nat.Coprime (Int.gcd (C w) (D w)) 6 := by
  have hgD : ((Int.gcd (C w) (D w) : ℕ) : ℤ) ∣ D w := Int.gcd_dvd_right _ _
  have h2 : ¬ 2 ∣ Int.gcd (C w) (D w) := fun h =>
    D_odd hsum ((by exact_mod_cast h : (2 : ℤ) ∣ ((Int.gcd (C w) (D w) : ℕ) : ℤ)).trans hgD)
  have h3 : ¬ 3 ∣ Int.gcd (C w) (D w) := fun h =>
    D_not_three_dvd hlen
      ((by exact_mod_cast h : (3 : ℤ) ∣ ((Int.gcd (C w) (D w) : ℕ) : ℤ)).trans hgD)
  show Nat.Coprime _ (2 * 3)
  exact Nat.Coprime.mul_right ((Nat.Prime.coprime_iff_not_dvd Nat.prime_two).mpr h2).symm
    ((Nat.Prime.coprime_iff_not_dvd Nat.prime_three).mpr h3).symm

section TwoBlocks
variable (u v : List ℕ) (k l : ℕ)

/-- C002's (1). -/
theorem C_two : C (rep u k ++ rep v l) =
    (3 ^ v.length) ^ l * (C u * G (2 ^ u.sum) (3 ^ u.length) k)
      + (2 ^ u.sum) ^ k * (C v * G (2 ^ v.sum) (3 ^ v.length) l) := by
  rw [C_append, C_rep, C_rep, rep_length, rep_sum, pow_mul', pow_mul']

/-- C002's (2). -/
theorem D_two : D (rep u k ++ rep v l) =
    (2 ^ v.sum) ^ l * (2 ^ u.sum) ^ k - (3 ^ v.length) ^ l * (3 ^ u.length) ^ k := by
  rw [D, List.sum_append, List.length_append, rep_sum, rep_sum, rep_length, rep_length,
    pow_add, pow_add, pow_mul', pow_mul', pow_mul', pow_mul']
  ring

/-- C002's (3): `D_u C − C_u D = Q^k G_v(ℓ) K`. -/
theorem commutator_two_u :
    D u * C (rep u k ++ rep v l) - C u * D (rep u k ++ rep v l)
      = (2 ^ u.sum) ^ k * G (2 ^ v.sum) (3 ^ v.length) l * (D u * C v - D v * C u) := by
  rw [C_two, D_two]
  have h1 := G_mul (2 ^ u.sum) (3 ^ u.length) k
  have h2 := G_mul (2 ^ v.sum) (3 ^ v.length) l
  simp only [D] at h1 h2 ⊢
  linear_combination ((3 ^ v.length) ^ l * C u) * h1 + ((2 ^ u.sum) ^ k * C u) * h2

/-- C002's (4): `D_v C − C_v D = −R^ℓ G_u(k) K`. -/
theorem commutator_two_v :
    D v * C (rep u k ++ rep v l) - C v * D (rep u k ++ rep v l)
      = -((3 ^ v.length) ^ l * G (2 ^ u.sum) (3 ^ u.length) k * (D u * C v - D v * C u)) := by
  rw [C_two, D_two]
  have h1 := G_mul (2 ^ u.sum) (3 ^ u.length) k
  have h2 := G_mul (2 ^ v.sum) (3 ^ v.length) l
  simp only [D] at h1 h2 ⊢
  linear_combination ((2 ^ u.sum) ^ k * C v) * h2 + ((3 ^ v.length) ^ l * C v) * h1

end TwoBlocks

/-- **C002's (5).** `gcd(C, D) ∣ |K| · gcd(G_u(k), G_v(ℓ))`, with no coprimality premise on
the blocks (both blocks nonempty and positive, `k, ℓ ≥ 1`). -/
theorem gcd_dvd_K_mul_gcd (u v : List ℕ) (k l : ℕ) (_hu : ∀ a ∈ u, 1 ≤ a) (_hu0 : u ≠ [])
    (hv : ∀ a ∈ v, 1 ≤ a) (hv0 : v ≠ []) (_hk : 1 ≤ k) (hl : 1 ≤ l) :
    Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l))
      ∣ (D u * C v - D v * C u).natAbs
          * Int.gcd (G (2 ^ u.sum) (3 ^ u.length) k) (G (2 ^ v.sum) (3 ^ v.length) l) := by
  have hgC : ((Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℕ) : ℤ) ∣
      C (rep u k ++ rep v l) := Int.gcd_dvd_left _ _
  have hgD : ((Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℕ) : ℤ) ∣
      D (rep u k ++ rep v l) := Int.gcd_dvd_right _ _
  set g : ℕ := Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) with hg
  have hsum : 1 ≤ (rep u k ++ rep v l).sum := by
    rw [List.sum_append, rep_sum, rep_sum]
    have := Nat.mul_le_mul hl (one_le_sum_of_ne_nil hv0 hv)
    omega
  have hlen : 1 ≤ (rep u k ++ rep v l).length := by
    rw [List.length_append, rep_length, rep_length]
    have := Nat.mul_le_mul hl (List.length_pos_of_ne_nil hv0)
    omega
  have h6 := gcd_coprime_six' _ hsum hlen
  have hcopQ : IsCoprime (g : ℤ) (((2 : ℤ) ^ u.sum) ^ k) := by
    have := Nat.isCoprime_iff_coprime.mpr
      (Nat.Coprime.pow_right k (Nat.Coprime.pow_right u.sum
        (h6.coprime_dvd_right (by norm_num : 2 ∣ 6))))
    exact_mod_cast this
  have hcopR : IsCoprime (g : ℤ) (((3 : ℤ) ^ v.length) ^ l) := by
    have := Nat.isCoprime_iff_coprime.mpr
      (Nat.Coprime.pow_right l (Nat.Coprime.pow_right v.length
        (h6.coprime_dvd_right (by norm_num : 3 ∣ 6))))
    exact_mod_cast this
  -- `g ∣ K G_v` and `g ∣ K G_u`
  have h1 : (g : ℤ) ∣ (2 ^ u.sum) ^ k * (G (2 ^ v.sum) (3 ^ v.length) l * (D u * C v - D v * C u)) := by
    rw [← mul_assoc, ← commutator_two_u]
    exact dvd_sub (dvd_mul_of_dvd_right hgC _) (dvd_mul_of_dvd_right hgD _)
  have h2 : (g : ℤ) ∣ (3 ^ v.length) ^ l * (G (2 ^ u.sum) (3 ^ u.length) k * (D u * C v - D v * C u)) := by
    have := dvd_sub (dvd_mul_of_dvd_right hgC (D v)) (dvd_mul_of_dvd_right hgD (C v))
    rw [commutator_two_v, dvd_neg, mul_assoc] at this
    exact this
  have h1' : (g : ℤ) ∣ (D u * C v - D v * C u) * G (2 ^ v.sum) (3 ^ v.length) l := by
    rw [mul_comm]; exact hcopQ.dvd_of_dvd_mul_left h1
  have h2' : (g : ℤ) ∣ (D u * C v - D v * C u) * G (2 ^ u.sum) (3 ^ u.length) k := by
    rw [mul_comm]; exact hcopR.dvd_of_dvd_mul_left h2
  have := Int.dvd_gcd h2' h1'
  rwa [Int.gcd_mul_left] at this

/-! ### Strong divisibility of `U^i − V^i` -/

/-- For coprime `U, V`, `gcd(U^i − V^i, U^j − V^j) = |U^gcd(i,j) − V^gcd(i,j)|`. -/
theorem gcd_pow_sub_pow (U V : ℤ) (hUV : IsCoprime U V) (i j : ℕ) :
    Int.gcd (U ^ i - V ^ i) (U ^ j - V ^ j)
      = (U ^ Nat.gcd i j - V ^ Nat.gcd i j).natAbs := by
  induction i, j using Nat.gcd.induction with
  | H0 j => simp
  | H1 i j hi ih =>
    rw [Nat.gcd_rec, ← ih]
    have hj : j = i * (j / i) + j % i := (Nat.div_add_mod j i).symm
    have hsplit : U ^ j - V ^ j
        = U ^ (i * (j / i)) * (U ^ (j % i) - V ^ (j % i))
          + V ^ (j % i) * ((U ^ i) ^ (j / i) - (V ^ i) ^ (j / i)) := by
      conv_lhs => rw [hj]
      ring
    have hdvd : U ^ i - V ^ i ∣ (U ^ i) ^ (j / i) - (V ^ i) ^ (j / i) := sub_dvd_pow_sub_pow _ _ _
    have hcopU : IsCoprime U (U ^ i - V ^ i) := by
      have h1 : IsCoprime U (-(V ^ i)) := (hUV.pow_right (n := i)).neg_right
      have h2 := h1.add_mul_left_right (U ^ (i - 1))
      have e : U * U ^ (i - 1) = U ^ i := by rw [← pow_succ', Nat.sub_add_cancel hi]
      rwa [e, show -(V ^ i) + U ^ i = U ^ i - V ^ i by ring] at h2
    have hcop : IsCoprime (U ^ (i * (j / i))) (U ^ i - V ^ i) := hcopU.pow_left
    apply Nat.dvd_antisymm
    · apply Int.dvd_gcd
      · have hA : ((Int.gcd (U ^ i - V ^ i) (U ^ j - V ^ j) : ℕ) : ℤ) ∣
            U ^ (i * (j / i)) * (U ^ (j % i) - V ^ (j % i))
              + V ^ (j % i) * ((U ^ i) ^ (j / i) - (V ^ i) ^ (j / i)) := by
          rw [← hsplit]
          exact Int.gcd_dvd_right _ _
        have hB : ((Int.gcd (U ^ i - V ^ i) (U ^ j - V ^ j) : ℕ) : ℤ) ∣
            V ^ (j % i) * ((U ^ i) ^ (j / i) - (V ^ i) ^ (j / i)) :=
          dvd_mul_of_dvd_right ((Int.gcd_dvd_left _ _).trans hdvd) _
        have hC := (dvd_add_left hB).mp hA
        have hcop' : IsCoprime ((Int.gcd (U ^ i - V ^ i) (U ^ j - V ^ j) : ℕ) : ℤ)
            (U ^ (i * (j / i))) :=
          (hcop.of_isCoprime_of_dvd_right (Int.gcd_dvd_left _ _)).symm
        exact hcop'.dvd_of_dvd_mul_left hC
      · exact Int.gcd_dvd_left _ _
    · apply Int.dvd_gcd
      · exact Int.gcd_dvd_right _ _
      · rw [hsplit]
        exact dvd_add (dvd_mul_of_dvd_right (Int.gcd_dvd_left _ _) _)
          (dvd_mul_of_dvd_right ((Int.gcd_dvd_right _ _).trans hdvd) _)

/-! ### Intercepts of equal-total words: positivity, parity, injectivity, the bound (U2) -/

theorem C_nonneg : ∀ z : List ℕ, 0 ≤ C z
  | [] => le_rfl
  | a :: z => by
    simp only [C]
    exact add_nonneg (by positivity) (mul_nonneg (by positivity) (C_nonneg z))

theorem C_pos {z : List ℕ} (hz : z ≠ []) : 0 < C z := by
  cases z with
  | nil => exact absurd rfl hz
  | cons a z =>
    simp only [C]
    have := C_nonneg z
    positivity

theorem C_odd {z : List ℕ} (hz : z ≠ []) (hpos : ∀ a ∈ z, 1 ≤ a) : Odd (C z) := by
  cases z with
  | nil => exact absurd rfl hz
  | cons a z =>
    simp only [C]
    have ha : 1 ≤ a := hpos a (List.mem_cons_self ..)
    exact Odd.add_even (Odd.pow ⟨1, by norm_num⟩)
      ((even_two.pow_of_ne_zero (by omega)).mul_right _)

theorem length_le_sum : ∀ z : List ℕ, (∀ a ∈ z, 1 ≤ a) → z.length ≤ z.sum
  | [], _ => le_rfl
  | a :: z, hpos => by
    have ha : 1 ≤ a := hpos a (List.mem_cons_self ..)
    have := length_le_sum z (fun x hx => hpos x (List.mem_cons_of_mem _ hx))
    simp only [List.length_cons, List.sum_cons]
    omega

/-- Distinct positive words of equal length and equal total have distinct intercepts
(`v₂(C − 3^{m−1}) = a₀` recovers the first letter; the last letter is fixed by the total). -/
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

/-- **C002's (U2).** For a positive word of length `m` and total `A`,
`2^m C_z ≤ 2^A (3^m − 2^m)`. -/
theorem two_pow_mul_C_le : ∀ z : List ℕ, (∀ a ∈ z, 1 ≤ a) →
    (2 : ℤ) ^ z.length * C z ≤ 2 ^ z.sum * (3 ^ z.length - 2 ^ z.length)
  | [], _ => by simp [C]
  | a :: z, hpos => by
    have hpos' : ∀ x ∈ z, 1 ≤ x := fun x hx => hpos x (List.mem_cons_of_mem _ hx)
    have ih := two_pow_mul_C_le z hpos'
    have ha : 1 ≤ a := hpos a (List.mem_cons_self ..)
    have hlen : z.length ≤ z.sum := length_le_sum z hpos'
    simp only [C, List.length_cons, List.sum_cons]
    have h2 : (2 : ℤ) ^ (z.length + 1) ≤ 2 ^ (a + z.sum) :=
      pow_le_pow_right₀ (by norm_num) (by omega)
    have h3 : (0 : ℤ) < 3 ^ z.length := by positivity
    have hT : (0 : ℤ) ≤ 2 ^ a := by positivity
    have p1 := mul_le_mul_of_nonneg_left ih (by positivity : (0 : ℤ) ≤ 2 * 2 ^ a)
    have p2 := mul_le_mul_of_nonneg_left h2 h3.le
    simp only [pow_succ, pow_add] at h2 p2 ⊢
    nlinarith [p1, p2]

/-! ### C002's uniform equal-total exclusion (U1) -/

/-- The Euclid step `U^n − V^n = U^{n−h}(U^h − V^h) + V^h(U^{n−h} − V^{n−h})` gives
`U^{n−h}(U^h − V^h) < U^n − V^n` when `0 ≤ V < U` and `h < n`. -/
theorem pow_sub_pow_lower (U V : ℤ) (hV : 0 < V) (hUV : V < U) {h n : ℕ} (hhn : h < n) :
    U ^ (n - h) * (U ^ h - V ^ h) < U ^ n - V ^ n := by
  have e : U ^ n - V ^ n = U ^ (n - h) * (U ^ h - V ^ h) + V ^ h * (U ^ (n - h) - V ^ (n - h)) := by
    have : n = (n - h) + h := by omega
    conv_lhs => rw [this]
    ring
  rw [e]
  have hpos : 0 < V ^ h * (U ^ (n - h) - V ^ (n - h)) :=
    mul_pos (pow_pos hV h) (sub_pos.mpr (pow_lt_pow_left₀ hUV hV.le (by omega)))
  linarith

/-- **C002's (U1), full form.** Two distinct positive words `u ≠ v` of the same length `m`
and total `A`, with `U = 2^A > V = 3^m`, and `k, ℓ ≥ 1`, `k + ℓ ≥ 3`: the reduced
denominator of `u^k v^ℓ` exceeds `2^m · U/V`, i.e. `U · 2^m · gcd(C, D) < V · D`. -/
theorem uniform_two_block_strong (u v : List ℕ) (hu : ∀ a ∈ u, 1 ≤ a) (hv : ∀ a ∈ v, 1 ≤ a)
    (hu0 : u ≠ []) (huv : u ≠ v) (hlen : u.length = v.length) (hsum : u.sum = v.sum)
    (hUV : (3 : ℤ) ^ u.length < 2 ^ u.sum) (k l : ℕ) (hk : 1 ≤ k) (hl : 1 ≤ l)
    (hn : 3 ≤ k + l) :
    (2 : ℤ) ^ u.sum
        * (2 ^ u.length * (Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℤ))
      < 3 ^ u.length * D (rep u k ++ rep v l) := by
  have hv0 : v ≠ [] := fun h => hu0 (List.length_eq_zero_iff.mp (hlen.trans (by simp [h])))
  -- the common block data
  have hDv : D v = D u := by simp [D, hlen, hsum]
  have hE : D u = 2 ^ u.sum - 3 ^ u.length := rfl
  -- the gcd divides `|J| · |U^h − V^h|`
  have h5 := gcd_dvd_K_mul_gcd u v k l hu hu0 hv hv0 hk hl
  rw [hDv, ← hsum, ← hlen] at h5
  have hK : (D u * C v - D u * C u).natAbs = (D u).natAbs * (C v - C u).natAbs := by
    rw [← Int.natAbs_mul]; congr 1; ring
  have hcop23 : IsCoprime ((2 : ℤ) ^ u.sum) (3 ^ u.length) :=
    (Int.isCoprime_iff_gcd_eq_one.mpr (by decide)).pow
  have hsd := gcd_pow_sub_pow (2 ^ u.sum) (3 ^ u.length) hcop23 k l
  rw [← G_mul (2 ^ u.sum) (3 ^ u.length) k, ← G_mul (2 ^ u.sum) (3 ^ u.length) l, ← hE,
    Int.gcd_mul_left] at hsd
  have h5' : Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l))
      ∣ (C v - C u).natAbs
        * (((2 : ℤ) ^ u.sum) ^ Nat.gcd k l - (3 ^ u.length) ^ Nat.gcd k l).natAbs := by
    rw [hK] at h5
    have e : (D u).natAbs * (C v - C u).natAbs
        * Int.gcd (G (2 ^ u.sum) (3 ^ u.length) k) (G (2 ^ u.sum) (3 ^ u.length) l)
        = (C v - C u).natAbs * ((D u).natAbs
          * Int.gcd (G (2 ^ u.sum) (3 ^ u.length) k) (G (2 ^ u.sum) (3 ^ u.length) l)) := by ring
    rw [e, hsd] at h5
    exact h5
  -- numeric data
  have hh1 : 1 ≤ Nat.gcd k l := Nat.gcd_pos_of_pos_left _ hk
  have hhk : Nat.gcd k l ≤ k := Nat.gcd_le_left _ hk
  have hhl : Nat.gcd k l ≤ l := Nat.gcd_le_right _ hl
  have hHh : (0 : ℤ) < ((2 : ℤ) ^ u.sum) ^ Nat.gcd k l - (3 ^ u.length) ^ Nat.gcd k l :=
    sub_pos.mpr (pow_lt_pow_left₀ hUV (by positivity) (by omega))
  have hJ : (0 : ℤ) < |C v - C u| := by
    rw [abs_pos, sub_ne_zero]
    intro hCeq
    exact huv (C_injective u v hu hv hlen hsum hCeq.symm)
  -- `|J| 2^m < 2^A 3^m` from (U2) for both words
  have hJbound : (2 : ℤ) ^ u.length * |C v - C u| < 2 ^ u.sum * 3 ^ u.length := by
    have bu := two_pow_mul_C_le u hu
    have bv := two_pow_mul_C_le v hv
    rw [← hlen, ← hsum] at bv
    have hCu := C_pos hu0
    have hCv := C_pos hv0
    have h2m : (0 : ℤ) < 2 ^ u.length := by positivity
    have h2A : (0 : ℤ) < 2 ^ u.sum := by positivity
    have q1 := mul_pos h2A h2m
    have q2 := mul_pos h2m hCu
    have q3 := mul_pos h2m hCv
    rcases le_or_gt (C u) (C v) with hle | hgt
    · rw [abs_of_nonneg (by linarith)]
      nlinarith [bv, q1, q2]
    · rw [abs_of_neg (by linarith)]
      nlinarith [bu, q1, q3]
  -- `D w = U^n − V^n`
  have hDw : D (rep u k ++ rep v l)
      = ((2 : ℤ) ^ u.sum) ^ (k + l) - (3 ^ u.length) ^ (k + l) := by
    rw [D_two, ← hlen, ← hsum]
    ring
  -- assemble
  have hg_le : ((Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℕ) : ℤ)
      ≤ |C v - C u| * (((2 : ℤ) ^ u.sum) ^ Nat.gcd k l - (3 ^ u.length) ^ Nat.gcd k l) := by
    have hpos := mul_pos hJ hHh
    have hdvd : ((Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℕ) : ℤ)
        ∣ |C v - C u| * (((2 : ℤ) ^ u.sum) ^ Nat.gcd k l - (3 ^ u.length) ^ Nat.gcd k l) := by
      have := Int.natCast_dvd_natCast.mpr h5'
      rw [Nat.cast_mul, Int.natCast_natAbs, Int.natCast_natAbs, abs_of_pos hHh] at this
      exact this
    exact Int.le_of_dvd hpos hdvd
  have hlow := pow_sub_pow_lower ((2 : ℤ) ^ u.sum) (3 ^ u.length) (by positivity) hUV
    (show Nat.gcd k l < k + l by omega)
  have h2m : (0 : ℤ) < 2 ^ u.length := by positivity
  have h2A : (0 : ℤ) < 2 ^ u.sum := by positivity
  have h3m : (0 : ℤ) < 3 ^ u.length := by positivity
  have hU2 : (2 : ℤ) ^ u.sum * 2 ^ u.sum ≤ ((2 : ℤ) ^ u.sum) ^ (k + l - Nat.gcd k l) := by
    rw [← pow_two]
    exact pow_le_pow_right₀ (one_le_pow₀ (by norm_num)) (by omega)
  calc (2 : ℤ) ^ u.sum
        * (2 ^ u.length * ((Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℕ) : ℤ))
      ≤ 2 ^ u.sum * (2 ^ u.length * (|C v - C u|
          * (((2 : ℤ) ^ u.sum) ^ Nat.gcd k l - (3 ^ u.length) ^ Nat.gcd k l))) :=
        mul_le_mul_of_nonneg_left (mul_le_mul_of_nonneg_left hg_le h2m.le) h2A.le
    _ = 2 ^ u.sum * ((2 ^ u.length * |C v - C u|)
          * (((2 : ℤ) ^ u.sum) ^ Nat.gcd k l - (3 ^ u.length) ^ Nat.gcd k l)) := by ring
    _ < 2 ^ u.sum * ((2 ^ u.sum * 3 ^ u.length)
          * (((2 : ℤ) ^ u.sum) ^ Nat.gcd k l - (3 ^ u.length) ^ Nat.gcd k l)) :=
        mul_lt_mul_of_pos_left (mul_lt_mul_of_pos_right hJbound hHh) h2A
    _ = 3 ^ u.length * ((2 ^ u.sum * 2 ^ u.sum)
          * (((2 : ℤ) ^ u.sum) ^ Nat.gcd k l - (3 ^ u.length) ^ Nat.gcd k l)) := by ring
    _ ≤ 3 ^ u.length * (((2 : ℤ) ^ u.sum) ^ (k + l - Nat.gcd k l)
          * (((2 : ℤ) ^ u.sum) ^ Nat.gcd k l - (3 ^ u.length) ^ Nat.gcd k l)) :=
        mul_le_mul_of_nonneg_left (mul_le_mul_of_nonneg_right hU2 hHh.le) h3m.le
    _ < 3 ^ u.length * (((2 : ℤ) ^ u.sum) ^ (k + l) - (3 ^ u.length) ^ (k + l)) :=
        mul_lt_mul_of_pos_left hlow h3m
    _ = 3 ^ u.length * D (rep u k ++ rep v l) := by rw [hDw]

/-- **C002's (U1), weaker form.** Under the same hypotheses the reduced denominator exceeds
`2^m`, i.e. `2^m · gcd(C, D) < D`. -/
theorem uniform_two_block (u v : List ℕ) (hu : ∀ a ∈ u, 1 ≤ a) (hv : ∀ a ∈ v, 1 ≤ a)
    (hu0 : u ≠ []) (huv : u ≠ v) (hlen : u.length = v.length) (hsum : u.sum = v.sum)
    (hUV : (3 : ℤ) ^ u.length < 2 ^ u.sum) (k l : ℕ) (hk : 1 ≤ k) (hl : 1 ≤ l)
    (hn : 3 ≤ k + l) :
    (2 : ℤ) ^ u.length * (Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℤ)
      < D (rep u k ++ rep v l) := by
  have hstrong := uniform_two_block_strong u v hu hv hu0 huv hlen hsum hUV k l hk hl hn
  have hv0 : v ≠ [] := fun h => hu0 (List.length_eq_zero_iff.mp (hlen.trans (by simp [h])))
  have hsumw : 1 ≤ (rep u k ++ rep v l).sum := by
    rw [List.sum_append, rep_sum, rep_sum]
    have := Nat.mul_le_mul hl (one_le_sum_of_ne_nil hv0 hv)
    omega
  have hDw0 : D (rep u k ++ rep v l) ≠ 0 := fun h0 => D_odd hsumw (h0 ▸ dvd_zero 2)
  have hgpos : (0 : ℤ) < (Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℤ) := by
    exact_mod_cast Int.gcd_pos_of_ne_zero_right _ hDw0
  have h2m : (0 : ℤ) < 2 ^ u.length := by positivity
  have h3m : (0 : ℤ) < 3 ^ u.length := by positivity
  rcases lt_or_ge ((2 : ℤ) ^ u.length
      * (Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℤ)) (D (rep u k ++ rep v l))
    with h | h
  · exact h
  · exfalso
    have p1 := mul_le_mul_of_nonneg_left h h3m.le
    have p2 := mul_lt_mul_of_pos_right hUV (mul_pos h2m hgpos)
    linarith

/-! ### Main's C003 (`PROPORTIONAL_UNIFORM.md`): the fixed-pair bounds (5) and the uniform
effective bound (6), proved algebraically from the commutator identities -/

theorem G_pos (Q P : ℤ) (hQ : 0 < Q) (hP : 0 < P) : ∀ k, 1 ≤ k → 0 < G Q P k
  | 0, h => absurd h (by norm_num)
  | k + 1, _ => by
    simp only [G]
    have hG : 0 ≤ G Q P k := by
      rcases Nat.eq_zero_or_pos k with rfl | hk
      · simp [G]
      · exact (G_pos Q P hQ hP k hk).le
    exact add_pos_of_nonneg_of_pos (mul_nonneg hQ.le hG) (pow_pos hP k)

/-- The intermediate step of C002's (5): `gcd(C, D) ∣ K · G_v(ℓ)`. -/
theorem gcd_dvd_K_mul_Gv (u v : List ℕ) (k l : ℕ) (hv : ∀ a ∈ v, 1 ≤ a) (hv0 : v ≠ [])
    (hl : 1 ≤ l) :
    ((Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℕ) : ℤ)
      ∣ (D u * C v - D v * C u) * G (2 ^ v.sum) (3 ^ v.length) l := by
  have hgC : ((Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℕ) : ℤ) ∣
      C (rep u k ++ rep v l) := Int.gcd_dvd_left _ _
  have hgD : ((Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℕ) : ℤ) ∣
      D (rep u k ++ rep v l) := Int.gcd_dvd_right _ _
  set g : ℕ := Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) with hg
  have hsum : 1 ≤ (rep u k ++ rep v l).sum := by
    rw [List.sum_append, rep_sum, rep_sum]
    have := Nat.mul_le_mul hl (one_le_sum_of_ne_nil hv0 hv)
    omega
  have hlen : 1 ≤ (rep u k ++ rep v l).length := by
    rw [List.length_append, rep_length, rep_length]
    have := Nat.mul_le_mul hl (List.length_pos_of_ne_nil hv0)
    omega
  have h6 := gcd_coprime_six' _ hsum hlen
  have hcopQ : IsCoprime (g : ℤ) (((2 : ℤ) ^ u.sum) ^ k) := by
    have := Nat.isCoprime_iff_coprime.mpr
      (Nat.Coprime.pow_right k (Nat.Coprime.pow_right u.sum
        (h6.coprime_dvd_right (by norm_num : 2 ∣ 6))))
    exact_mod_cast this
  have h1 : (g : ℤ) ∣ (2 ^ u.sum) ^ k
      * (G (2 ^ v.sum) (3 ^ v.length) l * (D u * C v - D v * C u)) := by
    rw [← mul_assoc, ← commutator_two_u]
    exact dvd_sub (dvd_mul_of_dvd_right hgC _) (dvd_mul_of_dvd_right hgD _)
  rw [mul_comm]
  exact hcopQ.dvd_of_dvd_mul_left h1

/-- The other intermediate step of C002's (5): `gcd(C, D) ∣ K · G_u(k)`. -/
theorem gcd_dvd_K_mul_Gu (u v : List ℕ) (k l : ℕ) (hv : ∀ a ∈ v, 1 ≤ a) (hv0 : v ≠ [])
    (hl : 1 ≤ l) :
    ((Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℕ) : ℤ)
      ∣ (D u * C v - D v * C u) * G (2 ^ u.sum) (3 ^ u.length) k := by
  have hgC : ((Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℕ) : ℤ) ∣
      C (rep u k ++ rep v l) := Int.gcd_dvd_left _ _
  have hgD : ((Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℕ) : ℤ) ∣
      D (rep u k ++ rep v l) := Int.gcd_dvd_right _ _
  set g : ℕ := Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) with hg
  have hsum : 1 ≤ (rep u k ++ rep v l).sum := by
    rw [List.sum_append, rep_sum, rep_sum]
    have := Nat.mul_le_mul hl (one_le_sum_of_ne_nil hv0 hv)
    omega
  have hlen : 1 ≤ (rep u k ++ rep v l).length := by
    rw [List.length_append, rep_length, rep_length]
    have := Nat.mul_le_mul hl (List.length_pos_of_ne_nil hv0)
    omega
  have h6 := gcd_coprime_six' _ hsum hlen
  have hcopR : IsCoprime (g : ℤ) (((3 : ℤ) ^ v.length) ^ l) := by
    have := Nat.isCoprime_iff_coprime.mpr
      (Nat.Coprime.pow_right l (Nat.Coprime.pow_right v.length
        (h6.coprime_dvd_right (by norm_num : 3 ∣ 6))))
    exact_mod_cast this
  have h2 : (g : ℤ) ∣ (3 ^ v.length) ^ l
      * (G (2 ^ u.sum) (3 ^ u.length) k * (D u * C v - D v * C u)) := by
    have := dvd_sub (dvd_mul_of_dvd_right hgC (D v)) (dvd_mul_of_dvd_right hgD (C v))
    rw [commutator_two_v, dvd_neg, mul_assoc] at this
    exact this
  rw [mul_comm]
  exact hcopR.dvd_of_dvd_mul_left h2

/-- Positivity of `D(u^k v^ℓ)` for contracting blocks. -/
theorem D_two_pos (u v : List ℕ) (k l : ℕ) (hk : 1 ≤ k) (hl : 1 ≤ l) (hDu : 0 < D u)
    (hDv : 0 < D v) : 0 < D (rep u k ++ rep v l) := by
  have hPQ : (3 : ℤ) ^ u.length < 2 ^ u.sum := by simp only [D] at hDu; linarith
  have hRS : (3 : ℤ) ^ v.length < 2 ^ v.sum := by simp only [D] at hDv; linarith
  have hPQk : ((3 : ℤ) ^ u.length) ^ k < ((2 : ℤ) ^ u.sum) ^ k :=
    pow_lt_pow_left₀ hPQ (by positivity) (by omega)
  have hRSl : ((3 : ℤ) ^ v.length) ^ l < ((2 : ℤ) ^ v.sum) ^ l :=
    pow_lt_pow_left₀ hRS (by positivity) (by omega)
  rw [D_two]
  have := mul_lt_mul'' hRSl hPQk (by positivity) (by positivity)
  linarith

/-- **C003's (5), first form.** For contracting blocks with `K ≠ 0`:
`Q^k D_v · gcd(C, D) < |K| · D`, i.e. `den(u^k v^ℓ) > Q^k D_v/|K|`. -/
theorem fixed_pair_bound_u (u v : List ℕ) (k l : ℕ) (hv : ∀ a ∈ v, 1 ≤ a) (hv0 : v ≠ [])
    (hk : 1 ≤ k) (hl : 1 ≤ l) (hDu : 0 < D u) (hDv : 0 < D v)
    (hK : D u * C v - D v * C u ≠ 0) :
    ((2 : ℤ) ^ u.sum) ^ k * D v
        * (Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℤ)
      < |D u * C v - D v * C u| * D (rep u k ++ rep v l) := by
  have hGv : 0 < G (2 ^ v.sum) (3 ^ v.length) l := G_pos _ _ (by positivity) (by positivity) l hl
  have hdvd := gcd_dvd_K_mul_Gv u v k l hv hv0 hl
  have hg_le : ((Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℕ) : ℤ)
      ≤ |D u * C v - D v * C u| * G (2 ^ v.sum) (3 ^ v.length) l := by
    have h1 : ((Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℕ) : ℤ)
        ∣ |D u * C v - D v * C u| * G (2 ^ v.sum) (3 ^ v.length) l := by
      rw [← abs_of_pos hGv, ← abs_mul]
      exact (dvd_abs _ _).mpr hdvd
    exact Int.le_of_dvd (mul_pos (abs_pos.mpr hK) hGv) h1
  have hPQ : (3 : ℤ) ^ u.length < 2 ^ u.sum := by simp only [D] at hDu; linarith
  have hPQk : ((3 : ℤ) ^ u.length) ^ k < ((2 : ℤ) ^ u.sum) ^ k :=
    pow_lt_pow_left₀ hPQ (by positivity) (by omega)
  have hDvG : D v * G (2 ^ v.sum) (3 ^ v.length) l
      = ((2 : ℤ) ^ v.sum) ^ l - ((3 : ℤ) ^ v.length) ^ l := by
    unfold D; exact G_mul _ _ _
  have hR : (0 : ℤ) < ((3 : ℤ) ^ v.length) ^ l := by positivity
  calc ((2 : ℤ) ^ u.sum) ^ k * D v
          * ((Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℕ) : ℤ)
      ≤ ((2 : ℤ) ^ u.sum) ^ k * D v
          * (|D u * C v - D v * C u| * G (2 ^ v.sum) (3 ^ v.length) l) :=
        mul_le_mul_of_nonneg_left hg_le (mul_pos (by positivity) hDv).le
    _ = |D u * C v - D v * C u|
          * (((2 : ℤ) ^ u.sum) ^ k * (D v * G (2 ^ v.sum) (3 ^ v.length) l)) := by ring
    _ = |D u * C v - D v * C u|
          * (((2 : ℤ) ^ u.sum) ^ k * (((2 : ℤ) ^ v.sum) ^ l - ((3 : ℤ) ^ v.length) ^ l)) := by
        rw [hDvG]
    _ < |D u * C v - D v * C u|
          * (((2 : ℤ) ^ v.sum) ^ l * ((2 : ℤ) ^ u.sum) ^ k
            - ((3 : ℤ) ^ v.length) ^ l * ((3 : ℤ) ^ u.length) ^ k) := by
        apply mul_lt_mul_of_pos_left _ (abs_pos.mpr hK)
        nlinarith [mul_lt_mul_of_pos_left hPQk hR]
    _ = |D u * C v - D v * C u| * D (rep u k ++ rep v l) := by rw [D_two]

/-- **C003's (5), second form.** `S^ℓ D_u · gcd(C, D) < |K| · D`, i.e.
`den(u^k v^ℓ) > S^ℓ D_u/|K|`. -/
theorem fixed_pair_bound_v (u v : List ℕ) (k l : ℕ) (hv : ∀ a ∈ v, 1 ≤ a) (hv0 : v ≠ [])
    (hk : 1 ≤ k) (hl : 1 ≤ l) (hDu : 0 < D u) (hDv : 0 < D v)
    (hK : D u * C v - D v * C u ≠ 0) :
    ((2 : ℤ) ^ v.sum) ^ l * D u
        * (Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℤ)
      < |D u * C v - D v * C u| * D (rep u k ++ rep v l) := by
  have hGu : 0 < G (2 ^ u.sum) (3 ^ u.length) k := G_pos _ _ (by positivity) (by positivity) k hk
  have hdvd := gcd_dvd_K_mul_Gu u v k l hv hv0 hl
  have hg_le : ((Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℕ) : ℤ)
      ≤ |D u * C v - D v * C u| * G (2 ^ u.sum) (3 ^ u.length) k := by
    have h1 : ((Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℕ) : ℤ)
        ∣ |D u * C v - D v * C u| * G (2 ^ u.sum) (3 ^ u.length) k := by
      rw [← abs_of_pos hGu, ← abs_mul]
      exact (dvd_abs _ _).mpr hdvd
    exact Int.le_of_dvd (mul_pos (abs_pos.mpr hK) hGu) h1
  have hRS : (3 : ℤ) ^ v.length < 2 ^ v.sum := by simp only [D] at hDv; linarith
  have hRSl : ((3 : ℤ) ^ v.length) ^ l < ((2 : ℤ) ^ v.sum) ^ l :=
    pow_lt_pow_left₀ hRS (by positivity) (by omega)
  have hDuG : D u * G (2 ^ u.sum) (3 ^ u.length) k
      = ((2 : ℤ) ^ u.sum) ^ k - ((3 : ℤ) ^ u.length) ^ k := by
    unfold D; exact G_mul _ _ _
  have hP : (0 : ℤ) < ((3 : ℤ) ^ u.length) ^ k := by positivity
  calc ((2 : ℤ) ^ v.sum) ^ l * D u
          * ((Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℕ) : ℤ)
      ≤ ((2 : ℤ) ^ v.sum) ^ l * D u
          * (|D u * C v - D v * C u| * G (2 ^ u.sum) (3 ^ u.length) k) :=
        mul_le_mul_of_nonneg_left hg_le (mul_pos (by positivity) hDu).le
    _ = |D u * C v - D v * C u|
          * (((2 : ℤ) ^ v.sum) ^ l * (D u * G (2 ^ u.sum) (3 ^ u.length) k)) := by ring
    _ = |D u * C v - D v * C u|
          * (((2 : ℤ) ^ v.sum) ^ l * (((2 : ℤ) ^ u.sum) ^ k - ((3 : ℤ) ^ u.length) ^ k)) := by
        rw [hDuG]
    _ < |D u * C v - D v * C u|
          * (((2 : ℤ) ^ v.sum) ^ l * ((2 : ℤ) ^ u.sum) ^ k
            - ((3 : ℤ) ^ v.length) ^ l * ((3 : ℤ) ^ u.length) ^ k) := by
        apply mul_lt_mul_of_pos_left _ (abs_pos.mpr hK)
        nlinarith [mul_lt_mul_of_pos_right hRSl hP]
    _ = |D u * C v - D v * C u| * D (rep u k ++ rep v l) := by rw [D_two]

/-! #### The intercept and fixed-point bounds (7)–(9) -/

/-- C003's (7)+(8): for a contracting positive word, `2^m C_z < D_z (3^m + 1) 3^m`
(the fixed point is below `F(m) = (3^m + 1) 3^m / 2^m`). -/
theorem two_pow_mul_C_lt (z : List ℕ) (hpos : ∀ a ∈ z, 1 ≤ a) (hD : 0 < D z) :
    (2 : ℤ) ^ z.length * C z < D z * ((3 ^ z.length + 1) * 3 ^ z.length) := by
  have h7 := two_pow_mul_C_le z hpos
  have hQ : (2 : ℤ) ^ z.sum = D z + 3 ^ z.length := by simp [D]
  have h2m : (0 : ℤ) < 2 ^ z.length := by positivity
  have h3m : (0 : ℤ) < 3 ^ z.length := by positivity
  have h2A : (0 : ℤ) < 2 ^ z.sum := by positivity
  have hD1 : (1 : ℤ) ≤ D z := hD
  have hQ3 : (2 : ℤ) ^ z.sum * 3 ^ z.length = D z * 3 ^ z.length + 3 ^ z.length * 3 ^ z.length := by
    rw [hQ]; ring
  nlinarith [h7, hQ3, mul_pos h2A h2m, mul_le_mul_of_nonneg_left hD1 (mul_pos h3m h3m).le]

/-- `F(m) = (3^m + 1) 3^m / 2^m` is increasing, in cleared form. -/
theorem F_mono {m M : ℕ} (h : m ≤ M) :
    ((3 : ℤ) ^ m + 1) * 3 ^ m * 2 ^ M ≤ (3 ^ M + 1) * 3 ^ M * 2 ^ m := by
  obtain ⟨d, rfl⟩ := Nat.exists_eq_add_of_le h
  simp only [pow_add]
  have h3 : (3 : ℤ) ^ m + 1 ≤ 3 ^ m * 3 ^ d + 1 := by
    have h1 : (1 : ℤ) ≤ 3 ^ d := one_le_pow₀ (by norm_num)
    nlinarith [pow_pos (by norm_num : (0 : ℤ) < 3) m]
  have h23 : (2 : ℤ) ^ d ≤ 3 ^ d := pow_le_pow_left₀ (by norm_num) (by norm_num) d
  have hpos : (0 : ℤ) ≤ 3 ^ m * 2 ^ m := by positivity
  calc ((3 : ℤ) ^ m + 1) * 3 ^ m * (2 ^ m * 2 ^ d)
      = ((3 ^ m + 1) * 2 ^ d) * (3 ^ m * 2 ^ m) := by ring
    _ ≤ ((3 ^ m * 3 ^ d + 1) * 3 ^ d) * (3 ^ m * 2 ^ m) := by
        apply mul_le_mul_of_nonneg_right _ hpos
        exact mul_le_mul h3 h23 (by positivity) (by positivity)
    _ = (3 ^ m * 3 ^ d + 1) * (3 ^ m * 3 ^ d) * 2 ^ m := by ring

/-- C003's (9), one block: for `m_z ≤ M`, `2^M C_z < D_z (3^M + 1) 3^M`. -/
theorem two_pow_mul_C_lt_M (z : List ℕ) (hpos : ∀ a ∈ z, 1 ≤ a) (hD : 0 < D z) {M : ℕ}
    (hM : z.length ≤ M) :
    (2 : ℤ) ^ M * C z < D z * ((3 ^ M + 1) * 3 ^ M) := by
  have h1 := two_pow_mul_C_lt z hpos hD
  have h2 := F_mono hM
  have h2m : (0 : ℤ) < 2 ^ z.length := by positivity
  have h3 : (2 : ℤ) ^ z.length * (2 ^ M * C z) < 2 ^ z.length * (D z * ((3 ^ M + 1) * 3 ^ M)) := by
    calc (2 : ℤ) ^ z.length * (2 ^ M * C z) = 2 ^ M * (2 ^ z.length * C z) := by ring
      _ < 2 ^ M * (D z * ((3 ^ z.length + 1) * 3 ^ z.length)) :=
          mul_lt_mul_of_pos_left h1 (by positivity)
      _ = D z * ((3 ^ z.length + 1) * 3 ^ z.length * 2 ^ M) := by ring
      _ ≤ D z * ((3 ^ M + 1) * 3 ^ M * 2 ^ z.length) := mul_le_mul_of_nonneg_left h2 hD.le
      _ = 2 ^ z.length * (D z * ((3 ^ M + 1) * 3 ^ M)) := by ring
  exact lt_of_mul_lt_mul_left h3 h2m.le

/-- C003's (9), the determinant: `2^M |K| < D_u D_v (3^M + 1) 3^M` for contracting blocks of
lengths at most `M`. -/
theorem K_bound (u v : List ℕ) (hu : ∀ a ∈ u, 1 ≤ a) (hv : ∀ a ∈ v, 1 ≤ a) (hDu : 0 < D u)
    (hDv : 0 < D v) {M : ℕ} (hMu : u.length ≤ M) (hMv : v.length ≤ M) :
    |D u * C v - D v * C u| * 2 ^ M < D u * D v * ((3 ^ M + 1) * 3 ^ M) := by
  have hu0 : u ≠ [] := by
    rintro rfl
    simp [D] at hDu
  have hv0 : v ≠ [] := by
    rintro rfl
    simp [D] at hDv
  have hCu := two_pow_mul_C_lt_M u hu hDu hMu
  have hCv := two_pow_mul_C_lt_M v hv hDv hMv
  have hCu0 := C_pos hu0
  have hCv0 := C_pos hv0
  have h2M : (0 : ℤ) < 2 ^ M := by positivity
  rw [← abs_of_pos h2M, ← abs_mul, abs_lt]
  constructor
  · nlinarith [mul_lt_mul_of_pos_left hCu hDv, mul_pos (mul_pos hDu h2M) hCv0]
  · nlinarith [mul_lt_mul_of_pos_left hCv hDu, mul_pos (mul_pos hDv h2M) hCu0]

/-- **C003's (6), `u`-block form.** Both blocks contracting, `K ≠ 0`, `Q = 2^Σu ≥ S = 2^Σv`,
`k ≥ 3`, `ℓ ≥ 1`, `M ≥` both lengths with `3^M < Q`: then
`2^M Q^{k−3} · gcd(C, D) < D`, i.e. `den(u^k v^ℓ) > 2^M Q^{k−3}`. -/
theorem uniform_bound_u (u v : List ℕ) (k l : ℕ) (hu : ∀ a ∈ u, 1 ≤ a) (hv : ∀ a ∈ v, 1 ≤ a)
    (hv0 : v ≠ []) (hk : 3 ≤ k) (hl : 1 ≤ l) (hDu : 0 < D u) (hDv : 0 < D v)
    (hK : D u * C v - D v * C u ≠ 0) {M : ℕ} (hMu : u.length ≤ M) (hMv : v.length ≤ M)
    (h3M : (3 : ℤ) ^ M < 2 ^ u.sum) :
    (2 : ℤ) ^ M * ((2 : ℤ) ^ u.sum) ^ (k - 3)
        * (Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℤ)
      < D (rep u k ++ rep v l) := by
  have h5 := fixed_pair_bound_u u v k l hv hv0 (by omega) hl hDu hDv hK
  have hKb := K_bound u v hu hv hDu hDv hMu hMv
  have hDw := D_two_pos u v k l (by omega) hl hDu hDv
  have h2M : (0 : ℤ) < 2 ^ M := by positivity
  have hQ : (0 : ℤ) < 2 ^ u.sum := by positivity
  have hQ3 : (3 : ℤ) ^ M + 1 ≤ 2 ^ u.sum := by linarith
  have h3Mpos : (0 : ℤ) < 3 ^ M := by positivity
  have hF : ((3 : ℤ) ^ M + 1) * 3 ^ M < 2 ^ u.sum * 2 ^ u.sum := by
    nlinarith [mul_le_mul_of_nonneg_right hQ3 h3Mpos.le, mul_lt_mul_of_pos_left h3M hQ]
  have hDuQ : D u < 2 ^ u.sum := by
    simp only [D]
    linarith [pow_pos (by norm_num : (0 : ℤ) < 3) u.length]
  set g : ℤ := (Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℤ) with hg
  set W : ℤ := D (rep u k ++ rep v l) with hW
  have step1 : 2 ^ M * (((2 : ℤ) ^ u.sum) ^ k * D v * g) < 2 ^ M * (|D u * C v - D v * C u| * W) :=
    mul_lt_mul_of_pos_left h5 h2M
  have step2 : |D u * C v - D v * C u| * 2 ^ M * W
      < D u * D v * ((3 ^ M + 1) * 3 ^ M) * W := mul_lt_mul_of_pos_right hKb hDw
  have step3 : D u * D v * ((3 ^ M + 1) * 3 ^ M) * W ≤ D u * D v * (2 ^ u.sum * 2 ^ u.sum) * W := by
    apply mul_le_mul_of_nonneg_right _ hDw.le
    exact mul_le_mul_of_nonneg_left hF.le (mul_pos hDu hDv).le
  have step4 : D v * (2 ^ M * ((2 : ℤ) ^ u.sum) ^ k * g)
      < D v * (D u * (2 ^ u.sum * 2 ^ u.sum) * W) := by nlinarith [step1, step2, step3]
  have step5 : 2 ^ M * ((2 : ℤ) ^ u.sum) ^ k * g < D u * (2 ^ u.sum * 2 ^ u.sum) * W :=
    lt_of_mul_lt_mul_left step4 hDv.le
  have step6 : D u * (2 ^ u.sum * 2 ^ u.sum) * W < 2 ^ u.sum * (2 ^ u.sum * 2 ^ u.sum) * W := by
    apply mul_lt_mul_of_pos_right _ hDw
    exact mul_lt_mul_of_pos_right hDuQ (by positivity)
  have hk3 : ((2 : ℤ) ^ u.sum) ^ k = ((2 : ℤ) ^ u.sum) ^ (k - 3) * ((2 : ℤ) ^ u.sum) ^ 3 := by
    rw [← pow_add, Nat.sub_add_cancel hk]
  have step7 : ((2 : ℤ) ^ u.sum) ^ 3 * (2 ^ M * ((2 : ℤ) ^ u.sum) ^ (k - 3) * g)
      < ((2 : ℤ) ^ u.sum) ^ 3 * W := by
    calc ((2 : ℤ) ^ u.sum) ^ 3 * (2 ^ M * ((2 : ℤ) ^ u.sum) ^ (k - 3) * g)
        = 2 ^ M * (((2 : ℤ) ^ u.sum) ^ (k - 3) * ((2 : ℤ) ^ u.sum) ^ 3) * g := by ring
      _ = 2 ^ M * ((2 : ℤ) ^ u.sum) ^ k * g := by rw [← hk3]
      _ < 2 ^ u.sum * (2 ^ u.sum * 2 ^ u.sum) * W := lt_trans step5 step6
      _ = ((2 : ℤ) ^ u.sum) ^ 3 * W := by ring
  exact lt_of_mul_lt_mul_left step7 (by positivity)

/-- **C003's (6), `v`-block form.** As above with the roles of the blocks exchanged:
`S ≥ Q`, `ℓ ≥ 3`, `k ≥ 1`, `3^M < S`; then `2^M S^{ℓ−3} · gcd(C, D) < D`. -/
theorem uniform_bound_v (u v : List ℕ) (k l : ℕ) (hu : ∀ a ∈ u, 1 ≤ a) (hv : ∀ a ∈ v, 1 ≤ a)
    (hv0 : v ≠ []) (hk : 1 ≤ k) (hl : 3 ≤ l) (hDu : 0 < D u) (hDv : 0 < D v)
    (hK : D u * C v - D v * C u ≠ 0) {M : ℕ} (hMu : u.length ≤ M) (hMv : v.length ≤ M)
    (h3M : (3 : ℤ) ^ M < 2 ^ v.sum) :
    (2 : ℤ) ^ M * ((2 : ℤ) ^ v.sum) ^ (l - 3)
        * (Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℤ)
      < D (rep u k ++ rep v l) := by
  have h5 := fixed_pair_bound_v u v k l hv hv0 hk (by omega) hDu hDv hK
  have hKb := K_bound u v hu hv hDu hDv hMu hMv
  have hDw := D_two_pos u v k l hk (by omega) hDu hDv
  have h2M : (0 : ℤ) < 2 ^ M := by positivity
  have hS : (0 : ℤ) < 2 ^ v.sum := by positivity
  have hS3 : (3 : ℤ) ^ M + 1 ≤ 2 ^ v.sum := by linarith
  have h3Mpos : (0 : ℤ) < 3 ^ M := by positivity
  have hF : ((3 : ℤ) ^ M + 1) * 3 ^ M < 2 ^ v.sum * 2 ^ v.sum := by
    nlinarith [mul_le_mul_of_nonneg_right hS3 h3Mpos.le, mul_lt_mul_of_pos_left h3M hS]
  have hDvS : D v < 2 ^ v.sum := by
    simp only [D]
    linarith [pow_pos (by norm_num : (0 : ℤ) < 3) v.length]
  set g : ℤ := (Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℤ) with hg
  set W : ℤ := D (rep u k ++ rep v l) with hW
  have step1 : 2 ^ M * (((2 : ℤ) ^ v.sum) ^ l * D u * g) < 2 ^ M * (|D u * C v - D v * C u| * W) :=
    mul_lt_mul_of_pos_left h5 h2M
  have step2 : |D u * C v - D v * C u| * 2 ^ M * W
      < D u * D v * ((3 ^ M + 1) * 3 ^ M) * W := mul_lt_mul_of_pos_right hKb hDw
  have step3 : D u * D v * ((3 ^ M + 1) * 3 ^ M) * W ≤ D u * D v * (2 ^ v.sum * 2 ^ v.sum) * W := by
    apply mul_le_mul_of_nonneg_right _ hDw.le
    exact mul_le_mul_of_nonneg_left hF.le (mul_pos hDu hDv).le
  have step4 : D u * (2 ^ M * ((2 : ℤ) ^ v.sum) ^ l * g)
      < D u * (D v * (2 ^ v.sum * 2 ^ v.sum) * W) := by nlinarith [step1, step2, step3]
  have step5 : 2 ^ M * ((2 : ℤ) ^ v.sum) ^ l * g < D v * (2 ^ v.sum * 2 ^ v.sum) * W :=
    lt_of_mul_lt_mul_left step4 hDu.le
  have step6 : D v * (2 ^ v.sum * 2 ^ v.sum) * W < 2 ^ v.sum * (2 ^ v.sum * 2 ^ v.sum) * W := by
    apply mul_lt_mul_of_pos_right _ hDw
    exact mul_lt_mul_of_pos_right hDvS (by positivity)
  have hl3 : ((2 : ℤ) ^ v.sum) ^ l = ((2 : ℤ) ^ v.sum) ^ (l - 3) * ((2 : ℤ) ^ v.sum) ^ 3 := by
    rw [← pow_add, Nat.sub_add_cancel hl]
  have step7 : ((2 : ℤ) ^ v.sum) ^ 3 * (2 ^ M * ((2 : ℤ) ^ v.sum) ^ (l - 3) * g)
      < ((2 : ℤ) ^ v.sum) ^ 3 * W := by
    calc ((2 : ℤ) ^ v.sum) ^ 3 * (2 ^ M * ((2 : ℤ) ^ v.sum) ^ (l - 3) * g)
        = 2 ^ M * (((2 : ℤ) ^ v.sum) ^ (l - 3) * ((2 : ℤ) ^ v.sum) ^ 3) * g := by ring
      _ = 2 ^ M * ((2 : ℤ) ^ v.sum) ^ l * g := by rw [← hl3]
      _ < 2 ^ v.sum * (2 ^ v.sum * 2 ^ v.sum) * W := lt_trans step5 step6
      _ = ((2 : ℤ) ^ v.sum) ^ 3 * W := by ring
  exact lt_of_mul_lt_mul_left step7 (by positivity)

/-- **C003's (6) with `M = max(m_u, m_v)` and `Q_* = Q`.** If the `u`-block has the larger
binary power and is repeated `k ≥ 3` times, `den(u^k v^ℓ) > 2^M Q^{k−3} ≥ 2^M`. -/
theorem uniform_bound_max_u (u v : List ℕ) (k l : ℕ) (hu : ∀ a ∈ u, 1 ≤ a)
    (hv : ∀ a ∈ v, 1 ≤ a) (hv0 : v ≠ []) (hk : 3 ≤ k) (hl : 1 ≤ l) (hDu : 0 < D u)
    (hDv : 0 < D v) (hK : D u * C v - D v * C u ≠ 0) (hQS : (2 : ℤ) ^ v.sum ≤ 2 ^ u.sum) :
    (2 : ℤ) ^ max u.length v.length * ((2 : ℤ) ^ u.sum) ^ (k - 3)
        * (Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℤ)
      < D (rep u k ++ rep v l) := by
  apply uniform_bound_u u v k l hu hv hv0 hk hl hDu hDv hK (le_max_left _ _) (le_max_right _ _)
  have hPQ : (3 : ℤ) ^ u.length < 2 ^ u.sum := by simp only [D] at hDu; linarith
  have hRS : (3 : ℤ) ^ v.length < 2 ^ v.sum := by simp only [D] at hDv; linarith
  rcases le_total v.length u.length with h | h
  · rw [max_eq_left h]; exact hPQ
  · rw [max_eq_right h]; exact lt_of_lt_of_le hRS hQS

/-- The worked example `(1,2,2)^3 (2)` of C003: `C = 213341`, `D = 72023`, coprime. -/
example : C (rep [1, 2, 2] 3 ++ rep [2] 1) = 213341 ∧ D (rep [1, 2, 2] 3 ++ rep [2] 1) = 72023 ∧
    Int.gcd (C (rep [1, 2, 2] 3 ++ rep [2] 1)) (D (rep [1, 2, 2] 3 ++ rep [2] 1)) = 1 := by
  norm_num [rep, C, D]

/-! ### One-letter cuts (main's C004 `ROTATION_LATTICE.md` §2, (6)–(7)) -/

/-- C004's (6): cut the first letter `a` off `w = a :: v`, so `u = (a)`, `C_u = 1`,
`D_u = 2^a − 3` and `K = D_u C_v − D_v C_u`; then `2^a K = (2^a − 3) C_w − D_w`. This is
the `k = 1` case of `commutator`. -/
theorem cut_identity (a : ℕ) (v : List ℕ) :
    (2 : ℤ) ^ a * ((2 ^ a - 3) * C v - D v) = (2 ^ a - 3) * C (a :: v) - D (a :: v) := by
  simp only [C, D, List.sum_cons, List.length_cons, pow_succ, pow_add]
  ring

/-- `gcd(a, b − a) = gcd(a, b)` for integers. -/
theorem gcd_sub_self_right (a b : ℤ) : Int.gcd a (b - a) = Int.gcd a b := by
  apply Nat.dvd_antisymm
  · refine Int.dvd_gcd (Int.gcd_dvd_left _ _) ?_
    have h := dvd_add (Int.gcd_dvd_right a (b - a)) (Int.gcd_dvd_left a (b - a))
    rwa [sub_add_cancel] at h
  · exact Int.dvd_gcd (Int.gcd_dvd_left _ _)
      (dvd_sub (Int.gcd_dvd_right _ _) (Int.gcd_dvd_left _ _))

/-- C004's (7): for `w = a :: v` with `a ≥ 1`, `g = gcd(C_w, D_w)` and `d₀ = D_w/g`,
`gcd(D_w, K) = g · gcd(d₀, 2^a − 3)`, where `K = (2^a − 3) C_v − D_v` is the one-letter cut
commutator. -/
theorem cut_gcd (a : ℕ) (v : List ℕ) (ha : 1 ≤ a) :
    Int.gcd (D (a :: v)) ((2 ^ a - 3) * C v - D v)
      = Int.gcd (C (a :: v)) (D (a :: v))
        * Int.gcd (D (a :: v) / (Int.gcd (C (a :: v)) (D (a :: v)) : ℤ)) (2 ^ a - 3) := by
  have hsum : 1 ≤ (a :: v).sum := by
    simp only [List.sum_cons]; omega
  have hDodd : ¬ (2 : ℤ) ∣ D (a :: v) := D_odd hsum
  have hD0 : D (a :: v) ≠ 0 := fun h => hDodd (by rw [h]; exact dvd_zero 2)
  set g : ℕ := Int.gcd (C (a :: v)) (D (a :: v)) with hg
  have hgpos : 0 < g := Int.gcd_pos_of_ne_zero_right _ hD0
  have hgC : (g : ℤ) ∣ C (a :: v) := Int.gcd_dvd_left _ _
  have hgD : (g : ℤ) ∣ D (a :: v) := Int.gcd_dvd_right _ _
  have hcop : Int.gcd (C (a :: v) / g) (D (a :: v) / g) = 1 := Int.gcd_div_gcd_div_gcd hgpos
  set n : ℤ := C (a :: v) / g with hn
  set d₀ : ℤ := D (a :: v) / g with hd₀
  have hCw : C (a :: v) = g * n := (Int.mul_ediv_cancel' hgC).symm
  have hDw : D (a :: v) = g * d₀ := (Int.mul_ediv_cancel' hgD).symm
  -- Step 1: `2^a` is a unit modulo the odd `D_w`.
  have step1 : Int.gcd (D (a :: v)) ((2 ^ a - 3) * C v - D v)
      = Int.gcd (D (a :: v)) (2 ^ a * ((2 ^ a - 3) * C v - D v)) := by
    apply Nat.dvd_antisymm
    · exact Int.dvd_gcd (Int.gcd_dvd_left _ _)
        (dvd_mul_of_dvd_right (Int.gcd_dvd_right _ _) _)
    · have hD : ((Int.gcd (D (a :: v)) (2 ^ a * ((2 ^ a - 3) * C v - D v)) : ℕ) : ℤ)
          ∣ D (a :: v) := Int.gcd_dvd_left _ _
      have hK : ((Int.gcd (D (a :: v)) (2 ^ a * ((2 ^ a - 3) * C v - D v)) : ℕ) : ℤ)
          ∣ 2 ^ a * ((2 ^ a - 3) * C v - D v) := Int.gcd_dvd_right _ _
      have h2 : ¬ 2 ∣ Int.gcd (D (a :: v)) (2 ^ a * ((2 ^ a - 3) * C v - D v)) := fun h2 =>
        hDodd ((by exact_mod_cast h2 : (2 : ℤ) ∣
          ((Int.gcd (D (a :: v)) (2 ^ a * ((2 ^ a - 3) * C v - D v)) : ℕ) : ℤ)).trans hD)
      have hcop2 : IsCoprime
          ((Int.gcd (D (a :: v)) (2 ^ a * ((2 ^ a - 3) * C v - D v)) : ℕ) : ℤ) ((2 : ℤ) ^ a) := by
        have := Nat.isCoprime_iff_coprime.mpr (Nat.Coprime.pow_right a
          ((Nat.Prime.coprime_iff_not_dvd Nat.prime_two).mpr h2).symm)
        exact_mod_cast this
      exact Int.dvd_gcd hD (hcop2.dvd_of_dvd_mul_left hK)
  -- Step 2: the cut identity, then `gcd(D, X − D) = gcd(D, X)`.
  have step2 : Int.gcd (D (a :: v)) (2 ^ a * ((2 ^ a - 3) * C v - D v))
      = Int.gcd (D (a :: v)) ((2 ^ a - 3) * C (a :: v)) := by
    rw [cut_identity, gcd_sub_self_right]
  -- Step 3: factor out `g`.
  have step3 : Int.gcd (D (a :: v)) ((2 ^ a - 3) * C (a :: v))
      = g * Int.gcd d₀ ((2 ^ a - 3) * n) := by
    rw [hDw, hCw, show (2 ^ a - 3 : ℤ) * (g * n) = g * ((2 ^ a - 3) * n) by ring,
      Int.gcd_mul_left, Int.natAbs_natCast]
  -- Step 4: cancel `n`, which is coprime to `d₀`.
  have step4 : Int.gcd d₀ ((2 ^ a - 3) * n) = Int.gcd d₀ (2 ^ a - 3) := by
    apply Nat.dvd_antisymm
    · have hcopn : IsCoprime ((Int.gcd d₀ ((2 ^ a - 3) * n) : ℕ) : ℤ) n :=
        (Int.isCoprime_iff_gcd_eq_one.mpr hcop).symm.of_isCoprime_of_dvd_left
          (Int.gcd_dvd_left _ _)
      exact Int.dvd_gcd (Int.gcd_dvd_left _ _)
        (hcopn.dvd_of_dvd_mul_right (Int.gcd_dvd_right _ _))
    · exact Int.dvd_gcd (Int.gcd_dvd_left _ _)
        (dvd_mul_of_dvd_left (Int.gcd_dvd_right _ _) _)
  rw [step1, step2, step3, step4]

/-- The `d = 5` control `(1,2,2)`: `K = −14`, (6) reads `−28 = −28`, and both sides of (7)
are `1`. -/
example : (2 : ℤ) ^ 1 * ((2 ^ 1 - 3) * C [2, 2] - D [2, 2]) = -28 ∧
    (2 ^ 1 - 3 : ℤ) * C [1, 2, 2] - D [1, 2, 2] = -28 ∧
    Int.gcd (D [1, 2, 2]) ((2 ^ 1 - 3) * C [2, 2] - D [2, 2]) = 1 ∧
    Int.gcd (C [1, 2, 2]) (D [1, 2, 2]) = 1 := by
  norm_num [C, D]

/-! ### Mechanical words and their phases (C004 `ROTATION_LATTICE.md` §3, reverse direction) -/

/-- The word of successive differences `F(j+1) − F(j)`, `j < m`. -/
def diffWord (F : ℕ → ℕ) (m : ℕ) : List ℕ := (List.range m).map fun j => F (j + 1) - F j

/-- The phase-`l` mechanical word of total `A` and length `m`,
`a_j = ⌊((j+1)A + l)/m⌋ − ⌊(jA + l)/m⌋`; phase `0` is R71's mechanical word. -/
def mech (A m l : ℕ) : List ℕ := diffWord (fun j => (j * A + l) / m) m

theorem diffWord_zero (F : ℕ → ℕ) : diffWord F 0 = [] := rfl

theorem diffWord_succ (F : ℕ → ℕ) (m : ℕ) :
    diffWord F (m + 1) = (F 1 - F 0) :: diffWord (fun j => F (j + 1)) m := by
  simp [diffWord, List.range_succ_eq_map, List.map_map, Function.comp_def]

theorem length_diffWord (F : ℕ → ℕ) (m : ℕ) : (diffWord F m).length = m := by
  simp [diffWord]

theorem sum_map_range (f : ℕ → ℕ) :
    ∀ m, ((List.range m).map f).sum = ∑ j ∈ Finset.range m, f j
  | 0 => by simp
  | m + 1 => by
    rw [List.range_succ, List.map_append, List.sum_append, Finset.sum_range_succ,
      sum_map_range f m]
    simp

theorem sum_diffWord (F : ℕ → ℕ) (hF : Monotone F) (m : ℕ) :
    (diffWord F m).sum = F m - F 0 := by
  rw [diffWord, sum_map_range, Finset.sum_range_tsub hF]

/-- The closed form of the intercept: `2^{F 0} · C(diffWord F m) = ∑_{j<m} 3^{m−1−j} 2^{F j}`
(R71's sum, with `F j` the prefix sums). -/
theorem C_diffWord (F : ℕ → ℕ) (hF : Monotone F) :
    ∀ m, (2 : ℤ) ^ F 0 * C (diffWord F m)
      = ∑ j ∈ Finset.range m, (3 : ℤ) ^ (m - (j + 1)) * 2 ^ F j
  | 0 => by simp [diffWord_zero, C]
  | m + 1 => by
    have ih : (2 : ℤ) ^ F 1 * C (diffWord (fun j => F (j + 1)) m)
        = ∑ j ∈ Finset.range m, (3 : ℤ) ^ (m - (j + 1)) * 2 ^ F (j + 1) :=
      C_diffWord (fun j => F (j + 1)) (fun _ _ h => hF (Nat.add_le_add_right h 1)) m
    have h01 : F 0 ≤ F 1 := hF (Nat.zero_le 1)
    have hpow : (2 : ℤ) ^ F 0 * 2 ^ (F 1 - F 0) = 2 ^ F 1 := by
      rw [← pow_add, Nat.add_sub_of_le h01]
    rw [diffWord_succ, Finset.sum_range_succ']
    simp only [C, length_diffWord, Nat.add_sub_add_right, zero_add, Nat.add_sub_cancel]
    rw [← ih, ← hpow]
    ring

theorem mech_monotone (A m l : ℕ) : Monotone fun j : ℕ => (j * A + l) / m :=
  fun _ _ h => Nat.div_le_div_right (Nat.add_le_add_right (Nat.mul_le_mul_right A h) l)

theorem mech_length (A m l : ℕ) : (mech A m l).length = m := by
  simp [mech, diffWord]

theorem mech_sum {m : ℕ} (hm : 0 < m) (A l : ℕ) (hl : l < m) : (mech A m l).sum = A := by
  rw [mech, sum_diffWord _ (mech_monotone A m l)]
  simp only [zero_mul, zero_add]
  rw [show m * A + l = l + m * A by ring, Nat.add_mul_div_left _ _ hm, Nat.div_eq_of_lt hl]
  simp

/-- Every phase word has `D = 2^A − 3^m`. -/
theorem D_mech {m : ℕ} (hm : 0 < m) (A l : ℕ) (hl : l < m) : D (mech A m l) = 2 ^ A - 3 ^ m := by
  rw [D, mech_sum hm A l hl, mech_length]

/-- For `A ≥ m` the mechanical words are positive valuation words. -/
theorem mech_pos {m : ℕ} (hm : 0 < m) (A l : ℕ) (hAm : m ≤ A) : ∀ x ∈ mech A m l, 1 ≤ x := by
  intro x hx
  simp only [mech, diffWord, List.mem_map, List.mem_range] at hx
  obtain ⟨j, -, rfl⟩ := hx
  have h1 : (j * A + l + m) / m ≤ ((j + 1) * A + l) / m :=
    Nat.div_le_div_right (by nlinarith)
  rw [Nat.add_div_right _ hm] at h1
  omega

/-- The intercept of the phase-`l` word, `l < m`, as R71's sum. -/
theorem C_mech {m : ℕ} (A l : ℕ) (hl : l < m) :
    C (mech A m l) = ∑ j ∈ Finset.range m, (3 : ℤ) ^ (m - (j + 1)) * 2 ^ ((j * A + l) / m) := by
  have h := C_diffWord (fun j => (j * A + l) / m) (mech_monotone A m l) m
  simp only [zero_mul, zero_add, Nat.div_eq_of_lt hl, pow_zero, one_mul] at h
  exact h

theorem phase_floor_le (m A l j : ℕ) : j * A / m ≤ (j * A + l) / m :=
  Nat.div_le_div_right (Nat.le_add_right _ _)

theorem phase_floor_le_succ {m : ℕ} (hm : 0 < m) (A l j : ℕ) (hl : l < m) :
    (j * A + l) / m ≤ j * A / m + 1 := by
  rw [← Nat.add_div_right _ hm]
  exact Nat.div_le_div_right (by omega)

/-- `C_0 ≤ C_l`: each summand of phase `l` is at least the matching summand of phase `0`. -/
theorem C_mech_zero_le {m : ℕ} (hm : 0 < m) (A l : ℕ) (hl : l < m) :
    C (mech A m 0) ≤ C (mech A m l) := by
  rw [C_mech A 0 hm, C_mech A l hl]
  apply Finset.sum_le_sum
  intro j _
  simp only [add_zero]
  exact mul_le_mul_of_nonneg_left (pow_le_pow_right₀ (by norm_num) (phase_floor_le m A l j))
    (by positivity)

/-- `C_l < 2 C_0`: each summand of phase `l` is at most twice the matching summand of phase
`0`, and the `j = 0` summand `3^{m−1}` is the same in both. -/
theorem C_mech_lt_two {m : ℕ} (hm : 0 < m) (A l : ℕ) (hl : l < m) :
    C (mech A m l) < 2 * C (mech A m 0) := by
  rw [C_mech A 0 hm, C_mech A l hl, Finset.mul_sum]
  apply Finset.sum_lt_sum
  · intro j _
    have h := phase_floor_le_succ hm A l j hl
    simp only [add_zero]
    calc (3 : ℤ) ^ (m - (j + 1)) * 2 ^ ((j * A + l) / m)
        ≤ 3 ^ (m - (j + 1)) * 2 ^ (j * A / m + 1) :=
          mul_le_mul_of_nonneg_left (pow_le_pow_right₀ (by norm_num) h) (by positivity)
      _ = 2 * (3 ^ (m - (j + 1)) * 2 ^ (j * A / m)) := by ring
  · refine ⟨0, Finset.mem_range.mpr hm, ?_⟩
    simp only [zero_mul, zero_add, Nat.div_eq_of_lt hl, Nat.zero_div, pow_zero, mul_one]
    have : (0 : ℤ) < 3 ^ (m - 1) := by positivity
    linarith

/-! #### Rotations of a phase word are phase words -/

theorem step_add_mul {m : ℕ} (hm : 0 < m) (A r q : ℕ) :
    (r + m * q + A) / m - (r + m * q) / m = (r + A) / m - r / m := by
  rw [show r + m * q + A = r + A + m * q by ring, Nat.add_mul_div_left _ _ hm,
    Nat.add_mul_div_left _ _ hm, Nat.add_sub_add_right]

theorem step_mod {m : ℕ} (hm : 0 < m) (A N : ℕ) :
    (N + A) / m - N / m = (N % m + A) / m - N % m / m := by
  have h := step_add_mul hm A (N % m) (N / m)
  rwa [Nat.mod_add_div] at h

theorem step_congr {m : ℕ} (hm : 0 < m) (A : ℕ) {N₁ N₂ : ℕ} (h : N₁ % m = N₂ % m) :
    (N₁ + A) / m - N₁ / m = (N₂ + A) / m - N₂ / m := by
  rw [step_mod hm A N₁, step_mod hm A N₂, h]

/-- Rotating the phase-`l` word by `i` letters gives the phase `(l + iA) mod m`; in particular
every rotation of the mechanical word `mech A m 0` is the phase word of `iA mod m`. -/
theorem mech_rotate {m : ℕ} (hm : 0 < m) (A l i : ℕ) :
    (mech A m l).rotate i = mech A m ((l + i * A) % m) := by
  apply List.ext_getElem
  · simp [mech_length]
  · intro k hk₁ hk₂
    rw [List.getElem_rotate]
    simp only [mech, diffWord, List.getElem_map, List.getElem_range, List.length_map,
      List.length_range]
    have e1 : ((k + i) % m + 1) * A + l = (k + i) % m * A + l + A := by ring
    have e2 : (k + 1) * A + (l + i * A) % m = k * A + (l + i * A) % m + A := by ring
    rw [e1, e2]
    apply step_congr hm
    have h1 : (k + i) % m * A + l ≡ (k + i) * A + l [MOD m] :=
      ((Nat.mod_modEq (k + i) m).mul_right A).add_right l
    have h2 : k * A + (l + i * A) % m ≡ k * A + (l + i * A) [MOD m] :=
      (Nat.mod_modEq (l + i * A) m).add_left (k * A)
    have e3 : (k + i) * A + l = k * A + (l + i * A) := by ring
    have h2' : (k + i) * A + l ≡ k * A + (l + i * A) % m [MOD m] := by
      rw [e3]; exact h2.symm
    exact h1.trans h2'

/-- **C004 §3, reverse direction.** Every rotation of the mechanical word has its intercept in
`[C_0, 2 C_0)` and the common `D = 2^A − 3^m`; so, when `D > 0`, all states `C_i/D` of the
mechanical cycle lie in `[L, 2L)` with `L = C_0/D`: a mechanical cycle is narrow, `H < 2L`.
No coprimality of `A` and `m` is needed for the inequalities. -/
theorem narrow_mech {m : ℕ} (hm : 0 < m) (A i : ℕ) :
    C (mech A m 0) ≤ C ((mech A m 0).rotate i)
      ∧ C ((mech A m 0).rotate i) < 2 * C (mech A m 0)
      ∧ D ((mech A m 0).rotate i) = 2 ^ A - 3 ^ m := by
  rw [mech_rotate hm A 0 i]
  have hl : (0 + i * A) % m < m := Nat.mod_lt _ hm
  exact ⟨C_mech_zero_le hm A _ hl, C_mech_lt_two hm A _ hl, D_mech hm A _ hl⟩

/-- The `d = 5` control: `mech 5 3 0 = (1,2,2)`, rotations `(2,2,1)`, `(2,1,2)`, intercepts
`23, 37, 29` (C004's table), `37 < 2 · 23`. -/
example : mech 5 3 0 = [1, 2, 2] ∧ (mech 5 3 0).rotate 1 = [2, 2, 1] ∧
    (mech 5 3 0).rotate 2 = [2, 1, 2] := by decide

example : C [1, 2, 2] = 23 ∧ C [2, 2, 1] = 37 ∧ C [2, 1, 2] = 29 ∧ D [1, 2, 2] = 5 := by
  norm_num [C, D]

/-! ### Toward C004's forward direction (narrow ⇒ mechanical), part 1: the cyclic recursion
(1) on rotations, abstract narrow cycles, the exponent dichotomy, successor order and the
rank-shift lemmas of `ROTATION_LATTICE.md` §3 -/

/-- C004's (1) in cons form: `2^a C(v ++ [a]) = 3 C(a :: v) + D(a :: v)`. -/
theorem C_cons_rotate (a : ℕ) (v : List ℕ) :
    (2 : ℤ) ^ a * C (v ++ [a]) = 3 * C (a :: v) + D (a :: v) := by
  rw [C_append]
  simp only [C, D, List.sum_cons, List.length_cons, List.length_nil, pow_succ, pow_add, pow_zero,
    one_mul, mul_zero, add_zero]
  ring

theorem D_rotate (w : List ℕ) (i : ℕ) : D (w.rotate i) = D w := by
  simp only [D, (List.rotate_perm w i).sum_eq, List.length_rotate]

/-- C004's (1) on rotations: if `w.rotate i = a :: v` then `2^a C_{i+1} = 3 C_i + D_w`. -/
theorem C_rotate_succ {w : List ℕ} {i a : ℕ} {v : List ℕ} (h : w.rotate i = a :: v) :
    (2 : ℤ) ^ a * C (w.rotate (i + 1)) = 3 * C (w.rotate i) + D w := by
  have h1 : w.rotate (i + 1) = v ++ [a] := by
    rw [← List.rotate_rotate, h, List.rotate_cons_succ, List.rotate_zero]
  rw [h1, h, ← D_rotate w i, h]
  exact C_cons_rotate a v

/-! ### C009: exact excursion cuts and the elimination `D x = q C`

C009 (`EXCURSION_ARITHMETIC.md` §§1–2) takes a positive valuation word `w` of length `ℓ`, total
`a = Σ w`, prefix totals `P_j = Σ (take j w)` and prefix intercepts `C_j = C (take j w)`, and
positive odd integers `q, x, y` with the exact endpoint relation `2^a y = 3^ℓ x + q C_w`. The
cut states `u_j = (3^j x + q C_j)/2^{P_j}` are then positive odd integers with `u_0 = x`,
`u_ℓ = y` and the exact arrows `2^{a_j} u_{j+1} = 3 u_j + q`: no internal odd-only cylinder is
lost by passing to the endpoint relation. Oddness of `x` is a consequence, not a hypothesis. -/

/-- `C_w = 3^{ℓ−j} C_j + 2^{P_j} C_tail` (composition of the prefix and the tail). -/
theorem C_take_drop (w : List ℕ) (j : ℕ) :
    C w = 3 ^ (w.drop j).length * C (w.take j) + 2 ^ (w.take j).sum * C (w.drop j) := by
  rw [← C_append, List.take_append_drop]

/-- `Σ w = P_j + Σ tail`. -/
theorem sum_take_drop (w : List ℕ) (j : ℕ) : w.sum = (w.take j).sum + (w.drop j).sum := by
  rw [← List.sum_append, List.take_append_drop]

/-- The integrality step of C009's cut lemma: reducing the endpoint relation modulo `2^{P_j}`
and cancelling the unit `3^{ℓ−j}` gives `2^{P_j} ∣ 3^j x + q C_j`. -/
theorem cut_dvd (w : List ℕ) {q x y : ℤ} (h : 2 ^ w.sum * y = 3 ^ w.length * x + q * C w)
    {j : ℕ} (hj : j ≤ w.length) :
    (2 : ℤ) ^ (w.take j).sum ∣ 3 ^ j * x + q * C (w.take j) := by
  have hsplit := C_take_drop w j
  have hsum := sum_take_drop w j
  have hlen : w.length = j + (w.drop j).length := by rw [List.length_drop]; omega
  have hcop : IsCoprime ((2 : ℤ) ^ (w.take j).sum) (3 ^ (w.drop j).length) :=
    (Int.isCoprime_iff_gcd_eq_one.mpr (by norm_num)).pow
  apply hcop.dvd_of_dvd_mul_left
  refine ⟨2 ^ (w.drop j).sum * y - q * C (w.drop j), ?_⟩
  rw [hlen, hsum, hsplit] at h
  linear_combination (-1 : ℤ) * h

/-- The cut states `u_j = (3^j x + q C_j)/2^{P_j}` of C009's lemma. -/
def cutState (w : List ℕ) (q x : ℤ) (j : ℕ) : ℤ :=
  (3 ^ j * x + q * C (w.take j)) / 2 ^ (w.take j).sum

/-- `2^{P_j} u_j = 3^j x + q C_j`: the cut state is an integer. -/
theorem cutState_spec (w : List ℕ) {q x y : ℤ}
    (h : 2 ^ w.sum * y = 3 ^ w.length * x + q * C w) {j : ℕ} (hj : j ≤ w.length) :
    2 ^ (w.take j).sum * cutState w q x j = 3 ^ j * x + q * C (w.take j) :=
  Int.mul_ediv_cancel' (cut_dvd w h hj)

theorem cutState_zero (w : List ℕ) (q x : ℤ) : cutState w q x 0 = x := by
  simp [cutState, C]

theorem cutState_last (w : List ℕ) {q x y : ℤ}
    (h : 2 ^ w.sum * y = 3 ^ w.length * x + q * C w) : cutState w q x w.length = y := by
  have hs := cutState_spec w h (le_refl w.length)
  rw [List.take_length] at hs
  exact mul_left_cancel₀ (pow_ne_zero _ two_ne_zero) (hs.trans h.symm)

/-- The exact arrow `2^{a_j} u_{j+1} = 3 u_j + q` between consecutive cut states. -/
theorem cutState_arrow (w : List ℕ) {q x y : ℤ}
    (h : 2 ^ w.sum * y = 3 ^ w.length * x + q * C w) {j : ℕ} (hj : j < w.length) :
    2 ^ w[j] * cutState w q x (j + 1) = 3 * cutState w q x j + q := by
  have h1 := cutState_spec w h hj.le
  have h2 := cutState_spec w h (show j + 1 ≤ w.length from hj)
  rw [List.take_succ_eq_append_getElem hj, List.sum_append, C_append] at h2
  simp only [List.sum_cons, List.sum_nil, add_zero, List.length_singleton, List.length_nil,
    pow_one, pow_zero, C, mul_zero, mul_one] at h2
  apply mul_left_cancel₀ (pow_ne_zero (w.take j).sum (two_ne_zero : (2 : ℤ) ≠ 0))
  linear_combination h2 - 3 * h1

/-- Positivity of the cut states (`q, x > 0`). -/
theorem cutState_pos (w : List ℕ) {q x y : ℤ} (hq : 0 < q) (hx : 0 < x)
    (h : 2 ^ w.sum * y = 3 ^ w.length * x + q * C w) {j : ℕ} (hj : j ≤ w.length) :
    0 < cutState w q x j := by
  have hs := cutState_spec w h hj
  have hC := C_nonneg (w.take j)
  have h3 : (0 : ℤ) < 3 ^ j * x := mul_pos (by positivity) hx
  have hqC : 0 ≤ q * C (w.take j) := mul_nonneg hq.le hC
  have h2 : (0 : ℤ) < 2 ^ (w.take j).sum := by positivity
  have hpos : 0 < 2 ^ (w.take j).sum * cutState w q x j := by rw [hs]; linarith
  exact (mul_pos_iff_of_pos_left h2).mp hpos

/-- Oddness of the cut states: `u_ℓ = y` is odd, and for `j < ℓ` the arrow
`2^{a_j} u_{j+1} = 3 u_j + q` has an even left side (`a_j ≥ 1`) and odd `q`, so `u_j` is odd. -/
theorem cutState_odd (w : List ℕ) (hw : ∀ a ∈ w, 1 ≤ a) {q x y : ℤ} (hq : Odd q) (hy : Odd y)
    (h : 2 ^ w.sum * y = 3 ^ w.length * x + q * C w) {j : ℕ} (hj : j ≤ w.length) :
    Odd (cutState w q x j) := by
  rcases Nat.lt_or_ge j w.length with hlt | hge
  · have harrow := cutState_arrow w h hlt
    have ha : 1 ≤ w[j] := hw _ (List.getElem_mem hlt)
    have heven : Even (2 ^ w[j] * cutState w q x (j + 1)) :=
      even_iff_two_dvd.mpr (dvd_mul_of_dvd_left (dvd_pow_self 2 (by omega)) _)
    rw [harrow] at heven
    have hq' : ¬ Even q := Int.not_even_iff_odd.mpr hq
    have h3 : Odd (3 * cutState w q x j) :=
      Int.not_even_iff_odd.mp (fun he => hq' ((Int.even_add.mp heven).mp he))
    exact (Int.odd_mul.mp h3).2
  · rw [le_antisymm hj hge, cutState_last w h]
    exact hy

/-- **C009's cut lemma** (`EXCURSION_ARITHMETIC.md` §1). For a positive word `w` of length `ℓ`,
total `a` and intercept `C_w`, and integers `q > 0` odd, `x > 0`, `y` odd with
`2^a y = 3^ℓ x + q C_w`, the cut states `u_j` (`j ≤ ℓ`) satisfy `u_0 = x`, `u_ℓ = y`,
`2^{P_j} u_j = 3^j x + q C_j`, are positive odd integers, and obey the exact arrows
`2^{a_j} u_{j+1} = 3 u_j + q`. (Oddness of the next state is the exactness of the valuation.) -/
theorem cut_lemma (w : List ℕ) (hw : ∀ a ∈ w, 1 ≤ a) {q x y : ℤ} (hq0 : 0 < q) (hq : Odd q)
    (hx0 : 0 < x) (hy : Odd y) (h : 2 ^ w.sum * y = 3 ^ w.length * x + q * C w) :
    cutState w q x 0 = x ∧ cutState w q x w.length = y ∧
    (∀ j, j ≤ w.length →
      2 ^ (w.take j).sum * cutState w q x j = 3 ^ j * x + q * C (w.take j)) ∧
    (∀ j, j ≤ w.length → 0 < cutState w q x j ∧ Odd (cutState w q x j)) ∧
    (∀ j, (hj : j < w.length) →
      2 ^ w[j] * cutState w q x (j + 1) = 3 * cutState w q x j + q) :=
  ⟨cutState_zero w q x, cutState_last w h, fun _ hj => cutState_spec w h hj,
    fun _ hj => ⟨cutState_pos w hq0 hx0 h hj, cutState_odd w hw hq hy h hj⟩,
    fun _ hj => cutState_arrow w h hj⟩

/-- C009's (3): eliminating `y` from the endpoint equations of an excursion `E` and its
complement `P` gives `D x = q C` with `D = D_{EP} = 2^{a+b} − 3^{ℓ+r}` and
`C = C_{EP} = 3^r C_E + 2^a C_P`, the intercept of the full word based at `x`. -/
theorem elimination (E P : List ℕ) {q x y : ℤ}
    (hE : 2 ^ E.sum * y = 3 ^ E.length * x + q * C E)
    (hP : 2 ^ P.sum * x = 3 ^ P.length * y + q * C P) :
    D (E ++ P) * x = q * C (E ++ P) ∧
      C (E ++ P) = 3 ^ P.length * C E + 2 ^ E.sum * C P := by
  refine ⟨?_, C_append E P⟩
  rw [D, List.sum_append, List.length_append, C_append]
  linear_combination 2 ^ E.sum * hP + 3 ^ P.length * hE

/-- At `q = 1` an integer solution of the cycle equation forces `D_w ∣ C_w` (C009 §2,
necessity). -/
theorem D_dvd_C_of_cycle {w : List ℕ} {x : ℤ}
    (h : 2 ^ w.sum * x = 3 ^ w.length * x + C w) : D w ∣ C w :=
  ⟨x, by rw [D]; linear_combination (-1 : ℤ) * h⟩

/-- `D_w` is coprime to `2` (it is odd). -/
theorem isCoprime_two_D {w : List ℕ} (hw : 1 ≤ w.sum) : IsCoprime (2 : ℤ) (D w) := by
  rw [Int.isCoprime_iff_gcd_eq_one]
  have h1 : Int.gcd 2 (D w) ∣ 2 := by
    have := Int.gcd_dvd_left (2 : ℤ) (D w)
    exact_mod_cast this
  rcases (Nat.dvd_prime Nat.prime_two).mp h1 with h | h
  · exact h
  · exfalso
    apply D_odd hw
    have := Int.gcd_dvd_right (2 : ℤ) (D w)
    rw [h] at this
    exact_mod_cast this

/-- The rotation recurrence `2^{a_i} C_{(i+1)} = 3 C_{(i)} + D` propagates `D ∣ C_{(i)}` to
every phase (C009 §2; `D` is odd). -/
theorem dvd_C_rotate {w : List ℕ} (hw0 : w ≠ []) (hw : ∀ a ∈ w, 1 ≤ a) (hdvd : D w ∣ C w) :
    ∀ i, D w ∣ C (w.rotate i) := by
  intro i
  induction i with
  | zero => simpa using hdvd
  | succ i ih =>
    obtain ⟨a, v, hav⟩ : ∃ a v, w.rotate i = a :: v := by
      cases hrot : w.rotate i with
      | nil => exact absurd (List.rotate_eq_nil_iff.mp hrot) hw0
      | cons a v => exact ⟨a, v, rfl⟩
    have hrec := C_rotate_succ hav
    have h2 : D w ∣ 2 ^ a * C (w.rotate (i + 1)) := by
      rw [hrec]
      exact dvd_add (dvd_mul_of_dvd_right ih 3) dvd_rfl
    have hcop : IsCoprime (D w) (2 ^ a) :=
      (isCoprime_two_D (one_le_sum_of_ne_nil hw0 hw)).symm.pow_right
    exact hcop.dvd_of_dvd_mul_left h2

/-- Every phase quotient `C_{(i)}/D` is odd when `D ∣ C` (C009 §2). -/
theorem odd_quot_rotate {w : List ℕ} (hw0 : w ≠ []) (hw : ∀ a ∈ w, 1 ≤ a) (hdvd : D w ∣ C w)
    (i : ℕ) : Odd (C (w.rotate i) / D w) := by
  have hd := dvd_C_rotate hw0 hw hdvd i
  have hrot0 : w.rotate i ≠ [] := fun h => hw0 (List.rotate_eq_nil_iff.mp h)
  have hrotpos : ∀ a ∈ w.rotate i, 1 ≤ a := fun a ha => hw a (List.mem_rotate.mp ha)
  have hodd := C_odd hrot0 hrotpos
  rw [← Int.mul_ediv_cancel' hd] at hodd
  exact (Int.odd_mul.mp hodd).2

/-- C009 §2 at `q = 1`, sufficiency: if `D_w > 0` and `D_w x = C_w` for a positive word `w`,
then `x` is a positive odd integer closing the cycle equation `2^A x = 3^m x + 1 · C_w`. -/
theorem integer_cycle_of_dvd (w : List ℕ) (hw0 : w ≠ []) (hw : ∀ a ∈ w, 1 ≤ a) (hD : 0 < D w)
    {x : ℤ} (hx : D w * x = C w) :
    0 < x ∧ Odd x ∧ 2 ^ w.sum * x = 3 ^ w.length * x + 1 * C w := by
  have hC := C_pos hw0
  have hCodd := C_odd hw0 hw
  refine ⟨?_, ?_, ?_⟩
  · have hDx : 0 < D w * x := by rw [hx]; exact hC
    exact (mul_pos_iff_of_pos_left hD).mp hDx
  · rw [← hx] at hCodd
    exact (Int.odd_mul.mp hCodd).2
  · rw [D] at hx
    linear_combination hx

/-- C009 §2 at `q = 1`: `D_w ∣ C_w` (with `D_w > 0`, positive `w`) yields the odd integer cycle
through `x = C_w/D_w`, with every cut state a positive odd integer and every arrow exact —
the cut lemma recovers all the internal cylinders. -/
theorem cylinders_of_dvd (w : List ℕ) (hw0 : w ≠ []) (hw : ∀ a ∈ w, 1 ≤ a) (hD : 0 < D w)
    {x : ℤ} (hx : D w * x = C w) :
    cutState w 1 x 0 = x ∧ cutState w 1 x w.length = x ∧
    (∀ j, j ≤ w.length → 0 < cutState w 1 x j ∧ Odd (cutState w 1 x j)) ∧
    (∀ j, (hj : j < w.length) →
      2 ^ w[j] * cutState w 1 x (j + 1) = 3 * cutState w 1 x j + 1) := by
  obtain ⟨hx0, hxodd, hcyc⟩ := integer_cycle_of_dvd w hw0 hw hD hx
  obtain ⟨h0, hl, -, hpo, harr⟩ := cut_lemma w hw one_pos odd_one hx0 hxodd hcyc
  exact ⟨h0, hl, hpo, harr⟩

/-- The exponent `q` of C004 §3 exists: `2^q lo ≤ 3 lo + d < 2^{q+1} lo`. -/
theorem exists_exponent {lo d : ℤ} (hlo : 0 < lo) (hd : 0 < d) :
    ∃ q : ℕ, (2 : ℤ) ^ q * lo ≤ 3 * lo + d ∧ 3 * lo + d < 2 ^ (q + 1) * lo := by
  classical
  have hex : ∃ n : ℕ, 3 * lo + d < 2 ^ (n + 1) * lo := by
    obtain ⟨n, hn⟩ := pow_unbounded_of_one_lt (3 * lo + d) (by norm_num : (1 : ℤ) < 2)
    refine ⟨n, ?_⟩
    have h1 : (2 : ℤ) ^ n ≤ 2 ^ (n + 1) := pow_le_pow_right₀ (by norm_num) (Nat.le_succ n)
    have h2 : (2 : ℤ) ^ (n + 1) ≤ 2 ^ (n + 1) * lo :=
      le_mul_of_one_le_right (by positivity) (by linarith)
    linarith
  refine ⟨Nat.find hex, ?_, Nat.find_spec hex⟩
  rcases Nat.eq_zero_or_pos (Nat.find hex) with h0 | hpos
  · rw [h0, pow_zero, one_mul]; linarith
  · have hmin := Nat.find_min hex (Nat.sub_lt hpos Nat.one_pos)
    rw [Nat.sub_add_cancel hpos] at hmin
    exact not_lt.mp hmin

/-- The exponent dichotomy of C004 §3: if the states `x, y` of an arrow `2^a y = 3x + d` lie in
`[lo, 2 lo)` and `2^q lo ≤ 3 lo + d < 2^{q+1} lo`, then `a = q` exactly when
`3x + d < 2^{q+1} lo`, and `a = q + 1` exactly when `2^{q+1} lo ≤ 3x + d`. -/
theorem exponent_dichotomy {lo d x y : ℤ} {a q : ℕ} (hd : 0 < d) (hx : lo ≤ x) (hx2 : x < 2 * lo)
    (hy : lo ≤ y) (hy2 : y < 2 * lo) (harrow : (2 : ℤ) ^ a * y = 3 * x + d)
    (hq1 : (2 : ℤ) ^ q * lo ≤ 3 * lo + d) (hq2 : 3 * lo + d < 2 ^ (q + 1) * lo) :
    (a = q ∧ 3 * x + d < 2 ^ (q + 1) * lo) ∨ (a = q + 1 ∧ 2 ^ (q + 1) * lo ≤ 3 * x + d) := by
  have hlo : 0 < lo := by linarith
  have h2a : (0 : ℤ) < 2 ^ a := by positivity
  rcases lt_trichotomy a q with hlt | heq | hgt
  · exfalso
    have h1 : (2 : ℤ) ^ (a + 1) ≤ 2 ^ q := pow_le_pow_right₀ (by norm_num) hlt
    rw [pow_succ] at h1
    nlinarith [mul_lt_mul_of_pos_left hy2 h2a, mul_le_mul_of_nonneg_right h1 hlo.le]
  · subst heq
    left
    refine ⟨rfl, ?_⟩
    rw [pow_succ]
    nlinarith [mul_lt_mul_of_pos_left hy2 h2a]
  · rcases Nat.lt_or_ge (q + 1) a with hgt2 | hle
    · exfalso
      have h1 : (2 : ℤ) ^ (q + 2) ≤ 2 ^ a := pow_le_pow_right₀ (by norm_num) hgt2
      rw [pow_add] at h1
      rw [pow_succ] at hq2
      nlinarith [mul_le_mul_of_nonneg_left hy h2a.le, mul_le_mul_of_nonneg_right h1 hlo.le]
    · have ha : a = q + 1 := le_antisymm hle hgt
      subst ha
      right
      refine ⟨rfl, ?_⟩
      nlinarith [mul_le_mul_of_nonneg_left hy h2a.le]

/-- Successors of two states with the same exponent compare as the states. -/
theorem succ_order_same {d x x' y y' : ℤ} {a : ℕ} (harrow : (2 : ℤ) ^ a * y = 3 * x + d)
    (harrow' : (2 : ℤ) ^ a * y' = 3 * x' + d) : y < y' ↔ x < x' := by
  have h2a : (0 : ℤ) < 2 ^ a := by positivity
  constructor
  · intro h; nlinarith [mul_lt_mul_of_pos_left h h2a]
  · intro h; exact lt_of_mul_lt_mul_left (by linarith) h2a.le

/-- A high-exponent successor lies below every low-exponent successor (narrow states). -/
theorem succ_order_high_low {lo d x x' y y' : ℤ} {q : ℕ} (hd : 0 < d) (hx2 : x < 2 * lo)
    (hx' : lo ≤ x') (harrow : (2 : ℤ) ^ (q + 1) * y = 3 * x + d)
    (harrow' : (2 : ℤ) ^ q * y' = 3 * x' + d) : y < y' := by
  have h2q : (0 : ℤ) < 2 ^ q := by positivity
  rw [pow_succ] at harrow
  have h : (2 : ℤ) ^ q * 2 * y < 2 ^ q * 2 * y' := by linarith
  exact lt_of_mul_lt_mul_left h (by positivity)

/-- The exponent dichotomy in image form: if `y ∈ [lo, 2 lo)`, `2^a y = F` and
`2^q lo ≤ F < 2^{q+2} lo`, then `a = q` exactly when `F < 2^{q+1} lo`, and `a = q + 1` exactly
when `2^{q+1} lo ≤ F`. -/
theorem exponent_dichotomy_F {lo F y : ℤ} {a q : ℕ} (hy : lo ≤ y) (hy2 : y < 2 * lo)
    (harrow : (2 : ℤ) ^ a * y = F) (hq1 : (2 : ℤ) ^ q * lo ≤ F) (hq2 : F < 2 ^ (q + 2) * lo) :
    (a = q ∧ F < 2 ^ (q + 1) * lo) ∨ (a = q + 1 ∧ 2 ^ (q + 1) * lo ≤ F) := by
  have hlo : 0 < lo := by linarith
  have h2a : (0 : ℤ) < 2 ^ a := by positivity
  rcases lt_trichotomy a q with hlt | heq | hgt
  · exfalso
    have h1 : (2 : ℤ) ^ (a + 1) ≤ 2 ^ q := pow_le_pow_right₀ (by norm_num) hlt
    rw [pow_succ] at h1
    nlinarith [mul_lt_mul_of_pos_left hy2 h2a, mul_le_mul_of_nonneg_right h1 hlo.le]
  · subst heq
    left
    refine ⟨rfl, ?_⟩
    rw [pow_succ]
    nlinarith [mul_lt_mul_of_pos_left hy2 h2a]
  · rcases Nat.lt_or_ge (q + 1) a with hgt2 | hle
    · exfalso
      have h1 : (2 : ℤ) ^ (q + 2) ≤ 2 ^ a := pow_le_pow_right₀ (by norm_num) hgt2
      nlinarith [mul_le_mul_of_nonneg_left hy h2a.le, mul_le_mul_of_nonneg_right h1 hlo.le]
    · have ha : a = q + 1 := le_antisymm hle hgt
      subst ha
      right
      refine ⟨rfl, ?_⟩
      nlinarith [mul_le_mul_of_nonneg_left hy h2a.le]

/-- Abstract data of an ordered, dyadically normalised cycle of period `m` (C004 §3 with a
constant offset; C005's order lemma in general): states `x i`, periodic mod `m`, all in
`[lo, 2 lo)`; exponents `a i` with the arrows `2^{a i} x(i+1) = F i`, where the images `F i`
are strictly increasing in the states (`x i < x j ↔ F i < F j`) and lie in a factor-two window
(`F i < 2 F j`); and an exponent `q` with `2^q lo ≤ F i < 2^{q+2} lo`. For C004,
`F i = 3 x i + d`; for C005, `F i = 3 z_i + q/2^{h_i}` after scaling to integers. -/
structure NarrowCycle (m : ℕ) where
  x : ℕ → ℤ
  a : ℕ → ℕ
  F : ℕ → ℤ
  lo : ℤ
  q : ℕ
  hm : 0 < m
  periodic : ∀ i, x (i + m) = x i
  arrow : ∀ i, (2 : ℤ) ^ a i * x (i + 1) = F i
  lower : ∀ i, lo ≤ x i
  upper : ∀ i, x i < 2 * lo
  order : ∀ i j, x i < x j ↔ F i < F j
  window : ∀ i j, F i < 2 * F j
  hq1 : ∀ i, (2 : ℤ) ^ q * lo ≤ F i
  hq2 : ∀ i, F i < 2 ^ (q + 2) * lo

namespace NarrowCycle

variable {m : ℕ} (N : NarrowCycle m)

theorem lo_pos : 0 < N.lo := by
  have h1 := N.lower 0
  have h2 := N.upper 0
  linarith

theorem F_eq_of_x_eq {i j : ℕ} (h : N.x i = N.x j) : N.F i = N.F j := by
  have h1 : ¬ N.F i < N.F j := fun hlt => by
    have := (N.order i j).mpr hlt
    rw [h] at this
    exact lt_irrefl _ this
  have h2 : ¬ N.F j < N.F i := fun hlt => by
    have := (N.order j i).mpr hlt
    rw [h] at this
    exact lt_irrefl _ this
  exact le_antisymm (not_lt.mp h2) (not_lt.mp h1)

/-- Index `i` is *high* when its arrow has exponent `q + 1`. -/
def high (i : ℕ) : Prop := 2 ^ (N.q + 1) * N.lo ≤ N.F i

instance decHigh (i : ℕ) : Decidable (N.high i) :=
  inferInstanceAs (Decidable (2 ^ (N.q + 1) * N.lo ≤ N.F i))

/-- The exponent dichotomy on the cycle. -/
theorem a_eq (i : ℕ) : N.a i = if N.high i then N.q + 1 else N.q := by
  have hdi := exponent_dichotomy_F (N.lower (i + 1)) (N.upper (i + 1)) (N.arrow i) (N.hq1 i)
    (N.hq2 i)
  split_ifs with hc
  · rcases hdi with ⟨_, h2⟩ | ⟨h1, _⟩
    · exact absurd hc (not_le.mpr h2)
    · exact h1
  · rcases hdi with ⟨h1, _⟩ | ⟨_, h2⟩
    · exact h1
    · exact absurd h2 hc

theorem a_of_low {i : ℕ} (hi : ¬ N.high i) : N.a i = N.q := by rw [N.a_eq, ite_eq_right hi]

theorem a_of_high {i : ℕ} (hi : N.high i) : N.a i = N.q + 1 := by rw [N.a_eq, ite_eq_left hi]

/-- Low states lie below high states. -/
theorem x_lt_of_low_high {i j : ℕ} (hi : ¬ N.high i) (hj : N.high j) : N.x i < N.x j := by
  have hi' : N.F i < 2 ^ (N.q + 1) * N.lo := by simpa [high, not_le] using hi
  have hj' : 2 ^ (N.q + 1) * N.lo ≤ N.F j := hj
  exact (N.order i j).mpr (lt_of_lt_of_le hi' hj')

/-- Successors of two states with the same exponent compare as the states. -/
theorem succ_lt_iff_of_a_eq {i j : ℕ} (h : N.a i = N.a j) :
    N.x (i + 1) < N.x (j + 1) ↔ N.x i < N.x j := by
  have h1 := N.arrow i
  have h2 := N.arrow j
  rw [h] at h1
  have h2a : (0 : ℤ) < 2 ^ N.a j := by positivity
  rw [N.order i j, ← h1, ← h2]
  exact ⟨fun hlt => mul_lt_mul_of_pos_left hlt h2a, fun hlt => lt_of_mul_lt_mul_left hlt h2a.le⟩

theorem succ_lt_iff_low {i j : ℕ} (hi : ¬ N.high i) (hj : ¬ N.high j) :
    N.x (i + 1) < N.x (j + 1) ↔ N.x i < N.x j :=
  N.succ_lt_iff_of_a_eq (by rw [N.a_of_low hi, N.a_of_low hj])

theorem succ_lt_iff_high {i j : ℕ} (hi : N.high i) (hj : N.high j) :
    N.x (i + 1) < N.x (j + 1) ↔ N.x i < N.x j :=
  N.succ_lt_iff_of_a_eq (by rw [N.a_of_high hi, N.a_of_high hj])

/-- A high-exponent successor lies below every low-exponent successor (the factor-two window). -/
theorem succ_lt_of_high_low {i j : ℕ} (hi : N.high i) (hj : ¬ N.high j) :
    N.x (i + 1) < N.x (j + 1) := by
  have h1 := N.arrow i
  have h2 := N.arrow j
  rw [N.a_of_high hi, pow_succ] at h1
  rw [N.a_of_low hj] at h2
  have hw := N.window i j
  have h2q : (0 : ℤ) < 2 ^ N.q := by positivity
  have h : (2 : ℤ) ^ N.q * 2 * N.x (i + 1) < 2 ^ N.q * 2 * N.x (j + 1) := by linarith
  exact lt_of_mul_lt_mul_left h (by positivity)

/-- Shifting the summation index once around the cycle. -/
theorem sum_range_shift (f : ℕ → ℕ) (hf : f m = f 0) :
    ∑ j ∈ Finset.range m, f (j + 1) = ∑ j ∈ Finset.range m, f j := by
  have h1 := Finset.sum_range_succ f m
  have h2 := Finset.sum_range_succ' f m
  omega

theorem x_add_mul (n k : ℕ) : N.x (n + m * k) = N.x n := by
  induction k with
  | zero => simp
  | succ k ih => rw [Nat.mul_succ, ← Nat.add_assoc, N.periodic, ih]

theorem x_mod (i : ℕ) : N.x (i % m) = N.x i := by
  conv_rhs => rw [← Nat.mod_add_div i m]
  exact (N.x_add_mul _ _).symm

theorem x_m : N.x m = N.x 0 := by simpa using N.periodic 0

/-- The rank of index `i`: the number of indices `j < m` whose state lies below `x i`. -/
def rank (i : ℕ) : ℕ := ∑ j ∈ Finset.range m, if N.x j < N.x i then 1 else 0

/-- The number of high indices among `0, …, m − 1` (C004's `h`). -/
def numHigh : ℕ := ∑ j ∈ Finset.range m, if N.high j then 1 else 0

theorem numHigh_add_low :
    N.numHigh + (∑ j ∈ Finset.range m, if N.high j then 0 else 1) = m := by
  unfold numHigh
  rw [← Finset.sum_add_distrib]
  calc (∑ j ∈ Finset.range m, ((if N.high j then 1 else 0) + if N.high j then 0 else 1))
      = ∑ j ∈ Finset.range m, 1 := Finset.sum_congr rfl (fun j _ => by split_ifs <;> omega)
    _ = m := by simp

theorem numHigh_le : N.numHigh ≤ m := by
  have := N.numHigh_add_low
  omega

theorem sum_low : (∑ j ∈ Finset.range m, if N.high j then 0 else 1) = m - N.numHigh := by
  have := N.numHigh_add_low
  omega

theorem rank_succ (i : ℕ) :
    N.rank (i + 1) = ∑ j ∈ Finset.range m, if N.x (j + 1) < N.x (i + 1) then 1 else 0 := by
  unfold rank
  exact (sum_range_shift (fun j => if N.x j < N.x (i + 1) then 1 else 0) (by simp [N.x_m])).symm

/-- **C004 §3, rank shift at a low index:** `rank(i+1) = rank(i) + h`. -/
theorem rank_succ_of_low {i : ℕ} (hi : ¬ N.high i) : N.rank (i + 1) = N.rank i + N.numHigh := by
  rw [N.rank_succ, rank, numHigh, ← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro j _
  by_cases hj : N.high j
  · simp only [ite_eq_left (N.succ_lt_of_high_low hj hi),
      ite_eq_right (not_lt.mpr (N.x_lt_of_low_high hi hj).le), ite_eq_left hj, zero_add]
  · simp only [ite_eq_right hj, add_zero]
    by_cases hx : N.x j < N.x i
    · simp only [ite_eq_left hx, ite_eq_left ((N.succ_lt_iff_low hj hi).mpr hx)]
    · simp only [ite_eq_right hx, ite_eq_right ((fun h => hx ((N.succ_lt_iff_low hj hi).mp h)) :
        ¬ N.x (j + 1) < N.x (i + 1))]

/-- **C004 §3, rank shift at a high index:** `rank(i) = rank(i+1) + (m − h)`. -/
theorem rank_of_high {i : ℕ} (hi : N.high i) : N.rank i = N.rank (i + 1) + (m - N.numHigh) := by
  rw [← N.sum_low, N.rank_succ, rank, ← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro j _
  by_cases hj : N.high j
  · simp only [ite_eq_left hj, add_zero]
    by_cases hx : N.x j < N.x i
    · simp only [ite_eq_left hx, ite_eq_left ((N.succ_lt_iff_high hj hi).mpr hx)]
    · simp only [ite_eq_right hx, ite_eq_right ((fun h => hx ((N.succ_lt_iff_high hj hi).mp h)) :
        ¬ N.x (j + 1) < N.x (i + 1))]
  · simp only [ite_eq_left (N.x_lt_of_low_high hj hi),
      ite_eq_right (not_lt.mpr (N.succ_lt_of_high_low hi hj).le), ite_eq_right hj, zero_add]

/-- A high index has rank at least `m − h`. -/
theorem rank_ge_of_high {i : ℕ} (hi : N.high i) : m - N.numHigh ≤ N.rank i := by
  rw [← N.sum_low, rank]
  apply Finset.sum_le_sum
  intro j _
  by_cases hj : N.high j
  · simp only [ite_eq_left hj]
    exact Nat.zero_le _
  · simp only [ite_eq_right hj, ite_eq_left (N.x_lt_of_low_high hj hi), le_refl]

/-- A low index `i < m` has rank below `m − h`. -/
theorem rank_lt_of_low {i : ℕ} (hi : i < m) (hlow : ¬ N.high i) : N.rank i < m - N.numHigh := by
  rw [← N.sum_low, rank]
  apply Finset.sum_lt_sum
  · intro j _
    by_cases hj : N.high j
    · have h : ¬ N.x j < N.x i := not_lt.mpr (N.x_lt_of_low_high hlow hj).le
      simp only [ite_eq_right h, ite_eq_left hj, le_refl]
    · simp only [ite_eq_right hj]
      split_ifs <;> omega
  · exact ⟨i, Finset.mem_range.mpr hi, by simp [hlow]⟩

/-- The high indices are exactly the `h` largest ranks. -/
theorem high_iff_rank {i : ℕ} (hi : i < m) : N.high i ↔ m - N.numHigh ≤ N.rank i :=
  ⟨N.rank_ge_of_high, fun h => by
    by_contra hlow
    exact absurd h (not_le.mpr (N.rank_lt_of_low hi hlow))⟩

/-! #### Part 2: the rank formula, `gcd(h, m) = 1` and the letter formula -/

theorem rank_mod (i : ℕ) : N.rank (i % m) = N.rank i := by
  unfold rank
  rw [N.x_mod]

theorem F_mod (i : ℕ) : N.F (i % m) = N.F i := N.F_eq_of_x_eq (N.x_mod i)

theorem high_mod (i : ℕ) : N.high (i % m) ↔ N.high i := by
  unfold high
  rw [N.F_mod]

/-- `rank i < m`: the index `i` itself (reduced mod `m`) is never counted. -/
theorem rank_lt (i : ℕ) : N.rank i < m := by
  unfold rank
  calc (∑ j ∈ Finset.range m, if N.x j < N.x i then 1 else 0)
      < ∑ j ∈ Finset.range m, 1 := by
        apply Finset.sum_lt_sum
        · intro j _
          split_ifs <;> omega
        · refine ⟨i % m, Finset.mem_range.mpr (Nat.mod_lt _ N.hm), ?_⟩
          rw [N.x_mod]
          simp
    _ = m := by simp

/-- Ranks are strictly monotone in the states (for a counted index `i < m`). -/
theorem rank_lt_of_lt {i j : ℕ} (hi : i < m) (h : N.x i < N.x j) : N.rank i < N.rank j := by
  unfold rank
  apply Finset.sum_lt_sum
  · intro k _
    split_ifs <;> omega
  · refine ⟨i, Finset.mem_range.mpr hi, ?_⟩
    simp [h]

theorem x_eq_of_rank_eq {i j : ℕ} (hi : i < m) (hj : j < m) (h : N.rank i = N.rank j) :
    N.x i = N.x j := by
  rcases lt_trichotomy (N.x i) (N.x j) with hlt | heq | hgt
  · exact absurd h (ne_of_lt (N.rank_lt_of_lt hi hlt))
  · exact heq
  · exact absurd h.symm (ne_of_lt (N.rank_lt_of_lt hj hgt))

/-- Primitivity (the prose's "primitive state period"): the `m` states are distinct. -/
def Primitive : Prop := ∀ i j, i < m → j < m → N.x i = N.x j → i = j

theorem rank_inj (hp : N.Primitive) {i j : ℕ} (hi : i < m) (hj : j < m)
    (h : N.rank i = N.rank j) : i = j :=
  hp i j hi hj (N.x_eq_of_rank_eq hi hj h)

theorem all_low_of_numHigh_zero (h0 : N.numHigh = 0) (j : ℕ) : ¬ N.high j := by
  intro hj
  have h1 : m - N.numHigh ≤ N.rank j := N.rank_ge_of_high hj
  rw [h0, Nat.sub_zero] at h1
  exact absurd (N.rank_lt j) (not_lt.mpr h1)

theorem all_high_of_numHigh_eq (hm0 : N.numHigh = m) (j : ℕ) : N.high j := by
  by_contra hj
  have h1 := N.rank_lt_of_low (Nat.mod_lt j N.hm) ((not_congr (N.high_mod j)).mpr hj)
  rw [hm0, Nat.sub_self] at h1
  exact Nat.not_lt_zero _ h1

/-- A primitive narrow cycle with `m ≥ 2` has a high index: `h ≥ 1`. -/
theorem numHigh_pos (hp : N.Primitive) (hm2 : 2 ≤ m) : 0 < N.numHigh := by
  rcases Nat.eq_zero_or_pos N.numHigh with h0 | hpos
  · exfalso
    have h01 : N.rank 1 = N.rank 0 + N.numHigh :=
      N.rank_succ_of_low (N.all_low_of_numHigh_zero h0 0)
    rw [h0, Nat.add_zero] at h01
    have := N.rank_inj hp (by omega) (by omega) h01
    omega
  · exact hpos

/-- A primitive narrow cycle with `m ≥ 2` has a low index: `h ≤ m − 1`. -/
theorem numHigh_lt (hp : N.Primitive) (hm2 : 2 ≤ m) : N.numHigh < m := by
  rcases Nat.lt_or_ge N.numHigh m with h | h
  · exact h
  · exfalso
    have hm0 : N.numHigh = m := le_antisymm N.numHigh_le h
    have h01 : N.rank 0 = N.rank 1 + (m - N.numHigh) :=
      N.rank_of_high (N.all_high_of_numHigh_eq hm0 0)
    rw [hm0, Nat.sub_self, Nat.add_zero] at h01
    have := N.rank_inj hp (by omega) (by omega) h01
    omega

/-- The rank shift in one formula: `rank(i+1) = (rank i + h) mod m`. -/
theorem rank_succ_eq (hh : N.numHigh < m) (i : ℕ) :
    N.rank (i + 1) = (N.rank i + N.numHigh) % m := by
  by_cases hi : N.high i
  · have h1 := N.rank_of_high hi
    have h2 : m - N.numHigh ≤ N.rank i := N.rank_ge_of_high hi
    have h3 := N.rank_lt (i + 1)
    rw [Nat.mod_eq_sub_mod (show m ≤ N.rank i + N.numHigh by omega),
      Nat.mod_eq_of_lt (show N.rank i + N.numHigh - m < m by omega)]
    omega
  · rw [N.rank_succ_of_low hi]
    have h1 : N.rank i < m - N.numHigh := by
      have := N.rank_lt_of_low (Nat.mod_lt i N.hm) ((not_congr (N.high_mod i)).mpr hi)
      rwa [N.rank_mod] at this
    rw [Nat.mod_eq_of_lt (show N.rank i + N.numHigh < m by omega)]

/-- **C004 §3:** time `i` has rank `rank 0 + i h mod m`. -/
theorem rank_formula (hh : N.numHigh < m) (i : ℕ) :
    N.rank i = (N.rank 0 + i * N.numHigh) % m := by
  induction i with
  | zero => simp [Nat.mod_eq_of_lt (N.rank_lt 0)]
  | succ i ih =>
    rw [N.rank_succ_eq hh, ih, Nat.mod_add_mod, Nat.add_mul, Nat.one_mul, Nat.add_assoc]

/-- **C004 §3, the letters:** starting at the minimum (`rank 0 = 0`),
`a_i = q + ⌊(i+1)h/m⌋ − ⌊ih/m⌋`. -/
theorem a_formula (hh : N.numHigh < m) (h0 : N.rank 0 = 0) (i : ℕ) :
    N.a i = N.q + (((i + 1) * N.numHigh) / m - (i * N.numHigh) / m) := by
  have hr : N.rank i = (i * N.numHigh) % m := by
    rw [N.rank_formula hh i, h0, Nat.zero_add]
  have hlt : (i * N.numHigh) % m < m := Nat.mod_lt _ N.hm
  have hdiv : ((i + 1) * N.numHigh) / m - (i * N.numHigh) / m
      = ((i * N.numHigh) % m + N.numHigh) / m := by
    rw [Nat.add_mul, Nat.one_mul, step_mod N.hm, Nat.div_eq_of_lt hlt, Nat.sub_zero]
  rw [hdiv, N.a_eq]
  have hiff : N.high i ↔ m - N.numHigh ≤ N.rank i := by
    rw [← N.high_mod, ← N.rank_mod]
    exact N.high_iff_rank (Nat.mod_lt _ N.hm)
  split_ifs with hc
  · have h1 : m ≤ (i * N.numHigh) % m + N.numHigh := by
      have := hiff.mp hc
      omega
    rw [Nat.div_eq_of_lt_le (show 1 * m ≤ (i * N.numHigh) % m + N.numHigh by omega)
      (show (i * N.numHigh) % m + N.numHigh < Nat.succ 1 * m by omega)]
  · have h1 : (i * N.numHigh) % m + N.numHigh < m := by
      have := (not_congr hiff).mp hc
      omega
    rw [Nat.div_eq_of_lt h1, Nat.add_zero]

/-- **C004 §3:** `gcd(h, m) = 1` for a primitive narrow cycle with `m ≥ 2`. -/
theorem coprime_numHigh (hp : N.Primitive) (hm2 : 2 ≤ m) : Nat.Coprime N.numHigh m := by
  have hh := N.numHigh_lt hp hm2
  by_contra hne
  have hg1 : Nat.gcd N.numHigh m ≠ 1 := hne
  have hgpos : 0 < Nat.gcd N.numHigh m := Nat.gcd_pos_of_pos_right _ N.hm
  obtain ⟨m', hm'⟩ := Nat.gcd_dvd_right N.numHigh m
  obtain ⟨h', hh'⟩ := Nat.gcd_dvd_left N.numHigh m
  set g := Nat.gcd N.numHigh m with hg
  have hg2 : 2 ≤ g := by omega
  have hm'pos : 0 < m' := by
    rcases Nat.eq_zero_or_pos m' with h0 | h0
    · rw [h0, Nat.mul_zero] at hm'
      omega
    · exact h0
  have hm'lt : m' < m := by
    rw [hm']
    nlinarith
  have hmul : m' * N.numHigh = m * h' := by
    rw [hh', hm']
    ring
  have hr : N.rank m' = N.rank 0 := by
    rw [N.rank_formula hh m', hmul, Nat.add_mul_mod_self_left, Nat.mod_eq_of_lt (N.rank_lt 0)]
  have := N.rank_inj hp hm'lt N.hm hr
  omega

/-- The total over one period: `A = mq + h`. -/
theorem sum_a : ∑ i ∈ Finset.range m, N.a i = m * N.q + N.numHigh := by
  have h : ∀ i, N.a i = N.q + if N.high i then 1 else 0 := fun i => by
    rw [N.a_eq]
    split_ifs <;> omega
  simp_rw [h]
  rw [Finset.sum_add_distrib, Finset.sum_const, Finset.card_range, smul_eq_mul]
  rfl

/-! #### Part 3: the instance on words and C004 §3's forward direction -/

theorem rotate_ne_nil {w : List ℕ} (hw : w ≠ []) (i : ℕ) : w.rotate i ≠ [] :=
  fun h => hw (List.rotate_eq_nil_iff.mp h)

/-- The first letter of `w.rotate i`, for `i < w.length`, is `w[i]`. -/
theorem headD_rotate (w : List ℕ) {i : ℕ} (hi : i < w.length) :
    (w.rotate i).headD 0 = w[i] := by
  rw [List.rotate_eq_drop_append_take_mod, Nat.mod_eq_of_lt hi, List.drop_eq_getElem_cons hi,
    List.cons_append, List.headD_cons]

/-- The narrow-cycle data of a word `w` with `D_w > 0` that starts at its minimum and is narrow
(`H < 2L`): states `C(w.rotate i)`, letters the first letters of the rotations, images
`3 C(w.rotate i) + D_w` (constant offset), `lo = C_w`, and an exponent `q` with
`2^q C_w ≤ 3 C_w + D_w < 2^{q+1} C_w`. -/
def ofWord (w : List ℕ) (hm : 0 < w.length) (hD : 0 < D w)
    (hmin : ∀ i, C w ≤ C (w.rotate i)) (hnarrow : ∀ i, C (w.rotate i) < 2 * C w) (q : ℕ)
    (hq1 : (2 : ℤ) ^ q * C w ≤ 3 * C w + D w) (hq2 : 3 * C w + D w < 2 ^ (q + 1) * C w) :
    NarrowCycle w.length where
  x i := C (w.rotate i)
  a i := (w.rotate i).headD 0
  F i := 3 * C (w.rotate i) + D w
  lo := C w
  q := q
  hm := hm
  periodic i := by
    show C (w.rotate (i + w.length)) = C (w.rotate i)
    rw [← List.rotate_mod w (i + w.length), Nat.add_mod_right, List.rotate_mod]
  arrow i := by
    show (2 : ℤ) ^ (w.rotate i).headD 0 * C (w.rotate (i + 1)) = 3 * C (w.rotate i) + D w
    obtain ⟨a, v, h⟩ :=
      List.exists_cons_of_ne_nil (rotate_ne_nil (List.ne_nil_of_length_pos hm) i)
    have ha : (w.rotate i).headD 0 = a := by rw [h, List.headD_cons]
    rw [ha]
    exact C_rotate_succ h
  lower := hmin
  upper := hnarrow
  order i j := by
    show C (w.rotate i) < C (w.rotate j) ↔ 3 * C (w.rotate i) + D w < 3 * C (w.rotate j) + D w
    constructor <;> intro h <;> linarith
  window i j := by
    show 3 * C (w.rotate i) + D w < 2 * (3 * C (w.rotate j) + D w)
    have h1 := hnarrow i
    have h2 := hmin j
    linarith
  hq1 i := by
    show (2 : ℤ) ^ q * C w ≤ 3 * C (w.rotate i) + D w
    have := hmin i
    linarith
  hq2 i := by
    show 3 * C (w.rotate i) + D w < 2 ^ (q + 2) * C w
    have h1 := hnarrow i
    have h3 : (2 : ℤ) ^ (q + 2) * C w = 2 * (2 ^ (q + 1) * C w) := by ring
    rw [h3]
    linarith

/-- **C004 §3, forward direction, for a word starting at its minimum.** A word `w` of length
`m ≥ 2` with `D_w > 0` whose `m` rotations have distinct intercepts, all in `[C_w, 2 C_w)`, is
the mechanical word of its own total: `w = mech w.sum m 0`, and `gcd(w.sum, m) = 1`. -/
theorem eq_mech_of_narrow (w : List ℕ) (hm2 : 2 ≤ w.length) (hD : 0 < D w)
    (hmin : ∀ i, C w ≤ C (w.rotate i)) (hnarrow : ∀ i, C (w.rotate i) < 2 * C w)
    (hdist : ∀ i j, i < w.length → j < w.length → C (w.rotate i) = C (w.rotate j) → i = j) :
    w = mech w.sum w.length 0 ∧ Nat.Coprime w.sum w.length := by
  have hm0 : 0 < w.length := by omega
  have hne : w ≠ [] := List.ne_nil_of_length_pos hm0
  obtain ⟨q, hq1, hq2⟩ := exists_exponent (C_pos hne) hD
  set N : NarrowCycle w.length := ofWord w hm0 hD hmin hnarrow q hq1 hq2 with hN
  have hx : ∀ i, N.x i = C (w.rotate i) := fun _ => rfl
  have ha : ∀ i, N.a i = (w.rotate i).headD 0 := fun _ => rfl
  have hq : N.q = q := rfl
  have hp : N.Primitive := by
    unfold NarrowCycle.Primitive
    intro i j hi hj h
    exact hdist i j hi hj h
  have hh := N.numHigh_lt hp hm2
  have h0 : N.rank 0 = 0 := by
    unfold NarrowCycle.rank
    apply Finset.sum_eq_zero
    intro j _
    rw [hx, hx, List.rotate_zero]
    exact ite_eq_right (not_lt.mpr (hmin j))
  have hlet : ∀ i, (hi : i < w.length) →
      w[i] = q + (((i + 1) * N.numHigh) / w.length - (i * N.numHigh) / w.length) := by
    intro i hi
    rw [← headD_rotate w hi, ← ha, N.a_formula hh h0 i, hq]
  have hw : w = mech (w.length * q + N.numHigh) w.length 0 := by
    apply List.ext_getElem
    · simp [mech_length]
    · intro i hi _
      rw [hlet i hi]
      simp only [mech, diffWord, List.getElem_map, List.getElem_range, add_zero]
      have e1 : (i + 1) * (w.length * q + N.numHigh)
          = (i + 1) * N.numHigh + w.length * (q * (i + 1)) := by ring
      have e2 : i * (w.length * q + N.numHigh) = i * N.numHigh + w.length * (q * i) := by ring
      rw [e1, e2, Nat.add_mul_div_left _ _ hm0, Nat.add_mul_div_left _ _ hm0]
      have hmono : (i * N.numHigh) / w.length ≤ ((i + 1) * N.numHigh) / w.length :=
        Nat.div_le_div_right (Nat.mul_le_mul_right _ (Nat.le_succ i))
      rw [Nat.mul_add, Nat.mul_one]
      omega
  have hsum : w.sum = w.length * q + N.numHigh := by
    conv_lhs => rw [hw]
    exact mech_sum hm0 _ _ hm0
  refine ⟨?_, ?_⟩
  · rw [hsum]
    exact hw
  · rw [hsum]
    exact (Nat.coprime_mul_left_add_left N.numHigh w.length q).mpr (N.coprime_numHigh hp hm2)

/-- **C004 §3, forward direction (narrow ⇒ mechanical).** A word `w` of length `m ≥ 2` with
`D_w > 0`, whose `m` rotations have distinct intercepts (a primitive cycle) and which is narrow —
every rotated intercept is below twice every other, i.e. `H < 2L` — is a phase of the
mechanical word of its total: `w = mech w.sum m l` for some `l < m`, and `gcd(w.sum, m) = 1`.
Together with `narrow_mech` this is C004's narrow-cycle equivalence. -/
theorem is_mech_of_narrow (w : List ℕ) (hm2 : 2 ≤ w.length) (hD : 0 < D w)
    (hnarrow : ∀ i j, C (w.rotate i) < 2 * C (w.rotate j))
    (hdist : ∀ i j, i < w.length → j < w.length → C (w.rotate i) = C (w.rotate j) → i = j) :
    ∃ l < w.length, w = mech w.sum w.length l ∧ Nat.Coprime w.sum w.length := by
  have hm0 : 0 < w.length := by omega
  obtain ⟨i₀, hi₀, hmin₀⟩ := Finset.exists_min_image (Finset.range w.length)
    (fun i => C (w.rotate i)) ⟨0, Finset.mem_range.mpr hm0⟩
  rw [Finset.mem_range] at hi₀
  set w' := w.rotate i₀ with hw'
  have hlen : w'.length = w.length := List.length_rotate w i₀
  have hrot : ∀ j, w'.rotate j = w.rotate (i₀ + j) := fun j => List.rotate_rotate w i₀ j
  have hmin : ∀ j, C w' ≤ C (w'.rotate j) := by
    intro j
    rw [hrot, ← List.rotate_mod w (i₀ + j)]
    exact hmin₀ _ (Finset.mem_range.mpr (Nat.mod_lt _ hm0))
  have hnar : ∀ j, C (w'.rotate j) < 2 * C w' := fun j => by
    rw [hrot]
    exact hnarrow _ _
  have hdist' : ∀ i j, i < w'.length → j < w'.length →
      C (w'.rotate i) = C (w'.rotate j) → i = j := by
    intro i j hi hj h
    rw [hlen] at hi hj
    rw [hrot, hrot, ← List.rotate_mod w (i₀ + i), ← List.rotate_mod w (i₀ + j)] at h
    have h1 := hdist _ _ (Nat.mod_lt _ hm0) (Nat.mod_lt _ hm0) h
    have h2 : i % w.length = j % w.length := Nat.ModEq.add_left_cancel' i₀ h1
    rwa [Nat.mod_eq_of_lt hi, Nat.mod_eq_of_lt hj] at h2
  have hD' : 0 < D w' := by
    rw [hw', D_rotate]
    exact hD
  have hm2' : 2 ≤ w'.length := by
    rw [hlen]
    exact hm2
  obtain ⟨hmech, hcop⟩ := eq_mech_of_narrow w' hm2' hD' hmin hnar hdist'
  have hsum : w'.sum = w.sum := (List.rotate_perm w i₀).sum_eq
  rw [hlen, hsum] at hmech hcop
  have hback : w = w'.rotate (w.length - i₀) := by
    rw [hrot, Nat.add_sub_of_le hi₀.le, List.rotate_length]
  refine ⟨(0 + (w.length - i₀) * w.sum) % w.length, Nat.mod_lt _ hm0, ?_, hcop⟩
  conv_lhs => rw [hback]
  rw [hmech, mech_rotate hm0]

/-! #### Part 4: states indexed by rank (C006 §3's sorted order `z_[r]`, its extension
`z_[r+m] = 2 z_[r]` and the sorted gaps) -/

theorem rank_congr {i j : ℕ} (h : N.x i = N.x j) : N.rank i = N.rank j := by
  unfold rank
  simp only [h]

/-- On a primitive cycle the rank is onto `{0, …, m−1}`. -/
theorem exists_rank_eq (hp : N.Primitive) {r : ℕ} (hr : r < m) :
    ∃ i, i < m ∧ N.rank i = r := by
  have hsurj := Finset.surj_on_of_inj_on_of_card_le (s := Finset.range m)
    (t := Finset.range m) (fun i _ => N.rank i)
    (fun i _ => Finset.mem_range.mpr (N.rank_lt i))
    (fun i j hi hj h => N.rank_inj hp (Finset.mem_range.mp hi) (Finset.mem_range.mp hj) h)
    le_rfl
  obtain ⟨i, hi, hri⟩ := hsurj r (Finset.mem_range.mpr hr)
  exact ⟨i, Finset.mem_range.mp hi, hri.symm⟩

open Classical in
/-- The index below `m` of the state of rank `r` (on a primitive cycle). -/
noncomputable def idx (r : ℕ) : ℕ :=
  if h : ∃ i, i < m ∧ N.rank i = r then Classical.choose h else 0

theorem idx_spec (hp : N.Primitive) {r : ℕ} (hr : r < m) :
    N.idx r < m ∧ N.rank (N.idx r) = r := by
  have h := N.exists_rank_eq hp hr
  unfold idx
  rw [dite_eq_left h]
  exact Classical.choose_spec h

/-- The state of rank `r`: C006's sorted `z_[r]`. -/
noncomputable def y (r : ℕ) : ℤ := N.x (N.idx r)

/-- The sorted states increase strictly with the rank. -/
theorem y_lt_y (hp : N.Primitive) {r r' : ℕ} (hrr : r < r') (hr' : r' < m) : N.y r < N.y r' := by
  have h1 := N.idx_spec hp (lt_trans hrr hr')
  have h2 := N.idx_spec hp hr'
  unfold y
  rcases lt_trichotomy (N.x (N.idx r)) (N.x (N.idx r')) with h | h | h
  · exact h
  · exfalso
    have := N.rank_congr h
    rw [h1.2, h2.2] at this
    omega
  · exfalso
    have := N.rank_lt_of_lt h2.1 h
    rw [h1.2, h2.2] at this
    omega

theorem idx_zero (hp : N.Primitive) (h0 : N.rank 0 = 0) : N.idx 0 = 0 := by
  have h := N.idx_spec hp N.hm
  exact N.rank_inj hp h.1 N.hm (h.2.trans h0.symm)

theorem y_zero (hp : N.Primitive) (h0 : N.rank 0 = 0) : N.y 0 = N.x 0 := by
  unfold y
  rw [N.idx_zero hp h0]

/-- The extension over one more period: `yext r = y r` for `r < m` and `2 y (r − m)` beyond,
so `yext m = 2 y 0` (C006's seam). -/
noncomputable def yext (r : ℕ) : ℤ := if r < m then N.y r else 2 * N.y (r - m)

/-- The sorted gaps `Δ_r = z_[r+1] − z_[r]`, with the seam gap `2 z_[0] − z_[m−1]` at `r = m−1`. -/
noncomputable def gap (r : ℕ) : ℤ := N.yext (r + 1) - N.yext r

theorem yext_of_lt {r : ℕ} (hr : r < m) : N.yext r = N.y r := by
  unfold yext
  rw [ite_eq_left hr]

theorem yext_m : N.yext m = 2 * N.y 0 := by
  unfold yext
  rw [ite_eq_right (lt_irrefl m), Nat.sub_self]

/-- Every gap is positive (the states are distinct and below `2 lo ≤ 2 z_[0]`). -/
theorem gap_pos (hp : N.Primitive) (h0 : N.rank 0 = 0) {r : ℕ} (hr : r < m) : 0 < N.gap r := by
  unfold gap
  rcases Nat.lt_or_ge (r + 1) m with hlt | hge
  · rw [N.yext_of_lt hlt, N.yext_of_lt hr]
    linarith [N.y_lt_y hp (Nat.lt_succ_self r) hlt]
  · have hr1 : r + 1 = m := le_antisymm hr hge
    rw [hr1, N.yext_m, N.yext_of_lt hr]
    have h1 : N.y r < 2 * N.lo := N.upper _
    have h2 : N.lo ≤ N.x 0 := N.lower 0
    rw [N.y_zero hp h0]
    linarith

/-- The gaps over one period sum to `z_[m] − z_[0] = z_[0]`, the minimum. -/
theorem sum_gap (hp : N.Primitive) (h0 : N.rank 0 = 0) :
    ∑ r ∈ Finset.range m, N.gap r = N.x 0 := by
  unfold gap
  rw [Finset.sum_range_sub N.yext m, N.yext_m, N.yext_of_lt N.hm, N.y_zero hp h0]
  ring

/-- Hence each gap is below the minimum when `m ≥ 2` (C006's `G_start < 2^B L` after scaling). -/
theorem gap_lt (hp : N.Primitive) (h0 : N.rank 0 = 0) (hm2 : 2 ≤ m) {r : ℕ} (hr : r < m) :
    N.gap r < N.x 0 := by
  rw [← N.sum_gap hp h0]
  have hmem : r ∈ Finset.range m := Finset.mem_range.mpr hr
  rw [← Finset.add_sum_erase _ _ hmem]
  have hpos : 0 < ∑ j ∈ (Finset.range m).erase r, N.gap j := by
    apply Finset.sum_pos
    · intro j hj
      exact N.gap_pos hp h0 (Finset.mem_range.mp (Finset.mem_of_mem_erase hj))
    · obtain ⟨j, hj, hjr⟩ : ∃ j, j < m ∧ j ≠ r := by
        rcases Nat.eq_zero_or_pos r with h | h
        · exact ⟨1, by omega, by omega⟩
        · exact ⟨0, by omega, by omega⟩
      exact ⟨j, Finset.mem_erase.mpr ⟨hjr, Finset.mem_range.mpr hj⟩⟩
  linarith

/-- The successor of the state of rank `r` is the state of rank `(r + h) mod m`. -/
theorem x_idx_succ (hp : N.Primitive) (hh : N.numHigh < m) {r : ℕ} (hr : r < m) :
    N.x (N.idx r + 1) = N.y ((r + N.numHigh) % m) := by
  have h1 := N.idx_spec hp hr
  have h2 := N.idx_spec hp (Nat.mod_lt (r + N.numHigh) N.hm)
  have hrk : N.rank (N.idx r + 1) = (r + N.numHigh) % m := by
    rw [N.rank_succ_eq hh, h1.2]
  unfold y
  rw [← N.x_mod (N.idx r + 1)]
  congr 1
  apply N.rank_inj hp (Nat.mod_lt _ N.hm) h2.1
  rw [N.rank_mod, hrk, h2.2]

/-- The state of rank `r` is high exactly when `r ≥ m − h` (the final block of ranks). -/
theorem high_idx_iff (hp : N.Primitive) {r : ℕ} (hr : r < m) :
    N.high (N.idx r) ↔ m - N.numHigh ≤ r := by
  have h := N.idx_spec hp hr
  rw [N.high_iff_rank h.1, h.2]

/-- Prefix sums of the mechanical word: `Σ_{j<i} c_j = ⌊iA/m⌋` with `A = mq + h` (started at
the minimum). -/
theorem sum_a_range (hh : N.numHigh < m) (h0 : N.rank 0 = 0) (i : ℕ) :
    ∑ j ∈ Finset.range i, N.a j = (i * (m * N.q + N.numHigh)) / m := by
  have hf : ∀ j, N.a j = N.q + (((j + 1) * N.numHigh) / m - (j * N.numHigh) / m) :=
    N.a_formula hh h0
  simp_rw [hf]
  rw [Finset.sum_add_distrib, Finset.sum_const, Finset.card_range, smul_eq_mul]
  have hmono : Monotone fun j : ℕ => (j * N.numHigh) / m :=
    fun a b hab => Nat.div_le_div_right (Nat.mul_le_mul_right _ hab)
  rw [Finset.sum_range_tsub hmono i]
  simp only [zero_mul, Nat.zero_div, Nat.sub_zero]
  rw [show i * (m * N.q + N.numHigh) = i * N.numHigh + m * (i * N.q) by ring,
    Nat.add_mul_div_left _ _ N.hm]
  ring

/-! #### Part 5: the gap recurrence in rank coordinates (C006 (7)/(G3)) -/

/-- The image of the state of rank `r`. -/
noncomputable def Fr (r : ℕ) : ℤ := N.F (N.idx r)

/-- Its extension over one more period, `Fext m = 2 Fr 0` (C006's seam `ε_[m] = 2ε_[0]`
together with `z_[m] = 2z_[0]`). -/
noncomputable def Fext (r : ℕ) : ℤ := if r < m then N.Fr r else 2 * N.Fr (r - m)

/-- The exponent at rank `r`: `q` on the low ranks `r < m − h`, `q + 1` on the final `h` ranks
(C006's `1 + 1_{j ≥ m−s}` when `q = 1`). -/
def e (r : ℕ) : ℕ := if m - N.numHigh ≤ r then N.q + 1 else N.q

theorem Fext_of_lt {r : ℕ} (hr : r < m) : N.Fext r = N.Fr r := by
  unfold Fext
  rw [ite_eq_left hr]

theorem Fext_m : N.Fext m = 2 * N.Fr 0 := by
  unfold Fext
  rw [ite_eq_right (lt_irrefl m), Nat.sub_self]

theorem e_eq (hp : N.Primitive) {r : ℕ} (hr : r < m) : N.e r = N.a (N.idx r) := by
  unfold e
  rw [N.a_eq (N.idx r)]
  by_cases h2 : m - N.numHigh ≤ r
  · rw [ite_eq_left h2, ite_eq_left ((N.high_idx_iff hp hr).mpr h2)]
  · rw [ite_eq_right h2, ite_eq_right (fun h3 => h2 ((N.high_idx_iff hp hr).mp h3))]

/-- The arrow at the state of rank `r`: `2^{e_r} z_[(r+h) mod m] = F_[r]`. -/
theorem arrow_rank (hp : N.Primitive) (hh : N.numHigh < m) {r : ℕ} (hr : r < m) :
    (2 : ℤ) ^ N.e r * N.y ((r + N.numHigh) % m) = N.Fr r := by
  rw [N.e_eq hp hr]
  have h1 := N.arrow (N.idx r)
  rw [N.x_idx_succ hp hh hr] at h1
  exact h1

/-- **C006's gap recurrence (G3)** in rank coordinates: `2^{e_r} Δ_{(r+h) mod m} = F_[r+1] − F_[r]`
for every rank `r < m`, the seam `r = m − 1` using the extension `F_[m] = 2F_[0]`,
`z_[m] = 2z_[0]`. -/
theorem gap_recurrence (hp : N.Primitive) (hm2 : 2 ≤ m) {r : ℕ} (hr : r < m) :
    (2 : ℤ) ^ N.e r * N.gap ((r + N.numHigh) % m) = N.Fext (r + 1) - N.Fext r := by
  have hh := N.numHigh_lt hp hm2
  have hpos := N.numHigh_pos hp hm2
  have hA := N.arrow_rank hp hh hr
  rw [N.Fext_of_lt hr]
  rcases Nat.lt_or_ge (r + 1) m with hr1 | hr1
  · have hA' := N.arrow_rank hp hh hr1
    rw [N.Fext_of_lt hr1]
    by_cases hlow : m - N.numHigh ≤ r
    · -- both ranks high: exponents `q + 1`, successor ranks `r + h − m`, `r + h − m + 1`
      have hlow' : m - N.numHigh ≤ r + 1 := le_trans hlow (Nat.le_succ r)
      have he : N.e r = N.q + 1 := by
        unfold e
        rw [ite_eq_left hlow]
      have he' : N.e (r + 1) = N.q + 1 := by
        unfold e
        rw [ite_eq_left hlow']
      have hm1 : (r + N.numHigh) % m = r + N.numHigh - m := by
        rw [Nat.mod_eq_sub_mod (by omega), Nat.mod_eq_of_lt (by omega)]
      have hm2' : (r + 1 + N.numHigh) % m = r + N.numHigh - m + 1 := by
        rw [Nat.mod_eq_sub_mod (by omega), Nat.mod_eq_of_lt (by omega)]
        omega
      rw [he, hm1] at hA
      rw [he', hm2'] at hA'
      rw [hm1, he]
      unfold gap
      rw [N.yext_of_lt (by omega : r + N.numHigh - m + 1 < m),
        N.yext_of_lt (by omega : r + N.numHigh - m < m)]
      linarith
    · rw [not_le] at hlow
      have he : N.e r = N.q := by
        unfold e
        rw [ite_eq_right (not_le.mpr hlow)]
      by_cases hlow' : m - N.numHigh ≤ r + 1
      · -- `r` low, `r + 1` high: successor ranks `m − 1` and `0`, the seam gap
        have he' : N.e (r + 1) = N.q + 1 := by
          unfold e
          rw [ite_eq_left hlow']
        have hm1 : (r + N.numHigh) % m = m - 1 := by
          rw [show r + N.numHigh = m - 1 by omega]
          exact Nat.mod_eq_of_lt (by omega)
        have hm2' : (r + 1 + N.numHigh) % m = 0 := by
          rw [show r + 1 + N.numHigh = m by omega]
          exact Nat.mod_self m
        rw [he, hm1] at hA
        rw [he', hm2', pow_succ] at hA'
        rw [hm1, he]
        unfold gap
        rw [show m - 1 + 1 = m by omega, N.yext_m, N.yext_of_lt (by omega : m - 1 < m)]
        linarith
      · -- both ranks low: exponents `q`, successor ranks `r + h`, `r + h + 1`
        have he' : N.e (r + 1) = N.q := by
          unfold e
          rw [ite_eq_right hlow']
        have hm1 : (r + N.numHigh) % m = r + N.numHigh := Nat.mod_eq_of_lt (by omega)
        have hm2' : (r + 1 + N.numHigh) % m = r + N.numHigh + 1 := by
          rw [show r + 1 + N.numHigh = r + N.numHigh + 1 by ring]
          exact Nat.mod_eq_of_lt (by omega)
        rw [he, hm1] at hA
        rw [he', hm2'] at hA'
        rw [hm1, he]
        unfold gap
        rw [N.yext_of_lt (by omega : r + N.numHigh + 1 < m),
          N.yext_of_lt (by omega : r + N.numHigh < m)]
        linarith
  · -- the seam `r = m − 1` (high): successor rank `h − 1`; the next image is `2F_[0]`
    have hlow : m - N.numHigh ≤ r := by omega
    have he : N.e r = N.q + 1 := by
      unfold e
      rw [ite_eq_left hlow]
    have hA0 := N.arrow_rank hp hh N.hm
    have he0 : N.e 0 = N.q := by
      unfold e
      rw [ite_eq_right (by omega)]
    have hm0 : (0 + N.numHigh) % m = N.numHigh := by
      rw [Nat.zero_add]
      exact Nat.mod_eq_of_lt hh
    rw [he0, hm0] at hA0
    have hm1 : (r + N.numHigh) % m = N.numHigh - 1 := by
      rw [show r + N.numHigh = (N.numHigh - 1) + m by omega, Nat.add_mod_right]
      exact Nat.mod_eq_of_lt (by omega)
    rw [he, pow_succ, hm1] at hA
    rw [show r + 1 = m by omega, N.Fext_m, hm1, he, pow_succ]
    unfold gap
    rw [N.yext_of_lt (by omega : N.numHigh - 1 + 1 < m),
      N.yext_of_lt (by omega : N.numHigh - 1 < m), show N.numHigh - 1 + 1 = N.numHigh by omega]
    linarith

end NarrowCycle

/-! ### C005 `ORDER_THEORY.md` §2: the inversion formula (2) and the three-band observation -/

/-- C005's (2): with normalised states `z_i = n_i/2^h`, `z_j = n_j/2^{h+k}` and offsets `q/2^h`,
`q/2^{h+k}`, the difference of the images `F = 3z + q/2^{height}` is
`(3r − q(2^k − 1))/2^{h+k}` with `r = n_j − 2^k n_i`. -/
theorem inversion_formula (n_i n_j q : ℚ) (h k : ℕ) :
    (3 * (n_j / 2 ^ (h + k)) + q / 2 ^ (h + k)) - (3 * (n_i / 2 ^ h) + q / 2 ^ h)
      = (3 * (n_j - 2 ^ k * n_i) - q * (2 ^ k - 1)) / 2 ^ (h + k) := by
  rw [pow_add]
  field_simp
  ring

/-- C005's three-band observation at `q = 1`: a height gap `k ≤ 2` cannot invert, because
`3r − (2^k − 1) ≥ 0` for `r ≥ 1`, with equality only for `k = 2`, `r = 1`. -/
theorem no_inversion_of_le_two {r : ℤ} {k : ℕ} (hr : 1 ≤ r) (hk : k ≤ 2) :
    0 ≤ 3 * r - (2 ^ k - 1) ∧ (3 * r - (2 ^ k - 1) = 0 → k = 2 ∧ r = 1) := by
  interval_cases k <;> norm_num <;> omega

/-! ### C005 §§1–2 on actual cycles: dyadic heights, scaled normalised states, and the
three-band order at `q = 1` -/

/-- Heights exist: for `0 < L ≤ n` there is `h` with `2^h L ≤ n < 2^{h+1} L`. -/
theorem exists_height {L n : ℤ} (hL : 0 < L) (hn : L ≤ n) :
    ∃ h : ℕ, 2 ^ h * L ≤ n ∧ n < 2 ^ (h + 1) * L := by
  classical
  have hex : ∃ k : ℕ, n < 2 ^ (k + 1) * L := by
    obtain ⟨k, hk⟩ := pow_unbounded_of_one_lt n (by norm_num : (1 : ℤ) < 2)
    refine ⟨k, ?_⟩
    have h1 : (2 : ℤ) ^ k ≤ 2 ^ (k + 1) := pow_le_pow_right₀ (by norm_num) (Nat.le_succ k)
    have h2 : (2 : ℤ) ^ (k + 1) ≤ 2 ^ (k + 1) * L :=
      le_mul_of_one_le_right (by positivity) (by linarith)
    linarith
  refine ⟨Nat.find hex, ?_, Nat.find_spec hex⟩
  rcases Nat.eq_zero_or_pos (Nat.find hex) with h0 | hpos
  · rw [h0, pow_zero, one_mul]; exact hn
  · have hmin := Nat.find_min hex (Nat.sub_lt hpos Nat.one_pos)
    rw [Nat.sub_add_cancel hpos] at hmin
    exact not_lt.mp hmin

/-- `H < 8L` means heights at most `2`. -/
theorem height_le_two {L n : ℤ} {h : ℕ} (hL : 0 < L) (h1 : 2 ^ h * L ≤ n) (h8 : n < 8 * L) :
    h ≤ 2 := by
  by_contra hgt
  rw [not_le] at hgt
  have : (2 : ℤ) ^ 3 ≤ 2 ^ h := pow_le_pow_right₀ (by norm_num) hgt
  nlinarith [mul_le_mul_of_nonneg_right this hL.le]

/-- A power of two times an odd number determines both factors. -/
theorem pow_mul_eq_of_odd {x y : ℤ} {s t : ℕ} (hx : Odd x) (hy : Odd y)
    (h : (2 : ℤ) ^ s * x = 2 ^ t * y) : s = t ∧ x = y := by
  rcases lt_trichotomy s t with hlt | heq | hgt
  · exfalso
    have e : (2 : ℤ) ^ t = 2 ^ s * (2 * 2 ^ (t - s - 1)) := by
      rw [← pow_succ', ← pow_add]
      congr 1
      omega
    rw [e, mul_assoc] at h
    have hx' : x = 2 * 2 ^ (t - s - 1) * y := mul_left_cancel₀ (by positivity) h
    exact (Int.not_even_iff_odd.mpr hx) ⟨2 ^ (t - s - 1) * y, by rw [hx']; ring⟩
  · subst heq
    exact ⟨rfl, mul_left_cancel₀ (by positivity) h⟩
  · exfalso
    have e : (2 : ℤ) ^ s = 2 ^ t * (2 * 2 ^ (s - t - 1)) := by
      rw [← pow_succ', ← pow_add]
      congr 1
      omega
    rw [e, mul_assoc] at h
    have hy' : y = 2 * 2 ^ (s - t - 1) * x := mul_left_cancel₀ (by positivity) h.symm
    exact (Int.not_even_iff_odd.mpr hy) ⟨2 ^ (s - t - 1) * x, by rw [hy']; ring⟩

/-- Two numbers of `[lo, 2 lo)` whose quotient is a power of two are equal. -/
theorem eq_of_pow_mul_eq_in_window {lo x y : ℤ} {s t : ℕ} (hx : lo ≤ x) (hx2 : x < 2 * lo)
    (hy : lo ≤ y) (hy2 : y < 2 * lo) (h : (2 : ℤ) ^ s * x = 2 ^ t * y) : x = y := by
  have hlo : 0 < lo := by linarith
  rcases lt_trichotomy s t with hlt | heq | hgt
  · exfalso
    have e : (2 : ℤ) ^ (s + 1) ≤ 2 ^ t := pow_le_pow_right₀ (by norm_num) hlt
    rw [pow_succ] at e
    have h2s : (0 : ℤ) < 2 ^ s := by positivity
    have h3 : (2 : ℤ) ^ s * (2 * y) ≤ 2 ^ s * x := by
      have := mul_le_mul_of_nonneg_right e (by linarith : (0 : ℤ) ≤ y)
      linarith
    have h4 : 2 * y ≤ x := le_of_mul_le_mul_left h3 h2s
    linarith
  · subst heq
    exact mul_left_cancel₀ (by positivity) h
  · exfalso
    have e : (2 : ℤ) ^ (t + 1) ≤ 2 ^ s := pow_le_pow_right₀ (by norm_num) hgt
    rw [pow_succ] at e
    have h2t : (0 : ℤ) < 2 ^ t := by positivity
    have h3 : (2 : ℤ) ^ t * (2 * x) ≤ 2 ^ t * y := by
      have := mul_le_mul_of_nonneg_right e (by linarith : (0 : ℤ) ≤ x)
      linarith
    have h4 : 2 * x ≤ y := le_of_mul_le_mul_left h3 h2t
    linarith

/-! ### C006 `ORDER_RIGIDITY.md` §3, elementary parts: the zero-forcing run lemma behind (G1)
and the discrete intermediate-value step behind (H1) -/

/-- Binary divisibility along a zero-forcing run: if `2^{e_k} G_{k+1} = 3 G_k` for `k < t`,
then `2^{E_t} G_t = 3^t G_0` with `E_t = Σ_{k<t} e_k`. -/
theorem run_pow_mul (G : ℕ → ℤ) (e : ℕ → ℕ) (t : ℕ)
    (hrun : ∀ k, k < t → (2 : ℤ) ^ e k * G (k + 1) = 3 * G k) :
    (2 : ℤ) ^ (∑ k ∈ Finset.range t, e k) * G t = 3 ^ t * G 0 := by
  induction t with
  | zero => simp
  | succ t ih =>
    have ih' := ih (fun k hk => hrun k (Nat.lt_succ_of_lt hk))
    rw [Finset.sum_range_succ, pow_add, pow_succ]
    calc (2 : ℤ) ^ (∑ k ∈ Finset.range t, e k) * 2 ^ e t * G (t + 1)
        = 2 ^ (∑ k ∈ Finset.range t, e k) * (2 ^ e t * G (t + 1)) := by ring
      _ = 2 ^ (∑ k ∈ Finset.range t, e k) * (3 * G t) := by rw [hrun t (Nat.lt_succ_self t)]
      _ = 3 * (2 ^ (∑ k ∈ Finset.range t, e k) * G t) := by ring
      _ = 3 * (3 ^ t * G 0) := by rw [ih']
      _ = 3 ^ t * 3 * G 0 := by ring

/-- Hence `2^{E_t} ∣ G_0`: "since `G_start` is a positive integer and 2 and 3 are coprime". -/
theorem run_dvd (G : ℕ → ℤ) (e : ℕ → ℕ) (t : ℕ)
    (hrun : ∀ k, k < t → (2 : ℤ) ^ e k * G (k + 1) = 3 * G k) :
    (2 : ℤ) ^ (∑ k ∈ Finset.range t, e k) ∣ G 0 := by
  have h := run_pow_mul G e t hrun
  have h1 : (2 : ℤ) ^ (∑ k ∈ Finset.range t, e k) ∣ 3 ^ t * G 0 := ⟨G t, h.symm⟩
  have hcop : IsCoprime ((2 : ℤ) ^ (∑ k ∈ Finset.range t, e k)) (3 ^ t) :=
    IsCoprime.pow (Int.isCoprime_iff_gcd_eq_one.mpr (by norm_num))
  exact hcop.dvd_of_dvd_mul_left h1

/-- A positive run start is at least `2^{E_t} ≥ 2^t` when every run exponent is positive
(C006's `G_start ≥ 2^{e_run} ≥ 2^t`). -/
theorem run_lower (G : ℕ → ℤ) (e : ℕ → ℕ) (t : ℕ) (hG : 0 < G 0) (he : ∀ k, k < t → 1 ≤ e k)
    (hrun : ∀ k, k < t → (2 : ℤ) ^ e k * G (k + 1) = 3 * G k) :
    (2 : ℤ) ^ t ≤ G 0 := by
  have h1 := Int.le_of_dvd hG (run_dvd G e t hrun)
  have h2 : t ≤ ∑ k ∈ Finset.range t, e k := by
    calc t = ∑ _k ∈ Finset.range t, 1 := by simp
      _ ≤ ∑ k ∈ Finset.range t, e k :=
          Finset.sum_le_sum (fun k hk => he k (Finset.mem_range.mp hk))
  exact le_trans (pow_le_pow_right₀ (by norm_num) h2) h1

/-- A sequence of naturals starting at `0` that rises by at most one per step attains every
value up to any value it attains (C006 (H1): reaching height `B` from `0` visits all heights). -/
theorem exists_eq_of_step_le (f : ℕ → ℕ) (h0 : f 0 = 0) (hstep : ∀ i, f (i + 1) ≤ f i + 1)
    {j b : ℕ} (hb : b ≤ f j) : ∃ i, i ≤ j ∧ f i = b := by
  induction j with
  | zero => exact ⟨0, le_refl 0, by omega⟩
  | succ j ih =>
    rcases Nat.lt_or_ge b (f (j + 1)) with hlt | hge
    · obtain ⟨i, hi, hfi⟩ := ih (by have := hstep j; omega)
      exact ⟨i, Nat.le_succ_of_le hi, hfi⟩
    · exact ⟨j + 1, le_refl _, by omega⟩

/-! ### C008 `INDEPENDENT_MATCHING.md` §1: the cyclicity of `⟨2, 3⟩` -/

/-- C008's cyclicity, abstractly: in a commutative group, if `x^A = y^m` with `gcd(A, m) = 1`,
then `x` and `y` are powers of one element `t` with `t^m = x` and `t^A = y`, so `⟨x, y⟩ = ⟨t⟩`
is cyclic. -/
theorem exists_common_root {G : Type*} [CommGroup G] (x y : G) {A m : ℕ} (hAm : Nat.Coprime A m)
    (h : x ^ A = y ^ m) : ∃ t : G, t ^ m = x ∧ t ^ A = y := by
  obtain ⟨u, v, huv⟩ : ∃ u v : ℤ, u * (m : ℤ) + v * (A : ℤ) = 1 := by
    obtain ⟨u, v, huv⟩ := Nat.isCoprime_iff_coprime.mpr hAm.symm
    exact ⟨u, v, huv⟩
  have hx : x ^ (A : ℤ) = y ^ (m : ℤ) := by
    rw [zpow_natCast, zpow_natCast]
    exact h
  refine ⟨x ^ u * y ^ v, ?_, ?_⟩
  · calc (x ^ u * y ^ v) ^ m = (x ^ u * y ^ v) ^ (m : ℤ) := (zpow_natCast _ _).symm
      _ = x ^ (u * (m : ℤ)) * y ^ (v * (m : ℤ)) := by rw [mul_zpow, ← zpow_mul, ← zpow_mul]
      _ = x ^ (u * (m : ℤ)) * (y ^ (m : ℤ)) ^ v := by rw [mul_comm v, zpow_mul y]
      _ = x ^ (u * (m : ℤ)) * (x ^ (A : ℤ)) ^ v := by rw [hx]
      _ = x ^ (u * (m : ℤ) + v * (A : ℤ)) := by rw [← zpow_mul, ← zpow_add, mul_comm (A : ℤ)]
      _ = x := by rw [huv, zpow_one]
  · calc (x ^ u * y ^ v) ^ A = (x ^ u * y ^ v) ^ (A : ℤ) := (zpow_natCast _ _).symm
      _ = x ^ (u * (A : ℤ)) * y ^ (v * (A : ℤ)) := by rw [mul_zpow, ← zpow_mul, ← zpow_mul]
      _ = (x ^ (A : ℤ)) ^ u * y ^ (v * (A : ℤ)) := by rw [mul_comm u, zpow_mul x]
      _ = (y ^ (m : ℤ)) ^ u * y ^ (v * (A : ℤ)) := by rw [hx]
      _ = y ^ (u * (m : ℤ) + v * (A : ℤ)) := by rw [← zpow_mul, ← zpow_add, mul_comm (m : ℤ)]
      _ = y := by rw [huv, zpow_one]

/-- C008's cyclicity of `⟨2, 3⟩` modulo `N`: if `N ∣ 2^A − 3^m` with `gcd(A, m) = 1` and `N`
coprime to `2` and `3`, the units `2` and `3` of `ZMod N` are powers of one unit `t` with
`t^m = 2`, `t^A = 3`. -/
theorem zmod_common_root {N A m : ℕ} (hN2 : Nat.Coprime 2 N) (hN3 : Nat.Coprime 3 N)
    (hAm : Nat.Coprime A m) (hdvd : (N : ℤ) ∣ (2 : ℤ) ^ A - 3 ^ m) :
    ∃ t : (ZMod N)ˣ, t ^ m = ZMod.unitOfCoprime 2 hN2 ∧ t ^ A = ZMod.unitOfCoprime 3 hN3 := by
  have : NeZero N := ⟨fun h => by subst h; simp at hN2⟩
  apply exists_common_root _ _ hAm
  apply Units.ext
  simp only [Units.val_pow_eq_pow_val, ZMod.coe_unitOfCoprime]
  have h := (ZMod.intCast_zmod_eq_zero_iff_dvd ((2 : ℤ) ^ A - 3 ^ m) N).mpr hdvd
  push_cast at h ⊢
  linear_combination h

/-- An actual odd cycle of the raw `3x+q` map, listed from its minimum `n 0`, with dyadic
heights `h i` (`2^{h_i} n_0 ≤ n_i < 2^{h_i+1} n_0`) bounded by `B`: C005 §1's data. -/
structure OddCycle (m : ℕ) where
  n : ℕ → ℤ
  a : ℕ → ℕ
  h : ℕ → ℕ
  q : ℤ
  B : ℕ
  hm : 0 < m
  hq : 0 < q
  nper : ∀ i, n (i + m) = n i
  nodd : ∀ i, Odd (n i)
  nmin : ∀ i, n 0 ≤ n i
  npos : 0 < n 0
  arrow : ∀ i, (2 : ℤ) ^ a i * n (i + 1) = 3 * n i + q
  hlo : ∀ i, 2 ^ h i * n 0 ≤ n i
  hhi : ∀ i, n i < 2 ^ (h i + 1) * n 0
  hB : ∀ i, h i ≤ B

namespace OddCycle

variable {m : ℕ} (Γ : OddCycle m)

/-- The scaled normalised state `2^{B−h_i} n_i = 2^B z_i`. -/
def Z (i : ℕ) : ℤ := 2 ^ (Γ.B - Γ.h i) * Γ.n i

/-- The scaled image `2^B F_i = 3 Z_i + 2^{B−h_i} q`. -/
def F (i : ℕ) : ℤ := 3 * Γ.Z i + 2 ^ (Γ.B - Γ.h i) * Γ.q

/-- The normalised exponent `c_i = a_i + h_{i+1} − h_i` (C005 (1)). -/
def c (i : ℕ) : ℕ := Γ.a i + Γ.h (i + 1) - Γ.h i

/-- The scaled lower endpoint `2^B L`. -/
def lo : ℤ := 2 ^ Γ.B * Γ.n 0

theorem h_unique {L n : ℤ} {h h' : ℕ} (hL : 0 < L) (h1 : 2 ^ h * L ≤ n)
    (h2 : n < 2 ^ (h + 1) * L) (h1' : 2 ^ h' * L ≤ n) (h2' : n < 2 ^ (h' + 1) * L) : h = h' := by
  by_contra hne
  rcases Nat.lt_or_gt_of_ne hne with hlt | hgt
  · have : (2 : ℤ) ^ (h + 1) ≤ 2 ^ h' := pow_le_pow_right₀ (by norm_num) hlt
    nlinarith [mul_le_mul_of_nonneg_right this hL.le]
  · have : (2 : ℤ) ^ (h' + 1) ≤ 2 ^ h := pow_le_pow_right₀ (by norm_num) hgt
    nlinarith [mul_le_mul_of_nonneg_right this hL.le]

theorem h_zero : Γ.h 0 = 0 := by
  have h1 := Γ.hlo 0
  have hp := Γ.npos
  by_contra hne
  have h2 : (2 : ℤ) ^ 1 ≤ 2 ^ Γ.h 0 :=
    pow_le_pow_right₀ (by norm_num) (Nat.one_le_iff_ne_zero.mpr hne)
  nlinarith [mul_le_mul_of_nonneg_right h2 hp.le]

theorem h_per (i : ℕ) : Γ.h (i + m) = Γ.h i := by
  have h1 := Γ.hlo (i + m)
  have h2 := Γ.hhi (i + m)
  rw [Γ.nper i] at h1 h2
  exact h_unique Γ.npos h1 h2 (Γ.hlo i) (Γ.hhi i)

theorem n_add_mul (k t : ℕ) : Γ.n (k + m * t) = Γ.n k := by
  induction t with
  | zero => simp
  | succ t ih => rw [Nat.mul_succ, ← Nat.add_assoc, Γ.nper, ih]

theorem n_mod (k : ℕ) : Γ.n (k % m) = Γ.n k := by
  conv_rhs => rw [← Nat.mod_add_div k m]
  exact (Γ.n_add_mul _ _).symm

theorem h_mod (k : ℕ) : Γ.h (k % m) = Γ.h k := by
  have h1 := Γ.hlo k
  have h2 := Γ.hhi k
  rw [← Γ.n_mod k] at h1 h2
  exact h_unique Γ.npos (Γ.hlo (k % m)) (Γ.hhi (k % m)) h1 h2

theorem Z_per (i : ℕ) : Γ.Z (i + m) = Γ.Z i := by
  unfold Z
  rw [Γ.h_per, Γ.nper]

theorem Z_mod (k : ℕ) : Γ.Z (k % m) = Γ.Z k := by
  unfold Z
  rw [Γ.h_mod, Γ.n_mod]

theorem pow_sub_mul {B h : ℕ} (hh : h ≤ B) : (2 : ℤ) ^ (B - h) * 2 ^ h = 2 ^ B := by
  rw [← pow_add, Nat.sub_add_cancel hh]

theorem Z_lower (i : ℕ) : Γ.lo ≤ Γ.Z i := by
  unfold Z lo
  have h1 := Γ.hlo i
  have h2 : (0 : ℤ) < 2 ^ (Γ.B - Γ.h i) := by positivity
  calc (2 : ℤ) ^ Γ.B * Γ.n 0 = 2 ^ (Γ.B - Γ.h i) * (2 ^ Γ.h i * Γ.n 0) := by
        rw [← mul_assoc, pow_sub_mul (Γ.hB i)]
    _ ≤ 2 ^ (Γ.B - Γ.h i) * Γ.n i := mul_le_mul_of_nonneg_left h1 h2.le

theorem Z_upper (i : ℕ) : Γ.Z i < 2 * Γ.lo := by
  unfold Z lo
  have h2 := Γ.hhi i
  have hp : (0 : ℤ) < 2 ^ (Γ.B - Γ.h i) := by positivity
  have e := pow_sub_mul (Γ.hB i)
  calc (2 : ℤ) ^ (Γ.B - Γ.h i) * Γ.n i < 2 ^ (Γ.B - Γ.h i) * (2 ^ (Γ.h i + 1) * Γ.n 0) :=
        mul_lt_mul_of_pos_left h2 hp
    _ = 2 * (2 ^ Γ.B * Γ.n 0) := by
        rw [pow_succ]
        linear_combination (2 * Γ.n 0) * e

theorem Z_zero : Γ.Z 0 = Γ.lo := by
  unfold Z lo
  rw [Γ.h_zero, Nat.sub_zero]

theorem h_le_a_add (i : ℕ) : Γ.h i ≤ Γ.a i + Γ.h (i + 1) := by
  by_contra hlt
  rw [not_le] at hlt
  have h1 := Γ.arrow i
  have h2 := Γ.hhi (i + 1)
  have h3 := Γ.hlo i
  have hp := Γ.npos
  have hq := Γ.hq
  have hpow : (2 : ℤ) ^ (Γ.a i + Γ.h (i + 1) + 1) ≤ 2 ^ Γ.h i :=
    pow_le_pow_right₀ (by norm_num) hlt
  have h4 : (2 : ℤ) ^ Γ.a i * Γ.n (i + 1) < 2 ^ Γ.a i * (2 ^ (Γ.h (i + 1) + 1) * Γ.n 0) :=
    mul_lt_mul_of_pos_left h2 (by positivity)
  have h5 : (2 : ℤ) ^ Γ.a i * (2 ^ (Γ.h (i + 1) + 1) * Γ.n 0)
      = 2 ^ (Γ.a i + Γ.h (i + 1) + 1) * Γ.n 0 := by
    rw [← mul_assoc, ← pow_add, Nat.add_assoc]
  have h6 : (2 : ℤ) ^ (Γ.a i + Γ.h (i + 1) + 1) * Γ.n 0 ≤ 2 ^ Γ.h i * Γ.n 0 :=
    mul_le_mul_of_nonneg_right hpow hp.le
  have h7 : 0 < Γ.n i := lt_of_lt_of_le hp (Γ.nmin i)
  linarith

/-- C005 (1): `2^{c_i} Z_{i+1} = F_i`. -/
theorem c_arrow (i : ℕ) : (2 : ℤ) ^ Γ.c i * Γ.Z (i + 1) = Γ.F i := by
  unfold c F Z
  have h1 := Γ.arrow i
  have hle := Γ.h_le_a_add i
  have hB := Γ.hB (i + 1)
  have hBi := Γ.hB i
  have e : (2 : ℤ) ^ (Γ.a i + Γ.h (i + 1) - Γ.h i) * 2 ^ (Γ.B - Γ.h (i + 1))
      = 2 ^ (Γ.B - Γ.h i) * 2 ^ Γ.a i := by
    rw [← pow_add, ← pow_add]
    congr 1
    omega
  calc (2 : ℤ) ^ (Γ.a i + Γ.h (i + 1) - Γ.h i) * (2 ^ (Γ.B - Γ.h (i + 1)) * Γ.n (i + 1))
      = (2 ^ (Γ.a i + Γ.h (i + 1) - Γ.h i) * 2 ^ (Γ.B - Γ.h (i + 1))) * Γ.n (i + 1) := by ring
    _ = 2 ^ (Γ.B - Γ.h i) * (2 ^ Γ.a i * Γ.n (i + 1)) := by rw [e]; ring
    _ = 2 ^ (Γ.B - Γ.h i) * (3 * Γ.n i + Γ.q) := by rw [h1]
    _ = 3 * (2 ^ (Γ.B - Γ.h i) * Γ.n i) + 2 ^ (Γ.B - Γ.h i) * Γ.q := by ring

/-- Distinct odd numerators give distinct normalised states. -/
theorem Z_inj {i j : ℕ} (h : Γ.Z i = Γ.Z j) : Γ.h i = Γ.h j ∧ Γ.n i = Γ.n j := by
  unfold Z at h
  obtain ⟨h1, h2⟩ := pow_mul_eq_of_odd (Γ.nodd i) (Γ.nodd j) h
  refine ⟨?_, h2⟩
  have := Γ.hB i
  have := Γ.hB j
  omega

/-- C005 (2) in scaled form, for `h_i ≤ h_j`, `k = h_j − h_i`, `r = n_j − 2^k n_i`:
`F_j − F_i = 2^{B−h_j} (3r − q(2^k − 1))`. -/
theorem F_sub_of_le {i j : ℕ} (hij : Γ.h i ≤ Γ.h j) :
    Γ.F j - Γ.F i = 2 ^ (Γ.B - Γ.h j)
      * (3 * (Γ.n j - 2 ^ (Γ.h j - Γ.h i) * Γ.n i) - Γ.q * (2 ^ (Γ.h j - Γ.h i) - 1)) := by
  unfold F Z
  have e : (2 : ℤ) ^ (Γ.B - Γ.h i) = 2 ^ (Γ.B - Γ.h j) * 2 ^ (Γ.h j - Γ.h i) := by
    rw [← pow_add]
    congr 1
    have := Γ.hB j
    omega
  rw [e]
  ring

theorem Z_sub_of_le {i j : ℕ} (hij : Γ.h i ≤ Γ.h j) :
    Γ.Z j - Γ.Z i = 2 ^ (Γ.B - Γ.h j) * (Γ.n j - 2 ^ (Γ.h j - Γ.h i) * Γ.n i) := by
  unfold Z
  have e : (2 : ℤ) ^ (Γ.B - Γ.h i) = 2 ^ (Γ.B - Γ.h j) * 2 ^ (Γ.h j - Γ.h i) := by
    rw [← pow_add]
    congr 1
    have := Γ.hB j
    omega
  rw [e]
  ring

/-- The equality case of (2) is excluded in a primitive cycle: equal images give equal
normalised successors, hence equal states. -/
theorem Z_eq_of_F_eq (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j) {i j : ℕ}
    (h : Γ.F i = Γ.F j) : Γ.Z i = Γ.Z j := by
  rw [← Γ.c_arrow i, ← Γ.c_arrow j] at h
  have hZ : Γ.Z (i + 1) = Γ.Z (j + 1) :=
    eq_of_pow_mul_eq_in_window (Γ.Z_lower _) (Γ.Z_upper _) (Γ.Z_lower _) (Γ.Z_upper _) h
  have hn : Γ.n ((i + 1) % m) = Γ.n ((j + 1) % m) := by
    rw [Γ.n_mod, Γ.n_mod]
    exact (Γ.Z_inj hZ).2
  have hij := hprim _ _ (Nat.mod_lt _ Γ.hm) (Nat.mod_lt _ Γ.hm) hn
  have hmod : i % m = j % m := Nat.ModEq.add_right_cancel' 1 hij
  rw [← Γ.Z_mod i, ← Γ.Z_mod j, hmod]

/-- **C005 §2, the three-band order at `q = 1`:** with all heights at most `2` (`H < 8L`), the
images increase with the normalised states. -/
theorem F_lt_of_Z_lt (hq1 : Γ.q = 1) (hB2 : Γ.B ≤ 2)
    (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j) {i j : ℕ} (hZ : Γ.Z i < Γ.Z j) :
    Γ.F i < Γ.F j := by
  rcases Nat.lt_or_ge (Γ.h i) (Γ.h j) with hlt | hle
  · have hk : Γ.h j - Γ.h i ≤ 2 := by
      have := Γ.hB j
      omega
    have hsub := Γ.F_sub_of_le hlt.le
    have hZs := Γ.Z_sub_of_le hlt.le
    set r := Γ.n j - 2 ^ (Γ.h j - Γ.h i) * Γ.n i with hr
    have hpos : (0 : ℤ) < 2 ^ (Γ.B - Γ.h j) := by positivity
    have hr0 : 0 < r := by
      have hprod : 0 < 2 ^ (Γ.B - Γ.h j) * r := by
        rw [← hZs]
        linarith
      by_contra hneg
      rw [not_lt] at hneg
      nlinarith
    have hr1 : 1 ≤ r := by linarith
    obtain ⟨hnn, _⟩ := no_inversion_of_le_two hr1 hk
    rw [hq1] at hsub
    rcases lt_or_eq_of_le hnn with hgt | heq0
    · have hin : (0 : ℤ) < 3 * r - 1 * (2 ^ (Γ.h j - Γ.h i) - 1) := by linarith
      have := mul_pos hpos hin
      linarith
    · exfalso
      have hFeq : Γ.F i = Γ.F j := by
        have hz : (3 : ℤ) * r - 1 * (2 ^ (Γ.h j - Γ.h i) - 1) = 0 := by linarith
        rw [hz, mul_zero] at hsub
        linarith
      have := Γ.Z_eq_of_F_eq hprim hFeq
      linarith
  · have e1 : (2 : ℤ) ^ (Γ.B - Γ.h i) ≤ 2 ^ (Γ.B - Γ.h j) :=
      pow_le_pow_right₀ (by norm_num) (by have := Γ.hB i; have := Γ.hB j; omega)
    have hq := Γ.hq
    unfold F
    nlinarith [mul_le_mul_of_nonneg_right e1 hq.le]

theorem order_of_three_band (hq1 : Γ.q = 1) (hB2 : Γ.B ≤ 2)
    (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j) (i j : ℕ) :
    Γ.Z i < Γ.Z j ↔ Γ.F i < Γ.F j := by
  constructor
  · exact Γ.F_lt_of_Z_lt hq1 hB2 hprim
  · intro hF
    rcases lt_trichotomy (Γ.Z i) (Γ.Z j) with h | h | h
    · exact h
    · exfalso
      obtain ⟨hh, hn⟩ := Γ.Z_inj h
      have : Γ.F i = Γ.F j := by
        unfold F Z
        rw [hh, hn]
      linarith
    · exfalso
      have := Γ.F_lt_of_Z_lt hq1 hB2 hprim h
      linarith

theorem F_zero : Γ.F 0 = 3 * Γ.lo + 2 ^ Γ.B * Γ.q := by
  unfold F
  rw [Γ.Z_zero, Γ.h_zero, Nat.sub_zero]

theorem F_lt_two_F_zero (i : ℕ) : Γ.F i < 2 * Γ.F 0 := by
  rw [Γ.F_zero]
  unfold F
  have h1 := Γ.Z_upper i
  have h2 : (2 : ℤ) ^ (Γ.B - Γ.h i) ≤ 2 ^ Γ.B :=
    pow_le_pow_right₀ (by norm_num) (Nat.sub_le _ _)
  have hq := Γ.hq
  have hB : (0 : ℤ) < 2 ^ Γ.B := by positivity
  nlinarith [mul_le_mul_of_nonneg_right h2 hq.le]

theorem F_zero_le (hord : ∀ i j, Γ.Z i < Γ.Z j ↔ Γ.F i < Γ.F j) (j : ℕ) : Γ.F 0 ≤ Γ.F j := by
  by_contra hlt
  rw [not_le] at hlt
  have := (hord j 0).mpr hlt
  rw [Γ.Z_zero] at this
  linarith [Γ.Z_lower j]

/-- An ordered actual cycle gives a `NarrowCycle` on its scaled normalised states, with
exponents `c_i`, images `2^B F_i` and `lo = 2^B L` (C005 §§1–2). -/
def toNarrow (hord : ∀ i j, Γ.Z i < Γ.Z j ↔ Γ.F i < Γ.F j) (q' : ℕ)
    (hq1 : (2 : ℤ) ^ q' * Γ.lo ≤ Γ.F 0) (hq2 : Γ.F 0 < 2 ^ (q' + 1) * Γ.lo) : NarrowCycle m where
  x := Γ.Z
  a := Γ.c
  F := Γ.F
  lo := Γ.lo
  q := q'
  hm := Γ.hm
  periodic := Γ.Z_per
  arrow := Γ.c_arrow
  lower := Γ.Z_lower
  upper := Γ.Z_upper
  order := hord
  window i j := by
    have h1 := Γ.F_lt_two_F_zero i
    have h2 := Γ.F_zero_le hord j
    linarith
  hq1 i := le_trans hq1 (Γ.F_zero_le hord i)
  hq2 i := by
    have h1 := Γ.F_lt_two_F_zero i
    have h3 : (2 : ℤ) ^ (q' + 2) * Γ.lo = 2 * (2 ^ (q' + 1) * Γ.lo) := by ring
    rw [h3]
    linarith

/-- The normalised and original totals agree over a period: `Σ c_i = Σ a_i` (the height
coboundary telescopes). -/
theorem sum_c : ∑ i ∈ Finset.range m, Γ.c i = ∑ i ∈ Finset.range m, Γ.a i := by
  have hshift : ∑ i ∈ Finset.range m, Γ.h (i + 1) = ∑ i ∈ Finset.range m, Γ.h i :=
    NarrowCycle.sum_range_shift Γ.h (by simpa using Γ.h_per 0)
  have hc : ∀ i ∈ Finset.range m, Γ.c i + Γ.h i = Γ.a i + Γ.h (i + 1) := fun i _ => by
    unfold c
    have := Γ.h_le_a_add i
    omega
  have := Finset.sum_congr rfl hc
  rw [Finset.sum_add_distrib, Finset.sum_add_distrib, hshift] at this
  omega

/-- **C005 §2, the three-band restriction at `q = 1`.** A primitive odd cycle of the `3x+1`
map with `m ≥ 2` and all dyadic heights at most `2` (`H < 8L`) has mechanical normalised
exponents: there are `q'` and `h'` coprime to `m` with `c_i = q' + ⌊(i+1)h'/m⌋ − ⌊ih'/m⌋`,
and the total `A = Σ a_i = Σ c_i = mq' + h'` is coprime to `m`. -/
theorem three_band (hq1 : Γ.q = 1) (hB2 : Γ.B ≤ 2) (hm2 : 2 ≤ m)
    (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j) :
    ∃ q' h' : ℕ, Nat.Coprime h' m ∧ (∀ i, Γ.c i = q' + (((i + 1) * h') / m - (i * h') / m)) ∧
      ∑ i ∈ Finset.range m, Γ.a i = m * q' + h' ∧
      Nat.Coprime (∑ i ∈ Finset.range m, Γ.a i) m := by
  have hord := Γ.order_of_three_band hq1 hB2 hprim
  have hlo : 0 < Γ.lo := by
    unfold lo
    exact mul_pos (by positivity) Γ.npos
  have hd : (0 : ℤ) < 2 ^ Γ.B * Γ.q := mul_pos (by positivity) Γ.hq
  obtain ⟨q', hq1', hq2'⟩ := exists_exponent hlo hd
  rw [← Γ.F_zero] at hq1' hq2'
  set N : NarrowCycle m := Γ.toNarrow hord q' hq1' hq2' with hN
  have hx : ∀ i, N.x i = Γ.Z i := fun _ => rfl
  have ha : ∀ i, N.a i = Γ.c i := fun _ => rfl
  have hq : N.q = q' := rfl
  have hp : N.Primitive := by
    unfold NarrowCycle.Primitive
    intro i j hi hj h
    exact hprim i j hi hj (Γ.Z_inj h).2
  have hh := N.numHigh_lt hp hm2
  have h0 : N.rank 0 = 0 := by
    unfold NarrowCycle.rank
    apply Finset.sum_eq_zero
    intro j _
    rw [hx, hx, Γ.Z_zero]
    exact ite_eq_right (not_lt.mpr (Γ.Z_lower j))
  have hsum : ∑ i ∈ Finset.range m, Γ.a i = m * q' + N.numHigh := by
    rw [← Γ.sum_c]
    have := N.sum_a
    rw [hq] at this
    exact this
  refine ⟨q', N.numHigh, N.coprime_numHigh hp hm2, ?_, hsum, ?_⟩
  · intro i
    rw [← ha, N.a_formula hh h0 i, hq]
  · rw [hsum]
    exact (Nat.coprime_mul_left_add_left _ _ _).mpr (N.coprime_numHigh hp hm2)

/-- **C005's denominator corollary**, contrapositive form: a primitive odd cycle with `m ≥ 2`,
heights at most `2` and `gcd(A, m) > 1` is not a `3x+1` cycle (`q ≠ 1`). -/
theorem q_ne_one_of_not_coprime (hB2 : Γ.B ≤ 2) (hm2 : 2 ≤ m)
    (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j)
    (hg : ¬ Nat.Coprime (∑ i ∈ Finset.range m, Γ.a i) m) : Γ.q ≠ 1 := by
  intro hq1
  obtain ⟨_, _, _, _, _, hcop⟩ := Γ.three_band hq1 hB2 hm2 hprim
  exact hg hcop

/-! #### C007 `HEIGHT_DENOMINATOR.md` §§2–3: the modular lemma and the min–top inequality -/

/-- The prefix sums `P_i = Σ_{j<i} c_j` of the normalised word. -/
def P (i : ℕ) : ℕ := ∑ j ∈ Finset.range i, Γ.c j

/-- C007's modular lemma (2) in integer form: `2^{P_i} Z_i ≡ 3^i Z_0 (mod q)`, i.e.
`z_i ≡ L 3^i 2^{−P_i}` once the powers of two are inverted modulo `q`; the height profile does
not appear. -/
theorem residue_law (i : ℕ) : (2 : ℤ) ^ Γ.P i * Γ.Z i ≡ 3 ^ i * Γ.Z 0 [ZMOD Γ.q] := by
  induction i with
  | zero => simp [P]
  | succ i ih =>
    have harrow := Γ.c_arrow i
    have hP : Γ.P (i + 1) = Γ.P i + Γ.c i := by
      unfold P
      rw [Finset.sum_range_succ]
    rw [hP, pow_add, mul_assoc, harrow]
    unfold F
    have e : (2 : ℤ) ^ Γ.P i * (3 * Γ.Z i + 2 ^ (Γ.B - Γ.h i) * Γ.q)
        = 3 * (2 ^ Γ.P i * Γ.Z i) + Γ.q * (2 ^ Γ.P i * 2 ^ (Γ.B - Γ.h i)) := by ring
    rw [e, pow_succ]
    calc 3 * (2 ^ Γ.P i * Γ.Z i) + Γ.q * (2 ^ Γ.P i * 2 ^ (Γ.B - Γ.h i))
        ≡ 3 * (3 ^ i * Γ.Z 0) + 0 [ZMOD Γ.q] :=
          Int.ModEq.add (Int.ModEq.mul_left 3 ih)
            (Int.modEq_zero_iff_dvd.mpr (dvd_mul_right _ _))
      _ = 3 ^ i * 3 * Γ.Z 0 := by ring

/-- C007's modular lemma: when `3 ∤ q`, no numerator is divisible by `3`. -/
theorem three_not_dvd (hq3 : ¬ (3 : ℤ) ∣ Γ.q) (i : ℕ) : ¬ (3 : ℤ) ∣ Γ.n i := by
  intro h3
  have harrow := Γ.arrow (i + m - 1)
  have hidx : i + m - 1 + 1 = i + m := by
    have := Γ.hm
    omega
  rw [hidx, Γ.nper] at harrow
  have h1 : (3 : ℤ) ∣ 3 * Γ.n (i + m - 1) + Γ.q := by
    rw [← harrow]
    exact dvd_mul_of_dvd_right h3 _
  have h2 := dvd_sub h1 (dvd_mul_right 3 (Γ.n (i + m - 1)))
  rw [add_sub_cancel_left] at h2
  exact hq3 h2

/-- A divisor of `q` coprime to `2` that divides one numerator divides the next. -/
theorem dvd_succ_of_dvd {p : ℤ} (hp : p ∣ Γ.q) (hp2 : IsCoprime p 2) {i : ℕ} (hi : p ∣ Γ.n i) :
    p ∣ Γ.n (i + 1) := by
  have harrow := Γ.arrow i
  have h1 : p ∣ (2 : ℤ) ^ Γ.a i * Γ.n (i + 1) := by
    rw [harrow]
    exact dvd_add (dvd_mul_of_dvd_right hi 3) hp
  exact hp2.pow_right.dvd_of_dvd_mul_left h1

/-- Hence such a divisor divides every numerator: a reduced cycle (numerators with no common
factor) has all numerators coprime to `q` — C007's "every numerator is a unit modulo `6q`",
together with `three_not_dvd` and oddness. -/
theorem dvd_all_of_dvd {p : ℤ} (hp : p ∣ Γ.q) (hp2 : IsCoprime p 2) {i : ℕ} (hi : p ∣ Γ.n i)
    (j : ℕ) : p ∣ Γ.n j := by
  have hk : ∀ k, p ∣ Γ.n (i + k) := by
    intro k
    induction k with
    | zero => simpa using hi
    | succ k ih => exact Γ.dvd_succ_of_dvd hp hp2 ih
  have hle : i ≤ j + m * i := le_trans (Nat.le_mul_of_pos_left i Γ.hm) (Nat.le_add_left _ _)
  have := hk (j + m * i - i)
  rw [Nat.add_sub_of_le hle, Γ.n_add_mul] at this
  exact this

/-- C007's min–top inequality (3): in an ordered cycle every state above the minimum
satisfies `q(2^{h_j} − 1) < 3(n_j − 2^{h_j} n_0)`; at the top band `h_j = B` this is
`3r > q(2^B − 1)` with `r = n_j − 2^B L`. -/
theorem min_top (hord : ∀ i j, Γ.Z i < Γ.Z j ↔ Γ.F i < Γ.F j) {j : ℕ} (hj : Γ.Z 0 < Γ.Z j) :
    Γ.q * (2 ^ Γ.h j - 1) < 3 * (Γ.n j - 2 ^ Γ.h j * Γ.n 0) := by
  have hF := (hord 0 j).mp hj
  have hsub := Γ.F_sub_of_le (i := 0) (j := j) (by rw [Γ.h_zero]; exact Nat.zero_le _)
  rw [Γ.h_zero, Nat.sub_zero] at hsub
  have hpos : (0 : ℤ) < 2 ^ (Γ.B - Γ.h j) := by positivity
  have hprod : 0 < 2 ^ (Γ.B - Γ.h j)
      * (3 * (Γ.n j - 2 ^ Γ.h j * Γ.n 0) - Γ.q * (2 ^ Γ.h j - 1)) := by
    rw [← hsub]
    linarith
  by_contra hneg
  rw [not_lt] at hneg
  have hX : 3 * (Γ.n j - 2 ^ Γ.h j * Γ.n 0) - Γ.q * (2 ^ Γ.h j - 1) ≤ 0 := by linarith
  nlinarith

/-! #### C006 §§1, 3 on actual cycles: `c ≤ 2` under `q ≤ L`, chronological height steps -/

/-- Under `q ≤ L` every normalised exponent is at most `2` (C005 §1, C006 §1). -/
theorem c_le_two (hqL : Γ.q ≤ Γ.n 0) (i : ℕ) : Γ.c i ≤ 2 := by
  by_contra hgt
  rw [not_le] at hgt
  have harrow := Γ.c_arrow i
  have hZ := Γ.Z_lower (i + 1)
  have hZi := Γ.Z_upper i
  have hpow : (2 : ℤ) ^ 3 ≤ 2 ^ Γ.c i := pow_le_pow_right₀ (by norm_num) hgt
  have hlo : 0 < Γ.lo := by
    unfold lo
    exact mul_pos (by positivity) Γ.npos
  have hoff : (2 : ℤ) ^ (Γ.B - Γ.h i) * Γ.q ≤ Γ.lo := by
    unfold lo
    have h1 : (2 : ℤ) ^ (Γ.B - Γ.h i) ≤ 2 ^ Γ.B :=
      pow_le_pow_right₀ (by norm_num) (Nat.sub_le _ _)
    have h2 : (0 : ℤ) ≤ 2 ^ Γ.B := by positivity
    linarith [mul_le_mul_of_nonneg_right h1 Γ.hq.le, mul_le_mul_of_nonneg_left hqL h2]
  have hF : Γ.F i < 7 * Γ.lo := by
    unfold F
    linarith
  have h8 : (8 : ℤ) * Γ.lo ≤ 2 ^ Γ.c i * Γ.Z (i + 1) := by
    have h2c : (0 : ℤ) ≤ 2 ^ Γ.c i := by positivity
    linarith [mul_le_mul_of_nonneg_right hpow hlo.le, mul_le_mul_of_nonneg_left hZ h2c]
  linarith

/-- Chronological heights rise by at most one per odd step when `q ≤ L` and the valuation is
positive (the first half of C006's (H1)). -/
theorem h_succ_le (hqL : Γ.q ≤ Γ.n 0) (i : ℕ) (hai : 1 ≤ Γ.a i) : Γ.h (i + 1) ≤ Γ.h i + 1 := by
  have h1 := Γ.c_le_two hqL i
  have h2 := Γ.h_le_a_add i
  unfold c at h1
  omega

/-- Every height between `0` and an attained height is attained (C006 (H1)): with `q ≤ L` and
positive valuations, reaching height `h_j` from `h_0 = 0` visits all heights `0, …, h_j`. -/
theorem exists_height_eq (hqL : Γ.q ≤ Γ.n 0) (hapos : ∀ i, 1 ≤ Γ.a i) {j b : ℕ}
    (hb : b ≤ Γ.h j) : ∃ i, i ≤ j ∧ Γ.h i = b :=
  exists_eq_of_step_le Γ.h Γ.h_zero (fun i => Γ.h_succ_le hqL i (hapos i)) hb

/-! #### C008 `INDEPENDENT_MATCHING.md` §1 on actual cycles: the cycle identities and the
sorted-rank residue law -/

/-- The prefix totals `A_i = Σ_{j<i} a_j`. -/
def Apre (i : ℕ) : ℕ := ∑ j ∈ Finset.range i, Γ.a j

/-- The prefix intercepts `C_i = Σ_{j<i} 3^{i−1−j} 2^{A_j}`, by `C_{i+1} = 3 C_i + 2^{A_i}`. -/
def Cpre : ℕ → ℤ
  | 0 => 0
  | i + 1 => 3 * Cpre i + 2 ^ Γ.Apre i

theorem Apre_succ (i : ℕ) : Γ.Apre (i + 1) = Γ.Apre i + Γ.a i := by
  unfold Apre
  rw [Finset.sum_range_succ]

/-- The exact prefix identity `2^{A_i} n_i = 3^i n_0 + q C_i`. -/
theorem prefix_identity (i : ℕ) :
    (2 : ℤ) ^ Γ.Apre i * Γ.n i = 3 ^ i * Γ.n 0 + Γ.q * Γ.Cpre i := by
  induction i with
  | zero => simp [Apre, Cpre]
  | succ i ih =>
    rw [Γ.Apre_succ, pow_add]
    simp only [Cpre]
    calc (2 : ℤ) ^ Γ.Apre i * 2 ^ Γ.a i * Γ.n (i + 1)
        = 2 ^ Γ.Apre i * (2 ^ Γ.a i * Γ.n (i + 1)) := by ring
      _ = 2 ^ Γ.Apre i * (3 * Γ.n i + Γ.q) := by rw [Γ.arrow i]
      _ = 3 * (2 ^ Γ.Apre i * Γ.n i) + Γ.q * 2 ^ Γ.Apre i := by ring
      _ = 3 * (3 ^ i * Γ.n 0 + Γ.q * Γ.Cpre i) + Γ.q * 2 ^ Γ.Apre i := by rw [ih]
      _ = 3 ^ (i + 1) * Γ.n 0 + Γ.q * (3 * Γ.Cpre i + 2 ^ Γ.Apre i) := by ring

/-- The cycle identity `(2^A − 3^m) n_0 = q C_m`, `A = Σ_{j<m} a_j` (C005's (4), C006's (2)). -/
theorem cycle_identity : ((2 : ℤ) ^ Γ.Apre m - 3 ^ m) * Γ.n 0 = Γ.q * Γ.Cpre m := by
  have h := Γ.prefix_identity m
  rw [show Γ.n m = Γ.n 0 by simpa using Γ.nper 0] at h
  linarith

/-- For a reduced cycle (`q` coprime to its minimum), `q ∣ 2^A − 3^m`: C008's `Q ∣ D`. -/
theorem q_dvd_D (hcop : IsCoprime Γ.q (Γ.n 0)) : Γ.q ∣ (2 : ℤ) ^ Γ.Apre m - 3 ^ m := by
  have h : Γ.q ∣ ((2 : ℤ) ^ Γ.Apre m - 3 ^ m) * Γ.n 0 := ⟨Γ.Cpre m, Γ.cycle_identity⟩
  exact hcop.dvd_of_dvd_mul_right h

theorem Cpre_succ (i : ℕ) : Γ.Cpre (i + 1) = 3 * Γ.Cpre i + 2 ^ Γ.Apre i := rfl

/-- The prefix intercepts are positive from index `1` on. -/
theorem Cpre_pos (i : ℕ) : 0 < Γ.Cpre (i + 1) := by
  induction i with
  | zero =>
    rw [Γ.Cpre_succ]
    simp only [Cpre]
    positivity
  | succ i ih =>
    rw [Γ.Cpre_succ (i + 1)]
    have h2 : (0 : ℤ) < 2 ^ Γ.Apre (i + 1) := by positivity
    linarith

/-- `D = 2^A − 3^m` is positive for a positive cycle: `D n_0 = q C_m` with `q, C_m, n_0 > 0`. -/
theorem D_pos : 0 < (2 : ℤ) ^ Γ.Apre m - 3 ^ m := by
  have h := Γ.cycle_identity
  have hC : 0 < Γ.Cpre m := by
    have h1 := Γ.Cpre_pos (m - 1)
    have hm := Γ.hm
    rw [show m - 1 + 1 = m by omega] at h1
    exact h1
  have hqC : 0 < Γ.q * Γ.Cpre m := mul_pos Γ.hq hC
  have hn := Γ.npos
  by_contra hD
  rw [not_lt] at hD
  have : ((2 : ℤ) ^ Γ.Apre m - 3 ^ m) * Γ.n 0 ≤ 0 := mul_nonpos_of_nonpos_of_nonneg hD hn.le
  linarith

/-- With positive valuations the additive parameter is odd: `2^{a_0} n_1 = 3 n_0 + q` has an even
left side and `3 n_0` is odd. -/
theorem q_odd (hapos : ∀ i, 1 ≤ Γ.a i) : Odd Γ.q := by
  have harrow := Γ.arrow 0
  have heven : Even (2 ^ Γ.a 0 * Γ.n 1) :=
    even_iff_two_dvd.mpr (dvd_mul_of_dvd_left (dvd_pow_self 2 (by have := hapos 0; omega)) _)
  rw [harrow] at heven
  have h3 : Odd (3 * Γ.n 0) := Int.odd_mul.mpr ⟨⟨1, by norm_num⟩, Γ.nodd 0⟩
  have hne : ¬ Even (3 * Γ.n 0) := Int.not_even_iff_odd.mpr h3
  exact Int.not_even_iff_odd.mp (fun hq => hne ((Int.even_add.mp heven).mpr hq))

theorem toNarrow_primitive (hord : ∀ i j, Γ.Z i < Γ.Z j ↔ Γ.F i < Γ.F j) (q' : ℕ)
    (hq1 : (2 : ℤ) ^ q' * Γ.lo ≤ Γ.F 0) (hq2 : Γ.F 0 < 2 ^ (q' + 1) * Γ.lo)
    (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j) :
    (Γ.toNarrow hord q' hq1 hq2).Primitive := by
  unfold NarrowCycle.Primitive
  intro i j hi hj h
  exact hprim i j hi hj (Γ.Z_inj h).2

theorem toNarrow_rank_zero (hord : ∀ i j, Γ.Z i < Γ.Z j ↔ Γ.F i < Γ.F j) (q' : ℕ)
    (hq1 : (2 : ℤ) ^ q' * Γ.lo ≤ Γ.F 0) (hq2 : Γ.F 0 < 2 ^ (q' + 1) * Γ.lo) :
    (Γ.toNarrow hord q' hq1 hq2).rank 0 = 0 := by
  unfold NarrowCycle.rank
  apply Finset.sum_eq_zero
  intro j _
  show (if Γ.Z j < Γ.Z 0 then 1 else 0) = 0
  rw [Γ.Z_zero]
  exact ite_eq_right (not_lt.mpr (Γ.Z_lower j))

/-- C008's sorted-rank law (R1) in integer form: for an ordered primitive cycle, at time
`i < m` the state has sorted rank `(i h) mod m` and `2^{P_i} z_[rank_i] ≡ 3^i z_[0] (mod q)`,
with `P_i = Σ_{j<i} c_j = ⌊iA/m⌋` (`A = mq' + h`). Dividing by the unit `2^{P_i}` modulo `q`
and substituting `2 = t^m`, `3 = t^A` gives the prose's `z_[j] ≡ L t^j`. -/
theorem sorted_residue_law (hord : ∀ i j, Γ.Z i < Γ.Z j ↔ Γ.F i < Γ.F j) (q' : ℕ)
    (hq1 : (2 : ℤ) ^ q' * Γ.lo ≤ Γ.F 0) (hq2 : Γ.F 0 < 2 ^ (q' + 1) * Γ.lo) (hm2 : 2 ≤ m)
    (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j) {i : ℕ} (hi : i < m) :
    (2 : ℤ) ^ Γ.P i * (Γ.toNarrow hord q' hq1 hq2).y
        ((i * (Γ.toNarrow hord q' hq1 hq2).numHigh) % m)
      ≡ 3 ^ i * Γ.Z 0 [ZMOD Γ.q] ∧
    Γ.P i = (i * (m * q' + (Γ.toNarrow hord q' hq1 hq2).numHigh)) / m := by
  set N := Γ.toNarrow hord q' hq1 hq2 with hN
  have hp : N.Primitive := Γ.toNarrow_primitive hord q' hq1 hq2 hprim
  have h0 : N.rank 0 = 0 := Γ.toNarrow_rank_zero hord q' hq1 hq2
  have hh := N.numHigh_lt hp hm2
  have hx : ∀ j, N.x j = Γ.Z j := fun _ => rfl
  have ha : ∀ j, N.a j = Γ.c j := fun _ => rfl
  have hq : N.q = q' := rfl
  have hyi : N.y ((i * N.numHigh) % m) = Γ.Z i := by
    have hr := N.idx_spec hp (Nat.mod_lt (i * N.numHigh) N.hm)
    have hri : N.rank i = (i * N.numHigh) % m := by
      rw [N.rank_formula hh i, h0, Nat.zero_add]
    unfold NarrowCycle.y
    rw [← hx]
    exact N.x_eq_of_rank_eq hr.1 hi (hr.2.trans hri.symm)
  refine ⟨?_, ?_⟩
  · rw [hyi]
    exact Γ.residue_law i
  · have := N.sum_a_range hh h0 i
    rw [hq] at this
    unfold P
    simp_rw [← ha]
    exact this

end OddCycle

/-! ### C006 §3 on actual cycles: the height term `T_r`, the zero-forcing recurrence and the
per-run bound of the sparse-forcing law -/

/-- **The cyclic pigeonhole behind C006's (G1).** If `J ≥ 1` of the `m` positions of a cycle are
forced, some forced position is followed by `⌈m/J⌉ − 1 = ⌊(m−1)/J⌋` consecutive unforced ones.
Proof: otherwise every forced position is followed within `t = ⌊(m−1)/J⌋` steps by another, and
iterating `J` times from a forced position produces `J + 1` distinct forced positions inside an
arc of length `Jt + 1 ≤ m`. -/
theorem exists_run {m : ℕ} (hm : 0 < m) (forced : ℕ → Prop) [DecidablePred forced]
    (hJ : 0 < ((Finset.range m).filter forced).card) :
    ∃ k₀, k₀ < m ∧ forced k₀ ∧
      ∀ j, j < (m - 1) / ((Finset.range m).filter forced).card →
        ¬ forced ((k₀ + 1 + j) % m) := by
  classical
  by_cases hex : ∃ k₀, k₀ < m ∧ forced k₀ ∧
      ∀ j, j < (m - 1) / ((Finset.range m).filter forced).card →
        ¬ forced ((k₀ + 1 + j) % m)
  · exact hex
  exfalso
  have hstep : ∀ k, k < m → forced k → ∃ d, 1 ≤ d ∧
      d ≤ (m - 1) / ((Finset.range m).filter forced).card ∧ forced ((k + d) % m) := by
    intro k hk hf
    by_contra h2
    apply hex
    refine ⟨k, hk, hf, fun j hj hfj => h2 ⟨j + 1, by omega, by omega, ?_⟩⟩
    rw [show k + (j + 1) = k + 1 + j by ring]
    exact hfj
  choose! d hd using hstep
  obtain ⟨k₀, hk₀⟩ := Finset.card_pos.mp hJ
  have hk₀m : k₀ < m := Finset.mem_range.mp (Finset.mem_filter.mp hk₀).1
  have hk₀f : forced k₀ := (Finset.mem_filter.mp hk₀).2
  let pos : ℕ → ℕ := fun i => Nat.rec (motive := fun _ => ℕ) k₀ (fun _ p => (p + d p) % m) i
  have pos_zero : pos 0 = k₀ := rfl
  have pos_succ : ∀ i, pos (i + 1) = (pos i + d (pos i)) % m := fun _ => rfl
  have pos_prop : ∀ i, pos i < m ∧ forced (pos i) := by
    intro i
    induction i with
    | zero => exact ⟨hk₀m, hk₀f⟩
    | succ i ih =>
      rw [pos_succ]
      exact ⟨Nat.mod_lt _ hm, (hd (pos i) ih.1 ih.2).2.2⟩
  let s : ℕ → ℕ := fun i => ∑ j ∈ Finset.range i, d (pos j)
  have s_succ : ∀ i, s (i + 1) = s i + d (pos i) := fun i => Finset.sum_range_succ _ _
  have pos_eq : ∀ i, pos i = (k₀ + s i) % m := by
    intro i
    induction i with
    | zero =>
      rw [pos_zero]
      simp [s, Nat.mod_eq_of_lt hk₀m]
    | succ i ih =>
      rw [pos_succ, s_succ, ← Nat.add_assoc]
      have hmod : pos i ≡ k₀ + s i [MOD m] := by
        unfold Nat.ModEq
        rw [ih, Nat.mod_mod]
      exact hmod.add_right _
  have s_le : ∀ i, s i ≤ i * ((m - 1) / ((Finset.range m).filter forced).card) := by
    intro i
    induction i with
    | zero => simp [s]
    | succ i ih =>
      rw [s_succ, Nat.add_mul, Nat.one_mul]
      have := (hd (pos i) (pos_prop i).1 (pos_prop i).2).2.1
      omega
  have s_mono : StrictMono s := by
    apply strictMono_nat_of_lt_succ
    intro i
    rw [s_succ]
    have := (hd (pos i) (pos_prop i).1 (pos_prop i).2).1
    omega
  have hJt : ((Finset.range m).filter forced).card
      * ((m - 1) / ((Finset.range m).filter forced).card) ≤ m - 1 :=
    Nat.mul_div_le (m - 1) _
  have hinj : Set.InjOn pos (Finset.range (((Finset.range m).filter forced).card + 1) : Set ℕ) := by
    intro i hi i' hi' h
    simp only [Finset.coe_range, Set.mem_Iio] at hi hi'
    rw [pos_eq, pos_eq] at h
    have hsi : s i < m := by
      have h1 := s_le i
      have h2 : i * ((m - 1) / ((Finset.range m).filter forced).card)
          ≤ ((Finset.range m).filter forced).card
            * ((m - 1) / ((Finset.range m).filter forced).card) :=
        Nat.mul_le_mul_right _ (by omega)
      omega
    have hsi' : s i' < m := by
      have h1 := s_le i'
      have h2 : i' * ((m - 1) / ((Finset.range m).filter forced).card)
          ≤ ((Finset.range m).filter forced).card
            * ((m - 1) / ((Finset.range m).filter forced).card) :=
        Nat.mul_le_mul_right _ (by omega)
      omega
    have hmod : s i ≡ s i' [MOD m] := Nat.ModEq.add_left_cancel' k₀ h
    unfold Nat.ModEq at hmod
    rw [Nat.mod_eq_of_lt hsi, Nat.mod_eq_of_lt hsi'] at hmod
    exact s_mono.injective hmod
  have hmaps : ∀ i ∈ Finset.range (((Finset.range m).filter forced).card + 1),
      pos i ∈ (Finset.range m).filter forced := by
    intro i _
    exact Finset.mem_filter.mpr ⟨Finset.mem_range.mpr (pos_prop i).1, (pos_prop i).2⟩
  have hcard := Finset.card_le_card_of_injOn pos hmaps hinj
  rw [Finset.card_range] at hcard
  omega

/-- Adjacent changes bound the number of distinct values: a sequence on `{0, …, n}` takes at
most `1 + #{r < n : f(r+1) ≠ f r}` distinct values (the counting step of C006's (H1)). -/
theorem card_image_le_changes (f : ℕ → ℕ) (n : ℕ) :
    ((Finset.range (n + 1)).image f).card
      ≤ 1 + ((Finset.range n).filter (fun r => f (r + 1) ≠ f r)).card := by
  induction n with
  | zero => simp
  | succ n ih =>
    conv_lhs => rw [Finset.range_add_one, Finset.image_insert]
    conv_rhs => rw [Finset.range_add_one, Finset.filter_insert]
    by_cases h : f (n + 1) ≠ f n
    · have hn : n ∉ (Finset.range n).filter (fun r => f (r + 1) ≠ f r) := fun hmem =>
        lt_irrefl n (Finset.mem_range.mp (Finset.mem_filter.mp hmem).1)
      rw [ite_eq_left h, Finset.card_insert_of_notMem hn]
      have h1 := Finset.card_insert_le (f (n + 1)) ((Finset.range (n + 1)).image f)
      omega
    · rw [ite_eq_right h]
      have h' : f (n + 1) = f n := not_not.mp h
      have hmem : f (n + 1) ∈ (Finset.range (n + 1)).image f := by
        rw [h']
        exact Finset.mem_image_of_mem f (Finset.mem_range.mpr (Nat.lt_succ_self n))
      rw [Finset.card_insert_of_mem hmem]
      exact ih

/-! ### C009: the one-point deletion theorem for the first-return permutation

C009 (`FIRST_RETURN_ORDER.md`): for the rank shift `R(j) = (j + s) mod m` on `m ≥ 2` ranks with
`1 ≤ s < m`, delete rank `0` and take the first-return map on the retained ranks `1, …, m − 1`
(compressed to `0, …, m − 2`). The induced map is a circular rank shift if and only if `s = 1` or
`s = m − 1`. (The prose also assumes `gcd(s, m) = 1`; it is not needed for this statement. The
deleted rank is `0` without loss of generality, by rotating the circle.) -/

/-- The first-return map on the retained old ranks after deleting rank `0`: one step of
`j ↦ (j + s) mod m`, or two steps when the first lands on the deleted rank. -/
def retMap (m s j : ℕ) : ℕ := if (j + s) % m = 0 then (j + 2 * s) % m else (j + s) % m

/-- The compressed first-return permutation on `{0, …, m − 2}` (old rank `j + 1 ↦` new rank). -/
def compMap (m s j : ℕ) : ℕ := retMap m s (j + 1) - 1

/-- "The induced permutation is a circular rank shift": some `c` with
`compMap j = (j + c) mod (m − 1)` on all compressed ranks. -/
def IsRankShift (m s : ℕ) : Prop := ∃ c, ∀ j, j < m - 1 → compMap m s j = (j + c) % (m - 1)

theorem retMap_of_lt {m s j : ℕ} (h : j + s < m) (h0 : 0 < j + s) : retMap m s j = j + s := by
  unfold retMap
  rw [Nat.mod_eq_of_lt h]
  exact ite_eq_right (by omega)

theorem retMap_of_ge {m s j : ℕ} (h1 : m ≤ j + s) (h2 : j + s < 2 * m) (h0 : j + s ≠ m) :
    retMap m s j = j + s - m := by
  unfold retMap
  have hmod : (j + s) % m = j + s - m := by
    rw [Nat.mod_eq_sub_mod h1]
    exact Nat.mod_eq_of_lt (by omega)
  rw [hmod]
  exact ite_eq_right (by omega)

theorem retMap_of_eq {m s j : ℕ} (h : j + s = m) (hsm : s < m) : retMap m s j = s := by
  unfold retMap
  rw [h, Nat.mod_self, ite_eq_left rfl, show j + 2 * s = s + m by omega, Nat.add_mod_right,
    Nat.mod_eq_of_lt hsm]

/-- **C009's one-point deletion theorem.** For `m ≥ 2` and `1 ≤ s < m`, the compressed
first-return map after deleting one rank is a circular rank shift iff `s = 1` or `s = m − 1`.
For `2 ≤ s ≤ m − 2` the compressed shifts of old ranks `1` and `m − 1` are `s` and `s − 1`,
which differ modulo `m − 1`; for `s = 1` every compressed shift is `1`, for `s = m − 1` it is
`m − 2 ≡ −1`. -/
theorem one_point_deletion (m s : ℕ) (hm : 2 ≤ m) (hs1 : 1 ≤ s) (hsm : s < m) :
    IsRankShift m s ↔ (s = 1 ∨ s = m - 1) := by
  constructor
  · rintro ⟨c, hc⟩
    by_contra hne
    rw [not_or] at hne
    obtain ⟨hne1, hne2⟩ := hne
    have h0 := hc 0 (by omega)
    have h1 := hc (m - 2) (by omega)
    have hc0 : compMap m s 0 = s := by
      unfold compMap
      rw [retMap_of_lt (by omega) (by omega)]
      omega
    have hc1 : compMap m s (m - 2) = s - 2 := by
      unfold compMap
      rw [retMap_of_ge (by omega) (by omega) (by omega)]
      omega
    rw [hc0, zero_add] at h0
    rw [hc1] at h1
    have hcm : c % (m - 1) = s := h0.symm
    have hval : (m - 2 + c) % (m - 1) = s - 1 := by
      rw [Nat.add_mod, hcm, show (m - 2) % (m - 1) = m - 2 from Nat.mod_eq_of_lt (by omega),
        show m - 2 + s = (s - 1) + (m - 1) by omega, Nat.add_mod_right,
        Nat.mod_eq_of_lt (by omega)]
    omega
  · rintro (rfl | rfl)
    · refine ⟨1, fun j hj => ?_⟩
      unfold compMap
      rcases Nat.lt_or_ge (j + 2) m with hlt | hge
      · rw [retMap_of_lt (by omega) (by omega), Nat.mod_eq_of_lt (by omega)]
        omega
      · rw [retMap_of_eq (by omega) (by omega), show j + 1 = m - 1 by omega, Nat.mod_self]
    · refine ⟨m - 2, fun j hj => ?_⟩
      unfold compMap
      rcases Nat.eq_zero_or_pos j with hj0 | hjpos
      · subst hj0
        rw [retMap_of_eq (by omega) (by omega), Nat.zero_add, Nat.mod_eq_of_lt (by omega)]
        omega
      · rw [retMap_of_ge (by omega) (by omega) (by omega),
          show j + (m - 2) = (j - 1) + (m - 1) by omega, Nat.add_mod_right,
          Nat.mod_eq_of_lt (by omega)]
        omega

/-- C009's `q = 13` control in this normalisation: for `m = 5`, `s = 3` (the ordered cycle
`(283, 431, 653, 493, 373)` with the positive-height state deleted) the compressed first-return
map is `(3, 2, 0, 1)` — the prose's `(2, 0, 3, 1)` conjugated by the relabelling that puts the
deleted rank at `0` — and not a rank shift. -/
example : (List.range 4).map (compMap 5 3) = [3, 2, 0, 1] := by decide

example : ¬ IsRankShift 5 3 := by
  rw [one_point_deletion 5 3 (by norm_num) (by norm_num) (by norm_num)]
  omega

/-! ### C011: the two-arc identity and the two-defect cancellation bounds

C011 (`ROTATION_DEFECTS.md` §§2–3) compares a positive word `w` with a rotation `w'` differing from
it in exactly two positions; after cutting at the first mismatch and exchanging the roles if
necessary, `w = a :: (u₀ ++ (a + k) :: v₀)` and `w' = (a + k) :: (u₀ ++ a :: v₀)` with `k ≥ 1`.
With the complementary arcs `u = u₀ ++ [a + k]` and `v = v₀ ++ [a]`, `g = gcd(C_w, D_w)` divides
`(2^k − 1) gcd(C_u, C_v)` (its (2)), and the intercept bound `C_z ≤ 2^{S−l−(b−1)} (3^l − 2^l)`
for a word of length `l`, total `S` and last letter `b` (its (4)) gives
`g² < (2^k − 1)² 2^{A−m−k−2a+2} 3^m` (its (5)) and `g² < 2^{2A−2m} 3^m` (its (7)). Everything is
kept in cleared integer form. The combinatorial reduction of an arbitrary two-defect rotation to
this normal form, the real-analytic (6)–(8) and the imported Matveev/Hercher inputs of
`EXCLUSION.md` are not formalised. -/

/-- The intercept of a word does not depend on its last letter: `C (z ++ [b]) = 3 C_z + 2^{Σz}`. -/
theorem C_append_singleton (z : List ℕ) (b : ℕ) : C (z ++ [b]) = 3 * C z + 2 ^ z.sum := by
  rw [C_append]
  simp [C]

/-- C011's two-arc identity (1): `C_{w'} − C_w = (2^k − 1) 2^a 3^{|v₀|} C_u`, `u = u₀ ++ [a + k]`. -/
theorem two_arc_identity (a k : ℕ) (u₀ v₀ : List ℕ) :
    C ((a + k) :: (u₀ ++ a :: v₀)) - C (a :: (u₀ ++ (a + k) :: v₀))
      = (2 ^ k - 1) * 2 ^ a * 3 ^ v₀.length * C (u₀ ++ [a + k]) := by
  rw [C_append_singleton]
  simp only [C, C_append, List.length_append, List.length_cons, pow_add, pow_succ]
  ring

/-- The cut at the second mismatch is a rotation: rotating `x :: (u₀ ++ y :: v₀)` by `|u₀| + 1`
gives `y :: (v₀ ++ x :: u₀)`. -/
theorem rotate_cut (x y : ℕ) (u₀ v₀ : List ℕ) :
    (x :: (u₀ ++ y :: v₀)).rotate (u₀.length + 1) = y :: (v₀ ++ x :: u₀) := by
  have h1 : x :: (u₀ ++ y :: v₀) = (x :: u₀) ++ (y :: v₀) := by simp
  have h2 : y :: (v₀ ++ x :: u₀) = (y :: v₀) ++ (x :: u₀) := by simp
  rw [h1, h2, show u₀.length + 1 = (x :: u₀).length by simp,
    List.rotate_eq_drop_append_take (by simp), List.drop_left, List.take_left]

/-- `D_w` is coprime to `3` (`3 ∤ D_w`). -/
theorem isCoprime_three_D {w : List ℕ} (hw : 1 ≤ w.length) : IsCoprime (3 : ℤ) (D w) := by
  rw [Int.isCoprime_iff_gcd_eq_one]
  have h1 : Int.gcd 3 (D w) ∣ 3 := by
    have := Int.gcd_dvd_left (3 : ℤ) (D w)
    exact_mod_cast this
  rcases (Nat.dvd_prime Nat.prime_three).mp h1 with h | h
  · exact h
  · exfalso
    apply D_not_three_dvd hw
    have := Int.gcd_dvd_right (3 : ℤ) (D w)
    rw [h] at this
    exact_mod_cast this

/-- Every common divisor `g` of `C_w` and `D_w` that is coprime to `2` divides every rotated
intercept (the recurrence `2^{a_i} C_{(i+1)} = 3 C_{(i)} + D_w`). -/
theorem dvd_C_rotate_of_dvd {w : List ℕ} (hw0 : w ≠ []) {g : ℤ} (hg2 : IsCoprime g 2)
    (hgC : g ∣ C w) (hgD : g ∣ D w) : ∀ i, g ∣ C (w.rotate i) := by
  intro i
  induction i with
  | zero => simpa using hgC
  | succ i ih =>
    obtain ⟨a, v, hav⟩ : ∃ a v, w.rotate i = a :: v := by
      cases hrot : w.rotate i with
      | nil => exact absurd (List.rotate_eq_nil_iff.mp hrot) hw0
      | cons a v => exact ⟨a, v, rfl⟩
    have hrec := C_rotate_succ hav
    have h2 : g ∣ 2 ^ a * C (w.rotate (i + 1)) := by
      rw [hrec]
      exact dvd_add (dvd_mul_of_dvd_right ih 3) hgD
    exact (hg2.pow_right).dvd_of_dvd_mul_left h2

/-- `g = gcd(C_w, D_w)` is coprime to `2` (it divides the odd `D_w`). -/
theorem gcd_isCoprime_two {w : List ℕ} (hw : 1 ≤ w.sum) :
    IsCoprime ((Int.gcd (C w) (D w) : ℕ) : ℤ) 2 :=
  (isCoprime_two_D hw).symm.of_isCoprime_of_dvd_left (Int.gcd_dvd_right _ _)

/-- `g = gcd(C_w, D_w)` is coprime to `3`. -/
theorem gcd_isCoprime_three {w : List ℕ} (hw : 1 ≤ w.length) :
    IsCoprime ((Int.gcd (C w) (D w) : ℕ) : ℤ) 3 :=
  (isCoprime_three_D hw).symm.of_isCoprime_of_dvd_left (Int.gcd_dvd_right _ _)

/-- C011's (2): in the two-defect normal form `w = a :: (u₀ ++ (a + k) :: v₀)` with
`w' = (a + k) :: (u₀ ++ a :: v₀)` a rotation of `w` and `k ≥ 1`, `g = gcd(C_w, D_w)` divides
`(2^k − 1) gcd(C_u, C_v)` for the complementary arcs `u = u₀ ++ [a + k]`, `v = v₀ ++ [a]`. -/
theorem two_arc_dvd (a k : ℕ) (hk : 1 ≤ k) (u₀ v₀ : List ℕ)
    (hrot : ∃ r, (a :: (u₀ ++ (a + k) :: v₀)).rotate r = (a + k) :: (u₀ ++ a :: v₀)) :
    ((Int.gcd (C (a :: (u₀ ++ (a + k) :: v₀))) (D (a :: (u₀ ++ (a + k) :: v₀))) : ℕ) : ℤ)
      ∣ (2 ^ k - 1) * ((Int.gcd (C (u₀ ++ [a + k])) (C (v₀ ++ [a])) : ℕ) : ℤ) := by
  obtain ⟨r, hr⟩ := hrot
  have hw0 : a :: (u₀ ++ (a + k) :: v₀) ≠ [] := List.cons_ne_nil _ _
  have hsum : 1 ≤ (a :: (u₀ ++ (a + k) :: v₀)).sum := by
    simp only [List.sum_cons, List.sum_append]
    omega
  have hlen : 1 ≤ (a :: (u₀ ++ (a + k) :: v₀)).length := by simp
  have hg2 := gcd_isCoprime_two hsum
  have hg3 := gcd_isCoprime_three hlen
  have hgC : ((Int.gcd (C (a :: (u₀ ++ (a + k) :: v₀))) (D (a :: (u₀ ++ (a + k) :: v₀))) : ℕ) : ℤ)
      ∣ C (a :: (u₀ ++ (a + k) :: v₀)) := Int.gcd_dvd_left _ _
  have hgD : ((Int.gcd (C (a :: (u₀ ++ (a + k) :: v₀))) (D (a :: (u₀ ++ (a + k) :: v₀))) : ℕ) : ℤ)
      ∣ D (a :: (u₀ ++ (a + k) :: v₀)) := Int.gcd_dvd_right _ _
  have hrotall := dvd_C_rotate_of_dvd hw0 hg2 hgC hgD
  set g : ℤ :=
    ((Int.gcd (C (a :: (u₀ ++ (a + k) :: v₀))) (D (a :: (u₀ ++ (a + k) :: v₀))) : ℕ) : ℤ) with hg
  -- the first arc
  have hu : g ∣ (2 ^ k - 1) * C (u₀ ++ [a + k]) := by
    have hdiff : g ∣ C ((a + k) :: (u₀ ++ a :: v₀)) - C (a :: (u₀ ++ (a + k) :: v₀)) := by
      have := hrotall r
      rw [hr] at this
      exact dvd_sub this hgC
    rw [two_arc_identity, show (2 ^ k - 1) * 2 ^ a * 3 ^ v₀.length * C (u₀ ++ [a + k])
        = (2 ^ a * 3 ^ v₀.length) * ((2 ^ k - 1) * C (u₀ ++ [a + k])) by ring] at hdiff
    exact ((hg2.pow_right).mul_right (hg3.pow_right)).dvd_of_dvd_mul_left hdiff
  -- the second arc: cut at the other mismatch
  have hv : g ∣ (2 ^ k - 1) * C (v₀ ++ [a]) := by
    have hW : g ∣ C ((a + k) :: (v₀ ++ a :: u₀)) := by
      have := hrotall (u₀.length + 1)
      rwa [rotate_cut] at this
    have hW' : g ∣ C (a :: (v₀ ++ (a + k) :: u₀)) := by
      have := hrotall (r + (u₀.length + 1))
      rwa [← List.rotate_rotate, hr, rotate_cut] at this
    have hdiff := dvd_sub hW hW'
    rw [two_arc_identity, show (2 ^ k - 1) * 2 ^ a * 3 ^ u₀.length * C (v₀ ++ [a + k])
        = (2 ^ a * 3 ^ u₀.length) * ((2 ^ k - 1) * C (v₀ ++ [a + k])) by ring] at hdiff
    have := ((hg2.pow_right).mul_right (hg3.pow_right)).dvd_of_dvd_mul_left hdiff
    rwa [C_append_singleton, ← C_append_singleton v₀ a] at this
  have hX1 : (1 : ℤ) ≤ 2 ^ k := one_le_pow₀ (by norm_num)
  have hX0 : (0 : ℤ) ≤ 2 ^ k - 1 := by linarith
  have hdvd := Int.dvd_gcd hu hv
  rw [Int.gcd_mul_left] at hdvd
  have h' : ((Int.gcd (C (a :: (u₀ ++ (a + k) :: v₀))) (D (a :: (u₀ ++ (a + k) :: v₀))) : ℕ) : ℤ)
      ∣ (((2 ^ k - 1 : ℤ).natAbs * Int.gcd (C (u₀ ++ [a + k])) (C (v₀ ++ [a])) : ℕ) : ℤ) :=
    Int.natCast_dvd_natCast.mpr hdvd
  rw [Nat.cast_mul, Int.natAbs_of_nonneg hX0] at h'
  exact h'

/-- C011's (4) for a word with last letter `b`, in cleared form: `2^{l−1} C_z ≤ 2^{S−b} (3^l − 2^l)`
with `z = z₀ ++ [b]`, `l = |z₀| + 1`, `S − b = Σ z₀` (the last letter does not enter). -/
theorem intercept_bound_last (z₀ : List ℕ) (b : ℕ) (hz : ∀ x ∈ z₀, 1 ≤ x) :
    (2 : ℤ) ^ z₀.length * C (z₀ ++ [b])
      ≤ 2 ^ z₀.sum * (3 ^ (z₀.length + 1) - 2 ^ (z₀.length + 1)) := by
  rw [C_append_singleton]
  have h := two_pow_mul_C_le z₀ hz
  have h3 : (2 : ℤ) ^ z₀.length * (3 * C z₀ + 2 ^ z₀.sum)
      = 3 * (2 ^ z₀.length * C z₀) + 2 ^ z₀.length * 2 ^ z₀.sum := by ring
  rw [h3, pow_succ, pow_succ]
  linarith

/-- The arithmetic of C011's (5): from `G ≤ X H`, `H ≤ C_u, C_v`, the cleared intercept bounds
`P_u C_u ≤ B_u < T_u`, `P_v C_v ≤ B_v < T_v`, one gets `G² P_u P_v < X² T_u T_v`. -/
theorem two_defect_arith {G H X Cu Cv Pu Pv Bu Bv Tu Tv : ℤ} (hG0 : 0 ≤ G) (hX : 0 < X)
    (hH0 : 0 ≤ H) (hGXH : G ≤ X * H) (hHu : H ≤ Cu) (hHv : H ≤ Cv) (hPu : 0 ≤ Pu)
    (hPv : 0 ≤ Pv) (hbu : Pu * Cu ≤ Bu) (hbv : Pv * Cv ≤ Bv) (hBuT : Bu < Tu) (hBvT : Bv < Tv)
    (hTu : 0 < Tu) : G ^ 2 * (Pu * Pv) < X ^ 2 * (Tu * Tv) := by
  have hPuPv : 0 ≤ Pu * Pv := mul_nonneg hPu hPv
  have h1 : G ^ 2 ≤ (X * H) ^ 2 := pow_le_pow_left₀ hG0 hGXH 2
  have hPuH : Pu * H ≤ Bu := le_trans (mul_le_mul_of_nonneg_left hHu hPu) hbu
  have hPvH : Pv * H ≤ Bv := le_trans (mul_le_mul_of_nonneg_left hHv hPv) hbv
  have hPuH0 : 0 ≤ Pu * H := mul_nonneg hPu hH0
  have hPvH0 : 0 ≤ Pv * H := mul_nonneg hPv hH0
  have hBu0 : 0 ≤ Bu := le_trans hPuH0 hPuH
  have hBv0 : 0 ≤ Bv := le_trans hPvH0 hPvH
  have hX2 : 0 < X ^ 2 := pow_pos hX 2
  calc G ^ 2 * (Pu * Pv) ≤ (X * H) ^ 2 * (Pu * Pv) := mul_le_mul_of_nonneg_right h1 hPuPv
    _ = X ^ 2 * ((Pu * H) * (Pv * H)) := by ring
    _ ≤ X ^ 2 * (Bu * Bv) :=
        mul_le_mul_of_nonneg_left (mul_le_mul hPuH hPvH hPvH0 hBu0) hX2.le
    _ < X ^ 2 * (Tu * Tv) := by
        apply mul_lt_mul_of_pos_left _ hX2
        calc Bu * Bv ≤ Tu * Bv := mul_le_mul_of_nonneg_right hBuT.le hBv0
          _ < Tu * Tv := mul_lt_mul_of_pos_left hBvT hTu

/-- C011's (5) in cleared integer form: in the two-defect normal form (`k ≥ 1`, positive arcs),
`g² · 2^{|u₀| + |v₀|} < (2^k − 1)² · 2^{Σu₀ + Σv₀} · 3^m` with `m = |u₀| + |v₀| + 2`, i.e.
`g² < (2^k − 1)² 2^{A − m − k − 2a + 2} 3^m`. -/
theorem two_defect_bound_sharp (a k : ℕ) (hk : 1 ≤ k) (u₀ v₀ : List ℕ)
    (hu : ∀ x ∈ u₀, 1 ≤ x) (hv : ∀ x ∈ v₀, 1 ≤ x)
    (hrot : ∃ r, (a :: (u₀ ++ (a + k) :: v₀)).rotate r = (a + k) :: (u₀ ++ a :: v₀)) :
    ((Int.gcd (C (a :: (u₀ ++ (a + k) :: v₀))) (D (a :: (u₀ ++ (a + k) :: v₀))) : ℕ) : ℤ) ^ 2
        * 2 ^ (u₀.length + v₀.length)
      < (2 ^ k - 1) ^ 2 * 2 ^ (u₀.sum + v₀.sum) * 3 ^ (u₀.length + v₀.length + 2) := by
  have hg := two_arc_dvd a k hk u₀ v₀ hrot
  have hG0 : (0 : ℤ) ≤
      ((Int.gcd (C (a :: (u₀ ++ (a + k) :: v₀))) (D (a :: (u₀ ++ (a + k) :: v₀))) : ℕ) : ℤ) :=
    Nat.cast_nonneg _
  have hH0 : (0 : ℤ) ≤ ((Int.gcd (C (u₀ ++ [a + k])) (C (v₀ ++ [a])) : ℕ) : ℤ) :=
    Nat.cast_nonneg _
  have hCu : 0 < C (u₀ ++ [a + k]) := C_pos (by simp)
  have hCv : 0 < C (v₀ ++ [a]) := C_pos (by simp)
  have hHpos : (0 : ℤ) < ((Int.gcd (C (u₀ ++ [a + k])) (C (v₀ ++ [a])) : ℕ) : ℤ) := by
    have := Int.gcd_pos_of_ne_zero_left (C (v₀ ++ [a])) hCu.ne'
    exact_mod_cast this
  have hHu : ((Int.gcd (C (u₀ ++ [a + k])) (C (v₀ ++ [a])) : ℕ) : ℤ) ≤ C (u₀ ++ [a + k]) :=
    Int.le_of_dvd hCu (Int.gcd_dvd_left _ _)
  have hHv : ((Int.gcd (C (u₀ ++ [a + k])) (C (v₀ ++ [a])) : ℕ) : ℤ) ≤ C (v₀ ++ [a]) :=
    Int.le_of_dvd hCv (Int.gcd_dvd_right _ _)
  have hX : (0 : ℤ) < 2 ^ k - 1 := by
    have : (1 : ℤ) < 2 ^ k := one_lt_pow₀ (by norm_num) (by omega)
    linarith
  have hGXH := Int.le_of_dvd (mul_pos hX hHpos) hg
  have hbu := intercept_bound_last u₀ (a + k) hu
  have hbv := intercept_bound_last v₀ a hv
  have hBuT : (2 : ℤ) ^ u₀.sum * (3 ^ (u₀.length + 1) - 2 ^ (u₀.length + 1))
      < 2 ^ u₀.sum * 3 ^ (u₀.length + 1) :=
    mul_lt_mul_of_pos_left (sub_lt_self _ (by positivity)) (by positivity)
  have hBvT : (2 : ℤ) ^ v₀.sum * (3 ^ (v₀.length + 1) - 2 ^ (v₀.length + 1))
      < 2 ^ v₀.sum * 3 ^ (v₀.length + 1) :=
    mul_lt_mul_of_pos_left (sub_lt_self _ (by positivity)) (by positivity)
  have key := two_defect_arith hG0 hX hH0 hGXH hHu hHv (by positivity) (by positivity) hbu hbv
    hBuT hBvT (by positivity)
  calc ((Int.gcd (C (a :: (u₀ ++ (a + k) :: v₀))) (D (a :: (u₀ ++ (a + k) :: v₀))) : ℕ) : ℤ) ^ 2
        * 2 ^ (u₀.length + v₀.length)
      = ((Int.gcd (C (a :: (u₀ ++ (a + k) :: v₀))) (D (a :: (u₀ ++ (a + k) :: v₀))) : ℕ) : ℤ) ^ 2
        * (2 ^ u₀.length * 2 ^ v₀.length) := by rw [pow_add]
    _ < (2 ^ k - 1) ^ 2 * ((2 ^ u₀.sum * 3 ^ (u₀.length + 1)) * (2 ^ v₀.sum * 3 ^ (v₀.length + 1))) :=
        key
    _ = (2 ^ k - 1) ^ 2 * 2 ^ (u₀.sum + v₀.sum) * 3 ^ (u₀.length + v₀.length + 2) := by ring

/-- C011's (7) in cleared integer form: `g² · 2^{2m} < 2^{2A} · 3^m`, i.e. `g² < 2^{2A−2m} 3^m`, for
the two-defect normal form with `a, k ≥ 1` and positive arcs (`A = Σw`, `m = |w|`). -/
theorem two_defect_bound (a k : ℕ) (ha : 1 ≤ a) (hk : 1 ≤ k) (u₀ v₀ : List ℕ)
    (hu : ∀ x ∈ u₀, 1 ≤ x) (hv : ∀ x ∈ v₀, 1 ≤ x)
    (hrot : ∃ r, (a :: (u₀ ++ (a + k) :: v₀)).rotate r = (a + k) :: (u₀ ++ a :: v₀)) :
    ((Int.gcd (C (a :: (u₀ ++ (a + k) :: v₀))) (D (a :: (u₀ ++ (a + k) :: v₀))) : ℕ) : ℤ) ^ 2
        * 2 ^ (2 * (a :: (u₀ ++ (a + k) :: v₀)).length)
      < 2 ^ (2 * (a :: (u₀ ++ (a + k) :: v₀)).sum) * 3 ^ (a :: (u₀ ++ (a + k) :: v₀)).length := by
  have hsharp := two_defect_bound_sharp a k hk u₀ v₀ hu hv hrot
  have hlen : (a :: (u₀ ++ (a + k) :: v₀)).length = u₀.length + v₀.length + 2 := by
    simp only [List.length_cons, List.length_append]
    omega
  have hsum : (a :: (u₀ ++ (a + k) :: v₀)).sum = a + u₀.sum + (a + k) + v₀.sum := by
    simp only [List.sum_cons, List.sum_append]
    omega
  rw [hlen, hsum]
  set G : ℤ :=
    ((Int.gcd (C (a :: (u₀ ++ (a + k) :: v₀))) (D (a :: (u₀ ++ (a + k) :: v₀))) : ℕ) : ℤ) with hG
  have hX1 : (1 : ℤ) ≤ 2 ^ k := one_le_pow₀ (by norm_num)
  have hX0 : (0 : ℤ) ≤ 2 ^ k - 1 := by linarith
  have hX : (2 : ℤ) ^ k - 1 < 2 ^ k := sub_one_lt _
  have hX2 : ((2 : ℤ) ^ k - 1) ^ 2 ≤ (2 ^ k) ^ 2 := by
    rw [sq, sq]
    exact (mul_self_lt_mul_self hX0 hX).le
  have hlu := List.length_le_sum_of_one_le u₀ hu
  have hlv := List.length_le_sum_of_one_le v₀ hv
  have hexp : 2 * k + (u₀.sum + v₀.sum) + (u₀.length + v₀.length + 4)
      ≤ 2 * (a + u₀.sum + (a + k) + v₀.sum) := by omega
  have hpow : (2 : ℤ) ^ (2 * k + (u₀.sum + v₀.sum) + (u₀.length + v₀.length + 4))
      ≤ 2 ^ (2 * (a + u₀.sum + (a + k) + v₀.sum)) := pow_le_pow_right₀ (by norm_num) hexp
  have hQ : (0 : ℤ) < 2 ^ (u₀.length + v₀.length + 4) := by positivity
  calc G ^ 2 * 2 ^ (2 * (u₀.length + v₀.length + 2))
      = (G ^ 2 * 2 ^ (u₀.length + v₀.length)) * 2 ^ (u₀.length + v₀.length + 4) := by ring
    _ < ((2 ^ k - 1) ^ 2 * 2 ^ (u₀.sum + v₀.sum) * 3 ^ (u₀.length + v₀.length + 2))
          * 2 ^ (u₀.length + v₀.length + 4) := mul_lt_mul_of_pos_right hsharp hQ
    _ ≤ ((2 ^ k) ^ 2 * 2 ^ (u₀.sum + v₀.sum) * 3 ^ (u₀.length + v₀.length + 2))
          * 2 ^ (u₀.length + v₀.length + 4) := by
        apply mul_le_mul_of_nonneg_right _ hQ.le
        apply mul_le_mul_of_nonneg_right _ (by positivity)
        exact mul_le_mul_of_nonneg_right hX2 (by positivity)
    _ = 2 ^ (2 * k + (u₀.sum + v₀.sum) + (u₀.length + v₀.length + 4))
          * 3 ^ (u₀.length + v₀.length + 2) := by ring
    _ ≤ 2 ^ (2 * (a + u₀.sum + (a + k) + v₀.sum)) * 3 ^ (u₀.length + v₀.length + 2) :=
        mul_le_mul_of_nonneg_right hpow (by positivity)

/-- The reduced denominator form of C011's (7): with `D_w = g q`, `q > 0`,
`D_w² · 2^{2m} < q² · 2^{2A} · 3^m`, i.e. `q > (1 − 3^m/2^A) (2/√3)^m`. -/
theorem two_defect_q_bound (a k : ℕ) (ha : 1 ≤ a) (hk : 1 ≤ k) (u₀ v₀ : List ℕ)
    (hu : ∀ x ∈ u₀, 1 ≤ x) (hv : ∀ x ∈ v₀, 1 ≤ x)
    (hrot : ∃ r, (a :: (u₀ ++ (a + k) :: v₀)).rotate r = (a + k) :: (u₀ ++ a :: v₀))
    {q : ℤ} (hq0 : 0 < q)
    (hq : D (a :: (u₀ ++ (a + k) :: v₀)) =
      ((Int.gcd (C (a :: (u₀ ++ (a + k) :: v₀))) (D (a :: (u₀ ++ (a + k) :: v₀))) : ℕ) : ℤ) * q) :
    D (a :: (u₀ ++ (a + k) :: v₀)) ^ 2 * 2 ^ (2 * (a :: (u₀ ++ (a + k) :: v₀)).length)
      < q ^ 2 * 2 ^ (2 * (a :: (u₀ ++ (a + k) :: v₀)).sum)
          * 3 ^ (a :: (u₀ ++ (a + k) :: v₀)).length := by
  have h := two_defect_bound a k ha hk u₀ v₀ hu hv hrot
  rw [hq]
  calc (((Int.gcd (C (a :: (u₀ ++ (a + k) :: v₀))) (D (a :: (u₀ ++ (a + k) :: v₀))) : ℕ) : ℤ) * q)
          ^ 2 * 2 ^ (2 * (a :: (u₀ ++ (a + k) :: v₀)).length)
      = q ^ 2 * (((Int.gcd (C (a :: (u₀ ++ (a + k) :: v₀)))
          (D (a :: (u₀ ++ (a + k) :: v₀))) : ℕ) : ℤ) ^ 2
            * 2 ^ (2 * (a :: (u₀ ++ (a + k) :: v₀)).length)) := by ring
    _ < q ^ 2 * (2 ^ (2 * (a :: (u₀ ++ (a + k) :: v₀)).sum)
          * 3 ^ (a :: (u₀ ++ (a + k) :: v₀)).length) :=
        mul_lt_mul_of_pos_left h (pow_pos hq0 2)
    _ = q ^ 2 * 2 ^ (2 * (a :: (u₀ ++ (a + k) :: v₀)).sum)
          * 3 ^ (a :: (u₀ ++ (a + k) :: v₀)).length := by ring

/-! ### C010: sharp odd-spacing bounds on the complete dyadic circle

C010 (`ODD_ROUNDING.md` §§2–3) bounds each complete sorted gap `Δ_r` from below by a sharp
constant `b_q(a, b)` depending on the adjacent sorted heights `a = H_r`, `b = H_{r+1}`: `2/2^a`
for `b = a`, `1/2^a` for `b < a` (the seam included, with `b = −1`), and
`[q(2^k − 1) + η]/(3 · 2^b)` for `b = a + k > a`, where strict image order gives `3r > q(2^k − 1)`
for the odd numerator `r` and the residue of `q(2^k − 1)` modulo `6` supplies `η ∈ {6, 2, 4}`.
Summing over the circle, `L ≥ R_q(H) = Σ b_q(H_r, H_{r+1})`. Here everything is scaled by `2^B`
(`G_r = 2^B Δ_r`) and the upward bound is multiplied by `3` to stay in `ℤ`. -/

/-- C010's residue increment `η(q, k)`: `6` for even `k`; for odd `k`, `2` if `q ≡ 1 (mod 6)` and
`4` otherwise (`q ≡ 5 (mod 6)` in the intended domain `gcd(q, 6) = 1`). -/
def eta (q : ℤ) (k : ℕ) : ℤ := if Even k then 6 else if q % 6 = 1 then 2 else 4

/-- C010 §2's increment: for odd `r, q` and `k ≥ 1`, `q (2^k − 1) < 3 r` forces
`q (2^k − 1) + η(q, k) ≤ 3 r`, because `3 r ≡ 3 (mod 6)` while `q (2^k − 1) ≡ 3` (`k` even) or
`≡ q` (`k` odd) modulo `6`. The prose assumes `3 ∤ q`; it is not needed, since for `q ≡ 3 (mod 6)`
the true increment is `6 ≥ 4`. -/
theorem eta_refine {q r : ℤ} (k : ℕ) (hk : 1 ≤ k) (hq : Odd q) (hr : Odd r)
    (h : q * (2 ^ k - 1) < 3 * r) : q * (2 ^ k - 1) + eta q k ≤ 3 * r := by
  have hx2 : (2 : ℤ) ∣ 2 ^ k := dvd_pow_self 2 (by omega)
  have hxodd : Odd ((2 : ℤ) ^ k - 1) := by
    obtain ⟨c, hc⟩ := hx2
    exact ⟨c - 1, by omega⟩
  have hyodd : Odd (q * (2 ^ k - 1)) := Int.odd_mul.mpr ⟨hq, hxodd⟩
  have hmod : (2 : ℤ) ^ k ≡ (-1) ^ k [ZMOD 3] := (show (2 : ℤ) ≡ -1 [ZMOD 3] by decide).pow k
  obtain ⟨s, hs⟩ := hyodd
  obtain ⟨u, hu⟩ := hr
  obtain ⟨v, hv⟩ := hq
  unfold eta
  rcases Nat.even_or_odd k with hke | hko
  · rw [hke.neg_one_pow] at hmod
    have h3y : (3 : ℤ) ∣ q * (2 ^ k - 1) := Dvd.dvd.mul_left hmod.symm.dvd q
    rw [ite_eq_left hke]
    omega
  · rw [hko.neg_one_pow] at hmod
    have h3' : (3 : ℤ) ∣ 2 ^ k + 1 := by
      have := hmod.symm.dvd
      rwa [sub_neg_eq_add] at this
    have h3y : (3 : ℤ) ∣ q * (2 ^ k - 1) - q := by
      have hrew : q * (2 ^ k - 1) - q = q * (2 ^ k + 1) - 3 * q := by ring
      rw [hrew]
      exact dvd_sub (Dvd.dvd.mul_left h3' q) (dvd_mul_right 3 q)
    rw [ite_eq_right (Nat.not_even_iff_odd.mpr hko)]
    split_ifs with h6 <;> omega

/-- An ordered primitive odd cycle with `m ≥ 2`, together with its exponent window: C006's
domain (order of the normalised successor is the hypothesis `hord`). -/
structure OrdCycle (m : ℕ) where
  Γ : OddCycle m
  hord : ∀ i j, Γ.Z i < Γ.Z j ↔ Γ.F i < Γ.F j
  q' : ℕ
  hq1 : (2 : ℤ) ^ q' * Γ.lo ≤ Γ.F 0
  hq2 : Γ.F 0 < 2 ^ (q' + 1) * Γ.lo
  hm2 : 2 ≤ m
  hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j

namespace OrdCycle

variable {m : ℕ} (Ω : OrdCycle m)

/-- The underlying ordered `NarrowCycle` on the scaled normalised states. -/
noncomputable def N : NarrowCycle m := Ω.Γ.toNarrow Ω.hord Ω.q' Ω.hq1 Ω.hq2

theorem N_prim : Ω.N.Primitive := Ω.Γ.toNarrow_primitive Ω.hord Ω.q' Ω.hq1 Ω.hq2 Ω.hprim

theorem N_rank_zero : Ω.N.rank 0 = 0 := Ω.Γ.toNarrow_rank_zero Ω.hord Ω.q' Ω.hq1 Ω.hq2

theorem N_x (i : ℕ) : Ω.N.x i = Ω.Γ.Z i := rfl

theorem N_q : Ω.N.q = Ω.q' := rfl

theorem numHigh_lt : Ω.N.numHigh < m := Ω.N.numHigh_lt Ω.N_prim Ω.hm2

theorem numHigh_pos : 0 < Ω.N.numHigh := Ω.N.numHigh_pos Ω.N_prim Ω.hm2

/-- The low exponent is at least `1` (the least image exceeds `3 lo > 2 lo`). -/
theorem q'_pos : 1 ≤ Ω.q' := by
  rcases Nat.eq_zero_or_pos Ω.q' with h | h
  · exfalso
    have h2 := Ω.hq2
    rw [h, Nat.zero_add, pow_one] at h2
    have hF := Ω.Γ.F_zero
    have hlo : 0 < Ω.Γ.lo := by
      unfold OddCycle.lo
      exact mul_pos (by positivity) Ω.Γ.npos
    have hd : (0 : ℤ) < 2 ^ Ω.Γ.B * Ω.Γ.q := mul_pos (by positivity) Ω.Γ.hq
    linarith
  · exact h

/-- The height of the state of rank `r`. -/
noncomputable def hr (r : ℕ) : ℕ := Ω.Γ.h (Ω.N.idx r)

/-- The scaled offset `2^{B−h'_r} q` of the state of rank `r`, and its seam extension. -/
noncomputable def off (r : ℕ) : ℤ := 2 ^ (Ω.Γ.B - Ω.hr r) * Ω.Γ.q

noncomputable def offext (r : ℕ) : ℤ := if r < m then Ω.off r else 2 * Ω.off (r - m)

/-- C006's `T_r = 2^B(ε_[r+1] − ε_[r])`, with the seam `ε_[m] = 2ε_[0]`. -/
noncomputable def T (r : ℕ) : ℤ := Ω.offext (r + 1) - Ω.offext r

theorem Fr_eq (r : ℕ) : Ω.N.Fr r = 3 * Ω.N.y r + Ω.off r := rfl

/-- The image difference between consecutive sorted ranks is `3Δ_r + T_r`. -/
theorem Fext_sub {r : ℕ} (hr : r < m) :
    Ω.N.Fext (r + 1) - Ω.N.Fext r = 3 * Ω.N.gap r + Ω.T r := by
  unfold NarrowCycle.gap T
  rcases Nat.lt_or_ge (r + 1) m with h1 | h1
  · rw [Ω.N.Fext_of_lt h1, Ω.N.Fext_of_lt hr, Ω.N.yext_of_lt h1, Ω.N.yext_of_lt hr]
    unfold offext
    rw [ite_eq_left h1, ite_eq_left hr, Ω.Fr_eq, Ω.Fr_eq]
    ring
  · have hm : r + 1 = m := le_antisymm hr h1
    rw [hm, Ω.N.Fext_m, Ω.N.Fext_of_lt hr, Ω.N.yext_m, Ω.N.yext_of_lt hr]
    unfold offext
    rw [ite_eq_right (lt_irrefl m), Nat.sub_self, ite_eq_left hr, Ω.Fr_eq, Ω.Fr_eq]
    ring

/-- **C006's (G3)** in its stated form: `2^{e_r} Δ_{(r+h) mod m} = 3Δ_r + T_r`. -/
theorem gap_rec {r : ℕ} (hr : r < m) :
    (2 : ℤ) ^ Ω.N.e r * Ω.N.gap ((r + Ω.N.numHigh) % m) = 3 * Ω.N.gap r + Ω.T r := by
  rw [Ω.N.gap_recurrence Ω.N_prim Ω.hm2 hr, Ω.Fext_sub hr]

theorem hr_le_B (r : ℕ) : Ω.hr r ≤ Ω.Γ.B := Ω.Γ.hB _

/-- `T_r = 0` exactly when the adjacent sorted heights agree (`r + 1 < m`). -/
theorem T_eq_zero_iff {r : ℕ} (hr1 : r + 1 < m) : Ω.T r = 0 ↔ Ω.hr (r + 1) = Ω.hr r := by
  unfold T offext off
  rw [ite_eq_left hr1, ite_eq_left (by omega : r < m)]
  constructor
  · intro h
    have hq := Ω.Γ.hq
    have h' : ((2 : ℤ) ^ (Ω.Γ.B - Ω.hr (r + 1)) - 2 ^ (Ω.Γ.B - Ω.hr r)) * Ω.Γ.q = 0 := by
      linarith
    rcases mul_eq_zero.mp h' with h'' | h''
    · have h3 : (2 : ℤ) ^ (Ω.Γ.B - Ω.hr (r + 1)) = 2 ^ (Ω.Γ.B - Ω.hr r) := by linarith
      have h4 : (2 ^ (Ω.Γ.B - Ω.hr (r + 1)) : ℕ) = 2 ^ (Ω.Γ.B - Ω.hr r) := by exact_mod_cast h3
      have h5 := Nat.pow_right_injective (le_refl 2) h4
      have := Ω.hr_le_B r
      have := Ω.hr_le_B (r + 1)
      omega
    · exact absurd h'' hq.ne'
  · intro h
    rw [h]
    ring

theorem hr_zero : Ω.hr 0 = 0 := by
  unfold hr
  rw [Ω.N.idx_zero Ω.N_prim Ω.N_rank_zero]
  exact Ω.Γ.h_zero

/-- The seam term is always positive: `T_{m−1} = 2^{B+1} q − 2^{B−h'_{m−1}} q > 0`, so the seam
is a forced position (`J ≥ 1`). -/
theorem T_seam_pos : 0 < Ω.T (m - 1) := by
  have hm := Ω.Γ.hm
  unfold T offext
  rw [show m - 1 + 1 = m by omega, ite_eq_right (lt_irrefl m), Nat.sub_self,
    ite_eq_left (by omega : m - 1 < m)]
  unfold off
  rw [Ω.hr_zero, Nat.sub_zero]
  have h1 : (2 : ℤ) ^ (Ω.Γ.B - Ω.hr (m - 1)) ≤ 2 ^ Ω.Γ.B :=
    pow_le_pow_right₀ (by norm_num) (Nat.sub_le _ _)
  have hq := Ω.Γ.hq
  have h2 : (0 : ℤ) < 2 ^ Ω.Γ.B := by positivity
  nlinarith [mul_le_mul_of_nonneg_right h1 hq.le, mul_pos h2 hq]

/-- The rank reached after `k` successor steps from rank `r₀`: `(r₀ + k h) mod m`. -/
noncomputable def orb (r₀ k : ℕ) : ℕ := (r₀ + k * Ω.N.numHigh) % m

theorem orb_lt (r₀ k : ℕ) : Ω.orb r₀ k < m := Nat.mod_lt _ Ω.Γ.hm

theorem orb_zero {r₀ : ℕ} (hr₀ : r₀ < m) : Ω.orb r₀ 0 = r₀ := by
  unfold orb
  rw [Nat.zero_mul, Nat.add_zero]
  exact Nat.mod_eq_of_lt hr₀

theorem orb_succ (r₀ k : ℕ) : Ω.orb r₀ (k + 1) = (Ω.orb r₀ k + Ω.N.numHigh) % m := by
  unfold orb
  rw [Nat.mod_add_mod, Nat.add_mul, Nat.one_mul, Nat.add_assoc]

/-- **C006's per-run bound.** Along a zero-forcing run of length `t` starting at rank `r₀`
(`T = 0` at the first `t` ranks of its successor orbit), `2^t ≤ Δ_{r₀} < 2^B L`; hence
`L > 2^{t−B}`. -/
theorem run_bound {r₀ t : ℕ} (hr₀ : r₀ < m) (hrun : ∀ k, k < t → Ω.T (Ω.orb r₀ k) = 0) :
    (2 : ℤ) ^ t ≤ Ω.N.gap r₀ ∧ Ω.N.gap r₀ < 2 ^ Ω.Γ.B * Ω.Γ.n 0 := by
  have hG : ∀ k, k < t →
      (2 : ℤ) ^ Ω.N.e (Ω.orb r₀ k) * Ω.N.gap (Ω.orb r₀ (k + 1)) = 3 * Ω.N.gap (Ω.orb r₀ k) := by
    intro k hk
    rw [Ω.orb_succ, Ω.gap_rec (Ω.orb_lt r₀ k), hrun k hk, add_zero]
  have hpos : 0 < Ω.N.gap r₀ := Ω.N.gap_pos Ω.N_prim Ω.N_rank_zero hr₀
  have hq : 1 ≤ Ω.N.q := Ω.q'_pos
  have he : ∀ k, k < t → 1 ≤ Ω.N.e (Ω.orb r₀ k) := by
    intro k _
    unfold NarrowCycle.e
    split_ifs <;> omega
  have h1 := run_lower (fun k => Ω.N.gap (Ω.orb r₀ k)) (fun k => Ω.N.e (Ω.orb r₀ k)) t
    (by show 0 < Ω.N.gap (Ω.orb r₀ 0); rw [Ω.orb_zero hr₀]; exact hpos) he hG
  have h1' : (2 : ℤ) ^ t ≤ Ω.N.gap r₀ := by
    have := h1
    rw [Ω.orb_zero hr₀] at this
    exact this
  refine ⟨h1', ?_⟩
  have h2 := Ω.N.gap_lt Ω.N_prim Ω.N_rank_zero Ω.hm2 hr₀
  rw [Ω.N_x, Ω.Γ.Z_zero] at h2
  unfold OddCycle.lo at h2
  exact h2

/-- `L > 2^{t−B}` in cleared form: `2^t < 2^B L` for every zero-forcing run of length `t`. -/
theorem run_bound_L {r₀ t : ℕ} (hr₀ : r₀ < m) (hrun : ∀ k, k < t → Ω.T (Ω.orb r₀ k) = 0) :
    (2 : ℤ) ^ t < 2 ^ Ω.Γ.B * Ω.Γ.n 0 := by
  obtain ⟨h1, h2⟩ := Ω.run_bound hr₀ hrun
  exact lt_of_le_of_lt h1 h2

/-! #### The forced positions along the orbit, `J`, and (G1)'s first inequality -/

theorem orb_zero_eq_rank (k : ℕ) : Ω.orb 0 k = Ω.N.rank k := by
  unfold orb
  rw [Ω.N.rank_formula Ω.numHigh_lt k, Ω.N_rank_zero]

theorem orb_orb (a j : ℕ) : Ω.orb (Ω.orb 0 a) j = Ω.orb 0 (a + j) := by
  unfold orb
  rw [Nat.zero_add, Nat.zero_add, Nat.mod_add_mod, Nat.add_mul]

theorem orb_mod (k : ℕ) : Ω.orb 0 (k % m) = Ω.orb 0 k := by
  unfold orb
  rw [Nat.zero_add, Nat.zero_add, Nat.mul_mod, Nat.mod_mod, ← Nat.mul_mod]

/-- The `k`-th rank of the orbit of rank `0` is a forced position: `T ≠ 0` there. -/
noncomputable def forcedAt (k : ℕ) : Prop := Ω.T (Ω.orb 0 k) ≠ 0

noncomputable instance decForcedAt (k : ℕ) : Decidable (Ω.forcedAt k) :=
  inferInstanceAs (Decidable (Ω.T (Ω.orb 0 k) ≠ 0))

/-- C006's `J`, the number of forced positions (`T_j ≠ 0`), counted along the orbit. -/
noncomputable def J : ℕ := ((Finset.range m).filter Ω.forcedAt).card

/-- `J` counts the ranks with `T_r ≠ 0`, as in the prose (the orbit visits every rank once). -/
theorem J_eq : Ω.J = ((Finset.range m).filter (fun r => Ω.T r ≠ 0)).card := by
  unfold J
  apply Finset.card_bij (fun k _ => Ω.orb 0 k)
  · intro k hk
    rw [Finset.mem_filter] at hk ⊢
    exact ⟨Finset.mem_range.mpr (Ω.orb_lt 0 k), hk.2⟩
  · intro k hk k' hk' h
    rw [Ω.orb_zero_eq_rank, Ω.orb_zero_eq_rank] at h
    exact Ω.N.rank_inj Ω.N_prim (Finset.mem_range.mp (Finset.mem_filter.mp hk).1)
      (Finset.mem_range.mp (Finset.mem_filter.mp hk').1) h
  · intro r hr
    rw [Finset.mem_filter] at hr
    obtain ⟨k, hk, hrk⟩ := Ω.N.exists_rank_eq Ω.N_prim (Finset.mem_range.mp hr.1)
    refine ⟨k, Finset.mem_filter.mpr ⟨Finset.mem_range.mpr hk, ?_⟩, ?_⟩
    · show Ω.T (Ω.orb 0 k) ≠ 0
      rw [Ω.orb_zero_eq_rank, hrk]
      exact hr.2
    · rw [Ω.orb_zero_eq_rank, hrk]

/-- The seam makes `J ≥ 1`. -/
theorem J_pos : 0 < Ω.J := by
  rw [Ω.J_eq]
  apply Finset.card_pos.mpr
  refine ⟨m - 1, Finset.mem_filter.mpr ⟨Finset.mem_range.mpr ?_, ?_⟩⟩
  · have := Ω.Γ.hm
    omega
  · exact ne_of_gt Ω.T_seam_pos

/-- Some rank `r₀` starts a zero-forcing run of length `⌊(m−1)/J⌋ = ⌈m/J⌉ − 1`. -/
theorem exists_zero_run :
    ∃ r₀, r₀ < m ∧ ∀ j, j < (m - 1) / Ω.J → Ω.T (Ω.orb r₀ j) = 0 := by
  obtain ⟨k₀, _, _, hrun⟩ := exists_run Ω.Γ.hm Ω.forcedAt Ω.J_pos
  refine ⟨Ω.orb 0 (k₀ + 1), Ω.orb_lt _ _, ?_⟩
  intro j hj
  have h := hrun j hj
  unfold forcedAt at h
  rw [Ω.orb_mod] at h
  rw [Ω.orb_orb]
  exact not_ne_iff.mp h

/-- **C006's (G1), first inequality:** `L > 2^{⌈m/J⌉ − 1 − B}`, in the cleared form
`2^{⌊(m−1)/J⌋} < 2^B L`. -/
theorem G1_first : (2 : ℤ) ^ ((m - 1) / Ω.J) < 2 ^ Ω.Γ.B * Ω.Γ.n 0 := by
  obtain ⟨r₀, hr₀, hrun⟩ := Ω.exists_zero_run
  exact Ω.run_bound_L hr₀ hrun

/-! #### C006's (H1): `J ≥ B + 1` in sorted order -/

/-- The height of the state of rank `rank i` is the height of state `i`. -/
theorem hr_rank {i : ℕ} (hi : i < m) : Ω.hr (Ω.N.rank i) = Ω.Γ.h i := by
  unfold hr
  have hr := Ω.N.idx_spec Ω.N_prim (Ω.N.rank_lt i)
  have hx : Ω.N.x (Ω.N.idx (Ω.N.rank i)) = Ω.N.x i := Ω.N.x_eq_of_rank_eq hr.1 hi hr.2
  rw [Ω.N_x, Ω.N_x] at hx
  exact (Ω.Γ.Z_inj hx).1

/-- Under `q ≤ L` and positive valuations every height up to an attained one is the height of
some ranked state. -/
theorem exists_rank_height (hqL : Ω.Γ.q ≤ Ω.Γ.n 0) (hapos : ∀ i, 1 ≤ Ω.Γ.a i) {j b : ℕ}
    (hb : b ≤ Ω.Γ.h j) : ∃ r, r < m ∧ Ω.hr r = b := by
  obtain ⟨i, _, hi⟩ := Ω.Γ.exists_height_eq hqL hapos hb
  refine ⟨Ω.N.rank (i % m), Ω.N.rank_lt _, ?_⟩
  rw [Ω.hr_rank (Nat.mod_lt _ Ω.Γ.hm), Ω.Γ.h_mod, hi]

/-- `J` is one plus the number of adjacent sorted-height changes (the seam counted once). -/
theorem J_eq_changes :
    Ω.J = 1 + ((Finset.range (m - 1)).filter (fun r => Ω.hr (r + 1) ≠ Ω.hr r)).card := by
  rw [Ω.J_eq]
  have hm := Ω.Γ.hm
  have hsplit : Finset.range m = insert (m - 1) (Finset.range (m - 1)) := by
    conv_lhs => rw [show m = (m - 1) + 1 by omega]
    exact Finset.range_add_one
  have hfeq : (Finset.range (m - 1)).filter (fun r => Ω.T r ≠ 0)
      = (Finset.range (m - 1)).filter (fun r => Ω.hr (r + 1) ≠ Ω.hr r) := by
    apply Finset.filter_congr
    intro r hr
    have hr1 : r + 1 < m := by
      have := Finset.mem_range.mp hr
      omega
    exact not_congr (Ω.T_eq_zero_iff hr1)
  have hnot : m - 1 ∉ (Finset.range (m - 1)).filter (fun r => Ω.T r ≠ 0) := fun hmem =>
    lt_irrefl (m - 1) (Finset.mem_range.mp (Finset.mem_filter.mp hmem).1)
  rw [hsplit, Finset.filter_insert, ite_eq_left (ne_of_gt Ω.T_seam_pos),
    Finset.card_insert_of_notMem hnot, hfeq, add_comm]

/-- **C006's (H1), `J ≥ B + 1`:** under `q ≤ L` and positive valuations, every attained height
`h_j` satisfies `h_j + 1 ≤ J` (all heights `0, …, h_j` occur, so the sorted height list has at
least `h_j` changes, plus the seam). -/
theorem J_ge_height (hqL : Ω.Γ.q ≤ Ω.Γ.n 0) (hapos : ∀ i, 1 ≤ Ω.Γ.a i) (j : ℕ) :
    Ω.Γ.h j + 1 ≤ Ω.J := by
  have hm := Ω.Γ.hm
  have hsub : Finset.range (Ω.Γ.h j + 1) ⊆ (Finset.range m).image Ω.hr := by
    intro b hb
    obtain ⟨r, hr, hrb⟩ :=
      Ω.exists_rank_height hqL hapos (Nat.lt_succ_iff.mp (Finset.mem_range.mp hb))
    exact Finset.mem_image.mpr ⟨r, Finset.mem_range.mpr hr, hrb⟩
  have h1 := Finset.card_le_card hsub
  rw [Finset.card_range] at h1
  have h2 := card_image_le_changes Ω.hr (m - 1)
  rw [show m - 1 + 1 = m by omega] at h2
  rw [Ω.J_eq_changes]
  omega

/-! #### (G1)'s second inequality, in the true-intercept form -/

/-- (G1)'s second inequality with the true weighted intercept `C_h = C_m` (the chronological
intercept at the minimum, `D L = q C_h`): `D · 2^{⌊(m−1)/J⌋} < 2^B q C_h`, i.e.
`q > (D/C_h) 2^{⌈m/J⌉−1−B}`. C006 states the weaker `C_c` form through `C_h ≤ C_c`, which is
not formalised here. -/
theorem G1_second :
    ((2 : ℤ) ^ Ω.Γ.Apre m - 3 ^ m) * 2 ^ ((m - 1) / Ω.J)
      < 2 ^ Ω.Γ.B * (Ω.Γ.q * Ω.Γ.Cpre m) := by
  have hD := Ω.Γ.D_pos
  have h1 := Ω.G1_first
  have hc := Ω.Γ.cycle_identity
  calc ((2 : ℤ) ^ Ω.Γ.Apre m - 3 ^ m) * 2 ^ ((m - 1) / Ω.J)
      < ((2 : ℤ) ^ Ω.Γ.Apre m - 3 ^ m) * (2 ^ Ω.Γ.B * Ω.Γ.n 0) :=
        mul_lt_mul_of_pos_left h1 hD
    _ = 2 ^ Ω.Γ.B * (((2 : ℤ) ^ Ω.Γ.Apre m - 3 ^ m) * Ω.Γ.n 0) := by ring
    _ = 2 ^ Ω.Γ.B * (Ω.Γ.q * Ω.Γ.Cpre m) := by rw [hc]

/-! #### C010's sharp odd-spacing bounds and the summed bound `L ≥ R_q(H)` -/

/-- The sorted state of rank `r` in coordinates: `y_r = 2^{B − hr_r} n_{idx r}`. -/
theorem y_eq (r : ℕ) : Ω.N.y r = 2 ^ (Ω.Γ.B - Ω.hr r) * Ω.Γ.n (Ω.N.idx r) := rfl

/-- Adjacent sorted states are strictly increasing. -/
theorem y_succ_lt {r : ℕ} (hr1 : r + 1 < m) : Ω.N.y r < Ω.N.y (r + 1) :=
  Ω.N.y_lt_y Ω.N_prim (Nat.lt_succ_self r) hr1

/-- An interior gap is the difference of adjacent sorted states. -/
theorem gap_eq {r : ℕ} (hr1 : r + 1 < m) : Ω.N.gap r = Ω.N.y (r + 1) - Ω.N.y r := by
  unfold NarrowCycle.gap
  rw [Ω.N.yext_of_lt hr1, Ω.N.yext_of_lt (by omega)]

/-- Equal adjacent heights: `G_r ≥ 2 · 2^{B − a}` (two odd numerators differ by at least `2`). -/
theorem gap_ge_of_eq {r : ℕ} (hr1 : r + 1 < m) (heq : Ω.hr (r + 1) = Ω.hr r) :
    2 * 2 ^ (Ω.Γ.B - Ω.hr r) ≤ Ω.N.gap r := by
  have hy := Ω.y_succ_lt hr1
  have hyr := Ω.y_eq r
  have hyr1 := Ω.y_eq (r + 1)
  rw [heq] at hyr1
  have hPpos : (0 : ℤ) < 2 ^ (Ω.Γ.B - Ω.hr r) := by positivity
  rw [hyr, hyr1] at hy
  have hlt := lt_of_mul_lt_mul_left hy hPpos.le
  obtain ⟨s, hs⟩ := Ω.Γ.nodd (Ω.N.idx r)
  obtain ⟨t, ht⟩ := Ω.Γ.nodd (Ω.N.idx (r + 1))
  have h2 : (2 : ℤ) ≤ Ω.Γ.n (Ω.N.idx (r + 1)) - Ω.Γ.n (Ω.N.idx r) := by omega
  rw [Ω.gap_eq hr1, hyr, hyr1]
  have h3 := mul_le_mul_of_nonneg_left h2 hPpos.le
  rw [mul_sub] at h3
  linarith

/-- Downward adjacent heights: `G_r ≥ 2^{B − a}` (the numerator `2^{a−b} n_{[r+1]} − n_{[r]}` is a
positive integer). -/
theorem gap_ge_of_lt {r : ℕ} (hr1 : r + 1 < m) (hlt : Ω.hr (r + 1) < Ω.hr r) :
    2 ^ (Ω.Γ.B - Ω.hr r) ≤ Ω.N.gap r := by
  have hy := Ω.y_succ_lt hr1
  have hyr := Ω.y_eq r
  have hB := Ω.hr_le_B r
  have hsplit : Ω.Γ.B - Ω.hr (r + 1) = (Ω.Γ.B - Ω.hr r) + (Ω.hr r - Ω.hr (r + 1)) := by omega
  have hyr1 : Ω.N.y (r + 1) = 2 ^ (Ω.Γ.B - Ω.hr r) *
      (2 ^ (Ω.hr r - Ω.hr (r + 1)) * Ω.Γ.n (Ω.N.idx (r + 1))) := by
    rw [Ω.y_eq (r + 1), hsplit, pow_add, mul_assoc]
  have hPpos : (0 : ℤ) < 2 ^ (Ω.Γ.B - Ω.hr r) := by positivity
  rw [hyr, hyr1] at hy
  have hlt' := lt_of_mul_lt_mul_left hy hPpos.le
  have h1 : (1 : ℤ) ≤ 2 ^ (Ω.hr r - Ω.hr (r + 1)) * Ω.Γ.n (Ω.N.idx (r + 1))
      - Ω.Γ.n (Ω.N.idx r) := by omega
  rw [Ω.gap_eq hr1, hyr, hyr1]
  have h3 := mul_le_mul_of_nonneg_left h1 hPpos.le
  rw [mul_sub, mul_one] at h3
  linarith

/-- The seam: `G_{m−1} ≥ 2^{B − a}` with `a = hr_{m−1}` (the numerator `2^{a+1} L − n_{[m−1]}` is a
positive integer). -/
theorem gap_seam_ge : 2 ^ (Ω.Γ.B - Ω.hr (m - 1)) ≤ Ω.N.gap (m - 1) := by
  have hm := Ω.Γ.hm
  have hgap : Ω.N.gap (m - 1) = 2 * Ω.N.y 0 - Ω.N.y (m - 1) := by
    unfold NarrowCycle.gap
    rw [show m - 1 + 1 = m by omega, Ω.N.yext_m, Ω.N.yext_of_lt (by omega)]
  have hy0 : Ω.N.y 0 = 2 ^ Ω.Γ.B * Ω.Γ.n 0 := by
    rw [Ω.N.y_zero Ω.N_prim Ω.N_rank_zero, Ω.N_x, Ω.Γ.Z_zero]
    rfl
  have hpos := Ω.N.gap_pos Ω.N_prim Ω.N_rank_zero (Nat.sub_lt hm Nat.one_pos)
  have hB := Ω.hr_le_B (m - 1)
  have hsplit : Ω.Γ.B + 1 = (Ω.Γ.B - Ω.hr (m - 1)) + (Ω.hr (m - 1) + 1) := by omega
  have hpow : (2 : ℤ) ^ Ω.Γ.B * 2 = 2 ^ (Ω.Γ.B - Ω.hr (m - 1)) * 2 ^ (Ω.hr (m - 1) + 1) := by
    rw [← pow_succ, ← pow_add, ← hsplit]
  have h2y0 : 2 * Ω.N.y 0 = 2 ^ (Ω.Γ.B - Ω.hr (m - 1)) *
      (2 ^ (Ω.hr (m - 1) + 1) * Ω.Γ.n 0) := by
    rw [hy0]
    linear_combination Ω.Γ.n 0 * hpow
  have hym := Ω.y_eq (m - 1)
  have hPpos : (0 : ℤ) < 2 ^ (Ω.Γ.B - Ω.hr (m - 1)) := by positivity
  rw [hgap, h2y0, hym] at hpos ⊢
  rw [← mul_sub] at hpos ⊢
  have h1 : (1 : ℤ) ≤ 2 ^ (Ω.hr (m - 1) + 1) * Ω.Γ.n 0 - Ω.Γ.n (Ω.N.idx (m - 1)) := by
    have := (mul_pos_iff_of_pos_left hPpos).mp hpos
    omega
  have h3 := mul_le_mul_of_nonneg_left h1 hPpos.le
  rw [mul_one] at h3
  exact h3

/-- Upward adjacent heights, the order inequality: `2^{B−b} q (2^k − 1) < 3 G_r` with `k = b − a`
(strict increase of the images `F_{[r]} < F_{[r+1]}`). -/
theorem three_gap_gt_of_gt {r : ℕ} (hr1 : r + 1 < m) (hgt : Ω.hr r < Ω.hr (r + 1)) :
    2 ^ (Ω.Γ.B - Ω.hr (r + 1)) * (Ω.Γ.q * (2 ^ (Ω.hr (r + 1) - Ω.hr r) - 1))
      < 3 * Ω.N.gap r := by
  have hy := Ω.y_succ_lt hr1
  have hZ : Ω.Γ.Z (Ω.N.idx r) < Ω.Γ.Z (Ω.N.idx (r + 1)) := hy
  have hF : Ω.Γ.F (Ω.N.idx r) < Ω.Γ.F (Ω.N.idx (r + 1)) := (Ω.hord _ _).mp hZ
  have hB := Ω.hr_le_B (r + 1)
  have hsplit : Ω.Γ.B - Ω.hr r = (Ω.Γ.B - Ω.hr (r + 1)) + (Ω.hr (r + 1) - Ω.hr r) := by omega
  have hFi : Ω.Γ.F (Ω.N.idx r) = 3 * Ω.N.y r + 2 ^ (Ω.Γ.B - Ω.hr r) * Ω.Γ.q := rfl
  have hFj : Ω.Γ.F (Ω.N.idx (r + 1)) =
      3 * Ω.N.y (r + 1) + 2 ^ (Ω.Γ.B - Ω.hr (r + 1)) * Ω.Γ.q := rfl
  rw [hFi, hFj, hsplit, pow_add] at hF
  rw [Ω.gap_eq hr1]
  linear_combination hF

/-- Upward adjacent heights, C010's sharp form: `2^{B−b} (q (2^k − 1) + η(q, k)) ≤ 3 G_r`
(`q` odd). -/
theorem three_gap_ge_of_gt (hqodd : Odd Ω.Γ.q) {r : ℕ} (hr1 : r + 1 < m)
    (hgt : Ω.hr r < Ω.hr (r + 1)) :
    2 ^ (Ω.Γ.B - Ω.hr (r + 1)) * (Ω.Γ.q * (2 ^ (Ω.hr (r + 1) - Ω.hr r) - 1)
      + eta Ω.Γ.q (Ω.hr (r + 1) - Ω.hr r)) ≤ 3 * Ω.N.gap r := by
  have hB := Ω.hr_le_B (r + 1)
  have hsplit : Ω.Γ.B - Ω.hr r = (Ω.Γ.B - Ω.hr (r + 1)) + (Ω.hr (r + 1) - Ω.hr r) := by omega
  have hyr : Ω.N.y r = 2 ^ (Ω.Γ.B - Ω.hr (r + 1)) *
      (2 ^ (Ω.hr (r + 1) - Ω.hr r) * Ω.Γ.n (Ω.N.idx r)) := by
    rw [Ω.y_eq r, hsplit, pow_add, mul_assoc]
  have hyr1 := Ω.y_eq (r + 1)
  have hPpos : (0 : ℤ) < 2 ^ (Ω.Γ.B - Ω.hr (r + 1)) := by positivity
  have hgapeq : Ω.N.gap r = 2 ^ (Ω.Γ.B - Ω.hr (r + 1)) *
      (Ω.Γ.n (Ω.N.idx (r + 1)) - 2 ^ (Ω.hr (r + 1) - Ω.hr r) * Ω.Γ.n (Ω.N.idx r)) := by
    rw [Ω.gap_eq hr1, hyr, hyr1, mul_sub]
  have hstrict := Ω.three_gap_gt_of_gt hr1 hgt
  rw [hgapeq] at hstrict
  have hr' : Ω.Γ.q * (2 ^ (Ω.hr (r + 1) - Ω.hr r) - 1)
      < 3 * (Ω.Γ.n (Ω.N.idx (r + 1)) - 2 ^ (Ω.hr (r + 1) - Ω.hr r) * Ω.Γ.n (Ω.N.idx r)) := by
    have h' : 2 ^ (Ω.Γ.B - Ω.hr (r + 1)) * (Ω.Γ.q * (2 ^ (Ω.hr (r + 1) - Ω.hr r) - 1))
        < 2 ^ (Ω.Γ.B - Ω.hr (r + 1)) * (3 * (Ω.Γ.n (Ω.N.idx (r + 1))
          - 2 ^ (Ω.hr (r + 1) - Ω.hr r) * Ω.Γ.n (Ω.N.idx r))) := by
      linear_combination hstrict
    exact lt_of_mul_lt_mul_left h' hPpos.le
  have hodd : Odd (Ω.Γ.n (Ω.N.idx (r + 1))
      - 2 ^ (Ω.hr (r + 1) - Ω.hr r) * Ω.Γ.n (Ω.N.idx r)) := by
    have he : Even (2 ^ (Ω.hr (r + 1) - Ω.hr r) * Ω.Γ.n (Ω.N.idx r)) :=
      even_iff_two_dvd.mpr (dvd_mul_of_dvd_left (dvd_pow_self 2 (by omega)) _)
    exact (Ω.Γ.nodd _).sub_even he
  have hk : 1 ≤ Ω.hr (r + 1) - Ω.hr r := by omega
  have hbound := eta_refine _ hk hqodd hodd hr'
  rw [hgapeq]
  have h3' := mul_le_mul_of_nonneg_left hbound hPpos.le
  linarith

/-- Three times C010's sharp lower bound for the complete gap `G_r` (scaled by `2^B`): the seam,
equal, downward and upward cases of `b_q(H_r, H_{r+1})`, so that `Σ_r pairBound3 r / (3 · 2^B)`
is the prose's `R_q(H)`. -/
noncomputable def pairBound3 (r : ℕ) : ℤ :=
  if r + 1 < m then
    (if Ω.hr (r + 1) = Ω.hr r then 3 * (2 * 2 ^ (Ω.Γ.B - Ω.hr r))
     else if Ω.hr (r + 1) < Ω.hr r then 3 * 2 ^ (Ω.Γ.B - Ω.hr r)
     else 2 ^ (Ω.Γ.B - Ω.hr (r + 1)) * (Ω.Γ.q * (2 ^ (Ω.hr (r + 1) - Ω.hr r) - 1)
            + eta Ω.Γ.q (Ω.hr (r + 1) - Ω.hr r)))
  else 3 * 2 ^ (Ω.Γ.B - Ω.hr r)

/-- Each complete gap dominates its sharp bound: `pairBound3 r ≤ 3 G_r`. -/
theorem pairBound3_le (hqodd : Odd Ω.Γ.q) {r : ℕ} (hr : r < m) :
    Ω.pairBound3 r ≤ 3 * Ω.N.gap r := by
  unfold pairBound3
  split_ifs with h1 h2 h4
  · exact mul_le_mul_of_nonneg_left (Ω.gap_ge_of_eq h1 h2) (by norm_num)
  · exact mul_le_mul_of_nonneg_left (Ω.gap_ge_of_lt h1 h4) (by norm_num)
  · exact Ω.three_gap_ge_of_gt hqodd h1 (lt_of_le_of_ne (not_lt.mp h4) (Ne.symm h2))
  · have hm1 : r = m - 1 := by omega
    subst hm1
    exact mul_le_mul_of_nonneg_left Ω.gap_seam_ge (by norm_num)

/-- **C010's summed bound** `L ≥ R_q(H)` (its (3)) in scaled integer form: the sharp bounds of
the `m` complete gaps sum to at most `3 · 2^B L`, because the complete gaps sum to `2^B L`. -/
theorem rounding_bound (hqodd : Odd Ω.Γ.q) :
    ∑ r ∈ Finset.range m, Ω.pairBound3 r ≤ 3 * (2 ^ Ω.Γ.B * Ω.Γ.n 0) := by
  have hsum := Ω.N.sum_gap Ω.N_prim Ω.N_rank_zero
  rw [Ω.N_x, Ω.Γ.Z_zero] at hsum
  calc ∑ r ∈ Finset.range m, Ω.pairBound3 r
      ≤ ∑ r ∈ Finset.range m, 3 * Ω.N.gap r :=
        Finset.sum_le_sum fun r hr => Ω.pairBound3_le hqodd (Finset.mem_range.mp hr)
    _ = 3 * ∑ r ∈ Finset.range m, Ω.N.gap r := by rw [Finset.mul_sum]
    _ = 3 * Ω.Γ.lo := by rw [hsum]
    _ = 3 * (2 ^ Ω.Γ.B * Ω.Γ.n 0) := rfl

end OrdCycle

end Cyc
end LeanLane
