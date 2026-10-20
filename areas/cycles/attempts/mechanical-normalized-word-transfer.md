---
id: mechanical-normalized-word-transfer
kind: attempt
title: Transferring the mechanical-word denominator theorem to a mechanical normalised word
status: reviewed
claim: >
  Tried: for an ordered cycle (circular normalised successor order) the normalised word c is
  mechanical with gcd(A, m) = 1, so R71's gcd(C_c, D) = 1 might give reduced denominator D, or at
  least survive one legal height defect. Verdict: false. Ordered actual controls with mechanical c
  have large cancellation: q = 233, period 8, two bands, gcd(C_w, D) = 7; q = 5, period 17, four bands,
  gcd = 1,015,513; and a q = 233, period-8 cycle with a single height-one state has
  C_c = 14501, C_h = 13349, D = 1631 and gcd(C_h, D) = 7. The denominator is governed by the weighted
  intercept C_h = C_c − E_h, not by C_c.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: [dyadic-order-lemma]
evidence:
  - "../results/rotation-block-exclusion/ORDER_THEORY.md, section 3: the C005 counterexamples"
  - "../results/ordered-cycle-sparse-forcing/ORDER_RIGIDITY.md, sections 2 and 4: the weighted identity and the one-defect control"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-19
    scope: "Feed 2026-10-19 02:13, REFEREE C005 + C006: all 15 normalised q = 233 period-8 cycles have cancellation 7, strict order and rank shift 5; both q = 5 period-17 cycles (minima 187 and 347) have cancellation 1,015,513, strict order and rank shift 10"
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Feed 02:13, update 02:19: re-derived the weighted identity D·L = q·C_h and the one-defect q = 233 numbers (C_h = 13349, gcd(13349, 1631) = 7) with no error"
tags: [cycles, dyadic-order, cancellation, counterexample]
---

# Transferring the mechanical-word denominator theorem to a mechanical normalised word

## Idea

By [`dyadic-order-lemma`](../results/dyadic-order-lemma.md), an ordered cycle has a mechanical normalised word `c` with coprime totals, and R71's exact denominator theorem ([`mechanical-word-exact-denominator`](../results/mechanical-word-exact-denominator/README.md)) gives `gcd(C_c, D) = 1` for mechanical words. If the original intercept behaved like `C_c`, ordered cycles would have reduced denominator `D > 1` and the ordered class would be excluded at `q = 1`.

## What happened

The original word `a` differs from `c` by the height coboundary, and the exact weighted fixed-point equation, starting at `n_0 = L`, is

```
(2^A − 3^m)·L = q·Σ_j 3^(m−1−j)·2^(P_j − h_j),     P_j = Σ_(i<j) c_i,      (4)
```

whose sum is exactly the original intercept `C_w` (`P_j = A_j + h_j`). Discarding `h` replaces it by the unweighted mechanical intercept for `c`, which can have a different gcd with `D`. Exact controls (raw cycles, `d = q`):

| Cycle | Heights | `gcd(C_w, D)` | Order |
|---|---|---:|---|
| `q = 233`: `n = (1535, 2419, 3745, 2867, 4417, 3371, 5173, 1969)`, `a = (1,1,2,1,2,1,3,2)`, `c = (1,2,1,2,2,1,2,2)` | `(0,0,1,0,1,1,1,0)`, `H < 4L` | 7 (`C_w = 10745`, `D = 1631 = 7·233`) | strict, rank shift `+5 mod 8` |
| `q = 5`, period 17, from 187 | 0 to 3 | 1,015,513 (`C_w = 189900931`, `D = 5077565`) | strict, rank shift `+10 mod 17` |
| `q = 233` one-defect: `n = (1907, 2977, 2291, 3553, 2723, 4201, 3209, 2465)`, `a = (1,2,1,2,1,2,2,2)` | `(0,0,0,0,0,1,0,0)`, `H < 4L` | 7 (`C_c = 14501`, `E_h = M_5/2 = 1152`, `C_h = 13349`) | strict, rank shift `+5 mod 8` |

All three have the canonical lower mechanical `c` with `(A, m) = (13, 8)` or total 27 for `m = 17`, `q ≤ L`, and nonmechanical original words. The first refutes even a two-band, strictly order-preserving, `q ≤ L` version of the inference; the third shows that "one legal height defect preserves the mechanical unit gcd" is false.

## Why it fails

In C006's notation `C_h = C_c − E_h` with `E_h = Σ_j M_j·(1 − 2^(−h_j))`, `M_j = 3^(m−1−j)·2^(P_j)`, and `q = D/gcd(C_h, D)`. The mechanical theorem controls `gcd(C_c, D) = 1` only; it supplies no bound on `gcd(C_c − E_h, D)`, and a single legal height excursion already creates nontrivial cancellation. Neither `E_h < D` nor a single crossing of the `D` lattice holds uniformly: the two-band `q = 233` control has `E_h = 3756 > D = 1631`; the `q = 5` control has `C_c = 548440271`, `E_h = 358539340`, `D = 5077565`.

## What survives

- The exact weighted identity `D·L = q·C_h` and the positive Green comparison `q·2^(−B)·Y_i ≤ z_i ≤ q·Y_i` ([`ordered-cycle-sparse-forcing`](../results/ordered-cycle-sparse-forcing/README.md)).
- The precise missing step for `q = 1` ordered cycles is the congruence `D | C_h = C_c − E_h` for a **legal odd** profile, recorded as [`ordered-cycle-denominator-one`](../questions/ordered-cycle-denominator-one.md); its single-defect case is [`one-height-defect-ordered-cycles`](../questions/one-height-defect-ordered-cycles.md).
- Any next argument must retain the weighted intercept and allow the ordered `q = 5` and `q = 233` controls.

## History

- Split from `experiments/cycle_spectrum/C005/` (legacy ID `C005`; `ORDER_THEORY.md` §3, `REPORT.md` §2) and `experiments/cycle_spectrum/C006/` (legacy ID `C006`; `ORDER_RIGIDITY.md` §4, first table row "One legal height defect preserves the mechanical unit gcd") at commit `be73a66`, by the B03 migration (Claude, Opus 5.5). Main lane (ChatGPT/Codex), 2026-10-19.
