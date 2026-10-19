# Lean lane — LOG

Newest first. Each entry: iteration, target, outcome, axioms, receipts,
and any insight sent to the feed.

## Iteration 9, review — side lane verifies V007-a

- `claude/sidekick` 52244f7 (feed 23:23): V007-a at 6adac5a **verified** —
  independent regeneration of `ReverseClosure_Assembly.lean` byte-identical
  (`c5429174…`), V004 part unchanged (`3d570751…`), ScalarInterface part
  `df3dabd4…`, final part `6a056dec…`; nine declarations with the standard
  axioms; clean scan. It highlighted `automatic_two_iff_three` (Cobham-free,
  two-way, more than V007's prose) and posted the `b(0) = b(1) = b(2)` step
  for V008's first-shell finish.

## Iteration 9 — 2026-10-18, ~23:05 -03

- Woken by the side lane's feed `d0354c2` (my V007 check recorded; D8
  proposed to main). Monitor re-armed after expiry.
- **V007-a verified.** `ReverseClosure_Final.lean` (sha256 `6a056dec…90c2`)
  assembled by `build_reverse_assembly.sh` with `V004_Assembly.lean`
  (regenerated, unchanged) and `ScalarInterface.lean` into
  `ReverseClosure_Assembly.lean` (sha256 `c5429174…9883`, 1160 lines).
  `LeanLane.RevClos.binary_automatic_of_ternary` (V007 §1.1 reverse
  closure), `kernel2_ext_subset` (`K₂(ext b) ⊆ {ext b} ∪ K₂(b)`),
  `ternary_automatic_of_binary`, `automatic_two_iff_three` (2-automatic ⇔
  3-automatic for scalar sequences of invariant colourings, no external
  input), `constant_of_ternary_automatic` (modulo `CobhamStatement α`);
  axioms `[propext, Classical.choice, Quot.sound]`. Two compile rounds:
  the first had two errors in `kernel3_c_subset` (an `omega` that lost
  the division atom `2r / 3^e` — replaced by `Nat.le_one_iff_eq_zero_or_eq_one`;
  and a `show` with the image equation's sides swapped); the second has
  no diagnostics.
- Main pushed `9d66b69` (V008: two-exit counterexample, first-shell
  theorem, uniform future-cut lemma; dated Cobham notes added to
  V005–V007) during the build; read and checked (sound; details in
  STATE.md "Insights"). Queue: V006-a next, V008-a (first-shell theorem)
  queued as a candidate, V007-b larger.

## Iteration 8 — 2026-10-18, ~22:50 -03

- Woken by the monitor: main pushed `ceebb93` (V006, quadratic separation
  and the full graph constraints). Read REPORT, overlap, QUADRATIC_REVIEW,
  graph_interface, the AGENTS/RESULTS/brief diffs and `verify_examples.py`.
  Verdict sent to the side lane: the quadratic theorem is correct and
  elementary; the Collatz corollary's reduction to non-periodic `F` runs
  through V005/V004, hence Cobham, which main's text does not record (the
  side lane confirmed and posted it, feed `d407b8d`); the controls and
  graph identities check out. Details in STATE.md, "Insights".
- **Item 1b verified.** `GeneralPeriodic.lean` (sha256 `95555318…b7ab`,
  414 lines, `import Mathlib` only): `LeanLane.GenPer.invariant_classification`
  (every odd `d`, `M > 0`: period `gcd(M,d)`, `h(2n) = h(n)`,
  `h(3n) = h(n)`), `factors_through_zmod` (explicit `F : ZMod (gcd M d) → α`
  invariant under `×2`, `×3`), `invariant_of_class_function` (converse for
  every `g ∣ d`), `period_gcd_six_free` (period `gcd(M', d)` for the six-free
  part `M'`), `eventually_periodic_invariant`, `control_indicator` with
  instances `control_five`, `control_sixty_one`; axioms
  `[propext, Classical.choice, Quot.sound]` (converse `[propext]`,
  `period_gcd` `[propext, Quot.sound]`). Compiled on the first attempt with
  three linter warnings (two unused simp arguments, one `haveI`), fixed;
  the second build has no diagnostics. The side lane's independent proof
  sketch (feed, 22:2x) and its 6,000-case residue-graph check agree; the
  Lean route (odd rule extended to every `x` via `x+M`/`x+2M`) is the one
  described to it.
- Side lane verdicts received this iteration: V005-a **verified** (feed
  22:26, `bc76c7d`), with the bijection remark posted for main; my V006
  Cobham-scope point posted (feed 22:32, `d407b8d`) after the side lane
  checked it against main's text.
- Main pushed `b24020f` (V007, singleton-exit obstruction and reverse
  closure) while 1b was being committed. Read REPORT, separator,
  affine_growth, INDEPENDENT_REVIEW, side_review and the AGENTS/RESULTS/
  brief diffs; verdict sent (sound; the Collatz application of hypothesis
  (I) is conditional on Cobham through V005/V004, unstated). Queue
  re-prioritised: V007-a (reverse closure) next, then V006-a.
- Side lane verdict on 1b (feed 22:42, `7d9a267`): **verified** — statement
  match with V002 §4/Appendix as refined, converse for every `g ∣ d`, the
  `n > 1` restriction harmless under periodicity, six-free refinement
  covers its `3 ∣ d` remark, controls correct, axioms as reported, no
  `native_decide`, hash match. It suggests a later target: the `d`-version
  of the closure up to bounded shifts (`D_UNIFORM_AUTOMATIC.md` Step 1),
  which with `eventually_periodic_invariant` would give "automatic
  invariants of `3x+d` are the `⟨×2,×3⟩` class functions mod `d`" modulo
  `CobhamStatement`; noted as a candidate after V007-a/V006-a.

## Iteration 7 — 2026-10-18, ~22:30 -03

- **V005-a verified.** `ScalarInterface.lean` (sha256 `df3dabd4…26f5`,
  `import Mathlib` only): `LeanLane.Scalar.ext_tri_iff` — main's
  equivalence: the odd-part extension `ext b x = b((oddPart x − 1)/2)`
  satisfies `h(3n+1) = h(n)` at odd `n > 1` iff `b(3n) = b(4n)`,
  `b(3n+2) = b(2n+1)`, `b(4n+2) = b(n)` for all `n` — with
  `ext_three_mul_add_two` (main's `E(m)` induction, cases `m` odd / `4l` /
  `4l+2`), `ext_tri` (the rule then holds at every odd `n`, including 1),
  `scalar_interface_iff` (identities ⇔ odd-value sequence of an invariant
  colouring), `ext_odd_values` (round trip on positives, so the
  correspondence is a bijection), `v004_relation` (`b(3n+1) = b(16n+8)`);
  axioms `[propext, Classical.choice, Quot.sound]` (`v004_relation` only
  `[propext, Quot.sound]`). Compiled with no diagnostics on the first
  attempt. The side lane's 22:10 sketch used the same three-case split.
- Monitor re-armed after expiry (events: main `85a07c2`, already read, and
  the side lane's feed `3f6f147`). Main unchanged.

## Iteration 6, review — side lane verifies item 4 (partial)

- `claude/sidekick` a114b97/3f6f147 (feed 22:10): item 4 at 2789674
  **verified** (`collatzAccel` matches the audited definition in
  `StatementAudit.lean`; identities, `pair_iff` and the easy direction;
  `R1Converse` a `Prop`, not asserted; standard axioms; hash match; the
  minimal-counterexample remark checked: `2^a m ≡ 70 (mod 108)` forces
  `a = 1`, `m ≡ 35 (mod 54)`). Its exact sparse-control count (`G₂ = 2273`,
  `G₃ = 1631` at `D = 1000`, slopes ≈ 2.3 and 1.7) confirms main's
  `5D+3`/`3D+3` bounds and the saturation remark; Bell's Conjecture 3.4 is
  as main quotes it.

## Iteration 6 — 2026-10-18, ~22:25 -03

- **Item 4 partially verified.** `PairObligation.lean` (sha256
  `3b0e6d2e…d9d8`), importing the audited `Solution.Basic`:
  `collatzAccel_four_mul_add_one`, `collatzAccel_three_mul`, `pair_iff`,
  `accel_reaches_one`, `collatz_imp_pairs_meet`; axioms
  `[propext, Classical.choice, Quot.sound]`. Two compile rounds (a `rw [← hK]`
  that also rewrote the literal `1` inside an exponent; replaced by a `calc`).
  The converse of R.1 is recorded as not formalised (`R1Converse`, a `def`,
  no sorry), with the reason in STATE.md.
- Woken by the side lane's feed commits (main unchanged at `4f1704c`).
- Main pushed `85a07c2` (V005, quantitative rigidity) during this
  iteration; read and assessed (no error found; sparse-control count
  sanity-checked; insight sent). Queue re-prioritised: next unit V005-a,
  the scalar-interface equivalence (converse direction), then 1b.

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
