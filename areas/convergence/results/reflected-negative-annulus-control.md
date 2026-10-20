---
id: reflected-negative-annulus-control
kind: result
title: A reflected annulus on the negative integers has zero work and zero band masses yet admits no current
status: written
claim: >
  Negative integers, deliberately outside the positive Collatz domain: the odd Syracuse formula on negative odd
  integers, with positive 1 the only absorber. The reflected annulus Ã_96(−y) = A_96(y), y > 0, has
  H_L(Ã_96) = 0 for every L ≥ 0 and vanishing projections modulo 2, 4, 8, 6, 12, 24, but its 3204 source atoms
  follow checked finite paths (at most 86 steps) into the three negative cycles with signed component masses
  −20 (cycle −1), −73 (cycle −5 → −7) and +93 (the seven-state cycle through −17), verified by a stored
  5868-row current: Ã_96 = (I − P)J − 20δ_(−1) − 73δ_(−5) + 93δ_(−17). Hence no finite exact current and no
  finite current with everywhere nonpositive residual exists for Ã_96. This refutes the inference "balanced
  bands and bounded scalar work imply a current"; it is not a counterexample for the positive annulus or the
  five-ray theorem.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [disjoint-annular-recursion, orbit-component-current-criterion, binary-residue-projection-information-loss]
evidence:
  - "../exposure-potential-boundary-flux/check_duality.py (a certificate of that node): checks the reflected source classification (1000-step cap, cycle detection) and the stored current and residual against its receipt"
  - "../exposure-potential-boundary-flux/reflected_annulus_96_current.csv, reflected_annulus_96_residual.csv: the stored 5868-row current and three-atom residual"
aliases: [R10-c]
tags: [convergence, packet-currents, annular, negative-integers, control, counterexample]
---

# A reflected annulus on the negative integers has zero work and zero band masses yet admits no current

## Statement

This counterexample is deliberately outside the positive-integer Collatz domain. It tests the logic of methods based only on band balance, scalar work, or the coarse finite projections of [`binary-residue-projection-information-loss`](binary-residue-projection-information-loss.md).

Reflect the positive annulus `A_96` of [`disjoint-annular-recursion`](disjoint-annular-recursion/README.md) onto negative states, `Ã_96(−y) = A_96(y)` for `y > 0`. Use the same exact odd Syracuse formula on negative odd integers; positive 1 remains the only absorber.

**Proposition.** `H_L(Ã_96) = 0` for every `L ≥ 0`, and the projections modulo `2, 4, 8, 6, 12, 24` vanish. Nevertheless all 3204 sources follow finite, explicitly checked paths into three distinct negative cycles, with these signed component masses:

| Cycle | Source atoms | Signed source mass |
|---|---:|---:|
| `−1 → −1` | 1054 | −20 |
| `−5 → −7 → −5` | 1027 | −73 |
| `−17 → −25 → −37 → −55 → −41 → −61 → −91 → −17` | 1123 | **93** |

The stored current and residual verify

```
Ã_96 = (I − P)J − 20δ_(−1) − 73δ_(−5) + 93δ_(−17).
```

Consequently **no finite exact current and no finite current with an everywhere nonpositive residual exists** for `Ã_96`, including currents with arbitrary auxiliary states.

## Proof

From §5 of the legacy note `aggregate_duality.md` (now [`exposure-potential-boundary-flux`](exposure-potential-boundary-flux/README.md)), kept as written.

Negative odd states stay negative, so every source has infinite hitting time of 1; since the source has total mass zero, `H_L(Ã_96) = 0` at every horizon. Reflection permutes residue classes, so the projections vanish by [`binary-residue-projection-information-loss`](binary-residue-projection-information-loss.md) at `N = 96`. Every path reaches its chosen cycle anchor within 86 steps; the 5868-row signed current routes each source to its anchor, and the residual is the three anchor masses. The indicator of the basin of the seven-state cycle is globally invariant, zero at the absorber, and pairs to 93 with the source, so by [`orbit-component-current-criterion`](orbit-component-current-criterion/README.md) neither kind of current exists. ∎

## Remarks

- **What it shows.** A rigorous failure of the inference "balanced bands and bounded scalar work imply a current". A successful positive-integer argument must use more than those scalar facts: the distribution of source signs among actual orbit components.
- **Controls.** This is the annular analogue of the negative-integer example in [`orbit-component-current-criterion`](orbit-component-current-criterion/README.md) and of the PR1 lane's `d = −1` control ([`locally-collatz-like-control-barrier`](locally-collatz-like-control-barrier/README.md)). It is not a positive Collatz counterexample and says nothing against [`five-ray-current-criterion`](five-ray-current-criterion/README.md).
- Novelty undetermined.

## History

- Migrated from `experiments/annular_construction/duality/aggregate_duality.md` §5 (part of the legacy R10 round; alias `R10-c`) at commit `be73a66`, by the B08 migration (Claude, Opus 5.5). The stored tables stay with the checker in [`exposure-potential-boundary-flux`](exposure-potential-boundary-flux/README.md). Legacy status: "written graph/arithmetic identities and exact scoped counterexamples".
- Main lane (ChatGPT, Codex), 2026-10-17, commit `ce56699`. No review from another lane is on record.
