---
id: half-cancellation-counterexample-rotation-pair
kind: result
title: "The half-cancellation bound fails at four mismatches: a word of length 20 with G² ≈ 22·2^A"
status: written
claim: >
  Raw odd-only clock. The primitive positive word w = (1,1,1,1,6,1,5,1,1,2,1,5,1,1,2,1,1,1,1,6), m = 20, A = 40,
  D = 2^40 − 3^20 = 1,096,024,843,375 > 0, has rotation distance ρ(w) = 4 (the rotation by 5 differs from w in exactly
  four positions) and cancellation G = gcd(C_w, D) = 4,947,635 = 5·(2^20 − 3^10), so G² = 2^(44.48) > 2^A. It refutes
  the conjecture of half-cancellation-for-few-mismatch-words (G² < 2^A for every primitive word with ρ ≤ 4 and
  m ≥ 9). It is the valuation word of the actual 3x+221525 cycle through 28,147 (q = D/G = 5²·8861); it is the
  rotation pair (R_3 u, R_8 u) of the word u = (1,1,2,1,1,1,1,6,1,5) of the 3x+1267 cycle through 197, whose states
  1837 + 697 = 2·1267, hence of the form a·b·b·a with a = (1,1,1,1,6), b = (1,5,1,1,2); its primitive part is
  gcd(G, Φ_20(4, 3)) = 5. In the scan of every cycle of 3x+d, d ≤ 20,000 coprime to 6, from odd seeds ≤ 5,000
  (39,413 cycle words, 45,974 rotation pairs with d | n_r + n_s, 71 resulting words with ρ ≤ 4), exactly 12 words
  violate G² < 2^A: three cycle classes (3x+1267 through 197, m = 20; 3x+18571 through 3341, m = 28;
  3x+14833 through 2903, m = 36), all of the form (R_r u, R_(r+n/2) u) with gcd(C_w, 2^(A/2) + 3^(m/2)) = 5 and
  3^(m/2)/2^(A/2) ≤ 0.0564; the 28 of the 71 words that are near-critical (3^(m/2)/2^(A/2) > 1/√2) satisfy the bound
  by at least 1.01 bits.
authors:
  - Claude cycles lane (Fable 5.1; directed by Santiago Armstrong)
created: 2026-10-31
depends_on: [doubled-words-periodic-and-antiperiodic-points]
certificates: [check_counterexample.py]
lean:
  - LeanLane.HalfCancellationCounterexample.w_C
  - LeanLane.HalfCancellationCounterexample.w_D
  - LeanLane.HalfCancellationCounterexample.w_D_factor
  - LeanLane.HalfCancellationCounterexample.w_gcd
  - LeanLane.HalfCancellationCounterexample.w_gcd_factor
  - LeanLane.HalfCancellationCounterexample.w_violates_half_bound
  - LeanLane.HalfCancellationCounterexample.w_mismatches_five
  - LeanLane.HalfCancellationCounterexample.w_rotation_distance
  - LeanLane.HalfCancellationCounterexample.w_primitive
  - LeanLane.HalfCancellationCounterexample.w_D_pos
evidence:
  - "counterexample.json: the receipt; K1 every quantity of the word (C_w, D, G, q, the cycle states of 3x+221525, the factor Φ_20(4, 3) = 44,305 and the primitive part), K2 the 3x+1267 cycle and the two rotations, K3 the scan (counts, the twelve violating pair words with their d, minimum, rotations, ρ, gcd(C_w, Φ₂), excess and 3^n/2^S)"
tags: [cycles, denominators, cancellation, counterexample, rotation-distance]
---

# The half-cancellation bound fails at four mismatches: a word of length 20 with G² ≈ 22·2^A

## Statement

Notation of [`conventions/NOTATION.md`](../../../../conventions/NOTATION.md) §2. [`half-cancellation-for-few-mismatch-words`](../../questions/half-cancellation-for-few-mismatch-words.md) asked whether every primitive positive word `w` with `m ≥ 9`, `D = 2^A − 3^m > 0` and rotation distance `ρ(w) ≤ 4` satisfies `G² < 2^A`, `G = gcd(C_w, D)`. The answer is no:

```
w = (1,1,1,1,6 | 1,5,1,1,2 | 1,5,1,1,2 | 1,1,1,1,6) = a·b·b·a,     a = (1,1,1,1,6),  b = (1,5,1,1,2),
m = 20,  A = 40,  D = 2^40 − 3^20 = 1,096,024,843,375 = Φ₁·Φ₂,  Φ₁ = 2^20 − 3^10 = 989,527,  Φ₂ = 2^20 + 3^10 = 1,107,625 = 5³·8861,
C_w = 655,517,108,785,   G = gcd(C_w, D) = 4,947,635 = 5·Φ₁,   G²/2^A = 2^(4.4766) ≈ 22.3.
```

- `w` is primitive (its blocks `a ≠ b`), and `ρ(w) = 4`: the rotation by 5 turns `a·b·b·a` into `b·b·a·a`, which differs from `w` exactly where `a` and `b` differ (positions 1 and 4 of each block), four positions in all; no rotation differs in fewer (the rotation by 10, `b·a·a·b`, differs in eight).
- `w` is the valuation word of an actual cycle of `3x+q` with `q = D/G = 221,525 = Φ₂/5`, through the states `132491, 309499, 575011, 973279, 1570681, 77087, 226393, 28147, 152983, 340237, 310559, 576601, 60979, 202231, 414109, 365963, 659707, 1100323, 1761247, 2752633` (minimum 28,147).
- Its algebraic and primitive parts, in the sense of [`algebraic-and-primitive-cancellation-census`](../algebraic-and-primitive-cancellation-census/README.md): `e = gcd(A, m) = 20`, `Φ_20(2^2, 3) = 44,305 = 5·8861`, and `g_prim = gcd(G, Φ_20(4, 3)) = 5`. The whole of `Φ₁ = Π_(d | 10) Φ_d(4, 3)` is algebraic cancellation; the primitive part is the single factor 5.

**Construction.** `w = (R_3 u, R_8 u)` for `u = (1,1,2,1,1,1,1,6,1,5)`, the valuation word of the `3x+1267` cycle `197 → 929 → 2027 → 1837 → 3389 → 5717 → 9209 → 14447 → 697 → 1679 → 197`: the states at positions 3 and 8 satisfy `1837 + 697 = 2534 = 2·1267`, so by corollary (iii) of [`doubled-words-periodic-and-antiperiodic-points`](../doubled-words-periodic-and-antiperiodic-points/README.md) `Φ₁ = D_u | C_w`; the extra factor is `5 = gcd(C_w, Φ₂)`.

**The scan.** Every cycle of `3x+d` for `d ≤ 20,000` coprime to 6, reached from an odd seed `≤ 5,000` (39,413 cycle words of length `≥ 2`, denominators equal to `d`); every rotation pair `r < s` with `d | n_r + n_s` (45,974); among the resulting words `w = (R_r u, R_s u)`, those with `ρ(w) ≤ 4` (71, rotation distance computed exactly). Exactly 12 of the 71 violate `G² < 2^A`, all with `m ≥ 9`:

| cycle | `n` | `m` | pairs `(r, s)` | `ρ` | `g₂ = gcd(C_w, Φ₂)` | `log₂G − A/2` | `3^n/2^S` |
|---|---|---|---|---|---|---|---|
| `3x+1267` through 197 | 10 | 20 | (3,8), (4,9) | 4 | 5 | +2.238 | 0.0563 |
| `3x+18571` through 3341 | 14 | 28 | (3,10), (4,11), (5,12), (6,13) | 4 | 5 | +2.296 | 0.0178 |
| `3x+14833` through 2903 | 18 | 36 | (3,12), …, (8,17) | 4 | 5 | +2.314 | 0.0056 |

In every violating pair `s − r = n/2`, so each word has the form `(R_r u, R_(r+n/2) u) = a·b·b·a` with `(a, b) = R_r u` cut in half, and `ρ = 4` comes from `ham(a, b) = 2` under the rotation by `n/2`. The 59 other words with `ρ ≤ 4` have `g₂ ∈ {1, 5}` and satisfy the bound; the 28 near-critical ones (`3^n/2^S > 1/√2`) satisfy it by at least 1.01 bits (the `3x+499` words with `g₂ = 5` and `3^n/2^S = 0.90`).

## Proof

The claim about `w` is a finite computation, done directly in the certificate (K1): `C_w` from its definition, `D`, `G`, primitivity, the mismatch count of every rotation, `G² > 2^A`, the replay of the `3x+221525` orbit from `C_w/G` (it returns after 20 steps with the valuation word `w`), and `Φ_20(4, 3)` by the Möbius product `Π_(d | 20) (4^d − 3^d)^μ(20/d)`. K2 regenerates the `3x+1267` cycle and the two rotations. K3 is the scan; the criterion `d | n_r + n_s` for `Φ₁ | C_w` is the proved corollary (iii), and the certificate also confirms `Φ₁ | C_w` directly on every kept word.

## Certificates

[`check_counterexample.py`](check_counterexample.py) (standard library, about 75 s, almost all of it the scan) performs K1–K3 and compares the summary with [`counterexample.json`](counterexample.json) (K4); `--write-receipt` regenerates the receipt. Finite statements only.

## Lean

[`lean/LeanLane/HalfCancellationCounterexample.lean`](../../../../lean/LeanLane/HalfCancellationCounterexample.lean), namespace `LeanLane.HalfCancellationCounterexample`, a module of the `LeanLane` library (`import LeanLane.Words`), standard axioms only (receipts `HalfCancellationCounterexample.*` in [`lean/receipts/`](../../../../lean/receipts/)). It machine-checks every property of the word `w` in the Statement, with `C`, `D` from `LeanLane.Words` (as in `CycleSpectrum.lean`) and `mismatches z h` the number of positions where `z` differs from its rotation by `h` (indices modulo the length):
`w_C : C w = 655517108785`; `w_D : D w = 1096024843375`; `w_D_factor : D w = (2^20 − 3^10)(2^20 + 3^10)`; `w_gcd : Int.gcd (C w) (D w) = 4947635`; `w_gcd_factor : 4947635 = 5·(2^20 − 3^10)`; `w_violates_half_bound : 2^(w.sum) < (Int.gcd (C w) (D w))^2`; `w_mismatches_five : mismatches w 5 = 4`; `w_rotation_distance : ∀ h < 20, 0 < h → 4 ≤ mismatches w h` (so `ρ(w) = 4`); `w_primitive : ∀ p < 20, 0 < p → 20 % p = 0 → 0 < mismatches w p`; `w_D_pos : 0 < D w`. The status stays `written`: the construction from the `3x+1267` cycle, the identification of `w` as a `3x+221525` cycle word and the scan are Python certificates, not Lean.

## Remarks

- **What is refuted and what is not.** The plain bound `G² < 2^A` for all primitive words with `ρ ≤ 4`, `m ≥ 9`, is false; so is any attempt to extend it to `ρ ≤ 8` or beyond ([`doubled-words-periodic-and-antiperiodic-points`](../doubled-words-periodic-and-antiperiodic-points/README.md) lists violations at `ρ = 8, 10, 12, …`). Two forms survive and are posed in [`primitive-cancellation-below-half`](../../questions/primitive-cancellation-below-half.md): the bound on the **primitive** part, `g_prim < 2^(A/2)` (here `g_prim = 5`), which carries the whole payoff for `q = 1` cycles, and the plain bound restricted to **near-critical** words `2^A < 2·3^m`, which no word of this scan violates. The denominator candidate of [`rotation-defect-denominator-candidate`](../../questions/rotation-defect-denominator-candidate.md) also stands: at `s = 4`, `G^4·4^20 = 2^(128.95) < 2^160·3^20 = 2^(191.70)`.
- **Why the counterexample is far from critical.** `G = Φ₁·g₂ = 2^(A/2)·(1 − 3^n/2^S)·g₂`, so with `g₂ = 5` the bound fails iff `3^n/2^S < 0.8`. The three violating cycles have letters 5 and 6 and `3^n/2^S` between 0.006 and 0.056. A `q = 1` cycle is near-critical (`2^A < 2·3^m`), which is why the refutation does not touch the payoff: the conjecture was a statement about all `3x+q`, and its failure happens in the regime that `q = 1` never visits.
- **The `3x+11` exception explained.** The word `(1,1,2,2,1,1,3,3)` at `m = 8`, the only exception known before, is of the same kind: `Φ₁ = 47` divides `C_w` by the theorem (`47 | 2C_u + C_v`) and `g₂ = 19`. The restriction `m ≥ 9` in the conjecture removed it by accident of size, not of structure.
- **Controls.** Every word in the scan is an actual `3x+q` cycle word by construction (the half-word is, and `w` itself has `q = D/G`). Nothing here concerns `q = 1`.
- **Novelty.** Undetermined; the conjecture it refutes is this repository's own ([`half-cancellation-for-few-mismatch-words`](../../questions/half-cancellation-for-few-mismatch-words.md), posed 2026-10-28).

## History

- Written 2026-10-31 by the Claude cycles lane (Fable 5.1), directed by Santiago Armstrong, three days after the same lane posed the conjecture it refutes.
- 2026-10-31, later: the properties of `w` are machine-checked in `lean/LeanLane/HalfCancellationCounterexample.lean` (see the Lean section); the status stays `written` because the scan is a Python certificate (Claude cycles lane, Fable 5.1).
- 2026-10-31, later still: the two factors of the cancellation are now computed from the two states, `gcd(1837 + 697, 1267) = 1267` and `gcd(1837 − 697, 2^20 + 3^10) = 5` ([`rotation-pair-words-exact-cancellation`](../rotation-pair-words-exact-cancellation/README.md)) (Claude cycles lane, Fable 5.1).
