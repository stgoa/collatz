---
id: krasikov-2003-predecessors
kind: source
title: "Krasikov–Lagarias: predecessor counts at least X^0.84"
status: cited
citation: >
  I. Krasikov and J. C. Lagarias, "Bounds for the 3x+1 problem using difference inequalities",
  Acta Arithmetica 109 (2003), 237–258. arXiv:math/0205002. DOI 10.4064/aa109-3-4.
url: https://arxiv.org/abs/math/0205002
created: 2026-10-17
tags: [predecessors, density, convergence]
---

# Krasikov–Lagarias: predecessor counts at least X^0.84

## Citation

Krasikov and Lagarias, *Bounds for the 3x+1 problem using difference inequalities*, Acta Arithmetica 109 (2003), 237–258; [arXiv:math/0205002](https://arxiv.org/pdf/math/0205002); DOI 10.4064/aa109-3-4. An [author-hosted revised copy](https://websites.umich.edu/~lagarias/doc/krasikov.pdf) confirms the same quantifiers. Authors' initials completed from general knowledge, not verified against the source.

- **Theorem 6.1:** with the shortcut map `C` and `π_a(X) = #{1 ≤ n ≤ X : C^j(n) = a for some j ≥ 0}`, for every fixed positive `a` not divisible by 3 there is `X_0(a)` with `π_a(X) ≥ X^0.84` for all `X ≥ X_0(a)`. No assumption that `a` reaches 1.
- **Theorem 2.2, Table 2:** the linear-programming interface (`k = 11`, `λ = 1.7922310`, exponent ≈ `0.8417560`); displayed decimals are not a certified feasible vector.

## What we use

The fixed-target bound `π_a(X) ≥ X^0.84` for `a` coprime to 3, for `d = 1` only (transfer to `3x+d` unchecked). Legacy use: Phase 6 route node C.1 ([predecessor-exponent-certificate-replay](../areas/convergence/questions/predecessor-exponent-certificate-replay.md); audit L3 of [route-literature-transfer-audit](../areas/convergence/results/route-literature-transfer-audit.md), and part (ii) of [nonabsorbing-set-linear-lower-density](../areas/convergence/results/nonabsorbing-set-linear-lower-density/README.md): an eventual upper bound `C·X^(0.84−ε)` on unabsorbed counts would contradict it), and the earlier programme's "external amplification input" (master handoff). In the residual-progress sufficient-sets audit it is a comparison: the theorem is asymptotic and target-dependent and certifies no finite exit. It is no longer the strongest audited lower premise; see [lau-2026-positive-density](lau-2026-positive-density.md).

## How it is checked

`cited`. Not reproduced; no certified feasible vector or explicit cutoff was computed here.
