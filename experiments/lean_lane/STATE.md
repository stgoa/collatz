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
| 1b | General form: components = `⟨×2,×3⟩`-orbits on `Z/gcd(M,d)Z` (both directions) | same, Appendix | queued after 1 | — | — |
| 2 | Digit-count rigidity: every invariant `h = F(s₂(n))` is constant | `experiments/viewpoints/V003/digit_sum.md` | queued | — | — |
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

## Insights sent to the feed

- None yet in this lane (iteration 1).

## Rules in force

A Lean theorem counts only with axioms exactly `{propext, Classical.choice,
Quot.sound}` and a statement-match note. Never claim a proof of Collatz.
Never push to `main` or `claude/sidekick`. One bounded unit per iteration.
