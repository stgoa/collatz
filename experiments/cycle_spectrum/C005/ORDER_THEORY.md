# C005 — Dyadic order and rotation-block exclusion

**Status:** written elementary theorems and exact controls;
[independent proof review](INDEPENDENT_REVIEW.md) completed. The universal
exclusion of nontrivial integer Collatz cycles
is open. This note uses the raw positive odd-only map, without absorbing at
1. Every cycle mentioned is primitive unless stated otherwise. A rational
`S_1` cycle with common reduced denominator `q` is represented by its
positive odd numerator cycle under `S_q`.

## 1. Dyadic normalization retains a height label

Let `n_0,...,n_(m-1)` be distinct positive odd integers in a raw `3x+q`
cycle, with `q>=1` odd and coprime to 6, and exact valuations `a_i`:

```
3n_i+q = 2^a_i n_(i+1),       a_i>=1.
```

Rotate the cycle so `n_0=L=min_i n_i` and put `H=max_i n_i`. Define

```
h_i = floor(log_2(n_i/L)),
z_i = n_i/2^h_i in [L,2L),
F_i = (3n_i+q)/2^h_i = 3z_i+q/2^h_i,
c_i = a_i+h_(i+1)-h_i.                          (1)
```

Then `F_i=2^c_i z_(i+1)`, and `c_i>=1` because `F_i>3L` while
`z_(i+1)<2L`. The points `z_i` are distinct: equality would make two
odd numerators differ by a power of 2, forcing that power to be 1 and
the original states to coincide. The total normalized exponent equals
the original total, `sum_i c_i=sum_i a_i=A`; `c` and `a` differ by the
exact height coboundary `h_(i+1)-h_i`.

When `q<=L`, all normalized exponents are 1 or 2. Indeed
`3L<F_i<6L+q<=7L`, so
`3/2<F_i/z_(i+1)<7`. This does **not** imply that the chronological
`c` word is mechanical: the additive term `q/2^h_i` varies with the
height, and the sorted `F_i` can invert.

## 2. Exact inversion and a sufficient circle-order theorem

Sort the distinct normalized points `z_i`. Suppose `z_i<z_j`.
If `h_j<=h_i`, then `F_j>F_i`. If instead `h_j=h_i+k` for `k>=1`, put
`r=n_j-2^k n_i`; this is a positive **odd** integer, and direct
subtraction gives

```
F_j-F_i = [3r-q(2^k-1)]/2^h_j.                 (2)
```

Thus a strict inversion occurs **exactly** when
`3r<q(2^k-1)`. Equality cannot occur between two states of one
primitive cycle: a common `F` has a unique power-of-2 normalization
into `[L,2L)`, hence the same normalized successor; distinct odd
cycle states have distinct successors within that simple cycle.
Formula (2) is the arithmetic defect that a circle-order argument
must retain. Checking it for adjacent sorted `z` points suffices to
check strict monotonicity of the full sorted `F` list.

**Order lemma.** If the sorted `F_i` are strictly increasing with the
sorted `z_i`, then the normalized successor permutation is a circular
rank shift. Its chronological `c` word is mechanical with total `A`,
and `gcd(A,m)=1` when `m>1`.

**Proof.** The least normalized point is `z_0=L`, with height 0, so the
least `F` is `3L+q`. Every `F` is less than `6L+q<2(3L+q)`.
Consequently the unique powers of 2 moving the increasing `F` list
back into `[L,2L)` take two consecutive values, with the higher one
on a final block of `b` sorted ranks. The higher block's normalized
outputs precede the lower block's outputs; each block preserves order.
The successor rank is therefore `j+b mod m`. Primitivity gives
`gcd(b,m)=1` for `m>1`, and the same carry calculation as in
[C004](../C004/ROTATION_LATTICE.md) makes `c` mechanical. QED.

**Converse under `q<=L`.** For a primitive cycle with `m>1` and
`q<=L`, the normalized successor permutation is a circular rank shift
**if and only if** sorted `F` is strictly increasing.

For the reverse implication, suppose the shift is `+s mod m`, with
`1<=s<m`. In the first `m-s` sorted ranks the successor has larger
`z`. There `c=2` would give `F=4z_next>4z`, contradicting
`F=3z+q2^-h<=3z+L<=4z`; hence `c=1`. In the final `s` ranks the
successor has smaller `z`. There `c=1` would give
`F=2z_next<2z<3z<F`; hence `c=2`. Within each block, `F` increases
with the successor `z`. Across the boundary, every first-block value
is at most `2z_max<4L`, whereas every final-block value is at least
`4L`. Thus the entire sorted `F` list increases. The forward
implication is the order lemma. This equivalence explains the exact
order diagnostic; it still concerns only `c`, not the original `a` or
`gcd(C_w,D)`.

A mechanical `c` by itself can coexist with inversions and a
non-rotation successor permutation (Section 4). Keeping its letters
without the heights loses the order information.

### A three-band denominator restriction for d=1

For `q=1`, (2) cannot invert at a height gap `k=1`: `3r-1>=2`.
At `k=2`, `3r-3>=0`, and equality is excluded for a primitive cycle.
Therefore, if a nontrivial positive integer `3x+1` cycle satisfied

```
H<8L   (equivalently max_i h_i<=2),            (3)
```

the sorted `F` list would be strictly increasing. Its normalized word
`c` would be a primitive mechanical word of 1s and 2s, while
`a_i=c_i+h_i-h_(i+1)` would retain the original height changes.
This is a **necessary structure**, not an exclusion of the band `(3)`.
The first arithmetically possible inversion for `q=1` has `k=3,r=1`,
namely a pair `n_j=8n_i+1` in the indicated normalized order.
Existence of such a pair inside a nontrivial integer cycle is not
asserted.

**Denominator corollary.** Any primitive positive rational cycle with
`m>1`, `H<8L`, and `gcd(A,m)>1` has reduced denominator `q>1` (hence
`q>=5` in the coprime-to-6 domain). Equivalently, a hypothetical
nontrivial integer `3x+1` cycle whose total valuation and period have
a common factor must satisfy `H>8L`. The first statement follows by
contradiction from the `q=1` three-band order result and the order
lemma's `gcd(A,m)=1`; equality `H=8L` is impossible because the
original states are odd. This excludes a stated class of arbitrary
primitive words beyond C004's narrow `H<2L` class. It does not bound
the spread when `gcd(A,m)=1`.

More generally, with `B=max_i h_i`, the elementary condition
`q(2^B-1)<=3` ensures strict sorted `F` order, using the no-equality
argument. For supported odd `q` this is useful chiefly at `q=1,B<=2`.

### A complete exclusion for arbitrary concatenated rotation blocks

There is an all-size consequence for a language of words much broader
than one fixed repetition pattern. Let `v` be a primitive mechanical
word with coprime totals `(A_0,m_0)` and `D_0=2^A_0-3^m_0>0`.
Let its rational cycle states lie in `[l,h]`, and put `R=h/l<2` by
[C004](../C004/ROTATION_LATTICE.md). Form `w` by concatenating any
`r>=1` cyclic rotations of `v`, in any order and with repetitions.

**Rotation-block theorem.** Every positive rational cycle generated by
such a word has `H/L<=R^3<8`. Its reduced denominator exceeds 1,
except when the base word is `(2)`, in which case the whole word is a
repetition of the fixed point 1.

**Proof.** Every full block map has the same slope
`s=3^m_0/2^A_0` in `(0,1)`. If its rotation has fixed point
`X_t in [l,h]`, that block map is
`f_t(x)=s x+(1-s)X_t`. Each block preserves `[l,h]`; the unique
positive fixed point of their composition, and all successive block
boundary points, therefore lie in `[l,h]`. The composition slope is
`s^r<1`, so its fixed point is positive; the general word identity
from C004 gives exact valuations at every letter.

For any prefix of a block, write its affine map as `g_t(x)=alpha*x+beta`
with `alpha>0,beta>=0`. The base prefix state `g_t(X_t)` lies in
`[l,h]`. At a mixed-cycle block boundary, `x/X_t` lies in
`[1/R,R]`, and positivity gives

```
min(1,x/X_t) <= g_t(x)/g_t(X_t) <= max(1,x/X_t).
```

Thus **every** mixed-cycle state lies in `[l/R,Rh]`; its largest to
smallest ratio is at most `(Rh)/(l/R)=R^3<8`.

The displayed word has totals `(rA_0,rm_0)`, whose gcd is `r`.
Suppose it is `p` repetitions of its primitive cycle word. Then
`p|r` and the primitive word's total/length gcd is `r/p`.
If the mixed cycle had denominator 1, the three-band denominator
corollary above, applied to its primitive cycle with ratio below 8,
would force `r/p=1` when that primitive period exceeds 1. At period
1 its total/length gcd is already 1, giving the same conclusion.
Hence `p=r`. The primitive word has length
`m_0`, so every aligned rotation block of `w` is identical. Its
cycle is then the base mechanical cycle, whose denominator is exactly
`D_0` by R71. That is 1 only for the base word `(2)`. QED.

For a small exact example, take base `v=(1,2,2)`, whose rational
states are `(23,37,29)/5` and `R=37/23`. Concatenating `v` with
its rotation `(2,2,1)` gives
`w=(1,2,2,2,2,1)`, `C_w=1805`, `D_w=295`, `gcd=5`, and reduced
denominator 59. Its primitive raw `3x+59` cycle has minimum 221 and
maximum 571; its chronological numerators are
`(361,571,443,347,275,221)`, so `H/L=571/221<8`. This theorem allows arbitrary
block orders and counts but does not address words whose blocks are
not all rotations of one mechanical base.

For an infinite nonmechanical control family, take every prime
`m_0>=13` and `A_0=bit_length(3^m_0)`. Then
`m_0<A_0<2m_0`, so `gcd(A_0,m_0)=1`; the base word has only 1s and
2s, and [R71](../../residual_progress/lattice_cycles/BALANCED_DENOMINATORS.md)
gives its rational minimum `l>m_0/6`. Let `v_0` be the lower mechanical
word and `v_1` its **one-letter left cyclic shift**; they are distinct
because the base word is primitive. Concatenate the six blocks in the
block-label pattern `(0,0,1,0,1,1)`. This pattern has no proper cyclic
period dividing 6. Let `T` be the least cyclic period of the full
valuation word. It divides `6m_0` and must be a multiple of `m_0`,
because its average valuation is the reduced fraction `A_0/m_0`;
aligned block periodicity then forces `T=6m_0`.
The word is therefore primitive with total/length gcd 6, so it is
not mechanical. The rotation-block theorem gives reduced denominator
greater than 1 and every rational state above
`l/R>m_0/12>1`. In the associated raw integer `3x+q` shortcut
clock, its parity word has `6(A_0-m_0)` local minima: each
valuation-2 letter contributes one even descent before the next odd
state, and all normalized rational states exceed 1.
This count is in the **shortcut** clock; it is not an odd-only local
minimum count. The minima grow without bound as `m_0` grows. No
fixed-denominator high-cycle or published record claim follows.

## 3. Why a mechanical normalized word does not control the denominator

Let `P_j=sum_(i<j)c_i`, `P_0=0`, and start at `n_0=L`, so `h_0=0`.
Iterating `2^c_i z_(i+1)=3z_i+q2^-h_i` around the cycle gives the
exact weighted fixed-point equation

```
(2^A-3^m)L
  = q sum_(j=0)^(m-1) 3^(m-1-j) 2^(P_j-h_j).   (4)
```

Because `P_j=A_j+h_j`, where `A_j=sum_(i<j)a_i`, the sum in (4) is
exactly the original word intercept `C_w`. Thus normalization is an
invertible change of coordinates **only when the height labels are
retained**. Discarding `h` replaces the weighted sum by the unweighted
mechanical intercept for `c`, which can have a different gcd with
`D=2^A-3^m`. The R71 denominator-1 obstruction for a mechanical
*original* word cannot be transferred to a merely mechanical `c`.

An exact two-band counterexample to that transfer is the raw `d=q=233`
cycle

```
n=(1535,2419,3745,2867,4417,3371,5173,1969),
a=(1,1,2,1,2,1,3,2),
h=(0,0,1,0,1,1,1,0),
c=(1,2,1,2,2,1,2,2).
```

Here `L=1535`, `H=5173<4L`, and `q<=L`. The sorted `z` positions are
`(0,5,2,7,4,1,6,3)` and their exact `F` values are
`(4838,5173,5734,6140,6742,7490,7876,8834)`, strictly increasing.
The successor rank shift is `+5 mod 8`; `c` is the lower mechanical
word with `(A,m)=(13,8)`. Yet the original intercept is `C_w=10745`,
`D=2^13-3^8=1631=7*233`, so `gcd(C_w,D)=7` and the reduced denominator
is `233`, not `D`. The original word has a 3 and is nonmechanical.
This refutes even a two-band, strictly order-preserving, `q<=L`
version of the proposed denominator inference.

The stored raw `d=q=5` 17-cycle gives a larger cancellation example:

```
n=(187,283,427,643,967,1453,1091,1639,2461,1847,2773,
   2081,781,587,883,1327,1993),
a=(1,1,1,1,1,2,1,1,2,1,2,3,2,1,1,1,5),
h=(0,0,1,1,2,2,2,3,3,3,3,3,2,1,2,2,3),
c=(1,2,1,2,1,2,2,1,2,1,2,2,1,2,1,2,2).
```

Its sorted `F` values are, exactly,

```
(566,587,2461/4,643,1327/2,2773/4,1453/2,748,781,
 1639/2,854,883,1847/2,967,1993/2,2081/2,1091),
```

strictly increasing; the successor rank shift is `+10 mod 17`. The
normalized `c` is mechanical with total 27,
but `C_w=189900931`, `D=5077565`, `gcd(C_w,D)=1015513`, and reduced
denominator 5. This is one exact finite control; it does not prove an
unbounded cancellation theorem for primitive cycles.

## 4. Order failure with `q<=L`, and known-cycle controls

Even the order lemma's premise is not universal when `q<=L`. The raw
`d=q=11` primitive cycle

```
n=(13,25,43,35,29,49,79,31),
a=(1,1,2,2,1,1,3,3),
h=(0,0,1,1,1,1,2,1),
c=(1,2,2,2,1,2,2,2)
```

has `L=13>=q`. In sorted normalized order, `z=13<29/2` but
`F(13)=50>49=F(29/2)`. Formula (2) gives `k=1,r=3`, and
`3r-q(2^k-1)=9-11=-2`, divided by `2^1` yields `-1`.
Its full successor-rank list is `(7,6,0,1,2,3,4,5)`, not a circular
shift. Here `c` itself is the repeated mechanical word of total 14 and
length 8; that alone does not imply order preservation because the
height-dependent offsets remain in the map. Since `gcd(14,8)=2` and
`79<8*13`, this is also a nonintegral control for the denominator
corollary above.

The shorter raw `d=5` cycle `(19,31,49)` has `L=19>=q=5`, strictly
increasing sorted `F=(62,76,98)`, circular rank shift `+2`, and
mechanical `c=(1,2,2)`, but original `a=(1,1,3)` is nonmechanical.
It is the simplest control for the coboundary gap. The raw `d=7`
cycle `(5,11)` already has a sorted `F` inversion, with `q>L`;
the raw `d=13` fixed point at 1 has one state and no order question.
For ordinary `d=1`, the known fixed point 1 has `h=0,c=a=2`.
Cycles involving raw state 1 at generalized `d` are not presented as
nonconvergence witnesses under the absorbing convention.

The exact examples above were recomputed from their arrows. The
separate [C005 checker](check_order.py) and [receipt](order_audit.json)
provide a bounded catalogue replay; no finite catalogue can verify
the universal conditional statements in Sections 1–3.

## 5. Seven-field assessment

| Field | Outcome |
| --- | --- |
| Objects | Primitive positive rational odd-only cycles, their common reduced denominator, dyadic heights, normalized states and sorted successor order. |
| Structural gain | Exact inversion formula (2), order/rank equivalence for `q<=L`, a denominator-1 exclusion for common-factor `(A,m)` words below `8L`, and complete exclusion for arbitrary concatenations of rotations of one primitive mechanical block. |
| Translated unresolved gap | The original valuations differ by a height coboundary, and equation (4) retains those heights in the denominator arithmetic. The band and rotation-block theorems do not cover every word or exclude every possible `q=1` cycle. |
| Worked example | The `q=233` two-band cycle has strict order and mechanical `c` but cancellation `g=7`; the `q=11` cycle has a genuine inversion; `(122)(221)` has reduced denominator 59. |
| Known-cycle controls | Raw `d=1` fixed point and `d=5,7,13` cycles are checked with the absorber convention stated. |
| Cheapest meaningful next test | Find a condition involving the height labels and weighted sum in (4) that excludes `q=1` while surviving the `q=5,11,233` controls; test it at each dyadic boundary. |
| Genuinely intermediate milestone | The rotation-block theorem excludes denominator 1 for all orders and counts of rotations of one primitive mechanical base, including primitive nonmechanical families with growing minima. |
