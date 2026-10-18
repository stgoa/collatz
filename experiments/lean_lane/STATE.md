# Lean lane — STATE

**Updated: 2026-10-18, iteration 1 of the Lean lane. Branch
`claude/lean-lane` (cut from main `8572962`). Collatz remains open.** This
file is the resume point for the self-paced loop. Role: formal verification
of claims made on `main`, plus insights sent to the sidekick's feed.

## Toolchain

Container `leanaudit` (Rancher Desktop, linux/aarch64): elan home
`/opt/.elan`, `leanprover/lean4:v4.35.0-rc2` (commit `11acb17e`), Mathlib
`065356127b1dc0016f66b7283ce0ce2c4055aa55` built in
`/build/CollatzPositiveDensity/.lake` together with the audited
`CollatzPosDens` library. Files are compiled with
`lake env lean <file>` from that project directory (`docker cp` the file to
`/audit/` first). Receipts: build output and `#print axioms` lines in
`receipts/`, hashes of the `.lean` sources alongside.

## Queue

| # | Target | Prose source on main | Status | Axioms | Receipt |
|---|---|---|---|---|---|
| 1 | Periodic rigidity (d=1): every `M`-periodic `h` with `h(2n)=h(n)` and `h(3n+1)=h(n)` (odd `n>1`) is constant on `n>=1`; plus the `3x+5` control (indicator of `5∣n` is a nonconstant 5-periodic invariant) | `experiments/viewpoints/V002/invariant_colors.md` §4, Appendix | **verified** (iteration 1): `PeriodicRigidity.lean`, `LeanLane.periodic_invariant_const`, `LeanLane.control_three_x_plus_five` | `[propext, Classical.choice, Quot.sound]` | `receipts/PeriodicRigidity.{build,axioms,sha256}.txt`, `receipts/toolchain.txt` |
| V004-i | Odd-eventually-periodic rigidity: if `h` satisfies (1) and `n ↦ h(2n+1)` is eventually periodic, `h` is constant on positives (V004 §§2, 5; strictly strengthens target 1) | `experiments/viewpoints/V004/GLOBAL_RIGIDITY.md` §§2, 5 | **verified** (iteration 2): `OddEventuallyPeriodic.lean`, `LeanLane.OddEP.odd_eventually_periodic_const` | `[propext, Classical.choice, Quot.sound]` | `receipts/OddEventuallyPeriodic.{build,axioms,sha256}.txt` |
| V004-ii | Ternary closure of the positive-offset kernel `K₊` (V004 §3), as pure identities of `h`; binary closure; V004's two worked examples | same, §3 | **verified** (iteration 3): `KernelClosure.lean`, `LeanLane.Kernel.kernel_ternary_closure`, `kernel_binary_closure`, `example_12n5`, `example_12n3` | `[propext, Classical.choice, Quot.sound]` (binary closure and the first example need only `[propext, Quot.sound]`) | `receipts/KernelClosure.{build,axioms,sha256}.txt` |
| V004-iii | Assembly: binary-automatic invariant colourings are constant, with Cobham + finite-kernel characterisation as explicit named hypotheses (not in Mathlib) | same, §§1–5 | queued | — | — |
| 1b | General form: components = `⟨×2,×3⟩`-orbits on `Z/gcd(M,d)Z` (both directions); eventual periodicity | V002 Appendix | queued (partly subsumed by V004-i) | — | — |
| 2 | Digit-count rigidity: every invariant `h = F(s₂(n))` is constant | `experiments/viewpoints/V003/digit_sum.md` | queued (subsumed by V004 once iii lands; low priority) | — | — |
| 3 | Dichotomy corollary over `Solution.Basic`: a bad `n` ⇒ positive lower density of the non-absorbed set | lane-3 analysis; `Main.positive_density_collatz_and_collatzAccel_reaches_of_not_three_dvd` | queued | — | — |
| 4 | R40 reduction: Collatz ⇔ ∀ odd `u`, orbits of `u` and `18u+5` meet | `docs/RESULTS.md` R40/R43, `ROUTE_MAP.md` R.1 | queued | — | — |

## Statement-match notes

- Target 1: main's (1) in `invariant_colors.md` §1 is `h(2n)=h(n)` for
  `n>=1` and `h(3n+d)=h(n)` for odd `n>1`, with no identity at the absorber;
  §4/Appendix state "every periodic or eventually periodic d=1 invariant
  coloring is constant". The Lean theorem takes `h : ℕ → α`, `0 < M`,
  `∀ n, h (n+M) = h n`, `∀ n, h (2n) = h n`, `∀ n, Odd n → 1 < n → h (3n+1)
  = h n`, and concludes `∀ n, 0 < n → h n = h 1`. Hypotheses quantified
  over all of ℕ cost nothing: a colouring of the positive integers with
  period `M` extends to `0` by `h 0 := h M`, after which both all-ℕ
  hypotheses hold. So the Lean statement implies main's for every period.
  *Eventual* periodicity (Appendix, last paragraph) and the general
  `gcd(M,d)` classification are not yet formalised (queued under 1b). The
  control matches §5's `3x+5` example with the indicator of `5 ∣ n`.

- V004-i: V004 §5 assumes `b(n) = h(2n+1)` eventually periodic (from Cobham)
  and proves `h` constant; the Lean theorem takes exactly that: `0 < M` and
  `∀ n ≥ N, h(2(n+M)+1) = h(2n+1)`, with the two colouring rules as in
  target 1, and concludes `∀ n > 0, h n = h 1`. The proof differs from the
  prose in form (integer identities `b(4n+2)=b(n)`, `b(3n+2)=b(2n+1)`,
  `b(4n)=b(3n)` instead of the residue map on `Z/LZ`; period `3K ⇒ K` by
  strong induction instead of the `H^{e₃}` descent; translation by
  `c = (L+1)/2` instead of by `1/4`), but it uses only consequences of (1)
  and reaches the same statement. No finiteness of the colour set is needed.

- V004-ii: V004 §3 states that `K₊ = {n ↦ h(2^a n + r) : a ≥ 1, 0 < r < 2^a}`
  is closed under binary and ternary sections, with Case A (`3 ∤ c`,
  `v ∈ {1,2}`, `t = (2^v c − 1)/3`) and Case B (`3 ∣ c`, `t = 2^ℓ u`,
  offset `16u+1`). The Lean theorem states exactly the closure as
  identities: for `a ≥ 1`, `0 < r < 2^a`, `j < 3` there exist `a' ≥ 1`,
  `0 < r' < 2^a'` with `h(2^a(3n+j)+r) = h(2^a' n + r')` for all `n`; the
  witnesses are V004's (`a+v`, `t`) and (`s+4`, `16u+1`). It does not
  mention automata, finiteness or Cobham; those enter only in V004-iii.

## Insights sent to the feed

- Iteration 1 (on main `f54b741`/`4f1704c`, V004): full read of
  `GLOBAL_RIGIDITY.md` and `INDEPENDENT_REVIEW.md`; no gap found in
  identities (2)–(4), the ternary closure of `K₊` (both cases, including
  `n = 0`, `t = 1`), the Cobham application, the eventual→global odd period
  step, or the `Z/mZ` finish (`H∘J` vs `J∘H` differ by the unit `1/4`).
  Assessment sent: written proof modulo Cobham and the finite-kernel
  characterisation, neither in Mathlib; novelty check should start with
  Shallit–Wilson 1992 (Bull. EATCS 46); Lean plan V004-i/ii/iii above.

## Rules in force

A Lean theorem counts only with axioms exactly `{propext, Classical.choice,
Quot.sound}` and a statement-match note. Never claim a proof of Collatz.
Never push to `main` or `claude/sidekick`. One bounded unit per iteration.
