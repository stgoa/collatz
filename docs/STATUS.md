# Status

*Last updated: 2026-10-19, at the restructure. This is the single place for the current standing. Update it only when the headline changes.*

**The Collatz conjecture is open, and nothing in this repository claims otherwise.** The repository holds scoped theorems, exact computations, formal proofs and documented failed approaches. Most current work concerns the **cycle half**: showing that `3x+1` has no nontrivial cycle. The questions are put in terms of the reduced denominator `den(w)` of a valuation word, defined in [`CONVENTIONS.md`](CONVENTIONS.md) §2.

Status labels follow [`AGENTS.md`](../AGENTS.md) §4.

## Headline results on cycles

| Result | Statement (scoped) | Status | Where |
|---|---|---|---|
| Narrow cycles | Every nontrivial positive integer cycle of `3x+1` has a state above twice its minimum (`H > 2L`). Proof: `H < 2L` forces a mechanical (Christoffel) word, and mechanical words are never integer cycles. | `formal` | C004, R71; `lean/` units C004-b/c/d and R71-a |
| Rotation distance `ρ ≥ 3` | No nontrivial cycle's word differs from a nonidentity rotation in exactly two places. | `written` (C011, conditional on Matveev and the period bound); `formal` via S06, conditional on EXT-1, for `m ≥ 24,891` and minimum `> 2^71` | `experiments/cycle_spectrum/C011/`, `S06/` |
| Rotation distance `ρ ≥ 4` | No nontrivial cycle's word differs from a nonidentity rotation in exactly three places. | `formal`, conditional on EXT-1, for `m ≥ 2^19` and minimum `≥ 2^20` (both implied by the period and minimum bounds) | `experiments/cycle_spectrum/S07/`; Lean `four_le_mis_card_of_gap` |
| Height–mismatch link | Every rotation has `s > log₂3·m/(B + 342·log₂m + 172)`. A height bound `B = o(m)` would force `ρ → ∞`. | `formal`, conditional on EXT-1 | `experiments/cycle_spectrum/S05/` |
| Denjoy–Koksma height bound | `B ≤ (K(h/m) − 1)·(V_h + 2δ)` for every rotation `h` coprime to `m`, plus a denominator law for any mismatch count | `formal`, no external input | `experiments/cycle_spectrum/S12/` |
| Rise lemma | Each agreeing run of a rotation multiplies the log-height by at most `log₂3`. Hence short rotations (`|h|_m ≤ m^(1−θ)`) have at least about `1.5·θ·log₂m` mismatches. | Lemma: `formal`. Numerical consequences: `conditional` on EXT-1. | `experiments/cycle_spectrum/S13/` |
| Reduction to the largest letter | `ρ → ∞` follows from a sublinear bound `o(m)` on the largest valuation of a cycle. This is weaker than `B = o(m)`. | Mechanism: `formal`. Thresholds: `conditional` on EXT-1. | `experiments/cycle_spectrum/S13/` (Corollaries 6–7) |
| Two-block words | Different equal-total blocks `u, v` with `u^k v^ℓ`, `k + ℓ ≥ 3`, never give an integer cycle, and their denominator exceeds `2^m`. Proportional-slope blocks get explicit denominator growth. | `written`; the proportional-slope theorem (6)–(8) is `formal` (C002-b, parts 1–2) | `experiments/cycle_spectrum/C002/`, `C003/` |
| Shared background with markers | Any word built from one repeated background and nonconstant markers has a denominator that grows; bounded-denominator layers are effectively finite. | `written`. Uses Matveev; the variant using EXT-1 is S11. | `experiments/cycle_spectrum/C013/`, `S11/` |
| Mechanical phase languages | Concatenations of rotations of one mechanical word are never integer cycles, except for the base `(2)`. | `written`; core units `formal` (C005-a…h) | `experiments/cycle_spectrum/C005/` |
| Ordered cycles | In an ordered cycle, few changes of dyadic height force large gaps. At fixed `q`, the number `J` of height changes satisfies `J ≥ √m − O(log m)`. | `written`, using a classical two-logarithm bound; units `formal` (C006-a…f, one conditional on the gap) | `experiments/cycle_spectrum/C006/` |

## The objective, and how far it is

The active intermediate target ([`experiments/cycle_spectrum/BRIEF.md`](../experiments/cycle_spectrum/BRIEF.md)): find an explicit `F(m) → ∞` such that every hypothetical nontrivial integer cycle of period `m` differs from each nonidentity rotation in at least `F(m)` places.

| Rotations | What is known |
|---|---|
| All rotations | `ρ ≥ 4` (`formal`, conditional on EXT-1) |
| Short rotations, `|h|_m = o(m)` | Mismatch counts grow like `log m` (S13) |
| Long rotations, `|h|_m ≥ m/10` | Only the constant bound is known |

The exact obstruction at long rotations is a tall profile with one huge single-step drop: a valuation of size `εm`. Rotations with at most `S` mismatches are rare (at most 156 with `S = 4` at `m = 1.375·10^11`), and each one forces such a letter.

[`FRONTIER.md`](FRONTIER.md) lists the open targets.

## Other programmes (finished or paused)

| Programme | Outcome | Status |
|---|---|---|
| Packet currents (R1–R94) | Collatz convergence reduced to finite signed "current" certificates on five rays; many partial constructions and exact obstructions. Universal certificate supply is unresolved. | Frozen |
| Phase 6 (route map) | Calibrations and barriers for named proof obligations, plus an independent audit of an external positive-density Lean development | Finished |
| Viewpoints (V001–V009) | Every binary-automatic Collatz-invariant colouring is constant (V004). This is `formal`, with Cobham's theorem as a named hypothesis. The quantitative target is unresolved. | Finished |
| Explicit Tao | Making Tao (2019) explicit: Leg 1 closed as a scoped barrier | Closed |

The full list, with links, is in [`RESULTS.md`](RESULTS.md).

## What this repository does not claim

- No proof of the Collatz conjecture, of the cycle half, or of the absence of divergent orbits.
- No novelty for any result unless its folder says so after a literature check. Most say "novelty undetermined".
- External inputs are not proved here ([`CONVENTIONS.md`](CONVENTIONS.md) §5). Every result that uses them is marked `conditional`.
