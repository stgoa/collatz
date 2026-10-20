---
id: denjoy-koksma-height-bound
kind: result
title: "A Denjoy–Koksma height bound: B ≤ (K(h/m) − 1)·(V_h + 2δ) for every rotation coprime to the period"
status: formal
claim: >
  Odd-only 3x+q map, any odd q, any positive odd cycle n_0, …, n_(m−1) with letters ≥ 1 (no primitivity,
  gap, period or L/q hypothesis). For every rotation 0 < h < m with gcd(h, m) = 1, let μ_h(p) =
  log₂n_(p+h) − log₂n_p, Var(μ_h) its cyclic total variation, K = K(h/m) the sum of the partial quotients
  of h/m, V_h = Σ_t |a_t − a_(t+h)| the total letter variation at the mismatches of h, and δ = A − m·log₂3.
  Then for all positions x, y, |log₂n_y − log₂n_x| ≤ (K − 1)·Var(μ_h) ≤ (K − 1)·(V_h + 2δ); in particular
  the log-height B = log₂(H/L) is at most (K − 1)·(V_h + 2δ). It is informative only when some coprime
  rotation has small letter variation and tame partial quotients; for tall sawtooth cycles, whose drop sits
  at a mismatch, it is silent.
authors:
  - Claude side lane (Opus)
created: 2026-10-19
lean:
  - LeanLane.Cyc.DK.dk_core
  - LeanLane.Cyc.DK.dk_discrete
  - LeanLane.Cyc.OddCycle.dk_log
  - LeanLane.Cyc.OddCycle.varMu
  - LeanLane.Cyc.OddCycle.varMu_neg
  - LeanLane.Cyc.OddCycle.dk_log_either
  - LeanLane.Cyc.OddCycle.dk_log_iter
  - LeanLane.Cyc.OddCycle.dk_walk
  - LeanLane.Cyc.DK.Ladder
  - LeanLane.Cyc.DK.ostrowski_greedy
  - LeanLane.Cyc.DK.exists_chain_index
  - LeanLane.Cyc.OddCycle.varMu_nonneg
  - LeanLane.Cyc.OddCycle.height_le_varMu
  - LeanLane.Cyc.OddCycle.height_le_varMu'
  - LeanLane.Cyc.OddCycle.eps
  - LeanLane.Cyc.OddCycle.log_step
  - LeanLane.Cyc.OddCycle.sum_eps
  - LeanLane.Cyc.OddCycle.varMu_le
  - LeanLane.Cyc.OddCycle.Vh
  - LeanLane.Cyc.OddCycle.varMu_le_Vh
  - LeanLane.Cyc.DK.EuclidData
  - LeanLane.Cyc.DK.convQ
  - LeanLane.Cyc.DK.conv_det
  - LeanLane.Cyc.DK.conv_coprime
  - LeanLane.Cyc.DK.conv_adm
  - LeanLane.Cyc.DK.rem
  - LeanLane.Cyc.DK.quot
  - LeanLane.Cyc.DK.termIndex
  - LeanLane.Cyc.DK.convQ_termIndex
  - LeanLane.Cyc.DK.ladder_of_coprime
  - LeanLane.Cyc.DK.cfK
  - LeanLane.Cyc.OddCycle.height_le_varMu_coprime
  - LeanLane.Cyc.OddCycle.height_le_varMu_coprime'
  - LeanLane.Cyc.OddCycle.height_le_coprime
certificates: [check_legacy_replay.py]
evidence:
  - "s12_denjoy_koksma.py, s12_denjoy_koksma.json: side-lane probe (about 23 s): on every actual 3x+q cycle with odd q < 2,000 and every rotation coprime to m, checks (1) at every convergent denominator and start (12,229,083 instances), and (2), (3) on 52,484 pairs; no violation. Fails at its new path: it imports s1a_integer_cycle_check from its own folder (now in ../ordered-gap-closed-form/); with that folder on PYTHONPATH it exits 0 and leaves its receipt byte-identical (checked at migration). Passed at be73a66 as reviews/side_lane/s12_denjoy_koksma.py (archive/legacy-checker-run-be73a66.md). Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
reviewed_by:
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Feed S12 entry, update 15:23: adversarial review of step (1); it holds exactly in the discrete setting under gcd(p, q) = 1, 1 ≤ q < m and the strict |qh − pm| < m/q, which every proper convergent satisfies; Ostrowski digits give the sharper K − 1. Formalised as S12-a to S12-f (iterations 80-90)"
    link: ../../../../archive/side-lane/FEED.md
aliases: [S12]
tags: [cycles, height, denjoy-koksma, continued-fractions, formal]
---

# A Denjoy–Koksma height bound: B ≤ (K(h/m) − 1)·(V_h + 2δ) for every rotation coprime to the period

## Statement

Take any positive odd cycle of the odd-only `3x+q` map (odd `q`, letters `≥ 1`) with log-profile `y_p = log₂ n_p` (indices mod `m`), and a rotation `0 < h < m` with `gcd(h, m) = 1`. Put `μ_h(p) = y_(p+h) − y_p`, `Var(μ_h)` its cyclic total variation on `Z/m`, `K = K(h/m)` the sum of the partial quotients of `h/m`, `V_h = Σ_(e ∈ mis h) |a_e − a_(e+h)|` and `δ = A − m·log₂3` (bits). Then for all positions `x, y`

```
|y_y − y_x| ≤ (K − 1)·Var(μ_h) ≤ (K − 1)·(V_h + 2δ),
```

so the log-height `B = max y − min y` satisfies `B ≤ (K − 1)·(V_h + 2δ)`. No gap, no period import, no hypothesis on `L/q`, and no primitivity are needed.

## Proof

Legacy note `DENJOY_KOKSMA.md` (S12, side lane), §§1–2, lightly edited. Its status line read: "A rigorous inequality: classical Denjoy–Koksma and Ostrowski, applied to the cycle profile, plus exhaustive data. Its consequence for the mismatch problem is conditional. Novelty undetermined: the tools are classical, and this lane has not seen them applied to Collatz cycle profiles."

### 1. The identity

- `μ_h` has mean exactly 0 over `Z/m`, since `Σ_p μ_h(p) = 0`.
- Along the chain `x, x + h, x + 2h, …`, which visits every position because `gcd(h, m) = 1`, the profile is a **Birkhoff sum** of the rotation by `h`:

  ```
  y(x + Nh) − y(x) = Σ_(k<N) μ_h(x + kh).
  ```

### 2. The bounds

- **(1) Denjoy–Koksma.** Let `p/q` be a convergent of `h/m` with `q < m`, so `|qh − pm| < m/q`. For every start `x`,

  ```
  |Σ_(k<q) μ_h(x + kh)| ≤ Var(μ_h).
  ```

  The classical proof applies verbatim: the `q` points `x + kh` fall one in each of `q` consecutive arcs, and each term deviates from its arc's average by at most that arc's variation.
- **(2) Ostrowski.** Every `N < m` is `Σ b_i q_i` with `0 ≤ b_i ≤ a_(i+1)`. With (1) and mean 0, `B ≤ Var(μ_h)·K(h/m)`.
- **Review note (the Lean lane, 2026-10-19).** (1) holds exactly in the discrete setting, under `gcd(p, q) = 1`, `1 ≤ q < m` and the strict `|qh − pm| < m/q`. Every proper convergent satisfies it. In (2), the Ostrowski digits satisfy `b_0 ≤ a_1 − 1`, so `Σ b_i ≤ K − 1` and the bound sharpens to `Var·(K − 1)`, the form in the Statement.
- **(3) Variation from the letters.**

  ```
  μ_h(p+1) − μ_h(p) = (a_p − a_(p+h)) + (ε_(p+h) − ε_p),     with ε_p = log₂(1 + q/(3n_p)).
  ```

  Hence `Var(μ_h) ≤ V_h + 2δ`, since `Σ_p ε_p = δ`. Only the mismatches of `h` contribute, apart from the drift. At `q = 1`, `δ ≤ m/(3L ln 2)`, which is below `3·10^(−11)` at `m = 1.375·10^11` with `L > 2^71`.

## Certificates

None run by CI; `s12_denjoy_koksma.py` is a probe (see `evidence`). The test set is every actual `3x+q` cycle with odd `q < 2,000` and every rotation coprime to `m`.

| check | instances | violations | largest ratio |
|---|---|---|---|
| (1), every convergent denominator and start | 12,229,083 | 0 | `|S_q|/Var` = 0.42 |
| (2) | 52,484 pairs | 0 | `B/(Var·K)` = 0.12 |
| (3) | 52,484 pairs | 0 | — |

The side lane's independent checks at formalisation time (feed 15:39–16:54) add: the Denjoy–Koksma core on 278,384 random mean-zero periodic functions (`m ≤ 60`, every admissible `(p, q)`, every `x`), the greedy digit bound on 3,620,245 cases, `B ≤ (K − 1)·Var` on the 52,484 actual-cycle pairs (largest ratio 0.165), and the Euclidean invariants on 48,517 coprime pairs `h < m < 400`; none failed. Those scripts were not committed.

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B18-replay-revival migration; standard library) replays the unmodified legacy check `s12_denjoy_koksma.py` in a temporary copy of the legacy layout built by `tools/legacy_replay.py`, requiring exit 0 and every file unchanged (about 40 s). It checks finite steps only; the status is unchanged.

## Lean

`lean/CycleSpectrum.lean`, Lean units S12-a to S12-f (iterations 80–90; axioms `propext`, `Classical.choice`, `Quot.sound`, some helpers on subsets; receipts `lean/receipts/CycleSpectrum.*`), namespaces `LeanLane.Cyc.DK` and `LeanLane.Cyc.OddCycle`. Natural logarithms throughout, `δ_nat = A·log 2 − m·log 3`.

- **S12-a, (1).** `DK.dk_discrete` (`dk_core` for `x = 0`): for `f` `m`-periodic with `Σ_(t<m) f t = 0`, `q·h = p·m + r`, `q·r < m`, `gcd(p, q) = 1`, every `x`: `|Σ_(k<q) f(x + kh)| ≤ Σ_(t<m) |f(t+1) − f t|`. `OddCycle.dk_log`: the cycle form `|log n_(x+qh) − log n_x| ≤ Var(μ_h)`.
- **S12-b, the ladder walk.** `varMu`, `varMu_neg` (`Var(μ_(m−h)) = Var(μ_h)`), `dk_log_either` (either sign of `qh − pm`), `dk_log_iter`, `dk_walk`; `DK.Ladder`, `DK.ostrowski_greedy` (every `N < q_n` has digits with `Σ b_i + 1 ≤ K`).
- **S12-c, (2).** `DK.exists_chain_index`, `varMu_nonneg`, `height_le_varMu` (all `x, y`, given a ladder of admissible denominators ending at `m`), `height_le_varMu'` (relative to `n_0`).
- **S12-d, (3).** `eps`, `log_step`, `sum_eps` (`Σ ε_t = δ_nat`), `varMu_le`, `Vh`, **`varMu_le_Vh`** (`Var(μ_h) ≤ V_h·log 2 + 2δ_nat`).
- **S12-f, the ladder supply.** Part 1: `EuclidData`, `convQ`/`convP`, `conv_det`, `conv_coprime`, `conv_approx`, `conv_identity`, `conv_adm` (admissibility). Part 2: `rem`, `quot`, `termIndex`, `euclidData_rem`, `rem_termIndex`, `convQ_termIndex` (`q_n = m`), **`ladder_of_coprime`**. Part 3: **`cfK`** (the sum of the partial quotients), **`height_le_varMu_coprime`**, **`height_le_varMu_coprime'`**, **`height_le_coprime`** (`log n_y − log n_0 ≤ (K − 1)(V_h·log 2 + 2δ_nat)`). (S12-e, the denominator law, is [`denjoy-koksma-denominator-law`](../denjoy-koksma-denominator-law/README.md).)

**Statement match.** `height_le_varMu_coprime` and `height_le_coprime`, divided by `log 2`, are the Statement for `0 < h < m` with `gcd(h, m) = 1`; `K = DK.cfK m h`. The continued-fraction ladder is built formally from a Euclidean algorithm in `ℕ` (Mathlib's continued fractions were assessed as too heavy), so the tool has no non-formal input. The Lean statements need letters `≥ 1` and positive states; primitivity is not used.

## Remarks

The rest of the legacy note (§§3, 4, 5), lightly edited.

### 3. Consequence with S5 (conditional on EXT-1; not part of the claim)

At `q = 1`, S5 ([`mismatch-height-tradeoff`](../mismatch-height-tradeoff/README.md), conditional on [`musson-collatz-gap-all`](../../../../sources/musson-collatz-gap-all.md)) gives `s(h) > log₂3·m/(B + 342·log₂ m + 173)`. Combine it with (2) and (3), writing `a_M(h) = max_(e ∈ mis h) |a_e − a_(e+h)|` so that `V_h ≤ s·a_M`:

```
s(h)·(s(h)·a_M(h)·K(h/m) + 342·log₂ m + 173) > log₂3·m,    i.e.  s(h) ≳ √(log₂3·m/(a_M·K)).
```

The smallest `s` allowed, computed exactly (feed 15:17; not re-run at migration):

| `m` | `a_M = 1, K = 10` | `a_M = 2, K = 50` | `a_M = 3, K = 200` | `a_M = 10, K = 1000` |
|---|---|---|---|---|
| `10^7` | 917 | 360 | 156 | 40 |
| `1.375·10^11` | 146,986 | 46,620 | 19,048 | 4,668 |

**Reading.** A rotation with few mismatches forces at least one of two things: **(a)** a large letter difference at some mismatch, the tall-sawtooth structure of S7 ([`three-mismatch-exclusion`](../three-mismatch-exclusion/README.md)), where the huge drop sits at the aligned pair and `V_h ≈ 2V ≈ 2B`; or **(b)** `h/m` close to a rational with a small denominator, i.e. large `K`. Otherwise the height is small and S5 forces many mismatches.

**`h = 1` is vacuous** (the Lean lane's scope remark, ACK at 17:32). Here `K(1/m) = m` and `V_1 ≥ s ≥ 2` for any nonconstant cyclic word, so the right side of the denominator law ([`denjoy-koksma-denominator-law`](../denjoy-koksma-denominator-law/README.md)) carries at least `(m − 1)·s·log 2`, which exceeds its left side `log 2 + ((m − 1)/s)·log 3` for every `s ≥ 2`. Each mismatch contributes at least 1 to `V_h`, so the law can exclude a word only if `(K − 1)·s² ≲ (m − 1)·log₂3`, which needs both a small `K(h/m)` and a small `V_h`. The rise lemma ([`rise-lemma`](../rise-lemma/README.md)) covers short rotations, including `h = 1`, with no condition on `K`.

### 4. What it does not give

- **No unconditional height bound.** When a big letter sits at a mismatch, `Var(μ_h)` is about the height itself, and (2) is trivial. This is consistent with tall cycles.
- **Why a tall sawtooth survives (2).** The big drop at `x` makes `μ_h` jump on the arc `(x − h, x]`, an interval of length exactly `h`. That is a bounded-remainder set for the rotation by `h`, so its contribution to the Birkhoff sums is `O(jump)`, not `O(jump·K)`. A sharper version of (2) would split `μ_h` into bounded-remainder bumps (cost `O(jump)`) and the rest (cost `Var·K`). The side lane did not develop it.
- **`gcd(h, m) = g > 1`.** The chain covers one residue class. The bound applies within classes (rotation by `h/g` on `Z/(m/g)`), but the offsets between classes add a term of up to about `0.585g` plus the excess of a `g`-window. For large `g` this is weak.

### 5. The denominator form

The legacy §3a (a denominator law for any mismatch count) is [`denjoy-koksma-denominator-law`](../denjoy-koksma-denominator-law/README.md). The height frontier this tool addresses is [`cycle-height-bound`](../../questions/cycle-height-bound.md).

## History

- Migrated from `experiments/cycle_spectrum/S12/DENJOY_KOKSMA.md` (legacy ID `S12`; side-lane producer batch S12, 2026-10-19) at commit `be73a66`, by the B06 migration (Claude, Opus 5.5). §3a became [`denjoy-koksma-denominator-law`](../denjoy-koksma-denominator-law/README.md). The probe `reviews/side_lane/s12_denjoy_koksma.{py,json}` moved here. The note's §5 ("a first formalizable statement") is superseded by the Lean section; its "Reproduce" block pointed to the old paths.
- Side lane (Claude, Opus), feed 2026-10-19 15:17 (LEAD, S12). Update 15:23: the Lean lane's adversarial review of step (1) (exact discrete hypothesis, strict inequality; the Ostrowski sharpening `K − 1`, checked by the side lane).
- Formalised by the Lean lane (Claude, Fable): S12-a at 15:39 (`faad44f`), S12-b at 15:50 (`2a5b487`), S12-c at 15:54 (`2e22979`), S12-d at 16:02 (`4053e74`), S12-f parts 1–3 at 16:35–16:54 (`d74f9e1`, `2d49806`, `03b2807`); milestone entry 16:54 ("formal, with no external input"). Each unit was refereed by the side lane from receipts.
- **Scope remark (17:32).** The `h = 1` vacuity was not stated in the note before; added in Remarks.
