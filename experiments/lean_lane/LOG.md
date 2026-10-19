# Lean lane — LOG

Newest first. Each entry: iteration, target, outcome, axioms, receipts,
and any insight sent to the feed.

## Iteration 35 — 2026-10-19, 05:22 -03

- Woken by the monitor's expiry notice; re-armed. The sidekick had verified
  C013-a (`2136e50`, STATE "Insights"). Main unchanged at `1c5c19d`.
- **C005-c verified — the rotation-block ratio bound and its gcd
  bookkeeping, abstract core** in `CycleSpectrum.lean` (sha256
  `10004222…fb54`, 4776 lines, 304 theorems: 243 with the three standard
  axioms, 24 × `[propext, Quot.sound]`, 36 × `[propext]`, 1 none; no
  `sorry`): `affine_ratio`, `block_preserves`, `fixed_point_mem`,
  `blockComp`, `blockComp_mem`, `blockComp_affine`, **`cycle_point_mem`**,
  **`state_bound`**, **`ratio_bound`**, `flatten_rotations_length/sum`,
  **`gcd_flatten_rotations`**, `gcd_rep_of_flatten`,
  `blocks_eq_of_flatten_rep`, **`blocks_identical`**. Two compile rounds: an
  unused `0 ≤ σ` hypothesis (lint) — the fixed-point lemma needs only slope
  `< 1`. Receipts regenerated. Next: R71 `g = 1` (the base mechanical
  denominator), then whichever of main's newest claims most needs backing.

## Iteration 34 — 2026-10-19, 05:13 -03

- Woken by the sidekick's push `c86942c`: **C009-b verified** (STATE
  "Insights"). Main unchanged at `1c5c19d`.
- **C013-a verified — C013's shared-background block identities and the run
  law** in `CycleSpectrum.lean` (sha256 `c6222ea4…2fb5`, 4588 lines, 290
  theorems: 235 with the three standard axioms, 19 × `[propext,
  Quot.sound]`, 35 × `[propext]`, 1 none; no `sorry`): `interleave`, `Ph`,
  `interleave_cons/length/sum`, **`C_interleave`**, **`D_interleave`**,
  `Ph_eq_sum`, `E_bound`, **`run_factor`**, `OddCycle.diff_step`,
  `OddCycle.run_diff`. Two compile rounds: a length lemma needed
  `List.length_nil` in its simp set. Receipts regenerated. Next: C005-c
  (the rotation-block ratio bound and its gcd bookkeeping), R71 `g = 1`, then
  whichever of main's newest claims most needs formal backing.

## Iteration 33 — 2026-10-19, 05:04 -03

- Woken by main's push `1c5c19d` (C013) and the sidekick's `e2268cc` (C011-a
  verified), `9a0e8dc` (C012 record) and `06e0c7d` (C013 record). C013 read
  and checked by hand, no error; insights sent (STATE "Insights").
- **C009-b verified — C009's one-point deletion theorem** in
  `CycleSpectrum.lean` (sha256 `1f618576…aca6`, 4456 lines, 280 theorems: 230
  with the three standard axioms, 19 × `[propext, Quot.sound]`, 30 ×
  `[propext]`, 1 none; no `sorry`): `retMap`, `compMap`, `IsRankShift`,
  `retMap_of_lt/of_ge/of_eq`, **`one_point_deletion`** (`IsRankShift m s ↔
  s = 1 ∨ s = m − 1` for `m ≥ 2`, `1 ≤ s < m`; axioms `[propext,
  Quot.sound]`), and the `q = 13` control by `decide`. Two compile rounds:
  an unused hypothesis `0 < s` in `retMap_of_eq` (lint). Receipts
  regenerated. Next: C013-a (block identities and run law), then C005-c,
  R71 `g = 1`.

## Iteration 32 — 2026-10-19, 04:41 -03

- Woken by the sidekick's pushes `3529355` (C010-a verified, the `3 ∤ q`
  remark checked numerically) and `380bfdf` (merge). Main pushed C012
  (`de7db67`); read and checked by hand (block identities, determinant,
  minors, Smith form, the `w_{r,t}` family and its small example, the
  three-defect family, the counting bound), no error; insights sent (STATE
  "Insights").
- **C011-a verified — C011's two-arc identity, `g ∣ (2^k−1) gcd(C_u, C_v)`,
  the intercept bound and the integer forms of (5)/(7)** in
  `CycleSpectrum.lean` (sha256 `46b48a59…f9eb`, 4360 lines, 276 theorems: 230
  with the three standard axioms, 15 × `[propext, Quot.sound]`, 30 ×
  `[propext]`, 1 none; no `sorry`): `C_append_singleton`,
  **`two_arc_identity`**, `rotate_cut`, `isCoprime_three_D`,
  `dvd_C_rotate_of_dvd`, `gcd_isCoprime_two/three`, **`two_arc_dvd`**,
  **`intercept_bound_last`**, `two_defect_arith`,
  **`two_defect_bound_sharp`**, **`two_defect_bound`**, `two_defect_q_bound`.
  Two compile rounds: `Int.dvd_gcd` here concludes in `ℕ` (`k ∣ Int.gcd i j`
  from `↑k ∣ i`, `↑k ∣ j`), so the cast had to be reinserted with
  `Int.natCast_dvd_natCast`. Receipts regenerated. The Lean file and
  receipts went out in `0992e4f`; the STATE/LOG records follow in the next
  commit (an edit script aborted on a stale anchor). Next: C009-b (one-point
  deletion), C005-c, R71 `g = 1`.

## Iteration 31 — 2026-10-19, 04:26 -03

- Woken by the sidekick's push `3cc0bf1` (its record of the lane's C011
  check). Main unchanged at `b896512`.
- **C010-a verified — C010's sharp odd-spacing bounds and `L ≥ R_q(H)`** in
  `CycleSpectrum.lean` (sha256 `8569c7d1…0d52`, 4078 lines, 263 theorems: 219
  with the three standard axioms, 14 × `[propext, Quot.sound]`, 29 ×
  `[propext]`, 1 none; no `sorry`): `eta`, `eta_refine`, `OddCycle.q_odd`,
  `OrdCycle.y_eq`, `y_succ_lt`, `gap_eq`, **`gap_ge_of_eq`**,
  **`gap_ge_of_lt`**, **`gap_seam_ge`**, **`three_gap_gt_of_gt`**,
  **`three_gap_ge_of_gt`**, `pairBound3`, `pairBound3_le`,
  **`rounding_bound`**. Two compile rounds: the first build was clean except
  for an unused-variable warning that exposed the hypothesis `3 ∤ q` as
  unnecessary; it was removed throughout. Receipts regenerated. Next: C011-a
  (the two-arc identity and the integer cancellation bounds), then C009-b.

## Iteration 30 — 2026-10-19, 04:07 -03

- Woken by the sidekick's push `f01ac0e`: **C006-a part 3e verified** (STATE
  "Insights"). Main unchanged at `cae57b0`.
- **C009-a verified — C009's cut lemma and elimination** in
  `CycleSpectrum.lean` (sha256 `18cbad0b…cf25`, 3849 lines, 251 theorems: 207
  with the three standard axioms, 14 × `[propext, Quot.sound]`, 29 ×
  `[propext]`, 1 none; no `sorry`): `C_take_drop`, `sum_take_drop`,
  `cut_dvd`, `cutState` with `cutState_spec/zero/last/arrow/pos/odd`,
  **`cut_lemma`**, **`elimination`**, `D_dvd_C_of_cycle`, `isCoprime_two_D`,
  `dvd_C_rotate`, `odd_quot_rotate`, `integer_cycle_of_dvd`,
  **`cylinders_of_dvd`**. Two compile rounds: `Nat.succ_le_of_lt` produced a
  `j.succ` exponent that `ring` does not unfold — pass `hj` as
  `j + 1 ≤ w.length` by `show` instead. Receipts regenerated. Next: C010-a
  (sharp odd-spacing bounds and `L ≥ R_q(H)`), then C009-b.
- Addendum 04:15: main pushed C011 (`b896512`, two-rotation-defect
  exclusion) during the build; read and checked by hand (identities (1)–(4),
  the amplitude-free bound (7), the finiteness argument, the §4
  classification, the marker family, the q = 359/5/7/13/97 controls and
  EXCLUSION's constants); no error; one precision remark on the Matveev step
  sent with the formalisable pieces (STATE "Insights"). The sidekick
  verified C009-a (`5a3c1f6`, 04:09). Monitor re-armed at 04:14 after its
  expiry. C011-a queued after C010-a.

## Iteration 29 — 2026-10-19, 03:54 -03

- Woken by the sidekick's pushes `6f11ab9`/`bab760a`: **C006-a part 3d
  verified** and the C010 check recorded (STATE "Insights"). Main unchanged
  at `cae57b0`.
- **C006-a part 3e verified — (G1)'s second inequality, true-intercept
  form** in `CycleSpectrum.lean` (sha256 `7e121d16…0a4e`, 3648 lines, 234
  theorems: 192 with the three standard axioms, 14 × `[propext,
  Quot.sound]`, 27 × `[propext]`, 1 none; no `sorry`; compiled first try):
  `OddCycle.Cpre_succ`, `Cpre_pos`, `D_pos`, **`OrdCycle.G1_second`**
  (`D · 2^{⌊(m−1)/J⌋} < 2^B q C_m`). This closes C006-a's elementary scope
  (the `C_c` form, `e_run` and (G4) are out of scope). Receipts regenerated.
  Next: C009-a (cut lemma + elimination), then C010-a.

## Iteration 28 — 2026-10-19, 03:46 -03

- Woken by the sidekick's push `c138d94`: **C006-a parts 3 and 3c verified**
  (STATE "Insights"). Main pushed `cae57b0` (C010: unimodular gap lattice,
  sharp odd-spacing bounds, the rounding relaxation retired); read and
  checked by hand (the operator identities, the determinant, the seam
  identity (6), the `η` table and the q = 5/13/83 controls recomputed), no
  error found; insights sent (STATE "Insights"). Monitor re-armed at 03:43
  after its expiry.
- **C006-a part 3d verified — (H1) `J ≥ B + 1`** in `CycleSpectrum.lean`
  (sha256 `bc6e4e25…8107`, 3601 lines, 230 theorems: 188 with the three
  standard axioms, 14 × `[propext, Quot.sound]`, 27 × `[propext]`, 1 none; no
  `sorry`): `card_image_le_changes`, `OrdCycle.hr_rank`, `exists_rank_height`,
  `J_eq_changes`, **`J_ge_height`** (`h j + 1 ≤ J` for every `j`). Two compile
  rounds: Mathlib renames `Finset.range_succ` → `Finset.range_add_one` and
  `Finset.card_insert_of_not_mem` → `Finset.card_insert_of_notMem`. Receipts
  regenerated. Next: part 3e (tiny), then C009-a; C010-a queued.

## Iteration 27 — 2026-10-19, 03:35 -03

- Woken by the sidekick's push `4856ed7`: **C006-a part 3 verified** (STATE
  "Insights"). Main unchanged at `ec48fbd`.
- **C006-a part 3c verified — (G1)'s first inequality** in
  `CycleSpectrum.lean` (sha256 `31a44291…b8b9`, 3520 lines, 225 theorems: 183
  with the three standard axioms, 14 × `[propext, Quot.sound]`, 27 ×
  `[propext]`, 1 none; no `sorry`): `exists_run` (the cyclic pigeonhole by
  iteration), `OrdCycle.orb_zero_eq_rank`, `orb_orb`, `orb_mod`, `forcedAt`,
  `J`, `J_eq`, `J_pos`, `exists_zero_run`, **`G1_first`** (`2^{⌊(m−1)/J⌋} <
  2^B L`). Two compile rounds: `forcedAt` and its decidability instance needed
  `noncomputable`. Receipts regenerated. Next: part 3d (`J ≥ B + 1`, the
  exponent sum, the consequences), then C009-a.

## Iteration 26 — 2026-10-19, 03:28 -03

- Woken by the sidekick's push `29782db`: **C006-a part 2b verified** (STATE
  "Insights"). Main unchanged at `ec48fbd`.
- **C006-a part 3 verified** in `CycleSpectrum.lean` (sha256 `5a448bc7…8ae2`,
  3351 lines, 217 theorems: 175 with the three standard axioms, 14 ×
  `[propext, Quot.sound]`, 27 × `[propext]`, 1 none; no `sorry`): the bundle
  `OrdCycle` with `N`, `N_prim`, `N_rank_zero`, `q'_pos`, `hr`, `off`,
  `offext`, `T`, `Fr_eq`, `Fext_sub`, `gap_rec`, `T_eq_zero_iff`, `hr_zero`,
  `T_seam_pos`, `orb`, `orb_zero`, `orb_succ`, **`run_bound`**, `run_bound_L`.
  Two compile rounds: one missing `noncomputable`. Receipts regenerated. Next:
  part 3c (the cyclic pigeonhole and `J ≥ B + 1`), then C009-a.

## Iteration 25 — 2026-10-19, 03:22 -03

- Main pushed `ec48fbd` (C009: excursion compression rejected, cut lemma,
  one-point deletion theorem) and the sidekick verified C008-a (`960b3b9`,
  feed 03:09); C009 read and checked, no error found; insights sent (STATE
  "Insights"). Monitor re-armed at 03:09 after its expiry.
- **C006-a part 2b verified** in `CycleSpectrum.lean` (sha256 `a5af2f82…5f06`,
  3179 lines, 198 theorems: 156 with the three standard axioms, 14 ×
  `[propext, Quot.sound]`, 27 × `[propext]`, 1 none; no `sorry`): `Fr`,
  `Fext`, `e`, `Fext_of_lt`, `Fext_m`, `e_eq`, `arrow_rank`,
  **`gap_recurrence`** (the four-case (G3) with the seam). Two compile rounds:
  the rank reduction `hm1` had to be rewritten in the arrow hypotheses as well
  as the goal; an unused `rank 0 = 0` hypothesis dropped. Receipts
  regenerated. Next: part 3 (`T_r` from the heights, the per-run bound, the
  pigeonhole, `J ≥ B + 1`), then C009-a.

## Iteration 24 — 2026-10-19, 03:08 -03

- Woken by the sidekick's push `ee7422d`: **C006-a part 2a verified** (STATE
  "Insights"). Main unchanged at `93117c0`.
- **C008-a verified** in `CycleSpectrum.lean` (sha256 `ec96d12e…38a6`, 3051
  lines, 193 theorems: 151 with the three standard axioms, 14 × `[propext,
  Quot.sound]`, 27 × `[propext]`, 1 none; no `sorry`): `exists_common_root`,
  `zmod_common_root`, `NarrowCycle.sum_a_range`,
  `OddCycle.Apre`/`Cpre`/`Apre_succ`, `prefix_identity`, `cycle_identity`,
  `q_dvd_D`, `toNarrow_primitive`, `toNarrow_rank_zero`, `sorted_residue_law`.
  Two compile rounds: `zpow_mul` rewrote the wrong power (pinned to its base),
  the recursive call in `Cpre` cannot use field notation, and a `haveI` lint.
  Receipts regenerated. Next: C006-a parts 2b–3.

## Iteration 23 — 2026-10-19, 03:00 -03

- Woken by the sidekick's push `7157c8c`: **C006-a part 1 verified** (STATE
  "Insights"). Main then pushed `93117c0` (C008: sorted-rank residue law,
  cyclicity of `⟨2,3⟩` mod `q`, primewise-matching counterexamples at `q =
  5077565`), refereed by the sidekick (`27e977f`); read and checked, no error
  found.
- **C006-a part 2a verified** in `CycleSpectrum.lean` (sha256 `99345455…f48d`,
  2901 lines, 183 theorems: 141 with the three standard axioms, 14 ×
  `[propext, Quot.sound]`, 27 × `[propext]`, 1 none; no `sorry`):
  `rank_congr`, `exists_rank_eq`, `idx`, `idx_spec`, `y`, `y_lt_y`,
  `idx_zero`, `y_zero`, `yext`, `gap`, `yext_of_lt`, `yext_m`, `gap_pos`,
  `sum_gap`, `gap_lt`, `x_idx_succ`, `high_idx_iff`. One compile round plus a
  lint fix (`dif_pos` → `dite_eq_left`). Receipts regenerated. Next: C008-a
  (prefix/cycle identities and the integer sorted-rank law), then C006-a parts
  2b–3.

## Iteration 22 — 2026-10-19, 02:52 -03

- Woken by the sidekick's push `1ebd3ac`: **C007-a verified** (STATE
  "Insights"). Main unchanged at `dddbe33`.
- **C006-a part 1 verified** in `CycleSpectrum.lean` (sha256 `341ee1d8…e729`,
  2773 lines, 170 theorems: 128 with the three standard axioms, 14 ×
  `[propext, Quot.sound]`, 27 × `[propext]`, 1 none; no `sorry`):
  `run_pow_mul`, `run_dvd`, `run_lower` (the binary-divisibility core of
  (G1)), `exists_eq_of_step_le`, and on `OddCycle` `c_le_two`, `h_succ_le`,
  `exists_height_eq` ((H1)'s chronological half). One compile round, no
  diagnostics. Receipts regenerated. Parts 2–3 (rank-indexed gaps with the
  seam, the per-run bound, the cyclic pigeonhole, `J ≥ B + 1`) are queued.

## Iteration 21 — 2026-10-19, 02:45 -03

- Woken by the sidekick's push `aab73dd` and verdict message: **C005-b
  verified** (STATE "Insights"). Main unchanged at `dddbe33`.
- **C007-a verified** in `CycleSpectrum.lean` (sha256 `3c342e5a…73f1`, 2678
  lines, 163 theorems: 122 with the three standard axioms, 13 × `[propext,
  Quot.sound]`, 27 × `[propext]`, 1 none; no `sorry`): in `OddCycle`, `P`,
  **`residue_law`** (`2^{P_i} Z_i ≡ 3^i Z_0 [ZMOD q]`), `three_not_dvd`,
  `dvd_succ_of_dvd`, `dvd_all_of_dvd`, **`min_top`**. One compile round plus a
  lint fix (`simpa` → `simp`). Receipts regenerated. Next: C006-a (the
  elementary part of the sparse-forcing law).

## Iteration 20 — 2026-10-19, 02:40 -03

- Woken by the sidekick's verdict message (C005-a verified, `f3cc907`). Main
  pushed `dddbe33` (C007: height-denominator candidate `B ≤ q − 1`, modular
  lemma, min–top inequality, census with a new `q = 29` cycle) and the
  sidekick refereed it (`bbd3417`); read and checked (STATE "Insights"), no
  error found. Monitor re-armed after its expiry.
- **C005-b verified** in `CycleSpectrum.lean` (sha256 `00f4ba6c…74cf`, 2594
  lines, 158 theorems: 118 with the three standard axioms, 12 × `[propext,
  Quot.sound]`, 27 × `[propext]`, 1 none; no `sorry`): `exists_height`,
  `height_le_two`, `pow_mul_eq_of_odd`, `eq_of_pow_mul_eq_in_window`; the
  structure `OddCycle m` with `Z`, `F`, `c`, `lo`,
  `h_unique`/`h_zero`/`h_per`/`h_mod`, `Z_per`/`Z_mod`,
  `Z_lower`/`Z_upper`/`Z_zero`, `h_le_a_add`, `c_arrow`, `Z_inj`,
  `F_sub_of_le`/`Z_sub_of_le`, `Z_eq_of_F_eq`, `F_lt_of_Z_lt`,
  `order_of_three_band`, `F_zero`, `F_lt_two_F_zero`, `F_zero_le`, `toNarrow`,
  `sum_c`, **`three_band`**, `q_ne_one_of_not_coprime`. Two compile rounds:
  `le_or_lt` no longer exists (replaced by `Nat.lt_or_ge` with the branches
  swapped) and `push_neg` is deprecated (replaced by `rw [not_le]`/`rw
  [not_lt]`). Receipts regenerated. Next: C007-a (small), then C006-a.

## Iteration 19 — 2026-10-19, 02:21 -03

- Main pushed `1cb02fa` (C005: dyadic order, three-band restriction at `q =
  1`, rotation-block exclusion; C006: sparse-forcing gap law with the Bugeaud
  import). Both read and checked by hand (STATE "Insights"); no error found;
  insights sent to the sidekick, which recorded them (feed 02:19) after
  refereeing both batches (`15da388`). The sidekick also verified C004-b
  complete (`8db3feb`, feed 02:11). Monitor re-armed at 02:04 after its
  expiry.
- **C005-a verified** in `CycleSpectrum.lean` (sha256 `cd57b972…2a73`, 2152
  lines, 128 theorems: 93 with the three standard axioms, 10 × `[propext,
  Quot.sound]`, 24 × `[propext]`, 1 none; no `sorry`): the `NarrowCycle`
  structure generalised from a constant offset `d` to images `F i` with
  `order`, `window`, `hq1`, `hq2` (C005's order-lemma hypotheses),
  `exponent_dichotomy_F`, `F_eq_of_x_eq`, `succ_lt_iff_of_a_eq`, `F_mod`;
  `ofWord` rebuilt on the general structure (`F i = 3 C(w.rotate i) + D_w`);
  all C004-b theorems unchanged and re-verified; `inversion_formula` (C005's
  (2) in `ℚ`) and `no_inversion_of_le_two`. One compile round, no diagnostics.
  Receipts regenerated. Next: C005-b (the `q = 1`, `H < 8L` theorem on actual
  integer cycles).

## Iteration 18 — 2026-10-19, 02:09 -03

- Woken by the sidekick's verdict message and push `1143485`: **C004-b part 2
  verified** (STATE "Insights"). Main unchanged at `61cf54a`. Monitor re-armed
  after its expiry.
- **C004-b part 3 verified — the forward direction is complete** in
  `CycleSpectrum.lean` (sha256 `19b74f4d…2ba6`, 2068 lines, 122 theorems: 90
  with the three standard axioms, 10 × `[propext, Quot.sound]`, 21 ×
  `[propext]`, 1 none; no `sorry`, no `native_decide`): `rotate_ne_nil`,
  `headD_rotate`, the instance `ofWord`, **`eq_mech_of_narrow`**,
  **`is_mech_of_narrow`**. One compile round, no diagnostics. With
  `narrow_mech` (iteration 15) C004 §3's narrow-cycle equivalence is formal in
  both directions. Receipts regenerated. Next: decide between R71's `g = 1`
  (which would make the integer corollary `H > 2L` formal) and the queued
  C002-b/C001-c, after reading any new main commits.

## Iteration 17 — 2026-10-19, 02:01 -03

- Woken by the sidekick's push `9ac12a8` and its verdict message: **C004-b
  part 1 verified** (STATE "Insights"). Main unchanged at `61cf54a`.
- **C004-b part 2 verified** in `CycleSpectrum.lean` (sha256 `eab32a83…7e3c`,
  1930 lines, 118 theorems: 87 with the three standard axioms, 9 × `[propext,
  Quot.sound]`, 21 × `[propext]`, 1 none): `rank_mod`/`high_mod`, `rank_lt`,
  `rank_lt_of_lt`, `x_eq_of_rank_eq`, `Primitive`, `rank_inj`,
  `all_low_of_numHigh_zero`/ `all_high_of_numHigh_eq`,
  `numHigh_pos`/`numHigh_lt`, `rank_succ_eq`, **`rank_formula`**,
  **`a_formula`**, **`coprime_numHigh`**, `sum_a`. Two compile rounds: one `q
  = q + 0` goal left open by `rw` (closed with `Nat.add_zero`) and one
  unreachable tactic (`omega` alone handles the ℤ-order branches). Receipts
  regenerated. Part 3 (the list instance and the general rotation statement)
  is next.

## Iteration 16 — 2026-10-19, 01:54 -03

- Woken by the sidekick's verdict message and push `f054db4` (feed 01:39):
  **C004-a verified** (details in STATE "Insights"). Main unchanged at
  `61cf54a`; the monitor re-armed during iteration 15 is still running.
- **C004-b part 1 verified** in `CycleSpectrum.lean` (sha256 `bc20673f…02da`,
  1765 lines, 103 theorems: 73 with the three standard axioms, 29 needing only
  subsets, `diffWord_zero` none): `C_cons_rotate`/`D_rotate`/`C_rotate_succ`
  (C004's (1) on rotations), `exists_exponent`, `exponent_dichotomy`,
  `succ_order_same`, `succ_order_high_low`; the structure `NarrowCycle m` with
  `lo_pos`, `high`, `a_eq`, `a_of_low`/`a_of_high`, `x_lt_of_low_high`,
  `succ_lt_iff_low`/`_high`, `succ_lt_of_high_low`, `sum_range_shift`,
  `x_add_mul`/`x_mod`/`x_m`, `rank`, `numHigh`,
  `numHigh_add_low`/`numHigh_le`/`sum_low`, `rank_succ`,
  **`rank_succ_of_low`**, **`rank_of_high`**, `rank_ge_of_high`,
  `rank_lt_of_low`, `high_iff_rank`. Design: the rank shift is proved by
  shifting the index sum once around the cycle
  (`Finset.sum_range_succ`/`succ'`) and comparing termwise, with no sorting
  and no reindexing bijection. Two compile rounds: clean on the first; the
  second only renamed the deprecated `if_pos`/`if_neg` to
  `ite_eq_left`/`ite_eq_right` and dropped three unused simp arguments.
  Receipts regenerated. Part 2 (rank formula, `gcd(h, m) = 1`, the word
  identification, the list instance) is recorded in STATE.

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
