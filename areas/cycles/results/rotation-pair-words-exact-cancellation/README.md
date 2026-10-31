---
id: rotation-pair-words-exact-cancellation
kind: result
title: "Concatenating two rotations of an actual 3x+d cycle word: the cancellation is G_u·gcd(n_r + n_s, d)·gcd(n_r − n_s, 2^S + 3^n)"
status: written
claim: >
  Raw odd-only clock. Let u be the valuation word of a primitive actual 3x+d cycle (length n ≥ 2, total S,
  distinct states n_0, …, n_(n−1) coprime to d, reduced denominator d, cancellation G_u = gcd(C_u, D_u) =
  (2^S − 3^n)/d), and for 0 ≤ r < s < n let w = (R_r u, R_s u), a word of length 2n and total 2S. Then
  gcd(C_w, D_w) = G_u · gcd(n_r + n_s, d) · gcd(n_r − n_s, 2^S + 3^n), and w is the valuation word of an actual
  3x+q cycle with q = d·(2^S + 3^n) / (gcd(n_r + n_s, d)·gcd(n_r − n_s, 2^S + 3^n)). Consequently
  gcd(C_w, D_w) ≤ (2^S − 3^n)·|n_r − n_s|, the algebraic factor 2^S − 3^n divides C_w iff d | n_r + n_s, and the half
  bound gcd(C_w, D_w)² < 2^(2S) fails iff gcd(n_r + n_s, d)·gcd(n_r − n_s, 2^S + 3^n) ≥ d·2^S/(2^S − 3^n). Verified
  directly on all 739,757 rotation pairs of the 1,176 distinct cycle words (n ≥ 2) of actual-cycles-3x-d-corpus
  (742 pairs violate the half bound, 131 of them with d | n_r + n_s; the largest gcd(n_r − n_s, 2^S + 3^n) is
  20,665) and on all 7,468,269 pairs of the 4,202 cycle words of 3x+d, d ≤ 3,000 coprime to 6, reached from odd
  seeds ≤ 5,000 (3,280 violations, 478 with d | n_r + n_s; largest second factor 67,721). The counterexample of
  half-cancellation-counterexample-rotation-pair is the case d = 1267, (n_r, n_s) = (1837, 697):
  gcd(2534, 1267) = 1267 and gcd(1140, 2^20 + 3^10) = 5.
authors:
  - Claude cycles lane (Fable 5.1; directed by Santiago Armstrong)
created: 2026-10-31
depends_on: [doubled-word-cancellation-formula, actual-cycles-3x-d-corpus]
certificates: [check_rotation_pairs.py]
evidence:
  - "rotation_pairs.json: the receipt; R1 the corpus pairs (counts, the largest second factor, how many pairs have d | n_r + n_s, how many have a nontrivial second factor, the violations of the half bound and how many of them have d | n_r + n_s), R2 the same for the generated cycles with d ≤ 3,000, R3 the counterexample's numbers"
tags: [cycles, denominators, cancellation, doubled-words, controls, 3x+d]
---

# Concatenating two rotations of an actual `3x+d` cycle word: the cancellation is `G_u·gcd(n_r + n_s, d)·gcd(n_r − n_s, 2^S + 3^n)`

## Statement

Notation of [`conventions/NOTATION.md`](../../../../conventions/NOTATION.md) §2. Let `u` be the valuation word of a primitive actual `3x+d` cycle: length `n ≥ 2`, total `S`, states `n_0 → n_1 → … → n_(n−1) → n_0` (distinct, coprime to `d`), `D_u = 2^S − 3^n`, `G_u = gcd(C_u, D_u)`, reduced denominator `d = D_u/G_u`. For `0 ≤ r < s < n` put `w = (R_r u, R_s u)`: the two rotations starting at `n_r` and at `n_s`, concatenated; `|w| = 2n`, `Σw = 2S`, `D_w = (2^S − 3^n)(2^S + 3^n)`.

```
gcd(C_w, D_w) = G_u · gcd(n_r + n_s, d) · gcd(n_r − n_s, 2^S + 3^n),
den(w) = d · (2^S + 3^n) / ( gcd(n_r + n_s, d) · gcd(n_r − n_s, 2^S + 3^n) ),
```

so `w` is the valuation word of an actual `3x+den(w)` cycle. Consequences: `gcd(C_w, D_w) ≤ (2^S − 3^n)·|n_r − n_s|`; `2^S − 3^n | C_w` iff `d | n_r + n_s`; the half bound `gcd(C_w, D_w)² < 2^(2S)` fails iff `gcd(n_r + n_s, d)·gcd(n_r − n_s, 2^S + 3^n) ≥ d·2^S/(2^S − 3^n)`.

**Data (certificate).** Over the corpus ([`actual-cycles-3x-d-corpus`](../actual-cycles-3x-d-corpus/README.md)), 1,176 distinct primitive cycle words with `n ≥ 2` and all their 739,757 rotation pairs: the two formulas hold on every pair; `d | n_r + n_s` on 1,809 pairs; `gcd(n_r − n_s, 2^S + 3^n) > 1` on 69,476, with maximum 20,665; 742 pairs violate the half bound, 131 of them with `d | n_r + n_s` (these are the 131 violations of [`doubled-words-periodic-and-antiperiodic-points`](../doubled-words-periodic-and-antiperiodic-points/README.md)). Over the 4,202 cycle words of `3x+d`, `d ≤ 3,000`, from odd seeds `≤ 5,000`, and their 7,468,269 pairs: both formulas on every pair; 3,280 violations, 478 with `d | n_r + n_s`; largest second factor 67,721.

## Proof

By NOTATION §2 the rational cycle point of `R_r u` is `n_r/d = C_(R_r u)/D_u`, so `C_(R_r u) = n_r·G_u` with `G_u = D_u/d`. Apply [`doubled-word-cancellation-formula`](../doubled-word-cancellation-formula/README.md) to `(R_r u, R_s u)` with `j = 0` (equal totals), `K = G_u`, `L = d` (so `Φ₁ = 2^S − 3^n = L·K`), `A = n_r`, `B = n_s`: `gcd(C_w, D_w) = G_u·gcd(n_r + n_s, d)·gcd(n_r − n_s, 2^S + 3^n)` and `den(w) = (d/g₁)·((2^S + 3^n)/g₂)`. A word with reduced denominator `q` is the valuation word of an actual `3x+q` cycle (NOTATION §2). The consequences: `gcd(n_r + n_s, d) ≤ d` and `gcd(n_r − n_s, 2^S + 3^n) ≤ |n_r − n_s|` (`n_r ≠ n_s` since the cycle is primitive) give the bound; `2^S − 3^n | C_w` iff `G_u·gcd(n_r + n_s, d) = d·G_u`; and `gcd(C_w, D_w)² ≥ 2^(2S)` iff `(2^S − 3^n)·g₁·g₂/d ≥ 2^S`. The data are the certificate.

## Certificates

[`check_rotation_pairs.py`](check_rotation_pairs.py) (standard library, about 35 s) checks, directly from the definitions of `C` and `D`: **R1** on every rotation pair of every distinct cycle word of the corpus, `C_(R_r u) = n_r·G_u`, both formulas, and the bound; **R2** the same on every pair of every cycle of `3x+d`, `d ≤ 3,000` coprime to 6, found from odd seeds `≤ 5,000`; **R3** the counterexample's numbers; **R4** the receipt [`rotation_pairs.json`](rotation_pairs.json) (`--write-receipt` regenerates it). Finite statements only; the formula itself is the formal node.

## Lean

The formula and the cycle equation behind it are machine-checked in [`doubled-word-cancellation-formula`](../doubled-word-cancellation-formula/README.md) (`LeanLane.CycleEquation.rotation_pair_gcd`: for states following `w` under `3x+q` with period `|w|`, `q > 0`, `gcd(x_0, q) = 1`, the rotation pair's cancellation is `(D_w/q)·gcd(x_r + x_s, q)·gcd(x_r − x_s, 2^(Σw) + 3^|w|)`). This node adds the reading through actual cycles (NOTATION §2), the consequences and the data, so its status stays `written`.

## Remarks

- **What it explains.** Every word built from two rotations of an actual cycle has the whole algebraic factor `2^S − 3^n` in its cancellation exactly when the two states sum to a multiple of `d`, and its primitive-side factor is the gcd of the *difference* of the two states with `2^S + 3^n`: a number below the cycle's height, with no structural reason to be large. The counterexample to [`half-cancellation-for-few-mismatch-words`](../../questions/half-cancellation-for-few-mismatch-words.md) is the pair `(1837, 697)` of the `3x+1267` cycle, whose difference `1140 = 2²·3·5·19` shares the factor 5 with `2^20 + 3^10 = 5³·8861`.
- **Controls.** The construction takes actual `3x+d` cycles as input and produces actual `3x+q` cycles with the stated `q`; for example the `3x+5` cycle `19 → 31 → 49` gives `(1,1,3,1,3,1)` as a `3x+59` cycle word (`gcd(50, 5) = 5`, `gcd(12, 59) = 1`) and `(1,1,3,3,1,1)` as a `3x+295` cycle word (`gcd(68, 5) = 1`, `gcd(30, 59) = 1`). Nothing concerns `q = 1`: a rotation pair would be a `3x+1` cycle word only if `d | n_r + n_s` and `2^S + 3^n | n_r − n_s`.
- **Relation to the primitive conjecture.** When `gcd(2S, 2n) = 2` the primitive part of `w` is `gcd(n_r − n_s, 2^S + 3^n)` itself, so for this family [`primitive-cancellation-below-half`](../../questions/primitive-cancellation-below-half.md) (A) says that the difference of two states of a `3x+d` cycle never shares a factor `≥ 2^S` with `2^S + 3^n`; the largest observed is 67,721 against `2^S ≥ 2^14` for the words involved.
- **Novelty.** Undetermined.

## History

- Written 2026-10-31 by the Claude cycles lane (Fable 5.1), directed by Santiago Armstrong, as the explicit form of corollary (iii) of [`doubled-words-periodic-and-antiperiodic-points`](../doubled-words-periodic-and-antiperiodic-points/README.md).
