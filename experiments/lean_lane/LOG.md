# Lean lane — LOG

Newest first. Each entry: iteration, target, outcome, axioms, receipts,
and any insight sent to the feed.

## Iteration 15 — 2026-10-19, 01:38 -03

- Woken by the sidekick's push `2ea1c7f` (feed 01:19): **C003-a verified** —
  statement match with C003 §2 (block `u` nonempty because `D_u > 0`; the `Q`
  tie covered by either lemma), axioms 39 × standard, 3 × `[propext,
  Quot.sound]`, 9 × `[propext]`, clean build and scan, sha256 match; the C004
  notes recorded in the feed. Main unchanged at `61cf54a`. Monitor re-armed
  after its expiry.
- **C004-a verified** in `CycleSpectrum.lean` (sha256 `3226ae0c…6333`, 1493
  lines, 75 theorems: 51 with the three standard axioms, 24 needing only
  subsets): `cut_identity` (C004's (6), the `k = 1` commutator),
  `gcd_sub_self_right`, `cut_gcd` ((7) for `a ≥ 1`), the phase words `mech A m
  l` built from `diffWord`, `C_diffWord` (R71's sum derived from the recursive
  `C`), `mech_length`/`mech_sum`/`D_mech`/`mech_pos`, `C_mech`,
  `C_mech_zero_le`/`C_mech_lt_two` (`C_0 ≤ C_l < 2C_0`),
  `step_add_mul`/`step_mod`/ `step_congr` and `mech_rotate` (rotations of
  phase words are phase words), `narrow_mech` (every rotation of the
  mechanical word has intercept in `[C_0, 2C_0)` with `D = 2^A − 3^m`);
  controls `(1,2,2)` → `(2,2,1)`, `(2,1,2)`, intercepts `23, 37, 29`, cut `K =
  −14`. Two compile rounds: clean on the first, then one unused hypothesis
  removed (`C_mech` does not need `0 < m`). Receipts regenerated.

## Iteration 14 — 2026-10-19, 01:15 -03

- Monitor re-armed after its expiry. Main pushed `61cf54a` (C004: narrow
  cycles are mechanical, rotation lattice, close-pair rule refuted); the
  sidekick refereed it at `6b5b73b` (feed 01:06) and merged main (`67c691b`).
  C004 read and checked (STATE "Insights"); no error found; insights sent to
  the sidekick.
- **C003-a verified** in `CycleSpectrum.lean` (sha256 `651c8d08…c601`, 1230
  lines): `fixed_pair_bound_u`/`_v` (C003's (5) as `Q^k·D_v·gcd(C,D) <
  |K|·D_w` and `S^ℓ·D_u·gcd(C,D) < |K|·D_w`),
  `two_pow_mul_C_lt`/`F_mono`/`two_pow_mul_C_lt_M`/`K_bound` ((7)–(9)),
  `uniform_bound_u`/`_v`/`_max_u` (the uniform theorem (6), `2^M
  Q_*^{t_*−3}·gcd(C,D) < D_w`), helpers `G_pos`, `gcd_dvd_K_mul_Gv`/`_Gu`
  (extracted from C002's (5)) and `D_two_pos`, and the `(1,2,2)^3(2)` example.
  Purely algebraic: no cycle states, no integrality. Three compile rounds: an
  unassigned metavariable in `one_le_pow₀ (by norm_num)` inside a term-mode
  `le_mul_of_one_le_right` (then `positivity` ran on `0 ≤ ?b`); fixed by a
  tactic proof with explicit types. Axioms receipt regenerated for all 51
  theorems of the file: 39 with the three standard axioms, 12 needing only
  `[propext]` or `[propext, Quot.sound]`; no diagnostics.
- Clock note: the times in the iteration 12 and 13 headers were estimates and
  are too late; those commits are timestamped 00:31–00:50 -03. From this entry
  on, times come from `date`.

## Iteration 13, review — side lane verifies C002-a; (U1) strengthened

- `claude/sidekick` fe7377a (feed 00:45): C002-a at cf15b22 **verified**
  (hypotheses of (U1) exactly, supporting results read correctly, axioms
  20 × standard + 3 × `[propext]`, clean scan, hash match), with the
  precision note that the formal conclusion `2^m·gcd < D` is the weaker
  `den > 2^m`, whereas main's (U1) states `den > 2^m·U/V`.
- Strengthened in the same file: `uniform_two_block_strong` proves
  `U·2^m·gcd(C,D) < V·D`, i.e. `den > 2^m U/V`, main's full bound, by
  multiplying the chain through by `U` and `V`; `uniform_two_block` (the
  weaker form) is now a corollary. Twenty-four declarations with the
  standard axioms; no diagnostics; receipts regenerated (sha256
  `a64b42e3…7fb3`, 872 lines).
- Main pushed `7270d95` (C003: uniform denominator bounds for changing
  repeated blocks). Read and checked (STATE "Insights"); no error found;
  the effective theorem (5)–(6) is purely algebraic given C002's (5),
  which is the plan for C003-a.

## Iteration 13 — 2026-10-19, ~01:50 -03

- Side lane verdict on C001-b (feed 00:32, `9a17566`): **verified** — (7)
  without coprimality, the hypothesis-form periodicity sound for any
  factorisation `K₀`, totient version from `D_u` coprime to 6, axioms
  13 × standard + 3 × `[propext]`, clean scan, hash match; it also checked
  the `v₂` injectivity route on all 19,525 words with `m ≤ 6`, letters
  1–5.
- **C002-a verified** in `CycleSpectrum.lean` (sha256 `5e547237…2581`,
  841 lines, twenty-three declarations with the standard axioms):
  `C_two`/`D_two` (1)–(2), `commutator_two_u`/`_v` (3)–(4),
  `gcd_dvd_K_mul_gcd` (5), `gcd_pow_sub_pow` (strong divisibility of
  `U^i − V^i` for coprime `U, V`), `C_nonneg`/`C_pos`/`C_odd`,
  `length_le_sum`, `C_injective`, `two_pow_mul_C_le` (U2),
  `pow_sub_pow_lower`, and **`uniform_two_block`**, main's uniform
  equal-total exclusion (U1): `den(u^k v^ℓ) > 2^m` for distinct positive
  words of equal length and total with `2^A > 3^m`, `k, ℓ ≥ 1`,
  `k + ℓ ≥ 3`. Three compile rounds: `nlinarith` needing explicit
  products for `1 ≤ k·Σu + ℓ·Σv`; implicit divisors in
  `Nat.Coprime.coprime_dvd_right`; a `← mul_assoc` that should have been
  forward; a `rw … at hA` that also rewrote the gcd's argument (replaced
  by `rw [← hsplit]` on the goal); `pow_sub_pow_lower` first stated with
  `0 ≤ V`, which is false at `V = 0` (corrected to `0 < V`); `2 ^ A ^ h`
  parsing as `2 ^ (A ^ h)` (parenthesised); `set` variables hiding
  `Nat.gcd` from `omega` (removed); a `rw [hDw]` that rewrote `D w`
  inside the gcd (replaced by a final `calc` step); a `rw … at *` with a
  missing pattern (replaced by `simp only [pow_succ, pow_add]`). Main
  unchanged at `e14a4e3`.

## Iteration 12 — 2026-10-19, ~01:15 -03

- Side lane verdict on C001-a (feed 00:22, `b9c3fd7`): **verified** —
  recursive `C` matches R71's sum (index shift checked), `G` matches the
  geometric sum, hypotheses only on `v`, the two example theorems give the
  mod-6 law, axioms 9 × standard + 3 × `[propext]`, clean scan, hash
  match. It also posted a lead for main's rung-1 law (size constraint, not
  `gcd(2^A − 3^m, d)`, separates `d = 1`).
- **C001-b verified** in `CycleSpectrum.lean` (sha256 `99418d99…3e32`,
  483 lines): `gcd_two_sided` (7), `gcd_periodic` (9) in hypothesis form,
  `gcd_periodic_totient` with `T = φ(K₀|D_u|)`, `gcd_coprime_six`; sixteen
  declarations with the standard axioms. Two compile rounds (a
  `push_cast` that produced `|D u|` where the statement had
  `↑(natAbs)`; `exact_mod_cast` instead).
- Main pushed `e14a4e3` (C002: proportional-slope theorem, uniform
  equal-total exclusion, unequal-slope application of Corvaja–Zannier,
  exponential-cancellation example, 3x+d replay). Read and checked; no
  error found; verdict and a formalisation remark sent (STATE "Insights").
  Monitor re-armed after expiry. Next: C002-a.

## Iteration 11 — 2026-10-19, ~00:45 -03

- Woken by the side lane's feed `f827811`; main then pushed `14441c0`:
  the user's new goal, cycle denominators across `3x+d`
  (`docs/CYCLE_SPECTRUM_BRIEF.md`), with batch C001 (repetition
  spectrum theorem, perturbed mechanical family, `3x+d` scan). Read
  REPORT, REPETITION_SPECTRUM, the brief, the AGENTS diff, the
  independent review and `repetition_spectrum.py`; checked §§1–3 by
  re-derivation; no error found (details in STATE.md "Insights").
- **C001-a verified.** `CycleSpectrum.lean` (sha256 `88de824f…9221`,
  295 lines, `import Mathlib` only): `LeanLane.Cyc.commutator` (3),
  `gcd_dvd_K` (4), `gcd_le_natAbs_K` (5), `gcd_eq_gcd_K` (6), `C_w` (1),
  `D_w` (2), `C_rep`, `G_mul`, `D_odd`, `D_not_three_dvd`, the worked
  examples and the `d = 485` counterexample by `norm_num`, and
  `seven_dvd_D_example` / `gcd_example` for the `(1,1,3)^k(2)` law; axioms
  `[propext, Classical.choice, Quot.sound]` (`C_w`, `D_w`, `C_rep` only
  `[propext]`). Two compile rounds: in this Mathlib `Int.gcd_dvd_left/right`
  take explicit arguments, `Int.dvd_gcd` concludes in `ℕ`, and
  `IsCoprime.dvd_of_dvd_mul_left/right` cancel the coprime factor on the
  left/right respectively; the second build has no diagnostics.
- Queue re-prioritised to the C-series: C001-b next (periodicity (9),
  two-sided (7), `K = 0`, then §3's family); V008-a kept at low priority.

## Iteration 10, review — side lane verifies V006-a; triangle count added

- `claude/sidekick` 0074c1b (feed 23:55): V006-a at 6fbc3f8 **verified** —
  unconditional form (explicit non-periodicity hypothesis, no Cobham,
  finiteness unused), `Reach` is exactly main's `J_D`, `s2_balanced` covers
  every multiple, twelve declarations with the standard axioms, clean scan,
  hash match. It noted the `(D+1)(D+2)/2` evaluation as the open follow-up.
- Follow-up done in the same file: `triangle`, `mem_triangle`,
  `card_triangle` (`(D+1)(D+2)/2`, by `Finset.card_biUnion` over the
  sigma finset `(range (D+1)).sigma (fun a => range (D+1−a))`,
  `Finset.sum_range_reflect` and `2·Σ_{s≤D}(s+1) = (D+1)(D+2)`),
  `triangle_encard` and `reach_encard_ge` (main's (4) with the number).
  Three compile rounds: `Finset.Nat.antidiagonal` does not exist here and
  `Finset.antidiagonal` resolves to an `IsPWO` version, hence the sigma
  finset; then unreduced `Sigma` projections under `omega` and a `dsimp`
  with nothing to do. Receipts regenerated (sha256 `5b92658b…b070`, 515
  lines; fifteen declarations with the standard axioms).

## Iteration 10 — 2026-10-18, ~23:55 -03

- Woken by the side lane's V007-a verdict and feed `d0354c2`/`52244f7`;
  main pushed `4be9bae` (V009: unbounded additive excess
  `κ_h(D) − (D+1) → ∞` for every nonconstant invariant, plus the global
  detection bound) during the iteration. Read in full and checked (no gap;
  Cobham dependence stated by main); verdict sent, recorded in feed
  `7bcc778`. Monitor re-armed twice after expiry.
- **V006-a verified.** `QuadraticSeparation.lean` (sha256 `0f82a36b…ecdd`,
  450 lines, `import Mathlib` only): `LeanLane.Quad.Q_injective` (main's
  pairwise-distinctness theorem for `Q_(a,t) = F(t₀ + t + s₂(3^a n))`, `F`
  not eventually periodic), `Q_mem_Reach` (operator count `a + t`),
  `triangle_encard_le` (the joint family through depth `D` is at least as
  large as `{a + t ≤ D}`), with the digit-count identities
  `s2_add_pow_mul`, `s2_compl`, `s2_mul_pow_sub` (5), `s2_mul_pow_sub_one`
  (6), `three_pow_dvd`, `s2_balanced_block`, `s2_balanced` (7); axioms
  `[propext, Classical.choice, Quot.sound]`. Two compile rounds: the first
  had an unknown lemma name (`nat_sub_dvd_pow_sub_pow`; replaced by a direct
  induction), a `mul_add` that rewrote the exponent instead of the product
  (pinned by explicit arguments), and three `omega` failures where the
  cast of a power atom lost its nonnegativity (supplied `Nat.one_le_two_pow`
  / `Nat.le_add_right`); the second has no diagnostics. The numeric value
  `(D+1)(D+2)/2` of the triangle's cardinality is left for a follow-up.
- The user asked not to be prompted for Lean runs; the session was already
  in auto mode (`set_session_permission_mode` confirmed), so no change.

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
