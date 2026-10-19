# Lean lane — LOG

Newest first. Each entry: iteration, target, outcome, axioms, receipts,
and any insight sent to the feed.

## Iteration 5, review — side lane verifies item 3

- `claude/sidekick` 64d7ef5 (feed 21:57): item 3 at b980e52 **verified**
  (ordinary map and clock, natural density, `0 < n` needed since
  `collatz 0 = 0`, proof chain, the single `decide` adds no axiom, standard
  axioms transitively, hash match). Two notes taken: (1) the contrapositive's
  hypothesis is *lower* density zero, stronger than the docstring claimed —
  docstring and STATE corrected (file hash changes; receipts regenerated);
  (2) my message to the side lane mentioned threshold warnings in the build
  receipt, but the final run had none and the committed receipt
  ("exit=0 (no diagnostics)") is the accurate one — the warnings appeared
  only in the failed earlier runs. Correction sent.

## Iteration 5 — 2026-10-18, ~22:05 -03

- **Item 3 verified.** `Dichotomy.lean` (sha256 `02e1f309…665a`), importing
  the audited `Solution.Basic`: `LeanLane.Dichotomy.bad_positive_lower_density`
  (a positive `n` that never reaches 1 under `collatz` ⇒ explicit `c > 0`,
  `X₀` with `c·N ≤ #{n < N : 0 < n ∧ Bad n}` for `N ≥ X₀`) and
  `collatz_of_bad_density_zero` (natural density zero of the bad set ⇒ every
  positive integer reaches 1); axioms `[propext, Classical.choice,
  Quot.sound]`. Four compile rounds, all elaboration issues around the
  tower-sized density constant: `positivity`, `unfold` and a bare `rw`
  overflow the recursion limit on `2^2^2^87640`, as does `norm_cast` on the
  cast inequality; fixed by proving positivity for a general `q` and closing
  by definitional unfolding, and by `Nat.cast_le.mpr`. Deprecated
  `if_pos`/`if_neg` replaced by `split <;> omega`.
- Woken by the side lane's feed commit (main unchanged at `4f1704c`).

## Iteration 4, review — side lane verifies V004-iii

- `claude/sidekick` 3b95686 (feed 21:47): V004-iii at c453d38 **verified**;
  all four checklist items met; `CobhamStatement α` holds for every `α`
  (finite kernel ⇒ finite range ⇒ Eilenberg ⇒ Cobham), so the theorem is
  not vacuous; the Lean statement implies main's §1 since any extension to
  `h 0` keeps the 2-kernel finite. It regenerated `V004_Assembly.lean`
  independently (byte-identical, `3d570751…`), with the two included parts
  hashing to the previously verified files. For item 3 it will check that
  "bad" uses the same map and clock as the audited `Solution.Basic`
  theorems and whether the density is natural or logarithmic.

## Iteration 4 — 2026-10-18, ~21:10 -03

- **V004-iii verified.** `V004_Final.lean` (sha256 `e1f0c727…32e9`)
  assembled with the two earlier files by `build_assembly.sh` into
  `V004_Assembly.lean` (sha256 `3d570751…7e65`, 661 lines), which compiled
  with no diagnostics on the first attempt. `LeanLane.V004.automatic_rigidity`,
  axioms `[propext, Classical.choice, Quot.sound]`; the external input is
  the hypothesis `CobhamStatement α` (Cobham's theorem in kernel form, over
  every `f : ℕ → α`); `finite_range_of_kernel2` shows no separate
  finite-alphabet assumption is needed. With this, **all of main's V004
  theorem is formalised modulo one named classical theorem.**
- Side lane verdict on V004-ii: verified (statement exactly V004 §3 for all
  `n`, V004's witnesses, standard axioms, clean source, hash match); its
  pre-announced V004-iii checklist (general Cobham over every `f`, kernels
  as sets of functions, finite range derived, conclusion from
  `FiniteBinaryKernel h` alone) is met by the statement above.
- Monitor re-armed (previous one expired; both events were sidekick feed
  commits; main unchanged at `4f1704c`).

## Iteration 3 — 2026-10-18, ~21:00 -03

- **V004-ii verified.** `KernelClosure.lean` (sha256 `d533c5fd…1a5a`):
  `LeanLane.Kernel.kernel_ternary_closure` (axioms
  `[propext, Classical.choice, Quot.sound]`), `kernel_binary_closure`,
  `id3` (`h(3u) = h(16u+1)` for odd `u`), and V004's worked examples
  `h(12n+5) = h(8n+3)`, `h(12n+3) = h(64n+17)`. Two compile rounds: one
  `pow_add` rewrite shape and a deprecated `push_neg`.
- Woken by the side lane's feed commit (main unchanged at `4f1704c`);
  nothing new to review on main.

## Iteration 2, review — side lane verifies V004-i

- `claude/sidekick` f81dbc3 (feed 20:49): V004-i at d1e5b23 **verified**
  from source and receipts (statement match with V004's finish; `h 0`
  never constrained; axioms exactly the standard three; source scan clean;
  sha256 match). The side lane also hand-checked the alternative route
  (B1/B2/B4, the mod-4 induction, the `c = (L+1)/2` translation, which is
  by `1/2` where main uses `1/4`). On the audit close-out it reads the
  whole-library rejections as checker coverage limits on the ~441k-
  declaration default-target export (mostly meta code outside the
  theorems' cone); C.1a's status unchanged; "unresolved" label agreed.

## Iteration 2 — 2026-10-18, ~20:45 -03

- **V004-i verified.** `OddEventuallyPeriodic.lean` (sha256
  `cc9bbbaa…e1e9`): `LeanLane.OddEP.odd_eventually_periodic_const`, axioms
  `[propext, Classical.choice, Quot.sound]` (the three identities `B1`,
  `B2`, `B4` need only `[propext, Quot.sound]`). Three compile rounds: the
  first failed because section `variable` hypotheses are not included in
  theorem statements in this Lean (made them explicit binders), plus a
  missing generalisation in the iterate lemma and a reversed `calc`; the
  second left only a redundant final `norm_num`.
- Side lane verdict received: PR #3 **verified** from source and receipts
  (statement match with V002 §4, standard axioms, hash); V004 confirmed by
  its own probe (98,256 kernel sections, 666 moduli, d=5 control); pointer
  to `sidekick/writeup/D_UNIFORM_AUTOMATIC.md` (general-d form: automatic
  invariant colourings are `F(n mod d)` with `F` constant on
  `⟨×2,×3⟩`-orbits; offsets may leave `(0, 2^a)` by a bounded shift). Noted
  for 1b.
- Lean audit closed out: the paranoid comparator passed all five external
  checkers plus the Lean kernel ("Your solution is okay!"); `lake check
  --paranoid` on the whole library had Lean/paranoid/lean4lean accept,
  nanoda OOM-killed (exit 137), con-leche/con-ron "rejected" without a
  printed reason — recorded as unresolved in `experiments/lean_audit/README.md`.

## Iteration 1 — 2026-10-18 late evening

- Branch `claude/lean-lane` cut from main `8572962` (main had merged the
  lane-3 Lean audit as PR #2 at `dda3ee9`). Commit monitor on
  `origin/main` and `origin/claude/sidekick` armed (90 s polling).
- **Target 1 verified.** `PeriodicRigidity.lean` (sha256
  `75607bfe…3d1e`) compiles with `lake env lean` on Lean 4.35.0-rc2 /
  Mathlib `0653561`, no warnings. `#print axioms`:
  `periodic_invariant_const`, `const_of_odd_period`, `succ_eq`,
  `period_div_three`, `control_three_x_plus_five` all
  `[propext, Classical.choice, Quot.sound]`; `period_odd_part` `[propext]`.
  Proof: period drops to its odd part by doubling; a period `3K` drops to
  `K` by strong induction on `n` with a parity split; for an odd period
  coprime to 3, `h(6x+1) = h(x) = h(6x+2)` through odd representatives and
  the invertibility of 6 give `h(n+1) = h(n)`. Two compile rounds: the
  first failed only on two renamed Mathlib lemmas
  (`Nat.exists_mul_mod_eq_one_of_coprime`, `Nat.Coprime.mul_left`).
- Statement match recorded in STATE.md (Lean hypotheses on all of ℕ imply
  main's positive-integer version).
- Insight duty: main pushed `f54b741`/`4f1704c` (V004, "full
  binary-automatic Collatz invariant rigidity") during this iteration.
  Read in full; mathematics checks out modulo Cobham + finite-kernel
  characterisation. Sent the assessment, a literature pointer
  (Shallit–Wilson 1992) and the Lean plan to the sidekick for its feed.
  Queue re-prioritised: V004-i (odd-eventually-periodic rigidity) is the
  next target; it strictly strengthens target 1.
- Draft PR for the lane: stgoa/collatz#3.
