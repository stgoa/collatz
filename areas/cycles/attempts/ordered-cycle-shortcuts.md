---
id: ordered-cycle-shortcuts
kind: attempt
title: Four shortcuts toward excluding ordered denominator-one cycles, each refuted by an exact control
status: written
claim: >
  Tried, toward excluding ordered q = 1 cycles: (a) mechanical normalised exponents with correct
  heights imply order; (b) some normalised pair has primitive odd gap at most q; (c) a wide cycle
  loses at least one unit from the mechanical minimum; (d) ordered affine equations with integer
  coordinates suffice. Verdict: each is false by an exact control: (a) a primitive q = 1909, period-7
  cycle with both properties has two inversions; (b) the ordered q = 13 cycle (227, 347, 527, 797, 601)
  has minimum odd gap 15; (c) the q = 5 cycle (19, 31, 49) loses only 4/5; (d) 4 → 13 → 5 → 4 satisfies
  the ordered equations at q = 1 but has an even state, a zero valuation and a nonexact division.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: [dyadic-order-lemma]
evidence:
  - "../results/ordered-cycle-sparse-forcing/ORDER_RIGIDITY.md, sections 3-4: the controls"
  - "../results/rotation-block-exclusion/c005_c006_order_check.py, part (6): side-lane check of the q = 13 gap 15 and the q = 5 cycle"
tags: [cycles, dyadic-order, counterexample]
---

# Four shortcuts toward excluding ordered denominator-one cycles, each refuted by an exact control

## Idea

After [`dyadic-order-lemma`](../results/dyadic-order-lemma.md) and [`ordered-cycle-sparse-forcing`](../results/ordered-cycle-sparse-forcing/README.md), several simpler routes to [`ordered-cycle-denominator-one`](../questions/ordered-cycle-denominator-one.md) suggest themselves. Each fails on an exact control. (The fifth shortcut of the legacy C006 table, "one legal height defect preserves the mechanical unit gcd", is recorded with its C005 relatives in [`mechanical-normalized-word-transfer`](mechanical-normalized-word-transfer.md).)

## What happened

| Proposed shortcut | Exact obstruction |
| --- | --- |
| (a) Mechanical normalised exponents and correct heights imply order | The raw `q = 1909` cycle `n = (3991, 6941, 5683, 9479, 15173, 11857, 4685)`, `a = (1,2,1,1,2,3,2)`, `h = (0,0,0,1,1,1,0)`, `c = (1,2,2,1,2,2,2)` has `A = 12`, `m = 7`, `gcd(A, m) = 1`, canonical lower mechanical `c`, actual heights and `L = 3991 > q`; yet sorted `F = (13882, 15964, 15173, 18958, 18740, 22732, 23714)` has inversions at `(6, 3)` and `(2, 5)`, and the successor ranks `(5,0,6,2,1,3,4)` are not a rotation. |
| (b) Some normalised pair has primitive odd gap at most `q` | The ordered `q = 13` cycle `(227, 347, 527, 797, 601)`, valuations `(1,1,1,2,3)`, `h = (0,0,1,1,1)`, sorted normalised states `(227, 527/2, 601/2, 347, 797/2)`, increasing `F = (694, 797, 908, 1054, 1202)`: among **all** pairwise differences the least odd part is 15, from `347 − 227 = 120 = 8·15`, exceeding `q = 13`. |
| (c) A wide cycle loses at least one unit from the mechanical minimum | The `q = 5` cycle `(19, 31, 49)` loses only `4/5`. |
| (d) Ordered affine equations with integer coordinates suffice | The formal `q = 1` cycle `4 → 13 → 5 → 4` has exponents `(0, 3, 2)`, heights `(0, 1, 0)`, normalised word `(1,2,2)` and strictly ordered `F = (13, 16, 20)` at sorted `z = (4, 5, 13/2)`; it satisfies the weighted circle equations with `C_c = 23`, `D = 5`, `E_h = 3`, `D | C_c − E_h = 20`. It is **not** an odd-only cycle: 4 is even and the first valuation is zero. Strict validators reject it. |

## Why it fails

(a) Correct dyadic heights and a mechanical `c` do not control every adjacent-rank inequality; a proof starting from them must still verify all of them. (b) refutes that specific universal small-gap claim, not other gap estimates (compare the absolute version, [`close-pair-lattice-criterion`](close-pair-lattice-criterion/README.md)). (c) bounds the loss below one unit. (d) shows that any argument that allows zero valuations or forgets oddness can produce a false denominator-1 "cycle": exact legality (odd states, positive valuations, exact divisions) must be kept.

## What survives

The controls themselves, as tests for any future argument: the `q = 1909` and `q = 11` inversions, the `q = 13` gap, the `q = 5` and `q = 233` ordered cancellations, and the zero-valuation relaxation `4 → 13 → 5 → 4`. The surviving exact statements are those of [`ordered-cycle-sparse-forcing`](../results/ordered-cycle-sparse-forcing/README.md).

## History

- Split from `experiments/cycle_spectrum/C006/` (legacy ID `C006`; `REPORT.md` "Failed shortcuts retained as exact controls", `ORDER_RIGIDITY.md` §§3–4) at commit `be73a66`, by the B03 migration (Claude, Opus 5.5). Main lane (ChatGPT/Codex), 2026-10-19. Status `written`: the side lane independently confirmed controls (b) and (c) (feed 2026-10-19 02:13); (a) and (d) were checked only within the main lane.
