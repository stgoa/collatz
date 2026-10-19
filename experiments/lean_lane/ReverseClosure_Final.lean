/-!
# V007-a — Reverse closure: for a scalar sequence, binary and ternary automaticity
coincide, and either forces constancy modulo Cobham's theorem

This part is concatenated after `V004_Assembly.lean` (V004-i/ii/iii) and
`ScalarInterface.lean` (V005-a) by `build_reverse_assembly.sh` into
`ReverseClosure_Assembly.lean`, the file that is actually compiled.

Prose source: main's `experiments/viewpoints/V007/separator.md` §1.1 and
`affine_growth.md` §3 ("reverse closure"). Throughout, `b : ℕ → α` satisfies the
three scalar identities `b(3n) = b(4n)`, `b(3n+2) = b(2n+1)`, `b(4n+2) = b(n)`
(V005's interface), and `c(n) = b(2n)`.

* `kernel3_c_finite`: a finite 3-kernel of `b` gives a finite 3-kernel of `c`
  (`c(3^a n + r) = f(2n + q)` for a ternary section `f` of `b`, `q ∈ {0,1}`);
* `union_binary_closed`: `K₃(b) ∪ K₃(c)` is closed under both binary sections —
  the four displayed cases of V007 §1.1, one scalar identity each;
* `kernel2_subset_union`, `binary_automatic_of_ternary`: hence `K₂(b) ⊆ K₃(b) ∪ K₃(c)`
  and a 3-automatic `b` is 2-automatic;
* `kernel2_ext_subset`, `ext_automatic_of_automatic`: `K₂(ext b) ⊆ {ext b} ∪ K₂(b)`
  (V005's `K_D(h) = {h} ∪ K_{D−1}(b)` without the depth bookkeeping);
* `ternary_automatic_of_binary`, `automatic_two_iff_three`: the converse through
  V004's `K₃(b) ⊆ K₊(ext b) ⊆ K₂(ext b)`; so for a scalar sequence of an invariant
  colouring, **2-automatic ⇔ 3-automatic**, with no external input;
* `constant_of_ternary_automatic`: assuming `CobhamStatement α`, a 3-automatic `b`
  with the three identities is constant, `b n = b 0` (via `automatic_rigidity`).

Not formalised: V005's reconstruction of `b` from an arbitrary positive binary
section `g` of `h` (so the statements here are about `b` itself, which is V007's
first paragraph of §1.1), and the singleton-exit theorem (V007-b). No convergence
statement is involved.
-/

namespace LeanLane
namespace RevClos

open V004

variable {α : Type*}

/-- `c(n) = b(2n)`. -/
def c (b : ℕ → α) : ℕ → α := fun n => b (2 * n)

/-- Every ternary section of `c` is `n ↦ f (2n + q)`, `q ∈ {0,1}`, for a ternary
section `f` of `b`: write `2r = q·3^e + s`. -/
theorem kernel3_c_subset (b : ℕ → α) :
    Kernel 3 (c b) ⊆
      (fun p : (ℕ → α) × ℕ => fun n => p.1 (2 * n + p.2)) ''
        (Kernel 3 b ×ˢ ({0, 1} : Set ℕ)) := by
  rintro g ⟨e, r, hr, rfl⟩
  have hq : 2 * r / 3 ^ e < 2 := Nat.div_lt_of_lt_mul (by omega)
  refine ⟨(fun n => b (3 ^ e * n + 2 * r % 3 ^ e), 2 * r / 3 ^ e),
    ⟨⟨e, 2 * r % 3 ^ e, Nat.mod_lt _ (by positivity), rfl⟩, ?_⟩, ?_⟩
  · rcases Nat.le_one_iff_eq_zero_or_eq_one.mp (Nat.lt_succ_iff.mp hq) with h0 | h1
    · rw [h0]; simp
    · rw [h1]; simp
  · funext n
    show b (3 ^ e * (2 * n + 2 * r / 3 ^ e) + 2 * r % 3 ^ e) = b (2 * (3 ^ e * n + r))
    congr 1
    have hdm := Nat.div_add_mod (2 * r) (3 ^ e)
    calc 3 ^ e * (2 * n + 2 * r / 3 ^ e) + 2 * r % 3 ^ e
        = 3 ^ e * (2 * n) + (3 ^ e * (2 * r / 3 ^ e) + 2 * r % 3 ^ e) := by ring
      _ = 3 ^ e * (2 * n) + 2 * r := by rw [hdm]
      _ = 2 * (3 ^ e * n + r) := by ring

theorem kernel3_c_finite (b : ℕ → α) (hb : KAutomatic 3 b) : KAutomatic 3 (c b) :=
  ((hb.prod ((Set.finite_singleton 1).insert 0)).image _).subset (kernel3_c_subset b)

/-- **V007 §1.1, the four cases.** Binary sections of `K₃(b) ∪ K₃(c)` stay in the union:
with `v = 3^a i + r = 2w` or `2w+1`, the section of `b(3^a n + r)` is `c(3^a n + w)` or
`b(3^(a+1) n + 3w + 2)`, and the section of `c(3^a n + r)` is `b(3^(a+1) n + 3w)` or
`b(3^a n + w)`. -/
theorem union_binary_closed (b : ℕ → α)
    (I1 : ∀ n, b (3 * n) = b (4 * n)) (I2 : ∀ n, b (3 * n + 2) = b (2 * n + 1))
    (I3 : ∀ n, b (4 * n + 2) = b n) :
    ∀ g ∈ Kernel 3 b ∪ Kernel 3 (c b), ∀ i, i < 2 →
      (fun n => g (2 * n + i)) ∈ Kernel 3 b ∪ Kernel 3 (c b) := by
  rintro g (⟨a, r, hr, rfl⟩ | ⟨a, r, hr, rfl⟩) i hi
  · have hi' : 3 ^ a * i ≤ 3 ^ a := by
      calc 3 ^ a * i ≤ 3 ^ a * 1 := Nat.mul_le_mul_left _ (by omega)
        _ = 3 ^ a := mul_one _
    rcases Nat.even_or_odd (3 ^ a * i + r) with ⟨w, hw⟩ | ⟨w, hw⟩
    · -- `v = 2w`: a ternary section of `c` at offset `w`
      right
      refine ⟨a, w, by omega, funext fun n => ?_⟩
      show b (3 ^ a * (2 * n + i) + r) = b (2 * (3 ^ a * n + w))
      congr 1
      calc 3 ^ a * (2 * n + i) + r = 2 * (3 ^ a * n) + (3 ^ a * i + r) := by ring
        _ = 2 * (3 ^ a * n) + (w + w) := by rw [hw]
        _ = 2 * (3 ^ a * n + w) := by ring
    · -- `v = 2w+1`: `b(2m+1) = b(3m+2)` gives depth `a+1`, offset `3w+2`
      left
      refine ⟨a + 1, 3 * w + 2, by rw [pow_succ]; omega, funext fun n => ?_⟩
      show b (3 ^ a * (2 * n + i) + r) = b (3 ^ (a + 1) * n + (3 * w + 2))
      rw [show 3 ^ a * (2 * n + i) + r = 2 * (3 ^ a * n + w) + 1 by
          calc 3 ^ a * (2 * n + i) + r = 2 * (3 ^ a * n) + (3 ^ a * i + r) := by ring
            _ = 2 * (3 ^ a * n) + (2 * w + 1) := by rw [hw]
            _ = 2 * (3 ^ a * n + w) + 1 := by ring,
        ← I2, pow_succ]
      congr 1
      ring
  · have hi' : 3 ^ a * i ≤ 3 ^ a := by
      calc 3 ^ a * i ≤ 3 ^ a * 1 := Nat.mul_le_mul_left _ (by omega)
        _ = 3 ^ a := mul_one _
    rcases Nat.even_or_odd (3 ^ a * i + r) with ⟨w, hw⟩ | ⟨w, hw⟩
    · -- `v = 2w`: `b(4m) = b(3m)` gives depth `a+1`, offset `3w`
      left
      refine ⟨a + 1, 3 * w, by rw [pow_succ]; omega, funext fun n => ?_⟩
      show b (2 * (3 ^ a * (2 * n + i) + r)) = b (3 ^ (a + 1) * n + 3 * w)
      rw [show 2 * (3 ^ a * (2 * n + i) + r) = 4 * (3 ^ a * n + w) by
          calc 2 * (3 ^ a * (2 * n + i) + r) = 4 * (3 ^ a * n) + 2 * (3 ^ a * i + r) := by ring
            _ = 4 * (3 ^ a * n) + 2 * (w + w) := by rw [hw]
            _ = 4 * (3 ^ a * n + w) := by ring,
        ← I1, pow_succ]
      congr 1
      ring
    · -- `v = 2w+1`: `b(4m+2) = b(m)` gives depth `a`, offset `w`
      left
      refine ⟨a, w, by omega, funext fun n => ?_⟩
      show b (2 * (3 ^ a * (2 * n + i) + r)) = b (3 ^ a * n + w)
      rw [show 2 * (3 ^ a * (2 * n + i) + r) = 4 * (3 ^ a * n + w) + 2 by
          calc 2 * (3 ^ a * (2 * n + i) + r) = 4 * (3 ^ a * n) + 2 * (3 ^ a * i + r) := by ring
            _ = 4 * (3 ^ a * n) + 2 * (2 * w + 1) := by rw [hw]
            _ = 4 * (3 ^ a * n + w) + 2 := by ring,
        I3]

/-- The binary kernel of `b` lies in `K₃(b) ∪ K₃(c)` (induction on the binary depth,
peeling the most significant digit). -/
theorem kernel2_subset_union (b : ℕ → α)
    (I1 : ∀ n, b (3 * n) = b (4 * n)) (I2 : ∀ n, b (3 * n + 2) = b (2 * n + 1))
    (I3 : ∀ n, b (4 * n + 2) = b n) :
    Kernel 2 b ⊆ Kernel 3 b ∪ Kernel 3 (c b) := by
  rintro g ⟨e, j, hj, rfl⟩
  induction e generalizing j with
  | zero =>
    have hj0 : j = 0 := by rw [pow_zero] at hj; omega
    subst hj0
    left
    exact ⟨0, 0, by norm_num, funext fun n => by simp⟩
  | succ e ih =>
    have hj2 : j < 2 ^ e * 2 := by rw [← pow_succ]; exact hj
    have hi : j / 2 ^ e < 2 := Nat.div_lt_of_lt_mul hj2
    have hj' : j % 2 ^ e < 2 ^ e := Nat.mod_lt _ (by positivity)
    have key : (fun n => b (2 ^ (e + 1) * n + j)) =
        fun n => (fun m => b (2 ^ e * m + j % 2 ^ e)) (2 * n + j / 2 ^ e) := by
      funext n
      show b (2 ^ (e + 1) * n + j) = b (2 ^ e * (2 * n + j / 2 ^ e) + j % 2 ^ e)
      congr 1
      have hdm := Nat.div_add_mod j (2 ^ e)
      calc 2 ^ (e + 1) * n + j = 2 ^ e * (2 * n) + j := by ring
        _ = 2 ^ e * (2 * n) + (2 ^ e * (j / 2 ^ e) + j % 2 ^ e) := by rw [hdm]
        _ = 2 ^ e * (2 * n + j / 2 ^ e) + j % 2 ^ e := by ring
    rw [key]
    exact union_binary_closed b I1 I2 I3 _ (ih _ hj') _ hi

/-- **Reverse closure (V007 §1.1).** A 3-automatic scalar sequence is 2-automatic. -/
theorem binary_automatic_of_ternary (b : ℕ → α)
    (I1 : ∀ n, b (3 * n) = b (4 * n)) (I2 : ∀ n, b (3 * n + 2) = b (2 * n + 1))
    (I3 : ∀ n, b (4 * n + 2) = b n) (hb : KAutomatic 3 b) : KAutomatic 2 b :=
  (hb.union (kernel3_c_finite b hb)).subset (kernel2_subset_union b I1 I2 I3)

/-! ### The binary kernel of the odd-part extension -/

theorem ext_pow_two_mul (b : ℕ → α) (v x : ℕ) :
    Scalar.ext b (2 ^ v * x) = Scalar.ext b x := by
  induction v with
  | zero => simp
  | succ v ih => rw [pow_succ, mul_comm (2 ^ v) 2, mul_assoc, Scalar.ext_two_mul, ih]

/-- `K₂(ext b) ⊆ {ext b} ∪ K₂(b)`: a zero offset gives `ext b` itself, and a positive
offset `2^v (2j'+1)` at depth `v + k + 1` gives the section of `b` at depth `k`,
offset `j'`. -/
theorem kernel2_ext_subset (b : ℕ → α) :
    Kernel 2 (Scalar.ext b) ⊆ {Scalar.ext b} ∪ Kernel 2 b := by
  rintro g ⟨e, j, hj, rfl⟩
  rcases Nat.eq_zero_or_pos j with rfl | hj0
  · left
    show (fun n => Scalar.ext b (2 ^ e * n + 0)) = Scalar.ext b
    funext n
    rw [add_zero, ext_pow_two_mul]
  · right
    obtain ⟨v, m, hm2, rfl⟩ := Nat.exists_eq_pow_mul_and_not_dvd hj0.ne' 2 (by norm_num)
    obtain ⟨j', rfl⟩ : Odd m := Nat.not_even_iff_odd.mp (fun he => hm2 (even_iff_two_dvd.mp he))
    have hve : v < e := by
      rcases Nat.lt_or_ge v e with hve | hle
      · exact hve
      · exfalso
        have h1 := Nat.pow_le_pow_right (by norm_num : 0 < 2) hle
        have h2 := Nat.le_mul_of_pos_right (2 ^ v) (by omega : 0 < 2 * j' + 1)
        omega
    obtain ⟨k, rfl⟩ : ∃ k, e = v + k + 1 := ⟨e - v - 1, by omega⟩
    have hjk : j' < 2 ^ k := by
      have hlt : 2 ^ v * (2 * j' + 1) < 2 ^ v * (2 * 2 ^ k) := by
        calc 2 ^ v * (2 * j' + 1) < 2 ^ (v + k + 1) := hj
          _ = 2 ^ v * (2 * 2 ^ k) := by ring
      have := Nat.lt_of_mul_lt_mul_left hlt
      omega
    refine ⟨k, j', hjk, funext fun n => ?_⟩
    show Scalar.ext b (2 ^ (v + k + 1) * n + 2 ^ v * (2 * j' + 1)) = b (2 ^ k * n + j')
    rw [show 2 ^ (v + k + 1) * n + 2 ^ v * (2 * j' + 1) = 2 ^ v * (2 * (2 ^ k * n + j') + 1) by
        ring,
      ext_pow_two_mul, Scalar.ext_two_mul_add_one]

theorem ext_automatic_of_automatic (b : ℕ → α) (hb : KAutomatic 2 b) :
    KAutomatic 2 (Scalar.ext b) :=
  ((Set.finite_singleton _).union hb).subset (kernel2_ext_subset b)

/-- The forward direction through V004: a 2-automatic scalar sequence of an invariant
colouring is 3-automatic (`K₃(b) ⊆ K₊(ext b) ⊆ K₂(ext b)`). -/
theorem ternary_automatic_of_binary (b : ℕ → α)
    (I1 : ∀ n, b (3 * n) = b (4 * n)) (I2 : ∀ n, b (3 * n + 2) = b (2 * n + 1))
    (I3 : ∀ n, b (4 * n + 2) = b n) (hb : KAutomatic 2 b) : KAutomatic 3 b := by
  have htri := (Scalar.ext_tri_iff b).mpr ⟨I1, I2, I3⟩
  have hK : KAutomatic 2 (Scalar.ext b) := ext_automatic_of_automatic b hb
  have hsub : Kernel 3 (fun n => Scalar.ext b (2 * n + 1)) ⊆ Kernel 2 (Scalar.ext b) :=
    (kernel3_b_subset (Scalar.ext b) (Scalar.ext_two_mul b) htri).trans
      (Kplus_subset_kernel _)
  have hfun : (fun n => Scalar.ext b (2 * n + 1)) = b := funext (Scalar.ext_two_mul_add_one b)
  rw [hfun] at hsub
  exact hK.subset hsub

/-- **Two-base symmetry.** For a scalar sequence satisfying the three identities,
binary and ternary automaticity coincide; no external theorem is used. -/
theorem automatic_two_iff_three (b : ℕ → α)
    (I1 : ∀ n, b (3 * n) = b (4 * n)) (I2 : ∀ n, b (3 * n + 2) = b (2 * n + 1))
    (I3 : ∀ n, b (4 * n + 2) = b n) : KAutomatic 2 b ↔ KAutomatic 3 b :=
  ⟨ternary_automatic_of_binary b I1 I2 I3, binary_automatic_of_ternary b I1 I2 I3⟩

/-- **V007 §1.1 consequence, modulo Cobham.** A 3-automatic scalar sequence with the
three identities is constant. -/
theorem constant_of_ternary_automatic (cobham : CobhamStatement α) (b : ℕ → α)
    (I1 : ∀ n, b (3 * n) = b (4 * n)) (I2 : ∀ n, b (3 * n + 2) = b (2 * n + 1))
    (I3 : ∀ n, b (4 * n + 2) = b n) (hb : KAutomatic 3 b) : ∀ n, b n = b 0 := by
  have htri := (Scalar.ext_tri_iff b).mpr ⟨I1, I2, I3⟩
  have hK := ext_automatic_of_automatic b (binary_automatic_of_ternary b I1 I2 I3 hb)
  have hconst := automatic_rigidity cobham (Scalar.ext b) (Scalar.ext_two_mul b) htri hK
  intro n
  have := hconst (2 * n + 1) (by omega)
  rwa [Scalar.ext_two_mul_add_one, Scalar.ext_one] at this

end RevClos
end LeanLane
