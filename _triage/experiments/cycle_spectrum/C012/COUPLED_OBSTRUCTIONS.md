# C012 — Three defects can retain an arbitrary shared background

**Status: written elementary structural and counting obstructions.**
The results below rule out specific reductions to a fixed S-unit group
or a bounded number of controlled-height S-unit terms. They do not
refute the proposed denominator bound, prove bounded-denominator
finiteness at fixed defect count, or exclude an integer cycle. All
cycles use the raw positive odd-only map without an absorber. No
novelty or formal-verification claim is made.

## 1. A primitive three-defect family with arbitrary background

For any positive integer t, let U be any word containing t copies of
1 and 2t copies of 2, in arbitrary order. Put

```text
n=length(U)=3t,  A_U=5t,
w_U=(3,U,4,U,5,U),
m=9t+3,         A=15t+12.
```

The markers 3, 4 and 5 occur exactly once each. Hence `w_U` is
primitive: a proper repetition would repeat every marker. Rotation by
`n+1` preserves all three copies of U and cycles the three markers.
It has exactly three mismatches, with signed differences `1,1,-2`.

Every nonidentity rotation changes the entry at each of the three
marker positions. Uniqueness of each marker prevents it from agreeing
at its original position after a nonzero shift. Thus

```text
min_(1<=r<m) Hamming(w_U,R_r w_U) = 3.             (1)
```

The alphabet is fixed, the displayed mismatch amplitudes are at most
two, and the period grows with t. The background order is arbitrary
at the stated fixed totals. We have

```text
2^A/3^m = (4096/27)(32768/19683)^t > 1,
A<2m exactly when t>2.
```

Each word therefore gives a positive rational cycle. Its rotated
intercepts divided by their common gcd with D are positive odd
integers, giving an actual `3x+q` cycle at reduced `q=D/g`. A repeated
state would force repeated exact valuations and contradict primitivity.
No claim that this q is small is made. For every t>=3 this example
satisfies both total-exponent conditions `m log_2 3<A<2m` necessary
for a hypothetical nontrivial denominator-one cycle. These conditions
are not sufficient for denominator one or integer-cycle realization
at parameter one.

Consequently a fixed defect count does not bound the internal word
complexity of shared arcs. This example has gcd(shift,m)=n+1, which
grows. The coprime-shift restriction would remove this particular
construction and must not be silently imposed on the unrestricted
question.

## 2. The lawful intercepts escape every fixed S-unit group

For this separate illustration, take `V=(5,2^n)`, where here
`2^n` denotes n repetitions of the valuation 2. Direct concatenation
gives

```text
C_V = 3^n + 32(4^n-3^n)
    = 32*4^n-31*3^n.                              (2)
```

For every finite set S of primes, choose a positive n divisible by
`p-1` for every `p in S` other than 2 and 3. There are arbitrarily
large such n. The finite multiplicative group modulo p gives
`2^n=3^n=1 mod p`, and therefore

```text
C_V = 1 mod p   for every p in S minus {2,3}.
```

Also C_V is odd and is nonzero modulo 3. Since C_V>1, it has a prime
divisor outside S. In particular these legal shared-arc intercepts
are not all units in any fixed S-unit group. This is elementary and
does not import an S-unit theorem.

They occur in the primitive words `(1,V,3,V,4,V)`, whose unique
markers again give minimum rotation distance three. Here the totals
are `m=3n+6,A=6n+23`, so `A>2m`: this prime-escape illustration is
outside the total range of a nontrivial q1 cycle. The counting theorem
uses Section 1's different family and retains `A<2m`.

This fact alone does **not** rule out a bounded-term S-unit argument:
(2) is already a sum of two such terms. The stronger counting
obstruction below addresses that distinction.

## 3. No uniform bounded-term rewrite at controlled exponent height

Fix a finite set F of rational coefficients, fixed nonzero rational
generators `gamma_1,...,gamma_r`, a positive integer K and a real
constant H>0. Consider expressions with at most K terms of the form

```text
epsilon*f*gamma_1^e_1 ... gamma_r^e_r,
epsilon in {-1,1},  f in F,  e_j in Z,  |e_j| <= Ht. (3)
```

**Theorem.** For every sufficiently large integer t, some word U of
length 3t with exactly t ones and 2t twos
has intercept C_U that cannot be expressed in the form (3).
Nevertheless `w_U` has the fixed minimum defect count three in (1),
positive D, and `A<2m`.

**Proof of distinctness.** Positive words with the same length and
total have distinct intercepts. Indeed, for a word of length n>=2,

```text
C_U = 3^(n-1) + 2^a_0 C_tail,
```

and `C_tail` is odd. Thus `v_2(C_U-3^(n-1))` recovers the first
valuation. Division recovers C_tail, and induction recovers the first
n-1 valuations. The fixed total recovers the final valuation, which
the intercept itself omits. Hence the words used in the theorem give
exactly `binom(3t,t)` different intercepts at the same length 3t and
total `A_U=5t`.

**Proof by counting.** The number of possible individual terms in
(3) is at most

```text
2 |F| (2 floor(Ht)+1)^r.
```

Allowing zero padding, at most

```text
[1+2 |F| (2 floor(Ht)+1)^r]^K                     (4)
```

different sums result. This is a polynomial bound in t. On the other
hand `binom(3t,t)=product_(j=1)^t (2t+j)/j >= 3^t`, which eventually
exceeds (4). At least one lawful intercept is therefore missing from every
such collection of expressions. QED.

The quantifiers allow any fixed generators, coefficient set, term
count and linear exponent-height constant. Signed terms and negative
exponents are allowed in the counting argument. In particular the
claim applies to the fixed group generated by 2 and 3 used in C003.
Every term in the original positive intercept formula has exponents
bounded linearly in t, so that scale is already present in the problem.

This does not prove that all conceivable fixed-dimensional arithmetic
reductions fail. A successful argument could use a coupled relation
without separately rewriting each C_U, allow new coefficients or
generators with a justified height estimate, or control representations
with much larger term exponents. Those would be additional mathematical
steps. Neither fixed rotation defect count nor the existence of shared
arcs supplies them by itself.

## 4. Small exact example and finite checks

For `V=(5,2)`, equation (2) gives C_V=35. The complete word is

```text
w=(1,5,2,3,5,2,4,5,2),
m=9, A=29, C=151215095, D=536851229,
g=1, q=536851229.
```

Its raw cycle, in this displayed orientation, is

```text
(151215095,495248257,63206125,181617401,135212929,
 29452813,156302417,62859905,22669717).
```

The eight nonidentity rotation distances are
`(9,9,3,9,9,3,9,9)`. This demonstrates the minimum-three statement on
an actual cycle and does not test small denominator behavior.

A separate exact exploratory calculation checked distinct intercept
counts `2,6,20,70` for balanced backgrounds of lengths `2,4,6,8`.
Equation (2) was also checked modulo the prime sets `{5}`, `{5,7}`
and `{5,7,11,13}` at `n=4,12,60`; all residues are 1. These are
calibrations of the written proofs, not an exhaustive census or a
certificate of the all-size assertions.

The reproducible extension in [check_shared_arcs.py](check_shared_arcs.py)
and [its receipt](shared_arc_audit.json) also checks Section 1's
admissible-total family at `t=3,4,5`: respectively 84, 495 and 3,003
backgrounds. Its finite counts do not prove the expression-counting
theorem.

### Actual correlations can still give arithmetic information

The separate prime-escape family also calibrates the scope of the
obstruction. Let V have length n and total A_V, put `u=2^A_V`,
`alpha=3^(n+1)` and `E=3C_V+u`, and use the starting cut immediately
after the marker 1 in `(1,V,3,V,4,V)`. The three blocks are
`(V,3),(V,4),(V,1)` and all have the same intercept E. Thus

```text
C_cut = E S,
S=alpha^2+8u alpha+128u^2,
D=256u^3-alpha^3.
```

Since D is coprime to 2u, the following polynomial reduction is exact
for divisibility. Modulo S,

```text
D = 64u^2(alpha-12u) mod S,
S = 368u^2 = 16*23u^2 mod (alpha-12u).
```

It follows that `gcd(D,S)|23`, and hence `gcd(D,C_cut)<=23E`.
The arbitrary shared intercept can therefore be handled as one
correlated factor in this example. This is why the separate-intercept
counting obstruction must not be promoted to an impossibility theorem
for the complete coupled arithmetic. No general denominator estimate
is inferred from this calibration.

### Draft correction

An initial chat calculation wrote the first term of (2) as `3^(n+1)`
and consequently gave residue 3. The root reviewer caught the
off-by-one. The correct term is `3^n` and the correct residue is 1;
already `U=(k,2)` has intercept `3+2^k`. The incorrect formula was
never saved as a result. The corrected formula is used throughout
this note; the new-prime conclusion is unchanged.

## 5. Scope and decision

The two-defect theorem in C011 is consistent with this construction:
its exact minimum distance is three. The arbitrary-modulus cancellation
family in `COUPLED_SYSTEM.md` supplies a separate obstruction to the
matrix elimination; the present family explains why free shared
intercepts cannot simply be treated as fixed S-unit data.

The known d5, d7 and d13 cycles are unaffected. These arguments impose
no new exclusion on them and do not reinterpret a rational rescaling
as an integer cycle. No published cycle-period or local-minimum record
is improved.

| Required field | Outcome |
| --- | --- |
| Objects | Primitive positive valuation words with minimum rotation distance three, arbitrary shared-background order, and positive totals below 2m. |
| Structural gain | A fixed alphabet, bounded defect amplitudes and fixed defect count retain exponentially many lawful arc intercepts. |
| Translated unresolved gap | A uniform estimate must exploit coupled rotation compatibility; fixed-dimensional S-unit inputs do not follow from the defect count. |
| Worked example | The exact nine-state q536851229 cycle above. |
| Known-cycle controls | No claim excludes raw d5/7/13 cycles or repetitions of the denominator-one fixed point. |
| Cheapest meaningful next test | Test a concrete size estimate on the two surviving coupled forms, retaining the actual background dependence. |
| Intermediate milestone | Uniform fixed-defect bounded-denominator finiteness, or a quantitative relative-cancellation bound, remains open. |
