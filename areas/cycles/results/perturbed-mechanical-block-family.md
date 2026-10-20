---
id: perturbed-mechanical-block-family
kind: result
title: A primitive nonbalanced family u_m^k (2) with growing minima and denominator above 1
status: reviewed
claim: >
  Raw odd-only clock, no absorption. For m ≥ 13 let A = bit length of 3^m (= ceil(m·log₂3)) and
  u_m the lower mechanical word a_i = floor((i+1)A/m) − floor(iA/m). For every k ≥ 2 the word
  w = u_m^k (2) has D_w > 0, is primitive (also up to rotation), is not a rotation of a mechanical
  word, has an unbalanced shortcut parity word, and satisfies den(w) > 3·(3^m)^(k−1)/(2m) > 1.
  If moreover 2^(kA) ≥ 2·3^(km) (e.g. k ≥ ceil(3^m/(2^A − 3^m))), every state of its rational
  cycle exceeds m/10, it has k(2m − A) odd-only local minima and k(A − m) + 1 shortcut local
  minima.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: [repeated-block-cancellation-bound]
evidence:
  - "../repeated-block-cancellation-bound/REPETITION_SPECTRUM.md, section 3: the written proof"
  - "../repeated-block-cancellation-bound/LITERATURE.md, section 4: independent audit of the family"
  - "../repeated-block-cancellation-bound/spectrum_audit.json: 306 perturbed mechanical examples with m through 128, plus 256 and 512 (receipt of check_spectrum.py)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-19
    scope: "Side-lane feed (legacy archive/side_lane/FEED.md), entry 2026-10-19 00:18, REFEREE C001: w = u_m^k 2 is primitive and den(w) > 3·(3^m)^(k−1)/(2m) for all 192 pairs 13 <= m <= 60, 2 <= k <= 5 (c001_spectrum_check.py part 4); the batch judged correct. The height and local-minimum statements were not separately re-derived there"
tags: [cycles, mechanical-words, high-cycles, local-minima, clocks]
---

# A primitive nonbalanced family u_m^k (2) with growing minima and denominator above 1

## Statement

For `m ≥ 13` set `V = 3^m`, `A = bit_length(V) = ceil(m·log₂3)`, `U = 2^A`, `Δ = U − V`, and let `u_m = (a_0, …, a_(m−1))` with `a_i = floor((i+1)A/m) − floor(iA/m)`, the lower mechanical valuation word of length `m` and total `A` (R71's mechanical word). For `k ≥ 2` put `w = w_(m,k) = u_m^k (2)`.

1. **Denominator.** `D_w > 0` and `den(w) > 3·V^(k−1)/(2m) > 1`. No word in this family is a nontrivial `d = 1` integer cycle.
2. **Primitive and outside the balanced family.** `w` is primitive, including up to cyclic rotation; it is not a rotation of a mechanical word; its shortcut parity word is not balanced (not Christoffel).
3. **Heights**, under the extra condition `U^k ≥ 2·V^k` (10), for which `k ≥ ceil(V/Δ)` suffices: every state of the rational cycle exceeds `m/10 > 1`.
4. **Local minima**, under (10):

| Clock | Number of local minima |
|---|---:|
| Odd-only Syracuse | `k(2m − A)` |
| Shortcut Collatz, as in the cited cycle records | `k(A − m) + 1` |

Both the minimum and the shortcut count exceed any fixed cutoff as `m` grows (with `k` chosen by (10)).

## Proof

The written proof is [`REPETITION_SPECTRUM.md`](repeated-block-cancellation-bound/REPETITION_SPECTRUM.md) §3, in the folder of [`repeated-block-cancellation-bound`](repeated-block-cancellation-bound/README.md). Outline:

- **Denominator.** Here `K = Δ − C(u_m) < 0`. Each summand of `C(u_m)` is below `2·3^(m−1)`, because `2^floor(jA/m) ≤ 2^(jA/m) ≤ 3^j·2^(j/m) < 2·3^j`. So `C(u_m) < (2m/3)·V` and `|K| < (2m/3)·V < V²`, while `D_w = 4U^k − 3V^k > V^k ≥ V²`. The bound `den ≥ D_w/|K|` of [`repeated-block-cancellation-bound`](repeated-block-cancellation-bound/README.md) gives claim 1.
- **Heights.** The affine map of `u_m` has slope `q = V/U < 1` and fixed point `x_0 = C(u_m)/Δ`; R71 gives `x_0 > m/6 > 1` (every state of the mechanical cycle exceeds `m/6`). With `t = q^k ≤ 1/2`, the state after the appended 2 is `x = [3x_0(1 − t) + 1]/(4 − 3t)`, so `1 < x < x_0` and `x/x_0 > 3(1 − t)/(4 − 3t) ≥ 3/5`. Block starts move monotonically toward `x_0`, and every prefix map of `u_m` has positive slope and nonnegative intercept, so every state is at least 3/5 of the corresponding pure-`u_m` state: every state exceeds `m/10`.
- **Primitivity and nonbalance.** From `3² > 2³` and `3^17 < 2^27`, `3/2 < A/m < 27/17 + 1/13 = 368/221 < 5/3`. So `u_m` begins `(1,2,1,2)`, ends `(2,2)`, has no cyclic `(1,1)` and no cyclic `(2,2,2)`. Appending `(2)` creates exactly one cyclic `(2,2,2)`, so `w` is primitive. It contains `(1,2,1)` (sum 4) and `(2,2,2)` (sum 6), so it is not mechanical. In the shortcut parity encoding the factors give `11011` (four ones in five positions) and `01010` (two), so the parity word is unbalanced.
- **Local minima.** All states exceed 1, so valuation-1 odd steps increase and valuation-2 steps decrease; the 1s are isolated, giving `k(2m − A)` odd-only minima. In the shortcut clock each valuation-2 block has one even step and the next odd state is a local minimum, giving `k(A − m) + 1`.

## Remarks

- **Clocks.** The two clocks give different counts and must not be interchanged when using published local-minimum bounds.
- **Scope.** This is a rational, varying-`d` control family, not a fixed-`d` counterexample; its reduced denominator also grows. It lies outside R71's mechanical class and the Christoffel class of [`knight-2026-high-cycles`](../../../sources/knight-2026-high-cycles.md), and outside the direct hypotheses of fixed-minimum-count records ([`simons-2005-m-cycles`](../../../sources/simons-2005-m-cycles.md), [`hercher-2023-cycle-length`](../../../sources/hercher-2023-cycle-length.md)). It is not a claim to have improved the general 91-minimum bound, nor a claim that the family is absent from earlier literature. No claim about all nonbalanced words follows. Novelty undetermined.
- **Dependency not yet linked.** The proof uses R71's mechanical-word size bound (every state of the mechanical cycle exceeds `m/6`); R71 is legacy `experiments/residual_progress/lattice_cycles/BALANCED_DENOMINATORS.md` §3, not yet migrated, so it is not listed under `depends_on`.
- The analogous two-block family is [`rotating-mechanical-two-block-family`](rotating-mechanical-two-block-family.md).

## History

- Split from `experiments/cycle_spectrum/C001/` (legacy ID `C001`, `REPORT.md` §2 and `REPETITION_SPECTRUM.md` §3) at commit `be73a66`, by the B03 migration (Claude, Opus 5.5). Main lane (ChatGPT/Codex), 2026-10-19.
- During derivation an overly optimistic three-quarters height comparison was discarded before adoption; the proved three-fifths comparison keeps the extra exponent condition (10). Review separated the all-`k ≥ 2` denominator and primitivity statements from the height and local-minimum statements, which need (10).
