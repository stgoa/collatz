---
id: repeated-block-cancellation-bound
kind: result
title: A fixed defect bounds the denominator cancellation of repeated-block words
status: reviewed
claim: >
  Raw odd-only clock, no absorption at 1. Let u, v be nonempty positive valuation words, write
  Q = 2^Σu, P = 3^|u|, D_u = Q − P, D_v = 2^Σv − 3^|v|, K = D_u·C_v − D_v·C_u, and let
  w_k = u^k v (k ≥ 1) with D_k = D(w_k) > 0 and g_k = gcd(C(w_k), D_k). Then g_k divides the
  prime-to-6 part K_0 of K, so den(w_k) ≥ D_k/|K| when K ≠ 0. With H = gcd(D_k, K),
  H/gcd(H, D_u) divides g_k and g_k divides H; if gcd(D_u, D_v) = 1 then g_k = gcd(D_k, K).
  For K ≠ 0, g_(k+T) = g_k with T = lcm(ord_L(Q), ord_L(P)), L = K_0·|D_u|. If K = 0 (and
  D_k > 0), u and v are powers of one common primitive word and den(w_k) is that word's
  denominator. Consequently, if K ≠ 0 and D_u > 0, each fixed reduced denominator, 1 included,
  occurs for only finitely many k in the family u^k v.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: []
lean:
  - LeanLane.Cyc.commutator
  - LeanLane.Cyc.gcd_dvd_K
  - LeanLane.Cyc.gcd_le_natAbs_K
  - LeanLane.Cyc.gcd_eq_gcd_K
  - LeanLane.Cyc.gcd_two_sided
  - LeanLane.Cyc.gcd_periodic
  - LeanLane.Cyc.gcd_periodic_totient
  - LeanLane.Cyc.gcd_coprime_six
  - LeanLane.Cyc.seven_dvd_D_example
  - LeanLane.Cyc.gcd_example
  - LeanLane.Cyc.K0_letters
  - LeanLane.Cyc.K0_common_period
certificates: [check_spectrum.py]
evidence:
  - "REPETITION_SPECTRUM.md: the complete written proof (sections 1-2)"
  - "repetition_spectrum.py: finite constructors imported by check_spectrum.py; not a checker"
  - "spectrum_audit.json: receipt of check_spectrum.py"
  - "INDEPENDENT_REVIEW.md, SIDE_REVIEW.md, LITERATURE.md: main-lane review, side-input assessment and bounded literature audit"
  - "delivery_checks.json, full_gate.json: historical delivery receipt and historical finite gate (scripts/verify_all.py at the time); no script here regenerates them"
  - "c001_spectrum_check.py: side-lane independent check; exits 0 when run bare but then skips its part (5) and rewrites c001_spectrum_check.json with compared_with_main false; run with the corpus path (areas/cycles/results/actual-cycles-3x-d-corpus/actual_cycles.json) as argument it exits 0 and reproduces its committed receipt byte for byte (checked at migration). Passed bare at be73a66 as reviews/side_lane/c001_spectrum_check.py (archive/legacy-checker-run-be73a66.md)"
  - "c001_spectrum_check.json: receipt of the side-lane check, written with the corpus argument"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-19
    link: c001_spectrum_check.py
    scope: "Side-lane feed (legacy archive/side_lane/FEED.md), entry 2026-10-19 00:18, REFEREE C001 at main 14441c0: identities (1)-(3) re-derived by hand; divisibility, two-sided bound, exact coprime formula and periodicity checked on random blocks; worked law for k <= 80; the d = 485 counterexample; verdict correct and reproduced"
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Lean units C001-a and C001-b verified (feed entries 00:22 and 00:32): identity (3), g_k | K, the bound, the coprime formula (6), the two-sided bound (7), periodicity (9) and the worked examples are machine-checked; the K = 0 characterisation was queued (C001-c) and later partly covered by C002-b part 2"
aliases: [C001]
tags: [cycles, denominators, repeated-blocks, commutator, 3x+d]
---

# A fixed defect bounds the denominator cancellation of repeated-block words

## Statement

Notation as in [`conventions/NOTATION.md`](../../../../conventions/NOTATION.md): for a positive valuation word `z` of length `m`, `C_z = Σ_j 3^(m−1−j)·2^(A_j)`, `D_z = 2^A − 3^m`; when `D_z > 0` the word describes a genuine positive rational cycle with exact valuations and `den(z) = D_z/gcd(C_z, D_z)`. The clock is the raw odd-only map, with no absorbing state at 1.

Fix two nonempty positive words `u, v` and put

```
Q = 2^sum(u),  P = 3^len(u),  D_u = Q − P,
S = 2^sum(v),  R = 3^len(v),  D_v = S − R,
K = D_u·C_v − D_v·C_u,
w_k = u^k v  (k >= 1),  C_k = C(w_k),  D_k = D(w_k) > 0,  g_k = gcd(C_k, D_k).
```

Then, with `G_k = (Q^k − P^k)/(Q − P)`:

```
C_k = R·C_u·G_k + Q^k·C_v,                      (1)
D_k = S·Q^k − R·P^k,                            (2)
D_u·C_k − C_u·D_k = Q^k·K.                      (3)
```

1. **Bounded cancellation.** `g_k` divides `K`, indeed its prime-to-6 part `K_0`. If `K ≠ 0`, `den(w_k) ≥ D_k/|K|`.
2. **Exact formula.** With `H = gcd(D_k, K)`, `H/gcd(H, D_u)` divides `g_k`, which divides `H` (no coprimality premise). If `gcd(D_u, D_v) = 1`, then `g_k = gcd(D_k, K)`.
3. **Periodicity.** If `K ≠ 0`, put `L = K_0·|D_u|` and `T = lcm(ord_L(Q), ord_L(P))`. Then `g_(k+T) = g_k` whenever the denominators involved are positive. Euler's `φ(L)` is a simpler, possibly larger, period.
4. **The case `K = 0`.** If `K = 0` and `D_k > 0`, then `D_u, D_v > 0`, `C_u/D_u = C_v/D_v`, and `u`, `v` are powers of one common primitive word; `den(w_k)` is that word's denominator. Conversely such powers have `K = 0`.
5. **Consequence.** If `K ≠ 0` and `D_u > 0`, then `D_k` grows exponentially in `k` while the cancellation stays bounded, so each fixed denominator, including 1, occurs for only finitely many `k` in this family.

This is a structural exclusion for one fixed defect, not a universal cycle exclusion.

## Proof

The complete proof is in [`REPETITION_SPECTRUM.md`](REPETITION_SPECTRUM.md), §§1–2. In summary (legacy report, lightly edited):

> The proof uses the exact identity `D_u·C_w − C_u·D_w = 2^(k·A_u)·K`. The denominator is coprime to 2, so its common divisor with `C_w` must divide `K`. A finite invertible modular recurrence proves periodicity. No distribution assumption or unproved prime-factor conjecture is involved.

The `K = 0` case: the two blocks then have the same positive rational fixed point, so determinism makes the infinite words `uuu…` and `vvv…` identical, and their common least period divides both lengths. This case is essential: it includes the trivial Collatz cycle and repetitions of every genuine `d > 1` control.

The concatenation, commutator and repetition formulas are established algebra (Trümper 2014, §§3–4; Halbeisen–Hungerbühler 1997, Eq. (4)); see [`LITERATURE.md`](LITERATURE.md). The exact cancellation corollary was not located in that bounded audit.

### Exact example

For `u = (1,1,3)`, `v = (2)` one has `K = −14`, and the cancellation is 7 when `k ≡ 3 (mod 6)` and 1 otherwise. Hence

```
den((1,1,3)^k 2) = (4·32^k − 3·27^k)/(7 if k ≡ 3 mod 6 else 1),
```

an exact spectrum law for all `k ≥ 1`. The first denominator is 47. This family's rational minimum stays bounded (below `31/10`); it supplies no high-cycle control.

### A false strengthening, killed exactly

Dropping `gcd(D_u, D_v) = 1` from the exact formula is false:

```
u = (3), v = (1,5), k = 1,
D_u = 5, D_v = 55, K = −30,
C_w = 49, D_w = 485,
gcd(C_w, D_w) = 1, but gcd(D_w, K) = 5.
```

The actual `3x+485` cycle is `49 → 79 → 361 → 49`, with valuations 3, 1, 5. The divisibility theorem survives; the stronger equality does not.

## Certificates

- [`check_spectrum.py`](check_spectrum.py) (about 15 s): regenerates the finite word experiment in memory and compares it with [`spectrum_audit.json`](spectrum_audit.json), including the source hashes of itself and of [`repetition_spectrum.py`](repetition_spectrum.py). It refuses optimised Python (`-O`), since its checks use assertions. The receipt covers 26,628 block pairs and 239,345 positive word cycles, replaying 6,264,270 odd arrows; 238,328 nonzero-`K` divisibilities and 212,522 exact coprime-block formulas, plus 1,017 common-fixed-point repetitions; 3,235 distinct denominators; 128 certified modular periods; the mod-6 law through `k = 256`; and 306 perturbed mechanical examples (see [`perturbed-mechanical-block-family`](../perturbed-mechanical-block-family.md)). Its finite box restricts `u` to `2^sum(u) > 3^len(u)`; the general algebra also permits negative `D_u`, which the box does not cover. Repeated words and repeated denominators are counted as test cases, not as new primitive cycles.

These finite checks support the implementation; they do not replace the universal proofs.

## Lean

`lean/CycleSpectrum.lean`, Lean units C001-a and C001-b (legacy `lean/STATE.md`), plus part of C002-b:

- `LeanLane.Cyc.commutator` is identity (3), over ℤ, for every `k ≥ 0`.
- `gcd_dvd_K` and `gcd_le_natAbs_K`: `g_k | K` and `g_k ≤ |K|` for `K ≠ 0`; `gcd_coprime_six`: `g_k` is coprime to 6. The only hypotheses are that `v` is nonempty with positive entries.
- `gcd_eq_gcd_K`: claim 2's exact formula under `IsCoprime (D u) (D v)`; `gcd_two_sided`: the two-sided bound with no coprimality premise.
- `gcd_periodic`: claim 3 in hypothesis form, for any factorisation `|K| = 2^a·3^b·K_0` and any `T` with `Q^T ≡ P^T ≡ 1 (mod K_0·|D_u|)`; `gcd_periodic_totient`: the explicit period `φ(K_0·|D_u|)` when `K_0` is coprime to 6. `K_0` enters through the factorisation hypothesis, not as the exact prime-to-6 part.
- `seven_dvd_D_example`, `gcd_example`: the worked law (`7 | D((1,1,3)^k 2) ⇔ k ≡ 3 (mod 6)` and `gcd(C_k, D_k) = gcd(D_k, −14)`); the `d = 485` counterexample is also checked.
- `K0_letters`, `K0_common_period` (Lean unit C002-b part 2): for `K = 0`, the two infinite valuation words coincide and both words have period `gcd(|u|, |v|)`. The list packaging `u = z^(|u|/g)`, `v = z^(|v|/g)` and `den(u^k v^ℓ) = den(z)` was **not** formalised.

Axioms: `propext`, `Classical.choice`, `Quot.sound` (receipts in `lean/receipts/CycleSpectrum.*`). The node is not `formal`: claim 4's word packaging and the finiteness consequence 5 are written proofs only.

## Remarks

- **Scope.** This proves a restriction for repeated-block words `u^k v`. It does not exclude all Collatz cycles, does not bound cancellation for arbitrary words with many changing defects, and cannot settle the full denominator spectrum. Its intermediate conclusion is that a fixed noncommuting defect cannot create indefinitely large cyclotomic cancellation; the remaining gcd is a finite periodic function of the repetition count.
- **Controls.** The primitive words `(1,2,2)`, `(1,3)` and `(4)` have `(C, D) = (23, 5)`, `(5, 7)`, `(1, 13)`; scaling gives integer cycles of `3x+5`, `3x+7`, `3x+13`. Choosing `v = u` gives `K = 0`, and repetition keeps exactly those denominators. There is no universal exclusion of denominators 5, 7, 13. On the actual-cycle corpus ([`actual-cycles-3x-d-corpus`](../actual-cycles-3x-d-corpus/README.md)), 1,587 of the 2,013 nonfixed cycles have a tested split with `|K| < D_w`, and the bound permits the actual `d > 1` denominator in every case (a bound need not be sharp to pass). The tested decompositions use the orientation starting at each cycle's smallest state, not every rotation.
- **Application.** The bound applies to an infinite primitive, nonbalanced family with growing minima: [`perturbed-mechanical-block-family`](../perturbed-mechanical-block-family.md).
- **Two growing blocks.** For `u^k v^ℓ` with both exponents growing, elimination leaves a common geometric divisor rather than a fixed constant, and equal slopes can produce exponential cancellation, so a uniform bounded-cancellation claim would be false ([`constant-cancellation-two-growing-blocks`](../../attempts/constant-cancellation-two-growing-blocks.md)). The follow-up results are [`equal-total-two-block-exclusion`](../equal-total-two-block-exclusion/README.md), [`proportional-slope-two-block-bound`](../proportional-slope-two-block-bound.md) and [`unequal-slope-two-block-growth`](../unequal-slope-two-block-growth/README.md).
- **Literature and novelty.** The primary-source audit ([`LITERATURE.md`](LITERATURE.md)) identifies the affine concatenation, commutator and repetition formulas as established work, including Trümper 2014. The exact cancellation corollary was not located in that bounded audit; this does not establish novelty. The audit also checks Knight's precise extremal meaning of "high" ([`knight-2026-high-cycles`](../../../../sources/knight-2026-high-cycles.md)) and distinguishes Simons–de Weger's updated version, Hercher's journal result and its 2026 corrigendum from an unverified newer record claim. Novelty undetermined.
- **Review record.** The main lane's [`INDEPENDENT_REVIEW.md`](INDEPENDENT_REVIEW.md) audits the proof and the executable checks; the main lane's root separately checked the arithmetic argument and the scanner and reran the full discovery. Those are same-lane reviews. The independent reviews are listed under `reviewed_by`. No human peer review is claimed. [`SIDE_REVIEW.md`](SIDE_REVIEW.md) is the main lane's read of the side-lane feed at the time.
- **Legacy "what next".** The legacy report named two independently growing repeated blocks `u^k v^ℓ` as the next test, flagged that equal valuation slopes can produce exponential cancellation, and pointed to an S-unit gcd theorem ([`corvaja-2005-s-unit-height`](../../../../sources/corvaja-2005-s-unit-height.md)) for the unequal-slope case, with ineffective thresholds kept explicit. The headline stayed open because general primitive words need not have either fixed-block form.

## History

- Migrated from `experiments/cycle_spectrum/C001/` (legacy ID `C001`; report `REPORT.md`, proof `REPETITION_SPECTRUM.md`) at commit `be73a66`, by the B03 migration (Claude, Opus 5.5). The side-lane check `reviews/side_lane/c001_spectrum_check.{py,json}` moved here. Section 2 of the legacy report became [`perturbed-mechanical-block-family`](../perturbed-mechanical-block-family.md); its section 3 (the actual-cycle scan) became [`actual-cycles-3x-d-corpus`](../actual-cycles-3x-d-corpus/README.md).
- Main lane (ChatGPT/Codex), 2026-10-18 to 2026-10-19: first batch of the cycle-spectrum goal. Corrections before delivery, recorded in the legacy report: (i) review corrected a draft sign overstatement: `D_u > 0` makes `D(u^k v)` positive for all sufficiently large `k`, not for every `k` (for `u = (2)`, `v = (1,1,1)`, `k = 1` it is −49); the written statement keeps the domain `D_k > 0`; (ii) an overly optimistic three-quarters height comparison was discarded before adoption, and the proved three-fifths comparison keeps its extra exponent condition; (iii) the first default receipt replay exposed a tuple/list serialisation mismatch, corrected before the receipt was regenerated; no numerical cycle or theorem changed. No historical result was changed or found erroneous.
- The legacy prose cites R71 ([`mechanical-word-exact-denominator`](../mechanical-word-exact-denominator/README.md), §1 of its note) for the classical facts that `C_z/D_z` is a cycle with exact valuations and that `den` is rotation invariant.
