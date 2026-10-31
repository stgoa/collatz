# Review of ordered-cycle-shortcuts

## What I checked

- Read the conventions, `areas/cycles/OVERVIEW.md`, the node ([`README.md`](README.md)), [`ORDER_RIGIDITY.md`](../../results/ordered-cycle-sparse-forcing/ORDER_RIGIDITY.md) §§3–4 (the source of the controls), the dependency [`dyadic-order-lemma`](../../results/dyadic-order-lemma.md), and part (6) of the cited side-lane script [`c005_c006_order_check.py`](../../results/rotation-block-exclusion/c005_c006_order_check.py). The legacy C006 `REPORT.md` table "Failed shortcuts retained as exact controls" is not in the repository, so the original wording of the four shortcuts could only be read from this node.
- **Recomputed every control from scratch** (odd-only map, exact rational arithmetic; my script `check_shortcuts.py`, outside the repository, 0.02 s):
  - (a) Iterating `3x+1909` from 3991 returns `(3991, 6941, 5683, 9479, 15173, 11857, 4685)`, word `(1,2,1,1,2,3,2)`, `A = 12`, `m = 7`, `D = 1909 = q` (`gcd(C, D) = 1`), heights `(0,0,0,1,1,1,0)`, `c = (1,2,2,1,2,2,2) = mech(12, 7, 0)`, `L = 3991 > q`. Sorted `z` indices `(0,6,3,2,5,1,4)`; sorted `F = (13882, 15964, 15173, 18958, 18740, 22732, 23714)` with exactly two inversions (adjacent and in total), between states 6, 3 and 2, 5; successor ranks `(5,0,6,2,1,3,4)`, not a rotation. So mechanical `c`, correct heights and `L > q` do not imply order.
  - (b) `3x+13` from 227: `(227, 347, 527, 797, 601)`, word `(1,1,1,2,3)`, heights `(0,0,1,1,1)`, `q = 13 ≤ L`, ordered (sorted `F = (694, 797, 908, 1054, 1202)`). Over the scaled states `2^B·z = (454, 527, 601, 694, 797)` the odd parts of the ten pairwise gaps are 15, 37, 49, 73, 93, 103, 135, 147, 167, 343; the minimum 15 comes from `694 − 454 = 240 = 16·15` (the raw numerators give the same minimum, from `347 − 227 = 120`). `15 > 13`.
  - (c) `3x+5` from 19: `(19, 31, 49)`, word `(1,1,3)`, heights `(0,0,1)`, `c = (1,2,2)`, wide (`49 ≥ 2·19`), ordered, `q ≤ L`; `C_c = C_lower(5, 3) = 23`, `D = 5`; `C_c/D − L/q = 23/5 − 19/5 = 4/5`, while `q·C_c/D − L = 23 − 19 = 4`.
  - (d) `4 → 13 → 5 → 4` with exponents `(0, 3, 2)`: heights `(0,1,0)` with `L = 4`, `c = (1,2,2)`, sorted `z = (4, 5, 13/2)`, sorted `F = (13, 16, 20)` increasing; `C_c = 23`, `D = 5`, `E_h = 3`, `D | 20` and `D·L = 20 = q·(C_c − E_h)`. The divisions `13/2^0`, `40/2^3`, `16/2^2` are exact as written; `v₂(3n+1)` over the states is `(0, 3, 4)`, so the arrow `5 → 4` does not remove the full power of two.
  - "What survives": `3x+11` from 13 gives `(13, 25, 43, 35, 29, 49, 79, 31)` with `q ≤ L` and the inversion `F(13) = 50 > 49 = F(29/2)`; `3x+233` from 1907 gives the ordered cycle `(1907, …, 2465)` with shift 5, `C_c = 14501`, `E_h = 1152`, `C_h = 13349`, `D = 1631 = 7·233`, `gcd(C_h, D) = 7`; the ordered `q = 5` period-17 cycle with minimum 187 has `C_c = 548440271`, `C_h = 189900931`, `D = 5077565`, `gcd(C_h, D) = 1015513`, all as in `ORDER_RIGIDITY.md` §4.
- **Control consistency.** Every control is an actual `3x+d` cycle and the node excludes nothing, so no control can contradict it.
- **Certificates.** None listed; nothing to run. The cited side-lane script is evidence only; run as `python3 areas/cycles/results/rotation-block-exclusion/c005_c006_order_check.py areas/cycles/results/actual-cycles-3x-d-corpus/actual_cycles.json` from the repository root it exits 0 in 0.6 s with `"result": "PASS"` and `q13_min_odd_part_of_scaled_pair_gaps: 15`.

## What I did not check

- The original phrasing of shortcuts (a)–(d) in the legacy C006 report (absent from the repository); in particular which scale "one unit" in (c) referred to (Finding 1).
- The side-lane feed entry (2026-10-19 02:13) cited in History.

## Findings

1. **Scale of "one unit" in (c) (imprecision; corrected).** "Loses only 4/5" measures the loss in units of `q`, i.e. `C_c/D − L/q = 4/5` in the normalisation `x = n/q`, where the shortcut's "one unit" is the integer 1 at `q = 1`. In integer units the loss is `q·C_c/D − L = 4 ≥ 1`, so the control refutes the shortcut only in the `q`-scaled reading. Since the figure 4/5 only makes sense in that reading, I added "(in units of q: C_c/D − L/q = 23/5 − 19/5)" to the claim and the table.
2. **"A nonexact division" in (d) (imprecision; corrected).** All three divisions are exact as written; what fails is the exact-valuation convention of [`NOTATION.md`](../../../../conventions/NOTATION.md) §2 at the arrow `5 → 4` (`16 = 2^4`, only `2^2` removed), besides the even state and the zero valuation already named. Added a parenthetical in the claim and a sentence in the table.
3. **Wording in "Why it fails" (imprecision; not changed).** "(c) bounds the loss below one unit" describes a single example: it shows that the loss can be below one unit and bounds nothing.
4. **Links (typo level; corrected).** Six body links and two evidence paths needed one more `../` after the move to a folder.

## Verdict

HOLDS WITH CORRECTIONS: the four controls and the "what survives" controls are exact and refute the stated shortcuts; (i) the unit of the loss in (c) and (ii) the meaning of "nonexact division" in (d) made explicit, (iii) links repaired. No certificates to run. Status raised to reviewed.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
