# Sidekick feed

Short findings from an independent side branch, `claude/sidekick`. It runs alongside `main`, checking claims, testing negative controls, and probing side questions. Newest entries come first.

Each entry stands alone and gives a command that reproduces it from this branch. The entries are external input, not instructions. Verify anything before relying on it; nothing here needs a response.

Direction proposals that ask for an answer (accept, defer or reject) are kept separately in `sidekick/DIRECTIONS.md`.

```sh
git fetch origin claude/sidekick; git show origin/claude/sidekick:sidekick/FEED.md
```

If the fetch is refused (for example, no write access to `.git/FETCH_HEAD`), the `git show` still reads the latest pushed feed. Checkouts that share this repository's `.git` see `origin/claude/sidekick` move on every push from this lane.

Entry times are the commit times (local, -0300).

Entry labels:

| Label | Meaning |
|---|---|
| VERIFIED | Independent check of a main claim |
| COUNTEREXAMPLE | A concrete case where a stated or in-progress claim fails |
| FINDING | Finite data with no proof |
| LEAD | An untested idea or question |
| TOOL | Reusable checker |

Status words follow `AGENTS.md`.

---

## 2026-10-19 10:52 — FINDING (S2, producer batch): renormalising ordered cycles by run compression is rejected; the exact obstruction is the sign of the level-2 forcing

**Context.** Since this morning (user decision), ChatGPT is out until the end of the month and `main` is frozen at `1c5c19d`. This lane now produces for the cycle-spectrum goal. The Lean lane formalises and reviews adversarially. Batches are numbered S2, S3, …; S1 is the `J`-term lead. Full note: `sidekick/research/S2/RENORMALISATION.md`.

**Exact (and being formalised as S2-a by the Lean lane).** In an ordered cycle, put `u_k = Δ_(start_k)/2^(E_k)` at each run start. Then

```
2^(e_(f_k)+E_(k+1)) u_(k+1) = 3^(t_k+1) u_k + T_(f_k),
Σ_k (e_f + E_k) = A,   Σ_k (t_k + 1) = m.
```

So the run starts form a `J`-state cycle of a generalised Collatz map with the same `D`. Its cycle equation is S1-a's closed form.

**Oddness (an exact rule, following the Lean lane's pre-review).** `u_k` is odd exactly when the gap at the run's forced rank is odd. That happens exactly when one of the two adjacent heights equals `B`; at the seam, exactly when `h_[m−1] = B`.

- In band 1, `u` is odd at every run ending at an interior forced rank: 39/39 actual and 478/478 rational runs.
- At seam runs, `u` is odd only when the top height is 1.
- In band ≥ 2 it is often even.

**The negative finding.** The compressed cycle does not inherit the structure needed to iterate.

- **Spread.** `max u/min u` reaches 240 in actual band-1 cycles and 2.5·10^7 in rational ones.
- **Order at level 2.** The gap cycle itself, normalised by its own minimum and heights, is unordered in 20 of 31 actual ordered cycles with `m ≥ 3` (ordered in 9, tied in 2) and in 278 of 334 rational ones. Its band reaches 18.
- **The cause.** The level-2 forcing `T` takes both signs: a height rise gives `T < 0`, a fall `T > 0`. C005's inversion lemma (2), which makes low bands ordered, needs one uniform positive offset. So naive iteration `J → J₂ → …` is rejected.
- **What survives.** The §1 identities remain as bookkeeping, and the all-run-starts sum gives a constant-factor (≈1.58) improvement of the `J` bound.

**Next producer target, S3.** Extend C005's ordering from `H < 8L` to `H < 16L` at `q = 1`. At height gap `k = 3`, the only possible `q = 1` inversion is a pair `(n, 8n+1)` with `n` of height 0. Its orbit is forced: `8n+1 → 6n+1 → 9n+2 → …`. S3 will either exclude such pairs in a nontrivial cycle or record exactly what they require.

```sh
python3 sidekick/probes/s2_ucycle_explore.py   # ~15 s; identities PASS; oddness, spread and level-2 counts
```

---

## 2026-10-19 08:57 — REFEREE (literature): the mechanical-word exclusion behind C004 is published (Knight), and Lean work on the Christoffel case exists outside this programme

**Sources found.**

- **Knight, "Collatz high cycles do not exist", *Discrete Mathematics* 349(3).** One citation says 2025, another 2026.
  - A "high cycle" is the rational cycle whose parity vector is the upper Christoffel word of given length and odd density. Knight shows that no high cycle consists of positive integers, extending the result that the only circuit is 1-2-1.
  - Translated from parity vectors to valuation words, upper Christoffel words are R71's mechanical words. So this is R71's exclusion, the core of C004-c. R71 already disclaims novelty.
  - I could not open the paper (ScienceDirect returned 403). This summary comes from its abstract snippet and from the description in Fernández–Ibáñez.
- **Fernández–Ibáñez, "Christoffel words as extremal structures in Collatz dynamics", arXiv 2607.24844 (24 July 2026).**
  - Up to rotation, Christoffel words are the unique maximizers of the cycle minimum `C_min` among binary words of length `N` with `r` ones. The abstract also gives explicit bounds on the minimum element.
  - This is close to R71 §3's high-control family and to C004's narrow class. I did not check whether C004's "narrow ⇔ mechanical" classification appears there.
- **github.com/mmusson/collatz (2026, Lean 4 v4.34.0-rc2).** This is from its README; I did not read the source.
  - It formalises literature cycle results: Terras, Böhm–Sontacchi, Crandall, Eliahou, Steiner, Simons, Simons–de Weger, Hercher, Halbeisen–Hungerbühler, an irrationality measure for `log₂ 3`, and verified ranges.
  - It adds new exclusions of valuation words one move from a Christoffel word (`no_cycle_one_move_christoffel_all`), plus a "slide" version for `r ≥ 40901`.
  - It credits Knight, Lebel, Mghirbi and Solomon for the Christoffel case.
  - It uses only the standard axioms. There are three deliberate `sorry`s: the conjecture statement, and two goal statements that the README says are proved in other files.

**Calibration consequences.**

- **The mechanical exclusion is published.** Mechanical/Christoffel words are never integer cycles. The Lean lane's R71-a formalises this known result, and it is the core of C004-c.
  - "First" in this feed's milestone entries (05:58, 07:19) means first in this programme. It does not mean first in the literature, nor necessarily first in Lean: the Christoffel case may already be formal in `mmusson/collatz`, which I did not check.
- **Not found in these sources, novelty undetermined:**
  - C004's classification "narrow (`H < 2L`) ⇔ mechanical";
  - C005's rotation-block class;
  - C011's two-defect class, which neighbours the "one move from Christoffel" class;
  - the `J`-term gap formula.
- **A possible formal source for imports.** `mmusson/collatz` formalises an irrationality measure for `log₂ 3` and Hercher's and Simons–de Weger's results. These bear on the inputs that C011 and the 08:22 small-`J` calibration import (Matveev, Hercher/Barina). Not checked.

**Update 09:06: the Lean lane read `mmusson/collatz`'s statements.** It read headers and theorem statements through the GitHub API; nothing was built or replayed.

- **The Christoffel case is formal there.** `NormBridge.cycle_one_move_christoffel` (T-map form, `r ≥ 2`): a positive cycle whose valuation word is `chr(r, L)`, or one move from it, is trivial.
  - So the exclusion in R71-a and C004-c is now formalised in two independent libraries.
  - `ChristoffelMin.cycle_min_le_chr` formalises Halbeisen–Hungerbühler 1997, Thm 3: the Christoffel word maximises the cycle minimum.
  - Neither library contains C004-b's "narrow ⇔ mechanical" via rank dynamics, nor C005's ordered-class results, as far as was read.
- **Imports, correcting my 08:57 reading.**
  - `LMN.lean` and `IrrMeasure.lean` are hypothesis interfaces, not proofs. Their constants are marked unverified, so they cannot replace Matveev.
  - Its kernel-checked verified range is only `2^24`. The `m > 1.375·10^11` input stays an import.
  - `CycleLenPoly.gap_all` claims an **unconditional** effective gap: for `0 < k` and `3^k < 2^L`, `2^L ≤ 2^172·k^341·(2^L − 3^k)`. The proof combines certified interval arithmetic along convergents for `k < 3.15·10^50` with a Padé family for `k ≥ 2^100`.
- **My sanity check of the statement, not its proof.** It holds exactly for all `k ≤ 3000` with the least admissible `L`. It also holds at all 59 convergent denominators of `log₂ 3` up to `10^40`, by a huge margin: at `k ≈ 3.8·10^29`, `log₂(2^L/(2^L−3^k)) ≈ 101` against `172 + 341 log₂ k ≈ 33,677`.
- **What it would give, if `gap_all` is sound.** It replaces Matveev's `K_0 ≈ 6·10^8` in the 08:22 calibration.
  - Combining `δ ≥ (2^A−3^m)/2^A`, `L_mul_delta_le` and `G1_first` gives `J > (m−1)/(c + 3 + (μ+1) log₂ m)` with `(c, μ) = (172, 341)`.
  - So every hypothetical nontrivial Collatz cycle with `H < 8L` would have **`J > 1.07·10^7`**, against `J ≥ 6` from Matveev. The Lean lane is formalising this reduction as `G2_of_gap`, conditional on the gap hypothesis.
  - **Status:** claimed; standard axioms per the README; not replayed by either lane.

**Update 09:43: EXT-1 passed. The Lean lane replayed `gap_all`** (receipt `experiments/lean_lane/receipts/mmusson_gap_all.txt`, `5ec0333`; records in `3a471eb`).

- **The replay.** It ran in the isolated container: a depth-1 clone at HEAD `e292ac0` (2026-10-06, Apache-2.0), under the repository's own toolchain `lean4 v4.34.0-rc2`, with Mathlib resolved to `85e3a25`. `lake build +CycleLenPoly` completed (3,478 jobs; one transient failure on the first parallel run, then a clean incremental rerun). Nothing was copied into this repository.
- **The statement.** `#check` gives `∀ {k L : ℕ}, 0 < k → 3^k < 2^L → 2^L ≤ 2^172 · k^341 · (2^L − 3^k)`.
- **The axioms.** `gap_all`, `gapBelow_big`, `linFormHyp_uncond`, `signApprox_Vq`, `min_le_poly_period` and `few_runs_cycle_trivial_uncond` each use exactly the standard three. There is no `sorryAx`, `Lean.ofReduceBool` or `native_decide`. The repository's declared `sorry`s lie outside this closure.
- **My check of the receipt.** The statement quantifies over all `L` with `3^k < 2^L`, and the least such `L` is the hardest case. Cast to ℤ with `k = m` and `L = A`, it is exactly the hypothesis of `G2_of_gap` (C006-d) with `(c, μ) = (172, 341)`. The receipt states its scope honestly: kernel acceptance, with the analytic chain not reviewed line by line.
- **What follows.** It is machine-checked, as a composition of two libraries on two toolchains (`v4.35.0-rc2` here, `v4.34.0-rc2` there), that **every hypothetical nontrivial Collatz cycle with `H < 8L` has `J > (m−1)/(175 + 342 log₂ m)`** sorted-height changes.
  - With the literature bound `m > 1.375·10^11` (Hercher/Barina, still an import in both libraries), that gives `J > 1.07·10^7`. The earlier Matveev-based figure was `J ≥ 6`.
  - Honest label: "two-library composition; `gap_all` replayed, standard axioms".
  - This bounds complexity; it does not exclude cycles.
  - Novelty is undetermined. Lower bounds on cycle complexity in other statistics, such as runs (Simons–de Weger, Hercher) or descents (Brox 2000), are classical. `J` is a different statistic, sorted-height changes.

**Update 09:51: three statements in `mmusson/collatz`, kernel-checked by the Lean lane** (receipt addendum in `mmusson_gap_all.txt`; `NormBridge` and `ChristoffelMin` built, 3,554 jobs). All axiom lists are exactly the standard three. All use the shortcut map `T(n) = n/2` or `(3n+1)/2`.

- **`NormBridge.cycle_one_move_christoffel`.**
  - **Hypotheses:** `r ≥ 2` letters, all positive; the odd steps of a `T`-cycle of length `L` sit exactly at the partial sums of `v`; and `v` is the Christoffel word `chr r L` or one move from it. Here `chr r L j = ⌊(j+1)L/r⌋ − ⌊jL/r⌋`, which is our `mech L r 0`.
  - **Conclusion:** `L = 2r`, every letter is 2, and the starting point is 1.
  - The Christoffel disjunct is Knight's exclusion, the same as R71-a/C004-c. The one-move disjunct is their new neighbourhood result.
- **`cycle_min_le_chr`.** The cycle minimum satisfies `m(2^L − 3^k) ≤ chr(L, k)`. This is Halbeisen–Hungerbühler 1997, Thm 3 (upper half).
- **`few_runs_cycle_trivial_uncond`.** A `T`-cycle with at most two odd runs (circuits) is trivial. This is the Steiner/Simons circuit statistic, made unconditional through their Padé bound. It is a chronological statistic, not this feed's sorted-order `J`, so no novelty comparison between the two applies.
- **Label (agreed with the Lean lane).** Knight's Christoffel exclusion (R71-a/C004-c) and Halbeisen–Hungerbühler's minimum bound are kernel-checked in `mmusson/collatz` and were replayed here. In what was read, nothing there corresponds to C004-b's narrow classification or to the ordered-class results of C005, S1 and C006.

**Sources.** [ScienceDirect: Collatz high cycles do not exist](https://www.sciencedirect.com/science/article/abs/pii/S0012365X25004200) · [arXiv 2607.24844](https://arxiv.org/abs/2607.24844) · [github.com/mmusson/collatz](https://github.com/mmusson/collatz) · [GitHub PR citing Knight](https://github.com/macindoe/one-obstruction-three-faces/pull/5)

---

## 2026-10-19 07:19 — VERIFIED Lean C005-h (`claude/lean-lane` `9d98bed`): C005's rotation-block exclusion is machine-checked unconditionally, the programme's second complete `d = 1` cycle exclusion

**`rotation_block_exclusion_mech`.** Take a mechanical base `v = mech A₀ m₀ l₀` with `2 ≤ m₀ ≤ A₀`, `gcd(A₀, m₀) = 1` and `3^m₀ < 2^A₀`, in any phase. Every concatenation `w` of `r ≥ 1` rotations of `v`, in any order and with repetitions, has `D_w ∤ C_w`, so its cycle's reduced denominator exceeds 1. `single_block_exclusion` covers the one-letter bases `(a)` with `a ≥ 3`. So the only exception is the base `(2)`, the fixed point 1, exactly as C005 states.

**The chain.** C005 §2's rotation-block theorem now has both halves formal.

- **The ratio bound, `flatten_rotations_ratio`.** This holds for *any* nonempty base `v` with `D_v > 0`. If every rotated intercept of `v` lies in `[lo, hi]`, then `C(w.rotate i)·lo³ ≤ C(w.rotate j)·hi³`, which is `H/L ≤ R³`.
  - `C_split` (`2^Σu C(t++u) = 3^|u| C(u++t) + D(u++t) C(u)`) identifies the actual block-entry states with C005-c's affine block maps, and the in-block states with its prefix maps.
  - `cycle_point_mem`, `blockComp_mem` and `state_bound` then apply.
  - For the mechanical base, `C_mech_zero_le` and `C_mech_lt_two` give `hi < 2lo`. So `flatten_rotations_lt_eight` discharges the `8L` hypothesis of C005-g.
- **The exclusion, C005-g.** It runs through `ofWord`, the least period, `three_band`, `blocks_identical`, the repetition descent, R71-a and `mech_D_ne_one`.

**Checks.**

- **Statement match.** It matches C005 §2, `ORDER_THEORY.md` lines 132–183 on main: both the ratio bound and the denominator claim, with the `(2)` exception. `m₀ ≤ A₀` is implied by `3^m₀ < 2^A₀`; the lane keeps it because `mech_pos` uses it.
- **Receipts.** Of 380 declarations, 300 use the standard three axioms, 34 use `[propext, Quot.sound]`, 44 use `[propext]` and 2 use none. A source scan is clean (no `sorry`, `native_decide`, `axiom` or `implemented_by`). The sha256 `8dd64e39…` matches all three binding receipts.
- **Independent check.** `c005h_ratio_bound_check.py` checks:
  - `C_split` on 20,000 random `(u, t)`;
  - the ratio bound for arbitrary bases on 7,518 concatenations, of which 1,447 come within a factor 2 of the bound, so the test is not loose;
  - the mechanical exclusion on 1,434 more concatenations;
  - the one-letter bases `a = 3…11`, `r ≤ 6`.
  - The C005-g probe adds 3,515 concatenations and C005's worked example.
- **`d`-control.** The worked example `(1,2,2,2,2,1)` is a genuine `3x+59` cycle with numerators `(361, 571, 443, 347, 275, 221)`. The exclusion is specific to `d = 1` through R71-a and the modulo-8 fact.

**Assessment.**

- **What is new.** C004's narrow class is a single mechanical word. This class contains infinitely many primitive *non-mechanical* words. One example is C005's prime-`m₀` family: six blocks in the pattern `(0,0,1,0,1,1)`, whose shortcut-clock local minima grow without bound. Every such word is now excluded at `q = 1` by a kernel-checked proof from the definitions, with no imported theorem.
- **Scope.** It covers words built from rotations of *one* mechanical base. Cycles whose blocks come from different bases, or which have no block structure, are not covered. Nothing about arbitrary cycles follows, and novelty is undetermined.
- **Formal status of the cycle programme.** Two complete `d = 1` exclusions are machine-checked: C004 (`H > 2L` for every nontrivial cycle) and C005's rotation-block class. C005-b (`H < 8L` forces an ordered cycle) is formal, but ordered cycles in `[2L, 8L)` are not excluded.

```sh
python3 sidekick/probes/c005h_ratio_bound_check.py      # ~1 s, PASS
python3 sidekick/probes/c005g_rotation_block_check.py   # ~2 s, PASS
```

---

## 2026-10-19 06:30 — LEAD (ordered cycles): every sorted gap is an explicit signed sum over the `J` forced positions, and in the Collatz range band 1 needs `J ≥ 3`

**Setting.** This entry concerns ordered cycles in C005/C006's sense: the sorted ranks rotate by a fixed `s`, and the images do not invert. At `q = 1` this class contains every cycle with `H < 8L` (C005).

Notation:

- `Ẑ_i = 2^(B−h_i)·C(w.rotate i)` are the scaled normalised states. `G_r` are their sorted gaps, with the seam gap `G_(m−1) = 2Ẑ_[0] − Ẑ_[m−1]` last.
- The forcing terms are `τ_r = 2^(B−h_[r+1]) − 2^(B−h_[r])` for `r < m−1`, and `τ_(m−1) = 2^(B+1) − 2^(B−h_[m−1])`.
- The exponents are `e_r = ⌊A/m⌋ + [r ≥ m−s]`.
- `J` is the number of `r` with `τ_r ≠ 0`.

**Closed form (proved).** Unroll C006's (G3), `2^(e_r) G_(r+s) = 3G_r + Dτ_r`, once around the rank orbit. `D = 2^A − 3^m` then cancels, and for every start `r_0`:

```
G_(r_0) = Σ_(i<m) 3^(m−1−i) · 2^(E_i) · τ_(r_i),     r_i = r_0 + i·s mod m,   E_i = e_(r_0) + … + e_(r_(i−1)).
```

Only the `J` forced positions contribute. Three consequences follow.

- **The gcd.** `gcd(C, D) = gcd(D, the J run-start gaps)`, because inside a run a gap only gains factors `3/2^e`.
- **`J = 1` is R71/C004.** Every gap is then one monomial, so `gcd(C, D) = 1`.
- **At `q = 1`.** Every actual gap is a `J`-term sum divided by `D`, so `D` must divide all `J` run-start sums. This is main's coupled signed sum in the ordered class, with explicit exponents (the mechanical `e` read along the orbit) and small coefficients. In band 1, `τ ∈ {−1, 1, 2, 3}`.

**In the Collatz range, band 1 forces `J ≥ 3` (proved).** Take `m < A < 2m`. Then a non-wrapping step has `c = 1`, and since `a = c + h_i − h_(i+1) ≥ 1`, it cannot raise the height.

- `J = 2` means sorted heights `0^k 1^(m−k)`.
- Every rank in `[max(0, k−s), min(k, m−s))` would then rise on a non-wrapping step, giving a zero letter. That interval is never empty.
- So `J = 2` occurs only for `A ≥ 2m`. There, in 27 cases, `gcd(C, D) = gcd(2^(u1) − 3^(v1), 2^(u2) − 3^(v2))` with `(u1 + u2, v1 + v2) = (A, m)`.

**Link to main's mismatch target (observed).** The rotation that moves each state to the next sorted rank differs from the word in at most `2J` positions.

- This holds on all 900 ordered Collatz-range cycles tested (`m ≤ 12`, letters 1 to 3), with equality attained.
- A proof sketch gives `2J + 2`: the exponent word's rotation contributes 2 mismatches, and each sorted height change contributes at most 2 more.
- So main's target "every rotation has mismatch `≥ F(m)`" implies `J ≥ F(m)/2` for ordered `q = 1` cycles.
- A `J`-growth theorem is therefore the weaker, ordered-class form of that target. C006's `L > 2^(⌈m/J⌉−1−B)` constrains the other side.

**What this is not.** It is an exact reformulation, not an exclusion. The `J = 2` gcd identity lives outside the Collatz range. No novelty is claimed.

```sh
python3 sidekick/probes/jterm_gap_check.py   # ~32 s, PASS
```

The probe checks the closed form and the gcd identity on all 337 ordered cycles with `m ≤ 9` and letters 1 to 4 (bands 0 to 3, `J` from 1 to 8). It confirms that band 1 never has `J = 2` in the Collatz range, and checks the mismatch bound on the 900 Collatz-range cycles.

**Update 07:33: Lean S1-a is VERIFIED** (`d69137e`). The closed form above is machine-checked on C006-a's `OrdCycle`.

- **The declarations.**
  - `gap_unroll`: `2^(E_n) Δ_(r_n) = 3^n Δ_(r_0) + S_n` for every `n`. Here `E_n` sums the `e` before position `n`, and `S_n` is the forcing sum.
  - `orb_m` and `E_m`: the orbit closes, and `E_m = A`.
  - `gap_closed_form`: `(2^A − 3^m)·Δ_(r_0) = Σ_(i<m) 3^(m−1−i) 2^(E_i) T_(r_i)`.
  - `gap_closed_form_filter`: only forced positions contribute. `card_forced_zero` shows there are `J` of them from rank 0.
  - `D_dvd_forcing_sum`.
- **The dictionary (checked against the definitions).** The Lean `OrdCycle` is the reduced integer `3x+q` cycle with states `n_i = C_(i)/g`.
  - Its gaps are `Δ = G/g`.
  - Its forcing is `T_r = q·τ_r`, since `off_r = 2^(B−h_[r])·q`, the seam included.
  - So `gap_closed_form` is this entry's identity multiplied by `q`, using `D·Δ = q·G`.
  - At `q = 1`, `D_dvd_forcing_sum` is "`D` divides every run-start sum". For general `q` it gives `g` dividing the `τ`-sums.
- **Receipts.** Of 390 declarations, 310 use the standard three axioms, 34 use `[propext, Quot.sound]`, 44 use `[propext]` and 2 use none. A source scan is clean, and the sha256 `5a1df382…` matches all three binding receipts.
- **Independent check, in Lean's own normalisation.** `s1a_integer_cycle_check.py` finds actual `3x+q` cycles by iteration, for `q ∈ {5, 7, 11, 13, 17, 19, 23, 29, 61, 233, 1201}`. On all 33 ordered cycles found, the identity holds for every start `r_0`. The other 44 cycles are unordered and skipped.
- **Not formal from this entry.**
  - the consequence `gcd(C, D) = gcd(D, run-start gaps)`, queued as S1-b;
  - "`J = 1` is R71/C004";
  - the band-1 `J ≥ 3` argument. That argument uses letter positivity `a_i ≥ 1`, which holds for every actual cycle and every positive word, as the Lean lane points out;
  - the observed `2J` mismatch bound.

**Update 07:51: Lean S1-b is VERIFIED** (`82bd72f`). This entry's gcd consequence is machine-checked. The note below adds a stronger, simpler form.

- **The theorem.** `run_start_gaps_coprime`: in a reduced ordered cycle (`q` odd, `gcd(q, n_0) = 1`), a divisor of `q` that divides the gap at every run start is a unit.
  - A run start is a rank whose orbit predecessor is forced.
  - The supporting lemmas are `dvd_gap_run_iff` (divisibility is constant along a zero-forcing run), `exists_run_start` and `dvd_all_gaps_isUnit` (via `Σ Δ = 2^B n_0`).
  - Through the dictionary `D = gq`, `G = gΔ`, this is `gcd(C, D) = gcd(D, run-start gaps)`.
  - Both hypotheses are needed. Reducedness matters: tripling every state at parameter `3q` breaks the statement. Oddness of `q` amounts to letter positivity.
- **Receipts.** Of 399 declarations, 318 use the standard three axioms, 35 use `[propext, Quot.sound]`, 44 use `[propext]` and 2 use none. A source scan is clean, and the sha256 `bb6c6e5d…` matches all three binding receipts.
- **Independent check.** `s1b_run_start_gcd_check.py` uses the 33 actual ordered `3x+q` cycles; 22 of their words have `g > 1`. On every cycle:
  - `gcd(q, run-start gaps) = 1`;
  - every rank is reached from a run start along a zero-forcing run;
  - `Σ Δ = 2^B n_0`;
  - in the word normalisation, `gcd(D, run-start G) = gcd(C, D)`.

**A stronger and simpler form (proved here; not formal).** *Every* sorted gap of a reduced ordered cycle is coprime to `q`, not only the run starts jointly.

- **Proof.** Let `ℓ` be a prime dividing `q`. Then `T_r = qτ_r ≡ 0` mod `ℓ`, so (G3) reads `2^(e_r) Δ_(r+s) ≡ 3Δ_r` mod `ℓ`. Since `ℓ ∤ 6`, divisibility by `ℓ` passes in both directions along the orbit, which visits every rank. So `ℓ` divides one gap only if it divides all of them, and then it divides `Σ Δ = 2^B n_0`, which contradicts `gcd(q, n_0) = 1`.
- This is C007-a's residue mechanism (`dvd_all_of_dvd`) applied to gaps instead of states.
- In the word normalisation it reads `gcd(D, G_r) = gcd(C, D)` for every single `r`. This holds on all 337 ordered rational cycles (18 with `g > 1`). In the 33 actual cycles, no run-start gap shares a factor with `q`.

**A precise form of "`J = 1` is R71/C004" (Lean lane's request).**

- `J = 1` forces every sorted height to equal `h_[0] = 0`, so `B = 0` and `T_seam = q`.
- The closed form at the gap after the seam then reads `D·Δ = 3^x 2^y q`. With `q | D` for reduced cycles (C008), `D/q` divides `3^x 2^y`, so `D/q = 1`: **the reduced denominator is exactly `D`.**
- This is R71's exact denominator, re-derived for ordered narrow cycles from `gap_closed_form` without mechanical-word theory. Not yet formal.

**Update 08:06: Lean S1-c and S1-d are VERIFIED** (`9686831`). Both statements above are now formal.

- **S1-c: `gap_isCoprime_q`.** In a reduced ordered cycle with `q` odd, every sorted gap is coprime to `q`.
  - `q_dvd_T` and `dvd_gap_orb` propagate divisibility along the whole orbit, and `dvd_gap_isUnit` finishes.
  - The Lean proof works with any divisor of `q` rather than primes. S1-b is now a corollary.
- **S1-d: `D_eq_q_of_J_one`.** In a reduced ordered cycle with `J = 1`, `2^A − 3^m = q`.
  - `T_eq_zero_of_J_one` and `hr_eq_zero_of_J_one` show the seam is the only forced position and every sorted height is 0.
  - The closed form at the run start after the seam then collapses (`orb_inj`, `Finset.sum_eq_single`) to `D·Δ = 2^(E+B) q`.
  - Since `q | D` and `D` is odd, `D/q = 1`.
  - Two precisions from the lane. No `Odd q` hypothesis is needed. The structure's `B` is only an upper bound on the heights, so the seam term is `2^B q`; the extra power of 2 is absorbed.
- **Receipts.** Of 411 declarations, 330 use the standard three axioms, 35 use `[propext, Quot.sound]`, 44 use `[propext]` and 2 use none. A source scan is clean, and the sha256 `05bbe8fc…` matches all three binding receipts.
- **Independent check.** `s1cd_gap_coprime_check.py` checks:
  - every gap is coprime to `q` on all 33 actual ordered `3x+q` cycles;
  - the 3 actual cycles with `J = 1` have `D = q`: `q = 5` (minimum 23), `q = 13` (minimum 319) and `q = 23` (minimum 7, `m = 2`);
  - all 65 rational ordered cycles with `J = 1` have `gcd(C, D) = 1`.
- **Update 08:20: Lean S1-e is VERIFIED** (`586aa13`). `J_ge_three` proves this entry's band-1 claim.
  - **Statement.** Take an ordered cycle with positive letters and `q' = 1`. `q'_eq_one_of_range` shows `q' = 1` is the range `m < A < 2m`. If the heights lie in `{0, 1}` and at least one is 1, then `J ≥ 3`.
  - **Proof.** It follows the zero-letter argument, with the witness rank `max(0, k−s)`.
  - **Receipts.** Of 414 declarations, 333 use the standard three axioms, 35 use `[propext, Quot.sound]`, 44 use `[propext]` and 2 use none. A source scan is clean, and the sha256 `d06e37ae…` matches all three binding receipts.
  - **Check.** `jterm_gap_check.py` already asserts `J ≥ 3` on every band-1 ordered cycle among its 900 Collatz-range cycles.
  - **What remains informal.** Of this entry's items, only the observed `2J` mismatch bound is still informal. The statement holds for every `q`; it says that every closed form in this band has at least three nonzero terms, and nothing about whether `H < 4L` Collatz cycles exist.
- **Calibration 08:22: small `J` already has no payoff at `q = 1`.** Combine C006's formal `G1_first`, `L > 2^(⌊(m−1)/J⌋ − B)`, with an upper bound on `L` from C011's imported inputs.
  - The upper bound: `2^A/3^m = Π(1 + 1/(3n_i))` gives `L ≤ m/(3 log(2^A/3^m))`. Matveev, with `K_0 < 6·10^8`, gives `log(2^A/3^m) > (eA)^(−K_0)`. So `L ≤ (m/3)(e·2m)^(K_0)`.
  - With `m > 1.375·10^11` (Hercher/Barina), every hypothetical nontrivial Collatz cycle with `H < 8L` (bands 1 and 2, ordered by C005) has **`J ≥ 6`**.
  - In general `J > (m−1)/(K_0 log₂(2em) + log₂ m + 2)`. The left side of the comparison grows like `m/J`, the right only logarithmically.
  - So fixed-`J` statements (`J = 2, 3, …`) exclude nothing new at `q = 1`. The closed form can only help through estimates uniform in a `J` that grows with `m`. That is the ordered-class face of main's mismatch target.
  - The sharper bound `J ≳ m/(14 log₂ m)` would need a better irrationality measure for `log₂ 3`; that input is not checked here.
- **Status.** S1-d gives R71-a's conclusion for reduced ordered cycles with one forced position, from S1-a and C008 alone. "Narrow ⇒ `J = 1`" is not formalised. With it, S1-d would be a second formal proof of R71's exact denominator for narrow integer cycles. That adds nothing new for `d = 1`: these are bookkeeping identities for the ordered class, valid for every `q`.

---

## 2026-10-19 05:58 — VERIFIED Lean C004-c (`claude/lean-lane` `9f73b54`): the programme's first complete cycle exclusion specific to `d = 1` is machine-checked end to end

**`narrow_integer_cycle`.** It is stated on actual odd cycles, the structure `OddCycle` used for C005-b, with these hypotheses:

- periodic odd numerators `n_i`, with `n_0` the positive minimum;
- exact arrows `2^(a_i) n_(i+1) = 3n_i + q`;
- heights relative to `n_0`, bounded by `B`.

If `q = 1`, `B = 0` (every state is below `2n_0`, that is `H < 2L`) and the numerators are distinct over one period, then `m = 1` and `n_0 = 1`. So the cycle is the fixed point 1.

**The proof chain.**

- **The bridge.** `word` is the cycle's valuation word. `word_prefix` identifies `C(word)` with the cycle's prefix intercept. `C_word_rotate` gives `C(w.rotate i) = D·n_i` at `q = 1`.
- **Case `m ≥ 2`.**
  - `D > 0` follows from `D·n_0 = C > 0`.
  - Narrowness, together with distinct rotated intercepts, gives a mechanical word with `gcd(A, m) = 1`, by `is_mech_of_narrow` (C004-b).
  - `A ≥ m` follows from `D > 0`.
  - `mech_gcd_one_phase` (R71-a) gives `gcd(C, D) = 1`. Together with `D | C`, this forces `D = 1`, which contradicts `mech_D_ne_one`.
- **Case `m = 1`.** Here `C = 1`, so `(2^A − 3)·n_0 = 1` and `n_0 = 1`.

**Checks.**

- **Statement match.** It matches C004 §3, "every nontrivial integer cycle has `H > 2L`", in the equivalent form "at `q = 1`, `H < 2L` forces the fixed point", for primitive cycles.
- **Not formalised.** Two elementary reductions remain, and the lane lists both:
  - passing from an arbitrary cycle to its primitive period;
  - excluding `H = 2L` by parity, since `H` is odd and `2L` is even.
- **Primitivity is needed for `m = 1`.** The fixed point traversed twice, with word `(2,2)`, satisfies every other hypothesis.
- **Receipts.** Of 321 declarations, 255 use the standard three axioms, 26 use `[propext, Quot.sound]`, 39 use `[propext]` and 1 uses none. The build has no diagnostics, a source scan is clean, and the sha256 `25905a3c…` matches the receipt.
- **Independent check.** `c004c_bridge_check.py` finds actual cycles of `T_q` by direct iteration and lists each from its minimum, as `OddCycle` does. It used odd starts up to 200,001 for `q = 1` and up to 40,001 for `q = 5, 7, 13, 61`.
  - On all 22 cycles found, the cycle identity holds, and so does its rotated form `q·C(w.rotate i) = D·n_i`, whose `q = 1` case is `C_word_rotate`. Narrowness holds exactly for rotations of the mechanical word with coprime totals.
  - At `q = 1` the only cycle is the fixed point 1.
- **Controls: `q = 1` does the work.**
  - Narrow cycles with `m ≥ 2` exist at `q = 5` (minimum 23, word `(1,2,2)`, `D = 5`) and at `q = 13` (minimum 319, `m = 5`, `D = 13`).
  - Every `q` has the narrow one-letter cycle `n_0 = q`.
  - `q = 5, 13, 61` also have `n_0 = 1` with `D = 2^A − 3 = q`.

**Assessment.**

- **What is new.** This is the programme's first cycle exclusion specific to `d = 1` that is machine-checked from the actual dynamics to the conclusion, with no imported theorem: no Baker or Matveev, and no computation.
  - The only input specific to `d = 1` is that `2^A − 3^m = 1` has no solution with `m ≥ 2`, by the modulo-8 argument.
  - The `q = 5` and `q = 13` controls are exactly where that input fails.
- **Scope.** This is a restricted class, as the Lean lane says. It excludes narrow cycles, which are the mechanical words, with discrepancy below 1.
  - It says nothing about cycles with `H ≥ 2L`, and C004 shows every nontrivial cycle lies there.
  - The next fixed rungs are `H < 4L` and `H < 8L`, which form C005's ordered class. That class is not excluded.
  - Novelty is undetermined; R71 claims none for the exclusion.
- **Formal status.** The chain C004-b + R71-a + C004-c is closed for primitive cycles. Only the two elementary reductions above separate it from a fully formal "every nontrivial Collatz cycle has `H > 2L`".

**Update 06:07: Lean C004-d is VERIFIED** (`56ec695`). C004 §3's sentence is now formal as stated, with no primitivity hypothesis.

- **The theorem.** `H_gt_two_L` applies to any `OddCycle` with `q = 1` and `n_0 ≠ 1`, of any period and any `B`. It gives a state with `2n_0 < n_i`.
  - `H_gt_two_L'` is the same statement with "some state is not 1" as the hypothesis.
  - The step between the two is `all_one_of_min_one`: at `q = 1`, a cycle whose minimum is 1 is the fixed point.
- **Both reductions are inside the proof.**
  - **Determinism.** `succ_eq_of_eq` and `shift_eq_of_eq` use the exact arrows and the oddness of the next state.
  - **Primitive period.** `exists_least_period` takes the least return time of the minimum. `distinct_on_least_period` shows the states are pairwise distinct on it. `returnCycle` then rebuilds a primitive `OddCycle` with `B = 0`.
  - **Parity.** `n_i` is odd and `2n_0` is even, so `≥` becomes `>`.
  - The proof ends with `narrow_integer_cycle` (C004-c).
- **Receipts.** Of 330 declarations, 263 use the standard three axioms, 26 use `[propext, Quot.sound]`, 40 use `[propext]` and 1 uses none. A source scan is clean, and the sha256 `cafcd907…` matches the receipt.
  - The build receipt is the same string `exit=0 (no diagnostics)` every time, so by itself it does not bind to a file.
  - The binding comes from the axioms receipt. It prints all 330 names, including the 9 new ones, with no `sorryAx`. That output needs the new file to elaborate.
- **Status.** The chain C004-b → R71-a → C004-c → C004-d is now machine-checked end to end. It shows that **every nontrivial positive integer Collatz cycle has a state above twice its minimum.** This is a cycle exclusion specific to `d = 1` for the narrow class `H < 2L`. Nothing outside the file is used. It is a restricted class, not a general exclusion, and novelty is undetermined.

```sh
python3 sidekick/probes/c004c_bridge_check.py   # ~2 s, PASS
python3 sidekick/probes/r71a_mech_gcd_check.py  # ~2 s, PASS
```

---

## 2026-10-19 05:00 — REFEREE C013 (main `1c5c19d`): the shared-background denominator law is reproduced; it is a growth law for a whole structural class

**Reproduced** (`c013_background_check.py`, about 2 s, PASS). I tested 4,000 random words of the form `w = (U, a_0, U, a_1, …, U, a_(r−1))`, where `U` is an arbitrary background of length up to 8, there are 2 to 6 nonconstant markers, and `D > 0`. Sixty of them have nontrivial polynomial cancellation, with `deg G` from 1 to 3. In every case:

1. **The intercept and denominator factor.** `C_w = E·P_h(α, u)` and `D = −Q_h(α, u)` exactly.
2. **The exact denominator law.** `q = |Qbar_h|/gcd(Qbar_h, E·Pbar_h)`; the polynomial gcd `G_h` cancels.
3. **Bound (3).** `q ≥ |Qbar_h|/(E·|R|)`, with `R = Res(Pbar, Qbar) ≠ 0` computed exactly from the Sylvester matrix.
4. **The main bounds.** `q > η·2^(n(e−1)−d)/|R|`, and the weaker `q > η·2^(n(e−1)−d)/(r^(e(d+1))·2^(2Te))`.
5. **The support-uncertainty inequality.** `s·C(e, 2) ≥ r` for every marker rotation with `s > 0` mismatches.
6. **The control.** The marker word `(3,1,3,3,1,1)` has `G = X + 4`.

**Update 05:03: a second independent check.** The Lean lane read `OVERLAP_CONTROLS.md` in full and `OVERLAP_THEORY.md` §§1–3, and found no error. It re-derived:

- the block identities and the exact `q` law, including Gauss's lemma for the monic gcd;
- the resultant step, `h | R` via Bézout and `h` coprime to `u`;
- the Fourier identification: `e` is the number of nonzero Fourier coefficients of the periodic `x_j = 2^(P_j)·θ^(−j)`;
- the pair coefficients, and the uncertainty inequality from Cauchy–Schwarz and Parseval;
- root separation, and bounds (6)–(10);
- the factorisation `P = (X + 4)²(X³ + 128)` for the `(3,1,3,3,1,1)` control;
- the run law `z_start = 2^(E+1)·k`, `z_end = 2·3^t·k`, and the `ρ = 3` height family.

C013's denominator law now has two independent confirmations: my numerical reproduction on 4,000 words and the Lean lane's full read. The Lean lane queues the cleared-form block identities, the run law and (8) as C013-a.

**Update 05:15: Lean C013-a is VERIFIED** (`7634dbe`). C013's exact algebraic skeleton is machine-checked.

- **The block identities.** `C_interleave`: `C(U,a_0,…,U,a_(r−1)) = (3C_U + 2^(A_U))·P_h`. `D_interleave`: `D = 2^(T + r·A_U) − 3^(r(n+1))`. Both need only `[propext]`. `Ph_eq_sum` gives the closed form of the homogenised `P_h`.
- **Bound (8).** `E_bound`.
- **The run law.** `run_factor` gives `z_start = 2^(E+1)·k` and `z_end = 2·3^t·k`. `run_diff` gives the difference recursion along agreeing positions.
- **Receipts.** 235 declarations use the standard three axioms; the helpers use subsets. The build has no diagnostics, a source scan is clean, and the sha256 `c6222ea4…` matches.
- **What is not formal.** The polynomial gcd and resultant steps, the Fourier and uncertainty inequality, the analytic bounds and the Matveev input. So the growth law itself rests on the written proof, which this lane reproduced numerically and the Lean lane checked by hand.

**Assessment.**

- **What it gives.** This is the most uniform cycle law so far. The background `U` is arbitrary, of unbounded length and height. Any word with this structure needs its denominator to grow like `2^(n(e−1))` up to the resultant. So for `q = 1`, the representation count must grow: `r = Ω(√(m/log m))` when the average marker size is bounded. The `q = 1` step imports Matveev's estimate, as C011 does.
- **What it does not give.** As main says, `r` counts repetitions of *one* background. It is not the rotation mismatch count `s`, so the recommended target "`ρ(w) ≥ F(m) → ∞` for every cycle" is still open. Two of main's results mark the remaining difficulty:
  - polynomial coprimality does not prevent numerical cancellation: the `q = 5` period-17 cycle has `G = 1` but cancellation 1,015,513;
  - the height obstruction: generalized cycles with `ρ = 3`, `B = Θ(m)` and `L/q = Θ(m)`.

**Two earlier side remarks are now resolved.**

- **The Matveev remark (Lean lane, 04:15).** Main checked the source. The cited Theorem 2.1 bounds `|e^Λ − 1|` directly, so no conversion is needed. The Lean lane's message had anticipated exactly this case ("unless … Theorem 2.1 is itself stated for `|e^Λ − 1|`"). Closed, no change.
- **The `3 ∤ q` remark (04:28).** It is moot for the cycle spectrum. Reduced denominators divide `D = 2^A − 3^m`, so they are coprime to 6 automatically. Accepted. The remark matters only for the Lean statement's broader domain.

```sh
python3 sidekick/probes/c013_background_check.py     # ~2 s, PASS
```

**Update 10:44: the Lean lane's C013 `OVERLAP_THEORY.md` §§1–2 unit is VERIFIED** (`9a81b08`). It is the paired-state run law and its denominator consequences, on `OddCycle`.

- **The theorems.**
  - `z_even` and `z_ne_zero`: `z_i = n_(i+h) − n_i` is even, and nonzero for primitive cycles with `h ≢ 0`.
  - `z_step` and `z_run`: `2^E z_end = 3^t z_start` along an agreeing run.
  - `z_run_factor`: (3), `z_end = 2·3^t k` and `z_start = 2^(E+1) k`, with `k ≠ 0`.
  - `diameter_ge`: (4).
  - `K_mul_L_gt`: (5).
  - `q_bound_delta` and `q_bound_rational`: (6) and (7), cleared, over ℝ and over ℤ. The bound goes through C006-c's (G4) and `η ≤ δ`.
- **Statement match.** It matches the prose: no circular order is used, and nothing compares `q` with `L`. Two parts are not in this unit: the longest-run pigeonhole in (6), and the marker family of §§3–5. As the lane notes, primitivity enters only through `k ≠ 0`.
- **Receipts.** Of 487 declarations, 401 use the standard three axioms, 38 use `[propext, Quot.sound]`, 46 use `[propext]` and 2 use none. A source scan is clean, and the sha256 `19e73031…` matches all three binding receipts.
- **Bookkeeping issue.** The lane's STATE now has two rows labelled "C013-a", iteration 34 (the list-level identities, 05:15 above) and iteration 58 (this unit). This feed calls the new one "C013-b".
- **Independent check.** `c013b_run_law_check.py` uses 77 actual cycles with `m ≥ 2`, ordered or not, every nonidentity rotation, and every maximal agreeing run: 12,550 runs, including `t = 0`. On every run:
  - `z` is even and nonzero;
  - the run law holds exactly;
  - the factorisation holds with `k ≠ 0`;
  - the diameter bound holds;
  - the integer inequality (7) holds, with the real `B`, at slack between 4 and 1.8·10^7.

---

## 2026-10-19 04:35 — REFEREE C012 (main `de7db67`): obstructions confirmed; the candidate bound now has *discriminating* evidence (56,150 cases, no failure), and the earlier evidence was not discriminating

**C012's candidate.** For a word `w` and a rotation differing from it in `s` positions, `g^s·4^m < 2^(As)·3^m`, that is, `q > (1 − 3^m/2^A)·(4/3)^(m/s)`. If true, it would force every Collatz cycle to have `s ≳ m/log m`. Main correctly says its stored-cycle evidence is nondiscriminating.

**When a test can discriminate.** Every `q > 1` is coprime to 6, so `q ≥ 5`. The candidate can therefore fail only when its lower bound `(1 − 3^m/2^A)(4/3)^(m/s)` is at least 5. That requires `m/s ≥ log 5/log(4/3) ≈ 5.6`.

1. **The exhaustive grid is not discriminating.** I tested every primitive word with `D > 0` of length up to 9 and letters 1 to 5, at every nonidentity rotation: 18,892,900 rotations with `s` from 2 to 9. There are no counterexamples, but **0 of them are discriminating**, exactly as predicted. This confirms main's warning on a much larger set; it is not evidence for the candidate.
2. **A discriminating search finds no failure.** I sampled random structured words `(x_1, U, x_2, U, …, x_s, U)` with distinct markers, `U` over `{1,2,3}`, `|U|` from 4 to 20, `s = 3, 4, 5` and `m/s` up to about 21. Of 59,759 words, **56,150 are discriminating, and none fails.** The worst exponent ratio `log(g^s 4^m)/log(2^(As) 3^m)` among `g > 1` is 0.525, at `m = 18`, `s = 3`, `g = 1837`. So in this regime the candidate holds with wide slack.

This is random, not adversarial. Main's sharpness families (arbitrary even `s`, prescribed divisors of `g`) are the natural adversarial test, and the evidence remains finite.

**Also confirmed.**

- The corrected formula `C(k, 2^n) = 3^n + 2^k(4^n − 3^n)` for the word `(k, 2, …, 2)`.
- The family `(1, U, 3, U, 4, U)` is primitive with minimum rotation distance exactly 3, on 300 random backgrounds over `{2, 5}`.

**Update 04:45: a second independent check.** The Lean lane read `COUPLED_SYSTEM.md` and `COUPLED_OBSTRUCTIONS.md` §§1–3 by hand and found no error. It checked:

- the block identities, `det B = det B' = ±D`, `|det M| = D^(s−2)·Π|β'_i − β_i|`, divisibility of every `k`-minor by `D^(k−2)`, and the local Smith form;
- the family `w_(r,t)`, including the small example `(1,2,2,1,2,2,2)` with all seven states and `det = −2^10·1909²`;
- the three-defect family, the corrected `C(5, 2^n) = 32·4^n − 31·3^n`, and the counting bound.

**The `s = 2` base of the candidate is now machine-checked.** C011-a's `two_defect_q_bound` is exactly the candidate at `s = 2` in cleared integer form. Any future estimate for `s ≥ 3` can be stated as `g^s·2^(2m) < 2^(As)·3^m` and compared directly.

**Assessment.**

- **The obstructions are correct and useful.** All-cut elimination is vacuous for `s ≥ 3`, a three-mismatch word can hide an arbitrary background, and a fixed number of S-unit terms cannot encode the shared-arc intercepts. Main is right that they rule out shortcuts, not the candidate.
- **The recommended target is a sound intermediate step.** It is a growing lower bound `ρ(w) ≥ F(m) → ∞` on rotation distance for every Collatz cycle. It is uniform, specific to `d = 1` through `q = 1`, and strictly weaker than the headline.
- **For future tests.** Restrict to cases with `(1 − 3^m/2^A)(4/3)^(m/s) ≥ 5`. Below that threshold, every word passes automatically.

```sh
python3 sidekick/probes/c012_candidate_check.py     # ~76 s, PASS (discriminating counts reported)
```

---

## 2026-10-19 04:08 — REFEREE C011 (main `b896512`): the two-rotation-defect exclusion is reproduced, a genuine structural cycle exclusion for `d = 1`

**Reproduced** (`c011_two_defect_check.py`, about 25 s, PASS).

- **The theorem on a complete grid.** I took every primitive positive word with `D > 0`, length up to 9 and letters 1 to 5. In this range, 20,431 words have a nonidentity rotation differing in exactly two positions, giving 33,360 such rotations. In every case:
  - the two mismatches are a swapped pair of valuations `a, a+k`;
  - `den(w) > 1`;
  - `g² < (2^k − 1)²·2^(A−m−k)·3^m`;
  - `den(w) > (1 − 3^m/2^A)·(2/√3)^m`, checked in exact integer form.
- **The marker family.** For `(3, b_n, 4, b_n)` with `n = 2^r − 1` and `r = 2..6` (period up to 128), the word is primitive. Its half-period rotation has exactly two unit mismatches, every rational state exceeds `n/128`, and `den > 1`.
- **The cancellation counterfamily.** For `1^t 2^(2t)`, `gcd(C, D) = gcd(4^t − 1, 3^t − 2^t)` for every `t ≤ 60`. The powers of 5 grow: `5 | g` at `t = 2`, `25` at `t = 10`, `125` at `t = 50`. So counting mismatches cannot bound the cancellation by itself. The theorem needs the period and arc arithmetic, as main says.

**Update 04:14: a second independent check.** The Lean lane read `ROTATION_DEFECTS.md`, `EXCLUSION.md` and `GENERAL_DEFECTS.md` in full and found no error. It re-derived:

- the swap structure and the fact that two defects force primitivity;
- the two-arc identity, `g | (2^k − 1)·gcd(C_u, C_v)`, the intercept bound and inequalities (5)–(9), and the finiteness argument;
- the adjacent-defect classification;
- the marker family, including `β > n/12`, every state above `n/128`, and the local-minimum count;
- all the controls: `q = 359` (`g = 73`, where the bound is exact), `q = 5, 7, 13`, the `t = 2` cancellation word, and the `q = 97` coupling `100 = 36 + 64`;
- every numerical constant in `EXCLUSION.md` §4 (`K_0`, `2.45e9`, `373/2750`).

**One precision remark, not an error.** Matveev's bound applies to the linear form `δ = A log 2 − m log 3` itself. `EXCLUSION.md` (1) displays it for `log(1 − e^(−δ))`. Since `1 − e^(−δ) ≥ δ/2` for `δ ≤ 1`, the step costs at most `log 2`, which the `2.45e9` margin absorbs. One sentence in the note would make the displayed (1) match the cited statement.

The lane queues the integer core as C011-a: the two-arc list identity, `g | (2^k − 1)·gcd(C_u, C_v)`, the intercept bound and `q²·2^(2A−2m)·3^m > D²`.

**Update 04:44: Lean C011-a is VERIFIED** (`0992e4f`). The elementary integer core of C011 is machine-checked in the two-defect normal form, a word `a :: u₀ ++ (a+k) :: v₀` together with a rotation equal to the swapped word.

- **`two_arc_identity`.** `C(a+k, u₀, a, v₀) − C(a, u₀, a+k, v₀) = (2^k − 1)·2^a·3^|v₀|·C(u₀ ++ [a+k])`.
- **The cancellation bound.** `g | (2^k − 1)·gcd(C_u, C_v)`, together with the intercept bound that keeps the last letter.
- **`two_defect_q_bound`.** `D²·2^(2m) < q²·2^(2A)·3^m`. This is C011's (7), `q > (1 − 3^m/2^A)(2/√3)^m`, in exact integer form.
- **Receipts.** 230 declarations use the standard three axioms; the helpers use subsets. The build has no diagnostics, a source scan is clean, and the sha256 `46b48a59…` matches.
- **Not formalised.** The step to `q = 1` exclusion rests on the imported Matveev and Hercher/Barina inputs, which are not Lean targets. So the two-defect exclusion is now formal *up to* those two published inputs.
- **C012.** The Lean lane also read C012 and found no error.

**Assessment.**

- **What it gives.** This is the cycle goal's first exclusion defined by a property of the *whole word*, with no block decomposition assumed: no nontrivial Collatz cycle has a rotation differing from it in exactly two positions, for any period, heights or amplitudes.
  - The elementary bound `q > (1 − 3^m/2^A)(2/√3)^m` does most of the work.
  - Closing the `q = 1` case where `2^A/3^m` is extremely close to 1 imports two published results: Matveev's explicit linear forms in logarithms, and the Hercher/Barina odd-period lower bound. Main's checker confirms only that their endpoints are compatible. Neither was rerun, and the report says so.
- **Its size.** The class is thin. A typical word differs from every rotation in many positions. The natural target is the one main names: a lower bound on rotation mismatch count that grows with the period.
- **The obstacle to extending it.** The `q = 97`, `233` and `359` coupling controls (`100 = 36 + 64`, with `g = 5` dividing the total but neither part) show why a proof cannot just add up per-mismatch contributions.
- **The `d`-controls.** The bound is a lower bound on `den` valid for every `d`. Real `3x+d` cycles with such words simply have `den = d` above the bound, and main's controls at `q = 35` and `505` confirm that.

```sh
python3 sidekick/probes/c011_two_defect_check.py     # ~25 s, PASS
```

---

## 2026-10-19 03:39 — REFEREE C010 (main `cae57b0`): local rounding is rejected, and the rejection is confirmed; ordered-cycle exclusion is rightly demoted to a benchmark

**Reproduced** (`c010_gap_check.py`, under a second, PASS).

- **The gap lattice.** `E` shifts sorted coordinates by one place and doubles the wrapped coordinate. As exact integer matrices for `m ≤ 12`, `E^m = 2I`, and `U = E − I` has the integer inverse `I + E + … + E^(m−1)`. So the complete gap system preserves the integer lattice exactly. It adds no information beyond `D | C`.
- **The `q = 5` control.** `19 → 31 → 49`, divided by 5, has sorted normalised gaps `11/10` and `13/10` and seam `7/5`. These pass main's sharp spacing bounds `1/2, 1/2, 1` with slack, yet `den = 5`.
- **The mechanical seam.** For all 381 primitive mechanical words with coprime `(A, m)`, `2^A > 3^m` and `2 ≤ m < 30`, the sorted rotation intercepts satisfy `2B_0 − B_(m−1) = 3^(m−1)`. So the seam gap is `3^(m−1)/D`, as main states. Main combines this with the C004 approximants to obtain gaps of any size. That is the infinite counterfamily to rounding.

**Update 03:49: a second independent check.** The Lean lane read `GAP_LATTICE.md`, `ODD_ROUNDING.md` and `ROUNDING_PROBE.md` in full and found no error. It re-derived:

- the unimodular inverse, its explicit form, and that the gap equations add nothing to the minimum-state arrow;
- `|det(2E^s − 3I)| = 2^(m+s) − 3^m`, via the eigenvalues `2^(1/m)ζ^k`;
- the seam identity and every pair bound;
- every number in the `q = 5`, `q = 13` and `q = 83` controls, including `2407/545`;
- the invalid `4 → 13 → 5 → 4` loop.

**Two precision remarks, not errors.**

1. `GAP_LATTICE` §2's "the `Z_j` are distinct because the `n_i` are odd" also needs primitivity, meaning distinct states.
2. The determinant formula needs `gcd(s, m) = 1`. It is stated only implicitly, as "one `m`-cycle". C005's coprime rank shift supplies it.

The lane queues the pair bounds and the summed bound `L ≥ R_q(H)` as C010-a.

**Update 04:28: Lean C010-a is VERIFIED** (`9c44c0c`). C010's sharp odd-spacing pair bounds and the summed bound `L ≥ R_q(H)` are now machine-checked on ordered primitive odd cycles, in scaled integer form.

- **The four pair bounds.** Equal heights, downward, the seam, and upward. The upward case carries the mod-6 increment `η` (`eta_refine`).
- **The summed bound.** `rounding_bound` is the telescoped sum.
- **Receipts.** 219 declarations use the standard three axioms; the helpers use subsets. The build has no diagnostics, a source scan is clean, and the sha256 `8569c7d1…` matches.

**A remark for main: one hypothesis can be dropped.** C010 assumes `q` coprime to 6 for its `η` table. The formal statements need only `q` odd, which positive valuations already force (`q_odd`). For `q ≡ 3 (mod 6)` the true increment is 6, so `η = 4` remains a valid, if non-sharp, bound. I checked numerically that `3r − q(2^k − 1) ≥ η` at the first odd `r` above the threshold, for every odd `q < 200` (multiples of 3 included) and every `k < 12`. So the declared domain of C010's diagnostic can drop `3 ∤ q`.

**Assessment.**

- **Four batches without an exclusion.** This is the second consecutive disciplined rejection, after C009. C007–C010 have each produced correct structure and exact obstructions, but no new exclusion at `q = 1`. Main's conclusion is the right calibration: order is demoted from "the route" to "an open benchmark", with its payoff (`H > 8L`) stated conditionally.
- **The next mechanism.** It compares a word with a nontrivial rotation and asks whether sparse letter differences bound `gcd(C_w, D_w)`, uniformly in block sizes. This targets whole-word cancellation, which every route so far has shown to be the missing ingredient. One caution from earlier batches: rotation differences produce `C_(rot w) − C_w = D·(x_k − x_0)`. C004 showed that bounds on the size of state differences alone fail (the close-pair obstruction). So the gain has to come from the *arithmetic* of the sparse difference, not from its size.
- **The Lean lane.** It has just finished C006's run inequality. Its formal interface (prefix identities, `C_append`, rotations) is directly reusable for the rotation-difference mechanism.

```sh
python3 sidekick/probes/c010_gap_check.py     # <1 s, PASS
```

**Update 10:18: Lean C010-b is VERIFIED** (`4a707e3`). This is the complete dyadic gap lattice, `GAP_LATTICE.md` §§1–2.

- **§1, for any vector.**
  - `cgap` defines the complete gaps, with the seam `2Z_0 − Z_(m−1)`.
  - `Z_eq_sum_cgap` is (1), the telescoping inverse.
  - `dvd_cgap_iff`: the states and the gaps have the same divisors.
  - `cgap_int_iff` and `clears_iff`: the states and the gaps become integral together, so their least common denominators agree.
  - `cgap_pos_iff`: the gaps are all positive exactly when the states lie in the normalised order cone.
- **§2, for ordered cycles.**
  - `gap_eq_cgap`: C006's sorted gaps are these complete gaps.
  - `Z_dvd_isUnit` and `gap_dvd_isUnit`: in a reduced cycle, `gcd(Z) = gcd(G) = 1`.
- **Statement match.** It matches C010 §§1–2, with two scope notes.
  - `E^m = 2I` is not stated as a matrix identity, but the content it carries is formal.
  - §2 is stated on `OrdCycle`, while the prose says it also holds for unordered cycles. It needs the maximal height to be attained, because the structure's `B` is only an upper bound.
- **Receipts.** Of 467 declarations, 383 use the standard three axioms, 37 use `[propext, Quot.sound]`, 45 use `[propext]` and 2 use none. A source scan is clean, and the sha256 `abc5ff86…` matches all three binding receipts.
- **Independent check.** `c010b_gap_lattice_check.py` covers two sets.
  - **92 actual `3x+q` cycles, ordered and unordered.** On every cycle (1) holds, `gcd(Z) = gcd(G) = 1`, and every gap is positive, so the prose's unordered claim holds in data.
  - **All 337 rational ordered cycles, normalised to parameter 1.** The least common denominator of the scaled states equals that of their complete gaps, and both equal the reduced `q`.
- **What follows.** As C010 says, no denominator exclusion: moving from states to gaps does not make the lattice easier, and that is now a pair of formal equivalences.

**Update 10:32: Lean C010-c is VERIFIED** (`b192b3c`). This is C010 §2 without the ordering hypothesis, which closes the scope note above.

- **The theorems,** stated on `OddCycle`, so for any reduced cycle whose maximal height is attained, ordered or not.
  - `Z_dvd_isUnit`: the C010-b proof, which never used the ordering.
  - `cgap_dvd_isUnit`: the complete gaps of *any* arrangement of one period have gcd 1. The sorted arrangement is a special case.
  - `q_dvd_of_dvd_mul`, `clears_q_iff` and `q_le_of_clears`: the least positive common denominator of `Z/q` is exactly `q`.
  - `clears_q_cgap_iff`: `G/q` has common reduced denominator exactly `q`, for any arrangement.
- **Not formalised.** The prose's remark that the scaled states are distinct is neither used nor formalised.
- **Receipts.** Of 475 declarations, 391 use the standard three axioms, 37 use `[propext, Quot.sound]`, 45 use `[propext]` and 2 use none. A source scan is clean, and the sha256 `1379f455…` matches all three binding receipts.
- **Independent check.** `c010c_any_arrangement_check.py` covers 81 reduced actual `3x+q` cycles, ordered and unordered, with the sorted arrangement and 20 random permutations each (1,701 arrangements).
  - On every arrangement the gaps have gcd 1, and the least common denominator of the scaled gaps is exactly `q`. On every cycle, `lcd(Z/q) = q`.
  - The 11 non-reduced cycles found, the fixed points `n = q`, were skipped, since they are outside the theorem's `hred` hypothesis. Including them makes the denominator check fail, as it should.

---

## 2026-10-19 03:37 — VERIFIED Lean C006-a (`claude/lean-lane` `c4e4246`): C006's sparse-forcing inequality is machine-checked for every ordered primitive odd cycle

**`G1_first`.** On an `OrdCycle` (an ordered primitive odd cycle with `m ≥ 2` and the exponent window), `2^⌊(m−1)/J⌋ < 2^B·L`, where `J` is the number of sorted ranks with `T_r ≠ 0`. Since `⌊(m−1)/J⌋ = ⌈m/J⌉ − 1` (checked for all `m, J < 400`), this is exactly C006 §3's **`L > 2^(⌈m/J⌉ − 1 − B)`**.

**How it was built.** The units arrived over the last hour and I verified each from source and receipts:

- run lemma and height steps (part 1, `74d66d4`);
- sorted states, seam and gaps (2a, `61f252d`);
- gap recurrence (2b, `a5d6178`);
- height term, seam positivity and per-run bound (3, `a1e1054`);
- the cyclic pigeonhole `exists_run` (3c, `c4e4246`).

`exists_run` is a general combinatorial lemma: `J ≥ 1` forced positions on an `m`-cycle leave a run of `⌊(m−1)/J⌋` unforced positions after some forced one. It is proved by iteration, with no sorting. `J_eq` identifies the orbit count with the rank count.

**Checks.**

- **Hypotheses.** Only `q > 0`, order, primitivity and `m ≥ 2`. `q ≤ L` is not needed for this inequality.
- **Axioms.** 183 declarations use the standard three; the helpers use subsets.
- **Build.** No diagnostics.
- **Source scan.** Clean.
- **Hash.** The sha256 `31a44291…` matches the receipt.

**Update 03:49: part 3d is VERIFIED** (`3854bcf`). C006's (H1), `J ≥ B + 1`, is now machine-checked for ordered primitive odd cycles. Here `J` is 1 plus the number of adjacent changes of sorted height, and every height up to `B` is attained in sorted order. Of the declarations, 188 use the standard three axioms; the helpers use subsets. The build has no diagnostics, a source scan is clean, and the sha256 `bc6e4e25…` matches. The Lean lane also read C010 and found no error. Still open from the list below: the `e_run` exponent sum and the consequences for `q`.

**Update 03:56: part 3e is VERIFIED** (`ccb302f`). This closes the elementary scope of C006.

- **The theorem.** `G1_second` states `D·2^⌊(m−1)/J⌋ < 2^B·q·C_h`, that is, `q > (D/C_h)·2^(⌈m/J⌉ − 1 − B)`. It holds for every ordered primitive odd cycle with `m ≥ 2`, and uses `D > 0` (`D_pos`, from the cycle identity `D·L = q·C_h`).
- **A sharper form.** This uses the true weighted intercept `C_h`. C006's prose states the `C_c` form, and `C_h ≤ C_c`, so the formal statement is the sharper one.
- **Receipts.** 192 declarations use the standard three axioms; the helpers use subsets. The build has no diagnostics, a source scan is clean, and the sha256 `7e121d16…` matches.
- **What is now formal from C006.**
  - `2^⌊(m−1)/J⌋ < 2^B·L`;
  - `D·2^⌊(m−1)/J⌋ < 2^B·q·C_h`;
  - `J ≥ B + 1`;
  - the gap recurrence (G3).
- **Not planned.** The `e_run` refinement, the imported Bugeaud corollary (G2), and (G4).
- **What remains open.** The integrality step `D | C_h` at `q = 1` is still the open obligation, as C006 and C010 state. None of this is a cycle exclusion.

**Not yet formal (part 3d).**

- `J ≥ B + 1` in sorted order;
- the sharper exponent sum `e_run`;
- the consequences `q > (D/C_c)·2^(…)` and (G4);
- the Bugeaud corollary, which is imported and not a target.

**What is formal for the cycle programme.** The following are now all formalised, each within hours of the written proof:

- C001–C003's block theorems;
- C004's narrow classification;
- C005's `q = 1` three-band theorem;
- C006's run inequality;
- C007 and C008's identities.

The `q = 1` structural chain is formal up to R71's `g = 1`, and that is what remains for the integer corollary `H > 2L`.

**Update 08:47: Lean C006-b is VERIFIED** (`3faa040`). This is the `e_run` refinement of C006's run bound.

- **The theorems.**
  - `run_bound_E`: along a zero-forcing run, `2^(e_run)` divides the gap at the run start, so it is at most that gap. Here `e_run = E(r₀, t)` is S1-a's exponent sum.
  - `run_bound_E_L`: `2^(e_run) < 2^B n_0`.
  - `E_ge`: `e_run ≥ t`.
  - `G1_first_E`: (G1) in `e_run` form.
- **Receipts.** Of 434 declarations, 350 use the standard three axioms, 37 use `[propext, Quot.sound]`, 45 use `[propext]` and 2 use none. A source scan is clean, and the sha256 `282d9102…` matches all three binding receipts.
- **Independent check.** `c006b_erun_check.py` covers 97 zero-forcing stretches on the 33 actual ordered `3x+q` cycles. On every one, `2^(e_run)` divides the start gap and `2^(e_run) < 2^B n_0`. In 77 of them `e_run > t`, so the refinement over `2^t` is strictly sharper in most cases.
- **Still informal in C006.** (G4), `δ = Σ log(1 + q/(3n_i)) ≤ mq/(3L)`, is the lane's candidate next unit; it is the elementary `L` bound behind the 08:22 calibration. Also informal: the imported (G2)/(G5) and the `C_c` form of (G1).

**Update 08:57: Lean C006-c is VERIFIED** (`b113413`). C006's (G4) is now formal for every `OddCycle`, at any `q` and with no ordering or reducedness hypothesis.

- **The theorems.**
  - `prod_arrow`: `2^A Π n_i = Π(3n_i + q)`.
  - `log_identity`: `A log 2 − m log 3 = Σ log(1 + q/(3n_i))`, over ℝ.
  - `G4`: `δ ≤ mq/(3L)`.
  - `L_mul_delta_le`: the cleared form `3Lδ ≤ mq`.
- **What this settles.** Together with `G1_first` and `run_bound_E_L`, the elementary half of the 08:22 small-`J` calibration is formal. Only Matveev's estimate and the Hercher/Barina period bound remain imports.
- **Receipts.** Of 438 declarations, 354 use the standard three axioms, 37 use `[propext, Quot.sound]`, 45 use `[propext]` and 2 use none. A source scan is clean, and the sha256 `2d600c05…` matches all three binding receipts.
- **Independent check.** `c006c_g4_check.py` covers 93 actual cycles of `3x+q` for `q ∈ {1, 5, 7, 11, 13, 17, 19, 23, 29, 61, 233, 1201}`, ordered or not. On every cycle the integer product identity holds exactly, the log identity holds to 1e-12, and `δ ≤ mq/(3L)` holds. The bound is loose by a factor between 1.16 and 45.

**Update 09:08: Lean C006-d is VERIFIED** (`818d1d6`). This is (G2), conditional on an explicit linear-form gap.

- **The theorems.**
  - `delta_ge_gap`: `(2^A − 3^m)/2^A ≤ δ`, using `log x ≥ 1 − 1/x`.
  - `G2_of_gap`: under the hypothesis `2^A ≤ 2^c m^μ (2^A − 3^m)`, `3·2^⌊(m−1)/J⌋ < 2^(B+c) q m^(μ+1)`.
  - `G2_of_gap_collatz`: the instance with `q = 1` and `B ≤ 2`.
- **What it settles.** This is the reduction behind the 09:06 calibration. With `(c, μ) = (172, 341)`, it gives `J > 1.07·10^7` for every `H < 8L` Collatz cycle. That number is conditional on `mmusson/collatz`'s `gap_all`, which has not been replayed. In this lane the gap is an explicit hypothesis.
- **Receipts.** Of 441 declarations, 357 use the standard three axioms, 37 use `[propext, Quot.sound]`, 45 use `[propext]` and 2 use none. A source scan is clean, and the sha256 `12831a36…` matches all three binding receipts.
- **Independent check.** `c006d_g2_check.py` uses the 33 actual ordered `3x+q` cycles with `μ = 0` and the tightest admissible `c`. `delta_ge_gap` and the conclusion of `G2_of_gap` hold on every one, with a log₂ slack between 3.3 and 23.6.

**Update 10:05: Lean C006-e is VERIFIED** (`6c42229`). This is the `C_c` form of (G1).

- **The theorems.**
  - `Ppre_eq`: the normalised prefix sums are `P_i = A_i + h_i`.
  - `Cc` and `cword_prefix`: `C_c = Σ 3^(m−1−j) 2^(P_j)`.
  - `Cpre_le_Cc`: `C_h ≤ C_c`.
  - `D_mul_n_le`: `D·L ≤ q·C_c`.
  - `cword_eq_mech`: at `q = 1` with `B ≤ 2`, the normalised word read from the minimum is `mech(A, m, 0)`.
  - `Cc_gcd_one`: in that setting, `gcd(C_c, D) = 1` by R71-a.
  - `G1_second_c` and `run_bound_c`: (G1)'s second inequality in `C_c` form, overall and per zero-forcing run.
- **What this settles.** (G1) is now formal in all three of C006's forms. The third form's gap is a hypothesis (C006-d), and EXT-1 replayed an instance of it. C006's `C_c`, R71's `B_0` and `mmusson`'s `chr` are the same Böhm–Sontacchi sum.
- **Receipts.** Of 451 declarations, 367 use the standard three axioms, 37 use `[propext, Quot.sound]`, 45 use `[propext]` and 2 use none. A source scan is clean, and the sha256 `935508e4…` matches all three binding receipts.
- **Independent check.** `c006e_cc_check.py` uses all 33 actual ordered `3x+q` cycles and all 337 rational ordered cycles. On every cycle:
  - `P_j = A_j + h_j` and `C_h ≤ C_c`;
  - `gcd(C_c, D) = 1` whenever `gcd(A, m) = 1`;
  - on the actual cycles, `D n_0 ≤ q C_c` and `G1_second_c` hold.
- **A generalisation the data shows.** The normalised word from the minimum equals `mech(A, m, 0)` for *every* ordered cycle, at any `q`. This is C005's order lemma. Lean needs `q = 1` and `B ≤ 2` only to obtain the ordering through `three_band`; on an `OrdCycle` it should hold directly.

**Update 10:10: Lean C006-f is VERIFIED** (`e5e979a`). The generalisation above is now a theorem on every `OrdCycle`.

- **The theorems.**
  - `c_formula`: `c_i = q′ + ⌊(i+1)s/m⌋ − ⌊is/m⌋`.
  - `Apre_eq_ord`: `A = mq′ + s`.
  - `cword_eq_mech_ord`: the normalised word from the minimum is `mech(A, m, 0)`, with no `q = 1`, `B ≤ 2` or reducedness hypothesis.
  - `coprime_Apre`: `gcd(A, m) = 1` for every ordered cycle.
  - `Cc_gcd_one_ord`: with positive letters, `gcd(C_c, D) = 1`.
- **Statement match.** This is the word form of C005's order lemma. C006-e's results are its instances at `q = 1`, `B ≤ 2`.
  - As the lane notes, R71 bounds `gcd(C_c, D)`. The `q = 1` question is whether `D` divides `C_h = C_c − E_h`, and this theorem does not touch it.
- **Receipts.** Of 456 declarations, 372 use the standard three axioms, 37 use `[propext, Quot.sound]`, 45 use `[propext]` and 2 use none. A source scan is clean, and the sha256 `392efa2c…` matches all three binding receipts.
- **Independent check: the separation question.** `c006f_order_word_check.py` uses the actual `3x+q` cycles.
  - All 33 ordered cycles have the phase-0 mechanical normalised word and `gcd(A, m) = 1`.
  - 6 of the 44 unordered cycles also have it. Examples, as `(q, min, m, B)`: `(7, 5, 2, 1)`, `(13, 131, 15, 3)`, `(11, 13, 8, 2)`.
  - 26 of the 44 have a mechanical normalised word up to rotation or phase.
  - So the word statement does not characterise the ordered class, as C005 §4 says: a mechanical `c` can coexist with inversions. The ordering hypothesis is needed for the proof route, but it is strictly stronger than the word conclusion.

---

## 2026-10-19 03:17 — REFEREE C009 (main `ec48fbd`): the rejection of excursion compression is confirmed; the next milestone has a concrete payoff

**Reproduced** (`c009_excursion_check.py`, under a second, PASS).

- **The ordered `q = 13` cycle.** `283 → 431 → 653 → 493 → 373 → 283` follows exact `3x+13` arrows and is ordered with rank shift 3 on five ranks. Deleting the single height-one state 653 and keeping first returns leaves the sorted core `(283, 373, 431, 493)`. Its successor ranks are `(2, 0, 3, 1)`, which is not a circular shift.
- **The one-point deletion theorem.** Consider a circular shift by `s` on `m` ranks, with `gcd(s, m) = 1`. Deleting any one rank gives a circular first-return shift exactly when `s = 1` or `s = m − 1`. This holds in all 13,108 cases with `3 ≤ m ≤ 40`, every coprime `s` and every deleted rank.
- **The `q = 83` excursion.** `277 → 457 → 727 → 283` has valuations `(1, 1, 3)`, and `32·283 = 27·277 + 83·19`. Its slope `27/32` is below 1, yet it rises by 6. It lies on the ordered period-7 cycle through 157.
- **Open `q = 1` paths.** `7 → 11 → 17 → 13` and `19 → 29 → 11` are exact Collatz odd steps, as stated. They are open paths, not cycles.

**Update 03:19: a second independent check.** The Lean lane read C009 in full and found no error. It re-derived by hand:

- the cut lemma, through the prefix decomposition, which is the already-formal `C_append`, plus the parity step;
- the elimination `D·x = q·C`;
- the one-point deletion table: compressed shifts `s`, `s − 1` and `2s − 1 (mod m − 1)`, with both regular groups nonempty exactly when `2 ≤ s ≤ m − 2`;
- every number in the `q = 13`, `q = 83` and `q = 1` controls.

The deletion theorem now has two independent confirmations: this lane's exhaustive check up to `m = 40` and the Lean lane's proof by cases. The Lean lane queues the cut lemma as C009-a.

Its current unit, C006-a part 2b, formalises the gap recurrence in rank coordinates, with the seam: `2^(e_r)·Δ_((r+h) mod m) = F_[r+1] − F_[r]`. That is the formal counterpart of the "complete sorted-gap system" main names as its next mechanism, so the next main batch and the Lean lane are converging on the same object.

**Update 03:22: Lean C006-a part 2b is VERIFIED** (`a5d6178`).

- **The theorem.** `gap_recurrence`: for a primitive narrow cycle with `m ≥ 2`, `2^(e_r)·gap((r + h) mod m) = Fext(r + 1) − Fext(r)` for every sorted rank `r < m`. This is C006's gap recurrence (G3) in rank coordinates, including the seam. It covers all four cases: both low, low/high at the seam gap, both high, and the seam rank.
- **Receipts.** Of 198 declarations, 156 use the standard three axioms; the helpers use subsets. The build has no diagnostics, a source scan is clean, and the sha256 `a5af2f82…` matches.
- **What it is.** The "complete sorted-gap system" that main named as its next mechanism is now a Lean object.

**Update 03:28: Lean C006-a part 3 is VERIFIED** (`a1e1054`).

- **The structure.** `OrdCycle` packages an ordered primitive odd cycle with `m ≥ 2` and the exponent window.
- **The theorems.**
  - The height term `T_r`, with the seam, puts (G3) in C006's own form.
  - `T_eq_zero_iff`: `T_r = 0` exactly when adjacent sorted heights agree.
  - `T_seam_pos`: the seam term is forced positive.
  - `run_bound_L`: along a zero-forcing run of length `t` on the `+h` orbit, `2^t < 2^B·L`. This is C006's per-run bound `L > 2^(t−B)`.
- **Receipts.** 175 declarations use the standard three axioms; the helpers use subsets. The build has no diagnostics, a source scan is clean, and the sha256 `5a448bc7…` matches.
- **Remaining for C006's theorem (G1).** Part 3c: the cyclic pigeonhole `⌈m/J⌉ − 1` and `J ≥ B + 1`.

**Update 04:09: Lean C009-a is VERIFIED** (`3e78e0f`).

- **`cut_lemma`.** Take a positive word `w`, odd `q > 0`, `x > 0` and odd `y` with `2^Σw·y = 3^|w|·x + q·C_w`. Then every cut state `(3^j x + q·C(take j w))/2^(Σ take j w)` is a positive odd integer, and every arrow is exact. This is C009's cut lemma. Oddness of `x` turns out to be redundant.
- **`elimination`.** `D(E ++ P)·x = q·C(E ++ P)`.
- **The `q = 1` equivalence.** `D | C` holds exactly when there is an odd integer cycle with all the cylinders.
- **Receipts.** 207 declarations use the standard three axioms; the helpers use subsets. The build has no diagnostics, a source scan is clean, and the sha256 `18cbad0b…` matches.
- **What this formalises.** The "cuts add no congruence" half of C009's rejection.

**Update 05:07: Lean C009-b is VERIFIED** (`15838f0`). C009's one-point deletion theorem is machine-checked.

- **The theorem.** `one_point_deletion`: for `2 ≤ m` and `1 ≤ s < m`, the compressed first-return map after deleting a rank is a rank shift exactly when `s = 1` or `s = m − 1`.
- **Axioms.** Only `[propext, Quot.sound]`, a strict subset of the standard three: it is pure ℕ arithmetic.
- **The control.** The `q = 13` control holds by `decide`, as a cyclic relabelling of the prose's `(2,0,3,1)`.
- **Receipts.** The build has no diagnostics, a source scan is clean, and the sha256 `1f618576…` matches.

**A remark for main: `gcd(s, m) = 1` is not needed.** The three-row table holds for every `1 ≤ s < m`. I re-ran my deletion test with **no coprimality filter**: all 1,770 cases with `m ≤ 60` and `1 ≤ s < m` agree. The earlier 13,108-case check had restricted to coprime `s`.

**Assessment.**

- **This is a well-run negative result.** Main tested a specific mechanism, hit its own pivot criterion, and recorded *three* independent exact obstructions:
  - the lattice is unchanged, so the algebra gives back `D | C`;
  - order is not inherited, by the deletion theorem;
  - excursions have no automatic descent sign.

  It then retired the mechanism instead of growing a catalogue. That is the calibration the brief asks for.
- **The milestone now has a concrete payoff.** Main's recommended milestone is to exclude every nontrivial ordered integer cycle, with no bound on period, height or height changes. C005, now machine-checked in Lean as C005-b, says that every primitive `q = 1` cycle with `H < 8L` is ordered. So this milestone would imply **`H > 8L` for every nontrivial Collatz cycle**, up from the `H > 2L` given by C004 and R71. It would also rule out ordered cycles of any height.
- **Next step.** It is "global integer rounding in the complete sorted-gap system", with the same pivot rule. I have no dispute. The `H ≥ 4L` case (`B ≤ 1`) is still the smallest new instance on the way, if a bounded test is wanted.

```sh
python3 sidekick/probes/c009_excursion_check.py     # <1 s, PASS
```

---

## 2026-10-19 02:56 — REFEREE C008 (main `93117c0`): reproduced; residue methods describe the `q > 1` spectrum but cannot reach `q = 1`, as main itself concludes

**Reproduced** (`c008_residue_check.py`, under a second, PASS).

- **The sorted-rank law.** It holds on all 50 ordered census cycles with `q > 1`. Choose `um + vA = 1` and `t = 2^u 3^v (mod q)`. Then `t^m ≡ 2` and `t^A ≡ 3`, and the `j`-th smallest normalised state is `z_[j] ≡ L·t^j (mod q)`.
- **The necessary condition on ordered cycles.**
  - The group `⟨2,3⟩ mod q` is cyclic for every ordered cycle's `q`, because it is generated by `t`. That is an elementary consequence of C005's coprime totals.
  - It is **non**cyclic modulo 35, 65 and 91.
  - No ordered census cycle has 35, 65 or 91 dividing its `q`.
- **The two counterexamples to primewise matching.** Both are actual raw cycles of `3x + 5,077,565`, where `5,077,565 = 2^27 − 3^17`. Each has period 17 and reduced denominator `q`, is ordered, and has `q ≤ L`.
  - **`L = 446,400,719`, `B = 3`.** Modulo 5, normalised heights 1 and 3 both have residue set `{4}`. Raw heights 1, 2 and 3 have `{3}`, `{2,3}` and `{2}`: three levels sharing two residues. Both are Hall failures, as main states.
  - **`L = 365,289,811`, `B = 2`.** Every raw height set is `{1,4}`: three levels sharing two residues.

**Update 03:01: two Lean lane results.**

- **The Lean lane re-derived C008 by hand and found no error.** It checked the sorted-rank law from the mechanical `P_i = ⌊iA/m⌋` with `A = m + s`. It also checked `ord(t) ≥ 4`, and that `⟨2,3⟩ = (Z/35)^× ≅ Z/2 × Z/12` is not cyclic. It queues the prefix and cycle identities and the integer sorted-rank law as C008-a.
- **Lean C006-a part 2a is VERIFIED** (`61f252d`). This is C006 §3's sorted-order bookkeeping on the abstract `NarrowCycle`:
  - a rank bijection on primitive cycles;
  - sorted states `y` that are strictly increasing, with `y_0` the minimum;
  - the seam extension `yext m = 2y_0`;
  - positive gaps summing to the minimum (`sum_gap`), each below it (`gap_lt`);
  - the successor in rank coordinates, `x_idx_succ`: rank `r` goes to `(r + h) mod m`.

  Of 183 declarations, 141 use the standard three axioms; the helpers use subsets. The build has no diagnostics, a source scan is clean, and the sha256 `99345455…` matches.

**Update 03:09: Lean C008-a is VERIFIED** (`c8f3d2e`).

- **Common roots.** `exists_common_root` holds in any commutative group: `x^A = y^m` with `gcd(A, m) = 1` gives a common root `t`. `zmod_common_root` applies it in `(ZMod N)ˣ`: for `N` coprime to 6 with `N | 2^A − 3^m`, there is a unit `t` with `t^m = 2` and `t^A = 3`. So `⟨2,3⟩` is cyclic modulo every such `N`.
- **Prefix and cycle identities.** `prefix_identity` and `cycle_identity` give `(2^A − 3^m)·n_0 = q·C`. `q_dvd_D` then gives `q | 2^A − 3^m` for reduced cycles.
- **The residue law.** `sum_a_range` gives `P_i = ⌊iA/m⌋`. `sorted_residue_law` is the integer sorted-rank law: `2^(P_i)·z_[(ih) mod m] ≡ 3^i·z_[0] (mod q)`. The final substitution to `z_[j] ≡ L·t^j` is not written out in Lean.
- **Not formalised.** The forbidden factors 35, 65 and 91 (finite computations on top of the cyclicity theorem), `T ≥ 4`, and the counterexample cycles.
- **Receipts.** Of 193 declarations, 151 use the standard three axioms; the helpers use subsets. The build has no diagnostics, a source scan is clean, and the sha256 `ec96d12e…` matches.

**Assessment.**

- **What C008 establishes.** These are correct statements about the ordered spectrum *for `q > 1`*. The cyclicity condition is a genuine, if elementary, new necessary condition in the spectrum law.
- **Why it cannot reach the target.** At `q = 1` all residue information disappears, since every numerator is congruent to 0. So no residue-matching argument can reach the denominator-one target. Main's report says exactly this and rejects the primewise route.
- **The next step is right.** Main's plan is to couple `D | C_h` at `q = 1` with the sorted-rank gap inequalities and the height-legality constraints, by cutting at excursions. Its pivot rule is good discipline: if a pass only recovers `D | C_h`, change mechanism.

```sh
python3 sidekick/probes/c008_residue_check.py <path to main's actual_cycles.json>   # <1 s, PASS
```

---

## 2026-10-19 02:41 — VERIFIED Lean C005-b (`claude/lean-lane` `b60fd21`): the first statement in the cycle programme specific to `d = 1` is machine-checked

**`three_band`.** It is stated on actual odd cycles, the structure `OddCycle`, with these hypotheses:

- periodic odd numerators `n_i`, with `n_0` the positive minimum;
- exact arrows `2^(a_i) n_(i+1) = 3n_i + q`, with `q > 0`;
- heights `2^(h_i) n_0 ≤ n_i < 2^(h_i+1) n_0`, with `h_i ≤ B`.

If `q = 1`, `B ≤ 2` (that is, `H < 8L`), `m ≥ 2` and the cycle is primitive (distinct numerators over one period), then:

- the normalised exponents `c_i = a_i + h_(i+1) − h_i` form the mechanical word `q' + ⌊(i+1)h'/m⌋ − ⌊ih'/m⌋`, with `gcd(h', m) = 1`;
- `Σa = mq' + h'`;
- `gcd(Σa, m) = 1`.

`q_ne_one_of_not_coprime` is C005's denominator corollary: `B ≤ 2`, primitivity and `gcd(A, m) ≠ 1` together force `q ≠ 1`.

**Checks.**

- **Statement match.** It matches C005 §2's three-band theorem. The prose's "`q` coprime to 6" is not needed (only `q > 0`), and `a_i ≥ 1` is not used. Starting at the minimum is the hypothesis `nmin`.
- **The proof chain.**
  - Scaled normalised states `Z_i = 2^(B−h_i) n_i` lie in `[lo, 2lo)`.
  - C005's inversion formula holds in scaled form.
  - At `q = 1`, height gaps `k ≤ 2` give no inversions (`no_inversion_of_le_two`), and equal images are excluded by primitivity.
  - So the structure is an ordered `NarrowCycle` (`toNarrow`), and C004's rank-count machinery applies.
- **Receipts.**
  - **Axioms.** Of 158 declarations, 118 use the standard three, 12 use `[propext, Quot.sound]`, 27 use `[propext]` and 1 uses none.
  - **Build.** No diagnostics.
  - **Source scan.** No `sorry` or `native_decide`.
  - **Hash.** The sha256 `00f4ba6c…` matches the receipt.

**Why it matters.** Every earlier formal cycle result holds for every denominator. This one uses `q = 1`, and it fails for `q = 11`: the census cycle with minimum 13 is an exact counterexample (02:13 entry). So the first piece of arithmetic specific to Collatz, rather than to the whole `3x+d` family, is now checked by the Lean kernel.

**Update 02:46: Lean C007-a is VERIFIED** (`9ff5a8d`).

- **The theorems.**
  - `residue_law`: `2^(P_i)·Z_i ≡ 3^i·Z_0 (mod q)`. This is C007's modular lemma in integer form. It holds for every `q > 0`, and neither order nor heights enter.
  - `three_not_dvd`: `3 ∤ q` implies `3 ∤ n_i`.
  - `dvd_all_of_dvd`: a prime-to-2 divisor of `q` that divides one numerator divides them all.
  - `min_top`: C007's min-to-top inequality `q(2^(h_j) − 1) < 3(n_j − 2^(h_j) n_0)` for ordered cycles, at every band.
- **Receipts.** Of 163 declarations, 122 use the standard three axioms; the helpers use subsets. The build has no diagnostics, a source scan is clean, and the sha256 `3c342e5a…` matches.
- **Scope and what agrees.** The candidate `B ≤ q − 1`, the census and the `q = 29` cycle are not Lean targets. My census check (`c007_height_check.py`) confirms the residue law at all 28,823 states.

**Update 02:53: Lean C006-a part 1 is VERIFIED** (`74d66d4`).

- **The theorems.**
  - The zero-forcing run lemma, for an abstract run: `run_pow_mul` gives `2^(E_t) G_t = 3^t G_0`, `run_dvd` gives `2^(E_t) | G_0`, and `run_lower` gives `G_0 ≥ 2^t`.
  - `c_le_two`: `q ≤ L` implies every normalised exponent `c_i` is 1 or 2.
  - `h_succ_le`: heights rise by at most 1 per step.
  - `exists_height_eq`: every intermediate height is attained.
- **Receipts.** Of 170 declarations, 128 use the standard three axioms; the helpers use subsets. The build has no diagnostics, a source scan is clean, and the sha256 `341ee1d8…` matches.
- **Next.** Parts 2–3 carry the sorted-order bookkeeping: the gap system with its seam, `G_start < 2^B L`, the cyclic pigeonhole, and `J ≥ B + 1` in sorted order.

**The Lean lane's read of C007: no error.** It re-derived the modular lemma, the min-to-top inequality (an instance of C005's (2)) and the `q = 5` height-residue sets. It queues those as C007-a. The candidate `B ≤ q − 1` itself is open and is not a Lean target.

---

## 2026-10-19 02:28 — REFEREE C007 (main `dddbe33`): reproduced; the candidate law `B ≤ q − 1` is the natural spectrum law whose `q = 1` case is the ordered-cycle target

**Reproduced** (`c007_height_check.py`, under a second, PASS).

- **The new `q = 29` cycle.** From seed 5859 the raw `3x+29` orbit reaches the cycle with:
  - minimum 7055 and maximum 1,051,393;
  - odd period 41 and total exponent 65;
  - `gcd(C, D) = 14,499,716,215,459,201`, so `den = 29`;
  - `B = 7` and `J = 38`.

  It is **ordered**. C001's census missed it because its minimum exceeds C001's seed range. That bears out the completeness caveat in my 00:21 entry: a census bounded by seed size misses cycles with large minima.
- **The candidate law `B ≤ q − 1`.** It holds on all 194 normalised census cycles with `q ≤ L`, ordered or not; 51 of them are ordered. The largest ratio `B/(q−1)` among the ordered ones is 3/4, from the `q = 5` period-17 cycles.
- **The modular identity.** `z_i ≡ L·3^i·2^(−P_i) (mod q)` holds at every state of every normalised census cycle with `q > 1`: 28,823 states.
- **The failed mechanism.** The ordered `q = 5` cycle from 187 has raw residue 2 at all four heights 0, 1, 2 and 3, so height levels do not map injectively to residue classes. Its residue sets by height are `{2,3}`, `{2,3}`, `{1,2,3}` and `{1,2,3,4}`.

**Assessment.**

- **What the law would give.** `B ≤ q − 1` is a statement for every denominator. At `q = 1` it forces `B = 0`, which is narrow, then mechanical, then trivial (C004 and R71). It is the kind of rung-1 spectrum law the goal asks for, and its `q = 1` case is exactly the ordered-cycle intermediate target.
- **How strong the evidence is.** The census is consistent with the law, with margin 3/4 at the extreme. Most census cycles have small `B`, and the law is trivially weak for large `q`. The binding cases are small `q` with large `B`. The two `q = 5` period-17 cycles are the only near-tight data.
- **The two exact obstructions are valuable.** Modular cancellation erases heights, and the pairwise relaxation allows unbounded `B`. Together they show that any proof must couple `D | C_h` with *integrality and all rank inequalities at once*, which is main's stated next step. Neither obstruction is a counterexample to the law.
- **Next step.** I have no dispute. The highest-value next test is still `B ≤ 1` at `q = 1`, that is, every nontrivial Collatz cycle has `H ≥ 4L` (02:13 entry). It is the first case of the law that would be new.

```sh
python3 sidekick/probes/c007_height_check.py <path to main's actual_cycles.json>   # <1 s, PASS
```

---

## 2026-10-19 02:13 — REFEREE C005 + C006 (main `1cb02fa`): reproduced; the dyadic-order mechanism is the first cycle ingredient that is genuinely specific to `q = 1`

**Reproduced** (`c005_c006_order_check.py`, under a second, PASS).

- **C005's rotation-block theorem.** Take any primitive mechanical base `v ≠ (2)` with coprime totals and `2^A0 > 3^m0`. Every concatenation of rotations of `v` has `den > 1`. I tested 1,020 concatenations of 2 to 6 randomly phased blocks over 17 bases, with no exceptions.
- **The `q = 1` order lemma.** An inversion between normalised states needs `3r < q(2^k − 1)` with `r ≥ 1` odd. At `q = 1` that forces `k ≥ 3`. So a `q = 1` cycle with `H < 8L` has no inversions: its normalised successor is a rank rotation.
- **C005's controls, on the census.**
  - All 15 normalised `q = 233` cycles of period 8 have cancellation 7, strict order and rank shift 5. Main's report mentions one of them.
  - Both `q = 5` cycles of period 17 (minima 187 and 347) have cancellation 1,015,513, strict order and rank shift 10.
  - The `q = 11` cycle with minimum 13 has an inversion despite `H < 8L`, and `gcd(A, m) = 2`. This is exactly why the lemma needs `q = 1`.
- **C006's worked example.** The `q = 233` cycle `1663 → 2611 → 4033 → 3083 → 4741 → 1807 → 2827 → 4357` has valuations `(1,1,2,1,3,1,1,3)`, `B = 1` and `J = 3`. The rational bound gives `q > 208768/14501`, so `q ≥ 15`.
- **C006's bound on every ordered census cycle.** All 50 normalised cycles that are ordered and have `q ≤ L` satisfy `L > 2^(⌈m/J⌉ − 1 − B)` and `B + 1 ≤ J`.
- **C006's controls.**
  - The ordered `q = 13` cycle `(227, 347, 527, 797, 601)` has minimum odd part 15 among the pairwise differences of its height-scaled numerators, matching main's "minimum odd gap 15". The smallest difference is `694 − 454 = 16·15`.
  - The `q = 5` cycle `19, 31, 49` is confirmed.

**Update 02:19: a second independent check.** The Lean lane re-derived C005 and C006 by hand and found no error. Its checks:

- **C005.** The inversion formula, the order lemma and its converse under `q ≤ L`, the three-band `q = 1` statement, the rotation-block `R³ < 8` bound and the `R71` reduction.
- **C006.** The weighted identity `D·L = q·C_h`, `J ≥ B + 1`, the gap system with its seam, sparse forcing, and the one-defect `q = 233` numbers (`C_h = 13349`, `gcd(13349, 1631) = 7`). The imported Bugeaud corollary was not checked at the source; main labels it as imported.
- **A structural remark.** C005's order lemma uses only two properties of the images `F_i`: strict monotonicity in the normalised state, and the factor-two window `F_i < 2F_j`. Everything else is C004's rank-count argument, which is already formal.
- **Lean plan.** The lane is generalising its `NarrowCycle` structure to exactly those hypotheses, as C005-a. It lists C005-b (the `q = 1`, `H < 8L` theorem on actual integer cycles), C005-c (the `R³` bound) and C006-a (the elementary gap argument) as later targets.

**Update 02:22: Lean C005-a is VERIFIED** (`4715715`).

- **The generalised structure.** `NarrowCycle` now carries exactly C005's order-lemma hypotheses:
  - images `F` with `x i < x j ↔ F i < F j`;
  - the window `F i < 2·F j`;
  - the exponent bounds `2^q·lo ≤ F i < 2^(q+2)·lo`.
- **What is machine-checked on it.** The rank shift, `rank i = (rank 0 + ih) mod m`, the mechanical letter formula, `gcd(h, m) = 1` and `A = mq + h`. These now hold for every ordered, dyadically normalised cycle. C004's constant-offset case, `F = 3C + D`, is an instance.
- **Also formal.** `inversion_formula` is C005's (2), an identity over ℚ. `no_inversion_of_le_two` is the three-band arithmetic: for `k ≤ 2` and `r ≥ 1`, `3r ≥ 2^k − 1`, with equality only at `(k, r) = (2, 1)`.
- **Receipts.** Of 128 declarations, 93 use the standard three axioms; the helpers use subsets. The build has no diagnostics, a source scan is clean, and the sha256 `cd57b972…` matches.
- **Next.** C005-b instantiates this on actual integer cycles at `q = 1` with `H < 8L`.

**Update 05:24: Lean C005-c is VERIFIED** (`08bf5fb`). This is the abstract core of C005's rotation-block theorem.

- **The interval lemmas.** These include the affine prefix comparison, `block_preserves`, `fixed_point_mem` (which needs only slope below 1), `blockComp_mem` and `cycle_point_mem`.
- **The ratio bound.** `state_bound` puts every mixed-cycle state in `[l/R, R·h]`, and `ratio_bound` gives `H/L ≤ R³`.
- **The gcd bookkeeping.**
  - `gcd_flatten_rotations`: `gcd(A, m) = r` for a concatenation of `r` rotations of a coprime base.
  - `blocks_identical`: if the word is a power `z^p` and `z` has coprime totals, then `p = r` and every block equals `z`.
- **Receipts.** 243 declarations use the standard three axioms; the helpers use subsets. The build has no diagnostics, a source scan is clean, and the sha256 `10004222…` matches.
- **Not yet formal.** Wiring these into actual words: the prefix maps as affine maps and the mechanical states in `[l, h)`. Also the final step through R71's `g = 1`, which is the lane's next unit. Once that lands, `H > 2L` for every nontrivial Collatz cycle becomes fully formal.

**Update 06:17: Lean C005-d is VERIFIED** (`6136784`). This is R71 §1 as a constructor: every positive word gives an integer `3x+q` cycle at its reduced parameter.

- **The constructor.** `ofWord` takes a word `w` with positive letters and `D_w > 0`, rotated to a minimal intercept. It builds an `OddCycle` with `g = gcd(C_w, D_w)`, states `n_i = C(w.rotate i)/g`, letters `a_i` (the first letter of `w.rotate i`) and parameter `q = D_w/g`.
- **The interface lemmas.**
  - `gcdCD_mul_ofWord_n` and `gcdCD_mul_ofWord_q` recover `C(w.rotate i)` and `D_w` from `g`.
  - `ofWord_coprime`: the cycle is reduced, `gcd(q, n_0) = 1`.
  - `ofWord_primitive`: distinct rotated intercepts give distinct states.
  - `ofWord_word`: the cycle's chronological word is `w` again.
- **Statement match.** It matches R71 §1:
  - each `B_i` is odd;
  - (1) gives the exact valuations;
  - `gcd(B_i, D)` does not depend on `i`;
  - multiplying by `d = D/gcd` gives an integer `S_d` cycle.
- **What the build checks.** The fields `nper`, `nmin`, `arrow` and `hB` are discharged in the build; I read their proofs: `rotate_mod`, division by `g > 0`, `quot_arrow`, and a `Finset.sup` over one period. `q` being coprime to 6 is not stated, but it is immediate.
- **Receipts.** Of 347 declarations, 278 use the standard three axioms, 28 use `[propext, Quot.sound]`, 40 use `[propext]` and 1 uses none. A source scan is clean, and the sha256 `fd4c7e3c…` matches. **The build receipt now binds to the file.** It records the source sha256, the toolchain (`lean4 v4.35.0-rc2`, Mathlib `0653561`) and the UTC build time, and the axioms receipt is headed by the same sha256.
- **Independent check.** `c005d_ofword_check.py` uses 38,852 random positive words (`m ≤ 14`, letters 1 to 5); 4,559 of them have `g > 1`. On every word, `g` divides every rotated intercept and the states are positive odd integers with `n_0` the minimum. The exact arrows hold with `a_i = v2(3n_i + q)`, and `gcd(q, n_0) = gcd(q, 6) = 1`.
- **What it enables.** C004-c/d, the three-band theorem and the `OrdCycle` machinery now apply to the cycle of any positive word. The lane plans to assemble C005 §2(b), the rotation-block exclusion, next. Two pieces are still missing: a `returnCycle` that keeps a general `B`, and the wiring of `state_bound` to actual prefix maps.

**Update 06:30: Lean C005-e is VERIFIED** (`a7dcac0`). This is the repetition bookkeeping for the rotation-block exclusion.

- **The repetition identities.**
  - `D_rep`: `D(z^k) = D(z)·G(2^Σz, 3^|z|, k)`, using C001's `G`.
  - `C_rep_mul_D`: `C(z^k)·D(z) = C(z)·D(z^k)`. This is R71 §2's "the fixed point is unchanged by repetition", in cleared form, with no slope hypothesis.
  - `D_dvd_C_of_rep_dvd`: if `D(z^k) ≠ 0` and `D(z^k) | C(z^k)`, then `D(z) | C(z)`. So denominator 1 for a power gives denominator 1 for the base.
- **The period bookkeeping.**
  - `returnCycleB`: the cycle on a return time of the minimum, keeping `B`. This is the general-`B` `returnCycle` that the 06:17 update listed as missing.
  - `a_add_of_return`: letters are periodic along a return time.
  - `least_period_dvd`: the least return time divides `m`.
  - `word_eq_rep`: the word is the `m/p`-fold power of one least period.
- **Statement match.** It matches R71 §2's repeated-case remark and C005 §2's period bookkeeping.
- **Receipts.** Of 357 declarations, 284 use the standard three axioms, 29 use `[propext, Quot.sound]`, 43 use `[propext]` and 1 uses none. A source scan is clean. The sha256 `f263ea5b…` matches all three receipts, and the build receipt binds to it.
- **Independent check.** `c005e_rep_check.py` checks both identities on 180,000 random cases (letters 0 to 5, `k ≤ 6`); 11,856 integral powers all descend to an integral base. It also checks the least-period facts on 64 multiply-listed actual cycles at `q = 1, 5, 7, 13, 61`.
- **Still open for the exclusion.** Rotation of a power, identification of the blocks, the conditional assembly under `B ≤ 2`, and the `state_bound` wiring.

**Update 06:40: Lean C005-f is VERIFIED** (`cf7865c`). This is the last bookkeeping before the rotation-block assembly.

- **The declarations.**
  - `rep_rotate`: `(z^k).rotate u = (z.rotate u)^k` for every `u`.
  - `exists_min_rotation`: every word has a rotation starting at its minimal intercept.
  - `gcdCD_eq_D_of_dvd`, `ofWord_q_eq_one` and its converse: the reduced parameter of `ofWord w` is 1 exactly when `D_w | C_w`.
  - `ofWord_B_le_two`: if every rotated intercept is below `8C_w` (`H < 8L`), then `B ≤ 2`.
  - `coprime_least_period`: at `q = 1` with `B ≤ 2`, the least period has coprime totals. For `p ≥ 2` this is `three_band` on `returnCycleB`; `p = 1` is handled separately.
- **Statement match.** Each piece is one clause of C005 §2's rotation-block proof or of R71 §1.
- **Receipts.** Of 369 declarations, 293 use the standard three axioms, 30 use `[propext, Quot.sound]`, 44 use `[propext]` and 2 use none. A source scan is clean, and the sha256 `cbd41abd…` matches all three binding receipts.
- **Independent check.** `c005f_bookkeeping_check.py` verifies:
  - `rep_rotate` on 468,348 cases, including the empty word and `k = 0`;
  - the `q = 1 ⇔ D | C` criterion on 37,836 minimal-rotation words;
  - `B ≤ 2` on the 24,032 of them with `H < 8L`.
- **What remains for the exclusion.** The conditional assembly under `H < 8L`, then the `state_bound` wiring that discharges that hypothesis.

**Update 06:50: Lean C005-g is VERIFIED** (`1166d1b`). C005's rotation-block exclusion is machine-checked, **conditional on the `8L` hypothesis**.

- **The theorem.** `rotation_block_exclusion` takes a primitive mechanical base `v = mech A₀ m₀ l₀` with `m₀ ≥ 2`, `A₀ ≥ m₀` and `gcd(A₀, m₀) = 1`. Let `w` be any concatenation of `r ≥ 1` rotations of `v`, in any order and with repetitions, with `D_w > 0`. If every rotated intercept of `w` is below 8 times every other (`H < 8L`), then `D_w ∤ C_w`: the reduced denominator exceeds 1.
- **The proof chain.** Every step is a lemma verified earlier:
  - rotate `w` to its minimum and form `ofWord`, which has `q = 1` and `B ≤ 2`;
  - take the least period, which has coprime totals, so `w = (z.rotate u)^k`;
  - `blocks_identical` makes every block one phase of `v`;
  - `D | C` descends to that block, where R71-a and `mech_D_ne_one` exclude it.
- **Statement match.** It matches the second half of C005 §2's rotation-block theorem.
  - The prose derives `H < 8L` from the ratio bound `H/L ≤ R³ < 8`; the Lean theorem takes it as the explicit hypothesis `h8`.
  - `D_w > 0` is a hypothesis, as in the prose.
  - `m₀ ≥ 2` excludes the base `(2)`, as the prose does.
- **Receipts.** Of 371 declarations, 294 use the standard three axioms, 31 use `[propext, Quot.sound]`, 44 use `[propext]` and 2 use none. A source scan is clean, and the sha256 `5b3012ab…` matches all three binding receipts.
- **Independent check.** `c005g_rotation_block_check.py` reproduces C005's worked example: `w = (1,2,2,2,2,1)` has `C = 1805`, `D = 295` and gcd 5, giving reduced denominator 59, and its `3x+59` cycle has numerators `(361, 571, 443, 347, 275, 221)`. It also tests 3,515 random concatenations (`m₀ ≤ 12`, `r ≤ 6`):
  - the hypothesis `h8` always holds, since `H/L ≤ R³ < 8` with largest observed ratio 4.23;
  - `D_w ∤ C_w` holds every time.
- **The `d`-control.** The worked example is a genuine `3x+59` cycle, so the exclusion is specific to `d = 1`.
- **Status.** This is the programme's second complete `d = 1` exclusion, after C004. It now rests only on the unformalised ratio bound. That step is to identify actual states with C005-c's prefix maps so that `ratio_bound` discharges `h8`, and it is the lane's next unit. It is a restricted class, not a general exclusion.

**Assessment.**

- **This is the first `d = 1`-specific lever in the cycle programme.**
  - Every earlier cycle result was arithmetic of words, valid for all denominators. C005's inversion lemma uses `q = 1` (more precisely, small `q` relative to the height gap), and the `q = 11` control shows it fails without that.
  - Combined with C004, it gives a ladder of structure for hypothetical Collatz cycles. Below `2L` the pattern is mechanical, which is excluded. Below `8L` it is ordered, with mechanical normalised exponents. That case is not excluded, because the height weights can cancel, as the `q = 233` and `q = 5` controls show.
- **C006 restricts complexity; it does not exclude.** With Baker's two-logarithm bound, an ordered cycle at fixed `q` needs `J ≥ √m − O_q(log m)` height changes, and `(q, J)` bounded gives finitely many cycles. It is effective in principle, but it is not an exclusion.
- **A next fixed rung.** Prove that every nontrivial Collatz cycle has `H ≥ 4L`. That is the `B ≤ 1` case of main's ordered-cycle target. Such a cycle is ordered by C005, and its heights are only 0 or 1, so the weighted intercept has the simplest possible structure. Main's "one-defect profiles" probe is the natural first step.

```sh
python3 sidekick/probes/c005_c006_order_check.py <path to main's actual_cycles.json>   # <1 s, PASS
```

---

## 2026-10-19 02:11 — VERIFIED Lean C004-b (`claude/lean-lane` `8db3feb`): C004's narrow-cycle classification is machine-checked in both directions

**`is_mech_of_narrow`.** Take a word `w` with `m ≥ 2`, `D_w > 0`, `C(w.rotate i) < 2·C(w.rotate j)` for all `i, j`, and distinct rotated intercepts. Then `w = mech(w.sum, m, l)` for some phase `l < m`, and `gcd(w.sum, m) = 1`.

- **Statement match.** C004 §1 assumes a primitive positive rational cycle with `m` distinct odd states and `H < 2L`. With states `C_i/D` sharing one `D > 0`, `H < 2L` is exactly `C_i < 2C_j`, and distinct intercepts are exactly distinct states. The conclusion, a rotation of the mechanical word with coprime totals, is the phase-word statement, since `mech_rotate` shows rotations are phases.
- **Positivity.** Letter positivity is not assumed; it follows from `D_w > 0`.
- **The proof.** The abstract `NarrowCycle` is instantiated on rotations (`ofWord`), rotated to the minimal state, and then `a_formula`, `mech_sum` and `coprime_numHigh` are applied.

**Receipts.**

- **Axioms.** Of 122 declarations, 90 use the standard three, 10 use `[propext, Quot.sound]`, 21 use `[propext]` and 1 uses none.
- **Build.** No diagnostics.
- **Source scan.** No `sorry` or `native_decide`.
- **Hash.** The sha256 `19b74f4d…` matches the receipt.

**Status.** With `narrow_mech` from C004-a, **"narrow ⇔ mechanical" is formal**. The integer corollary, that every nontrivial Collatz cycle has `H > 2L`, now needs only R71's `g = 1` for primitive mechanical words. The lane lists that as a candidate next unit.

**Update 05:44: Lean R71-a is VERIFIED** (`09d4319`). R71's exact denominator for primitive mechanical words (`BALANCED_DENOMINATORS.md` §2) is machine-checked.

- **The theorems.**
  - `gcd_rotate_eq`: `gcd(C, D)` is the same for every rotation of a word with positive total.
  - `exists_unique_mech_jump`: for `gcd(A, m) = 1` there is exactly one `j < m` with `m | jA + 1`.
  - `C_mech_one_sub_zero`: R71's (4), `C(phase 1) − C(phase 0) = 3^(m−1−j)·2^⌊jA/m⌋`.
  - `mech_gcd_one` and `mech_gcd_one_phase`: for `m ≥ 2`, `A ≥ m` and `gcd(A, m) = 1`, every phase word has `gcd(C, D) = 1`. So its reduced denominator is exactly `D = 2^A − 3^m`.
  - `mech_D_ne_one`: `2^A − 3^m ≠ 1` for `m ≥ 2` and `A ≥ m`, by the modulo-8 argument.
- **Statement match.** It matches R71 §2's primitive case, which writes `k` for `m`. Two hypotheses differ from the prose, both harmlessly.
  - The Lean statement does not assume `2^A > 3^m`; the gcd claim does not need it.
  - `A ≥ m` is not needed in `mech_D_ne_one`, since `2^A − 3^m = 1` has only the solutions `(A, m) = (1, 0)` and `(2, 1)`. For a cycle, `D > 0` gives `A > m` anyway.
- **Receipts.** Of 312 declarations, 248 use the standard three axioms, 26 use `[propext, Quot.sound]`, 37 use `[propext]` and 1 uses none. The build has no diagnostics. A source scan finds no `sorry`, `native_decide`, `axiom` or `implemented_by`. The sha256 `56ba1e1d…` matches the receipt.
- **Independent check.** `r71a_mech_gcd_check.py` uses exact arithmetic and the recursive `C`.
  - `gcd(C, D) = 1` holds on all 16,887 phase words with `m ≤ 40`, `m ≤ A ≤ 2m + 7` and `gcd(A, m) = 1`.
  - (4), with a unique and nonzero jump index, holds on all 669 such `(A, m)` with `m ≥ 2`.
  - `mech_rotate` holds on 849,520 cases, and the gcd is rotation invariant on 19,569 random words.
  - **Control: coprimality is necessary.** For `g = gcd(A, m) > 1` and `D > 0`, all 6,109 phase words have `gcd(C, D) = D/(2^(A/g) − 3^(m/g)) > 1`. This is R71's (3) in the repeated case. For example, `(m, A) = (6, 10)` has `D = 295` and reduced denominator 5.
- **Not formal.** The repeated case; the one-letter case `m = 1`, where `C = 1` and an integer cycle needs `A = 2`, the fixed point 1; and §3's lower bound. R71 itself claims no novelty.
- **Correction to the status line above and to the C005-c update at 05:24.** Both said R71's `g = 1` was the only missing piece for "every nontrivial Collatz cycle has `H > 2L`". One more step is needed: the bridge from an actual `q = 1` cycle with all states in `[L, 2L)` to a mechanical word with `D | C`, including the case `m = 1`. The Lean lane has queued it as C004-c. With it, C004-b, R71-a and `mech_D_ne_one` close the chain. C005's rotation-block chain still needs the wiring listed at 05:24.

**Update 08:31: Lean R71-b is VERIFIED** (`c0db6af`). R71's theorem (3) is now formal in full, including the repeated case.

- **The theorem.** `den_mech`: for `0 < k ≤ A` and any phase `l < k`, `den(mech A k l) = 2^(A/g) − 3^(k/g)`, where `den(w) = D_w/gcd(C_w, D_w)` and `g = gcd(A, k)`.
- **The supporting lemmas.**
  - `gcdCD_rep` and `den_rep`: `C` and `D` both scale by `G_k > 0` under repetition, so the denominator is unchanged.
  - `mech_rep`: `mech(gA₀, gk₀, gh+r) = mech(A₀, k₀, h)^g`.
  - `mech_gcd_one_phase'`: R71-a extended to `k₀ = 1`.
- **Statement match.** It matches R71 §2's theorem (3), with both of the prose's steps formal. The fixed-point argument is replaced by the scaling of `C` and `D`. The formula needs no `2^A > 3^k`; the prose assumes it only to make the cycle positive. Still informal in R71 are the state bound `x > k/6` and the `3x+d` transport remarks.
- **Receipts.** Of 420 declarations, 337 use the standard three axioms, 37 use `[propext, Quot.sound]`, 44 use `[propext]` and 2 use none. A source scan is clean, and the sha256 `af06a190…` matches all three binding receipts.
- **Independent check.** `r71b_den_mech_check.py` verifies `den = 2^(A/g) − 3^(k/g)` from `C` and `D` directly on every phase word with `k ≤ 48`:
  - 8,232 words with `D > 0`, using the seven totals from `⌈k log₂ 3⌉`;
  - 22,828 words with `D < 0`, with `k ≤ A < k log₂ 3`.
  - It also checks `mech_rep` and `den(z^k) = den(z)` on 3,000 random cases, and R71's example `(6, 10)`: `D = 295`, `den = 5`.

**Update 08:39: Lean R71-c is VERIFIED** (`80ec685`). R71 §3's state bound (5) is now formal.

- **The theorems.**
  - `mech_state_bound`: if `0 < k` and `3^k < 2^A < 2·3^k`, then `k·D < 6·C` for every phase. So every state of the mechanical cycle exceeds `k/6`.
  - `exists_total`: `A = bit length of 3^k` satisfies the hypothesis.
  - `mech_cycle_state_bound`: the reduced integer `3x+q` cycle has every state `n_i > kq/6`. This is R71's "the integer `S_d` cycle has every state `> Cd`".
- **Statement match.** It matches R71 §3, (5) and its corollary. The proof replaces the prose's per-term real estimate with an integer `k`-th-power comparison; the strictness still comes from `D < 3^k`.
- **Receipts.** Of 428 declarations, 344 use the standard three axioms, 37 use `[propext, Quot.sound]`, 45 use `[propext]` and 2 use none. A source scan is clean, and the sha256 `82ee7c35…` matches all three binding receipts.
- **Independent check.** `r71c_state_bound_check.py` covers `k = 1…80` with `A` the bit length of `3^k`.
  - `6C > kD` holds for every phase, and `6n_i > kq` for every state of the reduced cycle.
  - **The bound is loose.** The smallest state is between 2.07 and 127 times `k/6`; the slack is large when `D ≪ 3^k`.
- **Threshold remark (the Lean lane's, confirmed).** R71 says "for `k > 6`, `d > 1`". The true threshold is `k ≥ 3`. By `den_mech` and `mech_D_ne_one`, `den = 1` forces `A = 2k`, and `2^(2k) < 2·3^k` fails for `k ≥ 3`. The probe finds `den = 1` exactly at `k = 1, 2`, the words `(2)` and `(2,2)`.
- **Status.** With R71-a/b/c, R71 §§1–3 are formal except the `d > 1` remark and the `3x+d` transport notes. R71's own status is unchanged: a restricted control family with published antecedents.

**Update 08:47: Lean R71-d is VERIFIED** (`3faa040`). The `d > 1` remark is now formal at its exact threshold.

- **The theorem.** `den_mech_gt_one`: for `k ≥ 3` and `3^k < 2^A < 2·3^k`, every phase has `den(mech A k l) > 1`. When `k/g ≥ 2` this follows from `den_mech` and `mech_D_ne_one`. When `k/g = 1`, `den = 1` would force `A = 2k`, which `4^k ≥ 2·3^k` rules out.
- **Independent check.** `c006b_erun_check.py` finds `den > 1` for every phase for `k = 3…80`, and `den = 1` only at `k = 1, 2`.
- **Status.** R71 §§1–3 are now formal except the `3x+d` transport remarks of §0.

---

## 2026-10-19 01:39 — VERIFIED Lean C004-a (`claude/lean-lane` `7959806`): C004's cut identities and the "mechanical ⇒ narrow" direction are machine-checked

**The theorems.**

- **`cut_identity` and `cut_gcd`.** These are C004's (6) and (7) for a one-letter cut: `gcd(D_w, K) = g·gcd(D_w/g, 2^a − 3)`.
- **Mechanical words.** `mech A m l` is the phase-`l` mechanical word `⌊((j+1)A + l)/m⌋ − ⌊(jA + l)/m⌋`. The lane proves its length, its total, its `D` and its positivity.
- **`C_diffWord` / `C_mech`.** These recover R71's closed sum `Σ_j 3^(m−1−j) 2^⌊(jA+l)/m⌋` from the recursive `C`.
- **`mech_rotate`.** Every rotation of a phase word is again a phase word.
- **`narrow_mech`.** Every rotation has `C_0 ≤ C_i < 2C_0` with the common `D`, so every mechanical cycle has all its states in `[L, 2L)`. This is the reverse direction of C004 §1. It needs no coprimality: `gcd(A, m) = 1` only makes the rotations distinct.
- **The `d5` control.** `mech 5 3 0 = (1,2,2)`, with intercepts 23, 37 and 29 for its rotations.

**Checks.**

- **Statement match.** It matches C004 (6), (7) and the reverse direction of §1.
- **Axioms.** Of 75 declarations, 51 use the standard three. The helpers use subsets: 7 use `[propext, Quot.sound]`, 16 use `[propext]`, and 1 (`diffWord_zero`) uses no axioms.
- **Build.** No diagnostics.
- **Source scan.** No `sorry` or `native_decide`. The `decide` uses are small numeric facts and list rotations.
- **Hash.** The sha256 `3226ae0c…` matches the receipt.

**Update 01:55: C004-b part 1 is VERIFIED** (`5be60e6`). These are the first lemmas of the forward direction.

- **The lemmas.**
  - `C_rotate_succ`, the cyclic recursion on rotations.
  - `exists_exponent` and `exponent_dichotomy`: in a narrow cycle every exponent is `q` or `q+1`.
  - The successor-order lemmas: every high-exponent successor lies below every low-exponent successor.
  - On an abstract `NarrowCycle` structure (periodic states in `[lo, 2lo)`, exact arrows, `d > 0`), the rank-shift lemmas `rank_succ_of_low`, `rank_of_high` and `high_iff_rank`.
- **Proof design.** The ranks are counted, with no sorting or permutations. Part 1 uses neither primitivity nor `gcd(A,m) = 1`.
- **Receipts.** Of 103 declarations, 73 use the standard three axioms, 9 use `[propext, Quot.sound]`, 20 use `[propext]` and 1 uses none. The build has no diagnostics, a source scan is clean, and the sha256 `bc20673f…` matches.
- **Next.** Part 2 turns the rank shift into `rank i ≡ rank 0 + ih (mod m)` and `gcd(h, m) = 1`. It then identifies the word as `mech(mq + h, m, l)`.

**Update 02:02: C004-b part 2 is VERIFIED** (`692fd04`). These results are proved on abstract narrow cycles.

- **The rank formula.** `rank_formula`: `rank i = (rank 0 + ih) mod m`.
- **Primitive cycles.** Here `Primitive` means distinct states over one period.
  - `numHigh_pos` and `numHigh_lt`: for a primitive cycle with `m ≥ 2`, the number of high steps satisfies `1 ≤ h ≤ m − 1`.
  - `coprime_numHigh`: `gcd(h, m) = 1`.
- **The letter formula.** `a_formula`: started at the minimum, `a_i = q + ⌊(i+1)h/m⌋ − ⌊ih/m⌋`.
- **The total.** `sum_a`: `A = mq + h`.
- **Receipts.** Of 118 declarations, 87 use the standard three axioms; the helpers use subsets. The build has no diagnostics, a source scan is clean, and the sha256 `eab32a83…` matches.
- **Next.** Part 3 instantiates this on actual words, `x_i = C(w.rotate i)`, to close "narrow primitive ⇒ mechanical". The integer corollary `H > 2L` will still rest on R71's `g = 1`.

**Not yet formal.** The forward direction "narrow ⇒ mechanical" (queued as C004-b), R71's `g = 1`, the integer corollary `H > 2L`, the narrow spectrum law, and the Smith-form statements.

---

## 2026-10-19 01:19 — VERIFIED Lean C003-a (`claude/lean-lane` `8388c38`): C003's effective bounds are machine-checked as pure algebra; the Lean lane also confirms C004

**The theorems.** `CycleSpectrum.lean` adds 13 new declarations.

- **`fixed_pair_bound_u` and `fixed_pair_bound_v`.** For `D_u, D_v > 0` and `K ≠ 0`, `Q^k·D_v·gcd(C_w, D_w) < |K|·D_w`, and symmetrically. The proof never refers to integer cycle states.
- **`uniform_bound_u`, `uniform_bound_v` and `uniform_bound_max_u`.** This is C003's (6). Take contracting blocks with `K ≠ 0`, block `u` attaining `Q*`, `k ≥ 3` and `ℓ ≥ 1`. Then `2^max(m_u, m_v) · Q*^(k−3) · gcd < D_w`. I read the statement: block `u` is nonempty because `D_u > 0`.
- **The supporting intercept bounds.** `two_pow_mul_C_lt`, `K_bound` and the others.
- **The worked example.** `(1,2,2)^3 (2)` has `C = 213341`, `D = 72023`, gcd 1, stated as an `example`.

**Checks.**

- **Statement match.** It matches C003 §2 with its stated hypotheses. The tie `Q_u = Q_v` is covered by either lemma.
- **Axioms.** Of the 51 declarations, 39 use the standard three, 3 use `[propext, Quot.sound]` and 9 use `[propext]`.
- **Build.** No diagnostics.
- **Source scan.** Clean.
- **Hash.** The sha256 `651c8d08…` matches the receipt.
- **Not formalised.** The effective enumeration (10), the proportional comparison of §4, the Corvaja–Zannier branch and the `d = 499` example.

**The Lean lane's C004 read, re-derived by hand: no error.** It covers `det B_w = ±D`, the Smith argument via Cramer minors, the cut identity and gcd formula, both directions of the narrow theorem, the letter-1 lemma and the `d5` control. Its notes:

- **The cut identity is not new algebra.** C004's identity (6) is C001's commutator at `k = 1`, which is already formal.
- **The next unit.** The reverse narrow direction, plus (7), is next for formalisation (C004-a). Each summand of `C_l` is 1 or 2 times the matching summand of `C_0`. The forward direction (C004-b) is a larger combinatorial unit. Smith normal form is thin in Mathlib, so the Smith statements are not a near-term target.
- **A label for citations.** The integer conclusion "`H > 2L` for every nontrivial `d = 1` cycle" rests on R71's `g = 1` for primitive mechanical words. That is a written proof, not yet formalised. Everything else in C004 is elementary.

---

## 2026-10-19 01:06 — REFEREE C004 (main `61cf54a`): narrow cycles are exactly mechanical, reproduced on a different grid; the narrow spectrum law matches the census exactly

**Reproduced** (`c004_narrow_check.py`, about 3 s, PASS).

- **The narrow-cycle theorem.** Here `H` and `L` are the largest and smallest odd states of a cycle. I tested every primitive word with `D > 0` of length 1 to 7 and entries 1 to 5: 97,020 words, a different grid from main's 1–8 × 1–4.
  - `H < 2L` holds exactly when the word is a rotation of the mechanical word `⌊(j+1)A/m⌋ − ⌊jA/m⌋`. 311 words are narrow.
  - Every narrow cycle with `m > 1` has `gcd(A, m) = 1` and **no cancellation**, so `den = D`.
- **The narrow spectrum law across `d` (rung 1), checked against data.** There are 19 coprime pairs `(A, m)` with `0 < 2^A − 3^m ≤ 999`.
  - For every `d ≤ 999` coprime to 6, the law predicts one narrow cycle per pair with `D | d`.
  - All 551 predicted cycles with minimum `≤ 5000` appear in C001's census.
  - Every narrow cycle in the census is predicted. The match is exact in both directions.
- **The cut formula.** `gcd(D, K_i) = g·gcd(D/g, 2^(a_i) − 3)` holds for every one-letter cut of 3,000 random words.
- **Controls.**
  - The `d5` cycle `19 → 31 → 49` has normalised minimum gap `12/5 > 2`.
  - The `d13` mechanical cycle, word `(1,2,1,2,2)`, has numerators `319, 367, 421, 485, 557`, with ratio below 2.

**Assessment.**

- **What is proved.** C004 converts the mechanical-word theory (R71) into an intrinsic geometric statement: **every nontrivial integer Collatz cycle has `H > 2L`.** It also gives a complete, data-verified law for the narrow part of the `3x+d` spectrum. Rung 1 is met for narrow cycles. Novelty is undetermined; the exclusion itself follows from R71 once the classification is proved.
- **What it shows.** The all-rotation dependence result is a useful negative. Making every rotation integral gives exactly one condition, so the rotation congruences carry no extra information. The close-pair counterexamples are also useful, and correct.

**On main's assessment of my 00:26 bounded-discrepancy lead: correction accepted.** Excluding cycles for *every* discrepancy ceiling `Δ` is the headline, so "for all `Δ`" is not a smaller criterion. The intended milestones were the fixed-`Δ` cases, and C004 is the first of them: `H < 2L` amounts to discrepancy below 1, the mechanical words. The next fixed case is cycles spanning two dyadic ranges, `H < 4L`. That is the "order across different dyadic ranges" which main's report names as its next mechanism. The discrepancy estimate also carries an additive term `m/(3 x_min ln 2)`, as main notes. That term is negligible only for cycles beyond the verified range.

```sh
python3 sidekick/probes/c004_narrow_check.py <path to main's actual_cycles.json>   # ~3 s, PASS
```

---

## 2026-10-19 00:48 — REFEREE C003 (main `7270d95`): the effective contracting theorem is reproduced; the asymptotic theorem is ineffective by design; still a two-block class

**Reproduced** (`c003_variable_blocks_check.py`, about 3 s, PASS).

- **The effective contracting theorem (§2).** Take `D_u, D_v > 0` and `K ≠ 0`. Suppose the block attaining `Q* = max 2^(sum)` occurs `t* ≥ 3` times and the other at least once. Then `den(u^k v^ℓ) > 2^(m*) · Q*^(t*−3)`. Lengths, totals and slopes may all differ. It holds in every one of:
  - 142,144 exhaustive eligible cases (all 76 contracting words of length `≤ 3` with entries `≤ 4`, counts `≤ 6`);
  - 3,000 random eligible cases (length `≤ 7`, entries `≤ 5`).
- **Worked example.** `(1,2,2)^3 (2)` has `C = 213341`, `D = 72023`, gcd 1, and the bound is 8.
- **The `d = 499` obstruction.** `(1)^4 (1,3)^3` has `D_u = −1`, so its first block expands. It has `K = −12`, `C = 85865`, `D = 6487`, `g = 13` and `den = 499`. I replayed the actual `3x+499` cycle through 6605 with exactly these valuations. The cycle start lies outside the interval between the block fixed points `−1` and `5/7`, so interval trapping genuinely fails for expanding blocks.
- **The integer lemma behind the proportional branch.** `5(Rk + Sℓ − gcd(Rk, Sℓ) + 1) ≥ 7(R + S)` holds for coprime `R, S ≤ 40` and `k, ℓ` from 2 to 14, 165,451 cases. Also `η = (5 log₃2 − 3)/14 = 0.0110463406`.

**Update 00:50: the Lean lane confirms §2 and both examples, and finds an algebraic route.** The lane re-derived §2 and both worked examples. It notes that the interval-trapping and lattice argument for (5) can be replaced by pure algebra already formalised. For `K ≠ 0` and `D_u > 0`, the bound is `Q^k · D_v · gcd(C,D) < |K| · D_w`, and similarly with the roles swapped. This needs only the commutator identity and `g | K·G_v(ℓ)`, with no appeal to integrality of cycle states. I tested this form on 142,050 contracting cases with `K ≠ 0` (lengths up to 3, counts up to 5): it always holds. The lane will formalise (5)–(6) in this form as C003-a.

**Not checkable here.** The uniform asymptotic theorem (§1) says `den ≥ 2^((η−ε)A)` beyond a threshold independent of the blocks. It rests on Corvaja–Zannier and is **ineffective**, as main says: it gives finiteness of each denominator layer but cannot exhibit the exceptions.

**Assessment.**

- **What it adds.** C003 removes C002's equal-shape restriction for contracting blocks, with no ineffective cutoff. That is a real strengthening at rung 2.
- **What stays the same.** The class is still "two repeated blocks". Main has, unprompted, redirected the next batch to "a restriction intrinsic to arbitrary cycle words, connecting their denominator to the sizes of their rotated cycle points". That is the direction of my 00:21 and 00:26 leads: size constraints, and bounded discrepancy for bounded-oscillation cycles.
- **The random-model lead now has a proof.** Main's `SIDE_REVIEW.md` gives an exact proof that the naive random-residue model diverges: `T(m) > 1/(2m)`, because the `m`-th head in fair tosses falls at or after time `2m` with probability exactly 1/2. That turns my numerical observation into a theorem about the model.

```sh
python3 sidekick/probes/c003_variable_blocks_check.py     # ~3 s, PASS
```

---

## 2026-10-19 00:45 — VERIFIED Lean C002-a (`claude/lean-lane` `cf15b22`): C002's uniform two-block exclusion is machine-checked

**`uniform_two_block`.** Let `u ≠ v` be nonempty words with positive entries, equal length `m` and equal total `A`, with `3^m < 2^A`. Let `k, ℓ ≥ 1` with `k + ℓ ≥ 3`. Then `2^m · gcd(C, D) < D` for `w = u^k v^ℓ`, that is, `den(w) > 2^m`. So no such word gives an integer Collatz cycle, uniformly in the blocks.

**Supporting results.**

- **Identities.** `C_two`/`D_two` give (1)–(2), and `commutator_two_u/_v` give (3)–(4).
- **`gcd_dvd_K_mul_gcd`.** This is (5), `gcd(C,D) | |K|·gcd(G_u(k), G_v(ℓ))`, with no coprimality or positivity premise.
- **`gcd_pow_sub_pow`.** This is strong divisibility: `gcd(U^i − V^i, U^j − V^j) = |U^gcd(i,j) − V^gcd(i,j)|` for coprime integers.
- **`C_injective`.** It uses the dynamics-free `v₂` recursion.
- **`two_pow_mul_C_le`.** This is (U2): `2^m C ≤ 2^A(3^m − 2^m)`.
- **`pow_sub_pow_lower`.** This is the geometric lower bound.

**Checks.**

- **Statement match.** It uses C002's hypotheses exactly.
- **One scope note.** The Lean conclusion is `den > 2^m`. Main's (U1) states the stronger `den > 2^m · 2^A/3^m`. Both exclude integer cycles. The formal statement is the weaker of the two bounds, and should be cited that way.
- **Receipts.**
  - **Axioms.** 20 declarations use the standard three. The 3 pure identities use only `[propext]`.
  - **Build.** No diagnostics.
  - **Source scan.** Clean.
  - **Hash.** The sha256 `5e547237…` matches the receipt.
- **Not formalised (queued as C002-b).** The general proportional theorem (6)–(8), the `K = 0` case, §3's sharpness identities and §4's family. The Corvaja–Zannier input is imported, not a target.

**Update 00:50: the full (U1) is now formal** (`325130a`). `uniform_two_block_strong` proves `2^A · 2^m · gcd < 3^m · D`, that is, `den > 2^m · 2^A/3^m`, under the same hypotheses. `uniform_two_block` (`den > 2^m`) is now its corollary.

- **Axioms.** 21 declarations use the standard three and 3 use only `[propext]`.
- **Build.** No diagnostics.
- **Hash.** The sha256 `a64b42e3…` matches the receipt.

The scope note above is closed.

**Calibration.** Both of the cycle goal's proved structural exclusions so far, C001's repetition bound and C002's uniform two-block theorem, are now machine-checked within hours of being written.

---

## 2026-10-19 00:32 — VERIFIED Lean C001-b (`claude/lean-lane` `0cde415`): the two-sided bound and the periodicity of C001 are machine-checked

**The theorems.** They are added to `CycleSpectrum.lean`. Both blocks are nonempty with positive entries.

- **`gcd_two_sided`.** This is C001's (7) with no coprimality premise. With `H = gcd(D_k, K)` and `e = gcd(H, |D_u|)`, it gives `H/e | gcd(C_k, D_k) | H`.
- **`gcd_periodic`.** This is (9) in hypothesis form.
  - Hypotheses: a factorisation `|K| = 2^a 3^b K₀`, and any `T` with `Q^T ≡ P^T ≡ 1 (mod K₀|D_u|)`.
  - Conclusion: `gcd(C_(k+T), D_(k+T)) = gcd(C_k, D_k)` for every `k`.
- **`gcd_periodic_totient`.** It gives the explicit period `T = φ(K₀|D_u|)` when `K₀` is coprime to 6.
- **`gcd_coprime_six`.** The cancellation factor is coprime to 6.

**Checks.**

- **Correctness of the hypothesis form.** It is correct for *any* such `K₀`. Each `g_k` divides `K` and is coprime to 6, so it divides `K₀`. The congruences `C_(k+T) ≡ C_k` and `D_(k+T) ≡ D_k (mod K₀)` follow from `D_u(G_(k+T) − G_k) = Q^k(Q^T − 1) − P^k(P^T − 1)`. So `g_k = gcd(C_k, D_k, K₀)` is periodic.
- **Totient version.** `D_u` is coprime to 6, so Euler's theorem gives the totient period.
- **Scope.** The lane's statement-match note records that `K₀` enters through the factorisation hypothesis, not as the exact prime-to-6 part.
- **Receipts.**
  - **Axioms.** 13 declarations use the standard three and 3 use only `[propext]`.
  - **Build.** No diagnostics.
  - **Source scan.** Clean.
  - **Hash.** The sha256 `99418d99…` matches the receipt.

**Status.** C001's algebra is now formal except the `K = 0` characterisation and §3's mechanical family. Next is C002-a.

---

## 2026-10-19 00:26 — REFEREE C002 (main `e14a4e3`): the uniform two-block exclusion is confirmed; plus a lead on the class real cycles must live in

**The uniform theorem: confirmed by hand and by exhaustive search** (`c002_two_block_check.py`, about 9 s, PASS).

- **Statement.** Let `u ≠ v` have equal length `m` and total `A`, with `2^A > 3^m`, and let `k + ℓ ≥ 3`. Then `den(u^k v^ℓ) > 2^m · 2^A/3^m`.
- **My derivation.** Write `U = 2^A`, `V = 3^m`, `G_t = (U^t − V^t)/(U − V)`, `n = k + ℓ`, `J = C_v − C_u` and `D = U − V`.
  - Then `C_w = C_u G_n + U^k J G_ℓ = C_v G_n − V^ℓ J G_k`.
  - So `g = gcd(C_w, D_w)` divides both `D·J·G_ℓ` and `D·J·G_k`, hence `D·J·G_(gcd(k,ℓ))` by strong divisibility.
  - This gives `den ≥ G_n/(|J| G_h) > U^(n−h)/|J|`.
  - With `|J| < UV/2^m` and `n − h ≥ 2`, the claim follows.
- **Checks.**
  - The inequality holds in every one of 434,350 exhaustive cases (`m ≤ 4`, `A ≤ 2m+2`, `k, ℓ ≤ 6`) and 3,902 random ones (`m ≤ 9`).
  - The ingredients hold: `0 < C_z ≤ 2^(A−m)(3^m − 2^m)`, distinct equal-shape words have distinct `C`, and the intermediate bound.
- **Exact examples.**
  - `den((1,1,3)^t (1,2,2)^t) = 5(32^t + 27^t)`, with cancellation `(32^t − 27^t)/5` growing past `K = 20`.
  - `den((1,3)^t (3,1)^t) = 7(16^t + 9^t)`.
  - Both hold for `t ≤ 40`.
- **The `3x+59` cycle.** The cycle `221 → 361 → 571 → 443 → 347 → 275` has word `(1)^2 (2)^4`, with `C = 1105`, `D = 295` and `g = 5 > |K| = 2`.
- **The rotating mechanical family.** For `13 ≤ m ≤ 30` and `k, ℓ ≤ 3`, `u_m^k v_m^ℓ` is primitive, every rational cycle state exceeds `m/12`, and `den > 1` once `k + ℓ ≥ 3`.

**Assessment.** The theorem is correct and elementary, and it is uniform over the contents of the blocks. That is a real step up from C001's fixed pattern, and it meets ladder rung 2. Its class is still structural, two equal-shape blocks repeated, and main states the remaining gap honestly. The unequal-slope part relies on Corvaja–Zannier, which is ineffective; main flags that too.

**Update 00:31: a second independent check.** The Lean lane re-derived `PROPORTIONAL.md` §§1–4 and the exact examples, and audited `INDEPENDENT_SLOPES.md`. It found no error.

- **A cleaner route to `J ≠ 0`.** The lane notes this route needs no dynamics: `C_z = 3^(m−1) + 2^(a₀) C_tail`, with `C_tail` odd, so `v₂(C_z − 3^(m−1)) = a₀` exactly when `m ≥ 2`. The first letter is therefore recoverable from `C`; recurse on the tail, with the last letter fixed by the total `A`. I checked `v₂(C − 3^(m−1)) = a₀` on all 19,525 words with `2 ≤ m ≤ 6` and letters `1–5`.
- **Lean status.** The lane queues C002's identities (3)–(5), strong divisibility and the uniform corollary as Lean targets.

**LEAD: where real high cycles must live, and a uniform target.**

- **Bounded oscillation forces near-mechanical words.** Take a cycle with all points at least `x_min` and ratio `R = x_max/x_min`. Then for every window of `j` letters, the valuation sum satisfies `|A_(i,j) − j·log₂3| ≤ log₂R + m/(3 x_min ln 2)`.
  - This follows from `x_(i+j) = 3^j x_i/2^(A_(i,j)) · Π(1 + 1/(3x_t))`.
  - So a cycle with bounded oscillation has a valuation word of bounded *discrepancy*.
- **The families so far sit in that class.** C001's and C002's families, and the Christoffel class from Knight's theorem in C001's literature note, are all bounded-discrepancy (mechanical-based) words.
- **A natural uniform target.** For each fixed `Δ`, prove `den(w) > 1` for every primitive word of discrepancy `≤ Δ`, uniformly in `m`. That would exclude every nontrivial cycle with `x_max/x_min ≤ 2^Δ`.
- **It respects the controls.** The `3x+d` cycles have small discrepancy but `den = d > 1`, so the statement does not contradict them. Any growing lower bound on `den` would have to stay consistent with them.

```sh
python3 sidekick/probes/c002_two_block_check.py     # ~9 s, PASS
```

---

## 2026-10-19 00:22 — VERIFIED Lean C001-a (`claude/lean-lane` `a0cf28a`): the algebra of C001's repetition theorem is machine-checked

**Checks.**

- **The definitions match R71's closed-sum convention.**
  - `C [] = 0` and `C (a::z) = 3^|z| + 2^a·C z`. Unfolding gives `Σ_j 3^(m−1−j) 2^(A_j)`; I checked the index shift.
  - `D z = 2^Σz − 3^|z|`.
  - `rep u (k+1) = u ++ rep u k`.
  - `G_(k+1) = Q G_k + P^k`, so `G_k = Σ Q^(k−1−i) P^i`.
  - `C_append` matches `C_(uv) = 3^|v| C_u + 2^(A_u) C_v`.
- **The statements are over ℤ, for every `k ≥ 0` and any `u`.**
  - `commutator` is C001's identity (3).
  - `gcd_dvd_K` and `gcd_le_natAbs_K` give (4) and its bound.
  - `gcd_eq_gcd_K` is (6), under `IsCoprime (D u) (D v)`.

  The only hypotheses are that `v` is nonempty with positive entries, which is what makes `D` odd.
- **Worked example.** `seven_dvd_D_example` gives `7 | D((1,1,3)^k 2) ↔ k ≡ 3 (mod 6)`. `gcd_example` gives `gcd(C_k, D_k) = gcd(D_k, −14)`, with `K = 5·1 − 1·19 = −14`. Together they give main's cancellation law. The counterexample `C(3,1,5) = 49`, `D = 485` is also checked.
- **Receipts.**
  - The `decide` uses are only on small integer facts: `¬2 | 3`, `32^6 ≡ 1 (mod 7)`, and residues mod 6. There is no `native_decide`.
  - Axioms: 9 declarations use the standard three, and 3 use only `[propext]`.
  - The build has no diagnostics, and the sha256 `88de824f…` matches the receipt.
- **Scope.** The lane queues three items as C001-b: the two-sided bound (7) and periodicity (9); the `K = 0` characterisation; and §3's mechanical family.

---

## 2026-10-19 00:21 — LEAD (cycle-spectrum goal, rung 1): the naive "random residue" model predicts infinitely many Collatz cycles, so any spectrum law has to carry the size constraint, which is where `d` enters beyond the gcd

**The trap.** A natural first model for the cycle spectrum treats `C_w mod D_w` as uniform. Then `P(den(w) | d) = gcd(D_w, d)/D_w`, and the expected number of cycles of `3x+d` is `Σ_(m,A) N(m,A)·gcd(2^A − 3^m, d)/(2^A − 3^m)`, where `N(m,A) ≈ C(A−1, m−1)/m` counts the words. At `d = 1` this **diverges**.

- **Computation.** With `T(m) = Σ_A C(A−1,m−1)/(m(2^A − 3^m))`, I get `m·T(m) = 1.66, 1.12, 1.0004, 1.0003` at `m = 10, 20, 50, 100`. So `T(m) ~ 1/m`, and the cumulative count grows like `ln M` (6.5 by `m = 100`).
- **Source of the divergence.** It comes from words with average valuation about 2, `A ≈ 2m`, where `Σ_A C(A−1,m−1)/2^A = 1`. It does not come from `A ≈ m log₂3`.
- **Calibration note.** This is a heuristic computation, not a theorem.

**Why the model fails, and where `d` really enters.** A positive integer cycle of `3x+d` needs every rescaled cycle point `y_i = x_i/d` to be at least `1/d`. Then `2^A = Π(3 + 1/y_i) ≤ (3 + d)^m`.

- **At `d = 1`.** Points `y_i ≥ 1` force `A < 2m` unless the cycle is trivial, which cuts the divergent region at its centre. Beyond the verified range, `y_i ≥ 2^68` forces `0 < A − m log₂3 < m·2^(−68)/(3 ln 2)`. That is the classical Eliahou/Simons–de Weger route to cycle-length bounds.
- **At `d > 1`.** The admissible word region is exponentially larger, up to `A ≈ m log₂(3+d)`. This plausibly explains why `3x+d` has many cycles while `3x+1` has one.
- **Residue structure is not enough.** Uniformity of `C_w mod D_w` fails exactly on words with small cycle points, where `C_w < D_w/d`. So a law for the spectrum across `d` (rung 1) has to model the joint distribution of residue *and size*. Residue structure alone, through `gcd(2^A − 3^m, d)`, cannot separate `d = 1`.

**Suggested test, for whichever lane takes it.**

- **A complete census by word enumeration.** List every cycle with at most 6 odd steps, all words with `A ≤ 60` (about 5M words). For each, record `den(w)` and every `d ≤ 999` it serves.
- **Cross-check the seed scan.** Compare with C001's census, which is bounded by seed. This checks completeness: cycles with large minima can avoid every seed `≤ 5000`.
- **Then fit a size-constrained model.**

---

## 2026-10-19 00:18 — REFEREE C001 (main `14441c0`, first batch of the cycle-spectrum goal): correct and reproduced; it relocates the obstacle to unbounded block structure, the same wall the cycle records face

**Reproduced with independent code** (`c001_spectrum_check.py`, under a second, PASS).

- **The repetition theorem.** With `w_k = u^k v` and `K = D_u C_v − D_v C_u`:
  - identities (1)–(3) hold, including `D_u C_k − C_u D_k = Q^k K`;
  - `g_k = gcd(C_k, D_k)` divides the prime-to-6 part of `K`;
  - the two-sided bound (7) holds, and the exact formula `g_k = gcd(D_k, K)` holds whenever `gcd(D_u, D_v) = 1`;
  - `g_k` is periodic with the stated period `T`.

  Random blocks gave 34,207 two-sided checks, 30,546 exact-formula checks and 2,473 periodicity checks. I also re-derived (3) by hand.
- **The worked law.** `den((1,1,3)^k 2) = (4·32^k − 3·27^k)/(7 if k ≡ 3 mod 6 else 1)` holds for every `k ≤ 80`; the first value is 47.
- **The killed strengthening.** For `u = (3)`, `v = (1,5)`: `K = −30`, `gcd(C,D) = 1` but `gcd(D,K) = 5`. The actual `3x+485` cycle `49 → 79 → 361 → 49` is confirmed.
- **The perturbed mechanical family.** `w = u_m^k 2` is primitive and satisfies `den(w) > 3·(3^m)^(k−1)/(2m)` for all 192 pairs with `13 ≤ m ≤ 60` and `2 ≤ k ≤ 5`.
- **The 3x+d data.** My own raw scan (state 1 not absorbing), over all 67 values `d ≤ 199` coprime to 6 with odd seeds `≤ 5000`, finds exactly the same cycles per `d` as main's `actual_cycles.json`, compared by minimum state.

**Assessment.**

- **Correct, with the controls built in.** The theorem is a clean consequence of the concatenation (commutator) identity. Main's literature note credits that identity to established work (Trümper 2014); the gcd corollary itself was not located. Every `d > 1` control passes, as it must, because the bound need not be sharp.
- **It meets ladder rungs 1–2 at its stated scope, but the scope is thin.** For any fixed one-defect pattern `u^k v` with `K ≠ 0`, the denominator grows exponentially while the cancellation stays bounded, so integer cycles of that shape are finite. Such words are a very small corner of all valuation words.
- **Where the obstacle now sits.** It sits with words whose block structure is unbounded. That is the same wall the published records face. Simons–de Weger and Hercher handle cycles with a bounded number `m` of local minima, using linear forms in logarithms and computation, and `m ≤ 91` is limited by that computation. C001's family escapes their *hypotheses* only because its block count grows through repetition of one fixed pattern, not through genuinely independent blocks.
- **Main's next step is what I would expect.** For two repeated blocks `u^k v^ℓ`, the gcd question becomes an S-unit problem. Bugeaud–Corvaja–Zannier-type bounds on `gcd(a^n − 1, b^n − 1)` are ineffective, which main already flags. Even a full theorem for any fixed number of independent blocks would give finiteness for each block pattern, not the headline.

**A possible side-lane contribution (rung 1).** The persisted data, 333 values of `d` and 1,184 primitive rational cycles, could test a random-model law for the cycle count against `d`. The heuristic is that the expected number of words with `den | d` is roughly `d·Σ_m (count of words)/D`. I may run that as a calibration next.

```sh
python3 sidekick/probes/c001_spectrum_check.py <path to main's actual_cycles.json>   # ~1 s, PASS
```

---

## 2026-10-18 23:55 — VERIFIED Lean V006-a (`claude/lean-lane` `6fbc3f8`): V006's quadratic separation theorem is machine-checked in its unconditional form

**What is formalized.** `QuadraticSeparation.lean` imports only Mathlib. It defines `s2 n = (Nat.digits 2 n).sum` and `Q F t₀ a t = (n ↦ F(t₀ + t + s2(3^a n)))`.

- **The arithmetic lemmas.**
  - Block additivity, and the complement identity `s2(2^k − 1 − x) + s2 x = k`.
  - Main's (5), in the additive form `s2(m(2^k − c)) + s2(mc − 1) = k + s2(m − 1)`, and (6).
  - `3^(r+1) | 2^(3^r) + 1`.
  - `s2_balanced`: `s2((2^(2·3^r·j) − 1)/3^(r+1)) = 3^r j` for **every** `j`. This is main's (7), with all multiples handled through non-overlapping blocks, as the review asked.
- **`Q_injective`.** If `F` is not eventually periodic, then `(a, t) ↦ Q F t₀ a t` is injective.
- **`Q_mem_Reach` and `triangle_encard_le`.** Each `Q F t₀ a t` is reachable from `Q F t₀ 0 0` in at most `a + t` section steps. Here `Reach` is the set of states reachable in at most `D` binary or ternary steps, which is main's `J_D`; I checked the definition. So `#{(a,t) : a + t ≤ D} ≤ |Reach D|`.

**Checks.**

- **Statement match.** It matches `overlap.md` §2 in the **unconditional** form, with "`F` not eventually periodic" as an explicit hypothesis. So no Cobham is involved, and finite-valuedness is never used.
- **Scope.** Two things are not yet formalized:
  - the arithmetic step that evaluates the triangle count as `(D+1)(D+2)/2`, a small follow-up;
  - the Collatz corollary of §3, which would reuse `kernel_ternary_closure`'s depth witnesses.
- **Receipts.**
  - **Axioms.** All 12 reported declarations use exactly the standard three.
  - **Build.** No diagnostics.
  - **Source scan.** No `sorry`, `decide`, `native_decide` or `axiom`.
  - **Hash.** The sha256 `0f82a36b…` matches the receipt.

**Update 00:02 (2026-10-19): the count is now closed** (`f5a6d76`).

- **New theorems.** `card_triangle` gives `(triangle D).card = (D+1)(D+2)/2`. `reach_encard_ge` then gives `(D+1)(D+2)/2 ≤ |Reach(Q F t₀ 0 0) D|` in `ℕ∞` for every non-eventually-periodic `F`. That is main's bound (4) with the number.
- **Receipts.** All 15 reported declarations use exactly the standard three axioms. The build has no diagnostics, the source scan is clean, and the new sha256 `5b92658b…` matches the receipt.

**Formal record, updated.** The following are now machine-checked:

- V004 (modulo a named Cobham hypothesis);
- the scalar interface;
- the two-base equivalence (2-automatic ⇔ 3-automatic);
- V006's quadratic separation;
- the periodic classification for every odd `d`;
- the C.1a dichotomy.

V009's return argument is the largest piece of the written record still unformalized.

---

## 2026-10-18 23:36 — REFEREE V009 (main `4be9bae`): confirmed; the first all-invariant improvement over the generic bound, `κ_h(D) − (D+1) → ∞`

**The claim.** For every nonconstant finite-valued Collatz invariant `h`, the excess `κ_h(D) − (D+1)` tends to infinity. Equivalently, `κ_h(D) = D + O(1)` is impossible. The excess is nondecreasing, because each binary layer of an infinite kernel is nonempty, so "unbounded" and "tends to infinity" agree here.

This is the first quantitative improvement over the generic infinite-kernel bound that holds for **every** nonconstant invariant. It is the additive diagnostic that main named in its D8 reply. It is not the `(1+ε)` gain, and it is not the active unbounded-ratio goal; main says both.

**1. The finite core (§§4–7): recomputed independently** (`v009_escape_check.py`, under a second, PASS).

- **The boundary identity.** I enumerated the transition graph of window states allowed by (5), `X_n(z) Y_(n+1)(z²) = Y_n(z) X_(n+δ)(z³)`, for `δ = 2, 3, 4`. Every window on a cycle is either the all-digits case or all singletons, as §4 claims.
- **The singleton digit system.** For `c_n + 2d_(n+1) = d_n + 3c_(n+δ)` (6), the cycles are exactly:
  - the constant tails `(0,0)` and `(1,2)`;
  - no other cycle for `δ = 2`;
  - one cycle for `δ = 3`, a rotation of `1100 / 1012`;
  - one cycle for `δ = 4`, a rotation of `110111001000 / 222101000121`.

  This is §7's table, recovered by exhaustive search rather than through the `v`-recursion.
- **The quantities used later.** On both cycles:
  - `j_n ∈ {0,1,2}`;
  - the parity condition `c_n ≡ d_n + c_(n+δ)` holds;
  - every `y_n` has denominator exactly `2M`, so `y_n ≠ x_a` (14);
  - `x_n ≠ j + 3x_m` for every `j ≠ d_n` and every `m` (16).

**2. The return argument (§§1–3, 8–10): checked by reading.**

- **The tail ray.** The binary parent of `q_(n+1)` must be `q_n`. The depth-4 ternary bound (1) comes from V004.
- **The increment stabilizes.** `δ_n` is nonincreasing, and `δ_n ≤ 0` would leave a finite ternary-closed set. `δ = 1` is excluded by V007's singleton exit.
- **(5) is coefficient-exact.** The maximal depth `n+δ+1` is reached only through `C_n·D_(n+1)` and `D_n·C_(n+δ)`. Nonescaping children cannot reach it.
- **The `A`-recursion.** `A_(n+δ) = T_(j_n)(A_n)`, with the parity of the affine residue from (6).
- **Every `p`-block has a nonmaximal edge.** This follows from `y_n − x_a = 3^p(y_n − x_a)` together with (14).
- **The contraction (17).** It follows by commuting `k` critical edges through `T_j`, and the first differing digit enters with the favourable coefficient `λ − 1`.
- **The finish.** The contraction (18) bounds the `A_n` in a finite set, so they are eventually periodic. Induction on inputs then gives `q_(n+P) = q_n`, contradicting distinct minimal depths.

I found no gap.

**3. The global detection bound (`global_growth.md`): checked.** Suppose `|J_D(s)| ≤ C(D+1)` and a combination `g` first becomes nonzero at `N ≥ 9^L`. Sectioning by every `m = 2^a 3^b` with `a + b ≤ L` gives first nonzero indices `⌊N/m⌋`. These are distinct because `N ≥ m m'`, so the `(L+1)(L+2)/2` sections are triangular and independent inside `W_(A+L)`. That contradicts the dimension bound once `L > C + √(C² + 2C(A+1))`, which the stated `L` satisfies. The result is elementary and generic, with no Cobham.

**Scope.** The Collatz application uses hypothesis (I), so it inherits Cobham through V004, as main's report states.

**Update 23:49: a second independent check.** The Lean lane read `binary_tail.md` §§1–11, `global_growth.md` and `ADDITIVE_REVIEW.md` in full and found no gap. It re-derived the following steps rather than reading them:

- the parent and depth-4 bound (§1);
- the `δ` stabilisation (§2);
- the root-of-unity case analysis (§4);
- the telescoped congruence (7) (§5);
- the sign of `v_n` and both cycles (§7);
- the parity in (13) and the 2-adic separation of `y_n` from `x_a` (§8);
- the `λ − 1` coefficient in §9.

V009 now has two independent confirmations besides main's own reviews: this lane's exhaustive recomputation of §§4–7 and the Lean lane's full read. The return argument is a large formalisation unit, so the Lean lane is doing the V006 and V008 pieces first.

```sh
python3 sidekick/probes/v009_escape_check.py     # <1 s, PASS
```

---

## 2026-10-18 23:23 — VERIFIED Lean V007-a (`claude/lean-lane` `6adac5a`): for the scalar interface, 2-automatic ⇔ 3-automatic, with no external input

**What is formalized.** `ReverseClosure_Assembly.lean` works with V004's `Kernel` and `KAutomatic` and with `c(n) = b(2n)`. The hypotheses are the three scalar identities: `b(3n) = b(4n)`, `b(3n+2) = b(2n+1)` and `b(4n+2) = b(n)`.

- **`automatic_two_iff_three`.** A `b` satisfying the three identities is 2-automatic if and only if it is 3-automatic. This needs **no Cobham hypothesis**.
  - The direction 3 ⇒ 2 is V007's reverse closure: `union_binary_closed`, using the four offset cases, then `kernel2_subset_union`.
  - The direction 2 ⇒ 3 goes through V004's `K₃(b) ⊆ K₊(ext b)` and `kernel2_ext_subset`, which says `K₂(ext b) ⊆ {ext b} ∪ K₂(b)`.
- **`constant_of_ternary_automatic`.** `CobhamStatement α` together with a 3-automatic `b` forces `b` constant. This is V007's "ternary automaticity forces constancy" for `b` itself.

**Checks.**

- **Statement match.** It matches V007 §1.1.
- **Scope.** V005's reconstruction from an arbitrary positive section `g` is not formalized, so the statement is about `b`, not about every section. The lane says so.
- **Assembly.** I regenerated `ReverseClosure_Assembly.lean` independently as the concatenation `build_reverse_assembly.sh` describes. It is byte-identical (`c5429174…`), with one `import`. Its parts are unchanged from what I verified before: `V004_Assembly.lean` `3d570751…` and `ScalarInterface.lean` `df3dabd4…`. The new part `ReverseClosure_Final.lean` is `6a056dec…`.
- **Axioms.** All 9 reported declarations use exactly `[propext, Classical.choice, Quot.sound]`.
- **Build.** No diagnostics.
- **Source scan.** The new part has no `sorry`, `decide`, `native_decide`, `axiom` or `set_option`.

**Why the two-way statement is worth noting.** In general, Cobham's theorem only says that a sequence automatic in both bases is eventually periodic. Here the identities make the two notions *equivalent*. So for Collatz invariants, "automatic in either base" is one condition, and Cobham turns it into eventual periodicity. The written V007 states only the one direction.

**The lane's check of V008 (`9d66b69`): no error.** It verified the two-exit construction, including whole-sequence witnesses and the rational-frequency argument, and the uniform tail lemma. It found **one implicit step** in the finish of the first-shell theorem: "all outputs at zero agree" needs `b(0) = b(1) = b(2)`. That follows from identities 2 and 3 at `n = 0`, which give `b(2) = b(1)` and `b(2) = b(0)`. It is true, but worth a line in `ROOT_REVIEW.md`, since `v = E₁ b` has `v(0) = b(1)`.

```sh
git show origin/claude/lean-lane:experiments/lean_lane/receipts/ReverseClosure_Assembly.axioms.txt
```

---

## 2026-10-18 23:01 — REFEREE V008 (main `9d66b69`): the two-exit counterexample is confirmed and the batch is honestly scoped; D8 partly accepted

**1. The generic two-exit counterexample: reproduced.** Let `p(n) = 1_{nα} < α` with `α = (√5−1)/2`, and `s(n) = p(⌊n/6⌋)`.

- **Exits.** Both binary children of `s` equal `u(n) = p(⌊n/3⌋)`, and all three ternary children equal `v(n) = p(⌊n/2⌋)`. Checked exactly for `n < 10⁴`. The sequences `s`, `u` and `v` are pairwise distinct, so `{s}` is an interior with two exits.
- **Infinite kernels.** The frequency of 1s is `α` (0.61805 empirically), which is irrational. An automatic sequence whose frequency exists has a rational one, so every vertex has infinite kernels in both bases.
- **Not a Collatz invariant.** It fails the root equation `s(4n+2) = s(n)` at `n = 1` (`s(6) = 0`, `s(1) = 1`).

So the radix laws and two-base infinitude alone do not exclude two-exit boundaries. Main draws the right conclusion: separator widths cannot be excluded one at a time.

**2. Other results, read but not independently replayed.**

- **First-shell theorem.** The three scalar equations together with `|J_1(b)| ≤ 3` force `b` constant. The proof is elementary and needs no Cobham. Two reviews by main check it, including the correction of a draft row.
- **Uniform tail bound.** If `|B_D| ≤ C(D+1)`, then for every `C' > C` there are arbitrarily late cuts `r` with `|B_(r+t) \ B_r| ≤ C't` for all `t`. This is the standard maximisation argument.
- **Control.** The bounded-degree control rules out the "long uniformly thin stretches" shortcut.

None of these gives a rate improvement for all invariants, and main says so.

**3. Directions.** Main has added dated notes to V005, V006, V007 and `RESULTS.md` stating that their Collatz applications inherit Cobham through V004. That closes my 22:32 and 22:40 scope notes.

D8 is partly accepted.

- **Part 1 is kept as a diagnostic.** The `(1+ε)` gain is now a progress diagnostic, not a success condition. Main also notes, correctly, that an unbounded additive excess would be a weaker strengthening.
- **Part 2 is rejected.** Automatic abandonment conflicts with the user's active goal. I am not pursuing the dispute. Main accepted the methodological point, and V008 already acts on it.
- **Main's transfer point is fair.** A `d`-uniform growth theorem for non-periodic invariants is not adopted. My remarks were labelled assessments, and the finite samples do not prove one.

---

## 2026-10-18 22:42 — VERIFIED Lean item 1b (`claude/lean-lane` `79e8a69`): V13's periodic classification is machine-checked for every odd `d`

**The theorems.** `GeneralPeriodic.lean` imports only Mathlib. Its hypotheses are `h : ℕ → α`, odd `d` (multiples of 3 allowed), `h(2n) = h(n)`, and `h(3n+d) = h(n)` for odd `n > 1`.

- **`invariant_classification`.** An `M`-periodic `h` is `gcd(M, d)`-periodic and satisfies `h(3n) = h(n)`.
- **`factors_through_zmod`.** This gives an explicit `F : ZMod (gcd M d) → α` with `h n = F n` and `F(2z) = F(z) = F(3z)`.
- **`invariant_of_class_function`.** The converse holds for every `g | d`.
- **`period_gcd_six_free`.** For a period `2^a 3^b M'` with `M'` odd, `h` is `gcd(M', d)`-periodic. This is the refinement for `3 | d` from my 22:26 entry.
- **`eventually_periodic_invariant`.** The same conclusions hold on the positive integers for eventually periodic `h`.
- **`control_indicator`.** For odd `d` with `3 ∤ d`, `1_(d|n)` is a nonconstant invariant, instantiated at `d = 5` and `61`.

**Checks.**

- **Statement match.** This is V002 §4 and its Appendix, as refined in V13: "periodic invariant colourings correspond to `⟨×2, ×3⟩`-invariant functions on `Z/gcd(M, d)Z`", proved in both directions.
- **The excluded source `n = 1` costs nothing here.** Under periodicity, the rule at `1 + 2M` implies the rule at `1`. So assuming the rule only at odd `n > 1` makes the theorem stronger, not weaker.
- **Axioms.** 12 declarations use `[propext, Classical.choice, Quot.sound]`, one uses `[propext, Quot.sound]`, and the converse uses only `[propext]`.
- **`decide`.** Its uses are on `d | n` indicators and small numerals. There is no `native_decide`.
- **Receipts.** The build has no diagnostics, and the sha256 `95555318…` matches the receipt.

**Where this leaves the formal record.** The following are now machine-checked:

- the periodic classification for every odd `d`;
- V004 for `d = 1`, modulo a named Cobham hypothesis;
- the scalar interface;
- the C.1a dichotomy.

My d-uniform automatic classification (`writeup/D_UNIFORM_AUTOMATIC.md`) would follow by combining this file's eventual-period theorem with a `d`-version of the closure up to shifts. That closure is the one remaining unformalised piece. The lane has also recorded in its `STATE.md` that V006's Collatz corollary depends on Cobham.

```sh
git show origin/claude/lean-lane:experiments/lean_lane/receipts/GeneralPeriodic.axioms.txt
```

---

## 2026-10-18 22:40 — REFEREE V007 (main `b24020f`, singleton-exit obstruction): sound and honestly scoped, with no improved bound; plus direction D8 (a first milestone and a stopping rule)

**V007's reverse closure: checked by hand.** Let `c(n) = b(2n)`. Using the three scalar identities, the union of the ternary kernels of `b` and `c` is closed under binary sections. I checked all four cases and their offset bounds:

- `v` even: `c(3^a n + v/2)`;
- `v` odd: `b(3^(a+1) n + (3v+1)/2)`, from `b(2m+1) = b(3m+2)`;
- `v` odd: `b(3^a n + (v−1)/2)`, from `b(4m+2) = b(m)`;
- `v` even: `b(3^(a+1) n + 3v/2)`, from `b(4m) = b(3m)`.

So if `b` has a finite ternary kernel, it also has a finite binary kernel. Together with V005's affine reconstruction, which preserves finite ternary kernels, this gives hypothesis (I): every positive binary section of a nonconstant invariant has an infinite kernel in **both** bases.

**The singleton-exit theorem is generic, and is applied to Collatz through (I).** The six radix identities `T_j E_i = E_l T_k` (for `2j + i = 3l + k`) hold for every sequence, since both sides equal `s(6n + 2j + i)`. So the theorem is about all sequences satisfying (I). As main says, its numerical yield (`|J_D(b)| ≥ 2D+1`) converts to less than the generic binary bound.

**Scope note, continuing 22:32.** Deriving (I) for Collatz invariants ends in V004, since finite kernels make `h` constant. V004 uses Cobham's theorem, so V007's Collatz application inherits that dependence. `separator.md`, `REPORT.md` and `INDEPENDENT_REVIEW.md` never mention Cobham.

**Update 22:44: a second independent check.** The Lean lane read `separator.md` line by line and found no error. Its checks:

- the polynomial identity `X(z)B(z²) = Y(z)A(z³)`, where each exponent from 0 to 5 is paired uniquely;
- the step showing `A` is a monomial, including the constant case `p(m) = p(⌊2m/3⌋)`;
- the propagation of residue sets, locking into `(0,0)` or `(1,2)`;
- the eventually periodic `T₁`-orbit, which gives `q_(n+p) = q_n` as whole sequences;
- the reverse-closure table.

The lane reached the same Cobham scope conclusion independently. It plans next to formalize the reverse-closure lemma itself ("`b` ternary-automatic ⇒ `h` constant", modulo the named Cobham hypothesis).

**Calibration.** Three batches (V005–V007) have each been sound, and none has improved the generic all-invariant bound. `sidekick/DIRECTIONS.md` now carries **D8**, a proposal with two parts:

- name the first milestone as `κ_h(D) ≥ (1+ε)(D+1)` infinitely often, for every nonconstant `h`;
- if two more batches pass without it or another all-invariant improvement, record the goal as open with its structural results and move the main lane back to comparing viewpoints.

The reasons are in D8: the target appears `d`-uniform, and it cannot by itself bear on convergence. D7's status row is also updated with the Lean audit's close-out.

---

## 2026-10-18 22:32 — REFEREE (scope note on V005/V006, main `ceebb93`): two corollaries inherit Cobham through V004, unrecorded in their RESULTS lines

The Lean lane raised this and I checked it against main's text. It is a scope note, not an error.

- **V005's cylinder lemma inherits Cobham.** The lemma says one automatic positive section forces constancy. Its constancy step is V004 (`V005/direct_sections.md`: "V004 now makes h constant"), and V004 uses Cobham's theorem.
- **V006's corollary inherits it too.** The corollary says a nonconstant invariant with one digit-count section `h(2^K n + r) = F(s₂ n)` has `κ_h(K+4D) ≥ (D+1)(D+2)/2`. It excludes eventually periodic `F` through that V005 lemma, so it is conditional on Cobham as well.
- **Main's write-ups don't say so.** `V006/REPORT.md`, `overlap.md` and `QUADRATIC_REVIEW.md` never mention Cobham. The V005 and V006 lines in `docs/RESULTS.md` don't record the dependence; only the V004 line names Cobham.
- **The unconditional version.** With "`F` not eventually periodic" as an explicit hypothesis, the corollary needs no Cobham. The quadratic distinctness theorem itself (`overlap.md` §2) is elementary and uses no finiteness.
- **Why it matters.** Main's `AGENTS.md` keeps Cobham as an explicit hypothesis for V004, and the Lean V004 assembly states it as `CobhamStatement`. The same labelling would keep the two downstream results consistent.

The Lean lane also checked V006 line by line and reports no error. Its checks covered `overlap.md` (5)–(7) and the distinctness argument, the 11-pair control (including `z(7) = 1 ≠ z(9) = 0`, a direct failure of `b(3n) = b(4n)` at `n = 1`), the `T/U` action control, and `graph_interface.md`. Its depth accounting `K + t + 4a` matches the `kernel_ternary_closure` witnesses already in Lean.

---

## 2026-10-18 22:26 — REFEREE V006 (main `ceebb93`): the quadratic theorem is sound, but no genuine invariant tested meets its hypothesis; also VERIFIED Lean V005-a (scalar interface)

**1. V006's quadratic theorem: reproduced.** The theorem: for a finite-valued `F` that is not eventually periodic, the sequences `n ↦ F(t + s₂(3^a n))` are pairwise distinct. So a joint section family that contains a digit-count section has at least `(D+1)(D+2)/2` members.

- **Worked example.** I used main's `F` (the indicator of powers of 2). All 64 sequences with `a, t ≤ 7` are pairwise distinct on a 400-term prefix, a rigorous lower bound (`v006_quadratic_check.py` part 1).
- **The two lemmas hold.**
  - `s₂(m(2^k − 1)) = k` once `2^k ≥ m`. Proof: `(m−1)·2^k + (2^k − m)`, a complement block. Checked for odd `m < 1000` and `k ≤ 40`.
  - `s₂((2^K − 1)/3^r) = K/2` for `2·3^(r−1) | K`. Checked for `r ≤ 6`.
- **The conditional consequence follows.** If a nonconstant invariant has one section `h(2^K n + r) = F(s₂ n)`, then `κ_h(K + 4D) ≥ (D+1)(D+2)/2`. This uses V004's factor-4 depth bound. If `F` were eventually periodic, that section would be automatic, and V005's cylinder theorem forces `h` constant.

**2. The hypothesis has no instance among genuine invariants tested.** I tested every section `n ↦ c_d(2^K n + r)` with `K ≤ 9` and odd `r` of the actual 3x+d cycle labellings `c_5`, `c_13` and `c_61`, on `n < 2^13`. None is a nonconstant function of `s₂(n)` (part 2).

- **This does not test the extraction step.** These genuine invariants all have superlinear section counts (20:02 entry), while extraction is needed only for hypothetical linear-growth invariants. So the control neither supports nor refutes it.
- **What it does show.** The theorem's class has no known member in any `3x + d`. As main's own report says, V006 by itself does not advance the all-invariant goal. The 11-pair control's identities and its invariance failure (`z(3) = 1 ≠ z(10) = 0`) reproduce (part 3).

**3. Lean V005-a, `ScalarInterface.lean` (`claude/lean-lane` `3dd6cb7`): VERIFIED.** It imports only Mathlib.

- **`ext_tri_iff`.** It states main's equivalence verbatim, with `ext b x = b((oddPart x − 1)/2)`. The converse goes through `ext_three_mul_add_two` (`ext b (3m+2) = b m`), using the same strong-induction split as my 22:10 sketch.
- **`scalar_interface_iff` and `ext_odd_values`.** Together they make "solutions of the three identities ↔ invariant colourings" a bijection, so main can work on `b` alone with no loss.
- **The lane's checklist.**
  - The orientation `b(3n) = b(4n)` matches main.
  - `ext b 0 = b 0`, through truncated subtraction, matches main's `h(0) = b(0)`.
  - The colour type is arbitrary.
- **Receipts.** The sha256 `df3dabd4…` matches the receipt. The axioms are the standard three (`v004_relation` needs only `[propext, Quot.sound]`). The build has no diagnostics, and a source scan is clean.

**4. For the record: periodic invariants of `3x + d`, any odd `d`.** I found no counterexample to "every `M`-periodic invariant is `gcd(M, d)`-periodic". In 6,000 residue-graph cases (25 odd `d`, multiples of 3 included, and every `M ≤ 240`), `x` and `x + gcd(M, d)` are always in the same component.

- **Direct proof.** The PR #3 argument works with translation by `d`. From `h(6x+d) = h(x) = h(6x+2d)`, once `M` is coprime to 6, `h` is `d`-periodic.
- **Stronger when `3 | d`.** The period divides `gcd(M₆, d)`, where `M₆` is `M` without its 2- and 3-parts.
- I sent this to the Lean lane for its item 1b.

```sh
python3 sidekick/probes/v006_quadratic_check.py     # ~10 s, PASS
```

---

## 2026-10-18 22:10 — REFEREE V005 (main `85a07c2`, quantitative rigidity, first batch): sound partial results; main's counterexample to Bell's printed Conjecture 3.4 is confirmed; also VERIFIED Lean item 4 (partial)

**Goal.** Main has activated the `κ_h(D)/D` target: `docs/QUANTITATIVE_RIGIDITY_BRIEF.md` makes it the active goal. The batch honestly reports it as open.

**1. The sparse control refutes Bell's Conjecture 3.4 as printed. Confirmed.**

- **The conjecture.** I extracted the text from the CIRM PDF (Bell, "Cobham's theorem and its extensions", Actes des rencontres du CIRM 1, 2009).
  - Definition 4 is the cumulative count `G(f;k;m)` of distinct sections `f(k^a n + b)`, `a ≤ m`, `b < k^a`, exactly main's `G_k`.
  - Definition 5 is `Dim_k = limsup log G / log m`.
  - Conjecture 3.4 says that a finite-valued `f` with `Dim_k` and `Dim_ℓ` both finite, for multiplicatively independent `k` and `ℓ`, is eventually periodic.
- **The example.** For `f = 1_{6^(2^j)}`, I computed `G_2` and `G_3` **exactly**, not from finite prefixes, using `v_p(6^e) = e` (`v005_sparse_growth_check.py`).
  - Zero-offset sections are `D+1` distinct infinite sets.
  - Every other section is empty or a singleton `{⌊6^e/p^a⌋}`.
  - Results: `G_2 = 2273`, `G_3 = 1631` at `D = 1000`. The largest slopes over the tested `D` are 2.32 and 1.74, inside main's bounds `5D+3` and `3D+3`.
  - So both dimensions equal 1, and `f` is not eventually periodic.
- **Why the count is linear.** A single-point section `⌊6^e/2^a⌋` becomes `δ_0` once `a > e·log₂6`, so each `e` contributes at most about `1.6e` distinct functions. The Lean lane flagged this as easy to get wrong.
- **Literature.** A quick search found no published correction, consistent with main's bounded search. Novelty is undetermined.

**2. This supersedes part of my 21:26 note.** I wrote that excluding linear growth of `b` "in both bases" would be a linear-complexity Cobham theorem. Main's example shows the *separate* two-base version is false. Any route of that kind has to use the **joint** family `b(2^i 3^j n + r)`, as V005 now does (`J_D(b) ⊆ K⁺_(1+4D)(h)`, matching my d-uniform closure), or the scalar identities themselves.

**3. The scalar interface is equivalent to the invariant equations. Checked by hand.** Suppose `b(3n) = b(4n)`, `b(3n+2) = b(2n+1)` and `b(4n+2) = b(n)`. Set `h(x) = b((oddpart x − 1)/2)`. Then `h(3n+1) = h(n)` for odd `n` reduces to `h(3m+2) = b(m)`, which follows by strong induction on `m`:

- `m` odd uses identity 2;
- `m ≡ 0 (mod 4)` uses identity 1;
- `m ≡ 2 (mod 4)` uses identity 3 and recurses to `m' = (m − 2)/4`.

The forward direction is already Lean-checked (B1, B2, B4 in `OddEventuallyPeriodic.lean`). The lane has queued the converse.

**Calibration.**

- **This is a self-contained problem in automata theory.**
  - The quantitative reconstruction bound `κ_h(D) ≤ 1 + (C_g κ_g(D−1))^M` is polynomial, so it cannot exclude linear growth, as main says.
  - The real question is whether the three scalar identities force non-overlapping section families.
- **It still does not touch the convergence problem**, for the reasons in my 21:26 note: the analogue for `3x + d` should hold verbatim for non-periodic invariants.

**Lean item 4, partial (`claude/lean-lane` `2789674`): VERIFIED.**

- **Theorems.** `PairObligation.lean` uses `collatzAccel n = (3n+1)/2^(v₂(3n+1))` from the audited library. I checked its definition in `StatementAudit.lean` on main.
  - `S(4u+1) = S(u)` and `S(3(4u+1)) = 18u+5` for all `u`.
  - `pair_iff`: the W5 obligation at `w = 4u+1` is exactly "the orbits of `u` and `18u+5` meet".
  - `collatz_imp_pairs_meet`: the easy direction of R.1.
- **Receipts.** Axioms are the standard three. The `decide` uses only evaluate `collatz^[3] 1 = 1` and the parity of 4 and 2. The sha256 `3b0e6d2e…` matches the receipt, and the build has no diagnostics.
- **Scope.** The converse of R.1 is stated as a `Prop` (`R1Converse`) and not asserted. There is no `sorry`.
- **The lane's remark, checked.** A minimal-counterexample argument for the converse stalls. A preimage `(2^a m − 1)/3 ≡ 23 (mod 36)` of a component minimum `m` forces `a = 1` (from `2^a m ≡ 70 mod 108`) and `m ≡ 35 (mod 54)`. So R.1's `⇐` direction carries the whole frozen framework (R25, R37, R40, R43), and "R.1 is a reformulation" holds only for the `⇒` direction.

```sh
python3 sidekick/probes/v005_sparse_growth_check.py     # exact G_2, G_3; PASS
```

---

## 2026-10-18 21:57 — VERIFIED Lean queue item 3 (`claude/lean-lane` `b980e52`): the empty-or-positive dichotomy is machine-checked over the audited C.1a library

**The theorems.** `experiments/lean_lane/Dichotomy.lean` imports `Solution.Basic` from AxiomMath `CollatzPosDens` @`3a38bfbb`, the library audited in PR #2. Write `Bad n := ∀ k, collatz^[k] n ≠ 1`, using the ordinary map.

- **`bad_positive_lower_density`.** If some `n > 0` is bad, then for explicit `c > 0` and `X₀`, every `N ≥ X₀` has `c·N ≤ #{n < N : 0 < n ∧ Bad n}`.
- **`collatz_of_bad_density_zero`.** If the bad set has lower density zero, every `n > 0` reaches 1.

**Checks.**

- **Statement match.** This is my S1 card's dichotomy (VIEWPOINTS.md), "B is empty or has positive lower density", in natural density.
  - **Map and clock.** Ordinary-map iterates, matching the imported theorem. The accelerated clock is not used.
  - **Why `0 < n` is needed.** `collatz 0 = 0`.
  - **Scope.** The log-density passage is not formalised, and the lane's `STATE.md` says so.
- **The second theorem is stronger than its docstring.** Its hypothesis, "for every `c > 0` and `X₀` some `N ≥ X₀` has fewer than `c·N` bad numbers", is *lower* density zero, weaker than natural density zero.
- **Proof, checked by reading.**
  - A bad `n` gives the bad target `t = 3m + 1` with `3 ∤ t`, where `m` is the odd part of `n`.
  - Anything reaching a bad `t` is bad (`bad_of_reach`). The case "reached 1 first" is excluded because every iterate of 1 returns to 1.
  - The audited theorem's counted set (odd, reaches `t`) is a subset of the bad set.
  - The constant `collatzDensityDep t` unfolds to `1/(t^4 · 2^2^2^87640)`. This is the tower constant recorded on the S1 card. Its positivity is proved without evaluating the tower.
- **`decide`.** The single use is `collatz^[3] 1 = 1`, which the kernel evaluates in three steps. It adds no axiom.
- **Source scan.** No `sorry`, `native_decide`, `admit`, `axiom` or `set_option`.
- **Axioms.** Exactly `[propext, Classical.choice, Quot.sound]`, transitively through the imported library.
- **Build.** `exit=0 (no diagnostics)`.
- **Hash.** The sha256 `02e1f309…` matches the receipt.

**Update 21:59.** In `2765bdf` the lane corrected the docstring to say *lower* density zero. I stripped comments from both versions and the code is identical. The new sha256 `2edd749d…` matches the regenerated receipt, and the axioms are unchanged.

**Calibration.**

- **This is a restatement of the goal, not progress on it.** Proving that the bad set has lower density zero is now formally equivalent to Collatz, so any "density" milestone for `B` must stop strictly short of lower density zero.
- **Known density results do not reach it.**
  - Krasikov–Lagarias give `≥ x^0.84` numbers reaching 1, far from positive density.
  - Tao's almost-bounded-values theorem is about `Col_min(N) < f(N)` in log density, not about reaching 1.
- **Trust base.** The trust base now includes the imported AI-generated library. Its comparator certificate passes six kernels. The provenance caveat recorded in the PR #2 audit stands, as do main's two independent replays.

```sh
git show origin/claude/lean-lane:experiments/lean_lane/Dichotomy.lean | shasum -a 256   # 2edd749d… since 2765bdf (was 02e1f309…)
git show origin/claude/lean-lane:experiments/lean_lane/receipts/Dichotomy.axioms.txt
```

---

## 2026-10-18 21:47 — VERIFIED Lean V004-iii (`claude/lean-lane` `c453d38`): main's V004 theorem is machine-checked, modulo one named classical hypothesis that is true

**The theorem.** `LeanLane.V004.automatic_rigidity`, in `V004_Assembly.lean`:

```
CobhamStatement α → ∀ h : ℕ → α, (∀ n, h (2n) = h n) → (∀ n, Odd n → 1 < n → h (3n+1) = h n)
  → KAutomatic 2 h → ∀ n, 0 < n → h n = h 1
```

**Definitions.**

- `Kernel k f = {n ↦ f (k^e n + j) : j < k^e}`, a `Set (ℕ → α)`.
- `KAutomatic k f` means that kernel is finite. This is Eilenberg's characterization, taken as the definition and stated so in the file header.
- `CobhamStatement α = ∀ f : ℕ → α, KAutomatic 2 f → KAutomatic 3 f → ∃ N M, 0 < M ∧ ∀ n ≥ N, f (n+M) = f n`.

**My four checks from 20:55, all met.**

1. **Quantification.** The hypothesis covers every `f`. It is never specialised to `h` or `b`.
2. **Kernel shape.** The kernels have the standard form, with `e ≥ 0` and `j < k^e`.
3. **Finite range.** It is derived, not assumed (`finite_range_of_kernel2`, using the section with `e = j = m`).
4. **Hypotheses.** The conclusion needs only `KAutomatic 2 h`.

**The named hypothesis is true, so the theorem is not vacuous.** A finite kernel gives a finite range. Eilenberg's theorem then makes `f` 2- and 3-automatic over that finite alphabet, and Cobham's theorem (1969) gives eventual periodicity. The Lean statement implies main's §1: extending a positive-integer colouring by any `h 0` keeps the 2-kernel finite, and doubling at `0` is trivial.

**Proof structure, checked by reading.**

- `Kernel 2 b ⊆ Kernel 2 h`, via `b(2^e n + j) = h(2^(e+1) n + 2j+1)`.
- `Kernel 3 b ⊆ K_+ ⊆ Kernel 2 h`, by induction on ternary digits, peeling the top digit `j = 3^e q + m` and applying `kernel_ternary_closure`.
- Cobham applied to `b`, then `odd_eventually_periodic_const`.

**Receipts.**

- **Axioms.** Exactly `[propext, Classical.choice, Quot.sound]`.
- **Build.** `exit=0 (no diagnostics)`.
- **Source scan.** No `sorry`, `native_decide`, `decide`, `admit` or `axiom`.
- **Hashes.** `V004_Final.lean` `e1f0c727…` and `V004_Assembly.lean` `3d570751…` match their receipts.
- **Assembly file.** I regenerated the compiled file independently, as the concatenation `build_assembly.sh` describes. It is byte-identical, and its two included parts have the hashes I verified at 20:49 and 20:55. One `import` line.

**Status of V004 after this.** The only unformalised input is Cobham's theorem in kernel form, which is classical and not in Mathlib. Every step specific to Collatz is now checked by the Lean kernel. Calibration from the 20:40 and 21:26 entries is unchanged: this is a theorem about description classes, it is d-uniform except for the commutator step, and it says nothing about the actual bad set.

```sh
git show origin/claude/lean-lane:experiments/lean_lane/receipts/V004_Assembly.axioms.txt
git show origin/claude/lean-lane:experiments/lean_lane/V004_Assembly.lean | shasum -a 256   # 3d570751…
```

---

## 2026-10-18 21:26 — REFEREE (main's two candidate follow-ups in `VIEWPOINT_MAP.md`): both are d-uniform, and each needs a tool beyond the published state of the art

Main's map asks for a comparison of the quantitative-complexity target with the V12 statistical alternative before it activates a new goal. These are assessments with sources, not results.

**1. The `κ_h(D)/D → ∞` target (superlinear binary-kernel growth for every nonconstant invariant `h`).**

- **The best known quantitative Cobham theorem is far too weak.** Mol–Rampersad–Shallit–Stipulanti, "Cobham's theorem and automaticity" (IJFCS 2019, arXiv:1809.00679), make Krebs' proof explicit.
  - Their common-prefix bound for aperiodic `a`- and `b`-automatic sequences with `m` and `n` states is doubly exponential, `θ^(θ^(C m⁴ n⁴))` (Cor. 6).
  - The resulting `b`-automaticity lower bound for an aperiodic `a`-automatic sequence is only about `(log log n)^(1/4)` (Cor. 7).
  - Byszewski–Konieczny–Krawczyk (arXiv:1908.11244, Combinatorica) characterize common factors, but with no quantitative bound; their compactness proof is not effective.
- **The generic linear bound is tight for non-automatic sequences.** The indicator of `{2^(2^k)}` is not 2-automatic and has `κ(D) = D + 3`. So the target needs invariance-specific input, not just "non-automatic".
- **A two-base route would itself be new automata theory.** Through V004's closure, linear binary growth of `h` forces linear growth of `b = h(2n+1)` in *both* bases 2 and 3, with ternary depth `k` landing in binary depth `≤ 4k+1`. Excluding that for non-periodic `b` would be a linear-complexity Cobham theorem. I found no such theorem; the published bounds are many orders weaker.
- **It is d-uniform.** For `3x+5` and `3x+13`, the actual cycle labellings have at least 242 and 259 sections by depth 9 (rigorous lower bounds from distinct prefixes). Their counts grow at a ratio of about 1.8 per level. So the target's d-analogue is consistent with genuine separations, and a proof would not distinguish `d = 1`.

**2. The V12 target (power bounds `X^(-η)` for the failure mass and the endpoint collision mass of first passage below `X^(1/4)`).**

- **It asks for a better rate than Tao proves.** The published rate in Tao's theorem (arXiv:1909.03562v7, Thm 3.1) is `(log x)^(-c)`, with `c` unspecified. A power saving needs improving the rate-limiting steps:
  - the `O_A(m^(-A))` decay of Prop 1.17, where `m ≍ log x`;
  - the `log^(0.6..0.8) x` windows of §5.
- **The explicit-Tao lane found the problem gets worse when made explicit.** It found Tao's §5 window empty below `log x ≈ 6.27e13`.
- **Easy parts and hard parts.** The first `≍ ½ log₂ X` odd steps are governed by exactly equidistributed 2-adic bits. They reach about `X^0.79` with power-small failure, as in Terras, Everett and Korec. Descending further to `X^(1/4)` is exactly Tao's mixing problem.
- **It is also d-uniform**, as main's own card says ("may hold for cycle controls too").

**Calibration consequence.**

- **Cycles and divergence split by `d`.** Cycles exist for `d = 5, 7, 13, 61`, so excluding cycles at `d = 1` must use `d = 1` arithmetic. Hercher's `m ≤ 91` programme does this, through the Diophantine form of `2^A − 3^m`. Divergent orbits are not known for any `d`, so d-uniform tools can at most target divergence.
- **Neither candidate reaches individual orbits.** V004 and both follow-ups are d-uniform. Of the two, only V12 bears on divergence, and only in density: an "almost all" statement cannot exclude a single divergent orbit.
- **Assessment.** Both candidates relocate the obstacle. The `κ` target is the cleaner self-contained problem, with a modest payoff: it excludes one more description class. V12 is closer to (II), but it is research-hard at the level of strengthening Tao's rate.

Sources: arXiv:1809.00679 (Cor. 6–7); arXiv:1908.11244 (Thm C); arXiv:1909.03562v7 (Thm 3.1, Prop 1.17, §5); this branch's `automatic_rigidity_control.json` and `fable_L4_window_check.py`.

---

## 2026-10-18 20:55 — VERIFIED Lean V004-ii (`claude/lean-lane` `d6195bf`): the K_+ ternary closure is machine-checked

**What is formalized.** `LeanLane.Kernel.kernel_ternary_closure`, under the same two rules as V004-i. For `1 ≤ a`, `0 < r < 2^a` and `j < 3` there exist `a' ≥ 1` and `0 < r' < 2^a'` with `h(2^a(3n+j) + r) = h(2^a' n + r')` for every `n`, including `n = 0`.

**Checks.**

- **Statement match.** This is exactly V004 §3's claim that `K_+` is closed under ternary sections. The same file proves closure under binary sections (`kernel_binary_closure`), identity (3) (`id3`), and both worked examples (`h(12n+5) = h(8n+3)`, `h(12n+3) = h(64n+17)`).
- **Witnesses.** They are V004's own: `(a+2, (4c−1)/3)` when `c ≡ 1`, `(a+1, (2c−1)/3)` when `c ≡ 2`, and `(a−ℓ+4, 16u+1)` when `3 | c`. These are the same rewrites my `v004_rigidity_check.py` part (b) tested over 98,256 cases.
- **Axioms.** Exactly `[propext, Classical.choice, Quot.sound]`; some lemmas need only `[propext, Quot.sound]`. There is no `sorryAx`.
- **Source scan.** No `sorry`, `native_decide`, `decide`, `admit`, `axiom` or `unsafe`.
- **Hash.** The sha256 `d533c5fd…` matches the receipt.
- **Receipt gap (minor).** `KernelClosure.build.txt` is empty, where the earlier receipts held a timing line. The axioms receipt still shows the declarations elaborated without `sorryAx`, so I am not treating this as a defect.

**What remains for V004.** Only V004-iii, the assembly with Cobham and the finite-kernel characterization as named hypotheses. What I will check there:

- the named hypothesis is the *general* classical theorem, quantified over all sequences, not specialised to `h` or `b`;
- the kernel definitions use `k ≥ 0` and `0 ≤ j < base^k`;
- finiteness is of the set of sections as functions.

A mis-stated hypothesis could make the assembled theorem vacuous.

```sh
git show origin/claude/lean-lane:experiments/lean_lane/KernelClosure.lean | shasum -a 256   # d533c5fd…
```

---

## 2026-10-18 20:49 — VERIFIED Lean V004-i (`claude/lean-lane` `d1e5b23`): the elementary half of V004 is now machine-checked

**What is formalized.** `LeanLane.OddEP.odd_eventually_periodic_const` in `experiments/lean_lane/OddEventuallyPeriodic.lean`:

- **Hypotheses.** `h : ℕ → α`, with `h(2n) = h(n)` for all `n` and `h(3n+1) = h(n)` for odd `n > 1`. In addition, `n ↦ h(2n+1)` is periodic with period `M > 0` from some index `N` on.
- **Conclusion.** `h n = h 1` for every `n > 0`.

**Checks, from source and receipts.** This machine has no Lean toolchain.

- **Statement match.** It matches the finish of V004, from "`b` eventually periodic" to "constant". The hypotheses never constrain `h 0`, since doubling at `0` is trivial, so nothing is assumed beyond the informal statement. It holds for any colour type; finiteness is not needed for this half.
- **Axioms.** `#print axioms` gives exactly `[propext, Classical.choice, Quot.sound]` for the main theorem and every lemma. `B1`, `B2` and `B4` need only `[propext, Quot.sound]`. There is no `sorryAx`.
- **Source scan.** No `sorry`, `native_decide`, `admit`, `axiom`, `implemented_by`, `unsafe` or `opaque`.
- **Hash.** The sha256 of the `.lean` file, `cc9bbbaa…`, matches the receipt.

**The proof differs from main's prose, and I checked it by hand.**

- **Integer identities.** It uses `b(4n+2) = b(n)`, `b(3n+2) = b(2n+1)` and `b(4n) = b(3n)`. I checked each as an explicit path relation.
- **Period divisible by 3.** A period `3K` reduces to `K` by strong induction on `n mod 4`.
- **Period coprime to 6.** For a period `L` coprime to 6, set `c = (L+1)/2`, which is `1/2 mod L`. Then `b(3y+2) = b(y) = b(3(y+c))` gives a translation by `1/2`. Main uses a translation by `1/4`. Both generate `Z/LZ`.

**Scope.** This is stated honestly in the lane's `STATE.md`. V004 now rests on three pieces:

- the K_+ ternary-closure identities (V004-ii, queued, elementary);
- the assembly (V004-iii, queued);
- the two classical inputs, Cobham's theorem and the finite-kernel characterization, which are not in Mathlib and will enter as named hypotheses.

**Lean-audit close-out (C.1a, PR #2): status unchanged.**

- **The relevant certificate passed.** The comparator export of the four theorems' dependency closure (39,480 declarations) is accepted by all six kernels: nanoda, Lean paranoid, lean4lean, con-leche, con-ron and Lean default. That export is the certification the C.1a authors specify.
- **The whole-library run is different.** `lake check --paranoid` on the default targets exports about 441,790 declarations. Most of that bulk is Lean, Aesop and ProofWidgets elaborator code outside the theorems' dependency cone; con-leche reports modelling 52 inductive blocks of it. Lean paranoid, lean4lean and Lean default accept it. con-leche and con-ron reject without a reason, and nanoda is out of memory (exit 137 at a 7 GB limit).
- **Reading.** These look like checker coverage limits on meta-level code, not a defect in the theorems' cone. Recording them as unresolved is the right label.
- **Standing caveat.** The comparator ran without its sandbox (an unprivileged container), so the run is "not trustworthy" against an adversarial proof. Main's two independent replays already carry this caveat.

```sh
git show origin/claude/lean-lane:experiments/lean_lane/OddEventuallyPeriodic.lean | shasum -a 256   # cc9bbbaa…
git show origin/claude/lean-lane:experiments/lean_lane/receipts/OddEventuallyPeriodic.axioms.txt
```

---

## 2026-10-18 20:40 — REFEREE V004 (main `f54b741` / `4f1704c`): confirmed; VERIFIED Lean PR #3; plus a d-uniform version of the theorem (written proof)

**V004 verdict: confirmed as a written proof, modulo its two classical inputs.** The inputs are the finite-kernel characterization and Cobham's theorem. Checks run with this branch's own code, `v004_rigidity_check.py` parts (a)–(d):

- **Identities.** (2)–(4) hold as explicit path relations.
- **Ternary closure of `K_+`.** Checked for every `a ≤ 14`, `0 < r < 2^a`, `j < 3`: 98,256 sections, of which 65,504 are Case A and 32,752 are Case B. Every new offset stays in `(0, 2^a')`, and the integer relations hold.
- **Finish.** `b(4n+2) = b(n)` holds. `H∘J − J∘H = −1/4` is a unit for all 666 moduli `m ≤ 2000` coprime to 6.
- **Controls.** For `d = 5` the analogue `h(3m+5) = h(4m+5)` holds on the actual cycle labelling. The `d = 1` identities fail there; the first failure of `h(3u) = h(16u+1)` is at `u = 3`, with labels 1 and 19.

The Lean lane read the proof independently and found no gap. Relative to Collatz the verdict is *relocates*. As main's §6 says, automaticity of the actual bad set is equivalent to Collatz.

**New: the same proof works for every `3x + d`.** Written proof: `sidekick/writeup/D_UNIFORM_AUTOMATIC.md`.

For `gcd(d, 6) = 1`, the binary-automatic colorings with `h(2n) = h(n)` and `h(3n+d) = h(n)` (odd `n`) are exactly `h(n) = F(n mod d)` with `F` constant on `⟨×2, ×3⟩`-orbits of `Z/dZ`. For `d = 1` this is V004.

- **How it extends.** Main's `side_review.md` deferred this candidate because its closure uses positive offsets that are specific to `+1`. For general `d`, offsets leave `(0, 2^a)` only by a bounded shift. Comparing sections from a fixed index `S0` on keeps the family finite. The shift bound is 0 for `d = 1` (exactly `K_+`) and 1, 1, 2, 8 for `d = 5, 7, 13, 61`.
- **Where `d = 1` matters.** Only in the commutator step, where the translation is by `d/4`. A further all-valuations step supplies `×2`, which is V13's periodic classification.
- **Checks, part (e).** Every closure rewrite was tested on the actual cycle labellings, with no mismatch: 35,433 comparisons for `d = 5`, 59,055 for `d = 13` and 200,787 for `d = 61`.
- **Checks, part (f).** In 707 residue-graph cases, the component counts match the predicted orbit counts. The intermediate `⟨3, 4⟩` count differs from the final `⟨2, 3⟩` count: 3 versus 2 on `Z/13Z`, which is why the `×2` step is needed.

**Calibration for comparing next goals.** These are labelled remarks, not results.

1. **Non-automatic separations exist.** In `3x + 5`, the actual cycle partition among non-multiples of 5 (at least five cycles, through 1, 19, 23, 187 and 347) is non-automatic by this theorem. So non-automaticity is not evidence against a separation.
2. **The proposed `κ(D)/D` target looks d-uniform.** The `d = 5` and `d = 13` labellings already have at least 242 and 259 binary sections by depth 9. These are rigorous lower bounds from distinct prefixes (20:02 entry). The `d`-analogue of the target is consistent with this. A proof that uses `d = 1` only in the commutator step would also hold for these genuine separations. Converting it into convergence would need an upper bound on the actual bad set's section count, and none is known.

**Correction accepted.** My 20:02 phrase "the converse fails" is not a proved statement about `d = 1`, as main's `side_review.md` notes. The accurate statement is weaker: any derivation of Collatz from V004 would have to use `d = 1` beyond the commutator step, because everything else holds verbatim for `3x + 5`.

**Literature.** Shallit–Wilson (Bull. EATCS 46, 1992) show that ancestors of a fixed `x` within a bounded number of odd steps form a regular language; this description comes from Stérin, arXiv:1907.00775. That is a fixed-depth statement about ancestor languages, not about unbounded invariant classes, so it does not overlap V004. Novelty of both statements is undetermined.

**Lean PR #3 VERIFIED** (`claude/lean-lane` `fe63c9d`, now at `cf4c436`). Checked from source and receipts; this machine has no Lean toolchain.

- `LeanLane.periodic_invariant_const` matches V002 §4 in the periodic case. A colouring of the positive integers extends to `ℕ` by `h 0 := h M`, so nothing is assumed beyond the informal statement.
- The axioms are `[propext, Classical.choice, Quot.sound]`.
- `control_three_x_plus_five` uses `1_(5|n)` correctly.
- The `.lean` sha256 matches its receipt (`75607bfe…`).
- Scope: purely periodic only; eventual periodicity and the `gcd` classification are queued as 1b. Steps 2–4 of the d-uniform note would cover 1b in one statement.

```sh
python3 sidekick/probes/v004_rigidity_check.py      # ~16 s, PASS
```

---

## 2026-10-18 20:02 — REFEREE (main's proposed next goal "full automatic rigidity", `8572962`) + control data: the goal looks like it factors as a `d`-uniform step plus V13

**The proposal.** Every finite-valued 2-automatic `h` with `h(2n) = h(n)` and `h(3n+1) = h(n)` (odd `n > 1`) is constant. As a target it is:

- **well posed;**
- **strictly weaker than Collatz,** since Collatz implies it trivially and the converse fails;
- **specific to `d = 1`,** since for `d > 1` the periodic, hence automatic, coloring `1_(d|n)` is invariant and nonconstant. Its failure for `3x + d` sits exactly at V13's periodic classification.

**Control data.** This is finite evidence from `automatic_rigidity_control.py`. For `3x + d`, take the natural invariant coloring "which cycle the orbit ends in" and count its distinct 2-kernel elements, truncated to 60 terms, for levels `e ≤ 9`:

| d | cycles seen | cycle labelling, by level | `1_(d|n)` |
|---|---|---|---|
| 5 | 1, 5, 19, 23, 187, 347 | 1, 2, 4, 8, 14, 24, 42, 74, 133, 242 (growing) | saturates at 5 |
| 7 | 5, 7 | saturates at 7; the labelling **equals** `1_(7|n)` | saturates at 7 |
| 13 | 1, 13, 131, 211, 227, … | 1, 2, 4, 8, 16, 28, 48, 84, 146, 259 (growing) | saturates at 13 |

As a control, Thue–Morse saturates at 2. Any automaton for the `d = 5` or `d = 13` labelling would need at least 242 or 259 states respectively.

**Reading, a candidate structure rather than a claim.** The non-periodic invariant colorings that exist for `d = 5` and `d = 13` show no sign of automaticity, and the one automatic labelling seen (`d = 7`) is periodic. This fits a `d`-uniform statement: **every 2-automatic invariant coloring is eventually periodic**, a Cobham/Mahler-type rigidity in which `+d` plays no special role. V13's periodic classification then supplies the `d = 1` constancy.

If so:

- mechanism 3 of the proposal (a 3-Mahler relation, then Adamczewski–Bell) only needs to reach *periodicity*;
- every step before V13 can be sanity-checked against the `3x + 5` and `3x + 13` controls, where the conclusion must also hold.

Separately, verification below `2⁶⁸` already rules out nonconstant examples with fewer than 70 states for `d = 1`.

`python3 sidekick/probes/automatic_rigidity_control.py` (under 1 s; receipt alongside)

---

## 2026-10-18 19:50 — CONFIRMED (explicit-Tao L4 part 1, `e89ce02` + `478a069`): scoped barrier — Tao's printed architecture is vacuous below `log x ≈ 6.27·10¹³`

I recomputed the window certificate with 50-digit decimal arithmetic (`fable_L4_window_check.py`):

- **Window threshold.** With `α = 1.001`, the first-passage window (5.9) is nonempty iff `log x > (2·log(4/3)/(α(α−1)))⁵ = 6.274·10¹³`, that is `x > 2^(9.05·10¹³)`. The bracket at `0.999·thr` and `1.001·thr` confirms it.
- **Mixing depth.** `m₀ ≥ 1` needs `log x ≥ 10⁵`.
- **At `x = 2⁶⁸`.** The window is `I_y = [21.97, −21.48]`, so empty. The log-powers 0.6, 0.7 and 0.8 of `x` are 10.09, 14.84 and 21.81. There are 0.164 steps between scales, and `n₀ ≈ 6.8`.
- **Opening the window at `2⁶⁸`** would need `α = 1.2185`. The corrected figure in `478a069`, 1.22, matches; the earlier "2.2" was a slip.

The label **scoped barrier** is confirmed for "Tao's argument with its printed choices, constants made explicit". The further claim, that no re-optimisation within the architecture reaches `2⁶⁸`, is correctly marked a candidate.

The programme's Leg-1 post-mortem follows: no `C(δ)` at or below the verified range comes from this route, for any `δ < 1`. What survives is the explicit one-round descent (L2/L3) and the equivalence "Collatz ⇔ `B` has logarithmic density 0".

`python3 sidekick/probes/fable_L4_window_check.py` (instant; receipt alongside)

---

## 2026-10-18 19:44 — CONFIRMED (explicit-Tao L4 part 0, `a00a6c1`, as a calibration) + side-lane first-pass trace of Tao v7's `c`

**L4 part 0.** The Lean statements quoted there agree with main's independently written `lau_scope.md` §3.2:

- the Fourier decay `C_*·n^(−10241/4096)`, with `C_* = (160D_*)^(10241/4096)`;
- mixing only for `2^80000 ≤ m ≤ q`;
- the generation threshold `N_* = 6103914`;
- the challenge constants.

The order of magnitude also checks out: `3^(2^80000)` has about `10^24082` digits. Label **calibration** confirmed. The conclusion that this route adds only the trivial row at `δ = 1 − 2^(−2^(2^87640))` follows.

**Side-lane trace of Tao v7.** This is a first pass from the HTML, sent to the session to check against the PDF.

- **Theorem 3.1** gives `≪ (log N₀)^(−c)`, where `c` is a "small absolute constant" with no value given.
- **Remark 1.4** gives `C_δ ≪ exp(δ^(−O(1)))`.
- **Props 1.14 and 1.17** hold as `O_A(·^(−A))` for every `A`, with unspecified constants.
- **Where `c` is set (§5).** The mixing error is not the bottleneck, since `A` is free. The binding terms are the first-passage window (5.16) and the target error (5.7/5.20).
- **Parameters are tied to `log x`:** `n₀ = ⌊log x/(10 log 2)⌋` and `m₀ = ⌊(α−1)/100·log x⌋`, with windows `log^0.6`, `log^0.7` and `log^0.8` of `x`.

At `x ≈ 2⁶⁸`, `log x ≈ 47`, so `n₀ ≈ 6`, `m₀` is 0 unless `α > 3.1`, and the windows are about 10, 15 and 22. Every error term is `O(1)`. Read this way, Tao's architecture cannot give `C(δ) ≤ 2⁶⁸` for any `δ < 1`, even with optimal explicit constants. That target would need a structurally different argument, not sharper constants. This is a candidate barrier for the programme to record before assembling L5–L6.

---

## 2026-10-18 19:39 — LEAD (explicit-Tao L4): explicit mixing constants already exist, machine-checked, inside the audited C.1a Lean library

For the `claude/explicit-tao` programme's next unit, L4 (the explicit mixing of the Syracuse random variables). The audited library `AxiomMath/CollatzPositiveDensity` at `3a38bfbb` proves the following inside its own chain (main's `lau_scope.md` §3.2):

- **`FourierDecay.ChPrimitiveDecay`.** `|μ̂_n(ξ)| ≤ C_*·n^(−10241/4096)` for unit `ξ mod 3^n`, with `C_* = (160D_*)^(10241/4096)`.
- **`Mixing.Mixing`.** The mixing bound `2C/(3m^(3/2))`, valid only for `2^80000 ≤ m ≤ q`.
- **Seed lemmas.** These hold from `n ≥ 6000000`.

They are not imported axioms, and the library builds with only the standard axioms on two independent replays. So L4's constants can be read from the Lean statements instead of being re-derived from Tao v7.

**Calibration.** The mixing threshold `m ≥ 2^80000` suggests any `C(δ)` assembled from these constants will be astronomically far above `2⁶⁸`. That would show the `C(δ) ≤ V` target needs a much sharper mixing estimate than any now available, which is worth establishing before assembling L5–L6. I have sent this to that session.

---

## 2026-10-18 19:36 — CONFIRMED (explicit-Tao programme, branch `claude/explicit-tao` `88d2424`): L2/L2′/L3 hold; four displayed rate values in the lemma note are mistyped (the receipt is correct)

The side lane now checks the `claude/explicit-tao` branch while main is paused. That branch tries to make Tao's 2019 theorem explicit.

This branch's own check (`fable_L2_check.py`; nothing imported) covers:

- **(2) Chernoff.** `P(A_n ≤ t) ≤ exp(−n I(t/n))` holds against the exact law `C(A−1, n−1)/2^A` for every `n ≤ 60` and `θ ∈ [1.3, 1.95]`. The worst ratio is 0.61.
- **The rate formula.** It matches direct numerical minimisation over `u`.
- **The word count.** It equals `C(⌊t⌋, n)` (hockey-stick identity).
- **L2′ on actual integers.** At `X = 2²⁰`, `n ∈ {6, 8, 10}`, `θ ∈ {1.6, 1.7, 1.8}` and `d ∈ {1, 5}`, every count is below the bound.
- **L3.** The affine identity with the term `d·C_w` holds, as do `0 < C_w/2^A ≤ (3/2)^n − 1` and the descent inequality: 4,000 random odd `N < 2⁶⁴` with `n ≤ 40`.

**Minor correction.** The "Explicit values" line in `L2_valuation_tail.md` misquotes four rates:

| θ | true `I(θ)` | quoted |
|---|---|---|
| 1.5 | 0.084950 | 0.08530 |
| 1.6 | 0.050534 | 0.05054 |
| 1.7 | 0.026610 | 0.02663 |
| 1.8 | 0.011134 | 0.01112 |

Three of the four are overstatements, which is the unsafe direction for an exceptional-set bound. The checker's `rate()` and `receipts/L2_receipt.json` carry the correct values, so no computation is affected.

L2 and L3 are calibration-level, as the note says (Terras, Everett, and Lagarias's Theorem B). The crux remains L4, the explicit mixing of the Syracuse random variables.

**Update 19:39.** The branch corrected the quoted values in `e01d62f`. They now match this probe to six decimals: 0.084950, 0.050534, 0.026610, 0.011134 and 0.002633.

`python3 sidekick/probes/fable_L2_check.py` (about 4 s; receipt alongside)

---

## 2026-10-18 19:13 — LEAD (side-lane viewpoint S2): ×2×3 rigidity as the theoretical home of V13

No new main commits since 18:45. Main's 14 cards do not include the classical rigidity theory of the pair `×2, ×3`. The V13 results already sit inside it:

- Furstenberg (1967) and Rudolph (1990) on `×2`- and `×3`-invariant sets and measures;
- Cobham (1969), its automata analogue, which V13 already uses;
- V13's periodic classification, which is the clopen case on the profinite integers `Ẑ`.

The `+1` is the affine twist, and the commutator shift by `d` measures it. For `3x + d`, the clopen set `dẐ` is a nontrivial invariant set.

The cheapest test is a literature check on affine-semigroup versions of these theorems, plus one finite question: must every nonempty union of components meet every residue class mod every `M`? That milestone is strictly weaker than Collatz and stronger than V13's periodic result. The full seven-item card is in `sidekick/VIEWPOINTS.md` (S2).

---

## 2026-10-18 18:46 — REFEREE (V003): digit-count rigidity confirmed; V13 stays promising, and the crux is the mixed ternary sections (main `2ac44ef`)

This branch's own check (`v003_digit_count_check.py`) covers:

- **The identity family.** For `n_k = 32(2^k − 1) + 9`, `s₂(n_k) = k + 2` and `s₂(3n_k + 1) = k + 3`, for every `k = 2..3000`.
- **Small weights.** The sources 5, 13 and 23 connect weights 1 to 4.
- **Cross-check.** Union-find over every odd `n < 2·10⁵` puts all binary weights in one class.
- **Controls.** `1_(5|n)` and `1_(61|n)` do not factor through the digit count `s₂` (witnesses 3 vs 5 and 31 vs 61). Thue–Morse fails at `5 → 16`.

So every invariant coloring of the form `F(s₂(n))` is constant, with no assumption on `F`. The proof is correct and elementary.

**Verdict.** This is real but narrow progress within V13: it covers digit counts modulo every `m`. As main says, the binding question is closure of the mixed ternary sections. The 70-state remark from 18:43 still applies: by verification below `2⁶⁸`, any nonconstant 2-automatic invariant coloring has at least 70 states. So progress needs structural arguments; enumerating small automata cannot help.

`python3 sidekick/probes/v003_digit_count_check.py` (under 1 s; receipt alongside)

---

## 2026-10-18 18:42 — NOTE: second independent replay of the C.1a Lean artifact agrees with main's (lane 3, `claude/lean-audit` `5260896`, draft PR #2)

A separate Claude lane built `AxiomMath/CollatzPositiveDensity` at `3a38bfbb` from source. It used an isolated Linux container (Ubuntu 24.04, aarch64), `leanprover/lean4:v4.35.0-rc2` and Mathlib `0653561`. Results:

- **Build.** `Build completed successfully (4107 jobs)`, with no errors and no `sorry` warnings.
- **Axioms.** `#print axioms`, run in a fresh process, gives only `propext`, `Classical.choice` and `Quot.sound` for all four theorems.
- **Statements.** The `pp.all` statements and the seven definitions they use are byte-identical between `Challenge.Basic` and `Solution.Basic`.

Main's macOS replay at `5a11fcb` found the same. C.1a's input therefore has a machine-checked proof at the pinned commit, replayed on two platforms with the same kernel implementation. It is a positive proportion of integers reaching any `t` with `3 ∤ t`, with tower constants and a logarithmic clock.

**Still running in lane 3:** `lake comparator` (Lean kernel plus nanoda), then the paranoid external checkers. Inside Docker the comparator runs without its own nested sandbox; the container is the sandbox.

**Scope.** This says nothing about the paper's prose, about transfer to `3x + d`, or about C.2a, which remains open.

The receipts are in `experiments/lean_audit/README.md` on that branch. I confirmed that the commit and its receipt files exist; nothing was rerun here.

---

## 2026-10-18 18:24 — REFEREE (V002): V13 confirmed and rated promising; V11, V12 and V14 relocate the obstacle; ACK main's corrections to S1 and V3 (main `cdfb143`)

**V13 (selected by main).** I checked its periodic classification with this branch's own code. For `M ≤ 400` and `d ∈ {1, 5, 7, 11, 13, 61}` (2,400 cases), the components of the residue graph mod `M`, with edges `r – 2r` and `r – 3r + d` on odd residues, equal the `⟨×2, ×3⟩`-orbits on `Z/gcd(M, d)Z`. For `d = 1` the count is always 1. The controls `1_(d|n)` are invariant for `d = 5` and `61`.

This is the cleanest non-transferable statement so far: periodic invariant colorings are constant iff `gcd(M, d) = 1`.

On the milestone, two remarks:

- Verification below `2⁶⁸` already forces any nonconstant 2-automatic invariant coloring to have at least 70 states, by the shortest-accepted-word argument.
- `n ↦ 3n + 1` is a finite binary transducer, so invariance is decidable for each automaton, and the classification asks for finite invariant partitions under that transducer.

Verdict: **promising**.

**Others.** V11 (occupation measures) and V12 (ensemble information) move the obstacle to uniform quantitative control of the non-absorbed set. V14 (carry diagrams) relocates it too, but it is a natural tool for V13's automaton question.

**ACK.** Main's corrections to the density card stand:

- the result is a dichotomy, "empty or positive lower density", not literally zero–one;
- `c(a)` depends on the target, with infimum 0, so no single threshold works;
- Tao v7 Theorem 3.1 has unspecified constants.

The card is renamed S1 to avoid main's V11. The V3 wording is softened to "relocates; the relaxation is already solved". All changes are in `sidekick/VIEWPOINTS.md`.

`python3 sidekick/probes/v13_coloring_check.py` (about 1 s; receipt alongside)

---

## 2026-10-18 18:08 — REFEREE (viewpoint survey V001) + CONFIRMED (P6-004 labels none) + D7 status (main `bff8938`)

**Viewpoints.** The full sheet is `sidekick/VIEWPOINTS.md`. In short:

- **V1, V2, V4, V8, V9:** they relocate the obstacle.
- **V3:** a known dead end for the strong form (Applegate–Lagarias 2006 prove only the weak form).
- **V5:** equivalent as stated.
- **V7:** a tool only.
- **V10:** a control language.
- **V6:** promising as a measurement language, with a milestone strictly weaker than Collatz.

All ten send the difficulty to one of two places: **(I) integer realization** (V1–V3, V8–V10), or **(II) uniform control of the non-absorbed set** (V4, V6). By main's own rule, that points the next survey toward languages that act on both at once.

**Probe checks.** Main's concrete claims reproduce with this branch's own code:

- the `(1,4)` composite on `x ≡ 3 (mod 64)` (1,563 starts), and `35` with word `(1,5)`;
- the `3x+5` fixed point `19d/5`;
- Applegate–Lagarias `C⁶(5x) = (45x+5)/64` (2,000 members);
- the potential value `u = 1/(1+5T) ≈ 0.6621`, within `[9/14, 13/18]`.

**V11, proposed by the side lane: a zero–one law.** Given C.1a, `B` is either empty or has positive lower density. So Collatz ⇔ `liminf B(X)/X = 0`, and density control of `B` is all-or-nothing. This explains why the density theorems (Terras, Korec, S.1, Tao) stall: they control other sets. For `3x + d`, the multiples of `d` give an exact copy of Collatz that never reaches 1 (`S_d(dy) = d·S₁(y)`), which is the control. Next test: the quantitative form of Tao's estimate at a fixed height, combined with verification below `2⁶⁸`, to bound `B`'s logarithmic density explicitly. The card is in `VIEWPOINTS.md`.

**P6-004.** Both labels **none** are confirmed. C.1a is labelled none under the explicit-constant rubric, and the C.2a attempt failed as recorded.

**D7.** Main's replay meets items 1–4:

- a source build of the library in a network-denied macOS sandbox, with Mathlib from its official cache;
- `#print axioms` on all four theorems shows only `propext`, `Classical.choice` and `Quot.sound`;
- the statements match the side lane's reading.

The caveat is that this used the same kernel and prebuilt Mathlib. A second, Linux replay is pending in draft PR #2.

`python3 sidekick/probes/viewpoint_v001_check.py` (under 1 s; receipt alongside)

---

## 2026-10-18 17:58 — NOTE: an independent Lean build audit of C.1a is in progress elsewhere; main's 17:10 gate run was interrupted

**External lane.** A separate Claude lane is running D7 items 2–4 on the AxiomMath artifact (`3a38bfbb`): a from-source build in an isolated container, `#print axioms` on the four theorems, and a comparison of the challenge and solution statements. It works on branch `claude/lean-audit` with draft PR [stgoa/collatz#2](https://github.com/stgoa/collatz/pull/2) (`experiments/lean_audit/README.md`). It does not write to `main` or `claude/sidekick`.

**What that lane reports so far.** These are its claims, not rechecked here, apart from the PR's existence.

- **Toolchain.** The pinned toolchain `v4.35.0-rc2` contains the kernel soundness fix (lean4 PR #14577).
- **Tree scan.** Across 743 `.lean` files, the only `sorry` hits are the four challenge statements plus one lakefile comment. There are no `admit`, `native_decide`, `implemented_by`, `extern`, `unsafe` or `axiom` declarations.
- **CI.** The green CI runs restored a lake cache, so they certify little; the from-source build is the real test.
- **Status.** No verdict yet.

**Housekeeping.** The other lane reports that it accidentally terminated main's `verify_all.py --cpp --transfer-controls` run (PID 18053) at about 17:12. Its log `/private/tmp/collatz_phase6_linear_density_gate.log` was created at 17:10 and is empty, and the process is gone. That gate run needs to be repeated before the P6-004 batch can be delivered.

---

## 2026-10-18 16:57 — FINDING (D7, item 1): the AxiomMath Lean statements match C.1a; the proofs are in an unbuilt library

I read the source text of `Challenge/Basic.lean` at the pinned commit `3a38bfbb`; nothing was built. Its four theorems state a positive lower density of starts `n < N` that reach a target `t` within logarithmic time:

- the target `t = 1`;
- odd starts;
- targets `t` coprime to 6;
- targets `t` with `3 ∤ t`.

The constants are towers: `c = 1/2^2^2^87640` and `X₀ = 2^2^2^2^87640`. This matches what C.1a needs. Under it, C.3 would need only that the nonabsorbing set has density zero.

`Solution/Basic.lean` re-exports four modules of `CollatzPosDens` and has no `sorry`, `admit` or `native_decide` in that file. The proofs, axioms and build remain unaudited here: no Lean toolchain is installed on this machine. Details and the remaining audit items are in `DIRECTIONS.md`, D7.

---

## 2026-10-18 16:56 — CONFIRMED (P6-003, node S.2, label barrier) (main `2e619a2`)

**What is barred.** First-half transport cannot contract the power-growth norm on arbitrary targets, for any `0 < α < 1`. The proof has three parts:

- **Theorem 1:** the one-arrow suboperator does contract, by a factor below `10/13`, for `α ≥ 4/5`.
- **Theorem 2:** four explicit paths of at most two arrows give expansion `K(α)` for `α ≤ 7/8`.
- **Theorem 3:** first-crossing word codes plus averaging over residues cover every `α < 1`.

This branch's own check (`p6_003_growth_norm_check.py`; nothing imported from main) covers:

- **The four paths.** For `d ∈ {1, 5, 7, 13, 61}` and every `y ≡ 5d (mod 18)` below `10⁵`, 27,773 targets in all, the sources have exact words `(3)`, `(5)`, `(2,3)` and `(1,5)`. They first-half descend to `y` at times 1, 1, 2 and 2, and all four are distinct.
- **The constant `K(α)`.** The four integer inequalities in (9) and `241/240` hold. On a grid, `K(α)` is 1.059 at `α = 7/8`, 1.023 at `0.9` and 0.954 at `0.95`. So Theorem 3 is needed near `α = 1`, as the note says.
- **The count formula (5).** It holds exactly for `α ∈ {1/2, 2/3, 7/8}` and `d ∈ {1, 5}`, at every `X ≤ 2·10⁴`, using integer roots.
- **Theorem 3's mass bound.** An exact dynamic program over first-crossing words gives `p₉₀ = 0.99772`, above `1 − δ_m − 2^(−L)` for every split `m = 9..15` of `B = 90`. For `α = 0.9`, `p_B` already exceeds `2^(α−1)` at `B = 30`. The identity behind (15) holds termwise.

Label **barrier** confirmed. The ledger's decision to stop adding exponent variants, and its acceptance of D6, are noted.

`python3 sidekick/probes/p6_003_growth_norm_check.py` (under 1 s; receipt alongside)

---

## 2026-10-18 16:32 — CONFIRMED (P6-002, node S.2, label barrier) (main `de32608`)

The proof is correct and elementary. The named method is a transport bound with a constant `κ` over arbitrary target sets: `Σ_(y∈A) M_X(y) ≤ κ|A| + o(X)`. It is refuted for every finite `κ` and every supported `d`. One-arrow preimages `n = (2^a·y − d)/3` for `a = 3..J` give each target about `J/2` first-half sources, which makes the excess linear in `X`.

This branch's own check (`p6_002_transport_check.py`; nothing imported from main) covers:

- **The construction**, 1,122 cases with `d ∈ {1, 5, 7, 13, 61}`, `J = 3..8` and `t ≤ 40`. Every `n(a, y)` is odd and below `X_t`, with `v2(3n + d) = a`, `S_d(n) = y` and `2y < n`. All sources are distinct, and the exact counts `N_t` and `|A_t|` hold.
- **Brute force**, 78 cutoffs. Here the full transported mass into `A_t` is computed by iterating every odd `n ≤ X_t`, with cycles detected for `d = 5` and `61`. It is at least `N_t` in every case.
- **The sparse set.** Its count formula (15) holds exactly for `α ∈ {1/2, 1/3, 2/3, 3/4}` and every `Y ≤ 3·10⁴`, and its preimages are one arrow long.
- **Both singleton controls.** `L₁` sends `(10·4^j − 1)/3` to 5, and `L₅` sends `(38·4^j − 5)/3` to 19, which lies on the raw cycle `19 → 31 → 49`.

Label **barrier** confirmed.

**Observation.** The construction shows where the mass comes from. A target `y` has about `log₂(X/y)/2` one-arrow first-half preimages up to `X`, so the natural weight for transport is logarithmic in scale. That is the weighting behind logarithmic density, Tao's setting. The barrier leaves weighted transport and estimates specific to `B` open, as stated.

`python3 sidekick/probes/p6_002_transport_check.py` (about 7 s; receipt alongside)

---

## 2026-10-18 16:13 — CONFIRMED (P6-001, node S.1, label calibration; secondary S.2 label none) (main `546e891`)

I checked the proof line by line and ran this branch's own code (`p6_001_stopping_check.py`; nothing imported from main). It covers:

- **Parity lemma.** For the shortcut map `C_d`, length-`k` parity words biject onto residues mod `2^k`. On odd residues, `p − 1` is exactly `Binomial(k − 1, 1/2)`. Checked for `k ≤ 14` and `d ∈ {1, 5, 7, 13, 61}`, 70 cases.
- **Bad-class bound.** `δ = B/2^(k−1) ≤ (8/7)(16807/18432)^m` holds in exact rationals for `m = 9..120`. Tolerances `1/10` and `1/100` give `m = 34` and `59`, that is, horizons 170 and 295, as stated.
- **Good words.** For `m = 9` and `d ∈ {1, 5, 61}`, 1,095 random odd `n ≥ Z` with `p ≤ 27` satisfy `C⁴⁵(n) < n/2`. In each, the `p`-th odd-map iterate equals `oddpart(C⁴⁵(n))`.
- **W5 pullback.** For all 25,000 `w ∈ W5` below `2·10⁵`, `q = ν(3w)` lies in `{3w, (3w − 1)/2}`, follows the stated branch, has `q ≥ 7`, and is injective in `w`. `T^j(q) = ν(S^j(q))` holds. Half-descent implies `9T^j(q) + 5 < 8q` (22,601 cases within 24 steps).
- **Cited benchmark.** For `k = 6..16` and large `n`, the share of `{n : C^k(n) < n/2}` equals Borovkov–Pfeifer's `2^(−k)·Σ_(j < (k−1)/log₂3) binom(k, j)` exactly.

**Scope note.** The constants are explicit but very loose. The residue-counting term `B` dominates `X₀`: `ε = 1/10` needs `X ≥ ~10⁵⁰`, and `ε = 1/100` needs `X ≥ ~10⁸⁸`. This is inherent to counting residues mod `2^k`: the horizon `k` can only be about `log₂X`. The label **calibration** is confirmed. The statement carries over to every `d` (Sections 1–5); the pullback is specific to `d = 1`.

`python3 sidekick/probes/p6_001_stopping_check.py` (about 1 s; receipt alongside)

---

## 2026-10-18 15:52 — CONFIRMED (pin): P6-000 as committed in `b901e11`, label none

I re-verified the committed `experiments/phase6/cycle_fixtures.json` with this branch's own `3x + d` step. All 11 cycles pass, the same as in the 15:39 check of the working copy. The setup label **none** at node MAP is confirmed for this commit. `AGENTS.md` and `ROUTE_MAP.md` now carry the no-waiting protocol, so D5 is closed.

---

## 2026-10-18 15:39 — ACK: main's P6-000 answers to D1–D4 (main working copy on `9190ccf`)

The ledger accepts D1 and D2, defers D4, and rejects D3. The rejection is correct. D3 said that density results carry over to `3x + d`. That holds for stopping-type statements, such as fixed-factor descent, but not for "almost all reach 1": for `d > 1` the multiples of `d` have positive density and never reach 1. `DIRECTIONS.md` records the correction.

The draft route map now runs without approval gates, so D5 is moot. The chosen first node is S.1, calibration of fixed-factor stopping with explicit counts and the W5 pullback, which matches D3 as corrected.

---

## 2026-10-18 15:38 — CONFIRMED (Phase 6 setup, node MAP, label none): the transfer-harness cycle fixtures; route map reviewed (main working copy on `9190ccf`)

**Fixtures.** I verified all 11 cycles in `experiments/phase6/cycle_fixtures.json` with this branch's own `3x + d` step. Every arrow, every exact valuation, distinctness before closure, and the stated minimum are correct:

| d | cycle minima (lengths) |
|---|---|
| 5 | 1 (1), 19 (3), 23 (3), 187 (17), 347 (17) |
| 7 | 5 (2) |
| 13 | 1 (1), 131 (15), 211 (5) |
| 61 | 1 (1), 235 (41) |

They agree with the side lane's own scan of starting values below 20,000, which also lists further `d = 13` five-cycles with minima 227, 251, 259, 283, 287 and 319. The setup label **none** at node MAP is confirmed.

**Route map, read as a draft.**

- The nodes follow D1 closely. The transfer statements are careful. Highlights:
  - C.2 fails for every `d > 1` through the multiples of `d`, with no extra cycle needed.
  - C.3 uses `a = S(n)`, which is never divisible by 3.
  - H.2 notes that analyticity in the disk is automatic.
- Under D3, S.1 carries over to every `d`, so it can yield only calibration (b). C.2 and S.2 are the nodes where a non-transferable step must enter.
- The Y.1 reference to a 2026 corrigendum of Hercher's result was not checked here.
- The draft's approval gates read differently from the no-waiting protocol in `DIRECTIONS.md`. The gates are: user approval before node work, a stop after setup, and a stop for the user's next-node choice. See D5.

Reproduce: run the loop shown in this entry's commit message over the fixture file, with `T_d(x) = (3x + d)/2^v2(3x + d)`.

---

## 2026-10-18 11:32 — VERIFIED: the arithmetic parts of R15, R18, R21 and R29 (main `9190ccf`)

This uses this branch's own `S` and `ν`. Statements that need the annular measure `A_N` are not checked here: source and cluster masses, residual profiles and the `21N/4` bound.

- **R15.** For every odd `y < 10⁶`, a strictly smaller ancestor within two Syracuse steps exists exactly when `y ≡ 5, 11, 13, 17 (mod 18)`. That gives 222,221 such `y` and 277,778 without one. In each case the stated move is such an ancestor, via an exact path, and lies below `8y/9`: `(2y − 1)/3` for `y ≡ 5, 11`, `(8y − 5)/9` for `y ≡ 13`, and `(4y − 5)/9` for `y ≡ 17`.
- **R18.** On all odd `y < 10⁶`, the graph `E0` has in-degree and out-degree at most 1 (by brute force below 3000), no two consecutive valuation-2 arrows, two-step backward contraction below `8/9`, and no incoming arrow exactly on `{1, 3, 7, 9, 15} (mod 18)`. For the Mersenne family `L = 12 + 6k` with `k ≤ 12`, the states `x_j` form an `E0` path. Its first forbidden exit has valuation `3 + v2(L)` and lands at `w = (3^L − 1)/2^(2+v2(L))`. For odd `k`, `w ≡ 1 (mod 18)` is an inactive root.
- **R21.** For all odd `x < 2·10⁵` (41,666 allowed steps), the adjusted height grows by a factor above `3/4` from type 1 and above `3/2` from type 2, and a shrinking step always lands on type 2. The separation bounds 58 and 63 follow from `(9/8)^(m/2) < 32` and `(3/4)(9/8)^k < 32`.
  - **Sharp path.** For `t = 1..5`, the path from `x = 3·2⁹⁵·t − 5` has word `(1,2)³¹,1`, cost 94, lies inside `E0`, and has both ends in `(Q, 32Q)`.
  - **Forbidden edges.** Each of the 16,666 valuation-2 forbidden edges lands on a smaller inactive root. Each of the 25,000 with valuation 3 or more lands in a component whose root is below `x/4`.
- **R29.** Let `Q` be the `T`-closure of all canonical states below 3000, which has 1,269 states and maximum 252,233. Then:
  - `W_Q = {S(q), 3q + 2}` has `|W_Q| = 2|Q|` and `max W_Q = 3·max Q + 2`, and `S(W_Q) ⊆ W_Q`;
  - every odd `x < 2·10⁶` with `ν(x) ∈ Q` has `S(x) ∈ W_Q` (12,866 such `x`), and every element of `W_Q` is attained;
  - sampled `x` reach 1 within `1 + 2|Q|` arrows;
  - `S(x) ≤ 3ν(x) + 2` for all odd `x < 2·10⁶`;
  - `S⁴(327) = 415` and `S⁹(327) = 1579`.

`python3 sidekick/probes/batch_r15_r18_r21_r29_check.py` (about 3 s; receipt alongside)

---

## 2026-10-18 10:58 — FINDING (Q1): the absorbed share of `A_N`'s positive mass depends on the depth, not on `N`

For `N = 96·2^k` with `k = 0..9` (up to 49,152), the probe exposed the forward graph depth by depth from every source of `A_N`, as `depth_probe.py` does. At each depth it recorded the share of positive mass whose component contains 1.

| N | depth for 50% | 90% | 99% | 99.9% | 100% | 100% resolved | unabsorbed at depth 4 / 8 / 16 / 32 / 64 |
|---:|---:|---:|---:|---:|---:|---:|---|
| 96 | 3 | 8 | 28 | 33 | 33 | 28 | 17.17% / 9.01% / 2.36% / 0.13% / 0 |
| 192 | 2 | 7 | 26 | 28 | 42 | 28 | 19.13% / 8.69% / 3.16% / 0.04% / 0 |
| 384 | 2 | 7 | 23 | 41 | 42 | 42 | 16.52% / 7.91% / 2.02% / 0.38% / 0 |
| 768 | 2 | 7 | 22 | 41 | 73 | 63 | 17.01% / 8.53% / 2.54% / 0.26% / 0.02% |
| 1,536 | 2 | 7 | 22 | 52 | 63 | 63 | 17.21% / 7.63% / 2.59% / 0.32% / 0 |
| 3,072 | 2 | 7 | 24 | 52 | 66 | 60 | 16.88% / 7.85% / 2.66% / 0.39% / 0.003% |
| 6,144 | 2 | 7 | 24 | 45 | 94 | 64 | 17.14% / 7.87% / 2.39% / 0.39% / 0.009% |
| 12,288 | 2 | 7 | 24 | 47 | 96 | 96 | 16.81% / 7.71% / 2.48% / 0.43% / 0.03% |
| 24,576 | 2 | 7 | 25 | 49 | 116 | 116 | 17.13% / 7.99% / 2.56% / 0.46% / 0.04% |
| 49,152 | 2 | 7 | 25 | 50 | 113 | 113 | 17.24% / 8.04% / 2.61% / 0.48% / 0.04% |

- **The bulk is scale-free.** As `N` grows by a factor of 512, the depths for 50%, 90% and 99% stay at about 2, 7 and 22–25. The unabsorbed share at a fixed depth barely moves: about 17% at depth 4, 8% at depth 8, 2.5% at depth 16 and 0.4–0.5% at depth 32.
- **Only the extreme tail grows.** The last positive source joins at depth 33 for `N = 96` and at depth 113 for `N = 49152`, about `7.3·log₂N` at the top of this range.
- **Counting nonpositive components.** "100% resolved" also counts components of nonpositive total mass as done. That lowers the last depth in 5 of the 10 cutoffs, but not in the three largest.

In the measured range this answers Q1 more strongly than it asked. A fixed depth `d` already absorbs all but a share `ε(d)` of the positive mass, where `ε(d)` hardly depends on `N` and falls more slowly than exponentially here. Only that thin remainder needs depth growing like `log N`. These are finite data: no asymptotic claim is made, and nothing is said about the remainder's structure.

`python3 sidekick/probes/q1_giant_component.py` (about 15 s; receipt alongside)

---

## 2026-10-18 10:25 — FINDING (Q2): a protected chain ends when its own orbit returns to the source support

This uses the setting of `depth_probe.py` (main's unbounded-exposure-depth family): the chain `y_k = 3^k X/2^k − 1` with sources `(−2, +2, +2)`, and `D = 1..4` with four admissible `X` each. That gives 16 runs and 13 distinct cutoffs, with `N` from 312 to 63,816.

**An exact identity.** The exposure graph is a functional forest rooted at 1. So the chain's component contains 1 exactly when every edge of the forward orbit `O = (y₁, S(y₁), …, 1)` has been exposed. A source `s` that first meets `O` after `j_s` steps, at `O_(p_s)`, exposes edge `q ≥ p_s` at step `j_s + q + 1 − p_s`. Hence

    link depth = max over edges q of O of  min over sources s with p_s ≤ q of  dist(s, O_(q+1)).

An independent union-find exposure agrees with this formula in all 16 runs.

**Where the bottleneck sits.** The support of `A_N` ends at `144N`, while `y₁ = 64N − 1` climbs for `L = 8..11` valuation-one steps far above it. No other source lies on that excursion. In every cutoff the bottleneck edge comes after the climb, close to the orbit's first return to `≤ 144N`: one or two edges before it in 11 cutoffs, and three edges after it in 2. The link depth equals the return index minus 2, plus between −1 and +4.

| X | N | climb L | return to ≤ 144N | bottleneck edge | link depth | end depth | steps to 1 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 13312 | 312 | 8 | 10 | 13 | 11 | 11 | 59 |
| 40960 | 960 | 11 | 27 | 26 | 25 | 13 (mass) | 104 |
| 68608 | 1608 | 8 | 19 | 22 | 21 | 21 | 48 |
| 96256 | 2256 | 9 | 12 | 11 | 9 | 9 | 32 |
| 151552 | 3552 | 10 | 12 | 10 | 9 | 9 | 82 |
| 234496 | 5496 | 8 | 12 | 11 | 9 | 9 | 62 |
| 317440 | 7440 | 9 | 18 | 17 | 15 | 15 | 46 |
| 483328 | 11328 | 11 | 13 | 11 | 10 | 10 | 74 |
| 732160 | 17160 | 8 | 16 | 15 | 14 | 14 | 39 |
| 980992 | 22992 | 9 | 35 | 34 | 32 | 32 | 98 |
| 1229824 | 28824 | 8 | 15 | 14 | 12 | 12 | 70 |
| 1976320 | 46320 | 9 | 34 | 33 | 32 | 32 | 86 |
| 2722816 | 63816 | 8 | 35 | 34 | 33 | 33 | 121 |

The end depth is the link depth, except at `X = 40960`. There the component's mass becomes nonpositive at depth 13, before it links at depth 25.

**Answer to Q2 for this family.** The end depth is not the climb length, and not the stopping time of the climb's top: the step after the top always descends. It is the length of the chain orbit's excursion above the source support, which is `L` plus the time for the top to fall back to `2.25·y₁`. In other words, the plateau is a stopping-time quantity of the chain's own orbit, and the other sources cannot shorten it because none of them lies above `144N`. These are finite data around an exact identity; no general claim is made.

`python3 sidekick/probes/q2_end_depth.py` (about 2 min; receipt alongside)

---

## 2026-10-18 09:40 — VERIFIED: R42's joint-source interface, the 3 mod 32 block, the expanding family and the required-ray embedding (main `9190ccf`)

This uses this branch's own `S` and `ν`; nothing is imported from main. The retained-graph residual weight `R_N(x_r) = 1` in (12) uses the annular residual machinery and is not checked.

- **Interface for `C(v) = [18v + 3] − [v]`.** Both cases hold for all `v ≡ 3 (mod 4)` below `2·10⁵` plus 5,000 random 122-bit `v`, 55,000 cases in all:
  - `v ≡ 3 (mod 8)`: `S²(v) = z = (9v + 5)/2^(a+1)` and `S²(18v + 3) = 9·2^(a−1)z − 7`;
  - `v ≡ 7 (mod 8)`: `S²(v) = (9v + 5)/4` and `S²(18v + 3) = oddpart(9z − 7)`.
- **The `3 (mod 32)` class.** There were 15,500 cases. In each:
  - `u = S(t) = (9v + 5)/2^(h+3) ≤ (9v + 5)/32 ≤ v/3`;
  - the block (6) gives `S^(3+2j)(18v + 3) = q = 2^s·3^(2j+3)·u − 5` and `S²(v) = u`, with `q ≡ 22 (mod 27)`.

  Parametrization (4) also holds in the converse direction, for 8,443 pairs `(h, u)` with `h ≤ 39`. The two exact arrows (5), with valuations 1 and 2, hold in 3,000 random cases. These arrows are the 2-adic shadow of the negative cycle `{−5, −7}`.
- **Expanding family, `r = 0..12`.** These hold:
  - `S²(v_r) = 1` with word `(1, 6r + 4)`;
  - `18v_r + 3 = 2^(6r+6) − 7`;
  - `S^(4r+3)(18v_r + 3) = q_r = 2·3^(4r+3) − 5` with word `(2,1,2)(1,2)^(2r)`;
  - `q_r` is canonical, `≡ 1 (mod 8)` and `≡ 1 (mod 3)`, and `S(q_r) = (3^(4r+4) − 7)/2`.
- **Embedding, `r ∈ {9, 18, 27, 36, 54, 81, 108}`.** These hold:
  - the congruences of `w`, `t₀`, `x` and `p`, with `v2(x + 1) = 2` and `v2(3t₀ − 1) = 4`;
  - the four-arrow certificate (9), `p → w → F(v) → S(v) → 1`, with valuations `5, 2, 3, h + 2`;
  - the upper prefix `S³…S⁶`;
  - (10), `S^(4r+7)(x) = q_r`, with word `(1,2,2,1,3,3,2)(1,2)^(2r)`;
  - the identity `81(q_r − x) = 4374·81^r − 32768·64^r + 2960`, with `q_r > x`.

  For `27 | r`, `x = x_r = (2^(6r+15) − 3365)/81`, `x_r ≡ 3 (mod 12)`, `N_r < x_r < 9N_r/8` and `p < N_r`.

`python3 sidekick/probes/r42_joint_frontier_check.py` (under 1 s; receipt alongside)

---

## 2026-10-18 09:07 — VERIFIED: the arithmetic of R89 — window, three-node family, retained cell and the 25-arrow path (main `9190ccf`)

This uses this branch's own `S` and `ν`. The planner (`J_s`, `A_s`, the dispatcher) is not rebuilt, so statements about which plans pass are not checked here. "First exponent" is read in the R26 sense, `v2(x + 1)`.

- **Window (1).** There were 4,000 random W9 pairs `(C, Q)`: 1,287 with odd `d` and 2,713 with even `d`. In each:
  - `d = v2(9C − 1) ≥ 4`;
  - the actual `(h + 2)`-arrow prefix from `3C` ends at `F = 4(3z) + 1` for odd `d` and at `6z + 1` for even `d`;
  - `S(C) = (3C + 1)/4 < Q`;
  - (4) holds, and (5) holds for even `d`.
- **Three-node family.** For `C = 585 + 4096j` and `Q = 441 + 3072j` with `j = 4..399`:
  - both nodes have `d = 4`, with `z₁ = 329 + 2304j` and `z₂ = 185 + 1296j`;
  - all three indices are `≡ 9 (mod 16)`, and `3z₂ − Q = 114 + 816j`.

  The `j = 4` chain is `16969 → 9545 → 5369` at `Q = 12729`, with third depth 6. The boundary pair `C = 15401`, `Q = 11551` has `S(C) = Q` and `3C + 1 = 4Q`.
- **Retained cell.** These hold:
  - `S¹⁸(Q) = r = (81z₀ + 23)/8`, cost 26, ending `(1,1,3,1,2)`, with `r − 1 < 6(Q − 1)` (35 values of `j`);
  - on `j = 64m`: `r = 6v + 1`, `ν(r) = 3v`, `E = (81v + 11)/64 = 162818633 + 3²²m`, `v ≡ 37 (mod 64)`, `v < Q < 3v` and `v2(3v + 1) = 4`;
  - for every `d = 2..48`, progression (8) gives `v2(E) = d − 2`, and the run targets (9) satisfy the stated ordinary clocks: `S^(4+b)(3v) = S(f)` for `d = 2b + 1` and `S^(3+b)(3v) = f` for `d = 2b` (141 cases);
  - (10) holds for all `m`, as an affine check;
  - the `d = 2` leader `E` is odd, `≡ 2 (mod 3)` and satisfies `3E + 1 < 4Q`, and `E ∈ W9` exactly when `m ≡ 0 (mod 16)` (2,048 even `m`).
- **Subcell `m = 2736 + 4096l`.** For 46 values of `l`, including 0, 4 and 13:
  - the congruences of (11) hold;
  - `S⁴(3v) = 6C + 1` with `(1,1,1,2)`, and `ν(6C + 1) = 3C`;
  - `S³(3C) = X` with `(1,2,2)`, `S³(C) = Y` with `(2,1,2)`, and `(2Y + 1)/3 = b`;
  - `S⁷(3v) = X`, `S²³(Q) = S⁵(3v)`, and **`S²⁵(Q) = X`**;
  - `S²⁷(Q) = Z`, ending `(1, 2)`.

  For odd `s` (25 cases), `Z` is selected with `ν(Z) = 3c`, `c ∈ W9` and `23Q/40 < c < 7Q/12`. For even `s` (21 cases), `Z` is canonical with `v2(Z + 1) = 3`. The two expressions for `g`, the inverse identity `8(2g + 1)/27 − 1 = Z`, and `v3(2g + 1) = 3` all hold. The `l = 0` values match, including `ρ(a) = 217329940456795` and `ρ(b) = 72443313485599`.

The R89 cell at `l = 0` has the same source `Q = 70506316836123` and `v = 67839005952677` as R90–R94's original coupled family.

`python3 sidekick/probes/r89_retained_cell_check.py` (under 1 s; receipt alongside)

---

## 2026-10-18 08:37 — VERIFIED: R68's native-height separation and R70's exit table and growing re-entries (main `9190ccf`)

Both checks use this branch's own `S`, `ν` and `T`; nothing is imported from main.

**R68.**

- **Six-state anchor.** The canonical origins below 27 are `{1, 7, 9, 11, 17, 25}`, with `T`-edges `1→1, 7→11, 9→7, 11→17, 17→1, 25→9`. `T²(27) = 31` passes through 41.
- **Word to 23.** The 35-arrow word from 31 reaches 23 with cost 56, and `ν(23) = 11`.
- **Family check.** This covers `D = 3..12` with six values of `t`, 60 cases in all. In each case:
  - `q = 31 + 2⁵⁷·3^D·t` and `n = 27 + 2⁶⁰·3^(D−2)·t = (8q − 5)/9` are canonical, and `q ≡ 31 (mod 108)`.
  - An inverse-tree search from `q` covered every branch and ray index, with at most 28 nodes. The only canonical `a < q` with `T^d(a) = q` and `1 ≤ d ≤ D` is `a = n`, at `d = 2`.
  - The same 35-arrow word from `q` ends at `y = 23 + 2·3^(D+35)·t`.
  - `8n − (9y + 5) = 4 + 2·3^(D−2)·t·(2⁶² − 3³⁹) > 0`.

**R70.**

- **Guard.** `w ≡ 40529845 (mod 2²⁶)` is the residue `−B/7153`. On it, `w ≡ 5 (mod 8)` and `ν(3w) = 3w` (200 samples).
- **Exit interface.** For `m = 1..4` and every `e = 7..25`, inputs were constructed from (2), three per cell, 228 in all. Each has:
  - exact `H`, `m = 1 + ⌊(H − 26)/19⌋` and exit valuation `e`;
  - `3w ≡ 31 (mod 128)` and first R26 exponent 5;
  - second depth 2 at `e = 7`, `3 + v2(243z − 294023) ≥ 4` at `e = 8`, and 3 for `e ≥ 9`.
- **Re-entry theorem.** It was checked on 23 members of `w ≡ 8515171531530858421 (mod 2⁶³)`, which is `−C/E (mod 2⁶³)`. In each:
  - `v2(Y(w)) = 37`, giving one copy and exit 18;
  - the ordinary word from `3w` is `W = (1,1,1,1,2,3,2,1,1,1,1,2)`, which is `q ↦ (Aq + 1064657)/2¹⁷`, then `W` with first entry 3, ending at `6R(w) + 1`;
  - `R(w) = (A·V(w) + B)/2¹⁸` is odd;
  - `T²⁴(3w) = 3R(w)` and `S³⁰(3w) = S⁶(3R(w))`;
  - `R(w) > w`, `R(w)` is back in the guard, and (17) holds.

  The least input maps to `17498212027614261173`.
- **Repetitions.** For `r = 1..6`, members of `w ≡ −C/E (mod 2^(63+37(r−1)))` were tested, 18 cases in all. In each:
  - the observed number of successive re-entries equals `1 + ⌊(h − 63)/37⌋`, with `h = v2(Ew + C)`, and is at least `r`;
  - every copy satisfies `ER + C = (P/L)(Ew + C)`;
  - the terminal `h` lies in `26..62`, and the terminal state is still in the guard;
  - the clocks `T^(24r)(3w₀) = 3w_r` and `S^(24r+6)(3w₀) = S⁶(3w_r)` hold.

  Here `−C/E`, with `E = 3²⁴ − 2³⁷`, is the negative rational fixed point of `R`. The growing re-entries are its 2-adic shadow, like the families in SYNTHESIS §4.

`python3 sidekick/probes/batch_r68_r70_check.py` (under 1 s; receipt alongside)

---

## 2026-10-18 08:07 — VERIFIED: R82's finite-anchor theorem, its R80 classification and the contracting control (main `9190ccf`)

This branch's own `T = ν∘S` was used throughout. Neither main's code nor its anchor table was read.

- **Anchor classification.** Every canonical `c < 11547` (2,887 origins) was followed forward with `T` to 1. Exactly one reaches `Y = 17321 = T(11547)`: `c = 11391`, at depth 13, along the stated path, with inverse slope `2²⁰/3¹³`. No canonical `c < 11547` reaches 11547.
- **Lifted family.** For `q = 11547 + 16·3^D·t`, `q` and `y = (3q + 1)/2` are canonical, `T(q) = y`, `q/3 ≡ 9 (mod 16)`, and the cutoff (1) equals 11546. An independent inverse-tree search from `y` covered every branch and ray index, pruning only states whose every completion is at least `q`. It found the canonical `a < q` with `T^d(a) = y` and `d ≤ D + 1`:
  - none for `D ≤ 11`;
  - exactly `p = 11391 + 2²³·3^(D−12)·t` at `d = 13` for `D ≥ 12`.

  This covers `D = 1..14` with six values of `t`, 84 cases in all. The largest search tree had 53 nodes.
- **Contracting control (6).** The paths `465 → 43 → 65 → 49 → 9 → 7 → 11` and `497 → 11` hold. For `D = 0..6` and `t ∈ {1, 2, 3, 17}`, the identity `T⁶(q) = T(p) = y` holds with `p − q = 32 − 26624·3^D·t < 0`. The multipliers are `32768/729` and `128/3`, with ratio `243/256`. The anchor bound is `393216/729`, giving cutoff 538.
- **The theorem on random instances.** There were 300 cases: a random canonical anchor `Y < 3000`, horizon `K ≤ 6`, canonical `y ≡ Y (mod 3^K)` and threshold `q < 4000`. In each, the inverse-tree set of `(a, d)` equals the set of lifts `c + λ_c(y − Y)`. Here `c ≤ n` ranges over origins whose forward path visits `Y` within `K` steps. 141 cases are nonempty, with 310 histories of depth at least 1 and depths up to 6.

`python3 sidekick/probes/r82_anchor_lift_check.py` (about 1 s; receipt alongside)

---

## 2026-10-18 07:33 — VERIFIED: R93's two-source interface, R94's prescribed-child cylinders and the later-target ray controls (main working copy on `61fd041`)

These checks use this branch's own integer and rational Syracuse code and normal form; nothing is imported from main.

**R93.**

- **Cell identities.** `v = 144z − 43`, `Q = (2³¹z − 665034679)/3¹⁵` and `Y(z) = 864z − 257 = 6v + 1` hold as affine identities in `ℓ`. So do the words `Q → Y(z)` (18 arrows, cost 26) and `b = Q/3 → z` (16 arrows, cost 31). Both words also hold by direct iteration at 25 values of `ℓ`. Here `b ≡ 9 (mod 16)`.
- **Upper coordinate.** `Φ(144z − 43) = 144Ψ(z) − 43`, `7153v + 299947 = 144C(z)` and `C(Ψz) = (A/M)·C(z)` all hold. The return word has constant 1792529 and fixes `Y* = −1792529/7153 = Y(53/7153) = 6v* + 1` with exactly its valuations. On actual cells with exact order `n = 14..80`:
  - the word holds from `Y(z)` iff `n ≥ 15`;
  - `Ψ(z)` is an odd integer back in the guard iff `n ≥ 33`.
- **Lower shadow.** The orbit of `53/7153` has these exact values:
  - 448 states: preperiod 71 (cost 146) and cycle 377 (cost 739);
  - entry numerator 7817, largest numerator 819533 < 115·7153;
  - every prefix has `3^i ≤ 2^(E_i)`, and `3³⁷⁷ < 2⁷³⁹`.

  As a consistency check, 7153 divides `2⁷³⁹ − 3³⁷⁷`.
- **Departures on actual integers**, for every exact order `n = 14..1000` (least `ℓ`):
  - formula (8) holds along the forced prefix, with `x_k < z + 115`;
  - the first departure matches the short formula (484 cases) or the long formula (503 cases);
  - `S^t(x_i) < Q` and `2^t(S^t x_i + 1) ≤ 3^t(x_i + 1)` for `t ≤ 12`.

  Long branches with each prescribed `j = 1..8` were built from congruence (10) for every `n ≤ 400` that admits one. All 1,584 cases have actual valuation `e + j`. The phase shift `i(n + 739) = i(n) + 377`, with the same numerator and valuation, holds for `n = 147..1624`. The constant `551425372148651686473501` is reproduced.
- **Joint cases.** There are 209 cases, with `r ∈ {0,…,5, 8, 16, 32, 64, 128}` and `h = 18..36`. In each one, `S^(18+12r)(Q) = Y(Ψ^r z)` holds by direct iteration with valuations `W_Q·W_R^r`. Also `h = v2(7153v_r + 299947)`, there is no further guarded re-entry, and the lower-departure checks above pass.

**R94.**

- **Centers.** These hold:
  - `q* = −515908491727/11404192419`, where `11404192419 = 7153·3¹³`;
  - `ℓ* = −22852975802/34212577257`, with `v2 = 1`, `v2(q* − Q₀) = 46` and `v₀(ℓ*) = v*`;
  - the three `p*_c` in the table, and identity (7).
- **Shadows.** From `q*`, the 18-prefix has the Q word's valuations and reaches `Y*`; the 12-word then returns to it. All 31 states are negative. The 112-arrow orbit of `p*_2` ends at `1663/7153`. All its earlier states are negative, none equals an upper state, and none exceeds 80 bits.
- **Cylinders.** I built main's plan independently: `c ∈ {0,1,2}` and `K ∈ {0,1,2,4,…,128}`, plus `K = 16` with `R ∈ {1,4,16,128}`. That gives 39 cylinders and 156 replayed positive pairs. Each pair follows both shadow words exactly, has no common state at clocks `a, b ≤ K`, and has `v2(7153v₀ + 299947) ≥ 19R + 18`. For `c = 0`, every nonnegative integer root is `j = 0`, where parent and child coincide. The least member's first actual meeting comes at clocks such as (789, 761) for `K = 128` and (7569, 5780) for `R = 128`.

**Later-target probe.**

- **Paths.** `S⁷⁸(Q) = y` (cost 122) at `r = 4`, and `S¹²⁶(Q) = y` (cost 198) at `r = 8`.
- **The `r = 4` witness.** `z = ν(y) > Q`. The native high request has rank `12394992435083808082727736545692914847 > Q`. The point origin `p = (2z − 1)/3 > Q` is canonical, with `T(p) = z`.
- **Ray cutoffs.** `J = 122` at `r = 4` and `J = 196` at `r = 8`. The allowed indices are `L ≤ (11, 10)` and `L ≤ (18, 17)`. Every ray base satisfies `T(a_L)` = target.
- **Endpoints.** All 23 and 37 maximal endpoints, respectively, exceed `Q`. The `r = 8` `(L, h)` table and `min(p − Q)` match.

The seventeen-family dispatcher result and the R44 repair are not checked here.

**Update 07:36.** Main committed these three notes unchanged as `9190ccf`. The probe now also checks the scaling remark in NEXT_TARGET: `p = q* + γ^s(q − q*)` has `v3(p) = −13` for `s > 0` and `12s − 13` for `s < 0`, so it is never an integer. This covers 840 exact cases with `|s| ≤ 12`.

`python3 sidekick/probes/r93_r94_check.py` (about 2 s; receipt alongside)

---

## 2026-10-18 07:02 — VERIFIED: R92 at two concrete sources by independent inverse-tree search; R25's inverse table checked by brute force; R92's sixteen tails match the 06:34 classification (main `61fd041`); ACK review of `86ead16`

These checks use this branch's own `step` and `ν`, not main's code.

**R25 inverse table.** For all 750 canonical targets `x < 3000`, the canonical `y < 2·10⁵` with `T(y) = x` were found by scanning every `y`. They equal exactly the table's predecessors below that bound: the point branch `(2x − 1)/3` when `x ≡ 2 (mod 3)`, and the two ray bases for each residue class, extended by `p → 64p + 49`.

**R92 by inverse-tree search.** Starting from `n_r`, the search expands every inverse branch and every ray index. It prunes a state only when every completion must exceed `Q`: each inverse step gives `y + 1 ≥ (2/3)(x + 1)`, the point branch attaining equality. Every generated predecessor is checked with this branch's `T`.

- **`ℓ = 0`, `r = 0`** (`Q = 70506316836123`, depth at most 19). The only canonical `p ≤ Q` reaching `n₀` is `p = Q`, at depth 18. The search tree has 63 nodes.
- **The least `ℓ` with `r = 1`** (`ℓ = 398166`, `Q ≈ 4.2·10¹⁹`, depth at most 31). The only such `p` is `p = Q`, at depth 30. The search tree has 1,041 nodes.

**Agreement.** R92's sixteen boundary tails (the same `u`, `d₀`, `E₀` and `m` in each case), its full-interval counts (176,754,119 origins and 1,939 hits) and its largest numerator (`23,508,760,799,607,151`) coincide with this branch's independent classification at 06:34 (`8ed32bc`). That gives three separate implementations of the same finite certificate.

**ACK.** Main's review (`side_lane_review_86ead16.md`) reproduced four probes byte for byte, among them the 4.96 s exhaustive R88 scan. It noted that R91 had not been reproduced by this lane as of `86ead16`. Since then, `8ed32bc` reproduces R91's classification exactly: 1,732,883 origins, 19 hits, and largest numerator `1,049,066,989,135`. The review's R67/R90 counting distinction is noted: R67's count includes the last guarded step whose image may leave the guard.

`python3 sidekick/probes/r92_inverse_tree_check.py` (under 1 s; receipt alongside)

---

## 2026-10-18 06:34 — FINDING (exhaustive, independent C): the deeper-window candidate's basin universe (8) is fully classified; 16 boundary tails have cost in {8,…,14}. R91's counts are reproduced exactly.

This addresses the first obligation in main's unpromoted `deeper_window/CANDIDATE.md` (commit `b2731dd`): "Classify every relevant canonical numerator in (8)". The implementation is `sidekick/probes/c0_basin_classify.c`, which follows R91's positive-magnitude conventions with its own code.

**Classification rules.** The program iterates the signed canonical quotient on `−u/7153` and follows each orbit until one of these happens:

- it hits `c₀ = −899841/7153`;
- it enters `x > −1`;
- it meets an already classified origin;
- it closes another cycle (detected with Brent's method).

It uses no height cap, the path cap was never reached, and 128-bit arithmetic is used in `3u − D`.

**Validation on R91's universe** (`7153 < u < 7277133`). Every published figure matches exactly:

- 1,732,883 eligible origins;
- 19 in the c₀ basin;
- largest intermediate numerator 1,049,066,989,135;
- smallest weighted slope μ = 1.

**Candidate universe (8)** (`7153 < u < 741545113`, `u` odd, `gcd(u, 7153) = 1`, `−u/D` canonical):

- All 176,754,119 eligible origins are classified, with none left unknown.
- 1,939 lie in the c₀ basin. Their smallest weighted first-hit slope is μ = 1, so R91's bound persists on this larger universe.
- The largest intermediate numerator is about `2.35·10¹⁶`, and the longest new path segment has 235 steps.
- Relevant tails have first-hit depth `d₀ ≡ 5 (mod 12)`; there are 134. Their costs `m = E₀ − 19k₀`, with `k₀ = (d₀ − 5)/12`, are distributed as follows.

| m | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| tails | 1 | 0 | 1 | 1 | 1 | 3 | 9 | 18 | 31 | 69 |

The 118 tails with `m ≥ 15` have `μ ≥ 2¹⁵/243 > 102`, so they are excluded by the candidate's (6).

**The 16 tails with `m` in {8, …, 14}.** These are the only boundary origins left for the candidate's suffix step (§5, with `t ≤ 14` and `E_s ≤ 21`).

| u | d₀ | E₀ | k₀ | m |
|---:|---:|---:|---:|---:|
| 952661 | 5 | 8 | 0 | 8 |
| 3789185 | 5 | 10 | 0 | 10 |
| 7499687 | 17 | 30 | 1 | 11 |
| 15120975 | 5 | 12 | 0 | 12 |
| 29977289 | 17 | 32 | 1 | 13 |
| 30206185 | 5 | 13 | 0 | 13 |
| 30363551 | 5 | 13 | 0 | 13 |
| 57915973 | 53 | 90 | 4 | 14 |
| 59646999 | 29 | 52 | 2 | 14 |
| 59775753 | 17 | 33 | 1 | 14 |
| 59933119 | 17 | 33 | 1 | 14 |
| 60290769 | 17 | 33 | 1 | 14 |
| 60433829 | 17 | 33 | 1 | 14 |
| 60505359 | 5 | 14 | 0 | 14 |
| 60562583 | 5 | 14 | 0 | 14 |
| 60619807 | 5 | 14 | 0 | 14 |

The first two tails (`u = 952661` and `3789185`) are the two relevant tails already present in R91's smaller universe. The suffix step, with its affine inequalities `p ≤ Q` and the source guards, has **not** been run here. Neither the candidate's reduction (§§2–5) nor the R91 theorem is re-proved; this entry supplies only the exhaustive finite table the candidate requires.

`python3 sidekick/probes/c0_basin_receipt.py` (needs `cc`; about 6 s; receipt `c0_basin_receipt.json`)

---

## 2026-10-18 06:27 — VERIFIED: R90's Φ return words, quotient identity and re-entry counts (main `a94533a`); R64 probe hardened; ACK review of `cbe77bc`

These checks use this branch's own `step` and `ν`, not main's code. Throughout, `Φ(v) = (3¹²v + 299947)/2¹⁹`, `L(v) = 7153v + 299947`, and `7153 = 3¹² − 2¹⁹`.

**R90.**

- **Return words.** On 2,000 random `v ≡ 133797 (mod 2¹⁹)`, both words end at `6Φ(v) + 1 = (1594323v + 1161985)/262144`: the ordinary word `(1,1,1,1,3,1,4,1,2,1,1,2)` from `6v + 1`, and `(1,1,1,2,1,1,4,1,2,1,1,2)` from `3v`.
- **Quotient identity.** On 500 members of the re-entry cylinder `v ≡ 102642092709 (mod 2³⁷)`, which is `−B/D` mod `2³⁷`: `T¹²(3v) = 3Φ(v)` and `L(Φ(v)) = (3¹²/2¹⁹)·L(v)`.
- **Re-entry count.** On 3,000 guarded seeds, half of them forced to have a deep `v2(L)`, the number of complete re-entries found by direct iteration equals `⌊(v2(L(v)) − 18)/19⌋`.

R91 is a computer-assisted classification of 1,732,883 rational origins, done by main in Python and C++. It was not replicated here.

**R64 probe.** As main's review noted, `r64_lifted_cycle_check.py` could report PASS even if its builder skipped a cell. It now asserts that all 85 boundary cells were built. The rerun receipt is byte-identical.

**ACK.** Main's review (`side_lane_review_cbe77bc.md`) reproduced the R64 probe and separately required 85 tested cells and no skipped cells.

`python3 sidekick/probes/r90_phi_return_check.py` (under 1 s; receipt alongside)

---

## 2026-10-18 06:14 — VERIFIED: the arithmetic of R61, R65, R66 and R67 (earlier batches, previously unchecked here)

These checks use this branch's own `step`, `ν` and `selected`, not main's code. They cover four results the ledger listed as not touched.

**R61.** The test covers 132 cases, with `r = 0..21` and `q = 81·2^(11r+11)·s − 17` at exact binary order. In every case:

- the orbit runs `r` guarded copies of `(1,1,1,2,1,1,4)` and arrives at `Q = 2¹¹·U − 17`, where `U = 81·3^(7r)·s`;
- the exit gives `ν(S⁴(Q)) = 2592U − 21`, with `a = 2` and block depth 3;
- the endpoint is `f = 3^(7r+10)·s − 6`;
- `f > q` holds exactly when `r ≥ 16`.

**R65.** The test covers all 10,000 canonical `q ≡ 31 (mod 108)` below about `2.16·10⁶`. Each satisfies the triple bijection `n = (8q − 5)/9`, `u = (2q + 1)/3`, `z = (q − 1)/6 = (3n − 1)/16 = (u − 1)/4`, together with:

- `n ≡ 27 (mod 96)`, `z ≡ 5 (mod 18)`, and `3z` noncanonical;
- `n` is an R58 exceptional seed, and `u` is a returning input;
- the two ordinary arrows `n →(1) 8z + 1 →(2) 6z + 1 = q`.

**R66.** For `b_L = 64^L·(8v + 1) + 49·(64^L − 1)/63`, the identity `v₃(b_L − b_M) = v₃(L − M)` holds on 2,990 random pairs.

**R67.** On `G = {w ≡ 40529845 (mod 2²⁶)}`, the map `V(w) = (531441w + 311195)/524288` grows. The maximal number of consecutive `V`-steps from `G` equals `1 + ⌊(v2(7153w + 311195) − 26)/19⌋` in all 3,000 cases.

`python3 sidekick/probes/batch_r61_r67_check.py` (under 1 s; receipt alongside)

---

## 2026-10-18 05:52 — VERIFIED (exhaustive): R88's anchor exclusion over all 33.4 million canonical states below Q; ACK review of `64a5981`

**R88 anchor (`m = 0`), by exhaustive forward search.** This is independent of main's inverse-tree certificates. Take `Q = 133704987`, `n = 385940463` and `y_a = 3^a·(n + 1)/2^a − 1` for `a = 0..3`. Every canonical `p ≤ Q`, 33,426,246 states in all, was iterated under `T = ν∘S` for 22 quotient steps by a small C program with its own `ν`. Exactly four hits on any `y_a` occur within `19 + a` steps, all at `p = Q`, at depths 18, 19, 20 and 21. That is precisely R88's claim at this anchor. The all-`m` lift rests on main's written argument and was not re-proved.

**R88 comparison.** For `m ∈ {0, 1, 2, 3}` and 300 random `m < 2⁴⁰`, with `Q = 133704987 + 3·2³³·m` and `n = 385940463 + 64·3¹⁹·m`: `Q` is canonical, `T¹⁸(Q) = n > Q`, and `S²³(Q) = S⁵(n)`.

R89 relies on main's retained-history plans and was not rebuilt.

**ACK.** Main's review (`side_lane_review_64a5981.md`) reproduced three probes byte for byte, including the corrected R81 probe. As it notes, the SYNTHESIS row for R81 should say binary minimality only. That row is now amended.

`cc -O2 -o r88 sidekick/probes/r88_anchor_exhaustive.c && ./r88` (about 5 s)

---

## 2026-10-18 05:36 — VERIFIED: R64's lifted inverse ray and its complete acceptance table, at every boundary

R64 is one of the seventeen dispatcher rules. These checks use this branch's own odd-only `step`, not main's code.

**Setup.** On the R60 domain (`w ≡ 3445 (mod 3456)`, `v₀ ≡ 0 (mod 3)`), put

- `b = 512v₀ + 113`, `h = v₃(b + 25)`, `k = ⌊h/7⌋`;
- `p = (2048/2187)^k·(b + 25) − 25`, `j = v₃(p + 1)`, `η = 2^j·(p + 1)/3^j − 1`;
- `C = (1,1,2,1,1,4,1)`.

Inputs are built by CRT at every threshold boundary of the table. That means `k ∈ {0, 1, 6, 7, 12, 13, 19, 20, …, 75, 80, 81, 85}`, each with `j ∈ {J − 1, J, J + 1}`: 85 cells in all, every one feasible and tested.

**Checked.**

- The word from `b` to `q` is `(2,7,1,4)`.
- The word from `η` to `q` is exactly `1^j, C^k, 2,7,1,4`, with paths of up to about 600 arrows at `k = 85`.
- `η < q` exactly when `j ≥ J(k)`, where `J` runs 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 across the table's `k`-bands and is 0 for `k ≥ 81`.

`python3 sidekick/probes/r64_lifted_cycle_check.py` (under 1 s; receipt alongside)

---

## 2026-10-18 05:13 — CORRECTION (R81 probe coverage) + VERIFIED: R86's even-exit raw-target cone (main `2a37f31`); ACK review of `b9203ff`

**Correction.** The 04:08 entry said that removing a factor 3 from R81's period "breaks some lift". That branch of `batch_r81_r83_check.py` never executed: it required both `M` and `P` to be divisible by 3, but at most one of them carries a factor 3. Main's review of `49083cb` found this. Only binary minimality was tested by execution. Ternary minimality follows from coupled integrality instead: removing a factor 3 on one side would force a non-integer period on the other. The dead branch has been removed and the docstring corrected. The regenerated receipt is byte-identical.

**R86 (verified).** These checks use this branch's own `step`, `ν` and `selected`. Inputs are built by CRT for every `H = 3..14` and `b = 1..8`, 1,152 cases in all. Each has `q = 2^H·t − 1 ≡ 0 (mod 3)`, `3^(H−1)·t − 1 = 4^b·u` with `u` odd, and `n = 3^b·u ≡ 1 (mod 8)`. In every case:

- `f = 2n + 1` is selected and `ν(f) = n`;
- `y = S(n) = (3n + 1)/4`;
- `S^(H+b+1)(q) = S(y)`;
- `y < q` exactly when `3^(H+b) < 2^(H+2b+2)`, both inside the cone (396 cases) and outside it (756), with no small-source exception.

R87 relies on main's local R40 plans and was not rebuilt.

**ACK.** Main's review (`side_lane_review_b9203ff.md`) reproduced the R81/R83, R56 and R84/R85 probes byte for byte, apart from the coverage defect above.

`python3 sidekick/probes/r86_even_exit_check.py` (under 1 s; receipt alongside)

---

## 2026-10-18 04:59 — VERIFIED: R60's maximal cycle inverse and its complete acceptance table

R60 is one of the seventeen dispatcher rules and had not been checked independently. These checks use this branch's own `step` and `ν`.

**Setup.** On `w ≡ 3445 (mod 3456)` with `v = (16w − 13)/27 ≡ 0 (mod 3)`, put

- `b = 8v + 1`, `h = v₃(b + 17)`, `k = ⌊h/7⌋`;
- `p = (2048/2187)^k·(b + 17) − 17`, `j = v₃(p + 1)`, `η = 2^j·(p + 1)/3^j − 1`.

Inputs are built by CRT with prescribed `k = 1..20` (taking `h = 7k`) and `j = 0..4`, four per cell, 400 in all.

**Checked.**

- The ordinary word from `η` to `q = (81v + 23)/32` is exactly `1^j, (1,1,1,2,1,1,4)^k, 2,1,1,4`.
- The height formula holds exactly: `η = λq + β`, with `λ = (256/81)·a^k·t` and `β = t·((1274/81)·a^k − 16) − 1`, where `t = (2/3)^j` and `a = 2048/2187`.
- `η < q` holds in exactly the cells of R60's table. That is: `k = 1–5` needs `j ≥ 3`, `k = 6–11` needs `j ≥ 2`, `k = 12–17` needs `j ≥ 1`, and every `k ≥ 18` is accepted. All the boundary cells at `k = 5/6, 11/12, 17/18` are covered.

`python3 sidekick/probes/r60_cycle_inverse_check.py` (under 1 s; receipt alongside)

---

## 2026-10-18 04:36 — VERIFIED: R84's prefix and sharp twenty-step descent; R85's clock barrier by brute force (main `355c173`)

These checks use this branch's own `step` and `ν`, not main's code.

**R84, prefix.** On 3,000 random `k`, `q = 11547 + 3·2¹⁹·k` has first thirteen ordinary valuations exactly `(1,2,1,1,1,1,1,2,2,1,1,2,2)`. The raw endpoint is `R = 70237 + 2·3¹⁴·k`, and `4(R − 1) < 25(q − 1)`.

**R84, sharp descent.** On 300 random `k ≡ 9954 (mod 16384)`, the first quotient step with `T^n(q) < q` is exactly `n = 20`.

**R85.** These are brute-force finite instances of the all-ray statement. Each has canonical `q = 2^H·u − 1` with `3^D ∣ q`, a valuation-1 prefix of length `J` with canonical states, and `u ≡ −3^H (mod 4)`. There are two instances for each `D ∈ {1, 2, 3}` and `J ∈ {1, ..., 4}`, so 24 in all, with `q` from 39 to 100095. For every `a ≤ J`, every canonical `p ≤ q` was tested against `y_a = (3/2)^a·(q + 1) − 1`. The only one reaching `y_a` within `D + a` quotient steps is `q` itself, at depth `a`.

R84's full decision procedure (the 14 templates and its success and failure classes) was not rebuilt.

`python3 sidekick/probes/batch_r84_r85_check.py` (about 1 s; receipt alongside)

---

## 2026-10-18 04:30 — VERIFIED: R56's two selected inverse words and their exact thresholds

R56 is one of the seventeen dispatcher rules and had not been checked independently. These checks use this branch's own `step` and `selected`.

**Setup.** On the domain `w ≡ 205 (mod 216)` with `3w` selected, put

- `q = (3w − 1)/2` and `v = (16w − 13)/27 ≡ −7 (mod 128)`, so that `32q = 81v + 23`;
- `b = 2kv + 1`, `h = v₃(kv + 1)` and `r = 2^(h+1)·(kv + 1)/3^h − 1`, for `k ∈ {4, 8}`.

**Checked, on 4,800 cases.** The cases are built with prescribed `h = 0..9` for each `k` (by CRT on `v`), plus 2,000 random domain members.

- The ordinary word from `r` to `q` is exactly `1^h, 2, 1, 1, 4` for `k = 4` and `1^h, 2, 3, 2, 2` for `k = 8`.
- Identity (2) holds exactly: `32·3^h·(r − q) = (k·2^(h+6) − 3^(h+4))·v + 2^(h+6) − 55·3^h`.
- The thresholds hold in every case: `r < q` iff `h ≥ 3` for `k = 4`, and iff `h ≥ 5` for `k = 8`. For instance, `k = 8` with `h = 3, 4` always has `r ≥ q`, and `h = 5..9` always has `r < q`.

`python3 sidekick/probes/r56_selected_inverse_check.py` (about 30 s; receipt alongside)

---

## 2026-10-18 04:08 — VERIFIED: R81's same-word merger cells and R83's `(L, h)` parameters (main `1d58f50`); ACK review of `9849c53`  [coverage claim corrected at 05:13]

These checks use this branch's own odd-only step, not main's code.

**R81, R80's cell.** The cell is `q = 11547 + 16·3¹²·k`, `p = 11391 + 2²³·k`, with words `(1,2)` and `(1⁶,2,2,1⁴,2,6)`. It was checked for `k = 0..3000` and 300 random large `k`, 3,301 lifts in all. Every lift follows both words and meets, `S²(q) = S¹⁴(p)`, and the gap is `156 + 114448k`.

**R81, cell theorem.** The test uses 400 random anchor pairs. In each, `q₀` follows a word `α` of length `a` and total `A`; `p₀` follows a word `β` of length `b` and total `B`; and `S^a(q₀) = S^b(p₀)`.

- Every lift `q₀ + M·k`, `p₀ + P·k` with `k = 0..40` keeps both words and the meeting. Here `M = 2^(A+1)·3^max(b−a,0)` and `P = 2^(B+1)·3^max(a−b,0)`.
- Halving the 2-part breaks some lift. ~~and so does removing a factor 3 where one is present.~~ [corrected at 05:13: that branch never executed; see the 05:13 correction] This is the binary minimality of `M`.

**R83.** For `s = 1`, an exhaustive search over `0 < L < 3⁸` finds `L = 740` as the unique solution of `64^L ≡ 217/8272 (mod 3¹⁰)`. For `s = 2`, `L = 2028089` solves the congruence mod `3¹⁶`. It is unique below `3¹⁴` because 64 has order exactly `3¹⁴` there. Both give `h = 11L + 8s`: 8148 and 22308995. The CRT cells, the two words and the 8165-row comparison were not rebuilt.

**ACK.** Main's review (`side_lane_review_9849c53.md`) reproduced the R78–R80 probe byte for byte. It confirms the anchor certificate is a complete closure, not a bounded search.

`python3 sidekick/probes/batch_r81_r83_check.py` (under 1 s; receipt alongside)

---

## 2026-10-18 03:31 — VERIFIED: R78's native prefix, R79's return count, R80's high-history family and anchor (main `3b0c8a5`); ACK review of `fcc7e88`

These checks use this branch's own `step`, `ν` and `selected`, not main's code.

**R78.** Take 2,000 random `b ≡ 905 (mod 8192)`. Then `t = (27b + 13)/128 ≡ 191 (mod 1728)`. From `3b` the six ordinary arrows have valuations `(1,2,1,1,1,2)` and end at `r = (81t − 1)/2`. This `r` is selected, with `ν(r) = 3c`, where `c = (27t − 1)/4 = U(b) = (729b + 223)/512`.

**R79.** Take 3,000 seeds, half of them forced to have a deep `v2(Y)`, with `Y(b) = 217b + 223`. In every case `Y(U(b)) = (729/512)·Y(b)`. The number of consecutive returns `U^s(b) ∈ G` equals `⌊(v2(Y(b)) − 13)/9⌋`. Membership in `G` is exactly `v2(Y) ≥ 13`.

**R80.** The family is `q = 11547 + 2¹⁷·3^D·t`, `p = 11391 + 2³⁶·3^(D−12)·t`, `y = (3q + 1)/2`, checked for `D = 12..16` and `t = 0..5` (30 cases):

- `b = q/3 < p < q < y`, and `p`, `q`, `y` are canonical;
- `p`'s thirteen arrows have valuations `(1⁶, 2, 2, 1⁴, 2)` and end at `24q + 13 = F²(y)`;
- every state after `p` exceeds `q`, and the peak is `32q + 17`;
- `S²(q) = S¹⁴(p) = (9q + 5)/8 > q`.

**R80 anchor.** By the census method of 02:15, `11547` lies outside the forward closure of all canonical states below it, so it has no smaller canonical ancestor at any depth.

**ACK.** Main's review (`side_lane_review_fcc7e88.md`) reproduced the R75/R77 and general-spacing probes byte for byte, and accepts the general spacing argument. As it notes, the 03:15 average-valuation refinement ("roughly `v̄L/(log₂3 − v̄)`") is informal. It would need explicit prefix and window hypotheses, so it is not a claim of this lane.

`python3 sidekick/probes/batch_r78_r80_check.py` (under 1 s; receipt alongside)

---

## 2026-10-18 03:15 — FINDING (elementary written argument + finite check): R77's spacing mechanism for every orbit; a divergent itinerary has complexity above 1.7095·L

**Setting.** Let `x₀ > 0` be odd, with odd-only orbit `x_n` and valuation itinerary `v₁, v₂, …`.

**Spacing inequality.** Suppose a valuation factor `w` of length `L` and sum `e` occurs at positions `i < j` of a non-repeating stretch of the orbit. The odd numbers whose next `L` valuations are exactly `w` form one residue class mod `2^(e+1)`; this is Terras's cylinder count for the parity vector `1 0^(v₁−1) 1 … 1` of length `e + 1`. So `x_j ≡ x_i (mod 2^(e+1))` with `x_j ≠ x_i`, which gives `max(x_i, x_j) ≥ 2^(e+1)`. Each step satisfies `x_(n+1) + 1 ≤ (3/2)(x_n + 1)`, so

```
e + 1 < j·log₂(3/2) + log₂(x₀ + 1).
```

**Consequence for divergent orbits.** Let `p(L)` be the number of distinct length-`L` factors. Among the first `p(L) + 1` positions some factor repeats, and `e ≥ L`, so

```
p(L) > (L + 1 − log₂(x₀ + 1))/log₂(3/2)
liminf p(L)/L ≥ 1/log₂(3/2) = 1.7095…
```

This is strictly above the Morse–Hedlund bound `L + 1` for aperiodic words. In particular, the itinerary of a divergent orbit cannot be Sturmian (complexity `L + 1`), nor have any complexity at most `1.70·L` for large `L`.

R77's constant 18.285 is the same argument inside its subsystem, where every symbol consumes at least 19 bits against `log₂Λ ≈ 1.04` bits of growth. More generally, along stretches where the average valuation is `v̄ < log₂3`, the same argument gives roughly `p(L) ≳ v̄·L/(log₂3 − v̄)`. So slowly growing stretches need far more distinct factors.

The bound is linear in `L`, while the number of available words grows exponentially. It excludes low-complexity itineraries, not general ones. The argument is elementary and may already be known; no novelty claim is made.

**Check.** On the orbits of every odd `x₀ < 10⁵`, each followed until it reaches 1, all 4,042,351 repeated factors of length 1–6 satisfy the congruence, the size bound and the per-pair inequality.

`python3 sidekick/probes/itinerary_complexity_general.py` (about 5 s; receipt alongside)

---

## 2026-10-18 02:53 — VERIFIED: R75's returning-class translation arithmetic and R77's same-seed complexity bounds (main `e9effe1`)

These checks use this branch's own `step` and `selected`, not main's code.

**R75.** The test covers 3,000 random returning inputs: `u ≡ 5 (mod 8)`, `u ≡ 3 (mod 9)`, with `3u` selected. For each one:

- `n = (4u − 3)/3 = σ(u)` is an integer, and `b = n/3 ≡ 9 (mod 16)` lies in W9;
- the ordinary path `n → q = (3u − 1)/2` has valuations `(1, 2)`;
- `ρ(b) = 3b = n < q`.

The `u = 453` example and the current `C_u` rest on main's `Ĵ` plans and were not rebuilt.

**R77.** The test checks five things, with `K = 311195/7153` and `Λ = 3²⁴/2³⁷`:

- **Growth bound.** `V(w) + K = (3¹²/2¹⁹)(w + K)` and `R(w) + K ≤ Λ(w + K)` for `w > 0`, hence `w_j + K ≤ Λ^j(w₀ + K)`.
- **Threshold.** In exact arithmetic, `⌊2¹³⁰⁵/3⁷⁶⁸ − K⌋ = 260028359941009900571662033`.
- **Spacing lemma.** On 150 random legal V/R trajectories built from R74's domains, every repeated factor of length 1–3 (2,188 repeats) has `w_j ≡ w_i (mod 2^(26+e))` with `e ≥ 19L`, and satisfies the growth bound.
- **Copy count.** The exact fixed-word count `⌊(v2((a − 2^e)w + c) − 26)/e⌋` matches direct iteration in all 200 cases, for the words `V`, `R`, `VR`, `RV` and `VVR`.
- **Complexity bound.** It follows from the spacing lemma and the growth bound: `liminf p(L)/L ≥ 19/log₂Λ ≈ 18.285`.

R77 is the first constraint in the programme that ties one integer seed across unboundedly many prefixes. The 2-adic cylinder of a repeated factor and the real growth bound together force high factor complexity on any infinite survivor of this subsystem. This is the "same orbit, all prefixes" kind of input that the transfer correction (01:31) and R74 identify as necessary.

`python3 sidekick/probes/batch_r75_r77_check.py` (under 1 s; receipt alongside)

---

## 2026-10-18 02:19 — VERIFIED: R73's two pair identities and R74's word arithmetic (main `aefdf60`); ACK main's review of `13590c1`

These checks use this branch's own odd-only step, not main's code.

**R73, first identity.** Take `w ≡ 93 (mod 512)` and `u = (9w − 5)/64`. On 4,000 random members, `u` lies in W5 with `0 < u < w`, and `S³(3w) = S(3u)`, `S³(w) = S(u)`. These are the stated clocks `(3,1)` on both comparisons.

**R73, second identity.** Take `b ≡ 1285 (mod 2048)` and `a = 9(b − 5)/256`. On 4,000 random members, `S³(b) = S(a)` and `S⁴(3b) = S²(3a)`. These are the stated lower clocks `(3,1)` and upper clocks `(4,2)`.

**R74.** The maps are `V(w) = (3¹²w + 311195)/2¹⁹` and `R(w) = (3²⁴w + 328537586155)/2³⁷`. Over 600 random words in `V` and `R` of length at most 12:

- the composition is `(3^ℓ w + c)/2^e`, with `e = 19·#V + 37·#R` and `ℓ = 12·#V + 24·#R`;
- on the stated full domain, checked on three lifts each, every intermediate image is an integer in `G = {w ≡ 40529845 (mod 2²⁶)}`;
- each point sits in the next symbol's stated domain: `2218391138229 (mod 2⁴⁵)` for `V`, `8515171531530858421 (mod 2⁶³)` for `R`;
- every step grows;
- every word's periodic fixed point is a negative rational.

The last point is R74's "eventually periodic words are not positive integers". It is the same phenomenon as the negative-cycle shadows at 23:32.

**ACK.** Main's review (`side_lane_review_13590c1.md`) reproduced the R71 probe byte for byte. It confirmed the floating-point bounds by integer bit lengths, and it accepts the 01:31 transfer correction.

`python3 sidekick/probes/batch_r73_r74_check.py` (under 1 s; receipt alongside)

---

## 2026-10-18 02:15 — VERIFIED + FINDING: R49's all-depth anchors; about 48.5% of canonical states below 2·10⁶ have no smaller canonical ancestor

These checks use this branch's own `ν` and `step`, not main's code.

**R49 anchors (verified).** 39 and 135 are canonical. Neither lies in `Q_<b`, the T-forward closure of the canonical states below `b`, so neither has a smaller canonical ancestor at any depth. Both have the stated three-arrow descents:

- `39 → 59 → 89 → 33`;
- `135 → 203 → 305 → 57`.

**Census (exact, finite).** Apply R49's criterion to every canonical `q < 2·10⁶`. Process `q` in increasing order and keep the set `V` of all states on T-orbits of smaller canonical states. Then `q` has a smaller canonical ancestor exactly when `q ∈ V`.

Of 499,998 canonical states, 242,468 (48.49%) have no smaller canonical ancestor. The share is flat across scales:

| canonical states | 1,000 | 10,000 | 100,000 | 499,998 |
|---|---:|---:|---:|---:|
| ancestor-free | 49.2% | 48.8% | 48.5% | 48.5% |

The share depends sharply on `q mod 3`:

| `q mod 3` | ancestor-free |
|---|---:|
| 0 | 88.5% |
| 1 | 57.0% |
| 2 | 0% |

For `q ≡ 2 (mod 3)` the share is 0% because the inverse predecessor `(2q − 1)/3` always exists. The first ancestor-free states are 7, 9, 25, 27, 33, 39, 43, 57, 73, 75, ….

This is a finite count, not a density theorem. It says that R49's "no smaller ancestor at any depth" is the case for about half of all canonical states up to `2·10⁶`, not only for isolated anchors. For those states every certificate has to involve forward motion. It is the measured counterpart of the heuristic sentence withdrawn at 23:46.

`python3 sidekick/probes/r49_ancestor_free.py` (about 2 s; receipt alongside)

---

## 2026-10-18 02:02 — SYNTHESIS: a consolidated map of the programme (`sidekick/writeup/SYNTHESIS.md`)

`sidekick/writeup/SYNTHESIS.md` is a single survey of R1–R71 and C1–C5, through main commit `ea3278e`, together with the side lane's checks. It covers:

- the reduction chain down to the W5 obligation, and its `u ↔ 18u + 5` form;
- the ranks and the seventeen strict-ρ families;
- the scoped obstructions, with their scope sentences;
- the side lane's measurements;
- the stopping-threshold equivalence;
- the controls and transfer, with the integrality caveat;
- the programme's position in the literature (Terras, Lagarias, Bernstein, Berg–Meinardus, Bell–Lagarias, Siegel, Tao, Simons–de Weger, Hercher, Barina, Conway).

Appendix A is a verification ledger in three parts:

- every main result, with its side-lane check or "not touched";
- every main review of the side lane, with its outcome;
- every side-lane correction and withdrawal.

No novelty claims are made. Status labels follow `AGENTS.md`.

---

## 2026-10-18 01:52 — ACK: main's review of the transfer and catalogue entries (`side_lane_review_678e565.md`, in `ea3278e`)

- **Reproduction.** Main reran both probes, unchanged and under process caps, and the receipts were byte-identical.
- **Accepted.** The review accepts the covariance identities, the `u ↔ 18u + 5` restatement, and the catalogue as control data.
- **Rejected.** It rejects the finite-base-only inference from 01:04, which was already withdrawn at 01:3x.
- **Numbering.** The halving bridge is R23 in main's numbering, not R27. The 01:04 entry and the probe docstring are corrected.
- **Scope of the controls.** As the review notes, the mechanical-family controls vary `d`. They do not refute a method that has verified base cases and a valid integer induction. Their role is to show which domain and arithmetic hypotheses a proposed universal argument actually uses.

---

## 2026-10-18 01:43 — VERIFIED: R71's mechanical-word denominators (main working copy)

These checks use exact rational arithmetic and this branch's own iteration, not main's code. The test covers every `k ≤ 14`, every `A` with `3^k < 2^A ≤ 2^(⌈k log₂3⌉+6)`, and every offset `l`, for 735 words in all. For the mechanical word `a_i(l) = ⌊((i+1)A+l)/k⌋ − ⌊(iA+l)/k⌋`:

- **Rotation identity and exact valuations.** `3B_i + D = 2^(a_i)·B_(i+1)` holds for every rotation, with every `B_i` odd. Iterating the cycle point reproduces each valuation exactly.
- **Denominators.** Every state of the cycle has reduced denominator `2^(A/g) − 3^(k/g)`, where `g = gcd(A, k)`.
- **Integral cases.** The only integral cases are the 105 all-2s words, whose cycle is `{1}`.

`python3 sidekick/probes/r71_mechanical_check.py` (under 1 s; receipt alongside)

---

## 2026-10-18 01:31 — CORRECTION to the 01:04 transfer entry

The 01:04 entry said that `d = 1` "can enter only through the finite base region". That conclusion holds only for arguments that use nothing but the transferred identities: valuation words, normal-form steps and rank comparisons.

Under `x ↦ x/d`, the integers for `S_d` correspond to rationals in `d⁻¹Z` for `S_1`, not to integers. So exact integrality of states along a whole word does not transfer, and it can separate values of `d` at any height. Main's in-progress R71 note (`lattice_cycles/BALANCED_DENOMINATORS.md`) makes this point and gives an example. Every state of a mechanical valuation word's cycle has reduced denominator `2^(A₀) − 3^(k₀)`. Those cycles therefore sit above any prescribed constant and are never integral, apart from the all-2s word.

The corrected statement: arguments that use only the transferred identities cannot detect `d` except through which classes hold the base and the cycles. A proof for `d = 1` therefore needs some input that does not transfer. Exact integrality along whole words is such an input.

---

## 2026-10-18 01:20 — TOOL: catalogue of positive rational 3x+1 cycles, as control points; ACK main's review of the 00:53 entry

**Catalogue.** Every periodic valuation word with `2^m > 3^k` has exactly one 2-adic point that follows it forever. That point is `x = B_W/(2^m − 3^k)`, a positive rational with odd denominator, and it is a cycle point of 3x+1. Multiplying by the reduced denominator `d` turns it into an integer cycle of 3x+d (01:0x entry).

`sidekick/frameworks/rational_cycles.py` lists every primitive word with `k ≤ 9` and `m ≤ ⌈k·log₂3⌉ + 2`, and checks each cycle by exact iteration:

- There are 3,889 cycles. The only integral one is `{1}`.
- After rescaling, they reproduce known integer cycle minima: 3x+5 has 1, 19, 23; 3x+7 has 5; 3x+13 has 1, 211, 227, 251, 259, 283, 287, 319.
- The largest minimum is `319/13 ≈ 24.5`, at `(k, m) = (5, 8)`.

The catalogue (receipt `rational_cycles.json`) gives control points for any whole-type claim. A statement proved from 2-adic, 3-adic and size identities alone also holds at these points. There, forward descent fails at every cycle minimum, and the orbits never reach 1.

**ACK.** Main's review `side_lane_review_33c3829.md` (in `a489973`) reproduces both 00:53 probes exactly and confirms the stopping-threshold argument. It also correctly notes that the equivalence does not force every useful construction to follow this particular prefix.

`python3 sidekick/frameworks/rational_cycles.py` (about 1 min)

---

## 2026-10-18 01:04 — FINDING: the framework's identities transfer verbatim to 3x+d (gcd(d, 6) = 1); a one-line form of the target  [one sentence corrected at 01:31]

**Transfer.** For odd `d`, write `T_d(x) = (3x + d)/2^v2(3x + d)`. Then `T_d(dy) = d·T_1(y)` on 2-adic integers. So on `Z_2`, and on positive rationals with denominators prime to 6, 3x+d is 3x+1 rescaled by `d`. A finite word of valuations, an elementary normalization, a halving bridge or a cycle word for 3x+1 becomes the same object for 3x+d, with every `x` replaced by `x/d` and residue classes multiplied by `d` modulo `2^k·3^j`. Ratios of states, and hence rank comparisons, are unchanged.

We check this for `d ∈ {1, 5, 7, 13, 61}:

- **R23 halving** [numbering corrected from R27 at 01:52]. `x = 2^a t − d` with `t/d ≡ 3^a (mod 4)` gives `S_d^a(x) = S_d^a((x − d)/2)`, in about 1,000 cases per `d` with `a ≤ 11`.
- **R54 family.** `n₀ = 81·2^(11r+6)s − 17d` follows `(1,1,1,2,1,1,4)` `r` times, with `Ψ_d(n) + 17d = (2187/2048)(n + 17d)`. Every state stays at least `n₀`. This holds in 16 cases per `d`.

Consequently, any whole-type theorem built only from such identities and rank comparisons also holds for every 3x+d with `gcd(d, 6) = 1`. ~~The specific value `d = 1` can enter only through the finite base region: the classes holding the absorbing point `d`, and, for `d ≠ 1`, the extra cycles.~~ [corrected at 01:31: this holds only for arguments restricted to the transferred identities; see the 01:31 correction] Several of those maps, such as 3x+5, 3x+13 and 3x+61, have several positive cycles.

**One-line form of the target.** For `w = 4u + 1 ∈ W5` we have `S(w) = S(u)` and `S(3w) = 18u + 5`. With R40, Collatz is therefore equivalent to this:

> For every odd `u`, the orbits of `u` and `18u + 5` meet.

As a sanity check, the derivation holds and the pairs meet for every odd `u < 10⁵`.

`python3 sidekick/probes/transfer_3xd.py` (under 1 s; receipt alongside)

---

## 2026-10-18 00:53 — FINDING (written proof + validation): with target (8ρ(w) − 5)/9, plain quotient-orbit prefixes are strict-ρ plans for every W5 input

**Statement.** Let `w ∈ W5`, `q = ν(3w) = ρ(w)` and `z = ν(w)`. Follow `T = ν∘S` from `q` to the first state `x` with `9x + 5 < 8ρ(w)`. Then

```
J = N_3w + Σ_(i<n) quotient_bridge(Tⁱq) + H_x − N_w − H_z
```

has divergence `P(w) − requests(H_x) + requests(H_z)`, and every request has `ρ(u) < ρ(w)`.

**Proof, from main's own theorems.**

- **Requests of `H_x`.** R51 gives `σ(u) ≤ ν(x) = x`. R62 (1) says `ρ(u) = (9σ(u) + 5)/8` on `E` and `ρ(u) = σ(u)` off `E`. Either way `ρ(u) ≤ (9x + 5)/8 < ρ(w)`.
- **Requests of `H_z`.** R43 gives `ρ(u) ≤ (9z + 5)/8`. With `z ≤ (w − 1)/4` and `ρ(w) > w`, this is below `ρ(w)`.

For `w ∈ E` the target equals `σ(w)`, so these are exactly the 23:43 σ-plans. For `w ∉ E` the target is `(8ρ(w) − 5)/9` rather than `ρ(w)`, which removes R62's window (2).

**Consequence.** Induct on ρ, then apply R40's equivalence. Collatz is then equivalent to the following statement:

> For every `w ∈ W5`, the quotient orbit of `q = ν(3w)` reaches a state below `(8q − 5)/9`.

A complete strict-ρ recursion for all of W5 is therefore the same thing as this quotient stopping-time statement for the critical images `ν(3w)`. No rule recognition is involved; the lookahead is that orbit's own stopping time.

**Validation.** Main's own ρ validator (`critical_rank.rank_closure.validate_step`, at `793e835`) accepts all 3,600 plans, 1,200 each at 24, 40 and 64 bits, across every class. The table gives the share of inputs that need at most `n` quotient steps.

| n ≤ | 2 | 4 | 8 | 16 | 32 |
|---|---:|---:|---:|---:|---:|
| share | 13.0% | 49.1% | 76.1% | 92.4% | 98.7% |

The largest `n` observed is 79.

`python3 sidekick/probes/rho_prefix_plans.py` (about 25 s; receipt alongside)

---

## 2026-10-18 00:53 — VERIFIED: R62's σ/ρ compatibility theorem on actual σ-plans (main `793e835`)

- **Identity (1).** `8ρ(u) = 9σ(u) + 5` holds on 20,000 random `E` inputs.
- **The theorem.** We apply it to 3,000 quotient-prefix σ-plans from the 23:43 entry, 1,000 each at 24, 40 and 64 bits.
  - All 159 plans with an `E` parent are ρ-valid.
  - For the 2,841 plans with a parent outside `E`, the requests with `ρ(u) ≥ ρ(w)` are exactly the `E`-requests in window (2), in every case.
- **How often the frontier is empty.** 2,836 of those 2,841 plans (99.8%) are already strictly ρ-decreasing. The 00:53 entry above removes the remaining window cases by stopping at `(8ρ(w) − 5)/9` instead of `ρ(w)`.

`python3 sidekick/probes/r62_compatibility_check.py` (about 20 s; receipt alongside)

---

## 2026-10-18 00:22 — FINDING: the full signed closure of the fifteen-family dispatcher either finishes outright or stops about 2 bits below its root

This runs main's `refined_rules.close(w)` (commit `d265d94`) on random `w ≡ 5 (mod 8)`, 200 per size. That call expands every accepted plan recursively under strict ρ and keeps unrecognized inputs as signed leaves. No run reached the 20,000-node cap.

Column key:

- **root accepted:** `one_step(w)` returns a plan.
- **complete:** no leaf remains after exact cancellation.
- **leaves < 2²⁰:** every leaf is small enough for a finite table.
- **median gap:** the median of `log₂(ρ(w)/max leaf rank)` over closures with leaves.
- **gap ≥ 8:** the share of those closures whose gap is at least 8 bits.

| bits | root accepted | complete | leaves < 2²⁰ | median leaves | median gap | gap ≥ 8 |
|---|---:|---:|---:|---:|---:|---:|
| 16 | 74.5% | 11.0% | 100% | 1 | 1.42 | 10.7% |
| 24 | 62.5% | 5.5% | 37.0% | 1 | 1.25 | 13.2% |
| 32 | 72.0% | 6.0% | 11.5% | 2 | 1.42 | 14.4% |
| 48 | 71.0% | 5.5% | 6.0% | 3 | 2.08 | 16.9% |
| 64 | 76.0% | 5.5% | 5.5% | 3 | 2.08 | 14.3% |

Two features stand out:

- **A size-stable complete core.** About 5.5% of inputs close completely at every size from 24 to 64 bits. These closures are large: at 64 bits they expand 41 to 149 nodes (median 86), and at 48 bits 26 to 82. Independent ~70% acceptance at that many nodes would almost never finish, so the completions look structural. Their root rules are mainly R55, R48 and R41.
- **The rest stall near the top.** In the other closures, the largest leaf sits a median 1.3 to 2.1 bits below `ρ(w)`, and only 11–17% reach a gap of 8 bits. The share whose leaves all fit a fixed `2²⁰` table falls toward the complete-core share as size grows.

For the whole-recursion target in main's decision note (`side_lane_review_767af32.md`), then, the leaves to eliminate sit close to the original rank rather than spread down the tree.

**Addendum.** The complete core is not a union of low-modulus classes. At 32 bits, with 16 samples in each of the 72 W5 classes mod 576, no class closes completely more than 31% of the time; 35 classes never close completely, and the best class is 221. (`python3 sidekick/probes/complete_core_classes.py`, about 1 min.)

`python3 sidekick/probes/closure_frontier_meter.py` (about 3 min; receipt alongside)

---

## 2026-10-18 00:16 — VERIFIED: R58's classification of above-seed absorption requests (main working copy)

R58 states the following, with `n = ν(s)`:

- `H_s` never requests a rank above `n`, except in one case: `n ≡ 27 (mod 48)`, `v2(3n − 1) = 4`, and `3z` noncanonical, where `z = (3n − 1)/16`.
- In that case exactly one request is higher: `u* = 4z + 1`, with coefficient `+1` and `ρ(u*) = (9n + 5)/8`. Every other request then has `ρ < n`.
- For noncanonical `s`, every request has `ρ < s`.

We test these statements against main's committed R43 plans (`critical_rank/rank_closure.absorption_plan` at `7206f9c`), not R58's new module. The test covers 112,000 seeds:

- every odd `s` in `[3, 200001]`;
- 3,000 random odd `s` at each of 40 and 64 bits;
- 3,000 random canonical exceptional `n` at each of those sizes.

Every seed matches the statement: 103,773 ordinary cases, 8,227 exceptional cases with exactly the stated single `u*`, and 53,006 noncanonical seeds, all with requests below `s`.

`python3 sidekick/probes/r58_excess_check.py` (about 2 min; receipt alongside)

---

## 2026-10-17 23:51 — FINDING: the twelve-family dispatcher accepts a size-stable ~70% of W5

This is the same meter as the 22:46 entry, run on main's `selected_rules/selected_rules.py` (commit `7206f9c`), with 1,000 random `w ≡ 5 (mod 8)` per size.

| bits | 10 | 14 | 18 | 24 | 32 | 48 | 64 |
|---|---:|---:|---:|---:|---:|---:|---:|
| accepted | 67.7% | 69.5% | 71.6% | 72.2% | 68.7% | 69.5% | 70.7% |
| of which R55 | 22.3% | 21.1% | 23.5% | 24.0% | 21.2% | 21.0% | 24.5% |

- **Growth.** Acceptance was about 43% for the seven-rule union (22:46). The rise to about 70% is mostly R55.
- **R56 and R57.** These are in priority after the older rules, plus R55 in R57's case, so in these samples R56 is never the accepting rule and R57 accepts at most 0.2%. Their domains are thin progressions; for example R56's k4 class is `w ≡ 718 (mod 729)`.

**Acceptance by class at 48 bits:**

| class | accepted |
|---|---:|
| 3w selected, w ≡ 0 (mod 3) | 92% |
| 3w selected, w ≡ 1 (mod 3) | 75% |
| 3w selected, w ≡ 2 (mod 3) | 62% |
| 3w non-selected, w ≡ 0 (mod 3) | 64% |
| 3w non-selected, w ≡ 1 (mod 3) | 57% |
| 3w non-selected, w ≡ 2 (mod 3) | 68% |

The selected class `w ≡ 2 (mod 3)` was at 0% before R55. This measures the dispatcher; it does not check it.

`python3 sidekick/probes/selected_rules_meter.py` (about 30 s; receipt alongside)

---

## 2026-10-17 23:51 — VERIFIED: R57's descending cycle-exit family (main `7206f9c`)

These checks use this branch's own `nu` and `step`, not main's code. We take `r = 0..4`, odd `d ∈ {2r+5, 2r+7, 2r+9}`, and the first three positive members of progression (7), 45 inputs in all. For each:

- **The input.** `q = 81·2^(11r+12)s − 17` and `w = (2q+1)/3 ≡ 3445 (mod 3456)`, with `ν(3w) = q` and `v2(q + 17) = 11r + 12`.
- **The cycle copies.** Each of the `r` guarded copies is the ordinary word `(1,1,1,2,1,1,4)`, ending at `Ψ(x)`. Seven quotient steps reach the same point.
- **The exit.** `V = ν(S⁴(Q)) = 3^(7r+8)·64s − 21`, with `a(V) = 2` and `v2(3t − 1) = d`. The endpoint `f` of (8) equals `3^b(3t − 1)/2^d`.
- **Clocks and descent.** `T^(7r+b+5)(q) = ν(f)` and `S^(7r+b+6)(q) = S(f)`, and `(9f + 5)/8 < q`.

Of the 45 inputs, 15 lie in the subprogression (16). Each of them has `v = (32q − 23)/81 ≡ 0 (mod 3)`.

`python3 sidekick/probes/batch_r57_check.py` (under 1 s; receipt alongside)

---

## 2026-10-17 23:46 — CORRECTION to the 23:32 entry; ACK main's review of it

- **Correction.** The 23:32 heuristic ended with "a positive fraction of `q ≡ 1 (mod 3)` have no smaller ancestor at all". The moment bound `M(θ)ⁿ` does not imply this. A summable expected number of deep smaller ancestors still allows every `q` to have one. A positive probability of having none needs a separate non-hitting argument, or a total expectation below 1, and neither was shown. The sentence is withdrawn. The capped search rates (8.7% at the default budget, 9.3% at the larger one) remain finite evidence under their stated caps only.
- **ACK: main's review.** Main's working-copy review `side_lane_review_bae3969.md` reproduces the seven-arrow word and adds three things:
  - On the word's exact domain the plan strictly decreases ρ for every input, not only in the 12 tested cases.
  - That domain, `q ≡ −17 (mod 2187)`, which is `w ≡ 718 (mod 729)`, is exactly R56's k4 domain. The word therefore gives an independent reading of R56, not extra coverage.
  - An arbitrary smaller ancestor need not decrease ρ. In the selected `w ≡ 1 (mod 3)` sample, 31 plans were σ-valid and 30 of those decreased ρ.

---

## 2026-10-17 23:45 — VERIFIED: R53's delayed-exit family and its low-run law (main `8764158`)

These checks use this branch's own `nu` and `step`, not main's code.

We take `r = 1..6`, `d = 4r + 3`, and the first three positive members of the CRT progression (12), 18 inputs in all. For each:

- **The input.** `w = (2^(3r+8)s − 11)/9` is in `W5`, with `w ≡ 13 (mod 32)`, `w ≡ 45 (mod 81)`, and `3w` non-selected.
- **The prefix.** The ordinary word from `q = 3w` is `(1,1,2)` to `x0 = 9·2^(3r+4)s − 5`, then `(1,2)^r` to `xr = 16·9^(r+1)s − 5`. Every boundary is `≡ 1 (mod 3)` and exceeds `q`.
- **The exit.** At `xr`, `a = 2` and `v2(3t − 1) = 4r + 3`.
- **The endpoint.** `T^(a+b−1)(xr) = ν(y)`, with `y` as in (8), and `(9y + 5)/8 < q`.

For 4,000 consecutive `x ≡ 27 (mod 32)`, we also check `S² = (9x + 5)/8` with valuations `(1,2)`, and that the maximal run length is `⌊(v2(x + 5) − 2)/3⌋`.

`python3 sidekick/probes/batch_r53_check.py` (under 1 s; receipt alongside)

---

## 2026-10-17 23:43 — FINDING: under R51's σ, plain quotient-orbit prefixes give validated plans on all sampled W5, including the selected classes no current rule reaches

**Construction.** Let `w ∈ W5` and `q = ν(3w)`. Iterate `T = ν∘S` from `q` to the first state `x < σ(w)`, which takes `n` quotient steps. With `z = ν(w)`, the current

```
N_3w + Σ_{i<n} quotient_bridge(Tⁱq) + H_x − N_w − H_z
```

has divergence `P(w) − requests(H_x) + requests(H_z)`. R51's bound gives every request `σ ≤ max(x, z) < σ(w)`. This is R51's forward check with an arbitrary quotient prefix in place of a block endpoint.

**Validation.** Every plan is built from main's own `bridge`, `quotient_bridge` and `absorption_plan` (commit `8764158`). Main's `sigma_rank.validate` accepts all 3,600 random inputs, 1,200 at each of 24, 40 and 64 bits, across every class.

**Lookahead `n` needed, by class.** The second column is the share main's continued dispatcher accepts (seven rules + R52 + R53); the rest are cumulative shares by lookahead.

| class | continued dispatcher | n ≤ 2 | n ≤ 4 | n ≤ 8 | n ≤ 16 | n ≤ 32 | max n |
|---|---:|---:|---:|---:|---:|---:|---:|
| 3w selected, w ≡ 2 (mod 3) | 0.0% | 26% | 59% | 83% | 94% | 99.2% | 42 |
| 3w selected, w ≡ 1 (mod 3) | 13% | 27% | 59% | 82% | 94% | 99.2% | 44 |
| 3w selected, w ≡ 0 (mod 3), not returning | 100% | 27% | 58% | 78% | 92% | 98.4% | 64 |
| 3w selected, returning (w ≡ 3 mod 9) | 75% | 24% | 62% | 82% | 92% | 98.5% | 51 |
| 3w non-selected, w ≡ 0 (mod 3) | 57% | 0% | 37% | 71% | 89% | 98.0% | 77 |
| 3w non-selected, w ≡ 1 (mod 3) | 58% | 0% | 36% | 69% | 88% | 97.6% | 74 |
| 3w non-selected, w ≡ 2 (mod 3) | 60% | 0% | 35% | 68% | 88% | 97.7% | 89 |

Across all inputs, the shares needing `n ≤ 2, 4, 8, 16, 32` are 13%, 48%, 75%, 91% and 98.4%.

The two selected classes that the dispatcher barely reaches need *shorter* quotient prefixes than the non-selected classes. For this one plan family, the residual at lookahead `L` is exactly the set of `w` whose `ν(3w)` has quotient stopping time below `σ(w)` greater than `L`. Other σ-rules may do better.

Each fixed quotient word is affine on a 2-adic class of `q`, so these plans can be grouped into CRT families of the same kind as the existing rules, apart from finitely many small exceptions per word. This also fits the 23:32 entry. There, the R54 phase and the deep cycle shadows fail every bounded lookahead, which in this language means a long quotient stopping time.

`python3 sidekick/probes/sigma_stopping_plans.py` (about 40 s; receipt alongside; imports main's code read-only)

---

## 2026-10-17 23:32 — FINDING: R54's Ψ and R53's G are the negative cycles −17 and −5; one backward word resolves the `27 | s` part of R54's family  [one sentence withdrawn at 23:46]

**The cycles.** Extend `ν` to negative odd integers: F⁻¹ on `x ≡ 5 (mod 8)`, and halving on selected `x ≠ −1`. On `|x| ≤ 4000`, `T = ν∘S` then has exactly three cycles:

- `{−1}`
- `{−5, −7}`
- `{−17, −25, −37, −55, −21, −31, −23}`

Each of main's growing return maps is the return map of one of these cycles:

- R54's `Ψ(q) + 17 = (3⁷/2¹¹)(q + 17)` belongs to the 7-cycle (7 odd steps, 11 halvings). R54's column "shadow at q = −17" lists that cycle.
- R53's `G(x) + 5 = (9/8)(x + 5)` belongs to `{−5, −7}`.
- The climber runs shadow `−1`.

The negative `W5` indices with `|w| ≤ 4000` whose critical image lies on a cycle are only `w = −11` (`q = −17`) and `w = −3` (`q = −5`). R54's phase is `3445 ≡ −11 (mod 3456)`, and its row-4 `W9` index is `v = −7`, at `q = −21`.

**Why forward rules fail near these points.** A positive `q` that is 2-adically close to a cycle point follows that cycle for a number of blocks proportional to the 2-adic depth. Each block multiplies by the cycle's factor, which is greater than 1, so every forward state in that prefix exceeds the start.

**The backward word.** Running backward around the cycle multiplies by `2¹¹/3⁷ < 1`. Take any odd `q ≡ −17 (mod 3⁷)`. The seven inverse steps with exponents `(4,1,1,2,1,1,1)` are then integral, and they give an S-ancestor below `q`:

```
p = (2048q − 2363)/2187 < q,   S⁷(p) = q.
```

The condition is 3-adic only, so it holds at every 2-adic depth. With `z = ν(w)`, the current

```
N_3w − path(p→q) + H_p − N_w − H_z
```

has divergence `P(w) − requests(H_p) + requests(H_z)`. By R51, every request has `σ ≤ max(p, z) < q = σ(w)` when `w ∉ E_return`.

In R54's parametrization `q₀ = 81·2^K·s − 17`, the word applies exactly when `27 | s`. We tested `r = 1, 2, 3` with `s = 27, 54, 81, 135`, 12 cases in all:

- Main's `sigma_rank.validate` accepts the plan in every case.
- The plan also strictly decreases ρ in every case.
- A best-first preimage search finds this word first in every case.

R41's word at `h = 2` is the corresponding backward word of `{−5, −7}`, since `(8q − 5)/9 = G⁻¹(q)`.

**Beyond `27 | s`** (measurement). The general smaller-ancestor rule, built the same way, searches S-preimages best-first with a 4,000-node budget and a cap of `64q`. The table counts how many of 300 inputs per row it resolves; the inputs are 40-bit and are ones main's continued dispatcher leaves unresolved.

| inputs | resolved |
|---|---:|
| R54 phase `w ≡ 3445 (mod 3456)` | 29 / 300 |
| `3w` selected, `w ≡ 1 (mod 3)` | 31 / 300 |
| `3w` selected, `w ≡ 2 (mod 3)` | 3 / 300 |

On a separate R54-phase sample, raising the budget to 200,000 nodes and the cap to `2¹⁶ q` moves the rate only from 8.7% to 9.3%. A heuristic suggests why it saturates. Treat preimage residues mod 3 as random. Then the expected number of depth-`n` ancestors below `q` is at most a constant times `M(θ)ⁿ` for every `θ > 0`, where `M(θ) = 3^(θ−1)/(2^θ − 1)`. Its minimum is exactly `c^c/(2^c(c−1)^(c−1)) ≈ 0.9465`, with `c = log₂3`. That is the forward cylinder rate of the 19:48 entry and main's R28, under the shift `θ → θ − 1`. ~~So in this model a positive fraction of `q ≡ 1 (mod 3)` have no smaller ancestor at all.~~ [withdrawn at 23:46: the moment bound does not imply it; see the 23:46 correction]

**Returning row near the cycle points** (measurement, 200 samples per row; every input has `3w` selected and `w ≡ 3 (mod 9)`).

| inputs | continued dispatcher | R51 σ dispatcher |
|---|---:|---:|
| generic, 40-bit | 155 | 116 |
| `w ≡ −3 (mod 2^K)` exactly, K = 12, 16, 20, 28 | 0 each | 0 each |
| `w ≡ −11 (mod 2^K)` exactly, K = 12 / 16 | 200 / 102 | 0 / 0 |
| `w ≡ −11 (mod 2^K)` exactly, K = 20, 28 | 0 each | 0 each |

R54 §7 puts its leading inputs outside `E_return`. `E_return` nonetheless has deep shadows of both cycle points that neither dispatcher accepts: at every tested depth from `K = 12` near `−3`, and at `K = 20` and `28` near `−11`.

`python3 sidekick/probes/negative_cycle_shadows.py` (about 15 s) and `python3 sidekick/probes/backward_word_rule.py` (about 1 s); receipts alongside. Both import main's code read-only.

---

## 2026-10-17 23:32 — VERIFIED: R51 rank values; R54 phase and seven-step family (main `8764158`)

These checks use this branch's own `nu` and `step`, not main's code:

- **R54 phase.** For 400 consecutive `w ≡ 3445 (mod 3456)`: each `w` is in `W5`, `3w` is selected, `w ≡ 1 (mod 3)`, and `ν(3w) ≡ −17 (mod 5184)`.
- **R54 family.** We take `q₀ = 81·2^(11r+6)·s − 17` for `r = 1..5` and `s ∈ {1, 2, 3, 7}`. Each of the `r` seven-step blocks of `T` ends at `Ψ(q) = (2187q + 2363)/2048`, with `Ψ(q) + 17 = (2187/2048)(q + 17)`. Every intermediate state exceeds `q₀`.
- **R51 values.** `ρ(44981) = 134943`, `ρ(96069) = 144103` and `σ(96069) = 128091`; also `σ(4629) = 6171` and `ρ(2197) = σ(2197) = 6591`.

`python3 sidekick/probes/batch_r51_r54_check.py` (under 1 s; receipt alongside)

---

## 2026-10-17 22:46 — FINDING: expanded seven-rule union covers a size-stable ~43% of W5; one class stays fully uncovered

This is the meter of the 22:21 and 22:44 entries, rerun on main's `double_inverse/expanded_union.py` (commit `bcde58e`). Each `w` is accepted when `one_step(w)` returns a validated plan.

| bits | 10 | 14 | 18 | 24 | 32 | 48 | 64 |
|---|---:|---:|---:|---:|---:|---:|---:|
| accepted | 41.5% | 43.3% | 43.7% | 42.4% | 41.8% | 41.5% | 42.6% |

The rate is stable across sizes, so the new rules are scale-uniform. Most of the gain is R48, at about 23–25% of `W5`. R47 and R50 each add under 0.5%.

**Uncovered fraction by class at 48 bits** (1,000 samples; each class is about one sixth of `W5`):

| class | uncovered |
|---|---:|
| w mod 3 = 2, 3w selected | 100% |
| w mod 3 = 1, 3w selected | 83% |
| w mod 3 = 0, 3w non-selected | 52% |
| w mod 3 = 1, 3w non-selected | 47% |
| w mod 3 = 2, 3w non-selected | 46% |
| w mod 3 = 0, 3w selected | 14% |

Two classes stay largely uncovered: `w ≡ 2 (mod 3)` with `3w` selected, which no rule touches, and `w ≡ 1 (mod 3)` with `3w` selected.

This measures the dispatcher; it does not check it.

`python3 sidekick/probes/expanded_union_meter.py` (about 20 s; receipt alongside)

---

## 2026-10-17 22:44 — FINDING: map of the uncovered part of W5 under the rule union

This uses the same dispatcher as the 22:21 entry (main `a06ef3c`), with 20,000 random 48-bit `w ≡ 5 (mod 8)`. Since `w ≡ 5 (mod 8)`, `3w ≡ 7 (mod 8)` is always a climber. Each class below is about one sixth of `W5`.

| class | share of W5 | uncovered | share of the gap |
|---|---:|---:|---:|
| w mod 3 = 1, 3w non-selected | 16.9% | 99% | 20.5% |
| w mod 3 = 0, 3w non-selected | 16.4% | 100% | 20.1% |
| w mod 3 = 2, 3w selected | 16.2% | 100% | 19.9% |
| w mod 3 = 2, 3w non-selected | 17.4% | 89% | 18.9% |
| w mod 3 = 1, 3w selected | 16.5% | 87% | 17.6% |
| w mod 3 = 0, 3w selected | 16.6% | 15% | 3.0% |

Overall, 81.6% of `W5` is uncovered.

- **Mostly covered.** Only `3 | w` with `3w` selected; this is R41's domain `E`, where the returning row `w ≡ 3 (mod 9)` stays open.
- **Essentially untouched.** Three classes: `3 | w` with `3w` non-selected; `w ≡ 2 (mod 3)` with `3w` selected; `w ≡ 1 (mod 3)` with `3w` non-selected. Together they make up about 61% of the gap.
- **Partly covered.** R46 covers part of `w ≡ 1 (mod 3)` with `3w` selected. R45 covers part of `w ≡ 2 (mod 3)` with `3w` non-selected.

This measures the dispatcher; it does not check it.

`python3 sidekick/probes/union_gap_map.py` (seconds; receipt alongside)

---

## 2026-10-17 22:21 — FINDING: the R41/R44/R45/R46 rule union accepts a size-stable ~18% of W5

This measures main's fixed-priority dispatcher in `critical_rank/rules_union.py` (commit `a06ef3c`), using its own predicates. For random `w ≡ 5 (mod 8)` of each bit size, it records whether some top-level strict-rank rule accepts `w`. Rules are tried in the union's order: R41, R45, R44 (descending only), R46.

| bits | 10 | 14 | 18 | 24 | 32 | 48 | 64 | 80 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| accepted | 17.2% | 17.4% | 18.3% | 18.6% | 18.0% | 19.1% | 18.7% | 17.3% |

There are 4,000 samples at 18 bits and below, and 2,000 above. The acceptance rate is stable across sizes; the rules do not favour small inputs. The complement, where supplied currents are still required by R43's composition theorem, is about 81–83% of `W5` at every size measured. By rule at 48 bits: R41 about 11.9%, R44 3.0%, R45 1.8%, R46 2.2%.

This measures the dispatcher; it does not check it independently.

`python3 sidekick/probes/union_acceptance_meter.py` (seconds; receipt alongside)

---

## 2026-10-17 22:16 — VERIFIED: R46 escape identity and depth-4 law; R44/R45 rank values (main `a06ef3c`)

These checks use this lane's own `ν` and Syracuse step.

**R46 identity.** Take canonical `q > 1` with `q ≡ 1 (mod 3)`. Set `D = v3(q−1)`, `u = (q−1)/3^D`, `j = v3(4^D u + 2)` and `p = 2^j(4^D u+2)/3^j − 1`.

- The exact valuation word `1^j, 2^D` takes `p` to `q`.
- `p < q` holds exactly when `2^(2D+j) < 3^(D+j)`.

Both hold for all 33,333 such `q < 400000`.

**R46 depth-4 law, by brute force.** For all 1,112 canonical `q ≡ 1 (mod 18)` below 40,000, using quotient predecessors under `T = ν∘S`:

- no ancestor `y < q` exists at depths 1–3;
- at depth 4 one exists exactly when `q ≡ 10 (mod 81)`;
- that ancestor is uniquely `(64q−73)/81`, with valuation word `1, 1, 2, 2`.

The search is complete. Every `T`-preimage of `t` is at least `(2t−1)/3`, so chains that pass above `100q` cannot fall below `q` within four steps.

**Rank values.** With `ρ(w) = ν(3w)`: `ρ(6645) = 9967`, `ρ(4205) = 12615` and `ρ(1613) = 4839`, as stated.

The R43 composition theorem and the R44/R45 accepted-domain classifications were not rebuilt here.

`python3 sidekick/probes/batch_r43_r46_check.py` (about 3 s; receipt alongside)

---

## 2026-10-17 21:53 — VERIFIED: R37 planner properties, R40 tripling bound, R41 ancestor identity and inverse barrier (main `4a45eb0`)

These were rebuilt from the text of `CRITICAL_NINE_ELIMINATION.md` §2 and R41, with this lane's own `ν` and Syracuse step.

**R37 planner, as restated in R40.** The rules are:

- normalize `q = ν(x)`;
- if `q ≡ 1 (mod 8)`, step to `S(q) < q`;
- if `q ≡ 2 (mod 3)`, go to `(2q−1)/3 < q`;
- otherwise request `u = q/3` or `(2q+1)/3`, and continue from `u`.

Checked for all 99,999 odd `x < 200000`: it terminates, every request lies in `W5 ∪ W9`, requests strictly decrease, and `u ≤ (2x+1)/3`.

**R40 sharper tripling bound.** Every index in `I(3z) ∪ I(z)` is at most `(3z+1)/2`. Checked for all odd `z < 60000`.

**R41 ancestor identity.** For every odd `q ≡ 4 (mod 9)` below `10^6`, `p = 2^h(2q+1)/3^h − 1` with `h = v3(2q+1) ≥ 2` reaches `q` by the exact valuation word `1^(h−1), 2`, and `p < q`.

**R41 inverse barrier, by brute force.** The check covered 76 canonical `q < 4000` with `q ≡ 1 (mod 3^D)`, `D = 2, 3`, searching all `y < 2·10^6` with `T^j(y) = q`, where `T = ν∘S` and `j ≤ D`. Every such `y` is larger than `q`, and the least is `(4q−1)/3`, as stated.

The full R40 elimination compiler, with its per-`d` local identities, was not independently rebuilt here.

`python3 sidekick/probes/batch_r40_r41_check.py` (about 6 s; receipt alongside)

---

## 2026-10-17 21:31 — VERIFIED: R37 critical-domain bijection, R38 interface, R39 coupled recursion (main `436f51f`)

Everything was rebuilt with this lane's own normal form `ν` and Syracuse step.

**R37.** `W = {w ≡ 5 (mod 8)} ∪ {w ≡ 9 (mod 16)}`, and the claim is that `w ↦ ν(3w)` is a bijection from `W` onto the critical roots. Those are the canonical, non-selected climbers `≢ 2 (mod 3)`.

- All 16,668 critical roots below 200,000 map back into `W` under the stated inverse (`q/3`, or `(2q+1)/3`). The inverse is always smaller than `q`, and `ν(3w) = q` recovers the root.
- All 16,668 images of `W` below 200,000 are critical and distinct.

**R38.** For all 100,000 odd `z < 200000`, the identities `ν(6z+1) = ν(3u)` and `ν(z) = ν(u)` hold, where `u = z` if `3z` is canonical and `u = 4z+1` otherwise. So `Q(z) − P(u)` is elementary.

**R39.** For all 6,250 `v ≡ 19 (mod 32)` below 200,000, with `t = (3v−1)/8 < 3v/8`, the pairs `18v+3 ~ 18t+3` and `v ~ t` each meet at a state other than 1 within 3 steps. This is a genuinely local current. The terminal cylinder `v ≡ 39 (mod 8192)` satisfies `S^5(18v+3) = S^7(v)`.

**Controls on `W` itself.** The generic statement that `w` and `3w` share a future fails on `W` for every control map. Counts are below 4000:

- `3x−1`: 336 cases; for example `w = 5` (cycle `{5, 7}`) against `15` (trivial).
- `3x+13`: 285 cases; for example `w = 41` (trivial) against `123` (cycle at 259).
- `3x+61`: 57 cases; for example `w = 133` (trivial) against `399` (the 41-cycle).

**ACK.** R37/R38 state that universal currents for `P` on `W` are equivalent to Collatz. That agrees with the class-wise picture in PR1's C5 and the 19:40 entry.

`python3 sidekick/probes/batch_436f51f_check.py` (about 1 s; receipt alongside)

---

## 2026-10-17 21:09 — COUNTEREXAMPLE (generic form): the tripling-pair merger fails on maps with cycles

R35 (main `1603bf3`) leaves tripling pairs `P(w) = δ(3w) − δ(w)`, for `w ≡ 3 (mod 8)`, as an open obligation, together with doubling pairs. A universal certificate for `P(w)` implies that `w` and `3w` share a future, possibly only at the absorber.

On the control maps that statement fails at many `w ≡ 3 (mod 8)` below 4000:

| map | counterexamples | first examples |
|---|---:|---|
| `3x−1` | 357 | `w = 3` (trivial basin) and `9` (cycle `{5, 7}`); `w = 11` (trivial) and `33` (cycle at 17) |
| `3x+13` | 100 | `w = 19` (cycle at 131) and `57` (trivial) |
| `3x+61` | 30 | `w = 235`, on the 41-cycle, and `705` (trivial); also `w = 451, 707, 883` |

A rule that certifies every tripling pair must therefore use arithmetic that these maps lack. The `3x+61` cases are locally Collatz-like: every core point and every seed below 175 terminates there. They can serve as regression inputs for any generic version of a pair rule. The statement for `d = 1` is not tested here.

`python3 sidekick/probes/pair_merge_controls.py` (seconds; receipt alongside)

---

## 2026-10-17 21:06 — VERIFIED: R33 acceptance measure, R34 identities, R36 Mersenne mergers (main `1603bf3`)

Everything was rebuilt from the statements, using this lane's own Syracuse step and normal form `ν`.

**R33.** The mixed shrinking recognizer is rebuilt from its rules: branches O, E1 and E2, plus the even-case terminal test "`z` canonical". Its acceptance fraction among `w ≡ 3 (mod 8)` agrees with the stated cylinder measure `32/157 ≈ 0.203822`.

| sample | acceptance | difference |
|---|---:|---|
| full enumeration, `[2^21, 2^22)` | 0.203766 | |
| full enumeration, `[2^19, 2^20)` | 0.203888 | |
| 2,000,000 random 60-bit | 0.20366 | `−0.6σ` |
| 2,000,000 random 100-bit, run 1 | 0.20414 | `+1.1σ` |
| 2,000,000 random 100-bit, run 2 | 0.20423 | `+1.4σ` |

**R34.**

- `η(q) = 2^h(q+1)/3^h − 1` with `h = v3(q+1)` satisfies `S^h(η(q)) = q` for every odd `q < 20000`.
- On the cylinder `x ≡ 19199 (mod 65536)`, the numerators of `q` and `p` are exact, and `S^9(x) = S^2(p)`.
- Root `84735` gives `q = 67865 > N` and `p = 45243 < N` at `N = 65536`.

**R36.** `S^t(2^a−1) = S^t(2^(a−1)−1)` holds at `a = 1699` with `t = a+4`, and at `a = 659` with `t = a+5`.

`python3 sidekick/probes/batch_r33_r36_check.py` (about 1 s; receipt alongside)

---

## 2026-10-17 20:44 — VERIFIED: concrete identities in R30, R31, R32 (main `64fff1d`); ACK R32 scope

All checks below were rebuilt from the statements with this lane's own Syracuse step and annulus point evaluator.

**R30, shrinking pairs.**

- Take `w ≡ 3 (mod 8)` with `h = v2(3w−1) = 2k+2` even, and set `z = 3^k(3w−1)/2^h`. Then `S^k(3w) = 4z+1` and `S^(k+1)(w) = 2z+1`. This holds for all 10,922 such `w < 2^18`.
- When `z ≡ 101 (mod 128)`, the child `w′ = (3z+1)/16` satisfies `w′ ≡ 3 (mod 8)` and `0 < w′ < w/4`.
- Mersenne mergers `S^(a+3r+3)(2^a−1) = S^(a+3r+3)(2^(a−1)−1)` hold at `a = 199` and `a = 455` (`r = 1`, 205 and 461 steps), and at `a = 2887` (`r = 2`, 2896 steps).
- The `a = 39` example merges at step 47, which is `a + 8`.

**R31, bounded runs.**

- `4513·27 + 9221 = 2^17`.
- `4513·Ψ(x) + 9221 = (6561/2048)(4513x + 9221)`.
- `x ≡ −9221/4513 (mod 2^(11r+6))` forces `r` complete words `(1,2,1,1,1,1,2,2)`. This was checked by direct steps for `r = 1…6`.

**R32, early cancellation.** For `a = 19, 37, 55`, with `N = 12·2^(a−5)`, `z = 2^a−1`, `p = (4z−1)/3` and `q = 4p+1`, we have `A_N(p) = +1`, `A_N(q) = −1`, and `S(p) = S(q) = z`. `N` reaches about `1.35·10^16`.

**ACK.** R32's scoping of the earlier merge-density remarks is right on two points:

- Certifying by any common tail with known seeds amounts to being in the basin of 1, so no finite-sample density model can show that a proof must avoid mergers.
- R32's family cancels signed mass before its shared climb.

The 19:59 and 20:22 statements concern only roots that remain uncancelled along their own orbit.

`python3 sidekick/probes/batch_64fff1d_check.py` (under 1 s; receipt alongside)

---

## 2026-10-17 20:27 — FINDING: iterating the normalized return speeds up typical roots, not the slowest ones

This tests what happens if the R26 return is iterated. That means running the quotient map `q ↦ ν(S(q))` of R25 until it drops to `≤ N`.

**2-adic random model** (60,000 random 200-bit starts):

| map | mean drift per step | P(stay ≥ start), 15 steps | P(stay ≥ start), 30 steps | decay per step, 15→30 |
|---|---:|---:|---:|---:|
| `S` | -0.41 bits | 0.0348 | 0.0074 | 0.902 |
| `ν∘S` | -1.41 bits | 0.0177 | 0.0038 | 0.903 |

The quotient's mean drift is about 3.5 times stronger. The decay rate of staying high is the same within noise; only the constant changes. Its extra drops (F-chain `÷4`, halving `÷2`) matter only near the starting level.

**Actual R26 remainder at `N = 98304`** (1775 roots, after removing those certified by `ν(f(x)) ≤ N`):

- steps to reach `≤ N` under raw `S`: median 10, 90th percentile 25, maximum 81;
- steps under the quotient, started from `ν(f(x))`: median 5, 90th percentile 17, maximum 66.

The slowest roots are the same under both maps. For example `134379` needs 66 quotient steps against 72 raw.

Finite data and model estimates; no termination claim.

`python3 sidekick/probes/quotient_iteration_probe.py` (about 1 min; receipt alongside)

---

## 2026-10-17 20:26 — VERIFIED: R26 run bridges and coverage (main `541101a`, `complementary_bridge/RUN_BLOCK_BRIDGES.md`)

Return formulas were rebuilt from the statement. For a complementary root `x = 2^a t − 1`, put `z = 3^(a−1)t − 1`, `d = v2(z)` and `w = z/2^d`. Then `f(x) = 3^((d−1)/2)·w` when `d` is odd, and `f(x) = 2·3^(d/2)·w + 1` when `d` is even.

**Bridges.** All 25,002 complementary roots below 200,000 were checked.

- 25,000 have a common state with `f(x)` before 1. In 16,661 of them `f(x)` lies on `x`'s own orbit; in the other 8,339, `f(x)` is one step off.
- The `x` side needs at most 19 steps.
- The 2 remaining cases, `x = 75` and `x = 184111`, enter 1 through F-siblings of the absorbing class. For example `f(75) = 21` while `x`'s orbit reaches `85 = F(21)`.

**Coverage.** These use this lane's own normal form `ν` from the 20:23 entry. The certified complementary mass is the part with `ν(f(x)) ≤ N`.

| `N` | complementary mass | certified | remaining | remaining/`N` |
|---:|---:|---:|---:|---:|
| 6144 | 269 | 146 | 123 | 0.02002 |
| 49152 | 2132 | 1184 | 948 | 0.01929 |
| 98304 | 4269 | 2367 | 1902 | 0.01935 |

The `N = 6144` row reproduces main's stated 146 / 123 exactly. The larger cutoffs approach main's `≈ 0.01941·N`.

`python3 sidekick/probes/run_bridge_check.py` (receipt alongside)

---

## 2026-10-17 20:23 — VERIFIED: R27 fibre count (main `541101a`, `absorbed_fibers/ABSORBED_FIBERS.md`)

The normal form was rebuilt here by descent from the two bridge moves, without importing main's code:

- `x → (x−1)/4` when `x ≡ 5 (mod 8)`;
- `x → (x−1)/2` when `x` is a selected climber.

The fixed points of this descent are main's `B`.

Main's claim is `#(I_N ∩ [X, 2X)) = N/4 + O(log N)`, with error at most `2⌊log2 N⌋ + 3`. Two independent counts were checked against it:

- **Brute force.** Brute-force descent on every odd `x` in `[X, 2X)` agrees exactly with the count over the components `{F^k(q), F^k(2q+1)}`, `q ∈ B`, `q ≤ N`. This was checked for `N ∈ {8, 13, 64, 100, 257, 1000}` and `X` up to `N·2^14`.
- **Component count.** The component count stays within the stated bound for `X = N·2^64`, `N·2^200` and `N·2^512`. The largest error used is 19% of the bound.

`python3 sidekick/probes/fibre_count_check.py` (about 10 s; receipt alongside)

---

## 2026-10-17 20:22 — VERIFIED R28 tables; CORRECTIONS to the 19:46 and 19:59 entries

**VERIFIED (main `541101a`, R28).** This lane's dynamic program was extended with main's partial-closing rule. It now reproduces `cylinder_barrier/cylinder_audit.json` exactly (to `1e-15`) in all four modes, at 16, 32, 64 and 96 bits:

- D;
- D+M;
- D+M+H with exact closing;
- D+M+H with partial closing.

It also reproduces main's example, `3/4` at 4 bits. Main's exact rates `ρ = c^c/(2^c(c−1)^(c−1)) ≈ 0.946505` per odd step and `β = 2^H(1/c)/2 ≈ 0.965907` per bit, with `c = log2 3` and `H` the binary entropy, agree with the 19:48 closed form.

**CORRECTION to 19:46.** The D+M+H column there used exact closing. That is valid but conservative. The partial-closing rule certifies a selected run as soon as the bits show its closing valuation is `≥ 3`; this is main's fix. Under it, the uncertified fractions are:

| bits | 16 | 32 | 64 | 96 |
|---|---:|---:|---:|---:|
| uncertified | 14.8% | 4.08% | 0.598% | 0.120% |

The rate is unchanged.

**CORRECTION to 19:59.** The claim that all merge-type certificates share one `c/H²` law was wrong as stated, for two reasons:

- `c/H²` describes only the forward-orbit union `F_N`. Main's R27 fibres `I_N` are a larger certifiable set with density about `1/(2H)` at height `H·N`.
- R23 merges occur at unbounded relative height.

Revised statement (2-adic random model, not a proof):

- An orbit conditioned to stay above a level spends about `ℓ` steps near log-height `ℓ`. With target density `2^(−ℓ)`, the expected number of hits, `Σ ℓ·2^(−ℓ)`, is finite. Density `1/(2H)` therefore still leaves the rate unchanged in the model.
- In the model, a rate change needs certifiable targets whose density at height `H·N` decays more slowly than every power of `H`.

Main's R28 already scopes this: no obstruction to arbitrary bridges follows.

`python3 sidekick/probes/coalescence_check.py`. The receipt now carries all four modes.

---

## 2026-10-17 20:01 — FINDING: no sign bias among high-climbing annular sources

For every source `x` of `A_N`, take its peak orbit height relative to `x`. Then split the source mass by that climb ratio.

| `N` | climb `≥ 1` (all) | `≥ 4` | `≥ 16` | `≥ 64` | `≥ 128` |
|---|---|---|---|---|---|
| 6144 | +152064 / −152064 | +30453 / −30479 | +7730 / −7725 | +1891 / −1896 | +955 / −931 |
| 9216 | +228096 / −228096 | +45758 / −45806 | +11738 / −11712 | +2908 / −2791 | +1491 / −1402 |

Each cell is positive mass / negative mass. At every threshold the two balance to within fluctuations. This is consistent with CRT: the band table's residues mod 9 are independent of the binary digits that drive climbing.

High excursions therefore carry about as much positive mass as negative. Cancelling them would require positive and negative climbers to merge while high, which happens rarely there (19:49 entry). Finite data, no proof.

---

## 2026-10-17 19:59 — VERIFIED R24 arithmetic; FINDING: merge-type certificates all share one density law at large height  [density claim corrected at 20:22]

**VERIFIED (main `8e2b5eb`, R24).** The ordered cutoffs `a·2^b` (`b ≥ 9`) have consecutive ratios exactly in `{7/6, 8/7, 9/8}`, checked over 355 cutoffs. So `3N/2` always reaches the next cutoff, and every cutoff is divisible by 512. The base holds: every odd seed `≤ 6144` reaches 1. (`python3 sidekick/probes/r24_check.py`)

**ACK.** Main's review (`side_lane_review_20261017_latest.md`) gives a written proof of the 19:40 support identity for every allowed `N`. It also correctly notes that the one-step merger count does not by itself rule out other mechanisms. The following addresses that.

**FINDING** (2-adic random model plus the 19:49 data; not a proof).

Every finite current certifies positive mass by one of two routes: orbits meeting (R7's component masses), or absorption at 1. In the R20/R24 setting, every available partner orbit starts at height `≤ C·N`. This covers:

- absorbed seeds and their paths;
- F-chain siblings `4^k·u + (4^k−1)/3`;
- halving partners;
- annular blocks, whose sources lie below `9N/4`;
- negative annular atoms, absorbed or not.

The union of orbits started below `C·N` has density about `c/H²` among odd numbers at height `H·N`. The 19:49 entry measured `c ≈ 0.3` for `C = 1`. The reason is that an orbit reaches height `H×start` with probability about `1/H`, which is the root `κ = 1` of `3^κ = 2^(1+κ) − 1`.

A root climbing through heights `H = 2^k` therefore meets such a partner with total probability about `Σ_k c·4^(−k)`, which is bounded. Consequently, no catalogue of merge-type certificates, finite or infinite, changes the large-deviation rate of the 19:48 entry; catalogues change constants. A rule closing every complementary root at every `N` would then need a certification step whose chance at height `H·N` does not decay in `H`. Equivalently, it needs a non-merge argument that the orbit comes down.

---

## 2026-10-17 19:50 — SYNTHESIS: a map of the R20 outer-descent frontier (findings 19:34–19:49)

All statements below are finite data or exact arithmetic recorded in the entries cited. No termination claim is made.

1. **What the target is.** The support of `R_N` is the set of shell climbers in `(N, 3N/2)` that are not reached from `[1, N]` within two steps (19:40). About half are multiples of 3, which have no predecessors. Discharging R20 is therefore the strong-induction step for these roots.
2. **What local certificates achieve.** Exact 2-adic counts (19:37, 19:42, 19:46) cover descent below `N`, merger with `S([1,N])`, and halving coalescence anywhere below `2N`. At 64 bits they leave 1.06%, 0.84% and 0.61% of roots uncertified, respectively.
3. **What sets the remaining rate (19:48).** Each of these certificates fires only within a fixed multiple of `N`. Their uncertified set always contains the orbits that stay above that level. Its decay is the level-independent large-deviation rate `ρ ≈ 0.9466` per odd step, about `0.966` per bit, so the core is about `N^0.95` at scale `N`.
4. **What happens while orbits are high (19:49).** Absorbed-seed excursions have density about `0.3/H²` at height `H·N`. Meeting them while high changes constants only. The slowest roots meet `F_N` only after they come back down.
5. **What sets whole-annulus depth (19:34).** The last positive component is a fixed absolute slow cluster, `270271, 360361, …` with stopping times of about 150. Four rays share it at `64N`, so depth is not inherited from scale `N`.

In this picture, a mechanism that changes item 3 would have to act on orbits while they are arbitrarily high relative to `N`. Equivalently, it would have to bound how long an orbit can stay above a given multiple of its start.

---

## 2026-10-17 19:49 — FINDING (Q6): merging with absorbed-seed excursions is rare while high

`F_N` is the union of the Syracuse orbits of all odd seeds `≤ N`. The sample is `N = 49152`, where `F_N` has 38,912 states and its largest state is about `821N`.

**Density.** Among odd numbers in the band `[HN, 2HN)`, the density of `F_N` is about `0.3/H²` for `H ≤ 2^6`. It falls to about `0.16/H²` at `H = 2^8`, and is zero above `H ≈ 2^9`.

**Merge versus descent.** For the 3,925 roots of `R_N`:

| | first descent below `N` | first meeting with `F_N` |
|---|---:|---:|
| median steps | 4 | 3 |
| 99th percentile | 36 | 28 |
| maximum | 96 | 96 |

30% of roots meet `F_N` strictly before they descend. The slowest root, `60975`, meets it only on its descent at step 96, at height `0.35N`.

**Reading.** The meeting chance decays like `1/H²`, so its sum over a high excursion is bounded. This channel shifts constants, like the certificates in the 19:48 entry, and does not change the core rate. Finite data, no proof.

`python3 sidekick/probes/excursion_merge_probe.py` (seconds; receipt alongside)

---

## 2026-10-17 19:48 — FINDING: why local certificates cannot change the core's decay rate

Fix the threshold at `N` and start roots higher, in `(KN, 3KN/2)`. The exact dynamic program gives these per-bit rates from 96 to 128 bits:

| K | 1 | 4 | 16 | 64 |
|---|---:|---:|---:|---:|
| rate | 0.9546 | 0.9565 | 0.9573 | 0.9581 |

Only the constants change appreciably with `K`.

The common limit is a large-deviation constant. The log-height walk takes steps `log2(3) − a` per odd step, with `a ~ Geom(1/2)`. The probability that it stays above any fixed level for `n` odd steps decays like `ρ^n`, where

```
ρ = min_θ 3^θ / (2^(1+θ) − 1) ≈ 0.9466,   attained at 2^(1+θ) = ln 3 / ln(3/2).
```

The optimal tilt has mean valuation `log2 3`. Per bit this gives `ρ^(1/log2 3) ≈ 0.966`, so the core is about `N^0.95` at scale `N`. The finite-depth rates above (0.951 to 0.958) are still converging toward it.

**Consequence.** The uncertified set always contains the paths that stay above `C·N` for the whole bit budget. Descent, `S([1,N])`-merger, and halving coalescence below `2N` (19:42, 19:46) all fire only within a fixed multiple of `N`. Each of them, and any finite combination of such certificates, therefore has the same asymptotic rate and changes only the constant.

A certificate can change the rate only if it fires while the orbit is still arbitrarily high relative to `N`. One example would be merging with excursions of already-absorbed seeds at large heights. Exact rational arithmetic and a standard Cramér estimate; no termination claim.

---

## 2026-10-17 19:46 — VERIFIED + FINDING: halving coalescence  [D+M+H numbers corrected at 20:22] (main `8e2b5eb`, `residual_return/SHRINKING_COALESCENCE.md`)

**Verified.**

- **Identity.** `S^a(x) = S^a((x−1)/2)` holds for every selected `x < 2^21`, which is 262,144 cases. Selected means `x = 2^a·t − 1` with `t ≡ 3^a (mod 4)`. It also holds for 2,000 random selected 200-bit `x`.
- **Coverage.** At `N = 96, 768, 6144, 49152, 98304`, explicit enumeration of `R_N` and its selected part gives a remaining mass within main's stated `6A` of `25N/576`. The ratio is `1.009` at `N = 6144` and `1.0005` at `N = 98304`.

**Finding: effect on the 2-adic core of R20.**

Selection has a simple valuation form: a climber is selected exactly when the valuation right after its run of 1s is `≥ 3`.

Coalescence can therefore be applied at any orbit state, not only the root. A selected climber `y ≤ 2N` has its partner `(y−1)/2 ≤ N` already absorbed.

An exact dynamic program for roots in `(N, 3N/2)` allows three certificates at every state: D (descent below `N`), M (merger with `S([1,N])`), and H (halving coalescence).

| bits `m` | 16 | 32 | 64 | 96 |
|---|---:|---:|---:|---:|
| uncertified, D | 24.8% | 7.04% | 1.06% | 0.214% |
| uncertified, D+M | 21.2% | 5.76% | 0.843% | 0.168% |
| uncertified, D+M+H | 15.6% | 4.18% | 0.611% | 0.122% |

From 64 to 96 bits the decay rate per bit is `0.9514` for D, `0.9509` for D+M, and `0.9508` for D+M+H.

Adding H cuts the uncertified fraction by about a further 28% at every depth, but leaves the asymptotic rate unchanged. These three local certificates shift constants on one exponential core. Exact rational arithmetic; no termination claim.

`python3 sidekick/probes/coalescence_check.py` (about 2 s; receipt alongside)

---

## 2026-10-17 19:44 — VERIFIED: the fixed-h depth theorem (main `8e2b5eb`, `phase_depth/FIXED_H_DEPTH.md`)

The theorem was rebuilt with this branch's own code.

**Barrier lemma, finite data.**

- The union of Syracuse orbits of odd `1…33` is exactly the stated 54-element set.
- Enumerating `u0 = 2^s·3^r` with `9u0 < z0 < 10u0` reproduces exactly the 22-row `(z0, u0, c0)` table.
- Every `c0 > 1` lies in a basin of the `3x−1` map (`d = −1` in `affine_controls.py`) whose cycle avoids 1. The cycles are `{5, 7}` and `{17, 25, 37, 55, 41, 61, 91}`.

**Theorem, by full brute force.** At the least admissible `X` for `D = 1, 2, 3, 4`, the whole depth-`D` component of `144N−1` is exactly the chain `y1…y_{D+3}`. Its sources are `(−2, +2, +2)`, and `h = v3(X−1) = 2`. The cutoffs are `N = 528, 528, 2472, 8304`.

**Ladder.** For every `D ≤ 12`, `2^e ≡ 10 (mod 3^(D+2))` has solutions with `6 | e`, so they lie on `N = 96·64^k`.

**Observation.** The protecting mechanism is the dynamics of `3x−1`: the auxiliary values `c` evolve under `T−`. The obstruction lasts as long as those values sit in the `3x−1` cycles. That is the negative-integer control of PR1, appearing inside the positive-integer obstruction itself.

`python3 sidekick/probes/fixed_h_check.py` (about 5 s; receipt alongside)

---

## 2026-10-17 19:42 — FINDING: allowing merger with absorbed seeds changes the cylinder count only by a constant factor

This addresses the "testable intermediate task" in main's in-progress `SUFFICIENT_SETS_AUDIT.md` §4: certify R20 exits or roots by exact valuation cylinders, allowing either descent or merger.

The 19:37 dynamic program is extended. A root in `(N, 3N/2)` now also counts as certified once its orbit reaches a state `y ≤ 3N/2` through an odd valuation `≥ 3`. Such a `y` is `≡ 2 (mod 3)`, and its valuation-1 predecessor `(2y−1)/3 ≤ N` is an absorbed seed off the orbit; this is merger with `S([1,N])`.

| bits `m` | 16 | 32 | 64 | 96 | 128 |
|---|---:|---:|---:|---:|---:|
| uncertified, descent only | 24.8% | 7.04% | 1.06% | 0.214% | 0.0484% |
| uncertified, descent or merger | 21.2% | 5.76% | 0.843% | 0.168% | 0.0381% |

The ratio settles near `0.79`. The decay rate per bit is unchanged: `0.9528` with merger against `0.9530` without, measured from 64 to 128 bits. One-step lookback therefore removes a constant fraction of the uncertified classes but leaves the same exponential core. Exact rational arithmetic.

`python3 sidekick/probes/residual_cylinder_core.py --merge`

---

## 2026-10-17 19:40 — FINDING: R17's outer residual is exactly the strong-induction residual with two-step lookback

Assume, as R20 does, that every odd seed `≤ N` reaches 1. Then the support of `R_N` (R17, `RETAINED_GRAPH_EXTENSION.md` §4) is **exactly** the following set: the odd climbers `x ≡ 3 (mod 4)` in the shell `(N, 3N/2)` that are not reached from `[1, N]` in one or two Syracuse steps.

```
supp R_N = { odd x in (N, 3N/2) : x ≡ 3 (mod 4), x ∉ S([1,N]) ∪ S²([1,N]) }
```

**Range checked.** The identity was checked exactly at `N = 96, 768, 6144, 9216, 49152, 98304`.

**Details.**

- `x ≡ 2 (mod 3)` climbers are excluded because they equal `S((2x−1)/3)`.
- The sliver `x ≡ 31 (mod 36)` in `(N, 9N/8)` is excluded because it equals `S²((8x−5)/9)`.
- `R_N`'s mass exceeds the support size only through its coefficient-2 roots.

**What follows.**

- R20's outer-descent obligation for `R_N` is the classical strong-induction step on this set.
- About half the support (for example 256 of 490 at `N = 6144`) is multiples of 3. These have no Syracuse predecessors, so no backward lookback of any depth can reach them. Only their own forward orbits can bring them into the absorbed set.
- Combined with the 19:37 entry, a fixed-bit residue rule leaves a positive fraction of them uncertified.

`python3 sidekick/probes/residual_vs_induction.py` (under 1 s; receipt alongside)

---

## 2026-10-17 19:37 — FINDING: how far 2-adic cylinders go toward R20's outer descent

R20 (main `46198fb`) asks for a noncircular rule that takes every outer residual root below `N` into the absorbed seeds. R17 defines those roots as `x ≡ 3, 7 (mod 12)` in the shell `(N, 3N/2)`.

**The rule tested.** It is Terras-style. The first `j` valuations of `x` are fixed by `x mod 2^(A_j+1)`, where `A_j` is their sum. If some determined prefix has `3^j·(3/2) < 2^(A_j)`, then every root in that residue class drops below `N`, for all large `N`. This uses only 2-adic arithmetic and no orbit search. The classes mod 12 and mod 36 that define `R_N` are independent of those bits (CRT), so they do not change the counts.

**Exact uncertified fraction** of roots, as a function of the number of bits used. It is computed by dynamic program and cross-checked by brute-force enumeration for `m ≤ 14`.

| bits `m` | 16 | 24 | 32 | 48 | 64 | 96 | 128 |
|---|---:|---:|---:|---:|---:|---:|---:|
| uncertified | 24.8% | 12.8% | 7.0% | 2.5% | 1.06% | 0.21% | 0.048% |

Between 64 and 128 bits the decay is about `0.953` per bit.

**Consequences.**

- Any rule that uses a fixed number of bits, independent of `N`, leaves a positive fraction of `R_N` uncertified. That fraction is linear in `N`.
- If the bits grow like `log2 N`, about `N^0.93` roots remain at scale `N`, and the rule becomes per-root.

**Actual roots**, as a check against the class prediction:

- `N = 6144`: 490 roots; median descent 4 steps; slowest 48 steps.
- `N = 98304`: 7850 roots; median descent 4 steps; slowest 81 steps (for example `140479`).

This is finite exact arithmetic with no termination claim. The uncertified classes are exactly Terras's undecided stopping-time cylinders, restricted to `R_N`.

`python3 sidekick/probes/residual_cylinder_core.py` (under 1 s; receipt alongside)

---

## 2026-10-17 19:34 — FINDING: whole-annulus exposure depth is set by absolute slow clusters, not by the ×64 self-similarity

`d*(N)` is the first exposure depth at which no component outside the component of 1 has positive source mass. The question was whether the obstruction at `64N` is a lifted copy of the one at `N`. If it were, an induction down the `×64` ladder could reach the verified base. Each of the five rays was compared one step apart.

| ray `a` | `N = 8a` | `d*(N)` | `64N` | `d*(64N)` |
|---:|---:|---:|---:|---:|
| 12 | 96 | 28 | 6144 | 64 |
| 14 | 112 | 32 | 7168 | 91 |
| 16 | 128 | 44 | 8192 | 90 |
| 18 | 144 | 29 | 9216 | 90 |
| 21 | 168 | 34 | 10752 | 90 |

At `64N` the last positive component for rays 14, 16, 18 and 21 contains the **same twelve absolute states**: `270271, 360361, 405407, 432923, 480481, 487039, 608111, 649385, 730559, 810815, 865847, 912167`. Note that `360361 = (4·270271 − 1)/3`; the cluster consists of related predecessors. These states have stopping times of about 150 odd steps. Every annulus whose window contains them stalls at about depth 90, whatever its ray.

For these samples, then, the end of the last plateau is fixed by a cluster of slow orbits in absolute terms. It is not inherited from the obstruction one scale down. A `×64` descent of obstructions would need a different correspondence than this one. Finite data, no proof.

`python3 sidekick/probes/slow_cluster_probe.py` (about 2 min; receipt alongside)

---

## 2026-10-17 19:22 — FINDING (Q3): zero-cost cancellation of the isolated chain is rare; three further depth-7 classes at h = 2

**Setting.** The setting is that of main's `DELAYED_RELEASE.md`:

- `v3(X−1) = h`, `2^max(h+5,10) | X`, `U = (X−1)/3^h`;
- chain block `y1 (−2)`, `y2 (+2)`, `y3 (+2)`.

**Method.** A bounded backward search from `{y1, y2, y3}`. It covers every inverse branch that a source below `144N` reaches within 16 forward steps, with any valuation word. It looks for negative annular sources with total coefficient `≤ −2`; such a set gives an everywhere nonpositive current for the block plus those sources.

**Calibration.** On main's two families (`U ≡ 70, 313 mod 729`), the search recovers exactly `v` at distance 5 and `u` at distance 7.

| h | admissible classes of `U` | cancel in every representative | depends on representative | none within depth 16 | depths seen |
|---:|---:|---:|---:|---:|---|
| 2 | 486 (mod 729), 4 reps each | 11 | 34 | 441 | 7–15 |
| 3 | 1458 (mod 2187), 2 reps each | 20 | 24 | 1414 | 9–13 |

**New depth-7 classes at `h = 2`.** These are in addition to main's 70 and 313.

- `U ≡ 124, 610`: two `−1` sources enter `y1`, with forward valuation words `(1,1,1,2,2,3)` and `(1,1,1,1,2,2,3)`.
- `U ≡ 691`: one `−2` source enters `y1` with word `(1,1,1,1,2,2,3)`, which suffices alone. There is also a `−1` source on `(1,1,1,1,1,4,3)`.

**Structure.** These words lie on the ladder above `y1` used in main's proof:

- inverse valuation 3 to `4X−3`;
- then `h` inverse valuation-2 steps to `w_h = 4^(h+1)U + 1`;
- then `l` inverse valuation-1 rungs `z_l = 2^l(w_h+1)/3^l − 1`.

Rung `l` is an integer exactly when `3^l | 4^(h+1)U + 2`. For example, at `U = 124` this is `7938 = 2·3^4·49`, so rungs exist up to `l = 4`, matching the sources found at `l = 3` and `l = 4`.

**Reading (finite, bounded).** For about 95–97% of classes, the chain's backward tree does not re-enter the annulus within 16 steps. In those classes, any cancellation of the `+2` has to happen further along the chain's forward orbit, at positive current cost. Absence within depth 16 is not absence at every depth.

`python3 sidekick/probes/chain_cancellation_scan.py` (about 1 s; receipt alongside)

---

## 2026-10-17 19:13 — VERIFIED: delayed-release cancellation and the sharpened isolation lemma (main `65093c4`, `DELAYED_RELEASE.md`)

Everything was rebuilt from the statement with this branch's own `A_N`.

- **Current identity.** For every qualifying `h ≤ 12`, both `V ∈ {47, 155}`, and three members of each progression (16 families in all), the following hold:
  - parameters (1)–(6);
  - coefficients `(u, t, v, y1, y2, y3) → (−1, 0, −1, −2, +2, +2)`;
  - arrows `u →(2) t →(1) v`;
  - valuation word `(1^r, 2^h, 3)` from `v` to `y1`;
  - `(I−P)J = μ`, with `J ≤ 0` and at most `2h+5` rows.
- **Ladder example.** The stated cutoff `N = 96·64^89` (`X = 2^546`) holds, with a 9-row current, by point evaluation.
- **Qualifying h.** The qualifying `h ≤ 64` match; no two consecutive values fail.
- **Sharpened isolation, by full brute force.** At depth `h+1`, the component of `144N−1` is exactly the three-source chain. Checked at `N = 96, 312, 1608, 5496, 11328, 6144`, including the ladder points 96 and 6144.
- **Observation.** At depth `h+2` the chain is still exactly isolated at 5 of the 6 cutoffs; the exception is `N = 5496`.

`python3 sidekick/probes/delayed_release_check.py` (receipt alongside)

## 2026-10-17 19:13 — FINDING: how much of the chain obstruction the delayed-release families cover

- **Consistency with the 19:03 finding.** The five cutoffs in the 19:03 finding are all outside the delayed-release families: `X = 13312, 68608, 234496, 483328, 2^18`. The two findings are consistent. Inside the families, the chain block cancels at zero cost. At those outside cutoffs, the full component stayed positive until it joined the component of 1.
- **Coverage.** Among `X` with `v3(X−1) = h`, let `U = (X−1)/3^h`. Then `U` takes `2·3^(r+3)` admissible classes modulo `3^(r+4)`. The two families (`V = 47, 155`) cover 2 of them, a fraction of `1/3^(r+3)`. For example, this is `1/243` when `h = r = 2`.
- **Open.** Other valuation words or source pairs may cancel the chain in the remaining classes; that has not been tested.

---

## 2026-10-17 19:05 — VERIFIED: the two release-packing families (main `65093c4`, `RELEASE_PACKING.md`)

Both families were rebuilt from their statements alone. They were checked against this branch's own `A_N`, without importing main's constructor.

- **Pair.** The family is `36N < q < 54N`, `q ≡ 31 (mod 54)`, `u = (4q−1)/3`. Checked: `S(u) = q` with valuation 2, `u ≡ 5 (mod 18)` in `(48N, 72N)`, and coefficients `+2` at `q`, `−2` at `u`.
- **Triple.** The family is `64N < q < 72N`, `q ≡ 31, 103 (mod 108)`. Checked: arrows `u → q → v` with valuations 2 and 1, and coefficients `−1, +2, −1`.
- **Exact floor counts.** `P(N)` and `T(N)` match direct enumeration. They grow by exactly 72 and 32 under `N → N+216`, and the removed mass satisfies `2P + 2T = 26N/27 + O(1)`.
- **No reuse.** No state is used twice, within either family or across the two.

Ranges:

- every multiple of 8 up to 1024, by full construction;
- the first two and last two members of each progression at 40 random cutoffs up to about `8·10^9`, by point evaluation.

Disjointness from the older catalogue was **not** checked here. Main's written disjointness argument was not re-derived.

`python3 sidekick/probes/release_families_check.py` (receipt alongside)

## 2026-10-17 19:03 — VERIFIED: unbounded exposure depth (main `2be37b7`)

`UNBOUNDED_EXPOSURE_DEPTH.md` was checked by brute force. The check builds the full forward exposure graph from every source of `A_N`, using a separate union-find rather than the inverse oracle.

Cutoffs checked:

- the least admissible `X` for each `D = 1, 2, 3, 4`, giving `N = 312, 1608, 5496, 11328`;
- the ray example `N = 6144`, `X = 2^18`.

Result in all five cases:

- the depth-`D` component of `144N−1` is exactly the chain `y_1 … y_{D+3}`;
- its sources are `(−2, +2, +2)`;
- it is not linked to 1.

These are finite checks; the theorem's quantifiers rest on its written proof.

`python3 sidekick/probes/depth_probe.py` (receipt `depth_probe.json`)

## 2026-10-17 19:03 — FINDING: the protected chains end by reaching 1, not by cancellation

Same cutoffs. Exposure continued until the chain's component either had nonpositive mass or contained 1.

| D | N | protection `v3(X−1)−2` | depth at which it stops being an obstruction | component mass then | linked to 1 |
|---:|---:|---:|---:|---:|---|
| 1 | 312 | 1 | 11 | −20 | yes |
| 2 | 1608 | 2 | 21 | +38 | yes |
| 3 | 5496 | 3 | 9 | +64 | yes |
| 4 | 11328 | 5 | 10 | +108 | yes |
| 1 | 6144 | 1 | 51 | +23 | yes |

In four of the five cases, the component was still net positive at the step it joined the component of 1. The end depth does not follow the 3-adic protection.

For this family, then, a progress argument in which negative mass joins and cancels the chain would not describe what actually happens. The plateau ends through absorption: some orbit in the merged component reaches 1. This is finite data with no proof.

`python3 sidekick/probes/depth_probe.py`

## 2026-10-17 19:03 — ACK: PR1 review accepted

`PR1_REVIEW.md` is correct, and the corrected wording stands.

- The minimality lemma gives a lower bound under its cycle hypothesis.
- Minimum-cost one-sided certificates are not unique.
- The `δ21−δ3` example is valid, and the `A_768` numbers match this lane's own receipts: `J0(5) = −55`, `‖J0⁺‖₁ = 53758`, 40,106 rows.
- The earlier "no alternative search" phrasing is withdrawn.

## TOOL — controls and checker (on main since PR1)

- **Certificate checker.** `python3 collatz_research_20261017/negative_controls/affine_controls.py --check CERT.json` rebuilds `Π_N` for any `3x+d` independently and validates the certificate `(J, ζ)`.
- **Failure cases.**
  - `(d, N) = (61, 213)`: locally Collatz-like, yet the criterion fails.
  - `(d, N) = (−1, 16)`.
  - The `T_61` increments `A'_N` at `N = 8…32` (`progress_measures_audit.py`).

  Any generic argument or checker should fail on these.

---

## Open questions this branch is probing

These are not claims.

- **Q1 — answered empirically for `N ≤ 49152`** (entry of 2026-10-18 10:58): the absorbed share at fixed depth is nearly independent of `N`. 99% of the positive mass is in 1's component by depth about 25, and only the last sources need depth of about `7.3·log₂N`.
- **Q1 (original) — absorption as a giant component.** Probes so far resolve plateaus by merging with the component of 1. By some depth `c·log N`, is all but a vanishing fraction of the positive mass of `A_N` inside the component of 1? If so, almost-all descent estimates, which apply to unions of residue classes over long intervals, might reduce the problem to an explicitly thin remainder.
- **Q3 — answered for `h = 2, 3` within depth 16** (entry of 19:22).
- **Q4 — positive-cost cancellation.** For the classes with no zero-cost cancellation, where along the chain's forward orbit does the cumulative negative arrival first reach 2? Is that point bounded in terms of `h`?
- **Q5 — forward descent of shell multiples of 3.** These are leaves with no predecessors. Is there any structure in the forward orbits of `x ≡ 3 (mod 12)` in `(N, 3N/2)` beyond 2-adic cylinders? For example, does their first odd successor `(3x+1)/2 ≡ 2 (mod 3)` fall into a class that the annular currents certify?
- **Q6 — answered for one sample** (entry of 19:49): meeting chance is about `0.3/H²`, so only constants change.
- **Q6 (original) — certificates at large relative height.** Merging with the excursions of seeds `≤ N` is the only local mechanism found here that can fire at heights `≫ N`. How dense is `∪_{s ≤ N} orbit(s)` at height `H·N`, and how often does a residual root's orbit meet it while high?
- **Q2 — answered for the `D ≤ 4` chains** (entry of 2026-10-18 10:25): the end depth is a relay bottleneck along the chain's own orbit. It sits where that orbit returns to the source support, so it equals the length of the excursion above `144N`.
- **Q2 (original) — what sets the end depth.** For the protected chains, compare the end depth with the length of the all-valuation-1 climb plus the stopping time of the climb's top.
