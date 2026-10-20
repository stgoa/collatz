# C013 — Paired-state divisibility and the height conversion obstruction

**Status: written elementary run law and an exact infinite actual-cycle
obstruction to a proposed height conversion.** No bound forcing rotation
distance to grow at fixed reduced denominator is proved here. The
construction below has growing denominators, so it does not refute that
target. All states and arrows use the raw positive odd-only map.

## 1. The information supplied by an actual shared cycle

Let `n_0,...,n_(m-1)` be a primitive positive odd cycle at reduced parameter
q, with `m>1`, and let

```
3n_i+q=2^a_i n_(i+1),   a_i>=1,
A=sum a_i,   D=2^A-3^m>0,
L=min n_i,   H=max n_i,   B=floor(log_2(H/L)).
```

Fix a nonidentity rotation h, and set `z_i=n_(i+h)-n_i`. Primitivity
makes every z_i nonzero; oddness makes it even. These are differences
of states in the same cycle, so they also satisfy the actual overlap
identities

```
sum_(i in each orbit of +h on Z/mZ) z_i=0.          (1)
```

At a position where `a_i=a_(i+h)`, subtraction gives

```
2^a_i z_(i+1)=3z_i.                               (2)
```

If t consecutive positions agree, and their valuation sum is E, then

```
2^E z_end=3^t z_start,
z_start=2^(E+1)k,    z_end=2*3^t k                (3)
```

for some nonzero integer k. The last assertion uses coprimality of 2
and 3 and the evenness of z_end. It remains valid for t=E=0.
Consequently

```
H-L >= 2 max(2^E,3^t).                            (4)
```

If the selected rotation has s mismatches, they divide its m-s agreeing
positions into s cyclic runs. Some run has
`t>=ceil(m/s)-1`. Equation (4) is a diameter lower bound, not a lower
bound for the minimum L.

## 2. Exact denominator consequences, retaining the height cost

Put `delta=A log 2-m log 3>0` and `K_B=2^(B+1)-1`.
Since `H/L<2^(B+1)`, each run gives

```
L > 2 max(2^E,3^t)/K_B.                           (5)
```

The full-cycle product gives

```
delta=sum_i log(1+q/(3n_i)) < mq/(3L).
```

Combining these statements yields

```
q > 6 delta max(2^E,3^t)/(m K_B),
q > 6 delta 3^(ceil(m/s)-1)/(m K_B).               (6)
```

These inequalities require no circular order and no assumption `q<=L`.
They retain the denominator q, the selected rotation, and the actual
height B. Replacing B by a function of s without proof would change the
statement.

For an entirely rational finite check, set `eta=D/2^A=1-exp(-delta)`.
Then `0<eta<delta`, and the weaker consequence of (6) is exactly

```
6 D max(2^E,3^t) < m q 2^A (2^(B+1)-1).           (7)
```

The estimate improves with the actual E,t of each run; a census should
not replace them by the average run length. Nor does (1) alone provide
an upper bound for H. The next construction shows that a uniform
polynomial conversion from L to H cannot be inferred from a bounded
rotation distance, even when `q<=L` and the total drift tends to zero.

## 3. A primitive distance-three family at vanishing drift

Let `(a,b)` range over integer pairs such that

```
delta_0=a log 2-b log 3>0,  delta_0 -> 0,
b -> infinity,             a/b -> alpha=log_2 3.
```

Eventually the integers

```
u=2b+2-a,   v=a-b-3
```

are positive. Define

```
U=1^u 2^v,
w=(3,U,4,U,5,U),
m=3b,       A=3a.                                (8)
```

The three markers 3,4,5 each occur exactly once. Hence w is primitive.
For every nonidentity rotation, all three marker positions are
mismatches: their values occur nowhere else. Rotation by b positions
has exactly those three mismatches. Therefore the minimum nonzero
rotation distance is exactly

```
rho(w)=3.                                        (9)
```

Since `2^A>3^m`, every such word gives a positive rational cycle for
additive parameter 1. Dividing its rotated intercepts by their common
gcd with D gives a primitive positive odd integer cycle at the reduced
parameter q. A smaller state period would force a smaller period of
the exact valuation word and is therefore impossible.

This is an actual-cycle construction. The coefficients below describe
its rational states `x_i=n_i/q`; they do not reinterpret a fractional
state as an integer Collatz state.

## 4. Exact affine calculation

Write `f_k(x)=(3x+1)/2^k` and put

```
r=3^b/2^a=exp(-delta_0),
tau=(3/4)^v,
lambda=(16/3)r,
beta=lambda+1-2tau.
```

The two constant runs have exact compositions

```
f_1^u(x)=(3/2)^u(x+1)-1,
f_2^v(y)=(3/4)^v(y-1)+1.
```

Thus the U block acts by `F_U(x)=lambda*x+beta`. If
`b_k=beta+lambda/2^k`, a marker k followed by U acts by

```
F_U(f_3(x))=2r*x+b_3,
F_U(f_4(x))=r*x+b_4,
F_U(f_5(x))=(r/2)*x+b_5.                          (10)
```

Let X0, X1, X2 be the rational states just before markers 3,4,5. Then

```
X1=2r X0+b_3,
X2=r X1+b_4,
X0=(r/2)X2+b_5,

X0=T/(1-r^3),
T=(r^2/2)b_3+(r/2)b_4+b_5.                       (11)
```

No approximation has been made in (10)-(11). For `r>=1/2` and
`u,v>=1`, lambda is greater than 1, and F_U takes its starting state
to a larger state. The bounds below give `X0>=9/4`, `X1>=X0` and
`X2>=X0/2>1`, so every marker step strictly reduces its input.
During U, the one-run increases the state; the
two-run then moves monotonically toward 1. It follows that the minimum
within each marker-plus-U block is its state immediately after the
marker. Therefore

```
L/q = min((3X0+1)/8, (3X1+1)/16, (3X2+1)/32).      (12)
```

As `delta_0->0` and `b->infinity`, one has

```
lambda -> 16/3,  beta -> 19/3,
(b_3,b_4,b_5) -> (7,20/3,13/2),
T -> 40/3,
X1/X0 -> 2,     X2/X0 -> 2.
```

The minimum in (12) is eventually its third entry. The maximum state
is eventually at the end of one of the one-runs, each of length u.
Consequently

```
delta_0*(L/q) -> 5/6,
(H/L)/(3/2)^u -> 2.                               (13)
```

In particular the normalized minimum tends to infinity, while

```
B/m -> ((2-log_2 3)*log_2(3/2))/3 > 0.             (14)
```

Thus `q<=L` eventually, yet the dyadic height grows linearly with the
period at the fixed rotation distance 3.

### Convenient exact finite bounds

For `r>=1/2`, `u,v>=1`, one has
`beta>=13/6`, `b_5>=9/4`, and `T>=9/4`. Also
`X1>=X0` and `X2>=X0/2`. Substitution into (12) yields

```
L/q > 27/[256(1-r^3)].                            (15)
```

Every one-run starts at a state at least L/q. Its endpoint gives

```
H/L > (3/2)^u.                                   (16)
```

For finite integer checking, with `P=3^b,Q=2^a`, these read

```
256 L (Q^3-P^3) > 27 q Q^3,
H*2^u > L*3^u.
```

Pairs `(a,b)=(27,17),(65,41),(485,306)` lie in the stated domain.
They are finite controls, not a numerical proof of the limiting claims.

## 5. Linear normalized minimum can coexist with exponential height

The pairs in (8) can be chosen so that

```
L/q=Theta(m),   rho(w)=3,   B=Theta(m).            (17)
```

Here is an elementary choice that avoids an additional logarithm-bound
input. Start with upper continued-fraction convergents `(a0,b0)` to
alpha. Their positive errors satisfy
`delta00=a0 log 2-b0 log 3 < (log 2)/b0`.
Set

```
k=ceil((b0*delta00)^(-1/2)),
a=k*a0,  b=k*b0,  delta_0=k*delta00.
```

Then `delta_0->0` and

```
1 <= b*delta_0 < (1+sqrt(log 2))^2 < 4.
```

Apply (13)-(14). The totals a,b need not remain coprime; the unique
markers, not a coprimality assumption, prove primitivity of w.

This family refutes uniform assertions such as
`B=O(s+log m)` or `B=O(s+log(L/q))` based only on actual overlap,
positive exact arrows, `q<=L`, and small positive drift. Equivalently,
no bound `H<=q*poly(m)` follows from those premises at bounded s.

It does not refute a height bound that also uses additional arithmetic
at a fixed q. In fact q tends to infinity in the balanced construction
just given. Apply (4) to the matching U run at rotation b:

```
q*((H-L)/q) >= 2*3^(b-1).
```

Using (13), `delta_0=Theta(1/b)` and
`u=(2-alpha)b+o(b)` shows

```
liminf (log q)/b >= log 3-(2-alpha)log(3/2)>0.
```

This last observation separates the obstruction from a bounded-q
counterexample. It is not presented as a new fixed-family exclusion
milestone.

## 6. Decision and scope

The actual overlap supplies the exact nonzero even differences (3) and
the zero sums (1). These are stronger data than free block variables.
The diameter estimate is uniform and can be checked on every actual
cycle. The missing step remains a useful consequence of the full
overlap that survives arbitrary height. Replacing H by L or by a
polynomial multiple of q would discard a real obstruction.

| Required field | Outcome |
| --- | --- |
| Objects | Differences between two phases of one primitive raw positive odd cycle, agreeing runs, and the cycle height. |
| Structural gain | Exact endpoint divisibility, a denominator inequality retaining height, and a distance-three actual family with linear normalized minimum and linear dyadic height. |
| Translated unresolved gap | A bound forcing rotation distance to grow at fixed q still needs arithmetic beyond this diameter/minimum conversion. |
| Worked example | The marker word (3,U,4,U,5,U) at (a,b)=(27,17), with its exact affine formula (11). |
| Known-cycle controls | The run law applies to the stored q5/q7/q13 cycles; repeated words and zero differences are excluded by the stated primitive/nonidentity domain. |
| Cheapest meaningful next test | Check (3), (7), (11), (15) and (16) exactly on stored cycles and the three declared upper-approximation controls. |
| Intermediate milestone | A height-independent relative denominator law or a growing minimum rotation-distance bound for every hypothetical q1 cycle; neither is achieved by this note alone. |

The result is an obstruction to a specific conversion, not a claim that
shared-word arithmetic cannot work. It improves no published cycle
exclusion record. Correctness, usefulness and novelty remain separate;
no novelty or formal-verification claim is made.
