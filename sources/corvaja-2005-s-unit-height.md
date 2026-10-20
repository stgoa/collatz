---
id: corvaja-2005-s-unit-height
kind: source
title: "Corvaja–Zannier: height of a rational function at S-unit points"
status: cited
citation: >
  P. Corvaja and U. Zannier, "A lower bound for the height of a rational function at S-unit points",
  Monatshefte für Mathematik 144 (2005), 203–224. DOI 10.1007/s00605-004-0273-0.
  Preprint arXiv:math/0311030v2 (22 April 2004).
url: https://doi.org/10.1007/s00605-004-0273-0
created: 2026-10-19
tags: [s-units, gcd, cycles, ineffective]
---

# Corvaja–Zannier: height of a rational function at S-unit points

## Citation

P. Corvaja and U. Zannier, *A lower bound for the height of a rational function at S-unit points*, Monatshefte für Mathematik 144 (2005), 203–224, DOI 10.1007/s00605-004-0273-0. The inspected [full author preprint, math/0311030v2](https://arxiv.org/pdf/math/0311030) is dated 22 April 2004; theorem and page references are to its printed pages.

Normalised absolute values `|p|_p = 1/p`, `log^−(t) = min(0, log t)`, height `h(x/y) = log max(|x|, |y|)` for coprime integers.

- **Input A: Corollary 1, Eq. (1.3), p. 2 (proof pp. 16–17).** For fixed finitely generated `Γ ≤ (Q^*)^2` and `ε > 0`, all but finitely many multiplicatively independent pairs `(U, V) ∈ Γ` satisfy `Σ_ν log^− max(|U−1|_ν, |V−1|_ν) ≥ −ε·max(h(U), h(V))`.
- **Input B: Proposition 1, Eq. (2.2), p. 4 (proof pp. 4–7).** For `S` containing the archimedean places and a Laurent polynomial `f` with constant monomial 1, the solutions of `Σ_(ν∈S) log^− |f(U,V)|_ν < −ε·max(h(U), h(V))` lie in finitely many translates of one-dimensional subtori plus a finite set.

## What we use

Applied with `S = {∞, 2, 3}` and S-unit coordinates `(P_u/Q_u)^k`, `(P_v/Q_v)^ℓ` (multiplicative independence from unequal valuation/odd-count ratios), to bound `gcd(C_w, D_w)` subexponentially for two-block words `w = u^k v^ℓ`. Legacy results using it: C002 (`INDEPENDENT_SLOPES.md`: for unequal ratios, `log den(w) = A·log 2 − o(k+ℓ)`, so each bounded denominator set occurs for finitely many exponent pairs) and C003 (`UNEQUAL_PROBE.md`, global gcd estimate in one fixed ambient group). C001 §5 named it as the bridge for the two-growing-block extension.

The theorem is **ineffective**: it gives finiteness of each denominator layer but no explicit threshold and cannot exhibit the exceptions.

## How it is checked

`cited`. Imported, not re-proved or formal. The C002 application audits every local contribution and exceptional translate in writing.
