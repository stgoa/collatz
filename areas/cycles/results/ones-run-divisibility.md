---
id: ones-run-divisibility
kind: result
title: A run of r letters 1 forces 2^r | n + q at its start and 2·3^r | n + q at its end, so 2·3^r ≤ n_e + q
status: formal
claim: >
  Raw odd-only 3x+q map, q odd, any cycle (no primitivity or order needed). If a_(i₀+k) = 1 for 0 ≤ k < r,
  then 2^r·(n_(i₀+r) + q) = 3^r·(n_(i₀) + q), 2^r divides n_(i₀) + q, 2·3^r divides n_(i₀+r) + q, and hence
  2·3^r ≤ n_(i₀+r) + q, i.e. 1 + r·log₂3 ≤ log₂(n_e + q) at the run's end e = i₀ + r. The inequality is not
  strict in general (equality at the step 3 → 5 at q = 1).
authors:
  - Claude side lane (Opus)
created: 2026-10-19
lean:
  - LeanLane.Cyc.OddCycle.one_step_add_q
  - LeanLane.Cyc.OddCycle.ones_run_identity
  - LeanLane.Cyc.OddCycle.ones_run_dvd
  - LeanLane.Cyc.OddCycle.ones_run_le
evidence:
  - "../attempts/four-mismatch-size-method-limit/README.md, section 1, constraint (5): the written statement at q = 1 (legacy S08 note), as corrected"
reviewed_by:
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Feed update 13:17 (S8 review: constraint (5) checks out) and 15:06 (Lean unit S8-a verified, iteration 78), with the correction that the size form holds with ≤, not <"
    link: ../../../archive/side-lane/FEED.md
tags: [cycles, comparison-orbit, formal]
---

# A run of r letters 1 forces 2^r | n + q at its start and 2·3^r | n + q at its end, so 2·3^r ≤ n_e + q

## Statement

Let `n_0, …, n_(m−1)` be a cycle of the raw odd-only `3x+q` map with `q` odd, `3n_i + q = 2^(a_i)·n_(i+1)`. If `a_(i₀+k) = 1` for `0 ≤ k < r`, then

```
2^r·(n_(i₀+r) + q) = 3^r·(n_(i₀) + q),     2^r | n_(i₀) + q,     2·3^r | n_(i₀+r) + q,
2·3^r ≤ n_(i₀+r) + q,   i.e.   1 + r·log₂3 ≤ log₂(n_e + q)  at the run's end e = i₀ + r.
```

## Proof

On a letter `1`, `2n_(i+1) = 3n_i + q`, so `2(n_(i+1) + q) = 3(n_i + q)`: the shifted state `n + q` is multiplied by `3/2` (comparison with the fixed point `−q` of `x → (3x+q)/2`; at `q = 1`, the integer cycle `{−1}`, word `1^∞`). Iterating gives the identity; since `gcd(2, 3) = 1`, `2^r | n_(i₀) + q` and `3^r | n_(i₀+r) + q`, and `n_(i₀+r) + q` is even (odd states, odd `q`), so `2·3^r` divides it. Positivity gives the size form.

## Lean

`lean/CycleSpectrum.lean`, Lean unit S8-a (iteration 78); axioms `propext`, `Classical.choice`, `Quot.sound`. In `OddCycle`: `one_step_add_q` (`2(n_(i+1) + q) = 3(n_i + q)` on a letter 1), `ones_run_identity`, `ones_run_dvd` (odd `q`: `2^r ∣ n_(i₀) + q` and `2·3^r ∣ n_(i₀+r) + q`), `ones_run_le` (`2·3^r ≤ n_(i₀+r) + q`). The statement matches the claim exactly; the `log₂` form is a restatement.

## Remarks

- **Not strict.** S8's constraint (5) was first written with `<`. Equality holds exactly when `n_e + q = 2·3^r`, e.g. the one-step `3 → 5` at `q = 1` (`5 + 1 = 6 = 2·3`). For a maximal run of exactly `r` ones, `v₂(n_(i₀) + q) = r + 1`, so `n_e + q = 2·3^r·(odd)`, which still allows equality.
- **Use.** A run of ones starting at height `y` (in `log₂`) gains `0.585` per step, so by the size form it can last at most about `y − 1` steps (`1 + 1.585r < y + 0.585r`); in particular the run leaving the minimum of a `q = 1` cycle has length below `ℓ − 1`, `ℓ = log₂ L`. The same device works with any integer cycle of the `3x+q` map as comparison orbit, e.g. `{−5, −7}` and the `−17` cycle at `q = 1` (written, not formalised).
- **Controls.** The statement holds for every odd `q`, so actual `3x+q` cycles satisfy it.
- Elementary; novelty: none claimed.

## History

- Created by the B05 migration (Claude, Opus 5.5) from the legacy S08 note §1, constraint (5) (`experiments/cycle_spectrum/S08/FOUR_MISMATCH_MAP.md` at `be73a66`; the note's headline is withdrawn, this by-product remains valid), and the side lane's message of 14:55 asking for the general-odd-`q` form. Side lane (Claude, Opus); formalised by the Lean lane (Claude, Fable) as part of S8-a.
- **Correction (2026-10-19 15:06, the Lean lane's).** The size form is `≤`, not `<`, as stated above. The S8 probes test the stricter `<`, so their margins remain valid.
- **Correction (2026-10-19 13:13).** The bound on the run leaving the minimum first read "at most about `0.63ℓ`", which ignored the run's own gain; corrected to "below `ℓ − 1`".
