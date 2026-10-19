# Frontier: where to push

These are open targets, ordered by how directly they advance the active goal. Each entry gives the precise statement, why it matters, the known obstruction, and where to start. Claim a target by opening an issue (*Research proposal* template) or by sending a PR. See [`CONTRIBUTING.md`](../CONTRIBUTING.md).

The active goal is the cycle half: no nontrivial cycle of `3x+1`. Its intermediate target is a rotation distance `ρ(w) ≥ F(m) → ∞` for every hypothetical cycle word, defined in [`CONVENTIONS.md`](CONVENTIONS.md) §2. The current standing is in [`STATUS.md`](STATUS.md).

## 1. A sublinear bound on the largest valuation

- **Target.** Prove that every nontrivial cycle of `3x+1` with period `m` has all valuations `a_i = v₂(3n_i+1) ≤ f(m)` with `f(m) = o(m)`. Then `ρ → ∞`. With `f(m) ≤ m^(1−ε)`, `ρ ≥ (ε − o(1))·log_{log₂3} m`.
- **Why.** [S13](../experiments/cycle_spectrum/S13/RISE_LEMMA.md), Corollaries 6–7, shows that a rotation with at most `S` mismatches forces a letter of size `≥ c_S·m`, e.g. `c_4 ≈ 0.022`. So, given EXT-1, a sublinear letter bound alone would reach the intermediate target.
- **Known.** Only `a_max ≤ B + log₂L + 2 ≤ 0.585m + O(log m)`.
- **Obstruction.** A tall profile with one single-step drop of `εm` bits is consistent with every size constraint known here. Excluding it needs arithmetic: the drop requires the orbit of the post-drop element `L'` to land exactly on `(2^V L' − 1)/3`.
- **Start with:**
  - S13 §§1–4;
  - [S10](../experiments/cycle_spectrum/S10/MULTI_ROTATION.md), for the shape of the surviving configurations;
  - [`lean/STATE.md`](../lean/STATE.md) units S13-a…d.

## 2. `ρ ≥ 5`: no rotation with exactly four mismatches

- **Target.** Exclude 4-mismatch rotations for `q = 1` cycles.
- **Known.**
  - [S07](../experiments/cycle_spectrum/S07/THREE_MISMATCHES.md) gives `ρ ≥ 4` (`formal`, conditional on EXT-1).
  - S13 shows a 4-mismatch rotation needs `|h|_m ≥ 0.075m` and a letter `≥ 0.022m`.
  - At most 156 such rotations can exist at `m = 1.375·10^11`.
- **Obstruction.** In S10's model, the `v₂ ≠ v₄` pattern survives size constraints from rotations `h, …, 8h` with margins shrinking towards 0. Exact certificates (Farkas multipliers per cell), finite-`m` handling, and the slope cost of letters `≥ 3` are listed in S10 §6.
- **Start with:** S10, S07 and S13.

## 3. A height bound `B = o(m)`

- **Target.** Bound the log-height `B = log₂(H/L)` of every `q = 1` cycle by `o(m)`.
- **Why.** [S05](../experiments/cycle_spectrum/S05/MISMATCH_HEIGHT.md) then gives `ρ ≳ m/(B + 342·log₂ m)`. In particular `B = O(log m)` gives the brief's stronger `m/log m` payoff.
- **Obstruction.** Size methods cannot rule out tall profiles; see S08–S10 and S13 §4.
- **Heuristic (labelled).** Actual `3x+q` cycles look like random bridges, with `B ~ √m`.

## 4. Uniform denominator estimates for many mismatches

- **Target.** One denominator estimate valid for an arbitrary mismatch count that retains the coupling between distinct overlapping arcs.
- **Known.**
  - [C011](../experiments/cycle_spectrum/C011/REPORT.md) does two mismatches by arc arithmetic.
  - [C012](../experiments/cycle_spectrum/C012/REPORT.md) and [C013](../experiments/cycle_spectrum/C013/REPORT.md) record what fails beyond.
  - The product of arc relations works for three mismatches only when the amplitude is small. Its base drops below 1 at four mismatches.
- **Start with:**
  - C011–C013;
  - [C014](../experiments/cycle_spectrum/C014/COMPATIBLE_ARCS.md), which is unreviewed work in progress. Reviewing and completing it is itself a contribution.

## 5. The ordered-cycle class

- **Target** (from the brief). Every nontrivial primitive positive rational cycle whose normalised successor preserves circular order has reduced denominator `> 1`. There is no bound on period, height or height-change count.
- **Start with:**
  - [C005](../experiments/cycle_spectrum/C005/REPORT.md)–[C010](../experiments/cycle_spectrum/C010/REPORT.md);
  - the controls `q = 5` and `q = 233`.

## 6. Formalisation queue (Lean)

All items are listed in [`lean/STATE.md`](../lean/STATE.md):
- C001-c;
- C002-b's list packaging and denominator invariance;
- the `(1,1,2)` window theorem (S10);
- V007-b and V008-a;
- the numerical corollaries of S13, together with EXT-1;
- a self-contained proof of EXT-1 (currently replayed, not ours).

## 7. Other open lines

- **Explicit Tao, Legs 2–3** ([`experiments/explicit_tao/`](../experiments/explicit_tao/STATE.md)): fill the `C(δ)` table.
- **Packet currents** ([`experiments/residual_progress/REPORT.md`](../experiments/residual_progress/REPORT.md)): universal terminal supply of current certificates. The line is frozen; new attempts should cite R94 and start a new folder.
- **Viewpoints:** the quantitative unbounded-ratio target ([brief](../experiments/viewpoints/briefs/QUANTITATIVE_RIGIDITY_BRIEF.md)) is unresolved.

## Reviews wanted

Independent reviews are as valuable as new results. These written results have no independent human review:
- the C-series (some batches carry agent reviews in their folders, e.g. C003 and C011);
- S11;
- the corollaries of S13;
- V004's d-uniform extension.

Re-deriving them independently, with new code where computation is involved, is welcome.

See the review playbook in [`CONTRIBUTING.md`](../CONTRIBUTING.md).
