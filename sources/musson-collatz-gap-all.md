---
id: musson-collatz-gap-all
kind: source
title: "mmusson/collatz: the effective gap Collatz.gap_all (Lean 4)"
status: replayed
citation: >
  mmusson, collatz (Lean 4 development, Apache-2.0), GitHub repository mmusson/collatz,
  file papers-lean/irrationality-measure-log2-3/CycleLenPoly.lean, theorem Collatz.gap_all;
  replayed at commit e292ac0d44ef3f27f82cdc6d1325d48b883218a2 (2026-10-06).
url: https://github.com/mmusson/collatz
created: 2026-10-19
aliases: [EXT-1]
tags: [linear-forms, lean, external-library, cycles]
---

# mmusson/collatz: the effective gap Collatz.gap_all (Lean 4)

## Citation

The Lean 4 repository `github.com/mmusson/collatz` (Apache-2.0), under its own toolchain `leanprover/lean4:v4.34.0-rc2` and Mathlib `v4.34.0-rc2` (rev `85e3a25e`). The theorem used is `Collatz.gap_all` in `papers-lean/irrationality-measure-log2-3/CycleLenPoly.lean`. The author is identified in the legacy record only by the GitHub handle `mmusson`; no year or paper accompanies it (citation incomplete in the legacy record).

Lean statement, as printed by `#check` in the replay:

```
Collatz.gap_all : ∀ {k L : ℕ}, 0 < k → 3 ^ k < 2 ^ L → 2 ^ L ≤ 2 ^ 172 * k ^ 341 * (2 ^ L - 3 ^ k)
```

Per the source, the regime `k < 2^100` is handled by `gapBelow_big` (certified interval arithmetic along convergents of `log₂ 3`, `K1big ≈ 3.15·10^50`) and `k ≥ 2^100` by `linFormHyp_uncond` (a Padé family, `FewRunsUncond.signApprox_Vq`).

## What we use

In NOTATION.md notation, with `k ↦ m` (odd steps) and `L ↦ A` (total valuation):

```
0 < m  and  3^m < 2^A   ⟹   2^A ≤ 2^172 · m^341 · (2^A − 3^m)     (EXT-1)
```

It plays the role of an effective Baker-type lower bound for `δ = A − m·log₂3`. Its ℤ-cast is the hypothesis of the Lean lane's `OrdCycle.G2_of_gap` with `(c, μ) = (172, 341)` (legacy C006-d). Legacy results using it: C006 (composition `G2_of_gap_collatz`, `J > (m−1)/(175 + 342 log₂ m)`), S05, S06 (replacing the Matveev input of C011), S07, S11. With the period bound of [hercher-2023-cycle-length](hercher-2023-cycle-length.md) this gives `J > ≈ 1.07·10^7`; that composition spans two libraries on different toolchains and is not a single Lean theorem.

The same checkout also supplied, in an addendum replay, these declarations (statements in the receipt):
- `Collatz.NormBridge.cycle_one_move_christoffel`: a positive shortcut-map `T`-cycle with `r ≥ 2` odd steps whose valuation word is the Christoffel word `chr r L` or one move from it is trivial (the Christoffel case is legacy R71-a / C004-c, Knight's exclusion; see [knight-2026-high-cycles](knight-2026-high-cycles.md));
- `Collatz.NormAll.no_cycle_one_move_christoffel_all` (word level);
- `Collatz.cycle_min_le_chr`: Halbeisen–Hungerbühler 1997 Theorem 3 upper half, `m(2^L − 3^k) ≤ chr(L, k)` for every `T`-cycle minimum (see [halbeisen-1997-rational-cycles](halbeisen-1997-rational-cycles.md));
- `Collatz.few_runs_cycle_trivial_uncond`: a `T`-cycle with at most two odd runs is `1` or `2` (the Steiner / Simons / Simons–de Weger circuit count, a different statistic from the sorted-height count `J`).

## How it is checked

`replayed`. The Lean lane cloned the repository at HEAD `e292ac0d44ef3f27f82cdc6d1325d48b883218a2` on 2026-10-19, built `lake build +CycleLenPoly` (3478 jobs; one transient `OneCircuit` failure in the first run, clean on the incremental rerun; the Sieve29 certificate parts were not built), then `+NormBridge +ChristoffelMin` (3554 jobs). `#print axioms` reports only `propext`, `Classical.choice`, `Quot.sound` for `gap_all`, `gapBelow_big`, `linFormHyp_uncond`, `signApprox_Vq`, `min_le_poly_period`, `few_runs_cycle_trivial_uncond` and the addendum declarations; no `sorryAx`, `Lean.ofReduceBool` or `native_decide`. The repository's own `sorry`s (the Collatz statement and the declared `NormGoal` targets) lie outside these closures.

Scope: the kernel accepted the theorem from the pinned sources; the statement was read, but **the proofs were not reviewed line by line**, and nothing of theirs is copied into this repository. Receipt: [`lean/receipts/mmusson_gap_all.txt`](../lean/receipts/mmusson_gap_all.txt). The Lean lane's unit table row is EXT-1 in [`archive/lean-lane/STATE.md`](../archive/lean-lane/STATE.md) (legacy path `lean/STATE.md`).
