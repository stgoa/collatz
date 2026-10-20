---
id: rotating-mechanical-two-block-family
kind: result
title: "Mechanical block and its rotation: u_m^k v_m^ℓ has growing minima and no denominator 1"
status: reviewed
claim: >
  Raw odd-only clock. For m ≥ 13 let A = bit length of 3^m, u_m the lower mechanical word of length
  m and total A, and v_m its one-letter left rotation. For all k, ℓ ≥ 1 every state of the rational
  cycle of w = u_m^k v_m^ℓ exceeds m/12 > 1, w is primitive, not mechanical, and its shortcut parity
  word is unbalanced; with n = k + ℓ it has n(2m − A) − 1 odd-only and n(A − m) shortcut local
  minima. If n ≥ 3, den(w) > 3·(3^m)^(n−h−1)/(2m) > 1 with h = gcd(k, ℓ), so w is not a 3x+1
  integer cycle.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: [equal-total-two-block-exclusion, proportional-slope-two-block-bound, mechanical-cycles-high-rational-controls]
evidence:
  - "../equal-total-two-block-exclusion/PROPORTIONAL.md, section 4: the written proof"
  - "../equal-total-two-block-exclusion/two_blocks_audit.json: 590 rotating-mechanical examples, including block lengths 256 and 512 (historical receipt)"
  - "../equal-total-two-block-exclusion/c002_two_block_check.py, part (4): side-lane numerical check"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-19
    scope: "Feed 2026-10-19 00:26, REFEREE C002: for 13 <= m <= 30 and k, ℓ <= 3, the word is primitive, every rational state exceeds m/12, and den > 1 once k + ℓ >= 3 (numerical check)"
    link: ../../../archive/side-lane/FEED.md
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Feed 00:26, update 00:31: the Lean lane re-derived PROPORTIONAL.md sections 1-4 by hand and found no error. Not formalised (queued under C002-b)"
    link: ../../../archive/side-lane/FEED.md
tags: [cycles, mechanical-words, two-blocks, local-minima, clocks]
---

# Mechanical block and its rotation: u_m^k v_m^ℓ has growing minima and no denominator 1

## Statement

Fix `m ≥ 13`, `V = 3^m`, `A = bit_length(V) = ceil(m·log₂3)`, `U = 2^A`, `Δ = U − V`. Let `u = u_m` be the lower mechanical word `a_i = floor((i+1)A/m) − floor(iA/m)` and `v = v_m = (a_1, …, a_(m−1), a_0)` its one-letter left rotation (same length and total). For `k, ℓ ≥ 1` put `w = u^k v^ℓ`, `n = k + ℓ`, `h = gcd(k, ℓ)`. Then `D_w = U^n − V^n > 0` and:

1. **Height at every phase:** every state of the rational cycle of `w` exceeds `m/12 > 1`, for all `k, ℓ ≥ 1`, with no separation condition.
2. **Denominator:** if `n ≥ 3`, `den(w) > U^(n−h)/J > 3·V^(n−h−1)/(2m) > 1`, where `J = C_v − C_u = (C_u + Δ)/2`.
3. **Primitivity and nonbalance:** `w` is primitive for every `k, ℓ ≥ 1`, is not a mechanical word, and its shortcut parity word is not Christoffel-balanced.
4. **Local minima:**

| Clock | Count |
| --- | ---: |
| Odd-only Syracuse | `n(2m − A) − 1` |
| Shortcut Collatz | `n(A − m)` |

Both counts and the rational minimum grow without bound with `m`, with `k, ℓ` free subject to `n ≥ 3` for claim 2.

## Proof

Written proof: `PROPORTIONAL.md` §4 in [`equal-total-two-block-exclusion`](equal-total-two-block-exclusion/README.md) ([file](equal-total-two-block-exclusion/PROPORTIONAL.md)). Outline:

- R71 ([`mechanical-cycles-high-rational-controls`](mechanical-cycles-high-rational-controls/README.md)) gives every state of either pure cycle above `m/6`. With `x_u = C_u/Δ`, `x_v = C_v/Δ` and first letter `a_0 = 1`, `x_v = (3x_u + 1)/2`, so `x_u < x_v < 2x_u` and `x_u > m/6 > 1`.
- Both block maps have slope `q = V/U < 1`. The return equations give `x = x_u + (x_v − x_u)(1 − z)/(1 − tz)` for the state before the first `u` (`t = q^k`, `z = q^ℓ`), so `x_u < x, y < x_v`, and every intermediate block start lies in `(x_u, x_v)`. A prefix of `u` from a start above `x_u` exceeds the corresponding pure-`u` state, hence `m/6`; a prefix of `v` starts above `x_u > x_v/2` and exceeds half the corresponding pure-`v` state, hence `m/12`. A rotated prefix need not itself have slope above one-half; the argument compares its input with half its own pure-cycle input and uses a positive affine map.
- Rotation gives `J = C_v − C_u = (C_u + Δ)/2 > 0`; R71's term estimate gives `C_u < (2m/3)V`, and `x_u > 1` gives `C_u > Δ`, so `J < C_u < (2m/3)V`. In the reduced notation of [`proportional-slope-two-block-bound`](proportional-slope-two-block-bound.md) (`c_0 = gcd(A, m)`, `r = s = c_0`), its `U_base^(L−h_theorem)` is the full-block `U^(n−h)`; for `n ≥ 3`, `n − h ≥ 2` and (7) yields claim 2.
- `3/2 < A/m < 27/17 + 1/13 < 5/3`. `u` begins `(1,2,1,2)`, ends `(1,2,2)`, has no cyclic `(1,1)` or `(2,2,2)`; `v` begins `(2,1,2)` and ends `(2,2,1)`. In `w` the `u`-to-`v` boundary creates exactly one cyclic `(2,2,2)` and the `v`-to-`u` boundary exactly one cyclic `(1,1)`; the unique `(2,2,2)` proves primitivity. Factors `(1,2,1)` and `(2,2,2)` (sums 4 and 6) exclude mechanical; shortcut factors `11011` and `01010` exclude balance.
- All states exceed 1, so valuation-1 odd steps increase and valuation-2 steps decrease; each block has `2m − A` letters 1 and exactly one cyclic pair of 1s merges two increasing runs, giving `n(2m − A) − 1`; in the shortcut clock each valuation-2 block contributes one even descent, giving `n(A − m)`.

## Remarks

- **Clocks.** The two counts use different clocks and must not be exchanged.
- **Scope.** A primitive, unbalanced rational family with growing minima and a varying denominator, not a fixed-`d` counterexample. It exceeds any fixed local-minimum-count cutoff and lies outside the direct balanced/Christoffel hypotheses examined in the C001 literature audit; it does not improve a general published record, and no novelty is claimed.
- **Dependency.** The proof uses R71's mechanical size bound and term estimate, [`mechanical-cycles-high-rational-controls`](mechanical-cycles-high-rational-controls/README.md) (legacy `BALANCED_DENOMINATORS.md` §3); linked at the B12 migration.
- The one-block analogue is [`perturbed-mechanical-block-family`](perturbed-mechanical-block-family.md).

## History

- Split from `experiments/cycle_spectrum/C002/` (legacy ID `C002`; `REPORT.md` §4, `PROPORTIONAL.md` §4) at commit `be73a66`, by the B03 migration (Claude, Opus 5.5). Main lane (ChatGPT/Codex), 2026-10-19.
- Corrected before delivery: the rotating family first used full block totals where the reduced exponents `c_0 = gcd(A, m)` were needed; the repaired text translates the reduced exponents back to full block powers.
