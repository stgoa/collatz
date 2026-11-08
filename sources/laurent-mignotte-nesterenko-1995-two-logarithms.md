---
id: laurent-mignotte-nesterenko-1995-two-logarithms
kind: source
title: "Laurent, Mignotte and Nesterenko (1995): an explicit two-logarithm bound"
status: cited
citation: >
  Michel Laurent, Maurice Mignotte and Yuri Nesterenko, Formes lineaires
  en deux logarithmes et determinants d'interpolation, Journal of Number
  Theory 55(2) (1995), 285-321, Corollary 2, p. 288.
url: https://doi.org/10.1006/jnth.1995.1141
created: 2026-11-08
tags: [linear-forms, logarithms, explicit-bounds, external-input]
---

# Laurent, Mignotte and Nesterenko (1995): an explicit two-logarithm bound

## Citation

Laurent, Mignotte and Nesterenko, *Formes lineaires en deux
logarithmes et determinants d'interpolation*, Journal of Number
Theory **55** (1995), 285-321,
[DOI 10.1006/jnth.1995.1141](https://doi.org/10.1006/jnth.1995.1141).

The formulation checked here is Theorem 3.3, printed p. 715, of
Yuri Bilu, Carlos A. Gomez, Jhonny C. Gomez and Florian Luca,
[*Elliptic curves over finite fields with Fibonacci numbers of
points*](https://nyjm.albany.edu/j/2020/26-32p.pdf), New York
Journal of Mathematics **26** (2020), 711-734. It explicitly
attributes the bound to the original Corollary 2, p. 288.

## What we use

All logarithms here are natural. Specialize that statement to
the rational bases 2 and 3, logarithmic height parameters
`log B_1=1`, `log B_2=2`, and field degree 1. For nonzero
integers `u,v`, put

```
Lambda=u*ln(2)+v*ln(3),       b'=|u|/2+|v|.
```

The positive bases are multiplicatively independent and have
heights `ln(2)<1`, `ln(3)<2`. The conclusion is

```
ln|Lambda| > -48.68*max(ln(b')+0.14,21,1/2)^2.
```

The absolute value covers both signs; no Collatz-specific
gap or near-critical hypothesis is imposed.

## How it is checked

`cited`, not replayed or formal. The primary research-paper
restatement and its parameter conditions were inspected on
2026-11-08. Direct access to the original publisher text
returned HTTP 403; its original proof was not inspected.
Certificates check the elementary specialization and subsequent
constants, not the external linear-form theorem.
