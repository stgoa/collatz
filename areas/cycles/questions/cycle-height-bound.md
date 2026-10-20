---
id: cycle-height-bound
kind: question
title: Is the height of a nontrivial 3x+1 cycle o(m)?
status: open
claim: >
  Prove or refute: every hypothetical nontrivial primitive integer cycle of the raw odd-only 3x+1 map, of
  period m, minimum L and maximum H, has height B = floor(log₂(H/L)) = o(m); a bound B = O(log m) would be the
  strong form. Known: B ≤ (log₂3 − 1)(m − 1) + (m − 1)·log₂(1 + 1/(3L)), about 0.585m.
created: 2026-10-19
tags: [cycles, height, rotation-distance, frontier]
---

# Is the height of a nontrivial 3x+1 cycle o(m)?

## Question

For a hypothetical nontrivial primitive integer cycle of the raw odd-only `3x+1` map (`q = 1`), with period `m`, minimum `L`, maximum `H` and height `B = floor(log₂(H/L))`, prove `B = o(m)`, or the strong form `B = O(log m)`; or show that no argument of a stated kind can give it. The trivial bound is the ceiling `B ≤ (log₂3 − 1)(m − 1) + (m − 1)·log₂(1 + 1/(3L)) ≈ 0.585m` ([`cycle-height-ceiling`](../results/cycle-height-ceiling.md)).

## Why it matters

By the mismatch–height trade-off ([`mismatch-height-tradeoff`](../results/mismatch-height-tradeoff/README.md), formal given the replayed gap), every nonidentity rotation of such a cycle has more than `log₂3·m/(B + 342·log₂ m + 172)` mismatches. So any `B = o(m)` answers [`rotation-distance-growth`](rotation-distance-growth.md) with a growing `F(m)`, and `B = O(log m)` gives its "order `m/log m`" form. The side lane called this "the open obstacle, now exactly a height bound for integer cycles" (legacy S05 §4).

## Known progress

- The ceiling above (formal), vacuous for the trade-off only in the top tenth of the height range: the trade-off stays above 3 mismatches for every `B ≤ 0.53m` at the literature period.
- **It cannot come from rotation distance alone.** [`distance-three-height-family`](../results/distance-three-height-family.md): bounded rotation distance, `q ≤ L` and vanishing drift do not bound the height of rational cycles. A proof must use `q = 1` arithmetic.
- Exactly two and three mismatches are excluded for large `m` without any height bound ([`two-mismatch-exclusion-via-gap`](../results/two-mismatch-exclusion-via-gap/README.md), [`three-mismatch-exclusion`](../results/three-mismatch-exclusion/README.md)): there the pigeonhole forces a very tall cycle, which the ceiling forbids.
- **Data, not evidence about `q = 1`.** Actual reduced `3x+q` cycles (odd `q < 1000`, 1,147 cycles with `m ≥ 2`) have `B ≤ 17` and `B/log₂ m ≤ 3.0` for `m ≥ 30` (S05 appendix, `mismatch-height-tradeoff/s5_cycle_heights.py`). These have `q/L = O(1)`, the opposite regime from a `q = 1` cycle with `L > 2^71`.
- **Literature (calibration only).** An extended search (side-lane feed 2026-10-19 15:08) found no bound on `H/L` for nontrivial `3x+1` cycles; it found bounds on the minimum in terms of the length, the Christoffel extremality of the minimum, and local-minima counts. Halbeisen–Hungerbühler's length-versus-minimum bound ([`halbeisen-1997-rational-cycles`](../../../sources/halbeisen-1997-rational-cycles.md)) was not retrieved there.

## Suggested attacks

Speculation, from the side-lane notes: use `q = 1` arithmetic that rational cycles at `q > 1` fail, for example the comparison with the integer cycles `{1}`, `{−1}`, `{−5, −7}`, `{−17, …}` as in [`ones-run-divisibility`](../results/ones-run-divisibility.md), or the mod-`D` relation over the mismatches (the Abel-summed form of C012's coupled system). The Denjoy–Koksma height inequality of the legacy S12 (not yet migrated, `experiments/cycle_spectrum/S12/`) bounds the height by the rotation's letter variation and is the programme's later attack on this question.
