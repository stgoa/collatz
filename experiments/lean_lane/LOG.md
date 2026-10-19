# Lean lane — LOG

Newest first. Each entry: iteration, target, outcome, axioms, receipts,
and any insight sent to the feed.

## Iteration 93 — 2026-10-19, 17:55 -03

- Woken by the monitor (sidekick `5764d7f`: the S13 review ACK; `55cf217`,
  `1d87059`, `2def4d0` with Corollaries 5–7 arrived during the build); main
  frozen at `1c5c19d`. Monitor `b80knxlwe` active. The PR body refresh is
  retried.
- **S13-a verified — the rise lemma in natural logs with a uniform `Δ`: `eta`,
  `kappa`, `Phi`; `rise_bound` (P), `rise_le_mul` (the uniform `Δ`);
  `witness_two_pow`, `witness_log` (W); `run_step`; `rise_lemma` (`Φ_v ≤
  κ^(k+1) Φ_u`); `rise_from_min` and `rise_from_min_uniform` (Corollary 1 from
  the minimum)** in `CycleSpectrum.lean` (sha256 `33085b09…3296`, 13,896
  lines, 772 theorems: 639 with the three standard axioms, 58 × `[propext,
  Quot.sound]`, 62 × `[propext]`, 13 none; no `sorry`). Second build (two
  Mathlib name fixes). Receipts regenerated. Corollaries 5–7 reviewed (all
  correct; one count rounding-sensitive). Next: S13-c (subadditivity, mean-
  zero `max ≤ Var/2`, the forced letter) or S13-b (orientation lemma, explicit
  log form).

## Iteration 92 — 2026-10-19, 17:33 -03

- Woken by the monitor (sidekick `ee62601`: the C002-b part 1 verdict,
  verified); main frozen at `1c5c19d`. Monitor re-armed on expiry
  (`b80knxlwe`). The PR body refresh is retried.
- **C002-b (part 2) verified — the `K = 0` case in integer form:
  `three_C_add_D` (`3 C_(a::z) + D_(a::z) = 2^a C_(z ++ [a])`),
  `two_pow_mul_odd_inj`, `K0_step` (equal rational points ⇒ equal first
  letters and `K = 0` for the rotated pair), `K0_letters` (the infinite
  valuation words coincide), `period_gcd`, `K0_common_period` (common period
  `gcd(|u|, |v|)`), and the controls `den_122`, `den_13`, `den_4` (`5, 7,
  13`)** in `CycleSpectrum.lean` (sha256 `f0e4c3f7…69a0`, 13,550 lines, 756
  theorems: 623 with the three standard axioms, 58 × `[propext, Quot.sound]`,
  62 × `[propext]`, 13 none; no `sorry`). Second build (`D_rotate` already
  existed; two unused simp arguments). Receipts regenerated. Remaining in
  C002-b: the list packaging `u = z^(|u|/g)`, `v = z^(|v|/g)`, `den(u^k v^ℓ) =
  den z`; §3's sharpness family; §4's family.
- Late in the iteration: the side lane's part 2 verdict (`41d3947`, verified)
  and its NEW producer batch S13 (the rise lemma, `3509a49`) arrived; the S13
  adversarial review was sent (correct; primitivity load-bearing; uniform-`Δ`
  natural-log form proposed for Lean; four numbers spot-checked). Next unit:
  S13-a.

## Iteration 91 — 2026-10-19, 17:13 -03

- Woken by the monitor (sidekick `2efc9e5`: the S12 milestone post); main
  frozen at `1c5c19d`. Monitor re-armed on expiry (`bd2yo82es`). The PR body
  refresh is retried.
- No producer statement pending; item 4's converse re-scoped (a framework
  theorem, no bounded piece). **C002-b (part 1) verified — main's
  proportional-slope denominator theorem (6)–(8): `E_dvd_commutator`,
  `proportional_gcd_dvd` (`gcd(C_w, D_w) ∣ J₀ H_h`), `proportional_den_lower`
  (`den(w) J₀ > U^(L−h) ≥ U^max(rk, sℓ)`, `(den(w) J₀)² > U^L`),
  `proportional_rectangle` (`den(w) ≤ d₀ ⇒ U^max(rk, sℓ) < d₀ J₀`), with the
  helpers `pow_sub_pow_dvd_of_dvd` and `pow_sub_pow_mul_pow_lt`** in
  `CycleSpectrum.lean` (sha256 `0248b759…b697`, 13,385 lines, 742 theorems:
  614 with the three standard axioms, 55 × `[propext, Quot.sound]`, 60 ×
  `[propext]`, 13 none; no `sorry`). First build. Receipts regenerated.
  Remaining in C002-b: the `K = 0` characterisation and §4's family.

## Iteration 90 — 2026-10-19, 16:53 -03

- Woken by the monitor (sidekick `20a3ecf`: the part 2 verdict in the feed,
  verified); main frozen at `1c5c19d`. The PR body refresh is retried.
- **S12-f (part 3) verified — the height tool with only `gcd(h, m) = 1`:
  `DK.cfK` (the sum of the partial quotients of `h/m`), `one_le_cfK`,
  `height_le_varMu_coprime` (`|log n_y − log n_x| ≤ (K − 1)·Var(μ_h)` for
  every `0 < h < m` coprime to `m`), `height_le_varMu_coprime'` (relative to
  `n 0`), `height_le_coprime` (`B ≤ (K − 1)(V_h log 2 + 2δ)`),
  `dk_denominator_law_coprime` and `word_dk_denominator_law_coprime` (no
  ladder, no minimal rotation)** in `CycleSpectrum.lean` (sha256
  `a3cf4400…83d1`, 13,072 lines, 736 theorems: 608 with the three standard
  axioms, 55 × `[propext, Quot.sound]`, 60 × `[propext]`, 13 none; no
  `sorry`). Second build (a `Γ`-free lemma under `variable (Γ)` is not a
  field; moved to `DK`). Receipts regenerated. S12 now has no non-formal
  input. Next: the side lane's newest material, else the paused `(1, 1, 2)`
  window theorem.

## Iteration 89 — 2026-10-19, 16:41 -03

- Woken by the monitor (sidekick `aec3c89`: the part 1 verdict in the feed);
  main frozen at `1c5c19d`. The PR body refresh is retried.
- **S12-f (part 2) verified — the Euclidean algorithm for `h/m`: remainders,
  quotients, the termination index, the gcd invariant, `rem n = 1`, `q n = m`,
  and `ladder_of_coprime` (for `0 < h < m` coprime to `m`, a DK-admissible
  `Ladder` ending at `m`)** in `CycleSpectrum.lean` (sha256 `dc3319fc…a2a9`,
  12,984 lines, 730 theorems: 602 with the three standard axioms, 55 ×
  `[propext, Quot.sound]`, 60 × `[propext]`, 13 none; no `sorry`). Second
  build (`k.succ` versus `k + 1`). Receipts regenerated. Next: part 3, the
  height tool with only `gcd(h, m) = 1`.

## Iteration 88 — 2026-10-19, 16:34 -03

- Woken by the side lane's approval of the Euclidean route; main frozen at
  `1c5c19d`. The PR body refresh is retried.
- **S12-f (part 1) verified — convergents from Euclidean data: `EuclidData`,
  `convQ`/`convP`, `ladder_convQ`, `conv_det` (determinant `(−1)^i`),
  `conv_coprime`, `conv_approx` and `conv_approx_either` (`q_i r_1 − p_i r_0 =
  (−1)^i r_(i+1)`), `conv_identity` (`r_0 = q_(i+1) r_(i+1) + q_i r_(i+2)`),
  `conv_adm` (`q_i r_(i+1) < r_0`)** in `CycleSpectrum.lean` (sha256
  `efc57f90…b2c5`, 12,827 lines, 713 theorems: 593 with the three standard
  axioms, 53 × `[propext, Quot.sound]`, 58 × `[propext]`, 9 none; no `sorry`).
  First build. Receipts regenerated. Next: part 2, the Euclidean algorithm for
  `h/m` (remainders `r i`, quotients, termination at `r_n = 1`, `r_(n+1) = 0`,
  `q_n = m`).

## Iteration 87 — 2026-10-19, 16:26 -03

- Woken by the monitor (sidekick `3edc878`, the S9-e verdict). Scoping
  iteration, no Lean change: probed Mathlib's `GenContFract` API for the
  ladder supply (`probe3.lean` in the scratchpad; 15 of 34 candidate names
  exist). Verdict: the Mathlib route is heavy; the elementary Euclidean
  construction of the convergents in `ℕ` is bounded. Monitor re-armed on
  expiry. The PR body refresh is retried. File unchanged (sha256
  `0964cf4f…6002`, 698 theorems).

## Iteration 86 — 2026-10-19, 16:22 -03

- Woken by the side lane's S12-e verdict and its choice of (a); main frozen at
  `1c5c19d`. The PR body refresh is retried.
- **S9-e verified — the word laws without the minimal-rotation normalisation:
  `word_two_mismatch_law'`, `word_three_mismatch_law'`,
  `word_dk_denominator_law'`, via `den_rotate`, `hdist_rotate`,
  `mismatch_card_rotate`, `Vh_sum_rotate` (periodic shifts of indicator sums),
  `rotate_sum`, `rotate_add_length`, `gcdCD_rotate`, `sum_range_shift_nat`**
  in `CycleSpectrum.lean` (sha256 `0964cf4f…6002`, 12,661 lines, 698 theorems:
  589 with the three standard axioms, 49 × `[propext, Quot.sound]`, 58 ×
  `[propext]`, 2 none; no `sorry`). Second build (a duplicate of the existing
  `exists_min_rotation`, reused instead). Receipts regenerated. Next: scope
  (b), Mathlib's continued fractions for the ladder supply; take it only if
  bounded.

## Iteration 85 — 2026-10-19, 16:14 -03

- Woken by the side lane's S9-d verdict and its go for S12-e; main frozen at
  `1c5c19d`. The PR body refresh is retried.
- **S12-e verified — S12's denominator law for every mismatch count:
  `dk_denominator_law` (`log 2 + ((m − 1)/s) log 3 < log q + λ + (K − 1)(V_h
  log 2 + 2δ)` for a primitive cycle, a coprime rotation with `s ≥ 1`
  mismatches and a ladder of `h/m`), `word_dk_denominator_law` (the same with
  `den(w)`), with `mis_empty_of_mod_zero` and `ofWord_Vh`** in
  `CycleSpectrum.lean` (sha256 `00462994…0629`, 12,439 lines, 687 theorems:
  581 with the three standard axioms, 47 × `[propext, Quot.sound]`, 57 ×
  `[propext]`, 2 none; no `sorry`). First build. Receipts regenerated. The S12
  note is now formal except the continued-fraction supply of the ladder. Next:
  the side lane's direction (candidates: rotation invariance of `den` and of
  mismatch counts, removing the `hmin` normalisation caveat; the ladder supply
  if Mathlib's continued fractions make it bounded).

## Iteration 84 — 2026-10-19, 16:09 -03

- Woken by the side lane's S12-d verdict; the word side scoped (the `ofWord`
  reduced cycle already carries `q = den(w)`), so S9-d is the glue only; main
  frozen at `1c5c19d`. The PR body refresh is retried.
- **S9-d verified — the denominator laws for words: `word_two_mismatch_law`
  and `word_three_mismatch_law` for a positive word with `D_w > 0`, minimal
  first rotation and distinct rotated intercepts, with `den(w)` in place of
  `q`; glue lemmas `ofWord_den`, `ofWord_Apre`, `ofWord_D`, `gcdCD_mul_den`,
  `den_odd`, `sum_pos_of_pos`, `ofWord_mis`** in `CycleSpectrum.lean` (sha256
  `c704ec93…85fb`, 12,310 lines, 683 theorems: 577 with the three standard
  axioms, 47 × `[propext, Quot.sound]`, 57 × `[propext]`, 2 none; no `sorry`).
  Second build (section variables not included when used only in proofs; a
  missing `(m − 1) log(3/2)` term). Receipts regenerated. Next: the S12
  denominator corollary for every mismatch count (S12-e).

## Iteration 83 — 2026-10-19, 16:01 -03

- Woken by the side lane's S12-c verdict; main frozen at `1c5c19d`. Monitor
  re-armed on expiry. The PR body refresh is retried.
- **S12-d verified — S12 (3): `log_step` (`log n_(t+1) − log n_t = log 3 − a_t
  log 2 + ε_t`), `sum_eps` (`Σ ε_t = A log 2 − m log 3`), `varMu_le` and
  `varMu_le_Vh` (`Var(μ_h) ≤ V_h log 2 + 2δ`), with `eps`, `eps_nonneg'`,
  `eps_per`, `sum_eps_shift`, `Vh`, `Vh_cast`, `n_cast_pos`** in
  `CycleSpectrum.lean` (sha256 `52619fc9…900b`, 12,206 lines, 674 theorems:
  570 with the three standard axioms, 45 × `[propext, Quot.sound]`, 57 ×
  `[propext]`, 2 none; no `sorry`). Second build (`abs_add_le`;
  `Nat.cast_natAbs` + `Int.cast_abs`). Receipts regenerated. S12's height tool
  is now formal end to end given the ladder of convergents. Next: S9-d, the `q
  = den(w)` glue.

## Iteration 82 — 2026-10-19, 15:53 -03

- Woken by the side lane's S12-b verdict; main frozen at `1c5c19d`. The PR
  body refresh is retried.
- **S12-c verified — S12 (2) assembled: `DK.exists_chain_index` (coprime
  rotations reach every residue within `m` chain steps), `height_le_varMu`
  (ladder with `q n = m`, admissible denominators, `gcd(h, m) = 1`: `|log n_y
  − log n_x| ≤ (K − 1)·Var(μ_h)` for all `x, y`), `height_le_varMu'` (the side
  lane's `B ≤ Var·(K − 1)` relative to the minimum)** in `CycleSpectrum.lean`
  (sha256 `789a2f7c…5b55`, 12,058 lines, 665 theorems: 561 with the three
  standard axioms, 45 × `[propext, Quot.sound]`, 57 × `[propext]`, 2 none; no
  `sorry`). First build. Receipts regenerated. Next: S12-d (`Var(μ_h) ≤ V_h
  log 2 + 2δ`), then S9-d.

## Iteration 81 — 2026-10-19, 15:48 -03

- Woken by the side lane's S12-a verdict and its priority call (S12 (2)
  first); main frozen at `1c5c19d`. The PR body refresh is retried.
- **S12-b verified — the DK step for either sign (`dk_log_either`, via
  `varMu_neg`: `Var(μ_(m−h)) = Var(μ_h)`), the iterated step (`dk_log_iter`),
  the ladder walk (`dk_walk`: `|log n_(x+Nh) − log n_x| ≤ (Σ b_i)·Var(μ_h)`
  for `N = Σ b_i q_i` over DK-admissible `q_i`), and the greedy Ostrowski
  decomposition (`DK.ostrowski_greedy`: every `N < q n` is `Σ_(i<n) b_i q_i`
  with `Σ b_i + 1 ≤ Σ_(1≤i≤n) a_i`, for a `Ladder` `q 0 = 1`, `q 1 = a 1`, `q
  (i+2) = a (i+2) q (i+1) + q i`)** in `CycleSpectrum.lean` (sha256
  `6e9d93df…9277`, 11,972 lines, 661 theorems: 557 with the three standard
  axioms, 45 × `[propext, Quot.sound]`, 57 × `[propext]`, 2 none; no `sorry`).
  Third build (a structure field `rec` collides with the recursor; `if` under
  beta-redexes and deprecated `if_pos`/`if_neg`; eta-mismatch `∑ i, b i`
  versus `s.sum b` for omega; a `linear_combination` sign). Receipts
  regenerated. Next: S12-c, the assembly `B ≤ (K − 1)·Var(μ_h)` for `gcd(h, m)
  = 1` (every position is `x + N h mod m`, `N < m`).

## Iteration 80 — 2026-10-19, 15:38 -03

- Woken by the side lane's S9-c verdict and S12 posting; the discrete
  Denjoy–Koksma question analysed and answered (strict Diophantine hypothesis;
  all proper convergents), the S12 denominator corollary reviewed; main frozen
  at `1c5c19d`. Monitor re-armed on expiry. The PR body refresh is retried.
- **S12-a verified — the discrete Denjoy–Koksma inequality `|Σ_(k<q) f(x +
  kh)| ≤ Σ_(t<m) |f(t+1) − f t|` for `m`-periodic zero-mean `f` with `q h = p
  m + r`, `q r < m`, `gcd(p, q) = 1` (`DK.dk_discrete`, `DK.dk_core`), by the
  one-point-per-cell argument with integer weights, and its cycle form `|log
  n_(x+qh) − log n_x| ≤ Var(μ_h)` (`OddCycle.dk_log`)** in
  `CycleSpectrum.lean` (sha256 `4a71fc9f…8b67`, 11,754 lines, 654 theorems:
  552 with the three standard axioms, 43 × `[propext, Quot.sound]`, 57 ×
  `[propext]`, 2 none; no `sorry`). Second build
  (`Finset.card_eq_sum_card_fiberwise` now takes `Set.MapsTo`;
  `Nat.mul_le_mul_right` with `j < q` yields `j.succ * m`; omega needs
  matching product atoms; lemmas applied to lambdas come back beta-reduced, so
  `simp only at` makes no progress). Receipts regenerated. Next: S12 (2) via a
  greedy Ostrowski decomposition, or S9-d (the `q = den(w)` glue).

## Iteration 79 — 2026-10-19, 15:18 -03

- Woken by the side lane's S8-a verdict; queue item 4's converse found not
  bounded (frozen R25–R43 framework), C013 §3's resultant algebra judged
  multi-iteration; the side lane's S9-c proposal with its computed constant
  taken up after an independent margin computation. Main frozen at `1c5c19d`.
  The PR body refresh is retried.
- **S9-c verified — S9 (ii) in linear form: for a primitive cycle with odd
  `q`, `m ≥ 2^19` and a rotation with exactly three mismatches, `(m/70) log 2
  < log q + δ + λ` (`three_mismatch_denominator_law`), via S7's chain with the
  global-drift ceiling: `n_le_drift`, `log_of_drift_bound`,
  `three_mismatch_witness_drift`, `numeric_WA_drift`, `numeric_F_drift`, and
  `no_three_mismatch_of_small_drift` (no gap, no `L/q` hypothesis)** in
  `CycleSpectrum.lean` (sha256 `3523e28e…645e`, 11,270 lines, 635 theorems:
  535 with the three standard axioms, 41 × `[propext, Quot.sound]`, 57 ×
  `[propext]`, 2 none; no `sorry`). First build. Receipts regenerated. Next:
  the `q = den(w)` glue between the word side (C008/C009) and the `OddCycle`
  parameter, if the file has the construction; else the (1, 1, 2) window
  theorem or the side lane's first height statement.

## Iteration 78 — 2026-10-19, 15:03 -03

- Woken by the side lane's S9-b verdict with the exact S8 by-product
  statements; its S11 note (C013 with the replayed gap instead of Matveev)
  read and reviewed; main frozen at `1c5c19d`. The PR body refresh is retried.
- **S8-a verified — the by-products of S8: `ones_run_dvd` (odd `q`, a run of
  `r` ones: `2^r ∣ n_(i₀) + q`, `2·3^r ∣ n_(i₀+r) + q`), `ones_run_le` (`≤`,
  not strict: `3 → 5`), and the 1-cycle `one_cycle_D_dvd` (`D ∣ 2^(A−m) − 1`),
  `one_cycle_D_le`, `one_cycle_pow_lt`, `no_one_cycle_of_gap` (`m ≥ 2^13`;
  exact threshold `4287`), with `one_step_add_q`, `ones_run_identity`,
  `m_le_Apre`, `Apre_ones`, `Cpre_ones`** in `CycleSpectrum.lean` (sha256
  `8abc45c4…935f`, 10,874 lines, 628 theorems: 528 with the three standard
  axioms, 41 × `[propext, Quot.sound]`, 57 × `[propext]`, 2 none; no `sorry`).
  Third build (`IsCoprime.dvd_of_dvd_mul_left/right` orientation;
  `pow_lt_pow_left`/`pow_le_pow_left` are not in this Mathlib — `gcongr`;
  `push_neg` deprecated). Receipts regenerated. Next: the remaining part of
  queue item 4 if it is a bounded unit, else the (1, 1, 2) window theorem,
  pending the side lane's next mechanism.

## Iteration 77 — 2026-10-19, 14:52 -03

- Woken by the side lane's S9-a verdict and its queue suggestion (S9-b first);
  its decision to pause `ρ ≥ 5` and the S10 headline change (`efc8caf`)
  recorded. Main frozen at `1c5c19d`. Monitor re-armed on expiry. The PR body
  refresh is retried.
- **S9-b verified — S9 (i), the two-mismatch denominator law at general `q`:
  for a primitive cycle with letters `≥ 1` (or odd `q`) and a rotation with
  exactly two mismatches, `log 2 + ⌈(m−2)/2⌉ log 3 < log q + (m−1) log(3/2) +
  δ + λ`, `δ = A log 2 − m log 3`, `λ = log(m 2^A/(3D))`
  (`two_mismatch_denominator_law`, `…'`, `…_odd`), with `exists_longest_run`,
  `D_div_le_delta` and `three_L_D_le` (S7's (F4))** in `CycleSpectrum.lean`
  (sha256 `c7424159…0268`, 10,687 lines, 617 theorems: 517 with the three
  standard axioms, 41 × `[propext, Quot.sound]`, 57 × `[propext]`, 2 none; no
  `sorry`). First build. Receipts regenerated. Next: the S8 by-products
  (`ones_run_dvd`; the 1-cycle through `D ∣ 2^(A−m) − 1`), from the S8 note's
  §1 (5) and §4.

## Iteration 76 — 2026-10-19, 14:43 -03

- Woken by the monitor (sidekick `c42326e`: the S10-a verdict and the `v₂ ≠
  v₄` model update). Three review points sent (trivial rotations, finite-`m`
  threshold, one rotation per region), all checked or adopted by the side
  lane; its correction of my small-rotation remark accepted; its `s = 5, 6`
  survivors recorded. Main frozen at `1c5c19d`. The PR body refresh is
  retried.
- **S9-a verified — the global-drift ceiling `n_k 2^(A_k) 3^m ≤ n_0 3^k 2^A`
  for `k ≤ m` (`global_drift`, from the exact prefix and closing identities,
  no hypothesis on `L/q`), its log form `log n_k + X_k log 2 ≤ log L + k
  log(3/2) + δ` with `δ = A log 2 − m log 3` (`global_drift_log`), and the
  height bounds `h_k log 2 ≤ k log(3/2) + δ` (`h_le_drift`) and `B log 2 ≤ (m
  − 1) log(3/2) + δ` (`B_le_drift`), with `Cpre_mul_pow_le` and
  `Apre_eq_excess_add`** in `CycleSpectrum.lean` (sha256 `a05396ef…c79a`,
  10,525 lines, 611 theorems: 511 with the three standard axioms, 41 ×
  `[propext, Quot.sound]`, 57 × `[propext]`, 2 none; no `sorry`). Second build
  (an `add_le_add_left` argument order). Receipts regenerated. Next: the S8
  by-products (`ones_run_dvd`, the 1-cycle through `D ∣ 2^(A−m) − 1`), then
  S9-b if wanted.

## Iteration 75 — 2026-10-19, 14:33 -03

- Woken by the monitor (sidekick `a203cc1`, `9efda9b`: the `ρ ≥ 4` milestone
  entry and its scoping). The entry's EXT-1 attribution checked against STATE
  and confirmed to the side lane. Main frozen at `1c5c19d`. The PR body
  refresh is retried.
- **S10-a verified — the four-mismatch dichotomy (`four_mismatch_dichotomy`:
  `|D| = |U| = 1` with two non-changes, or `|D| = |U| = 2` with none) and the
  cyclic alternation in the two-and-two case (`four_mismatch_alternation`:
  `mis h = {a, b, c, d}`, `a < b < c < d < m`, `down, up, down, up` or `up,
  down, up, down`), with the partition `mis_card_partition`, the
  between-change lemmas and the period lemmas** in `CycleSpectrum.lean`
  (sha256 `ab47164c…a89a`, 10,402 lines, 605 theorems: 505 with the three
  standard axioms, 41 × `[propext, Quot.sound]`, 57 × `[propext]`, 2 none; no
  `sorry`). Second build (the Mathlib lemma is
  `card_filter_add_card_filter_not`; `filter_eq_empty_iff` has a
  strict-implicit binder; a `tauto` on a permuted four-way disjunction timed
  out and was replaced by a cardinality argument). Receipts regenerated. Next:
  S9-a.

## Iteration 74 — 2026-10-19, 14:17 -03

- Woken by the scheduled tick; the side lane's S7-d part 1 verdict (feed
  `f6b616b`) checked and accurate; its S10 bug report, retraction and
  fixed-model finding (`218b0c1`, `f3d907e`) read; my single-drop-case error
  corrected and the `window_conditions` remark sent (both adopted). Main
  frozen at `1c5c19d`. The PR body refresh is retried.
- **S7-d (part 2) verified — the assembly `no_three_mismatch_of_gap`
  (primitive, `q = 1`, the linear-form gap (172, 341), `m ≥ 2^19`, `L ≥ 2^20`,
  rotation `1 ≤ h < m` ⇒ not exactly three mismatches) and
  `four_le_mis_card_of_gap` (with S6 and `hB`: every rotation has at least
  four mismatches — `ρ ≥ 4` given the gap), with the helpers `log_of_bound`,
  `log_of_bound'`** in `CycleSpectrum.lean` (sha256 `afd0892b…e111`, 10,163
  lines, 595 theorems: 497 with the three standard axioms, 41 × `[propext,
  Quot.sound]`, 55 × `[propext]`, 2 none; no `sorry`). Second build (a real
  literal `1` defaulting to `ℤ` in a helper's `≠ 0` fact). Receipts
  regenerated by the new `axioms_pipeline.py` (clean build asserted: exit 0,
  no diagnostics). Next: the `s = 4` dichotomy with the cyclic interleaving of
  the changes, then S9-a.

## Iteration 73 — 2026-10-19, 13:51 -03

- Woken by the sidekick's messages (`f5efd81`…`16ed9b5`): **S7-c part 2
  verified** by the side lane; S7-d guidance received; **S8 headline withdrawn
  by its author** (the survivors fail rotation `2h`); the run law at rotation
  `2h` confirmed available (parametric lemmas); this lane's S8 review gap
  recorded; S10 preliminary noted. Main frozen at `1c5c19d`. Monitor re-armed
  on expiry. The PR body refresh still fails (GitHub GraphQL error, five
  attempts).
- **S7-d (part 1) verified — the numeric conditions of S7 at `m ≥ 2^19` over
  `ℝ`: `log_three_bounds` (`1054/665 < log₂3 < 485/306`), `numeric_WA`
  (conditions W and A from the run bound, the longest run, the
  witness-versus-ceiling inequality at the maximum, `D > 0` and the `L`-bound)
  and `numeric_F` (the final contradiction from `m − 3 ≤ τ + 2T` and the
  witness inequality)** in `CycleSpectrum.lean` (sha256 `10a4ec83…06fd`, 9880
  lines, 591 theorems: 493 with the three standard axioms, 41 × `[propext,
  Quot.sound]`, 55 × `[propext]`, 2 none; no `sorry`). Third build (`norm_num`
  does not evaluate real powers above its exponent threshold 256: evaluate in
  `ℕ` under `set_option exponentiation.threshold 1100` and cast). The
  `linarith` steps closed at the first attempt after bounding seven products
  by numerals. Receipts regenerated. Next: S7-d part 2, the assembly
  `no_three_mismatch_of_gap`.

## Iteration 72 — 2026-10-19, 13:40 -03

- Woken by the sidekick's messages (`f07182b`…`f5efd81`): **S7-c part 1
  verified** by the side lane; the Step 5 simplification and the `m = 2^19`
  margins for S7-d received. Main frozen at `1c5c19d`. The PR body refresh
  failed three times on a transient GitHub GraphQL error (STATE itself is
  committed).
- **S7-c (part 2) verified — Step 5: with the aligned pair and the windows,
  the third mismatch is below `e_a` or between `e_a` and `e_b`; the run ending
  at it has its witness (`n_{e_c+h}` or `n_{e_c}`) at an index at most `τ + τ′
  + 1`, so `2·3^τ < L (3/2)^{τ+τ′+1} (1 + q/(3L))^{τ+τ′+1}`, with the three
  runs exhibited and summing to `m − 3`** in `CycleSpectrum.lean` (sha256
  `01de2bfa…e88f`, 9788 lines, 588 theorems: 490 with the three standard
  axioms, 41 × `[propext, Quot.sound]`, 55 × `[propext]`, 2 none; no `sorry`):
  `OddCycle.agree_of_ne_three`, `agree_of_pos`, **`three_mismatch_witness`**.
  Second build (three `rwa` linter suggestions and an unused hypothesis —
  linter output counts as not clean). Receipts regenerated. Next: S7-d —
  assemble `run_bound_max`, `hsep_of_runs`, `three_mismatch_structure`,
  `three_mismatch_witness` with the gap and the numeric step at `m ≥ 2^19`
  into `no_three_mismatch_of_gap`.

## Iteration 71 — 2026-10-19, 13:31 -03

- Woken by the monitor and the sidekick's messages (`4b355ee`…`d9c8549`):
  **S7-b part 3b verified** by the side lane; **S9 reviewed** (denominator
  laws at any `q`: no hidden `q = 1`; drift caveat intrinsic, general ceiling
  with `min`); **this lane's iteration-63 "sharp in exponent" remark
  corrected** (both bounds are lower bounds; the family's `den ≈ D`). Main
  frozen at `1c5c19d`.
- **S7-c (part 1) verified — Step 1: every agreeing run with `z ≠ 0` at its
  end has `2·3^t < L (3/2)^{m−1} (1 + q/(3L))^{m−1}`; with exactly three
  mismatches the forward arc between two of them is at most `2(T + 1)` for any
  uniform run bound `T`, so distinct mismatches have both arcs at least `m −
  2(T + 1)` (the spacing hypothesis of part 3b)** in `CycleSpectrum.lean`
  (sha256 `fa53df45…ecce`, 9592 lines, 585 theorems: 487 with the three
  standard axioms, 41 × `[propext, Quot.sound]`, 55 × `[propext]`, 2 none; no
  `sorry`): `OddCycle.run_bound_max`, `third_mismatch`, `eq_third`,
  **`arc_le`**, **`hsep_of_runs`**. Second build (an unascribed real literal
  defaulted to `ℤ`). Receipts regenerated. Next: S7-c part 2 — Step 5 (the
  witness index of the third run, `n_le_climb` at it) and Step 6 (the count `m
  − 3 ≤ 2 t_max + τ_max`); then S7-d (the numeric conditions W, A, F at `m ≥
  2^19`).

## Iteration 70 — 2026-10-19, 13:20 -03

- Woken by the sidekick's messages and pushes `52f0303`…`aa2130d`: **S7-b part
  3a verified** by the side lane; **S8 reviewed** (the four-mismatch map:
  constructions check; the claim rescoped as relaxation feasibility on
  request); S9 preview (global-drift ceiling) received and found correct. Main
  frozen at `1c5c19d`. Monitor re-armed on expiry.
- **S7-b (part 3b) verified — the window structure from the spacing bound: `σ
  ≥ 2d − 1` with the two located mismatches forces `d ≤ h ≤ j`; `σ ≥ d` makes
  each window hold one mismatch, so its other positions agree; assembled with
  parts 2 and 3a into `three_mismatch_structure` (`e_a ∈ [j − h, m − h)` a
  `+→−` change, `e_b ∈ [j, m)` a `−→+` change, `d ≤ h ≤ j`, `e_b = e_a + h`)**
  in `CycleSpectrum.lean` (sha256 `993cc7ff…32a3`, 9452 lines, 580 theorems:
  482 with the three standard axioms, 41 × `[propext, Quot.sound]`, 55 ×
  `[propext]`, 2 none; no `sorry`): `OddCycle.window_conditions`,
  `unique_in_window`, `agree_of_window`, **`three_mismatch_structure`**.
  Second build (`Nat.mod_eq_sub_mod` for the residue; the window lemmas need
  only `d ≤ σ`, since `d = 1` gives `σ ≥ 1` only). Receipts regenerated. Next:
  S7-c — Step 1's uniform run bound `t ≤ t_max` and the spacing bound `σ = m −
  2(t_max + 1)` from `Σ t_k = m − 3`, Step 5's witness index and refined
  ceiling; then S7-d.

## Iteration 69 — 2026-10-19, 13:09 -03

- Woken by the sidekick's message (`8e8c058`): **S7-b part 2 verified** by the
  side lane; independent confirmation of S7 relayed; condition P dropped from
  the formal plan (implied by the windows); S8 preview (size method stops at
  `s = 3`). Main frozen at `1c5c19d`.
- **S7-b (part 3a) verified — the alignment lemma: `X_c + X_d + m = A`; under
  `d ≤ h ≤ j` with one mismatch per window, `e_b ≠ e_a + h ⇒ X_d ≤ 2 X_c` (the
  shift `i ↦ i + h − m` injects the descent into the climb, and `a_{e_b}` is a
  copy of a climb letter); with condition A, `e_b = e_a + h`** in
  `CycleSpectrum.lean` (sha256 `e8128174…5128`, 9334 lines, 576 theorems: 478
  with the three standard axioms, 41 × `[propext, Quot.sound]`, 55 ×
  `[propext]`, 2 none; no `sorry`): `OddCycle.excess_eq_sum`, `dexcess` (def),
  **`excess_add_dexcess`**, **`dexcess_le_two_excess`**, **`alignment`**.
  Second build (an unused-variable warning: the transfer needs no letter
  hypothesis). Receipts regenerated. Next: S7-b part 3b — the window structure
  from the spacing bound (`d ≤ h ≤ m − d`, one mismatch per window), then S7-c
  (witness index, refined ceiling) and S7-d (numeric step).

## Iteration 68 — 2026-10-19, 13:01 -03

- Woken by the sidekick's message (`4a17854`): **S7-b part 1 verified** by the
  side lane; its telescoping suggestion for the counting lemma adopted. Main
  frozen at `1c5c19d`.
- **S7-b (part 2) verified — the sign-change counting: `σ_i = [z_i > 0]`
  telescopes over a period, so the `+→−` and `−→+` changes are equinumerous; a
  change happens only at a mismatch; discrete intermediate value locates a
  `+→−` change in `[j − h, m − h)` and a `−→+` change in `[j, m)`; with
  exactly three mismatches there is exactly one change of each kind and a
  mismatch without change** in `CycleSpectrum.lean` (sha256 `60c3aa13…9ce2`,
  9229 lines, 572 theorems: 474 with the three standard axioms, 41 ×
  `[propext, Quot.sound]`, 55 × `[propext]`, 2 none; no `sorry`):
  `OddCycle.z_per`, `sgn`, `sgn_per`, `down`, `up`, `down_per`, `up_per`,
  `sgn_succ_sub`, `sum_sgn_tele`, **`card_down_eq_card_up`**,
  **`down_mem_mis`**, **`up_mem_mis`**, **`exists_down`**, **`exists_up`**,
  **`exists_down_window`**, **`exists_up_window`**, `down_mod`, `up_mod`,
  **`three_mismatch_changes`**. Third build
  (`Finset.exists_mem_notMem_of_card_lt_card` is the current name of the
  card-lt lemma — replaced by a direct subset-cardinality contradiction; a
  membership proof must be stated before `Finset.mem_union_left`). Receipts
  regenerated. Next: S7-b part 3 — window disjointness (`d ≤ h ≤ m − d`) and
  alignment (`e_a + h = e_b`) by excess transfer; then S7-c, S7-d.

## Iteration 67 — 2026-10-19, 12:50 -03

- Woken by the sidekick's messages and pushes `d978b57`…`e4d97ad`: **S7-a
  verified** by the side lane; **S7 note reviewed** (three-mismatch exclusion
  at `q = 1`, `m ≥ 452,695`): Steps 3–5 attacked line by line, no gap; four
  explicitness points applied; S8 (`s = 4` frontier) announced. Main frozen at
  `1c5c19d`.
- **S7-b (part 1) verified — `Σ_{i<m} a_{i+k} = Σ_{i<m} a_i`, so exactly one
  mismatch is impossible; the run witness `max(n_e, n_{e+h}) > 2·3^t`; the
  excess `X_k` and the tracked ceiling `n_k 2^{X_k} ≤ L (3/2)^k (1 +
  q/(3L))^k`, `(h_k + X_k) log 2 ≤ k (log 3 − log 2) + k log(1 + q/(3L))`** in
  `CycleSpectrum.lean` (sha256 `dc9c5c7b…129d`, 9013 lines, 556 theorems: 465
  with the three standard axioms, 41 × `[propext, Quot.sound]`, 48 ×
  `[propext]`, 2 none; no `sorry`): `OddCycle.sum_a_shift`,
  **`mis_card_ne_one`**, **`witness_gt`**, `excess` (def), `excess_succ`,
  **`n_mul_pow_excess_le`**, **`h_add_excess_le`**. Second build (an index
  rewrite in a `sum_congr`, and `rw … at *` replaced by targeted rewrites).
  Receipts regenerated. Next: S7-b part 2 — the sign-change counting over `mis
  h` (as many `+→−` as `−→+` changes, both `≥ 1`), the window location of the
  two changes, window disjointness and alignment.

## Iteration 66 — 2026-10-19, 12:41 -03

- Woken by the sidekick's message (`43e0e25`): **S6-b/c verified** by the side
  lane (independent recheck of the numeric step); **S7 sketch pre-reviewed**
  (three-mismatch exclusion at `q = 1`: step (1) right, (2) constants agree,
  (3) right with both window conditions, (4) three questions on the witness).
  Main frozen at `1c5c19d`.
- **S7-a verified — the sign lemma: `z` keeps its sign across an agreeing
  position and along an agreeing run; strict extremes in a primitive cycle;
  `δ_0 > 0`, `δ_{−h} < 0`, `δ_j < 0`, `δ_{j−h} > 0`** in `CycleSpectrum.lean`
  (sha256 `ea6be221…db87`, 8856 lines, 550 theorems: 460 with the three
  standard axioms, 41 × `[propext, Quot.sound]`, 47 × `[propext]`, 2 none; no
  `sorry`): `OddCycle.z_pos_step`, `z_neg_step`, **`z_pos_run`**,
  **`z_neg_run`**, `n_lt_of_ne`, `n_lt_max_of_ne`, **`z_min_pos`**,
  `pred_add_mod`, **`z_pred_min_neg`**, **`z_max_neg`**, **`z_pred_max_pos`**.
  Second build (`mul_neg_iff_of_pos_left` does not exist — use
  `mul_neg_of_pos_of_neg` and `neg_of_mul_neg_right`; a lemma with no `Γ` in
  its statement cannot use `Γ.hm`). Receipts regenerated. Next: review the S7
  note when it lands; the sign-change counting and the excess-transfer lemma
  are the formal candidates if (3)–(4) survive.

## Iteration 65 — 2026-10-19, 12:07 -03

- Woken by the sidekick's message (`f2921dc`): **S6-a verified** by the side
  lane; framing dispute closed; S7 announced. Main frozen at `1c5c19d`.
- **S6-b/c verified — C011's two-mismatch exclusion by the S6 route, formal
  end to end given the gap: `two_mismatch_bound` (S5-a at `s = 2` with the
  ceiling), `no_two_mismatch` (with the numeric step as an explicit
  hypothesis), `numeric_step` (`m ≥ 2^15`, `L ≥ 2^20`, `(c, μ) = (172, 341)`,
  from `log 2` decimal bounds, `3^41 < 2^65`, `2^19 < 3^12`, a tangent bound
  for `log m` and `log(1+x) ≤ x`), and `no_two_mismatch_of_gap`** in
  `CycleSpectrum.lean` (sha256 `830d1ba7…7131`, 8725 lines, 539 theorems: 450
  with the three standard axioms, 40 × `[propext, Quot.sound]`, 47 ×
  `[propext]`, 2 none; no `sorry`). Both parts compiled first try. Receipts
  regenerated. Next: review S7 as it lands; a formal `s = 3` reading of
  `mismatch_height` as a lower bound on `B` is the natural companion.

## Iteration 64 — 2026-10-19, 11:50 -03

- Woken by the sidekick's messages and pushes `a3c4d91`…`790725e`: **S5-a
  verified** by the side lane; **S6 reviewed** (derivation correct; ceiling
  corrected to no `+1` and `(m − 1)` in the `ε` term; `L ≥ 3` suffices
  eventually). **Error of this lane withdrawn**: the suggestion that
  two-mismatch words fall under the `k`-cycle exclusions — refuted by the side
  lane's near-periodic example `(122)^a 1222 (122)^b` (two mismatches under
  rotation by `3`, about `m/3` local minima). Main frozen at `1c5c19d`.
- **S6-a verified — the height ceiling: `n_{i+1} ≤ (3/2)^{[a_i=1]} (1 +
  q/(3L)) n_i`, `n_j ≤ L (3/2)^{u_j} (1 + q/(3L))^j`, `h_j log 2 ≤ u_j (log 3
  − log 2) + j log(1 + q/(3L))`, and `B log 2 ≤ (m−1)(log 3 − log 2) + (m−1)
  log(1 + q/(3L))` when `B` is attained, with letters `≥ 1` automatic at `q =
  1`** in `CycleSpectrum.lean` (sha256 `da2bf768…74a0`, 8601 lines, 535
  theorems: 446 with the three standard axioms, 40 × `[propext, Quot.sound]`,
  47 × `[propext]`, 2 none; no `sorry`): `OddCycle.eps_nonneg`,
  `one_add_eps_pos`, `a_pos_of_odd`, `ones` (def), `ones_succ`, `ones_le`,
  **`n_succ_le`**, **`n_le_climb`**, **`h_le_climb`**, **`B_le_ceiling`**,
  **`B_le_ceiling_q1`**. Second build (`positivity` fails on `Int`-cast signs
  and on metavariable goals inside `rw`; `unfold` of a recursive def gives a
  `match`, use an `rfl` equation). Receipts regenerated. Next: S6-b, the
  composition excluding `s = 2` with the numeric step as an explicit
  hypothesis, then its discharge.

## Iteration 63 — 2026-10-19, 11:36 -03

- Woken by the sidekick's messages and pushes `2858b07`…`47c2fa8`: **S2-c
  verified** by the side lane; **S5 reviewed** (composition correct;
  off-by-one in the constant found and accepted; (a)–(c) confirmed with a
  sharper height ceiling; consistency check against C013 §3's family added to
  its note). Main frozen at `1c5c19d`.
- **S5-a verified — the mismatch–height trade-off as a two-library
  composition: the valuation word is `m`-periodic, a full period of agreement
  forces `z = 0` (so a nonidentity rotation of a primitive cycle has a
  mismatch), the pigeonhole `m ≤ (T+1) s`, the run bound `6·3^t < 2^{B+1+c}
  m^{μ+1}` from C013-b with the explicit gap, and `mismatch_height`: `∃ t, m ≤
  s(t+1) ∧ 6·3^t < 2^{B+1+c} m^{μ+1}`** in `CycleSpectrum.lean` (sha256
  `68c589ba…9ece`, 8427 lines, 525 theorems: 438 with the three standard
  axioms, 39 × `[propext, Quot.sound]`, 46 × `[propext]`, 2 none; no `sorry`):
  `OddCycle.a_per`, `a_add_mul`, `a_mod`, `agree_mod`, `agree_add_mul`,
  **`z_eq_zero_of_agree_period`**, **`exists_mis`**, `exists_mis_ge`,
  **`pigeonhole`**, **`run_bound_of_gap`**, **`mismatch_height`**. Compiled
  first try. Receipts regenerated. Next: review S6 (the height obstacle) as it
  lands; a formal unit for the height ceiling `B ≤ (log₂3 − 1)(m−1) + …` is a
  natural candidate.

## Iteration 62 — 2026-10-19, 11:24 -03

- Woken by the monitor (sidekick `a6e25c3`/`226e5cd`): **S3-a verified** by
  the side lane, with a 14,774-pair probe of `inversion_iff`; S5 started
  there. Main frozen at `1c5c19d`.
- **S2-c verified — the orbit exponent density: one orbit step raises `⌊(r₀ +
  ks)/m⌋` exactly at a high rank, `E r₀ t + ⌊r₀/m⌋ = t q′ + ⌊(r₀ + ts)/m⌋`,
  hence `E r₀ t ≥ ⌊t·A/m⌋`, and (G1)'s first inequality with the density** in
  `CycleSpectrum.lean` (sha256 `13de7cad…54b0`, 8201 lines, 514 theorems: 427
  with the three standard axioms, 39 × `[propext, Quot.sound]`, 46 ×
  `[propext]`, 2 none; no `sorry`): `OrdCycle.div_succ_step`, **`E_eq_div`**,
  **`E_ge_mul_div`**, **`G1_first_E_density`**. Compiled first try. Receipts
  regenerated. Next: review S5 as it lands; fallback C013's longest-run
  pigeonhole and orbit sums, or C012 §1's block identities.

## Iteration 61 — 2026-10-19, 11:18 -03

- Woken by the sidekick's messages and pushes `194bdfb`…`33a7429`: **S2-b
  verified** by the side lane; its S2 §4 constant re-attributed to the orbit
  exponent density `E ≥ ⌊tA/m⌋` (checked, correct); **S4 read and accepted**
  as a labelled negative search (no law for `g = gcd(C, D)` on ordered band-1
  cycles; block-divisor test negative). Main frozen at `1c5c19d`.
- **S3-a verified — C005's inversion lemma as a theorem: for `Z_i < Z_j` the
  images invert iff `h_i < h_j` and `3r < q(2^k − 1)`; at `q = 1` an inversion
  needs `k ≥ 3`, and `k = 3` forces `n_j = 8n_i + 1`; with `B = 3` that pair
  is sorted-adjacent** in `CycleSpectrum.lean` (sha256 `1a5a05ee…1ee8`, 8139
  lines, 510 theorems: 423 with the three standard axioms, 39 × `[propext,
  Quot.sound]`, 46 × `[propext]`, 2 none; no `sorry`): `OddCycle.r_pos`,
  **`inversion_iff`**, **`inversion_gap_ge_three`**,
  **`inversion_gap_three`**, **`pair_adjacent`** (`[propext, Quot.sound]`).
  Second build (my `Z_sub_of_le`/`F_sub_of_le` duplicated C005-b's; the
  existing ones are used, `F_sub_of_le` being stated as `F_j − F_i`). Receipts
  regenerated. Next: S2-c, the orbit exponent density `E r₀ t ≥ ⌊t·A/m⌋` and
  the resulting `A/m` factor in the `J` bound; then review S5 (three-mismatch
  rotations) as it lands.

## Iteration 60 — 2026-10-19, 11:05 -03

- Woken by the sidekick's messages and pushes `28f4491`…`c3b9550`: **S2-a
  verified** by the side lane; **S2 reviewed** (§1 = S2-a; §2 correct,
  formalised below; §3 a data-based rejection with a correct diagnosis; §4's
  constant queried); **S3 §1 checked** (inversion condition, `k ≤ 2`
  non-inversion with the primitivity tie, `r = 1` at `k = 3`, adjacency) and
  §3's defect recursion rederived; S4 pre-reviewed (`g = C_w/L`, `g ≤ C_c/L`).
  Main frozen at `1c5c19d`. Monitor re-armed on expiry.
- **S2-b verified — the oddness rule: `u` odd ⇔ the forced-rank gap is odd; a
  state is odd ⇔ its height is `B`; an interior gap is odd ⇔ exactly one of
  its heights is `B`; the seam gap is odd ⇔ `h_[m−1] = B`; interior forcing ⇔
  height change; band 1: interior-ending runs have odd `u`, seam-ending runs
  iff `h_[m−1] = B`** in `CycleSpectrum.lean` (sha256 `25f8beaf…0a87`, 8041
  lines, 505 theorems: 419 with the three standard axioms, 38 × `[propext,
  Quot.sound]`, 46 × `[propext]`, 2 none; no `sorry`): `OddCycle.Z_odd_iff`;
  `OrdCycle.run_quot_odd_iff_end`, `y_odd_iff`, **`gap_odd_iff`**,
  **`gap_seam_odd_iff`**, `T_ne_zero_iff`, **`band1_u_odd`**,
  **`seam_u_odd_iff`**. Second build (a duplicate `hr_le_B`; the existing one
  is used). Receipts regenerated. Next: S3-a, the inversion lemma as a theorem
  (`Z_i < Z_j` inverts iff `h_i < h_j` and `3r < q(2^k − 1)`; at `q = 1` this
  needs `k ≥ 3`, and `k = 3` forces `n_j = 8n_i + 1`), then whatever S4
  produces.

## Iteration 59 — 2026-10-19, 10:55 -03

- Woken by the sidekick's messages and pushes `c5435c7`…`9ab7807`: **lane
  change relayed** (ChatGPT's quota exhausted; main frozen at `1c5c19d`; the
  side lane becomes producer with S2, S3, …; this lane adds the
  adversarial-reviewer role; recorded in STATE as relayed, standing rules
  unchanged); **C013 unit verified** and relabelled **C013-b** (iteration 34
  holds C013-a), with the 12,550-run probe passing. Pre-review of S2's premise
  sent (exact identity, oddness not automatic, `τ` depends on `B`/`q`/seam,
  cycle equation = `gap_closed_form_filter`, side remark's integer part).
- **S2-a verified — pre-emptive formal backing for S2: run divisibility
  `2^{E_t} ∣ Δ_{r₀}`, the exact run-start recursion `2^{e_t} Δ_{orb r₀ (t+1)}
  = 3^{t+1} (Δ_{r₀}/2^{E_t}) + T(orb r₀ t)` and its two-run form, the oddness
  criterion `u` odd ⇔ `2^{E_t+1} ∤ Δ_{r₀}`, `E` additivity along the orbit,
  `Σ_{r<m} Δ_r = 2^B L` and the all-run-starts bound `Σ_{r∈R} 2^{E_r} ≤ 2^B
  L`** in `CycleSpectrum.lean` (sha256 `e0f0febe…ada0a`, 7930 lines, 497
  theorems: 411 with the three standard axioms, 38 × `[propext, Quot.sound]`,
  46 × `[propext]`, 2 none; no `sorry`): `OrdCycle.jsum_run`, **`run_dvd`**,
  `run_end_eq`, `orb_succ_eq`, **`run_start_rec`**, **`run_start_rec_two`**,
  **`run_quot_odd_iff`**, `E_add`, **`sum_gap_eq_lo`**, **`sum_run_bound`**.
  Second build (`Int.odd_iff_not_even` does not exist; `←
  Int.not_even_iff_odd`). The C013-b Lean header relabelled in the same build.
  Receipts regenerated. Next: review S2 as it lands and formalise what
  survives; fallback C013's longest-run pigeonhole and orbit sums, or C012
  §1's block identities.

## Iteration 58 — 2026-10-19, 10:42 -03

- Woken by the sidekick's message and push `74ebf13`: **C010-c verified**
  (receipts match; source scan clean), with the arrangement probe on 1,701
  arrangements of 81 reduced actual cycles and the note that the 11
  non-reduced cycles are the fixed points `n = q`. Main unchanged at
  `1c5c19d`. Read C012 `COUPLED_SYSTEM.md` and C013 `OVERLAP_THEORY.md`;
  C012's matrix theory (determinant, minors, Smith form) is too large for one
  unit, so the unit is C013 §§1–2.
- **C013-b verified — the paired-state run law and its denominator
  consequences: `z_i = n_(i+h) − n_i` even and nonzero, `2^a_i z_(i+1) = 3
  z_i` at agreeing positions, `2^E z_end = 3^t z_start` with `z_start =
  2^(E+1) k` and `z_end = 2·3^t k`, the diameter bound `H − L ≥ 2 max(2^E,
  3^t)`, `(2^(B+1) − 1) L > 2 max(2^E, 3^t)`, the real `6 δ max < m q (2^(B+1)
  − 1)` and the rational `6 D max < m q 2^A (2^(B+1) − 1)`** in
  `CycleSpectrum.lean` (sha256 `19e73031…2714`, 7816 lines, 487 theorems: 401
  with the three standard axioms, 38 × `[propext, Quot.sound]`, 46 ×
  `[propext]`, 2 none; no `sorry`): `OddCycle.z`, `runSum`, `runSum_succ`,
  `z_even`, `z_ne_zero`, **`z_step`**, `z_run`, **`z_run_factor`**,
  **`diameter_ge`**, **`K_mul_L_gt`**, `delta_pos`, **`q_bound_delta`**,
  **`q_bound_rational`**, `q_bound_rational_prim`. Compiled first try.
  Receipts regenerated. Next: whichever of main's newest claims most needs
  formal backing; otherwise C013's longest-run pigeonhole and orbit sums, or
  C012 §1's block compression identities.

## Iteration 57 — 2026-10-19, 10:28 -03

- Woken by the sidekick's message and pushes `f716dad`/`41d32b2`: **C010-b
  verified** (receipts match; source scan clean), with the probe on all 92
  actual cycles and 337 rational ordered cycles (gcd `1`, positive gaps,
  common denominator `q`), and the scope note that the prose's §2 is for
  unordered cycles. Main unchanged at `1c5c19d`.
- **C010-c verified — C010 §2 without the ordering hypothesis: gcd `1` of the
  scaled states of any reduced cycle with attained maximal height, of the
  complete gaps of any arrangement of one period, and the exact common
  denominator `q` of the normalised states and gaps (`k` clears `Z/q` or `G/q`
  iff `q ∣ k`)** in `CycleSpectrum.lean` (sha256 `1379f455…bedf`, 7600 lines,
  475 theorems: 391 with the three standard axioms, 37 × `[propext,
  Quot.sound]`, 45 × `[propext]`, 2 none; no `sorry`):
  `OddCycle.Z_dvd_isUnit`, `Z_dvd_isUnit_of_lt`, **`cgap_dvd_isUnit`**,
  **`q_dvd_of_dvd_mul`**, `q_clears`, **`clears_q_iff`**, `q_le_of_clears`,
  **`clears_q_cgap_iff`**; `OrdCycle.Z_dvd_isUnit` now delegates. Second build
  (a duplicate `Z_mod` — the existing one is reused — and explicit arguments
  for `Int.gcd_dvd_left/right`). Receipts regenerated. Next: whichever of
  main's newest claims most needs formal backing; otherwise C012's
  Smith-form/determinant statements or C013's polynomial forms.

## Iteration 56 — 2026-10-19, 10:16 -03

- Woken by the sidekick's message and pushes `a6547ec`/`0be4de1`: **C006-f
  verified** (receipts match), with the separation probe (6 of 44 unordered
  cycles also have the phase-`0` mechanical word). Main unchanged at
  `1c5c19d`.
- **C010-b verified — the complete dyadic gap lattice: the telescoping inverse
  (1), the divisor, integrality and common-denominator equivalences, the order
  cone, and gcd `1` for the sorted states and gaps of a reduced cycle** in
  `CycleSpectrum.lean` (sha256 `abc5ff86…0eb3`, 7492 lines, 467 theorems: 383
  with the three standard axioms, 37 × `[propext, Quot.sound]`, 45 ×
  `[propext]`, 2 none; no `sorry`): `cgap`, `sum_cgap_prefix`, `sum_cgap`,
  **`Z_eq_sum_cgap`**, **`dvd_cgap_iff`**, **`cgap_int_iff`**, `cgap_smul`,
  **`clears_iff`**, **`cgap_pos_iff`**; `OrdCycle.gap_eq_cgap`,
  **`Z_dvd_isUnit`**, **`gap_dvd_isUnit`**. Compiled first try. Receipts
  regenerated. Next: whichever of main's newest claims most needs formal
  backing; otherwise C012's Smith-form/determinant statements or C013's
  polynomial forms.

## Iteration 55 — 2026-10-19, 10:09 -03

- Woken by the monitor and the sidekick's message/push `8ed0d25`: **C006-e
  verified** (receipts match; probe on 370 ordered cycles), with the
  observation that the normalised word is `mech(A, m, 0)` for every ordered
  cycle. Main unchanged at `1c5c19d`.
- **C006-f verified — C005's order lemma in word form at any `q`: the
  normalised word of every ordered cycle is `mech A m 0`, `gcd(A, m) = 1`, and
  `gcd(C_c, D) = 1`** in `CycleSpectrum.lean` (sha256 `392efa2c…d1cc`, 7305
  lines, 456 theorems: 372 with the three standard axioms, 37 × `[propext,
  Quot.sound]`, 45 × `[propext]`, 2 none; no `sorry`): `OrdCycle.c_formula`,
  `Apre_eq_ord`, **`cword_eq_mech_ord`**, **`coprime_Apre`**,
  **`Cc_gcd_one_ord`**. Compiled first try. Receipts regenerated. Next:
  whichever of main's newest claims most needs formal backing; otherwise
  C010's gap-map identities or the informal remainder of C012/C013.

## Iteration 54 — 2026-10-19, 10:03 -03

- Woken by the monitor: the sidekick recorded EXT-1 and the three mmusson
  statement checks (feed 09:43, 09:51) with the agreed labels. Main unchanged
  at `1c5c19d`. Monitor re-armed at 09:59.
- **C006-e verified — the normalised intercept `C_c`, `C_h ≤ C_c`, the
  mechanical link at `q = 1` and the `C_c` forms of (G1)** in
  `CycleSpectrum.lean` (sha256 `935508e4…0629`, 7242 lines, 451 theorems: 367
  with the three standard axioms, 37 × `[propext, Quot.sound]`, 45 ×
  `[propext]`, 2 none; no `sorry`): `OddCycle.Ppre`, `Ppre_succ`,
  **`Ppre_eq`**, `Cc`, `Cc_succ`, `cword_prefix`, **`Cpre_le_Cc`**,
  **`D_mul_n_le`**, **`cword_eq_mech`**, **`Cc_gcd_one`**;
  `OrdCycle.G1_second_c`, `run_bound_c`. Two compile rounds (a `+ 0` that `rw
  [Nat.add_zero]` would not remove — stated away by `show`; an `omega` atom
  mismatch `j.succ` vs `j + 1` inside `/ m` — replaced by
  `Nat.add_sub_add_left`/`Nat.add_sub_assoc`). Receipts regenerated. Next:
  whichever of main's newest claims most needs formal backing; otherwise
  C010's gap-map identities.

## Iteration 53 — 2026-10-19, 09:41 -03

- Woken by the sidekick's message and pushes `2df3ccc`/`2bc1961`: **C006-d
  verified**, with the recommendation to replay mmusson/collatz's `gap_all` as
  an external audit ahead of the bookkeeping units. Main unchanged at
  `1c5c19d`. Monitor re-armed at 09:22.
- **EXT-1: external replay of `Collatz.gap_all` — PASS.** In the container:
  clone at depth 1 (HEAD `e292ac0d`), elan install of
  `leanprover/lean4:v4.34.0-rc2`, `lake update` (Mathlib `v4.34.0-rc2`, rev
  `85e3a25e`), `lake exe cache get`, `lake build +CycleLenPoly` (first run
  5m37s with a transient `OneCircuit` failure; incremental rerun 3m35s, 3478
  jobs), then `#print axioms`: `gap_all`, `gapBelow_big`, `linFormHyp_uncond`,
  `signApprox_Vq`, `min_le_poly_period`, `few_runs_cycle_trivial_uncond` all
  standard three; no `sorryAx`/`ofReduceBool`. Receipt:
  `receipts/mmusson_gap_all.txt` (committed as `5ec0333`; these records follow
  in a second commit because the first records script stopped at a
  wrapped-text assertion). Our `CycleSpectrum.lean` is unchanged this
  iteration (sha `12831a36…83dd`, 441 theorems). Consequence recorded in
  STATE: with `G2_of_gap_collatz`, `J > (m−1)/(175 + 342 log₂ m)` for
  hypothetical `H < 8L` Collatz cycles, `≈ 1.07·10⁷` at the literature's
  period bound; a two-library composition. Next: whichever of main's newest
  claims most needs formal backing; otherwise the `C_c` form of (G1)'s second
  inequality or C010's gap-map identities.

- **EXT-1 addendum (09:49)**: at the side lane's request, `lake build
  +NormBridge +ChristoffelMin` on the same checkout (3554 jobs, 4m44s) and
  `#check`/`#print axioms` for `NormBridge.cycle_one_move_christoffel`,
  `NormAll.no_cycle_one_move_christoffel_all`, `cycle_min_le_chr` and
  `few_runs_cycle_trivial_uncond`: all four standard three; `T` is the
  shortcut map; `chr r A j = ⌊(j+1)A/r⌋ − ⌊jA/r⌋` is this lane's `mech A r 0`;
  `oddRuns` counts odd runs (circuits), not `J`. Statements in the receipt
  addendum.
## Iteration 52 — 2026-10-19, 09:06 -03

- Woken by the sidekick's message and pushes `670701d`/`395908c`: **C006-c
  verified** (receipts match; probe on 93 actual cycles), plus a literature
  calibration: Knight's Christoffel exclusion, the mmusson/collatz Lean
  library, Fernández–Ibáñez. Read the library's README and the
  headers/statements of fifteen files through the GitHub API (not built);
  answered the side lane's two questions; corrected the claim labels of R71-a
  and C004-c to "known theorem, formalised here" and added a Literature
  calibration section to STATE. Main unchanged at `1c5c19d`. Monitor re-armed
  at 08:52.
- **C006-d verified — (G2) conditional on an explicit linear-form gap `2^A ≤
  2^c m^μ (2^A − 3^m)`** in `CycleSpectrum.lean` (sha256 `12831a36…83dd`, 7112
  lines, 441 theorems: 357 with the three standard axioms, 37 × `[propext,
  Quot.sound]`, 45 × `[propext]`, 2 none; no `sorry`):
  `OrdCycle.delta_ge_gap`, **`G2_of_gap`**, `G2_of_gap_collatz`. Compiled
  first try. Receipts regenerated. The hypothesis has the shape of
  mmusson/collatz's claimed-unconditional `gap_all` (`c = 172`, `μ = 341`);
  replaying that library in the container (different toolchain, v4.34.0-rc2)
  is a possible future unit, not started. Next: whichever of main's newest
  claims most needs formal backing; otherwise the `C_c` form of (G1)'s second
  inequality or C010's gap-map identities.

## Iteration 51 — 2026-10-19, 08:54 -03

- Woken by the sidekick's message and pushes `c702560`/`af3492c`: **R71-d and
  C006-b verified** (receipts match; probe on 97 zero-forcing stretches, 77
  with a strict `e_run` refinement). Main unchanged at `1c5c19d`. Monitor
  re-armed at 08:52.
- **C006-c verified — the exact identity (G4) `A log 2 − m log 3 = Σ log(1 +
  q/(3n_i)) ≤ mq/(3L)` over `ℝ`, for every odd cycle** in `CycleSpectrum.lean`
  (sha256 `2d600c05…fabe`, 7038 lines, 438 theorems: 354 with the three
  standard axioms, 37 × `[propext, Quot.sound]`, 45 × `[propext]`, 2 none; no
  `sorry`): `OddCycle.prod_arrow`, **`log_identity`**, **`G4`**,
  `L_mul_delta_le`. Compiled first try. Receipts regenerated. The elementary
  half of the side lane's small-`J` calibration is now formal. Next: whichever
  of main's newest claims most needs formal backing; otherwise the `C_c` form
  of (G1)'s second inequality, or C010's gap-map identities.

## Iteration 50 — 2026-10-19, 08:46 -03

- Woken by the sidekick's message and pushes `e9ee2d5`/`dd98c10`: **R71-c
  verified** (receipts match; probe `k = 1..80`; the bound is loose by a
  factor `≥ 2`). Main unchanged at `1c5c19d`.
- **R71-d and C006-b verified — `den > 1` for `k ≥ 3`, and the `e_run` form of
  the run bound** in `CycleSpectrum.lean` (sha256 `282d9102…cd36`, 6935 lines,
  434 theorems: 350 with the three standard axioms, 37 × `[propext,
  Quot.sound]`, 45 × `[propext]`, 2 none; no `sorry`):
  `two_mul_three_pow_le_four_pow`, **`den_mech_gt_one`**;
  `OrdCycle.run_bound_E`, `run_bound_E_L`, `E_ge`, `G1_first_E`. One compile
  round (a positivity fact rewritten alongside the goal in the `k/g = 1`
  branch). Receipts regenerated. Next: whichever of main's newest claims most
  needs formal backing; otherwise C006's (G4) over `Real.log`.

## Iteration 49 — 2026-10-19, 08:38 -03

- Woken by the sidekick's message and push `65d6ea9`: **R71-b verified**
  (receipts match; probe on all 31,060 phase words with `k ≤ 48`). Main
  unchanged at `1c5c19d`.
- **R71-c verified — the state bound (5), `k D < 6 C` for every phase of a
  mechanical word with `3^k < 2^A < 2·3^k`, and the integer-cycle form `k q <
  6 n_i`** in `CycleSpectrum.lean` (sha256 `82ee7c35…5761`, 6823 lines, 428
  theorems: 344 with the three standard axioms, 37 × `[propext, Quot.sound]`,
  45 × `[propext]`, 2 none; no `sorry`): `mech_term_lower`,
  `mech_summand_lower`, **`mech_state_bound`**, `exists_total`, `mech_ne_nil`,
  `mech_D_pos`, `mech_zero_min`, **`mech_cycle_state_bound`**. Compiled first
  try. Receipts regenerated. Next: whichever of main's newest claims most
  needs formal backing; otherwise C006's `(G4)`/`e_run`, or the `d > 1` remark
  of R71 §3.

## Iteration 48 — 2026-10-19, 08:29 -03

- Woken by the monitor and the sidekick's message/pushes `889ec48`/`7bc167c`:
  **S1-e verified** (receipts match), plus a calibration against small-`J`
  units (`J ≥ 6` for hypothetical `H < 8L` Collatz cycles via `G1_first` +
  Matveev + Hercher/Barina; checked, recorded in STATE) and the recommendation
  to take R71's repeated case. Main unchanged at `1c5c19d`.
- **R71-b verified — `den(z^k) = den(z)` and R71's (3) in full** in
  `CycleSpectrum.lean` (sha256 `af06a190…a0b9`, 6702 lines, 420 theorems: 337
  with the three standard axioms, 37 × `[propext, Quot.sound]`, 44 ×
  `[propext]`, 2 none; no `sorry`): `den`, `gcdCD_rep`, **`den_rep`**,
  `div_scale`, **`mech_rep`**, `mech_gcd_one_phase'`, **`den_mech`** (`den
  (mech A k l) = 2^{A/g} − 3^{k/g}`, `g = gcd(A, k)`, for `0 < k ≤ A`, `l <
  k`). One compile round: `gcdCD` is `OddCycle.gcdCD` and the block sits
  outside that namespace. Receipts regenerated. Next: whichever of main's
  newest claims most needs formal backing; otherwise R71's state bound (5) `x
  > k/6`, or C006's `(G4)`/`e_run`.

## Iteration 47 — 2026-10-19, 08:18 -03

- Woken by the monitor and the sidekick's message/push `41d96db`: **S1-c/d
  verified** (receipts match; probe on the 33 actual ordered cycles and the 65
  rational `J = 1` cycles), with the band-1 `J ≥ 3` statement suggested as the
  next unit. Main unchanged at `1c5c19d`. Monitor re-armed at 08:18.
- **S1-e verified — in band 1 with `m < A < 2m` an ordered cycle has at least
  three forced positions** in `CycleSpectrum.lean` (sha256 `d06e37ae…977b`,
  6596 lines, 414 theorems: 333 with the three standard axioms, 35 ×
  `[propext, Quot.sound]`, 44 × `[propext]`, 2 none; no `sorry`):
  `OrdCycle.hr_eq_of_no_change`, `q'_eq_one_of_range`, **`J_ge_three`** (`∀ i,
  1 ≤ a i`, `q' = 1`, `∀ i, h i ≤ 1`, `h j = 1` ⇒ `3 ≤ J`). One compile round:
  `push_neg` is deprecated in this Mathlib (warning = not clean); replaced by
  a direct `by_contra`. Receipts regenerated. Next: whichever of main's newest
  claims most needs formal backing; otherwise R71's repeated case (`den(z^k) =
  den(z)`) or C006's `(G4)`/`e_run`.

## Iteration 46 — 2026-10-19, 08:04 -03

- Woken by the sidekick's message and pushes `96e0518`/`e49c71e`: **S1-b
  verified** (receipts match; probe on 33 ordered cycles), with two stronger
  consequences proposed as cheap units. Main unchanged at `1c5c19d`.
- **S1-c/d verified — every gap of a reduced ordered cycle is coprime to `q`,
  and `J = 1` forces `D = q`** in `CycleSpectrum.lean` (sha256
  `05bbe8fc…b85b`, 6474 lines, 411 theorems: 330 with the three standard
  axioms, 35 × `[propext, Quot.sound]`, 44 × `[propext]`, 2 none; no `sorry`):
  `OrdCycle.q_dvd_off/offext/T`, **`dvd_gap_orb`**, **`dvd_gap_isUnit`**,
  **`gap_isCoprime_q`**; `orb_inj_aux`/**`orb_inj`**,
  **`T_eq_zero_of_J_one`**, `hr_eq_zero_of_J_one`, `T_seam_of_J_one`,
  **`D_eq_q_of_J_one`** (`IsCoprime q (n 0)`, `J = 1` ⇒ `2^A − 3^m = q`).
  Compiled first try. Receipts regenerated. Next: whichever of main's newest
  claims most needs formal backing; otherwise narrow ⇒ `J = 1` (closing the
  R71 link), R71's repeated case, or C006's `(G4)`/`e_run`.

## Iteration 45 — 2026-10-19, 07:48 -03

- Woken by the sidekick's message and pushes `a95a9cf`/`dc7876c`: **S1-a
  verified** (receipts match; dictionary confirmed; probe on 33 actual ordered
  `3x+q` cycles). Main unchanged at `1c5c19d`. Monitor re-armed at 07:45.
- **S1-b verified — the run-start gaps of a reduced ordered cycle are jointly
  coprime to `q`** in `CycleSpectrum.lean` (sha256 `bb6c6e5d…6cba`, 6309
  lines, 399 theorems: 318 with the three standard axioms, 35 × `[propext,
  Quot.sound]`, 44 × `[propext]`, 2 none; no `sorry`):
  `OrdCycle.isCoprime_q_two`, `isCoprime_q_three`, **`dvd_gap_run_iff`**,
  `orb_add`, `orb_pred_succ`, `orb_surj`, **`exists_run_start`**,
  **`dvd_all_gaps_isUnit`**, **`run_start_gaps_coprime`** (`Odd q`, `IsCoprime
  q (n 0)`, `d ∣ q`, `d` divides every run-start gap ⇒ `IsUnit d`). Compiled
  first try. Receipts regenerated. Next: whichever of main's newest claims
  most needs formal backing; otherwise R71's repeated case or C006's
  `(G4)`/`e_run`.

## Iteration 44 — 2026-10-19, 07:30 -03

- Woken by the sidekick's message and push `444de54`: **C005-h verified** as a
  milestone (receipts match; probe PASS incl. 7,518 arbitrary-base
  concatenations), with the feed calibration recorded. Main unchanged at
  `1c5c19d`.
- **S1-a verified — the unrolled (G3): every `D`-scaled sorted gap as a
  forcing sum** in `CycleSpectrum.lean` (sha256 `5a1df382…6687`, 6182 lines,
  390 theorems: 310 with the three standard axioms, 34 × `[propext,
  Quot.sound]`, 44 × `[propext]`, 2 none; no `sorry`): `OrdCycle.E`/`E_succ`,
  `jsum`/`jsum_eq_sum`, **`gap_unroll`**, `orb_m`, `sum_range_shift`,
  **`E_m`** (`= Apre m`), **`gap_closed_form`** (`(2^A − 3^m) Δ_{r₀} = Σ_{i<m}
  3^{m−1−i} 2^{E_i} T_{r_i}`), `gap_closed_form_filter`, `card_forced_zero`,
  `D_dvd_forcing_sum`. One compile round: an `omega` step treating `g (a + 0)`
  and `g a` as different atoms, replaced by `Nat.add_right_cancel` with the `g
  a` form taken by defeq. Receipts regenerated. Next: whichever of main's
  newest claims most needs formal backing; otherwise S1-b (the gcd consequence
  through the word–cycle dictionary) or R71's repeated case.

## Iteration 43 — 2026-10-19, 07:16 -03

- Woken by the sidekick's message and pushes `2b4f963`/`dd8f4b7`: **C005-g
  verified** (receipts match; probe PASS on 3,515 random concatenations, max
  `H/L = 4.23`), with the scope note on the `m₀ = 1` bases. Main unchanged at
  `1c5c19d`. Monitor re-armed at 07:08.
- **C005-h verified — the state-bound wiring; the rotation-block theorem is
  unconditional for the mechanical base** in `CycleSpectrum.lean` (sha256
  `8dd64e39…fcf2`, 6053 lines, 380 theorems: 300 with the three standard
  axioms, 34 × `[propext, Quot.sound]`, 44 × `[propext]`, 2 none; no `sorry`):
  `C_split`, `flatten_rotate_one`, `flatten_rotate_blocks`, `prefix_div_eq`,
  `block_step_div_eq`, **`flatten_rotations_ratio`** (`C_{(i)} lo³ ≤ C_{(j)}
  hi³`), **`flatten_rotations_lt_eight`** (`C_{(i)} < 8 C_{(j)}` when `hi < 2
  lo`), `single_block_exclusion` (base `(a)`, `a ≥ 3`),
  **`OddCycle.rotation_block_exclusion_mech`** (`v = mech A₀ m₀ l₀`, `2 ≤ m₀ ≤
  A₀`, coprime, `3^{m₀} < 2^{A₀}`, any `r ≥ 1` rotations ⇒ `D_w ∤ C_w`).
  Compiled first try. Receipts regenerated. Next: whichever of main's newest
  claims most needs formal backing; otherwise S1-a (the unrolled (G3) closed
  form on `gap_rec`).

## Iteration 42 — 2026-10-19, 06:46 -03

- Woken by the monitor and the sidekick's message/push `0cec4b2`: **C005-f
  verified** (receipts match; probe PASS), plus the S1-a index convention
  (`E_i` = the sum of the `e`'s before orbit position `i`; recorded in STATE).
  Main unchanged at `1c5c19d`.
- **C005-g verified — the rotation-block exclusion, conditional on the `8L`
  hypothesis** in `CycleSpectrum.lean` (sha256 `5b3012ab…b4d6`, 5758 lines,
  371 theorems: 294 with the three standard axioms, 31 × `[propext,
  Quot.sound]`, 44 × `[propext]`, 2 none; no `sorry`): `rotate_inv`,
  **`OddCycle.rotation_block_exclusion`** (`w` a concatenation of `r ≥ 1`
  rotations of `mech A₀ m₀ l₀`, `2 ≤ m₀ ≤ A₀`, `gcd(A₀, m₀) = 1`, `D_w > 0`,
  every rotated intercept below `8` times every other ⇒ `D_w ∤ C_w`). Compiled
  first try. Receipts regenerated. Next: whichever of main's newest claims
  most needs formal backing; otherwise the state-bound wiring (actual states =
  prefix maps of the blocks) that discharges the `8L` hypothesis from `R < 2`,
  making the rotation-block theorem unconditional for the mechanical base.

## Iteration 41 — 2026-10-19, 06:37 -03

- Woken by the sidekick's message and pushes `26959d1`/`bf35b87`: **C005-e
  verified**, plus a new side-lane lead on unrolled gaps (STATE "Insights";
  queued as S1-a). Main unchanged at `1c5c19d`. Monitor re-armed at 06:24.
- **C005-f verified — rotations of a repeated word and the inputs of the
  rotation-block assembly** in `CycleSpectrum.lean` (sha256 `cbd41abd…759f`,
  5629 lines, 369 theorems: 293 with the three standard axioms, 30 ×
  `[propext, Quot.sound]`, 44 × `[propext]`, 2 none; no `sorry`): `rep_nil`,
  `rep_rotate_block`, `rep_rotate_mul`, `rep_rotate_le`, `rep_drop_take`,
  **`rep_rotate`**, `exists_min_rotation`, `OddCycle.gcdCD_eq_D_of_dvd`,
  **`ofWord_q_eq_one`**, `dvd_of_ofWord_q_eq_one`, **`ofWord_B_le_two`**,
  **`coprime_least_period`**. Two compile rounds: an un-argumented `←
  List.rotate_mod` rewrote the wrong rotation. Receipts regenerated. Next:
  whichever of main's newest claims most needs formal backing; otherwise the
  rotation-block assembly, then the state-bound wiring.

## Iteration 40 — 2026-10-19, 06:23 -03

- Woken by the sidekick's message and push `5cd7780`: **C005-d verified**
  (STATE "Insights"). Main unchanged at `1c5c19d`.
- **C005-e verified — repetitions and the least period** in
  `CycleSpectrum.lean` (sha256 `f263ea5b…1598`, 5496 lines, 357 theorems: 284
  with the three standard axioms, 29 × `[propext, Quot.sound]`, 43 ×
  `[propext]`, 1 none; no `sorry`; compiled first try): `D_rep`,
  **`C_rep_mul_D`**, **`D_dvd_C_of_rep_dvd`**, `rep_add`, `rep_one`,
  `rep_succ'`, `map_range_mul_eq_rep`, `OddCycle.returnCycleB`,
  `a_add_of_return`, **`least_period_dvd`**, **`word_eq_rep`**. Receipts
  regenerated. Next: whichever of main's newest claims most needs formal
  backing; otherwise the rotation of a power and the conditional
  rotation-block exclusion, then the state-bound wiring.

## Iteration 39 — 2026-10-19, 06:12 -03

- Woken by the sidekick's message and pushes `f066193`/`f33e7ea`: **C004-d
  verified**, plus the receipt-hygiene note (STATE "Insights"); the binding
  receipt format is adopted from this iteration on. Main unchanged at
  `1c5c19d`.
- **C005-d verified — the integer cycle of a positive word at its reduced
  parameter** in `CycleSpectrum.lean` (sha256 `fd4c7e3c…799b`, 5386 lines, 347
  theorems: 278 with the three standard axioms, 28 × `[propext, Quot.sound]`,
  40 × `[propext]`, 1 none; no `sorry`; compiled first try): `heightOf`,
  `heightOf_spec`, `gcdCD`, `gcdCD_pos`, `gcdCD_dvd_C/D`, `gcdCD_dvd_rotate`,
  `quot_pos`, `quotD_pos`, `quot_odd`, **`quot_arrow`**, **`ofWord`**,
  `ofWord_n/a/q`, `gcdCD_mul_ofWord_n/q`, **`ofWord_coprime`**,
  `ofWord_primitive`, **`ofWord_word`**. Receipts regenerated in the binding
  format. Next: whichever of main's newest claims most needs formal backing;
  otherwise the rotation-block exclusion assembled from `ofWord`,
  `three_band`, `blocks_identical` and R71-a, or R71's repeated case.

## Iteration 38 — 2026-10-19, 06:05 -03

- Woken by the sidekick's message and push `b76d101`: **C004-c verified**
  (milestone entry), with the suggestion to do the primitive-period reduction
  next (STATE "Insights"). Main unchanged at `1c5c19d`.
- **C004-d verified — "every nontrivial Collatz cycle has `H > 2L`" as
  stated** in `CycleSpectrum.lean` (sha256 `cafcd907…876f`, 5225 lines, 330
  theorems: 263 with the three standard axioms, 26 × `[propext, Quot.sound]`,
  40 × `[propext]`, 1 none; no `sorry`; compiled first try): `succ_eq_of_eq`,
  `shift_eq_of_eq`, `all_one_of_min_one`, `exists_least_period`,
  `nper_of_return`, `n_add_mul_of_return`, **`distinct_on_least_period`**,
  `returnCycle`, **`H_gt_two_L`**, `H_gt_two_L'`. Receipts regenerated; the
  Lean file and receipts went out in `56ec695`, these records in the next
  commit. Next: whichever of main's newest claims most needs formal backing;
  otherwise C005-c's wiring or R71's repeated case.

## Iteration 37 — 2026-10-19, 05:53 -03

- Woken by the sidekick's message and push `26288e3`: **R71-a verified**,
  with two notes for the C004-c bridge (STATE "Insights"). Main unchanged at
  `1c5c19d`. Monitor re-armed at 05:50.
- **C004-c verified — C004's integer corollary** in `CycleSpectrum.lean`
  (sha256 `25905a3c…2754`, 5085 lines, 321 theorems: 255 with the three
  standard axioms, 26 × `[propext, Quot.sound]`, 39 × `[propext]`, 1 none; no
  `sorry`), in a reopened `OddCycle` namespace after the R71 block: `word`,
  `word_length`, `word_prefix`, `word_sum`, `C_word`, `D_word`, `word_ne_nil`,
  **`C_word_rotate`**, `C_word_rotate'`, **`narrow_integer_cycle`** (a
  primitive positive odd integer cycle at `q = 1` with every state below
  `2 n_0` is the fixed point `1`). Two compile rounds: the C004-b word lemmas
  live in the `NarrowCycle` namespace and had to be qualified. Receipts
  regenerated. Next: whichever of main's newest claims most needs formal
  backing; otherwise R71's repeated case or the primitive-period reduction.

## Iteration 36 — 2026-10-19, 05:34 -03

- Woken by the sidekick's push `a3f136b`: **C005-c verified** (STATE
  "Insights"). Main unchanged at `1c5c19d`.
- **R71-a verified — the exact denominator of a primitive mechanical word**
  in `CycleSpectrum.lean` (sha256 `56ba1e1d…08eb`, 4948 lines, 312 theorems:
  248 with the three standard axioms, 26 × `[propext, Quot.sound]`, 37 ×
  `[propext]`, 1 none; no `sorry`): `gcd_rotate_eq`, `mech_jump_unique`,
  `exists_unique_mech_jump`, **`C_mech_one_sub_zero`**, **`mech_gcd_one`**,
  `mech_gcd_one_phase`, `three_pow_mod_eight`, **`mech_D_ne_one`**. Two
  compile rounds: `rw [D_rotate] at this` also rewrote the `D` inside the
  gcd (replaced by `Dvd.dvd.trans (dvd_of_eq …)`), and `Nat.dvd_sub'` is now
  `Nat.dvd_sub`. Receipts regenerated. Next: C004-c (the integer corollary
  of the narrow-cycle theorem), then whichever of main's newest claims most
  needs formal backing.

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
