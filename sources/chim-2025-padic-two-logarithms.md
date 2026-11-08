---
id: chim-2025-padic-two-logarithms
kind: source
title: "Chim (2025): explicit bounds for two p-adic logarithms"
status: cited
citation: >
  Kwok Chi Chim, Lower bounds for linear forms in two p-adic
  logarithms, Journal of Number Theory 266 (2025), 295-349,
  Theorem 2.1, pp. 298-299. DOI 10.1016/j.jnt.2024.07.012.
url: https://doi.org/10.1016/j.jnt.2024.07.012
created: 2026-11-08
tags: [linear-forms, p-adic-logarithms, explicit-bounds, external-input]
---

# Chim (2025): explicit bounds for two p-adic logarithms

## Citation

Chim, *Journal of Number Theory* **266** (2025), 295-349,
[Theorem 2.1](https://tugraz.elsevierpure.com/ws/portalfiles/portal/92346766/1-s2.0-S0022314X24001793-main.pdf),
printed pp. 298-299.

## What we use

All logarithms here are natural. For odd integers `y>=35`,
`3` not dividing `y`, and integers `f>=1`, specialize to

```
p=3, alpha_1=2, alpha_2=-1/y, b_1=f, b_2=1,
D=1, ramification=1, residue degree=1, g=2,
A_1=3, A_2=y, C=4650, Z_1=3.
```

The bases are 3-adic units and multiplicatively independent:
the valuation at 2 first forces the exponent of 2 to vanish,
then absolute values force the other exponent to vanish.
The height conditions hold since `h(2)=ln(2)` and
`h(-1/y)=ln(y)`. The conclusion is

```
v_3(2^f*y+1) < 13950*(1.5*ln(3)+4.85)/(ln(3))^2 * H*ln(y),
H=max(ln(f/ln(y)+1/ln(3))+ln(ln(3)),
      1000*ln(3), 180*(1.5*ln(3)+4.85)*ln(3)).
```

## How it is checked

`cited`, not replayed or formal. The primary theorem and parameter
conditions were inspected on 2026-11-08. Dependent certificates
check the specialization's elementary constants, not Chim's proof.
