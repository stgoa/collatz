---
id: near-critical-four-mismatch-corpus-counterexample
kind: result
title: An existing 3x+295 cycle refutes both near-critical half-cancellation bounds
status: written
claim: >
  Raw odd-only clock, any 3x+q. The word w=(1,1,3,1,2,1,1,1,1,2,1,5)
  is primitive with m=12, A=20, C_w=1291961, D_w=517135 and
  G=gcd(C_w,D_w)=1753. Its rotation distance is 4, attained exactly
  at shifts 5 and 7, both coprime to 12. It is near-critical:
  3^12=531441 < 2^20=1048576 < 2*3^12=1062882. Nevertheless
  G^2=3073009>2^20. Also e=gcd(A,m)=4 and the homogeneous primitive
  factor Phi_4(2^5,3^3)=32^2+27^2=1753 equals G, so
  g_prim=1753>2^(A/2)=1024. This refutes forms (A-prime) and (B)
  of primitive-cancellation-below-half for near-critical words with
  m>=9 and rotation distance at most 4. The word is the already
  recorded positive 3x+295 cycle with minimum 737; no new cycle or
  statement about a 3x+1 cycle is claimed.
authors:
  - Codex cycle research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [actual-cycles-3x-d-corpus]
certificates: [check_near_critical.py]
evidence:
  - "check_near_critical.json: self-contained exact intercept, gcd, cyclotomic factor, all rotations, actual cycle and inequalities"
tags: [cycles, denominators, near-critical, primitive-cancellation, counterexample, four-mismatches]
---

# An existing 3x+295 cycle refutes both near-critical half-cancellation bounds

## Statement

Consider the positive valuation word

```
w = (1,1,3,1,2,1,1,1,1,2,1,5).
```

It has length `m=12`, total `A=20`, intercept `C_w=1291961`,
denominator `D_w=2^20-3^12=517135`, and cancellation `G=1753`.
Every nonidentity rotation differs from it; the minimum mismatch
count is 4, attained at shifts 5 and 7. It is near-critical because

```
531441 = 3^12 < 2^20 = 1048576 < 2*3^12 = 1062882.
```

Both half-cancellation inequalities fail:

```
G^2 = 3073009 > 1048576 = 2^A,
g_prim = gcd(G,Phi_4(32,27)) = 1753 > 1024 = 2^(A/2).
```

Here `e=gcd(A,m)=4` and `Phi_4(x,y)=x^2+y^2`, so the full
primitive cyclotomic factor cancels. This refutes the universal
near-critical forms (A′) and (B) in
[`primitive-cancellation-below-half`](../../questions/primitive-cancellation-below-half.md).

The cycle itself is already in
[`actual-cycles-3x-d-corpus`](../actual-cycles-3x-d-corpus/README.md),
at `d=295`, minimum 737, discovery seed 7. The contribution here
is recognizing and verifying its consequences for the later
cancellation questions, not discovering a new `3x+d` cycle.

## Proof

### 1. Exact arithmetic and near-criticality

Using the intercept definition
`C_w=sum_(i<m)3^(m-1-i)2^(sum_(r<i)w_r)` gives

```
C_w = 1291961 = 737*1753,
D_w = 517135 = 295*1753,
gcd(737,295)=1.
```

Thus `G=gcd(C_w,D_w)=1753`, and the reduced denominator is 295.
The displayed integer comparisons establish `D_w>0`,
`2^A<2*3^m`, and `G^2>2^A` without floating-point estimates.

Since `e=4`, the homogeneous factorization is

```
D_w = (32-27)(32+27)(32^2+27^2)
    = 5*59*1753.
```

Therefore `Phi_4(32,27)=1753=G`, so the primitive cancellation
also exceeds `2^(A/2)=1024`.

### 2. Every rotation and primitivity

The exact mismatch counts are

| Shift | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Mismatches | 8 | 6 | 7 | 8 | 4 | 8 | 4 | 8 | 7 | 6 | 8 |

No count is zero, so the word is primitive. The minimum is 4,
and both minimizing shifts are coprime to 12. In particular,
the half-period shift 6 has 8 mismatches; this counterexample
does not belong to the two-change half-pair families of the
recent signed-crossing exclusions.

### 3. The actual positive cycle

The complete raw odd-only `3x+295` cycle is

```
737 -> 1253 -> 2027 -> 797 -> 1343 -> 1081 -> 1769
    -> 2801 -> 4349 -> 6671 -> 5077 -> 7763 -> 737.
```

Its states are distinct positive odd integers. At each arrow,
`3*x_i+295 = 2^w_i*x_(i+1)` and `x_(i+1)` is odd, so the
prescribed valuation is exact. These identities independently
verify the word and the reduced denominator. They involve no
assumption that all `3x+d` orbits converge.

## Certificates

[`check_near_critical.py`](check_near_critical.py) recomputes every
stated number directly from the displayed word and states. It
checks the intercept and gcd, the homogeneous factorization,
near-criticality, both violated bounds, every nonidentity rotation,
and every exact cycle arrow. It also verifies that the weaker
[`rotation-defect-denominator-candidate`](../../questions/rotation-defect-denominator-candidate.md)
inequality still holds for this example at `s=4`.

```
python3 areas/cycles/results/near-critical-four-mismatch-corpus-counterexample/check_near_critical.py
```

The script uses only the standard library and exact integers.
Its proof checks are self-contained: it does not import the
historical corpus or depend on its discovery computation. Its
deterministic receipt is
[`check_near_critical.json`](check_near_critical.json), regenerated
with `--write-receipt`; all checks also run under `python3 -O`.

## Remarks

- **What is refuted.** Forms (A′) and (B), as universally
  quantified for near-critical primitive words with `m>=9` and
  `rho<=4`, are false. The primitive factor is fully present
  here, so separating algebraic from primitive cancellation
  does not rescue these particular inequalities.
- **What remains open.** Part (C) asks for mismatch-dependent
  exponents and a possible length threshold `m_0(s)`. This
  twelve-letter example does not rule out an asymptotic version
  with a larger threshold. The weaker denominator candidate
  also survives this test. No conclusion about denominator 1
  or the Collatz conjecture follows from this `q=295` cycle.
- **Why earlier tests missed it.** The all-shift census with
  letters at most 3 excludes this word, which contains a 5.
  The small half-defect exclusions concern the half-period
  rotation, which has 8 mismatches here. Their statements
  and finite certificates are consistent with this example.
- **Provenance and novelty.** The exact cycle was already in
  the committed corpus before these conjectures were posed.
  Novelty of the mathematical interpretation is undetermined.
  No new-cycle claim is made.
- **Status.** Written finite result with a reproducible
  certificate; no independent-session review or Lean
  formalisation is claimed.

## History

- 2026-11-08: Codex cycle research lane (GPT-6 Astra; directed
  by Santiago Armstrong) re-examined the stored corpus for
  primitive cancellation and all-shift rotation distance,
  identified this existing cycle as a near-critical
  counterexample, and independently rechecked its arithmetic.
