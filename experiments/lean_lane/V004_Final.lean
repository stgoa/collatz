/-!
# V004-iii — Assembly: binary-automatic Collatz-invariant colourings are constant,
modulo Cobham's theorem

This part is concatenated after `OddEventuallyPeriodic.lean` (V004-i) and
`KernelClosure.lean` (V004-ii) by `build_assembly.sh` into `V004_Assembly.lean`,
the file that is actually compiled.

Definitions. `Kernel k f` is the `k`-kernel of `f : ℕ → α`, the set of
sections `n ↦ f (k^e n + j)` with `j < k^e`; `KAutomatic k f` says it is
finite (Eilenberg's characterisation of `k`-automatic sequences, taken here
as the definition). `CobhamStatement α` is Cobham's theorem in this
formulation, quantified over **every** `f : ℕ → α`: a sequence with finite
2-kernel and finite 3-kernel is eventually periodic. It is the single
external input; it is not proved here and is not in Mathlib.
`finite_range_of_kernel2` records that a finite 2-kernel already forces a
finite range, so the hypothesis is the classical theorem for finite
alphabets and nothing stronger is being assumed.

Theorem `automatic_rigidity`: assuming `CobhamStatement α`, every `h : ℕ → α`
with `h (2n) = h n` for all `n`, `h (3n+1) = h n` for all odd `n > 1`, and
finite 2-kernel is constant on the positive integers. This is main's V004
theorem (`experiments/viewpoints/V004/GLOBAL_RIGIDITY.md`, §1) with its
external input made explicit in the hypotheses. No convergence statement is
involved.
-/

namespace LeanLane
namespace V004

variable {α : Type*}

/-- The `k`-kernel of `f`: all sections `n ↦ f (k^e n + j)` with `j < k^e`. -/
def Kernel (k : ℕ) (f : ℕ → α) : Set (ℕ → α) :=
  {g | ∃ e j : ℕ, j < k ^ e ∧ g = fun n => f (k ^ e * n + j)}

/-- Automaticity in base `k`, in Eilenberg's kernel formulation. -/
def KAutomatic (k : ℕ) (f : ℕ → α) : Prop := (Kernel k f).Finite

/-- **Cobham's theorem** (kernel form), as a named hypothesis quantified over every
sequence with values in `α`: finite 2-kernel and finite 3-kernel imply eventual
periodicity. -/
def CobhamStatement (α : Type*) : Prop :=
  ∀ f : ℕ → α, KAutomatic 2 f → KAutomatic 3 f →
    ∃ N M : ℕ, 0 < M ∧ ∀ n, N ≤ n → f (n + M) = f n

/-- A finite 2-kernel forces a finite range: `f m` is the value at `0` of the
section with `e = m`, `j = m`. -/
theorem finite_range_of_kernel2 (f : ℕ → α) (hK : KAutomatic 2 f) :
    (Set.range f).Finite := by
  apply (hK.image (fun g => g 0)).subset
  rintro _ ⟨m, rfl⟩
  exact ⟨fun n => f (2 ^ m * n + m), ⟨m, m, Nat.lt_two_pow_self, rfl⟩, by simp⟩

/-- V004's positive-offset family `K₊`. -/
def Kplus (h : ℕ → α) : Set (ℕ → α) :=
  {g | ∃ a r : ℕ, 1 ≤ a ∧ 0 < r ∧ r < 2 ^ a ∧ g = fun n => h (2 ^ a * n + r)}

theorem Kplus_subset_kernel (h : ℕ → α) : Kplus h ⊆ Kernel 2 h := by
  rintro g ⟨a, r, -, -, hr, rfl⟩
  exact ⟨a, r, hr, rfl⟩

/-- The 2-kernel of the odd restriction `b n = h (2n+1)` lies in the 2-kernel of `h`. -/
theorem kernel2_b_subset (h : ℕ → α) :
    Kernel 2 (fun n => h (2 * n + 1)) ⊆ Kernel 2 h := by
  rintro g ⟨e, j, hj, rfl⟩
  refine ⟨e + 1, 2 * j + 1, ?_, funext fun n => ?_⟩
  · rw [pow_succ]
    omega
  · show h (2 * (2 ^ e * n + j) + 1) = h (2 ^ (e + 1) * n + (2 * j + 1))
    congr 1
    rw [pow_succ]
    ring

/-- Every iterated ternary section of `b` is a positive-offset section of `h`
(induction on the number of ternary digits, using `kernel_ternary_closure`). -/
theorem b_sections (h : ℕ → α) (hdbl : ∀ n, h (2 * n) = h n)
    (htri : ∀ n, Odd n → 1 < n → h (3 * n + 1) = h n) :
    ∀ e j, j < 3 ^ e → ∃ a r, 1 ≤ a ∧ 0 < r ∧ r < 2 ^ a ∧
      ∀ n, h (2 * (3 ^ e * n + j) + 1) = h (2 ^ a * n + r) := by
  intro e
  induction e with
  | zero =>
    intro j hj
    have hj0 : j = 0 := by simpa using hj
    subst hj0
    exact ⟨1, 1, le_rfl, by norm_num, by norm_num, fun n => by congr 1; ring⟩
  | succ e ih =>
    intro j hj
    have hj3 : j < 3 ^ e * 3 := by rw [← pow_succ]; exact hj
    obtain ⟨q, m, hqm, hq3, hm⟩ : ∃ q m, j = 3 ^ e * q + m ∧ q < 3 ∧ m < 3 ^ e :=
      ⟨j / 3 ^ e, j % 3 ^ e, (Nat.div_add_mod j (3 ^ e)).symm, Nat.div_lt_of_lt_mul hj3,
        Nat.mod_lt _ (by positivity)⟩
    subst hqm
    obtain ⟨a, r, ha, hr0, hr, hsec⟩ := ih m hm
    obtain ⟨a', r', ha', hr0', hr', hcl⟩ :=
      Kernel.kernel_ternary_closure h hdbl htri ha hr0 hr hq3
    refine ⟨a', r', ha', hr0', hr', fun n => ?_⟩
    rw [show 3 ^ (e + 1) * n + (3 ^ e * q + m) = 3 ^ e * (3 * n + q) + m by rw [pow_succ]; ring,
      hsec (3 * n + q)]
    exact hcl n

/-- The 3-kernel of `b` lies in `K₊`. -/
theorem kernel3_b_subset (h : ℕ → α) (hdbl : ∀ n, h (2 * n) = h n)
    (htri : ∀ n, Odd n → 1 < n → h (3 * n + 1) = h n) :
    Kernel 3 (fun n => h (2 * n + 1)) ⊆ Kplus h := by
  rintro g ⟨e, j, hj, rfl⟩
  obtain ⟨a, r, ha, hr0, hr, hsec⟩ := b_sections h hdbl htri e j hj
  exact ⟨a, r, ha, hr0, hr, funext fun n => hsec n⟩

/-- **Binary-automatic rigidity (V004), modulo Cobham.** Assuming Cobham's theorem
for sequences in `α`, every colouring with `h (2n) = h n`, `h (3n+1) = h n` at odd
`n > 1`, and finite 2-kernel is constant on the positive integers. -/
theorem automatic_rigidity (cobham : CobhamStatement α) (h : ℕ → α)
    (hdbl : ∀ n, h (2 * n) = h n) (htri : ∀ n, Odd n → 1 < n → h (3 * n + 1) = h n)
    (hK : KAutomatic 2 h) : ∀ n, 0 < n → h n = h 1 := by
  have hb2 : KAutomatic 2 (fun n => h (2 * n + 1)) := hK.subset (kernel2_b_subset h)
  have hb3 : KAutomatic 3 (fun n => h (2 * n + 1)) :=
    (hK.subset (Kplus_subset_kernel h)).subset (kernel3_b_subset h hdbl htri)
  obtain ⟨N, M, hM, hev⟩ := cobham _ hb2 hb3
  exact OddEP.odd_eventually_periodic_const h hdbl htri hM hev

end V004
end LeanLane
