# Entering the paired recursion from the missing residue domain

2026-10-17. **Written partial construction and finite exact checks.**
Use odd-only Syracuse S, with1 absorbing, and killed divergence I-P.
For any positive odd w write P(w)=delta_(3w)-delta_w. This note supplies
two complete branches from w=1 modulo8 into the previously handled
w=3 modulo8 domain. It does not cover all w or prove Collatz.

The [mixed-pair constructor](../paired_completion/MIXED_SHRINKING_RULES.md) supplies
finite currents for an explicit subset of the3-modulo8 domain, with a
prescribed merger clock l satisfying S^l(3w)=S^(l+1)(w). Its accepted
clocks are at least3. Its unresolved outcomes remain unresolved here.
We use the elementary F and selected-halving identities of
[R25](../bridge_normal_form/BRIDGE_NORMAL_FORM.md), where F(y)=4y+1.

## 1. Why this is a different missing branch

For every a>=19, a=3 modulo16, put

```
x=2^a-1,  N=12*2^(a-4),  q=2^(a-1)-1,
w=(3^(a-1)-1)/8.
```

Then x is a full coefficient1 complementary R_N root, q<N, and w=1
modulo8. Exact prescribed prefixes give S^(a-1)(q)=w and
S^a(x)=F(3w). The needed remaining comparison is P(w), outside R30's
original domain. The [static catalogue audit](../pair_scope/PAIR_SCOPE.md)
proves that elementary identities plus all hypothetical3-modulo8 pair
bridges still leave the endpoints of this comparison distinct after the
first R26 run. Additional dynamic comparisons are therefore necessary
for that particular mechanism. The rules below supply some of them.

## 2. Branch A: one ordinary step and two elementary bridges

Suppose

```
w=16u+1,       u=1 modulo8,       v=3u.
```

Equivalently w=17 modulo128. The child v is3 modulo8 and
0<v=3(w-1)/16<w. Direct arithmetic gives

```
S(3w)=72u+5=F(18u+1),
S(w)=12u+1=F(3u),
18u+1=2(9u)+1.
```

Since9u is1 modulo8 and canonical,18u+1 is its selected partner.
The left prefix followed by the F bridge and selected-halving bridge
ends at9u=3v. The right prefix followed by its F bridge ends at3u=v.
Subtracting gives an explicit local current L_A with

```
div L_A=P(w)-P(v).                                   (1)
```

If J_v certifies P(v), then L_A+J_v certifies P(w). The orientation is
positive; this is different from the even recursive branches of R30.

For the clock, the selected partner of9u has run length2. Consequently

```
S^j(3w)=S^(j-1)(3v)  for j>=3,
S^j(w)=S^(j-1)(v)    for j>=2.
```

Thus any child merger clock l>=2 gives parent clock l+1:
S^(l+1)(3w)=S^(l+2)(w). No absorption assertion is used in this identity.

## 3. Branch B: two ordinary steps and two selected partners

Suppose w=105 modulo256, and put

```
v=(9w-1)/16.
```

Then v=11 modulo16, so both v and3v are canonical, v=3 modulo8,
and0<v<w. The first two valuations on3w are1,2; on w they are2,1.
The exact endpoints are

```
S^2(3w)=(27w+5)/8=2(3v)+1,
S^2(w)=(9w+7)/8=2v+1.
```

These are selected partners of3v and v. Append their elementary bridges
and subtract to obtain another explicit local current

```
div L_B=P(w)-P(v).                                   (2)
```

The left partner has selected run length2; the right has length3.
Therefore S^j(3w)=S^(j-2)(3v) for j>=4 and
S^j(w)=S^(j-2)(v) for j>=5. A child clock l>=2 gives parent clock l+2.
As in branch A, the child current is added, not subtracted.

The A and B domains are disjoint, being1 and9 modulo16 respectively.
Every recognized parent enters the3-modulo8 constructor after one strict
parameter decrease. Failure of either parent recognition or child
recognition is reported explicitly, never interpreted as nonconvergence.

## 4. Complete mixed cylinders and actual Mersenne roots

Let a complete accepted child word from the mixed-pair theorem have
origin v=r modulo M, where M is its power-of-two modulus. Branch A has
the unique complete parent cylinder

```
3w=16r+3 modulo16M.                                  (3)
```

For branch B require r=11 modulo16; its parent cylinder is

```
9w=16r+1 modulo16M.                                  (4)
```

Odd3 and9 are invertible modulo16M, so both are executable exact
binary cylinders. All necessary branch bits are retained. Every A
parent is17 modulo128. Every B parent is105 modulo256. The child word
has its proved prescribed finite depth, so the parent is accepted.
There are A parents of every finite mixed word and hence arbitrarily
large recursive depths. B includes the terminal word and every word
whose origin is11 modulo16; no other words are claimed for it.

Nonempty positive integer witnesses follow by CRT: for A choose the
child in its binary cylinder and v=0 modulo3, then w=1+16v/3.
For B choose v=5 modulo9, then w=(16v+1)/9. These witnesses prove
actual integer integrality, rather than relying only on2-adic notation.

For each parent residue c=1 modulo8 modulo2^m, elementary lifting gives
a unique a=3 modulo16 modulo2^(m+1) such that

```
3^(a-1)=1+8c modulo2^(m+3).                          (5)
```

Start with exponent a-1=2 modulo16 and lift one bit at a time using
3^(2^j)=1+2^(j+2) modulo2^(j+3). Each lift has exactly one choice.
This realizes each complete parent word in the actual exponential w
from Section1. Two explicit terminal examples are

| Parent branch | Parent w cylinder | Exponent cylinder | Pair clock |
|---|---|---|---:|
| A |1681 modulo2048|1699 modulo4096|4|
| B |105 modulo2048|659 modulo4096|5|

For every exponent in the A class, respectively B class,

```
S^(a+4)(2^a-1)=S^(a+4)(2^(a-1)-1),
S^(a+5)(2^a-1)=S^(a+5)(2^(a-1)-1).                  (6)
```

The normalized old return is(3w-1)/2 on A and3w on B. Both have
unbounded ratio to x along their exponent progression. These are
therefore smaller-seed mergers through the old growing-return obstruction,
including portions of the separate a=3 modulo16 family. No claim of a
uniform residual density improvement follows from this construction.

## 5. Supplied-input conversion and checks

Let D_x be the raw R26 bridge from x to3w, J_w the accepted pair current,
and H_(q,w) the prescribed q prefix. Then

```
div(D_x+J_w-H_(q,w))=delta_x-delta_q.                 (7)
```

Add a supplied finite exact current for q and extract a nonnegative
absorption current from that finite graph. The construction uses only
supplied or explicitly prescribed edges. Scale the entire identity for
any positive source multiplicity. Separate root certificates may reuse
known inputs; this is not a joint annular capacity assertion.

The code keeps R30 unchanged and imports its extended domain3 constructor.
The default checker is read-only:

```
python3 experiments/residual_progress/pair_one/check_pair_one.py
```

The receipt records direct domains, mixed-word examples, modular exponent
lifts, actual Mersenne bridges and a capped supplied-input conversion.
The small current for315 uses only a supplied105 path and the branch B
certificate. The much larger a659 conversion is regenerated under a
10000-step input-discovery cap and recorded by exact current hashes.
Current arithmetic and merger clocks are checked independently with
ordinary prefixes. These finite checks support the implementation; the
infinite claims rest on the written identities above.

Universal coverage, external novelty and human/formal verification remain
unestablished. In particular a147 is an explicit unresolved child example
for the present rule, despite entering parent branch B.
