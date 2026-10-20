module

/-
P6-004 statement correspondence audit.
Generated from pinned AxiomMath/CollatzPositiveDensity Challenge/Basic.lean at
3a38bfbb70379e051b51155def1423846fab3a90.
Source SHA256: e3e828be137de84f97cee84c4635f5f726fb975d1641dacff3b213130f5bf235.
The specification definitions and theorem types are copied unchanged into a new namespace;
only the import and theorem proof terms are replaced. No external code was executed to
generate this file. A successful later compile is required before claiming correspondence.
-/

public import Solution.Basic

/-! # The formal challenge file, written by humans

This is a human-written file certifying the formal statements that this repository proves.

-/

@[expose] public section

namespace LauStatementAudit

open Finset

/-- The Collatz map: `n ↦ n / 2` for even `n`, and `n ↦ 3n + 1` for odd `n`. -/
def collatz (n : ℕ) : ℕ :=
  if n % 2 = 0 then n / 2 else 3 * n + 1

/-- The orbit of `f` starting from `n` reaches target within `steps` steps. -/
@[reducible]
def ReachWithin {α : Type*} (f : α → α) (target n : α) (steps : ℕ) : Prop :=
  ∃ r ≤ steps, f^[r] n = target

/-- The density constant `c = 1 / 2^2^2^87640`. -/
def collatzDensity : ℚ :=
  1 / 2 ^ 2 ^ 2 ^ 87640

/-- The cutoff `X₀ = 2^2^2^2^87640`. -/
def collatzDensityThreshold : ℕ :=
  2 ^ 2 ^ 2 ^ 2 ^ 87640

/-- **The explicit density theorem**, ordinary clock: for every `N ≥ X₀`, at least `c N` of the
`n < N` reach `1` in at most `⌊10.46 log n⌋` Collatz steps. A direct corollary of the joint theorem
below. -/
theorem positive_density_collatz_reaches_one {N : ℕ} (hN : collatzDensityThreshold ≤ N) :
    collatzDensity * N ≤ #{n ∈ range N | ReachWithin collatz 1 n ⌊(10.46 : ℝ) * Real.log n⌋₊} :=
  _root_.positive_density_collatz_reaches_one hN

section with_accel

/-- Accelerated Collatz map, aka Syracuse map. Sends odd `n` to `3n + 1` divided by the highest
power of 2 that divides `3n + 1`. -/
def collatzAccel (n : ℕ) : ℕ :=
  (3 * n + 1) / 2 ^ padicValNat 2 (3 * n + 1)

/-- **The explicit density theorem**, both clocks at once: for every `N ≥ X₀`, at least `c N` of
odd starting values `n < N` reach `1` in at most `⌊10.46 log n⌋` Collatz steps and
in at most `⌊3.4881 log n⌋` accelerated Collatz steps. -/
theorem positive_density_collatz_and_collatzAccel_reaches_one
    {N : ℕ} (hN : collatzDensityThreshold ≤ N) :
    collatzDensity * N ≤
    #{n ∈ range N | Odd n ∧ ReachWithin collatz 1 n ⌊(10.46 : ℝ) * Real.log n⌋₊ ∧
      ReachWithin collatzAccel 1 n ⌊(3.4881 : ℝ) * Real.log n⌋₊} :=
  _root_.positive_density_collatz_and_collatzAccel_reaches_one hN

end with_accel

section generalized

/-- The density constant `c = 1 / (t^4 * 2^2^2^87640)`. -/
def collatzDensityDep (t : ℕ) : ℚ :=
  1 / (t ^ 4 * 2 ^ 2 ^ 2 ^ 87640)

/-- The cutoff `X₀ = 2^(s^3 * 2^2^2^87640)`. -/
def collatzDensityThresholdDep (t : ℕ) : ℕ :=
  2 ^ (t ^ 3 * 2 ^ 2 ^ 2 ^ 87640)

/-- **The generalized explicit density theorem**, both clocks at once:
for any `t` coprime to `6`, for every `N ≥ X₀(t)`, at least `c(t) N` of odd starting values `n < N`
reach `t` in at most `⌊10.46 log (n/t)⌋` Collatz steps and
in at most `⌊3.4881 log (n/s)⌋` accelerated Collatz steps. -/
theorem positive_density_collatz_and_collatzAccel_reaches_of_coprime_six
    {t : ℕ} (ht : t.Coprime 6) {N : ℕ} (hN : collatzDensityThresholdDep t ≤ N) :
    collatzDensityDep t * N ≤
    #{n ∈ range N | Odd n ∧ ReachWithin collatz t n ⌊(10.46 : ℝ) * Real.log (n / t)⌋₊ ∧
      ReachWithin collatzAccel t n ⌊(3.4881 : ℝ) * Real.log (n / t)⌋₊} :=
  _root_.positive_density_collatz_and_collatzAccel_reaches_of_coprime_six ht hN

/-- **The generalized explicit density theorem**, even targets permitted:
for any `t` not divisible by `3`, for every `N ≥ X₀(t)`,
at least `c(t) N` of odd starting values `n < N`
reach `t` in at most `⌊10.46 log (n/t)⌋` Collatz steps and
reach the odd part of `t` in at most `⌊3.4881 log (n/t)⌋` accelerated Collatz steps. -/
theorem positive_density_collatz_and_collatzAccel_reaches_of_not_three_dvd
    {t : ℕ} (ht : ¬3 ∣ t) {N : ℕ} (hN : collatzDensityThresholdDep t ≤ N) :
    collatzDensityDep t * N ≤
    #{n ∈ range N | Odd n ∧ ReachWithin collatz t n ⌊(10.46 : ℝ) * Real.log (n / t)⌋₊ ∧
      ReachWithin collatzAccel (t / 2 ^ padicValNat 2 t) n ⌊(3.4881 : ℝ) * Real.log (n / t)⌋₊} :=
  _root_.positive_density_collatz_and_collatzAccel_reaches_of_not_three_dvd ht hN

end generalized

end LauStatementAudit

/-!
## Independent namespace comparison and axiom reports

Each local theorem above elaborates its copied specification, then uses only the named
solution theorem as its proof. Successful elaboration checks definitional equality between
the two statements, including the independently named map and constant definitions.
This file does not import Challenge.Basic.
-/

#print axioms _root_.positive_density_collatz_reaches_one
set_option pp.proofs false in
#print _root_.positive_density_collatz_reaches_one

#print axioms _root_.positive_density_collatz_and_collatzAccel_reaches_one
set_option pp.proofs false in
#print _root_.positive_density_collatz_and_collatzAccel_reaches_one

#print axioms _root_.positive_density_collatz_and_collatzAccel_reaches_of_coprime_six
set_option pp.proofs false in
#print _root_.positive_density_collatz_and_collatzAccel_reaches_of_coprime_six

#print axioms _root_.positive_density_collatz_and_collatzAccel_reaches_of_not_three_dvd
set_option pp.proofs false in
#print _root_.positive_density_collatz_and_collatzAccel_reaches_of_not_three_dvd

#print axioms LauStatementAudit.positive_density_collatz_reaches_one
set_option pp.proofs false in
#print LauStatementAudit.positive_density_collatz_reaches_one

#print axioms LauStatementAudit.positive_density_collatz_and_collatzAccel_reaches_one
set_option pp.proofs false in
#print LauStatementAudit.positive_density_collatz_and_collatzAccel_reaches_one

#print axioms LauStatementAudit.positive_density_collatz_and_collatzAccel_reaches_of_coprime_six
set_option pp.proofs false in
#print LauStatementAudit.positive_density_collatz_and_collatzAccel_reaches_of_coprime_six

#print axioms LauStatementAudit.positive_density_collatz_and_collatzAccel_reaches_of_not_three_dvd
set_option pp.proofs false in
#print LauStatementAudit.positive_density_collatz_and_collatzAccel_reaches_of_not_three_dvd

