---
id: transposition-gap-fourteen-full-plus-cancellation
kind: result
title: A transposition of gap fourteen cancels the entire plus factor
status: written
claim: >
  Raw odd-only clock. For d=16383, the signed 3x+d orbit from -63 reaches
  453291 after exactly 187 odd steps, with valuation word z of total 320,
  and then reaches 21 with valuation 16. Put u=(1,z,15), v=(15,z,1) and
  w=uv. Then w is a primitive positive valuation word with m=378, A=672,
  rotation distance 4 attained only by shift 189, and exact cancellation
  gcd(C_w,2^672-3^378)=2^336+3^189. Its reduced denominator is
  2^336-3^189, so it is the word of an actual positive 3x+(2^336-3^189)
  cycle. In particular the full plus factor cancels for a transposition
  with letter gap 14, and G^2>2^A. The word is far from critical:
  2^672>=2*3^378, and gcd(A,m)=42, so this neither refutes the surviving
  near-critical half bound nor supplies a primitive-factor counterexample at index 2.
authors:
  - Codex cycle research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
certificates: [check_gap_fourteen.py]
evidence:
  - "check_gap_fourteen.json: the complete signed path, both half-words, intercept and denominator, exact gcds, all rotation mismatch counts, and positive cycle states"
tags: [cycles, denominators, transpositions, counterexample, cancellation, signed-orbits]
---

# A transposition of gap fourteen cancels the entire plus factor

## Statement

Use the raw odd-only map `S_d(x)=(3x+d)/2^v_2(3x+d)`, allowing signed
odd integers for the construction below and taking the valuation of
the absolute value when the numerator is negative. Define `d=16383=2^14-1`.
Starting at `-63`, take exactly 187 odd steps. Their valuation word `z`
has length 187 and total 320, and the resulting state is 453291.
The next arrow is

```
453291 -> 21,        3*453291+16383 = 2^16*21.
```

Define two positive words and their concatenation by

```
u = (1,z,15),        v = (15,z,1),        w = uv.
```

The words `u,v` have length `n=189` and total `B=336`; they differ by
transposing the first and last letters, whose gap is 14. For the
intercept `C_w=sum_(i<m) 3^(m-1-i)2^(sum_(r<i) w_r)` and
`D_w=2^A-3^m`, exact computation proves

```
m=378,       A=672,       gcd(A,m)=42,
G=gcd(C_w,D_w)=2^336+3^189,
den(w)=D_w/G=2^336-3^189 > 0,
rho(w)=4,    with the unique minimizing shift 189.
```

Every nonidentity rotation differs from `w`, so the word is primitive.
Its cancellation satisfies `G^2>2^A`. Thus a transposition need not
leave a proper divisor of the plus factor, and the unrestricted
transposition extension of the coprime exclusion in
[`antiperiodic-intercept-nondivisibility`](../antiperiodic-intercept-nondivisibility/README.md)
is false.

The exact inequality `2^672>=2*3^378` places this example outside the
near-critical range `2^A<2*3^m`. Also `gcd(A,m)=42`, rather than 2, so
the plus factor is not a single primitive cyclotomic factor at index 2.
The surviving near-critical questions in
[`primitive-cancellation-below-half`](../../questions/primitive-cancellation-below-half.md)
remain open.

## Proof

**The finite signed path.** The certificate implements the signed map
directly and verifies each of the 187 arrows from `-63` to 453291,
then the displayed arrow to 21. Every state is an odd integer, every
valuation is positive and exact, and no zero numerator occurs. Its
fixed iteration count prevents a failed search from passing. It prints
the entire path and word in its deterministic receipt.

**Why the plus factor cancels.** Let

```
F(z) = sum_(i=0)^187 3^(187-i) 2^(sum of the first i letters of z).
```

This is the intercept of `(z,16)`, since its last letter enters no
prefix sum. That word has length 188 and total 336. Composition along
the signed path gives

```
2^336*21 = 3^188*(-63)+16383*F(z),
16383*F(z) = 21*(2^336+3^189).                         (1)
```

Put `P=2^336+3^189` and `M=2^336-3^189`. Swapping the initial 1 and
terminal 15 of `u` changes every intermediate prefix exponent by 14.
The intercepts therefore satisfy

```
C_v-C_u = 2*(2^14-1)*F(z)=2*16383*F(z).               (2)
```

By concatenation, `C_w=3^189 C_u+2^336 C_v`. Reducing modulo `P`
gives `C_w=2^336(C_v-C_u) (mod P)`. Equations (1) and (2) prove
`P | C_w`. The certificate additionally computes `gcd(C_w,M)=1`.
Since `P` and `M` are coprime (a common divisor would divide both
`2^337` and `2*3^189` while being odd), it follows that

```
gcd(C_w,D_w)=gcd(C_w,P*M)=P.
```

The exact integer comparisons in the certificate give `M>0`,
`P^2>2^672`, and `2^672>=2*3^378`.

**Primitivity and rotation distance.** The certificate compares the
letters of `w` with each of its 377 nonidentity rotations. The least
mismatch count is 4, achieved only by shift 189. Since no count is
zero, no proper cyclic period exists. This is a complete finite
verification over all shifts, not only the half-period shift.

**Actual positive cycle.** For each rotation `R_i w`, the certificate
forms `x_i=C_(R_i w)/P`, verifies it is a positive odd integer, and
checks the 378 equations

```
3*x_i+M = 2^w_i*x_(i+1),       indices modulo 378.
```

All 378 states are distinct. Thus this word is an actual primitive
positive cycle of `3x+M`, with the displayed exact odd valuations and
reduced denominator `M`. These finite checks require no external
convergence bound or external cycle census.

## Certificates

[`check_gap_fourteen.py`](check_gap_fourteen.py) uses only the Python
standard library and exact integer arithmetic. It constructs the
signed word, verifies all stated counts and identities, computes both
factor gcds and the total gcd, checks every rotation, and verifies the
positive cycle arrow by arrow. It never relies on `assert`.

```
python3 areas/cycles/results/transposition-gap-fourteen-full-plus-cancellation/check_gap_fourteen.py
```

The script compares its deterministic result with
[`check_gap_fourteen.json`](check_gap_fourteen.json). The receipt
contains the full words and exact integers; `--write-receipt`
regenerates it. The checks also run under `python3 -O`.

## Remarks

- **Role of the signed construction.** The negative-to-positive segment
  is an auxiliary orbit of `3x+16383`. The resulting word belongs to
  the positive cycle of a different parameter, `3x+(2^336-3^189)`.
  Neither is an orbit of the positive `3x+1` problem.
- **What fails.** Full plus-factor cancellation is possible even for
  a primitive transposition word with exactly four mismatches under
  a nonidentity rotation. Consequently the coprimality condition in
  the signed-intercept theorem cannot simply be removed for all
  transpositions. No claim is made that gap 14 is the least possible
  failure.
- **What survives.** This counterexample leaves the near-critical
  restriction and any arithmetic advantage of reduced denominator 1
  available. The useful next target is to decide which signed
  crossing segments can satisfy the near-critical constraint
  `2^(2B)<2*3^(2n)`. Half-pairs with two changes that are not a
  transposition require an additional argument.
- **Controls.** This is an explicit constructed `3x+d` control, verified
  by exact arrows. It excludes no cycles of `3x+5`, `3x+7`, `3x+13`
  or `3x+61`, and makes no general cycle-exclusion claim.
- **Novelty and status.** Novelty undetermined. The counterexample is
  a written finite result with a reproducible certificate. No Lean
  formalisation or independent-session review is claimed.

## History

- 2026-11-08: Found by the Codex cycle research lane (GPT-6 Astra;
  directed by Santiago Armstrong) while challenging extension of
  the signed-crossing method beyond small transposition gaps.
