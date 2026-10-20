---
id: narrow-cycles-are-mechanical
kind: result
title: A cycle with H < 2L is exactly a mechanical word, so every nontrivial 3x+1 cycle has H > 2L
status: formal
claim: >
  Raw odd-only clock, no absorption. (i) A primitive positive rational cycle with m ≥ 2 distinct
  odd states, smallest L, largest H and total valuation A has H < 2L if and only if its valuation
  word is a rotation of the mechanical word a_j = floor((j+1)A/m) − floor(jA/m); then gcd(A, m) = 1
  and its reduced denominator is exactly D = 2^A − 3^m (no cancellation). (ii) Consequently every
  positive integer cycle of the odd-only 3x+1 map other than the fixed point 1 has a state H > 2L,
  where L is its minimum (any period, no primitivity assumed).
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: [mechanical-word-exact-denominator]
lean:
  - LeanLane.Cyc.narrow_mech
  - LeanLane.Cyc.mech_rotate
  - LeanLane.Cyc.NarrowCycle.is_mech_of_narrow
  - LeanLane.Cyc.mech_gcd_one_phase
  - LeanLane.Cyc.mech_D_ne_one
  - LeanLane.Cyc.OddCycle.narrow_integer_cycle
  - LeanLane.Cyc.OddCycle.H_gt_two_L
certificates: [c004c_bridge_check.py]
evidence:
  - "ROTATION_LATTICE.md: the written proofs (sections 1-4); it also holds the proofs of rotation-lattice-single-divisibility and narrow-cycle-spectrum-law"
  - "check_rotations.py, rotation_audit.json: main-lane finite checker and receipt. Fails at its new path: it loads the corpus as HERE.parent/'C001/actual_cycles.json' and the fixtures from experiments/phase6/ (cycle_fixtures.json, now in ../../../convergence/results/baseline-obligation-transfer-controls/, byte-identical). Passed at be73a66 as experiments/cycle_spectrum/C004/check_rotations.py (archive/legacy-checker-run-be73a66.md)"
  - "c004_narrow_check.py, c004_narrow_check.json: side-lane independent check (REFEREE C004). Needs the corpus path as argument, so it fails bare (passed with its argument; exit 1 bare at be73a66 as reviews/side_lane/c004_narrow_check.py, archive/legacy-checker-run-be73a66.md). Run as python3 <this folder>/c004_narrow_check.py areas/cycles/results/actual-cycles-3x-d-corpus/actual_cycles.json it exits 0 and reproduces its receipt byte for byte (checked at migration)"
  - "c004c_bridge_check.json: receipt of the side-lane bridge check (written only when an output path is given)"
  - "INDEPENDENT_REVIEW.md, ROOT_REVIEW.md: main-lane reviews; SIDE_REVIEW.md: the main lane's read of the side-lane feed"
  - "delivery_checks.json, full_gate.json: historical delivery receipt and historical finite gate"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-19
    link: c004_narrow_check.py
    scope: "Feed 2026-10-19 01:06, REFEREE C004 at main 61cf54a: narrow ⇔ mechanical on all 97,020 primitive words of length 1-7, entries 1-5 (a grid different from main's); narrow cycles with m > 1 have gcd(A, m) = 1 and den = D. Feed 05:58 and 06:07: VERIFIED Lean C004-c and C004-d, statement match and receipts checked, bridge checked by c004c_bridge_check.py"
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "C004 re-derived by hand with no error (feed 01:19); Lean units C004-a, C004-b, C004-c, C004-d (with R71-a) verified, 2026-10-19"
    link: ../../../../archive/side-lane/FEED.md
aliases: [C004]
tags: [cycles, narrow-cycles, mechanical-words, christoffel, formal]
---

# A cycle with H < 2L is exactly a mechanical word, so every nontrivial 3x+1 cycle has H > 2L

## Statement

Let a primitive positive rational cycle of the raw odd-only map have `m` distinct odd states, smallest `L`, largest `H`, and total valuation `A`. Here `m` is the **primitive state period**.

**Narrow-cycle theorem.** If `m > 1`, then

```
H < 2L  iff  w is a cyclic rotation of  a_j = floor((j+1)A/m) − floor(jA/m),      (8)
```

the mechanical valuation word with its actual total `A`. In this case `gcd(A, m) = 1`, and the reduced denominator is exactly `D = 2^A − 3^m`, with no numerator cancellation. A fixed point (`m = 1`) is mechanically coded and has `H = L`.

**Integer corollary.** Every hypothetical nontrivial positive **integer** odd-only Collatz cycle must satisfy

```
H > 2L.                                                                            (9)
```

Equality cannot occur: all reduced numerators are odd and share one odd denominator, so one state cannot be twice another. The theorem leaves every wide cycle and every aperiodic orbit open. It is an intrinsic condition on arbitrary primitive words, unlike the repeated-block hypotheses of C001–C003.

## Proof

Written proof: [`ROTATION_LATTICE.md`](ROTATION_LATTICE.md) §3. It uses only order and the exact mechanical denominator theorem (legacy summary, lightly edited):

> Sort the states in `[L, 2L)`. Their values `3x + 1` also span a ratio less than two. The exact division powers therefore have two adjacent exponents, `q` or `q + 1`, separated by one threshold in sorted order; the high outputs precede the low outputs. The successor permutation is a cyclic shift of ranks by `h`, with `gcd(h, m) = 1` because the orbit visits all states. Following that shift gives the displayed floor-difference word, `a_i = q + floor((i+1)h/m) − floor(ih/m)`, with `A = mq + h`. Conversely, the mechanical phase coefficients are all less than twice their minimum, term by term (`0 ≤ floor((jA+l)/m) − floor(jA/m) ≤ 1`), so `C_0 ≤ C_l < 2C_0`.

For the integer corollary: R71's exact denominator theorem ([`mechanical-word-exact-denominator`](../mechanical-word-exact-denominator/README.md)) gives `gcd(C, D) = 1` for a primitive mechanical word, and its elementary mod-8 argument shows `D = 2^A − 3^m = 1` cannot occur at `m > 1`; so the only integer mechanical cycle is the fixed point 1. R71 is [`mechanical-word-exact-denominator`](../mechanical-word-exact-denominator/README.md) (legacy `BALANCED_DENOMINATORS.md` §2); its two needed facts are formal here as `mech_gcd_one_phase` and `mech_D_ne_one` (Lean unit R71-a).

## Certificates

- [`c004c_bridge_check.py`](c004c_bridge_check.py) (about 2 s; side lane, independent code): finds actual cycles of `T_q(n) = (3n+q)/2^v₂(3n+q)` by direct iteration (`q = 1` and the controls `q = 5, 7, 13, 61`), lists each from its minimum as in Lean's `OddCycle`, and checks the cycle identity `D·n_0 = q·C(w)` and its rotated form `q·C(w.rotate i) = D·n_i`; that narrow cycles are exactly rotations of the mechanical word with coprime totals (or `m = 1`); that at `q = 1` the only narrow cycle is the fixed point 1, while the controls have narrow cycles with `m ≥ 2` and `m = 1` cycles other than `n_0 = 1`; and that primitivity is needed for "`m = 1`" (the doubled fixed point `(2, 2)`).

The main-lane checker [`check_rotations.py`](check_rotations.py) no longer runs at this path (see `evidence`). Its receipt [`rotation_audit.json`](rotation_audit.json) records:

| Check | Coverage |
| --- | --- |
| Stored actual cycles | 2,459 across 333 parameters; all eleven historical fixtures. |
| Actual rotations and raw arrows | 36,912 of each, with a separate normalized-arrow replay. |
| Distinct normalized cycles | 1,184: 1,176 nontrivial and 8 fixed. |
| Actual narrow nontrivial cycles | 105 source instances representing 11 normalized cycles; all mechanical, coprime totals and `g = 1`. |
| One-letter cuts | Every nontrivial rotation, with the full exact gcd formula. |
| Small matrices | 340 words, 18,964 square minors and 1,592 augmented maximal minors. |
| Short-word grid | 87,380 words of lengths 1–8 and valuations 1–4; 86,442 positive realizations and 663,079 raw arrows. |
| Primitive narrow words in that grid | 297 nontrivial rotations, with both directions of the equivalence checked; fixed points and proper powers separately counted. |
| Mechanical gap checks | 156 coprime upper approximants; 20,241 points and 20,085 adjacent gaps. |

Finite checks do not prove the classification; they support the implementation.

## Lean

`lean/CycleSpectrum.lean`, Lean units C004-a, C004-b, C004-c, C004-d and R71-a (legacy `lean/STATE.md`, now [`archive/lean-lane/STATE.md`](../../../../archive/lean-lane/STATE.md)). Axioms `propext`, `Classical.choice`, `Quot.sound`; receipts `lean/receipts/CycleSpectrum.*`. No external input is used.

- **(i), mechanical ⇒ narrow.** `LeanLane.Cyc.narrow_mech`: every rotation of `mech A m 0` has `C_0 ≤ C_i < 2C_0` and the common `D = 2^A − 3^m`; with `mech_rotate` (every rotation of a phase word is a phase word) this is the reverse direction for every phase. No coprimality is needed for the inequalities.
- **(i), narrow ⇒ mechanical.** `LeanLane.Cyc.NarrowCycle.is_mech_of_narrow`: a word `w` of length `m ≥ 2` with `D_w > 0`, distinct rotated intercepts (the `m` states `C(w.rotate i)/D` are distinct, i.e. primitive) and `C(w.rotate i) < 2·C(w.rotate j)` for all `i, j` (exactly `H < 2L` for the states `C_i/D`, which share `D > 0`) satisfies `w = mech w.sum m l` for some phase `l < m` and `gcd(w.sum, m) = 1`. Letter positivity is not assumed; it follows from `D_w > 0`.
- **(i), denominator.** `LeanLane.Cyc.mech_gcd_one_phase` (R71-a): for `m ≥ 2`, `A ≥ m`, `gcd(A, m) = 1`, every phase word has `gcd(C, D) = 1`, so `den = D`. `A ≥ m` holds for a cycle because `D > 0`.
- **(ii).** `LeanLane.Cyc.OddCycle.narrow_integer_cycle`: an `OddCycle` (periodic odd positive integers `n_i` with `n_0` the minimum, exact arrows `2^(a_i)·n_(i+1) = 3n_i + q`, `q > 0`) with `q = 1`, all heights 0 (every `n_i < 2n_0`) and distinct states over one period has `m = 1` and `n_0 = 1`; it combines `is_mech_of_narrow`, `mech_gcd_one_phase`, the cycle identity `D | C`, and `mech_D_ne_one` (`2^A − 3^m ≠ 1` for `m ≥ 2`). `LeanLane.Cyc.OddCycle.H_gt_two_L`: **any** `OddCycle` with `q = 1` and `n_0 ≠ 1` has a state with `2·n_0 < n_i`; this is (9) exactly, with no primitivity hypothesis (it passes to the least period internally, and parity turns `≥` into `>`). `H_gt_two_L'` states the same with "some state is not 1" as hypothesis.

## Remarks

- **Scope of the gain.** The hypothesis is geometric and testable on any cycle. The excluded word class itself is the mechanical class already handled by R71 ([`mechanical-word-exact-denominator`](../mechanical-word-exact-denominator/README.md)). This is not a new general cycle-count record, nor an exclusion of the wider cycles left by the theorem. Every nontrivial cycle lies in `H > 2L`, where this says nothing more.
- **Literature.** The exclusion of mechanical (upper Christoffel) words as integer cycles is Knight's published theorem ([`knight-2026-high-cycles`](../../../../sources/knight-2026-high-cycles.md)), and is also kernel-checked in `mmusson/collatz` (`NormBridge.cycle_one_move_christoffel`; see [`musson-collatz-gap-all`](../../../../sources/musson-collatz-gap-all.md)). The Christoffel extremal minimum bound is Halbeisen–Hungerbühler ([`halbeisen-1997-rational-cycles`](../../../../sources/halbeisen-1997-rational-cycles.md)). These are re-derived here by another route, not assumed. The classification "narrow ⇔ mechanical" by rank dynamics was not found in the sources read; novelty undetermined. "First" in the side-lane milestone entries means first in this programme.
- **Controls.** The `d = 5` cycle `(23, 37, 29)` (word `(1,2,2)`) is narrow and mechanical; the `d = 13` mechanical cycle has numerators `319, 367, 421, 485, 557` with ratio `557/319 < 2`; narrow cycles with `m ≥ 2` exist at `q = 5` (minimum 23, word `(1,2,2)`, `D = 5`) and `q = 13` (minimum 319, `m = 5`, `D = 13`), and every `q` has the narrow one-letter cycle `n_0 = q`. The only input specific to `d = 1` is that `2^A − 3^m = 1` has no solution with `m ≥ 2`; the `q = 5` and `q = 13` controls are exactly where that input fails.
- **Related.** The narrow spectrum across all `d`: [`narrow-cycle-spectrum-law`](../narrow-cycle-spectrum-law.md). The all-rotation divisibility system: [`rotation-lattice-single-divisibility`](../rotation-lattice-single-divisibility.md). The rejected close-pair criterion: [`close-pair-lattice-criterion`](../../attempts/close-pair-lattice-criterion/README.md). The next rung (`H < 8L` forces order): [`three-band-collatz-cycles-are-ordered`](../three-band-collatz-cycles-are-ordered.md).
- **Legacy decision.** The all-rotation mechanism produced a real classification in one geometric range; its two simplest extensions fail (the congruences are dependent, and absolute proximity has no universal bound). The next mechanism must retain the order of states across different dyadic ranges and how that order constrains cancellation. The side lane's bounded-discrepancy proposal was assessed in [`SIDE_REVIEW.md`](SIDE_REVIEW.md): its necessary estimate does not by itself bound discrepancy independently of period and minimum, and exclusion for every finite discrepancy ceiling would recover the full cycle headline, so it is not a smaller completion criterion.

## History

- Migrated from `experiments/cycle_spectrum/C004/` (legacy ID `C004`; `REPORT.md`, proof `ROTATION_LATTICE.md`) at commit `be73a66`, by the B03 migration (Claude, Opus 5.5). The side-lane checks `reviews/side_lane/c004_narrow_check.{py,json}` and `c004c_bridge_check.{py,json}` moved here. Parts of the legacy report became [`narrow-cycle-spectrum-law`](../narrow-cycle-spectrum-law.md), [`rotation-lattice-single-divisibility`](../rotation-lattice-single-divisibility.md) and [`close-pair-lattice-criterion`](../../attempts/close-pair-lattice-criterion/README.md) (with `SIZE_PROBE.md`).
- Main lane (ChatGPT/Codex), 2026-10-19. No proof correction was required in review; two scope clarifications were made (the maximum-state argument says `d = 1`; the generic R71 large-height family is only said to have reduced denominator greater than 1).
- Formalised by the Lean lane (Claude Lean lane, Fable), 2026-10-19: C004-a (iteration 15), C004-b (iterations 16–18), R71-a (iteration 36), C004-c (iteration 37), C004-d (iteration 38). A side-lane correction of 05:44 noted that besides R71's `g = 1` the bridge from actual cycles (C004-c) was also needed.
