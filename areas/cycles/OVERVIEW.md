# Cycles

**The question.** Does the Collatz map `3x+1` have a cycle other than the trivial one, `1 → 4 → 2 → 1`? Nothing here answers it. The nodes are scoped theorems, exact computations and documented failures; the status of each is in [`MAP.md`](../../MAP.md).

**The approach.** A candidate cycle of the odd-only map is encoded by its word of valuations (letters) `w = (a_0, …, a_(m−1))`. The word has a rational cycle point `C_w/D_w` with `D_w = 2^A − 3^m`, and it is an integer cycle of `3x+d` exactly when its reduced denominator `den(w)` divides `d` ([`conventions/NOTATION.md`](../../conventions/NOTATION.md) §2). The cycle half of Collatz is the statement that `den(w) = 1` only for repetitions of `(2)`. The work studies that denominator across the whole `3x+d` family, where actual cycles exist and serve as controls ([`actual-cycles-3x-d-corpus`](results/actual-cycles-3x-d-corpus/README.md)), and asks how far a cycle word can be from periodic. The intermediate target is a growing **rotation distance**: every hypothetical cycle word differs from each of its nonidentity rotations in at least `F(m) → ∞` positions ([`rotation-distance-growth`](questions/rotation-distance-growth.md)).

**Who did what.** The C-series (C001–C014) came from the main lane (ChatGPT/Codex); the S-series (S1–S13) from the Claude side lane, which also refereed the C-series; most units were then formalised by the Claude Lean lane (Fable) in `lean/CycleSpectrum.lean`. Many results rest on external inputs, listed under `assumes` and in MAP.md's "Rests on" column: above all the replayed linear-form gap EXT-1 ([`musson-collatz-gap-all`](../../sources/musson-collatz-gap-all.md)), the period bound ([`hercher-2023-cycle-length`](../../sources/hercher-2023-cycle-length.md)) with the convergence verification ([`barina-2025-convergence-2-71`](../../sources/barina-2025-convergence-2-71.md)), and Matveev's bound ([`matveev-2000-linear-forms`](../../sources/matveev-2000-linear-forms.md)).

## The main lines

### 1. Block words: repeated and two-block words (C001–C003, C005)

Words built from few repeated blocks have denominators that grow, so they cannot be integer cycles.
- A fixed perturbation bounds the cancellation of repeated blocks ([`repeated-block-cancellation-bound`](results/repeated-block-cancellation-bound/README.md), reviewed), but two unit defects can cancel arbitrarily much ([`fixed-defect-unbounded-cancellation`](results/fixed-defect-unbounded-cancellation.md)).
- Two different equal-total blocks `u^k v^ℓ` (`k + ℓ ≥ 3`) are never integer cycles ([`equal-total-two-block-exclusion`](results/equal-total-two-block-exclusion/README.md), formal); contracting and proportional-slope two-block words get explicit bounds ([`contracting-two-block-effective-exclusion`](results/contracting-two-block-effective-exclusion/README.md), [`proportional-slope-two-block-bound`](results/proportional-slope-two-block-bound.md), formal); unequal slopes and general two-block words get growth only ineffectively, from Corvaja–Zannier ([`unequal-slope-two-block-growth`](results/unequal-slope-two-block-growth/README.md), [`two-block-uniform-denominator-growth`](results/two-block-uniform-denominator-growth/README.md)).
- Concatenations of rotations of one mechanical word are never integer cycles ([`rotation-block-exclusion`](results/rotation-block-exclusion/README.md), formal).
- One background repeated between nonconstant markers forces denominator growth ([`shared-background-denominator-law`](results/shared-background-denominator-law/README.md), reviewed, Matveev); with EXT-1 instead, a `q = 1` cycle of that shape needs tens of thousands of background copies at the imported period ([`shared-background-copies-via-gap`](results/shared-background-copies-via-gap/README.md), written).

### 2. Narrow and ordered cycles (C004–C010, S1–S4)

- **Narrow cycles.** A cycle with `H < 2L` is exactly a mechanical word, so every nontrivial `3x+1` cycle has `H > 2L` ([`narrow-cycles-are-mechanical`](results/narrow-cycles-are-mechanical/README.md), formal; it uses the mechanical exclusion R71 of the residual-progress material). The narrow subfamily of `3x+d` is classified ([`narrow-cycle-spectrum-law`](results/narrow-cycle-spectrum-law.md)); a `3x+1` cycle with `H < 8L` is dyadically ordered ([`three-band-collatz-cycles-are-ordered`](results/three-band-collatz-cycles-are-ordered.md), formal).
- **Ordered cycles** (normalised successor preserves circular order) are the next class. The tools: the dyadic order lemma ([`dyadic-order-lemma`](results/dyadic-order-lemma.md)), closed forms for the sorted gaps ([`ordered-gap-closed-form`](results/ordered-gap-closed-form/README.md), [`complete-gap-lattice-equivalence`](results/complete-gap-lattice-equivalence.md)), residue laws ([`ordered-cycle-residue-law`](results/ordered-cycle-residue-law.md), [`ordered-cycle-sorted-rank-residues`](results/ordered-cycle-sorted-rank-residues/README.md)), and sparse forcing: few height changes force a huge minimum ([`ordered-cycle-sparse-forcing`](results/ordered-cycle-sparse-forcing/README.md), formal; growth `J ≥ √m − O_q(log m)` in [`ordered-cycle-height-change-growth`](results/ordered-cycle-height-change-growth.md), with a two-logarithm bound). The class itself is open ([`ordered-cycle-denominator-one`](questions/ordered-cycle-denominator-one.md)).

### 3. Rotation distance and mismatches (C011–C013, S5–S13)

The rotation distance `ρ(w)` is the least number of positions in which `w` differs from a nonidentity rotation.
- **`ρ ≥ 3`.** No rotation differs in exactly two positions: [`two-defect-rotation-exclusion`](results/two-defect-rotation-exclusion/README.md) (reviewed; Matveev and the period bound) and, from EXT-1 instead of Matveev, [`two-mismatch-exclusion-via-gap`](results/two-mismatch-exclusion-via-gap/README.md) (formal).
- **`ρ ≥ 4`.** No rotation differs in exactly three positions, for `m ≥ 2^19` and `L ≥ 2^20` given EXT-1: [`three-mismatch-exclusion`](results/three-mismatch-exclusion/README.md) (formal); with the period and minimum imports this covers every hypothetical nontrivial cycle.
- **The same steps at every `q`** become denominator laws for two- and three-mismatch words, through the global-drift ceiling ([`global-drift-ceiling`](results/global-drift-ceiling.md), [`two-three-mismatch-denominator-laws`](results/two-three-mismatch-denominator-laws/README.md), both formal, no external input). A repeated factor of a cycle word is a rotation run, so no long factor repeats ([`cycle-word-repeat-bound`](results/cycle-word-repeat-bound/README.md), written).
- **Short rotations.** The rise lemma ([`rise-lemma`](results/rise-lemma/README.md), formal) says each agreeing run multiplies the log-height by at most `log₂3`. With EXT-1, rotations with `|h|_m ≤ m^(1−θ)` have about `1.5·θ·log₂ m` mismatches, and few-mismatch rotations are long and rare ([`short-rotation-mismatch-growth`](results/short-rotation-mismatch-growth/README.md), reviewed). Its word form is a third denominator law ([`rise-lemma-denominator-law`](results/rise-lemma-denominator-law.md), reviewed).
- **The reduction to the largest letter.** A rotation with at most `S` mismatches forces a letter of linear size, so `ρ → ∞` would follow from a largest letter of size `o(m)` ([`largest-letter-rho-reduction`](results/largest-letter-rho-reduction.md), reviewed; mechanism formal, thresholds conditional on EXT-1).
- The sign structure of a four-mismatch rotation is formal ([`four-mismatch-sign-dichotomy`](results/four-mismatch-sign-dichotomy.md)); the exclusion of four mismatches is open.

### 4. Height bounds

The log-height `B = log₂(H/L)` links the lines: by the mismatch–height trade-off ([`mismatch-height-tradeoff`](results/mismatch-height-tradeoff/README.md), formal given EXT-1) every rotation has more than `log₂3·m/(B + 342·log₂ m + 172)` mismatches, so `B = o(m)` would give `ρ → ∞`.
- Known: the ceiling `B ≲ 0.585m` ([`cycle-height-ceiling`](results/cycle-height-ceiling.md), formal) and its drift form at every `q` ([`global-drift-ceiling`](results/global-drift-ceiling.md)).
- The Denjoy–Koksma bound `B ≤ (K(h/m) − 1)·(V_h + 2δ)` for every coprime rotation ([`denjoy-koksma-height-bound`](results/denjoy-koksma-height-bound/README.md), formal, no external input) and its denominator law for any mismatch count ([`denjoy-koksma-denominator-law`](results/denjoy-koksma-denominator-law/README.md), formal). Both are silent on tall sawtooth cycles, whose drop sits at a mismatch.
- Bounded rotation distance alone does not bound the height of rational cycles ([`distance-three-height-family`](results/distance-three-height-family.md)): a height bound must use `q = 1` arithmetic.
- For ordered cycles, the candidate `B ≤ q − 1` ([`height-denominator-candidate`](questions/height-denominator-candidate/README.md)) holds on a bounded census ([`ordered-cycle-height-census`](results/ordered-cycle-height-census.md)).

## Strongest results

| Result | Status | Rests on |
|---|---|---|
| Every nontrivial `3x+1` cycle has `H > 2L` ([`narrow-cycles-are-mechanical`](results/narrow-cycles-are-mechanical/README.md)) | formal | nothing external |
| `ρ ≥ 4` ([`three-mismatch-exclusion`](results/three-mismatch-exclusion/README.md)) | formal | EXT-1; period and minimum bounds for the applied form |
| Mismatch–height trade-off ([`mismatch-height-tradeoff`](results/mismatch-height-tradeoff/README.md)) | formal | EXT-1 |
| Denjoy–Koksma height bound ([`denjoy-koksma-height-bound`](results/denjoy-koksma-height-bound/README.md)) | formal | nothing external |
| Rise lemma ([`rise-lemma`](results/rise-lemma/README.md)) | formal | nothing external |
| Short-rotation growth ([`short-rotation-mismatch-growth`](results/short-rotation-mismatch-growth/README.md)) | reviewed | EXT-1 |
| Reduction to the largest letter ([`largest-letter-rho-reduction`](results/largest-letter-rho-reduction.md)) | reviewed | EXT-1 (and S7's imports for `ρ ≥ 5`) |
| Two-block exclusion ([`equal-total-two-block-exclusion`](results/equal-total-two-block-exclusion/README.md)) | formal | nothing external |
| Denominator laws at every `q` ([`two-three-mismatch-denominator-laws`](results/two-three-mismatch-denominator-laws/README.md)) | formal | nothing external |

## Open questions

- [`rotation-distance-growth`](questions/rotation-distance-growth.md): an explicit `F(m) → ∞` with `ρ(w) ≥ F(m)`. The intermediate target.
- [`largest-letter-sublinear`](questions/largest-letter-sublinear.md): is the largest letter `o(m)`? Given EXT-1, enough for `ρ → ∞`; the tall tooth with one huge drop is the obstruction.
- [`cycle-height-bound`](questions/cycle-height-bound.md): is the height `B = o(m)`? A stronger sufficient condition.
- [`rotation-distance-at-least-5`](questions/rotation-distance-at-least-5.md): exclude four-mismatch rotations.
- [`rotation-defect-denominator-candidate`](questions/rotation-defect-denominator-candidate.md): a uniform denominator estimate for many mismatches.
- Ordered cycles: [`ordered-cycle-denominator-one`](questions/ordered-cycle-denominator-one.md), [`height-denominator-candidate`](questions/height-denominator-candidate/README.md), [`height-residue-hall-matching`](questions/height-residue-hall-matching.md), [`one-height-defect-ordered-cycles`](questions/one-height-defect-ordered-cycles.md).

## Dead ends

Each attempt says exactly why it fails and what survives.
- **Size inequalities stop near four mismatches.** S8's claimed limit was withdrawn ([`four-mismatch-size-method-limit`](attempts/four-mismatch-size-method-limit/README.md)); with several rotations at once the method reaches at most `ρ ≥ 5` ([`multi-rotation-four-mismatch-exclusion`](attempts/multi-rotation-four-mismatch-exclusion/README.md), paused).
- **Block words.** A constant cancellation bound for two growing blocks ([`constant-cancellation-two-growing-blocks`](attempts/constant-cancellation-two-growing-blocks.md)) and interval trapping of block starts ([`interval-trapping-expanding-blocks`](attempts/interval-trapping-expanding-blocks.md)).
- **Shortcuts to many mismatches.** Dividing prefix plateaus termwise ([`termwise-plateau-divisibility`](attempts/termwise-plateau-divisibility.md)); a universal close pair ([`close-pair-lattice-criterion`](attempts/close-pair-lattice-criterion/README.md)). The unreviewed C014 drafts record limits of common partitions and resultants ([`compatible-arcs-common-partition-limits`](results/compatible-arcs-common-partition-limits/README.md), [`rotated-residual-resultant-invariance`](results/rotated-residual-resultant-invariance.md)).
- **Ordered cycles.** Excursion compression ([`excursion-compression`](attempts/excursion-compression/README.md)), local odd rounding ([`local-odd-rounding-exclusion`](attempts/local-odd-rounding-exclusion/README.md)), run renormalisation ([`ordered-cycle-run-renormalisation`](attempts/ordered-cycle-run-renormalisation/README.md)), four further shortcuts ([`ordered-cycle-shortcuts`](attempts/ordered-cycle-shortcuts.md)), a mechanical normalised-word transfer ([`mechanical-normalized-word-transfer`](attempts/mechanical-normalized-word-transfer.md)), and extending the ordering to `H < 16L` ([`band-three-ordering-extension`](attempts/band-three-ordering-extension/README.md)).
- **Height and gcd laws.** Proving `B ≤ q − 1` from residues or relaxations ([`height-bound-via-residues-or-relaxation`](attempts/height-bound-via-residues-or-relaxation.md)), primewise matching ([`primewise-height-residue-matching`](attempts/primewise-height-residue-matching.md)), and a search for a gcd law on band-1 words ([`band-one-gcd-law-search`](attempts/band-one-gcd-law-search/README.md)).

## History

Written by the B06 migration (Claude, Opus 5.5) from the legacy line README `experiments/cycle_spectrum/README.md`, `docs/STATUS.md` and `docs/FRONTIER.md` at commit `be73a66`. The owner's goal brief and the main lane's log are archived in [`archive/cycle-spectrum/`](../../archive/cycle-spectrum/BRIEF.md).
