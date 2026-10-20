# C006 — Arithmetic retained by ordered dyadic normalization

**Status:** written elementary gap theorem, an effective corollary using a
primary two-logarithm bound, and exact countercontrols;
[independent mathematical review](INDEPENDENT_REVIEW.md) completed, including
the height-free corollary. The
target of excluding reduced denominator 1 from every
nontrivial ordered cycle is **open**. This note uses the raw positive odd-only
map, without absorbing at 1. A rational `S_1` cycle with reduced denominator
`q` is represented by its primitive positive odd numerator cycle for `S_q`;
`q` is odd and coprime to 6. All cycles below are primitive unless a
qualification says otherwise.

## 1. Exact ordered-circle interface

Let `n_0,...,n_(m−1)` be a cycle, rotated so `n_0=L=min n_i`, and let
`H=max n_i`. Write

```
3n_i+q=2^a_i n_(i+1),       a_i>=1,
h_i=floor(log_2(n_i/L)),    z_i=n_i/2^h_i in [L,2L),
eps_i=q/2^h_i,              F_i=3z_i+eps_i,
c_i=a_i+h_(i+1)−h_i,        2^c_i z_(i+1)=F_i.
```

Put `A=sum a_i=sum c_i` and `D=2^A−3^m>0`. The [C005 order
lemma](../rotation-block-exclusion/ORDER_THEORY.md) proves that strictly increasing `F` in
sorted `z` order makes the successor permutation a circular rank shift.
When `q<=L`, the converse also holds. In that case, if the rank shift is
`+s mod m`, `1<=s<m`, then `c=1` on the nonwrapping sorted ranks and
`c=2` on the wrapping ranks. Starting at rank zero, `z_0=L`, gives

```
c_i=floor((i+1)A/m)−floor(iA/m),    A=m+s,
gcd(A,m)=gcd(s,m)=1.                              (1)
```

Thus the **normalized** word is the canonical lower mechanical word. The
original valuations retain the height coboundary
`a_i=c_i+h_i−h_(i+1)`; replacing `a` by `c` loses the denominator test.

## 2. Positive Green comparison and the missing congruence

Let `P_j=sum_(i<j)c_i`, `P_0=0`, and set

```
M_j=3^(m−1−j) 2^P_j,
C_c=sum_j M_j,
E_h=sum_j M_j(1−2^(−h_j)),
C_h=C_c−E_h=sum_j M_j/2^h_j.
```

The exact weighted cycle identity, starting at `h_0=0`, is

```
D L=q C_h=q(C_c−E_h).                          (2)
```

Each `M_j/2^h_j` is an integer because `P_j=A_j+h_j`. It is exactly
the corresponding monomial of the original valuation-word intercept.
In particular the reduced denominator is
`q=D/gcd(C_h,D)`. Equation (2) is an identity for actual cycles; it
does not license an arbitrary choice of height profile.

Let `Y_i` be the unique positive periodic solution of
`2^c_i Y_(i+1)=3Y_i+1`. Subtracting the normalized recurrence gives

```
2^c_i (qY_(i+1)−z_(i+1))
  =3(qY_i−z_i)+q(1−2^(−h_i)).                    (3)
```

The product of the homogeneous multipliers around the cycle is
`3^m/2^A<1`. Solving the periodic affine equation therefore gives

```
q 2^(−B)Y_i <= z_i <= qY_i,     B=max h_i,       (4)
```

at every phase. The right inequality is strict at every phase if any
height is positive; similarly the left one is strict if any height is
less than `B`. This is a positive Green comparison, not an integrality
argument. For ordered cycles, `Y_0=C_c/D` is the lower mechanical
minimum, so `L<qC_c/D` for a wide cycle. Yet the required denominator-1
step is the exact congruence

```
D | C_h = C_c−E_h.                              (5)
```

The mechanical denominator theorem gives `gcd(C_c,D)=1` when
`gcd(A,m)=1`. It supplies no bound on `gcd(C_c−E_h,D)`. Even one legal
height excursion can create nontrivial cancellation (Section 4).

## 3. What order says about heights and gaps

Sort the normalized states as `z_[0]<...<z_[m−1]`, with corresponding
height labels `H_j` and `eps_j=q2^(−H_j)`. Suppose their successor ranks
shift by `+s mod m`, with `q<=L`. From (1) and `a>=1` we get

```
H_((j+s) mod m)−H_j <= 1_{j>=m−s}.            (6)
```

Every nonwrapping rank edge therefore has nonincreasing height. If the
sorted height list were itself nondecreasing, then (6) would force all
heights to be zero: `H_0=0`, the edge `0→s` forces `H_s=0`, and
monotonicity plus the remaining nonwrapping edges propagates zero through
all ranks. Thus **every wide ordered cycle has a descent in its sorted
height list**. This is a necessary structural condition, not a
denominator exclusion; the controls in Section 4 have such descents.

The chronological relation supplies a second useful count. Since
`a_i=c_i+h_i−h_(i+1)>=1` and `c_i<=2`, every upward chronological
height step is at most one: `h_(i+1)−h_i<=1`. Starting at `h_0=0`
and reaching the maximum `B` therefore visits each integer height
`0,1,...,B`. The sorted height list contains all these `B+1`
distinct labels and so has at least `B` adjacent changes. Let `J`
denote one plus that change count, including the dyadic seam as in
the next subsection. Then

```
J >= B+1.                                         (H1)
```

This uses exact positive valuations and does not require any bound on
the maximum height in advance.

There is also an exact adjacent-gap system. Extend the sorted sequence
formally by `z_[j+m]=2z_[j]` and `eps_[j+m]=2eps_[j]`, and put
`Delta_j=z_[j+1]−z_[j]`. The ordered recurrence becomes

```
2 z_[j+s]=3z_[j]+eps_[j],
2 Delta_(j+s)=3Delta_j+eps_[j+1]−eps_[j].       (7)
```

The extension retains the seam term `eps_[m]=2eps_[0]`; dropping it
changes the equations. Positivity of every `Delta_j` verifies
consistency of a proposed sorted rank order. Equation (7) is a re-expression of the weighted
recurrence, so a denominator conclusion needs an additional arithmetic
restriction on its dyadic lattice solution.

### A sparse-forcing denominator law

The gap system does yield one quantitative restriction that **uses**
circle order. Put `B=max_j H_j`, and for `0<=j<m` define

```
G_j=2^B Delta_j in Z_(>0),
T_j=2^B(eps_[j+1]−eps_[j]) in Z,
J=#{j:T_j != 0}.
```

Here `eps_[m]=2eps_[0]=2q`, so the seam is always forced and `J>=1`.
For internal `j`, `T_j!=0` exactly when adjacent sorted heights differ;
therefore `J` is one plus the number of sorted-height transitions.

**Sparse-forcing theorem.** Let `m>1` and assume the ordered rank shift
above, with `q<=L`. Set
`delta=A log 2−m log 3>0`. Then

```
L > 2^(ceil(m/J)−1−B),
q > (D/C_c) 2^(ceil(m/J)−1−B),
q > (3 delta/m) 2^(ceil(m/J)−1−B).           (G1)
```

There are effective absolute constants `c_0>0,K_0>0` for which
[Bugeaud's two-logarithm bound, Theorem 1.1(1.2)](https://arxiv.org/pdf/2209.00275)
gives `delta>=c_0 m^(−K_0)` in this setting. This is an imported
linear-forms result, ultimately based on Waldschmidt and Matveev;
no numerical constant is claimed here. Consequently

```
q > (3c_0/m^(K_0+1)) 2^(ceil(m/J)−1−B),
m/J < B+1+log_2(q/(3c_0))+(K_0+1)log_2 m. (G2)
```

For each fixed `q,B,J`, only finitely many periods are possible,
effectively in principle. More generally, bounds `q<=Q`, `B<=B_0`,
`J<=J_0` leave only finitely many possible cycles: (G2) bounds `m`,
then `A<2m` leaves finitely many positive valuation words, each with
one rational cycle. For fixed `q,B`, every such ordered cycle has
`J=Omega(m/log m)`. The constants inherited from general
linear-forms theory are enormous; (G2) is a qualitative complexity
law, not a usable finite Collatz-cycle cutoff or denominator-1
exclusion.

**Height-free corollary.** The height bound is redundant when `J` is
bounded. Substituting (H1) into (G1)–(G2) gives

```
q > (D/C_c) 2^(ceil(m/J)−J),
q > (3 delta/m) 2^(ceil(m/J)−J),
m/J < J+log_2(q/(3c_0))+(K_0+1)log_2 m.       (G5)
```

Hence fixed upper bounds on `q,J` alone leave effectively finitely
many ordered cycles in the declared `q<=L`, `m>1` domain. For fixed
`q`, (G5) gives `m<J^2+O_q(J log m)`, and therefore
`J>=sqrt(m)−O_q(log m)`, in particular `J=Omega(sqrt(m))`. This is a
necessary asymptotic complexity law, not an exclusion of any finite
denominator-one cycle.

**Proof of the elementary part.** In modular sorted-rank notation,
subtracting adjacent equations in (7) gives

```
2^(1+1_{j>=m−s}) G_((j+s) mod m)=3G_j+T_j.   (G3)
```

The `+s` map visits all `m` ranks because the cycle is primitive.
Its `J` forced positions divide the remaining `m−J` positions into
`J` zero-forcing runs. One has length
`t>=ceil(m/J)−1`. Along that run, multiplying (G3) yields
`2^e_run G_end=3^t G_start`, where `e_run` is the sum of its rank
exponents and `e_run>=t`.
Since `G_start` is a positive integer and 2 and 3 are coprime,
`G_start>=2^e_run>=2^t`. The extended gaps are positive and sum
to `L`, so each is strictly less than `L` for `m>1`; hence
`G_start<2^B L`. In fact, for **each** zero-forcing run we have
`L>2^(e_run−B)` and, by the comparison `L<=qC_c/D` from (4),
`q>(D/C_c)2^(e_run−B)`. These imply the first two inequalities in
(G1).

Multiplying the original odd-cycle arrows gives the exact identity

```
delta=sum_i log(1+q/(3n_i)) <= mq/(3L).      (G4)
```

Combine it with the first inequality to obtain the third. Finally,
apply the cited theorem with algebraic numbers `2,3`, coefficients
`(A,−m)`, and number-field degree 1. The form is nonzero because
2 and 3 are multiplicatively independent. By (1), `A=m+s<2m`,
so its coefficient bound is below `2m`; the fixed-number heights
give `delta>=c_0 m^(−K_0)` with effective absolute constants.
Substitution and logarithms give (G2). No linear-forms
theorem is needed for (G1). QED.

One proposed shortcut was that some pair of normalized states must
have a primitive odd gap at most `q`. It already fails for the ordered
raw `q=13` cycle with numerators
`(227,347,527,797,601)` and valuations `(1,1,1,2,3)`.
Here `h=(0,0,1,1,1)`, the sorted normalized states are
`(227,527/2,601/2,347,797/2)`, and the sorted `F` values
`(694,797,908,1054,1202)` increase. Among **all** pairwise
differences of those normalized states, the least odd numerator after
removing all powers of two is `15`, attained by `347−227=120=8*15`;
thus it exceeds `q=13`. This control refutes that specific universal
small-gap claim, not other possible gap estimates.

## 4. Exact controls on the arithmetic bridge

### A single legal height defect already changes the gcd

The raw `q=233` cycle

```
n=(1907,2977,2291,3553,2723,4201,3209,2465),
a=(1,2,1,2,1,2,2,2),
h=(0,0,0,0,0,1,0,0),
c=(1,2,1,2,2,1,2,2)
```

has `L=1907`, `H=4201<4L`, `q<=L`, and strictly increasing sorted
`F=(5954,6418,7106,7628,8402,9164,9860,10892)`. Its rank shift
is `+5 mod 8`, so `c` is the canonical lower mechanical word with
`(A,m)=(13,8)`. Directly,

```
C_c=14501,  M_5=2304,  E_h=M_5/2=1152,
C_h=13349,  D=2^13−3^8=1631=7*233,
gcd(C_h,D)=7, reduced denominator q=233.
```

Thus “one defect preserves the mechanical unit gcd” is false. In the
general one-defect pattern `h_t=1` and all other heights zero,
`a_(t−1)>=1` requires `c_(t−1)=2`, and the exact open denominator-1
subproblem is whether a **legal and actual** profile can satisfy
`D | C_c−M_t/2`. A finite scan is not a proof of its failure.

The earlier ordered two-band `q=233` control in C005 has the same
mechanical `c`, but `E_h=3756>D=1631` and `gcd(C_h,D)=7`.
The ordered `q=5` period-17 control has
`C_c=548440271`, `C_h=189900931`, `E_h=358539340`,
`D=5077565`, `gcd(C_h,D)=1015513`. Consequently neither `E_h<D`
nor a single crossing of the `D` lattice holds uniformly.

### Correct heights and a primitive mechanical word do not imply order

The raw `q=1909` cycle

```
n=(3991,6941,5683,9479,15173,11857,4685),
a=(1,2,1,1,2,3,2),
h=(0,0,0,1,1,1,0),
c=(1,2,2,1,2,2,2)
```

has `A=12,m=7,gcd(A,m)=1`, and `c` is the canonical lower mechanical
word. Its heights are the **actual** heights and `L=3991>q=1909`.
Nevertheless sorted `z` indices are `(0,6,3,2,5,1,4)` and sorted
`F` values are `(13882,15964,15173,18958,18740,22732,23714)`.
There are inversions at `(6,3)` and `(2,5)`, so the successor ranks
`(5,0,6,2,1,3,4)` do not form a rotation. A proof starting only from
mechanical `c` and correct dyadic heights must still verify all
adjacent-rank inequalities.

### Exact legality cannot be relaxed to integer circle coordinates

The formal `q=1` cycle `4→13→5→4` has exponents `(0,3,2)`, heights
`(0,1,0)`, normalized word `(1,2,2)`, and strictly ordered
`F=(13,16,20)` at sorted `z=(4,5,13/2)`. It satisfies the weighted
circle equations and integer state coordinates; indeed
`C_c=23`, `D=5`, `E_h=3`, so `D | C_c−E_h=20`.
It is **not** a Collatz odd-only cycle: the state 4 is even and its
first valuation is zero. Hence any proposed argument that allows
zero valuations or forgets oddness can produce a false denominator-1
counterexample.

The raw `q=11` cycle from C005, with numerators
`(13,25,43,35,29,49,79,31)`, remains the separate inversion
control: sorted `z=13<29/2` has `F=50>49`. It shows that `q<=L`
alone does not imply order.

## 5. Generic extremal and packing baselines

The upper comparison `L<=qC_c/D` must not be credited to circle order.
There is a generic elementary cycle lemma. For an arbitrary positive
valuation word `a` with totals `(A,m)`, put
`b_j=A_j−jA/m` and extend `b` periodically. Rotate the word to an
index where `b_j` is maximal. Every rotated prefix then obeys
`A'_j−jA/m<=0`, hence `A'_j<=floor(jA/m)`. Termwise comparison of
the intercepts gives

```
min_i n_i <= q C_lower(A,m)/(2^A−3^m),         (8)
```

strictly if the original word is not a rotation of the lower
mechanical word. This generic bound is consistent with the published
mechanical extremal direction; it is not a new consequence of C006
order.

There is an elementary lattice packing consequence, also valid without
order. Let `r_h` count states of dyadic height `h`, and `B=max h_i`.
Because all numerators and `L` are odd, the available normalized
positions in `[L,2L)` number at most `(L+1)/2` at height zero and
`2^(h−1)L` at height `h>=1`. Thus, with

```
P=max(2r_0−1, max_(1<=h<=B) ceil(r_h/2^(h−1))),
P_odd=least positive odd integer >=P,
```

we have `L>=P_odd`. Combining this with (8) yields the exact necessary
denominator restriction

```
q >= ceil(P_odd D/C_lower(A,m)).                 (9)
```

Summing the capacities instead gives

```
m <= ((2^(B+1)−1)L+1)/2,
q >= ceil((2m−1)D/((2^(B+1)−1)C_lower(A,m))).  (10)
```

These all-size inequalities can exclude denominator 1 for specified
`(A,m,B)` or height histograms. Their arithmetic content is the odd
lattice and the generic extremal bound, not the successor rank order.
They are weak near the critical `2^A/3^m≈1` regime and do not exclude
all ordered integer cycles.

A separate generic baseline is the product identity

```
2^A/3^m = product_i (1+q/(3n_i))
        <= product_(j=0)^(m−1) (1+q/(3(L+2j))),   (11)
```

because the `n_i` are distinct odd integers. This bound can dominate
the packing restriction, and likewise uses no normalized order. Any
claim of a new order-based denominator gain must be compared with
(8)–(11), not only with R71's mechanical-word gcd theorem.

## 6. Decision and next test

The circular-order mechanism gives the order-specific sparse-forcing
law (G1): a bounded number of sorted-height changes forces an
exponentially large cycle minimum, and the primary two-logarithm
lower bound then makes periods finite for fixed `q,J`; the height
bound follows from (H1). At fixed `q`, the number of sorted-height
changes must grow at least on the order of the square root of the
period. This is a genuine restriction on all ordered cycles in the
declared domain. It does **not** give a
practical cutoff, and it does not exclude even one possible
nontrivial denominator-1 cycle at a finite period. T. Brox's
[published few-descents work](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/en/publishing-house/journals-and-series/acta-arithmetica/all/92/2/111840/collatz-cycles-with-few-descents)
concerns descending steps in the chronological odd-only orbit; `J`
counts changes of dyadic height in **sorted normalized rank**. The
two counts are different, and no novelty relative to all published
cycle bounds is asserted.

The remaining universal denominator-1 bridge is an inequality or
congruence that rules out `D | C_h` for every nontrivial **legal odd**
ordered profile, or a way to make the growing `J` bound incompatible
with such profiles. The positive weighted defect can cancel factors
of `D` on actual ordered cycles. Adjacent-rank inequalities and the
actual height coboundary must remain in any next attempt. Excluding
one-height defects for all periods would be a further intermediate
result; the single-defect congruence in Section 4 is only a candidate.

| Field | C006 assessment |
| --- | --- |
| Objects | Primitive positive odd numerator cycles, dyadic heights, sorted normalized gaps, and reduced denominator `q`. |
| Structural gain | Exact positive Green comparison, sorted-height descent and `J>=B+1`; the seam-correct gap system yields (G1), and imported linear forms give effective finiteness at fixed `q,J` and `J=Omega(sqrt(m))` at fixed `q`. |
| Translated unresolved gap | Prove `D` cannot divide the legal weighted intercept `C_h` at `q=1`; mechanical `C_c` alone is insufficient. |
| Worked example | The ordered one-height `q=233` cycle has `E_h=1152` and cancellation by 7. |
| Known-cycle controls | `q=5` and `q=233` ordered cancellation; `q=11` and `q=1909` inversions; `q=13` has no primitive odd pair gap at most `q`. |
| Cheapest meaningful next test | Strengthen the gap law with exact height-jump locations or a legal-height congruence in the one-defect case, retaining all adjacent inequalities and the `q=1` zero-valuation relaxation. |
| Genuinely intermediate milestone | The proved fixed-`q,J` finiteness and square-root change-count law restrict all periods in the ordered class. An all-period denominator-1 exclusion for one-defect ordered cycles remains a further, unproved milestone. |
