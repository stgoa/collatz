# Mixed shrinking rules for the pair (3w,w)

2026-10-17. **Written arithmetic proof, executable constructor, and finite
certificates.** This extends [R30](../second_return/SHRINKING_PAIRS.md) by
two complete recursive branches. Arbitrary finite mixtures have explicit
nonempty cylinders, including actual Mersenne residual roots. Recognition
terminates by integer decrease; several branches remain unresolved. No
universal convergence, novelty, human review, or formal verification is claimed.

Use odd-only Syracuse S, absorbing at1, killed divergence div=I-P, and
the canonical set B from [R25](../bridge_normal_form/BRIDGE_NORMAL_FORM.md).
Write

```
P(w)=delta_(3w)-delta_w,          w=3 modulo8, w>0.
```

A certificate for P(w) is a finite signed integer current, not an absorption
assumption on both its endpoints. Once either endpoint has a supplied finite
absorption current, the signed bridge certifies the other endpoint by the
finite component argument. Reversing a pair changes the current sign.

## 1. Complete paired-run identities for both parities of h

Put `h=v_2(3w-1)>=3`, and C=(3w-1)/2^h. Starting from
`3w=1+2^h C` and `S(w)=1+2^(h-1)C`, apply

```
S(1+2^e c)=1+3*2^(e-2)c        (c odd, e>=3).        (1)
```

Every use of (1) has valuation exactly2.

For even h=2k+2, k>=1, set z=3^k C. Then

```
S^k(3w)=4z+1,              S^(k+1)(w)=2z+1.          (2)
```

For odd h=2k+3, k>=0, set z=3^k C. Then

```
S^k(3w)=8z+1,              S^(k+1)(w)=4z+1.          (3)
```

Thus no parity of h is discarded from the arithmetic description. The
identities do not assert that both resulting pairs are always certifiable.

In the even case, if z belongs to B, R30's terminal rule applies. The
selected partner2z+1 merges with z after A=v_2(2z+2) odd steps, giving

```
S^(k+A)(3w)=S^(k+A+1)(w).                            (4)
```

The three recursive domains below are disjoint from this terminal case.

## 2. The new odd-h branch O_k

In (3), suppose z=3 modulo8. Then3z=1 modulo8 is canonical, and
6z+1 is its selected partner. Its selected run has length2. Also

```
S(8z+1)=6z+1,          S(4z+1)=S(z).                 (5)
```

Append the elementary current from6z+1 to3z to the left prefix in(3),
and the sibling current from4z+1 to z to the right prefix. Their difference
is an explicit finite current L_w with

```
div L_w=P(w)-P(z).                                  (6)
```

Therefore a child current J_z for P(z) is **added**:
`J_w=L_w+J_z`. Its parameter is

```
w'=z=(3^(k+1)w-3^k)/2^(2k+3),
0<w'<(3/8)(3/4)^k w<w/2.                            (7)
```

The domain is complete: h=2k+3 and z=3 modulo8, with no unmentioned
valuation or future-absorption condition.

If the child has prescribed merger clock l>=2,
`S^l(3w')=S^(l+1)(w')`, then

```
S^(k+l+1)(3w)=S^(k+l+2)(w).                          (8)
```

Indeed the left path is at6z+1 at time k+1, and its next l arrows agree
with the l-th successor of3z since l>=2. The right path is at4z+1 at
time k+1, and its next l+1 arrows agree with the corresponding successors
of z. Every accepted child in this constructor has l>=3, so the condition
l>=2 is always met.

## 3. Two even-h recursive branches

### New branch E1_k: z=29 modulo64

In(2) write

```
z=4u+1,       u=7 modulo16,
w'=S(u)=(3u+1)/2=(3z+1)/8=3 modulo8.                (9)
```

The arrow from u has valuation1. By the sibling identity, the left side
of(2) reaches w' at time k+1. On the right side,

```
S^(k+1)(w)=8u+3,
S(8u+3)=12u+5,
S^2(8u+3)=9u+4=6w'+1.                              (10)
```

The arrows displayed in(10) have valuations1 and2 respectively. Since
3w' is canonical1 modulo8, the last state is its selected partner of
length2. Append that selected current to the right prefix. The difference
of the left and right currents has divergence

```
P(w)+P(w').                                         (11)
```

The child current must therefore be **subtracted**. Moreover

```
w'=(3^(k+2)w+4^(k+1)-3^(k+1))/2^(2k+5),
0<w'=(3z+1)/8<w/2.                                 (12)
```

Here z<w follows from `z<(3/4)^(k+1)w`, and w>1.
If the child merger clock is l>=2, the parent clock is k+l+2:

```
S^(k+l+2)(3w)=S^(k+l+3)(w).                          (13)
```

The left path reaches w' at k+1; the right reaches6w'+1 at k+3.
Apply the child equality after the selected partner has merged.

### Existing branch E2_k: z=101 modulo128

For completeness retain R30's branch:

```
z=4u+1,       u=25 modulo32,
w'=S(u)=(3u+1)/4=(3z+1)/16=3 modulo8,
w'=(3^(k+2)w+4^(k+1)-3^(k+1))/2^(2k+6).             (14)
```

The local current again has divergence P(w)+P(w'), so the child current
is subtracted. Its parameter satisfies w'<w/4, and its merger clock also
increases by k+2. The proof and its exact prefix signs are retained in
R30 and independently rechecked by the new runner.

### Combined finite constructor

The algorithm first checks the even terminal rule, then the relevant
recursive domain O, E1, or E2. All remaining domains return unresolved.
Every recursive call remains in3 modulo8 and has positive parameter
less than w/2. Consequently the recognizer terminates for every positive
input and cannot silently loop on an uncovered branch.

The signs and clock increments are summarized here:

| Branch | k | Child numerator A w+B | Denominator2^p | Child sign | Clock increment |
|---|---:|---|---|---:|---:|
| O | >=0 | 3^(k+1)w-3^k | 2^(2k+3) | +1 | k+1 |
| E1 | >=1 | 3^(k+2)w+4^(k+1)-3^(k+1) | 2^(2k+5) | -1 | k+2 |
| E2 | >=1 | same as E1 | 2^(2k+6) | -1 | k+2 |

For each row, `J_w=L_w+sign*J_child`; equivalently
`div L_w=P(w)-sign*P(child)`. No signed row or source multiplicity is
discarded when the branches are composed.

## 4. Every finite mixed word has a complete nonempty cylinder

Fix a terminal parameter j>=1 and use R30's complete terminal class

```
3^(j+1)v = 3^j+2^(2j+2) modulo2^(2j+5).             (15)
```

Its terminal z is1 modulo8, so its merger clock is j+2. For j=1 this
is v=59 modulo128.

Now prescribe **any finite word** W in the three rows of the table,
allowing any of their stated k values and any order of signs. Work
backward from (15). If the current required child class is
`v=c modulo2^M` and the preceding row is `(A w+B)/2^p`, require

```
A w+B = 2^p c modulo2^(M+p),
w = (2^p c-B) A^(-1) modulo2^(M+p).                 (16)
```

A is odd, so each step defines exactly one binary residue class. It is
3 modulo8, and its positive members map to positive integer members of
the child class. Positivity follows directly from each displayed map on
positive w=3 modulo8. The conditions in(16) also force the exact parent
branch, rather than merely its affine formula:

- For O, an odd child gives exact h=2k+3. Child3 modulo8 is precisely
  the condition z=3 modulo8.
- For E1/E2, rewrite the numerator as
  `3^(k+1)(3w-1)+2^(2k+2)`. The odd child enforces exact h=2k+2.
  Child3 modulo8 forces z=29 modulo64 or101 modulo128 respectively.

The latter residues are5 modulo8 and hence noncanonical, so no earlier
terminal case is triggered. Distinct branches in the word remain the
ones prescribed. The final terminal class remains exact as well.

Thus(16) is a complete cylinder for this word followed by terminal(15).
Its modulus is `2^(2j+5+sum p)`. Every cylinder has arbitrarily large
positive members. No finite-word existence argument is being promoted
to an infinite positive orbit: integer decrease prevents such an orbit
for this recursion.

The exact prescribed merger clock is

```
l(W,j)=j+2 + sum_O(k+1) + sum_E1,E2(k+2),
S^l(3w)=S^(l+1)(w).                                 (17)
```

This includes arbitrarily long **mixed** recursion and the earlier pure
E2 family. It is not a list of isolated sampled templates.

## 5. Actual Mersenne residual families and supplied currents

Every cylinder c=3 modulo8 modulo2^M lifts, by R30's exact binary
exponent lifting, to a unique a=7 modulo16 modulo2^(M+1) such that

```
(3^(a-1)-1)/8 = c modulo2^M.                         (18)
```

The lift is elementary: after b=a-1 is fixed modulo2^i, exactly one of
b and b+2^i fixes the next bit, because
`3^(2^i)=1+2^(i+2) modulo2^(i+3)`. The function `mersenne_cylinder`
implements this finite modular calculation without constructing3^a.

For each such a>=7 put

```
x=2^a-1, q=2^(a-1)-1, N=12*2^(a-4), w=(3^(a-1)-1)/8.
```

These are actual weight1 complementary R_N roots, q<N, and the former
normalized return f=3w is canonical with unbounded f/x along every
progression. R30's identities `S^(a-1)q=w`, `S^a x=4(3w)+1`, together
with(17), give

```
S^(a+l)(x)=S^(a+l)(q).                              (19)
```

For terminal j=1, some new classes are

| Mixed word before terminal | a class | Exact merger time |
|---|---|---|
| O_0 | 631 modulo2048 | a+4 |
| O_1 | 7143 modulo8192 | a+5 |
| E1_1 | 3655 modulo32768 | a+6 |
| E2_1 | 2887 modulo65536 | a+6 |

All finite mixed words have the same explicit construction. Only the
last displayed row was already in R30's complete recursive family.

Let D_x be the old run bridge from x to3w, and H_(q,w) the explicit
prefix from q to w. The new current is

```
B_x=D_x+J_w-H_(q,w),       div B_x=delta_x-delta_q.    (20)
```

Given a finite exact input H_q, adding it certifies delta_x. A finite
signed input is sufficient: each component of the nonzero-row graph
away from1 has divergence sum zero; the sole positive source must
therefore lie in the absorbing component. An actual nonnegative path
current can be extracted using just those existing edges. No assumption
of universal cycle absence is used. Multiplying all inputs and bridge
rows by an integer coefficient preserves that coefficient exactly.

The finite a=631 demonstration supplies only the path from q, discovered
with a5000-step cap. Both x and its old return f are absent from the
elementary-plus-forward saturation of **that supplied single-seed path**.
The new signed bridge then certifies x. This check makes no claim about
the much larger, unconstructed union of all lower-seed paths through N.
The receipt stores deterministic input/output hashes and reproduces the
full conversion; it does not store an enormous U_N table.

## 6. Exact cylinder measure of the stated recognizer

This is a property of the explicit partial rule, not a contraction of
weighted R_N source mass or a probability of arbitrary orbit success.
Condition binary-cylinder measure on w=3 modulo8. Exact h=2k+2 has
measure4^(-k). Conditional on h, z ranges uniformly over odd binary
classes. The canonical set has relative odd measure1/2 by R25. Thus the
terminal mass is

```
t=(1/2) sum_(k>=1) 4^(-k)=1/6.
```

Each recursive row has a single class modulo2^(p+3), hence relative
measure2^(-p). Summing the complete branch families gives

```
r_O=1/6,        r_E1=1/96,        r_E2=1/192,
r=35/192.                                           (21)
```

Conditional on a recursive cylinder, its child is uniformly distributed
in3 modulo8: parent increments2^(p+3) become child increments8A, and A
is odd. This proves the product rule for finite words by exact cylinder
arithmetic; no independence model for Collatz iterates is assumed.

The measure accepted after finitely many recursive calls is therefore

```
t*(1+r+r^2+...)=32/157.                              (22)
```

After d unresolved recursive calls their total cylinder measure is r^d.
It tends to zero. Isolated infinite-valuation binary points and their
finite affine preimages have measure zero as well. All ordinary positive
inputs already have finite recognition by the decreasing parameter.
The immediately or eventually rejected part has measure125/157.
The prior R30 rule has the corresponding value32/191.

No quantitative count for a growing weighted interval, new R_N leading
coefficient, or all-future-horizon error bound is inferred from(22).

## 7. The remaining arithmetic is explicit

Removing the condition z=3 modulo8 from the odd branch is invalid as an
elementary substitution. At w=19, h=3 and z=7, the proposed endpoints
6z+1=43 and3z=21 have distinct canonical minima43 and1. Thus the known
elementary bridges do not certify their equality. This does not rule
out a deeper ordinary common tail.

The full odd-h residual is the pair `(8z+1,z)`, or after one left arrow
`(6z+1,z)`. Our O rule handles exactly the stated z class. In the even
case, noncanonical z is either an F-sibling or a selected halving partner.
Those other cases can produce powers-of-three pairs or pairs `(4q+3,q)`;
they have not all been reduced to the present parameter domain. The old
examples a=7 and a=23 remain unresolved by this recognizer.

Thus the new result is a complete three-branch arithmetic grammar with
strict parameter decrease on each recursive call and a full cylinder for
every finite word. A universal grammar covering the remaining domains
is still open.

## 8. Reproduction

```
python3 experiments/residual_progress/paired_completion/check_mixed_pairs.py
```

The default is read-only; `--write-receipt` regenerates the receipt and
the small signed table for P(499). Checks cover4096 domain inputs,
510 complete mixed cylinders,28 long words through depth64, four actual
Mersenne bridges, exact merger clocks, full source multiplicity, and one
conversion from a supplied lower current. The full arithmetic constructor
uses only prescribed finite prefixes. The5000-step absorption cap is
used solely to discover that one finite demonstration input.
