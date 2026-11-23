---
id: ridout-1958-p-adic-roth
kind: source
title: "Ridout: the p-adic generalization of the Thue–Siegel–Roth theorem"
status: cited
citation: >
  D. Ridout, "The p-adic generalization of the Thue-Siegel-Roth theorem", Mathematika 5 (1958), 40-48,
  DOI 10.1112/S0025579300001339; with D. Ridout, "Rational approximations to algebraic numbers",
  Mathematika 4 (1957), 125-131. Statements read in Y. F. Bilu, "The many faces of the Subspace Theorem
  [after Adamczewski, Bugeaud, Corvaja, Zannier...]", Séminaire Bourbaki 2006/2007, exposé 967,
  Astérisque (2008), arXiv:0907.2098, section 1; and in M. Waldschmidt, "Schmidt Subspace Theorem and
  S-unit equation", lecture notes, CIMPA school, Oujda, May 2015, Théorème 2.
url: https://arxiv.org/abs/0907.2098
created: 2026-11-23
tags: [diophantine-approximation, s-units, subspace-theorem, ineffective]
---

# Ridout: the p-adic generalization of the Thue–Siegel–Roth theorem

## Citation

D. Ridout, *The p-adic generalization of the Thue–Siegel–Roth theorem*, Mathematika 5 (1958), 40–48,
[DOI 10.1112/S0025579300001339](https://doi.org/10.1112/S0025579300001339), and D. Ridout, *Rational
approximations to algebraic numbers*, Mathematika 4 (1957), 125–131. The original papers were not read. The
statements below are quoted from two secondary sources, read on 2026-11-23:

- Y. F. Bilu, *The many faces of the Subspace Theorem [after Adamczewski, Bugeaud, Corvaja, Zannier…]*,
  Séminaire Bourbaki, exposé 967, [arXiv:0907.2098](https://arxiv.org/abs/0907.2098), section 1;
- M. Waldschmidt, *Schmidt Subspace Theorem and S-unit equation*, lecture notes for the CIMPA school in Oujda
  (May 2015), [author-hosted copy](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/SubspaceTheoremOujda2015.pdf),
  Théorème 2.

**Bilu's form.** For a prime `p`, or `p = infinity`, let `|.|_p` be the `p`-adic absolute value on the
rationals, extended to the algebraic numbers. For a rational `xi = y/x` in lowest terms put
`H(xi) = max(|x|, |y|)`. Let `S` be a finite set of primes including infinity, and fix an algebraic number
`alpha_p` for every `p` in `S`. Then, for every `epsilon > 0`, the inequality

```
product over p in S of min(1, |alpha_p - xi|_p)  <  1 / H(xi)^(2 + epsilon)
```

has finitely many solutions `xi` in the rationals. Bilu adds that the theorem "is quite non-trivial even when
the targets `alpha_p` are rational", and that infinite targets are allowed, with the convention
`infinity - xi = 1/xi`.

**Waldschmidt's form.** Let `alpha, beta` be algebraic numbers, not both zero. For `1 <= i <= s` let `p_i` be a
prime and `alpha_i, beta_i` rational numbers, not both zero. Let `epsilon > 0`. Then the set of rational numbers
`p/q` with

```
q * |q alpha - p beta| * product over i of |q alpha_i - p beta_i|_(p_i)  <  1 / max(|p|, q)^epsilon
```

is finite.

## What we use

The case `S = {infinity, 2, 3}` with targets `1`, `infinity` and `0`: in Waldschmidt's form,
`alpha = beta = 1`, `(alpha_1, beta_1) = (1, 0)` at the prime 2 and `(alpha_2, beta_2) = (0, 1)` at the prime 3.
For coprime positive integers `P = 3^n P'` and `Q = 2^c Q'` this says that

```
Q * |Q - P| * 2^(-c) * 3^(-n)  <  1 / max(P, Q)^epsilon
```

has only finitely many solutions. This is the shape of Mahler's theorem on the fractional parts of powers of a
rational number, which Bilu's survey attributes to Mahler "using the theorem of Ridout".

Used by [`half-period-four-mismatch-finiteness`](../areas/cycles/results/half-period-four-mismatch-finiteness/README.md).

**The theorem is ineffective.** It gives no bound on the size of the solutions. Every result resting on it is a
finiteness statement without an explicit bound.

## How it is checked

`cited`. Not reproduced and not formalised. The two secondary statements were compared with each other for the
case used: both give the same inequality for `S = {infinity, 2, 3}`. The original papers were not consulted, so
the attribution of each form to the 1957 or the 1958 paper is taken from the secondary sources.
