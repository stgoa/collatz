# C009 — Exact excursion cuts and their arithmetic limit

**Status: written elimination barrier and an exact return-order counterexample.**
No nontrivial denominator-one cycle is excluded. This note uses the raw
positive odd-only `3x+q` map, with no absorber at 1. A *cycle* below is
primitive unless a statement explicitly covers an arbitrary word. The
application domain is reduced odd denominator `q`, `q<=L=min n_i`, and
strict circular normalized successor order. The cut identities themselves
hold without order.

For a positive valuation word `w=(a_0,...,a_(m−1))`, put
`A_j=sum_(i<j) a_i`, `A=A_m`, and

```text
C_j = sum_(i=0)^(j−1) 3^(j−1−i) 2^A_i,
D = 2^A−3^m > 0.
```

The full intercept is `C=C_m`. Its rotation at phase `i` is `C_(i)`,
and `2^a_i C_(i+1)=3C_(i)+D`. All `C_(i)` and `D` are odd. As in
[C004](../C004/ROTATION_LATTICE.md), their rational cycle is
`C_(i)/D`, with reduced denominator `q_0=D/g`, where
`g=gcd(C,D)=gcd(C_(i),D)`.

## 1. A cut preserves every exact valuation cylinder

**Lemma (written proof).** Let a positive-valuation segment `E` have
length `ell`, total `a`, and exact intercept `C_E`. Let `q`, `x` and `y`
be positive odd integers satisfying

```text
2^a y = 3^ell x + q C_E.                         (1)
```

Then every intermediate state of `E` is a positive odd integer, and
every prescribed valuation is exact. Thus an exact affine endpoint
relation does not lose the internal odd-only cylinders.

For a cut after `j` arrows, let `P_j` and `C_j` be the prefix valuation
sum and intercept. Composition gives

```text
C_E = 3^(ell−j) C_j + 2^P_j C_tail.
```

Reduce (1) modulo `2^P_j`. Since 3 is invertible modulo that power,
`2^P_j` divides `3^j x+q C_j`. Hence
`u_j=(3^j x+q C_j)/2^P_j` is an integer. It is positive, and
`2^a_j u_(j+1)=3u_j+q`. If `u_j` were even for any `j<ell`, the
right side would be odd, impossible because `a_j>=1`. The endpoints
are odd by hypothesis, so every `u_j` is odd. Therefore the displayed
arrow has valuation exactly `a_j`. This argument retains the complete
intercept; replacing it by a mechanical or approximate intercept would
invalidate the conclusion. QED.

## 2. Closing an excursion gives the original single obstruction

Suppose `E` is a first return from a height-zero state `x` to another
height-zero state `y`, with every internal state at positive dyadic
height relative to the cycle minimum `L`. Let `P` be the complete
complementary path from `y` back to `x`; it may contain other excursions.
Write the respective lengths, valuation totals and exact intercepts as
`(ell,a,C_E)` and `(r,b,C_P)`. Their full endpoint equations are

```text
2^a y = 3^ell x + q C_E,
2^b x = 3^r y + q C_P.                        (2)
```

Eliminating `y` gives, without approximation,

```text
D x = q C,
D = 2^(a+b)−3^(ell+r),
C = 3^r C_E + 2^a C_P.                         (3)
```

The last `C` is precisely the intercept of the full word `EP` based
at `x`. At `q=1`, **an integer solution of (2) exists exactly when
`D|C`**. Indeed, necessity is (3). Conversely, if `D|C`, then
`x=C/D` is a positive odd integer. The rotation recurrence
`2^a_i C_(i+1)=3C_(i)+D`, together with `gcd(D,2)=1`, propagates
`D|C_(i)` to every phase. Every quotient `C_(i)/D` is odd, and the
lemma recovers every exact valuation cylinder. In particular the
complementary endpoint `y` is automatically integral and odd.

The same conclusion holds for any number of height-zero first-return
blocks. Compress each block using its **true** intercept, then compose
the blocks. If there are `k` blocks, the cyclic coefficient matrix has
one row `−3^ell_j x_j+2^a_j x_(j+1)=q C_j` per block. Its determinant
has absolute value `D`. Its Smith form is `diag(1,...,1,D)`: at a prime
dividing `D`, which is neither 2 nor 3, deleting the closing row and
column leaves a triangular `(k−1)`-minor that is a product of powers of
3 and hence a unit. At every other prime the determinant is a unit.
The maximal minors of the augmented matrix are `D` and, up to sign,
the Cramer numerators `q C_(i)` at block starts. Their gcd is
`gcd(D,qg)`. This is the block-level form of C004's one-obstruction
Smith calculation, not a second cancellation restriction.

There is an exact limit to this barrier. For a fixed word, first use the
rational parameter-one states `r_i=C_(i)/D`. Scaling **both** the states
and the additive parameter by the same positive `q` gives
`n_i=q r_i`. The minimum, normalized coordinates and scaled images all
scale by `q`, so dyadic heights, excursion membership and strict
sorted-rank inequalities are unchanged. Thus the cut
algebra and the legal shape together describe *the original word test*:
legal ordered shape plus `D|C` at `q=1`. The algebra supplies no new
independent congruence. A future proof could still show that the
**joint** shape and divisibility conditions are incompatible; this
note does not rule out such an argument.

## 3. Exact controls: the cut closes, but order need not descend

The ordered raw `q=5` cycle `(19,31,49)` has heights `(0,0,1)`.
Take the excursion `31 -> 49 -> 19`, with word `(1,3)`, and the
complement `19 -> 31`, with word `(1)`. Equations (2) are

```text
16*19 = 9*31 + 5*5,
 2*31 = 3*19 + 5.
```

Elimination gives `D=2^5−3^3=5` and `C=3*5+16*1=31`, so
`D*31=q*C`. At `q=1` the same legal rational shape has state `31/5`;
the failure is exactly `D∤C`, not an extra excursion congruence.

The height-zero first-return map does **not** generally inherit the
circular order of the full normalized cycle. An exact ordered `q=13`
control is

```text
n=(283,431,653,493,373),
a=(1,1,2,2,2),
h=(0,0,1,0,0),   L=283.
```

Its normalized states in increasing order are
`283, 653/2, 373, 431, 493`; the corresponding scaled images
`3z+13/2^h` are `862, 986, 1132, 1306, 1492`, strictly
increasing. The ordered height-zero states are
`(283,373,431,493)`. Their first-return ranks are
`[2,0,3,1]`, not a constant cyclic shift. The sole positive-height
excursion `431 -> 653 -> 493`, word `(1,2)`, and its complement,
word `(2,2,1)`, satisfy

```text
 8*493 =  9*431 + 13*5,
32*431 = 27*493 + 13*37.
```

Here `D=2^8−3^5=13` and `C=27*5+8*37=431`.
Thus applying C005's circular-order theorem recursively to the
height-zero return map would be invalid even on an actual ordered
cycle. The sibling [one-point deletion theorem](FIRST_RETURN_ORDER.md)
shows this is systematic when a single positive-height rank is removed:
an interior normalized shift loses circular return order. The raw
`d=7` cycle `(5,11)` has `L=5<q=7` and remains
outside the ordered domain; no claim here excludes it.

## 4. Decision in seven fields

| Field | C009 assessment |
| --- | --- |
| Objects | Exact positive-height excursions between height-zero states of primitive positive odd cycles, their complementary paths, and all original sorted-rank inequalities. |
| Structural gain | Exact endpoint compression preserves every intermediate odd valuation cylinder. Closing any number of compressed blocks has Smith form `diag(1,...,1,D)` and one integrality obstruction. |
| Translated unresolved gap | Prove that a legal **ordered** word cannot also satisfy `D|C` at `q=1`; excursion congruences alone reproduce that condition. |
| Worked example | The ordered `q=5` `(19,31,49)` cycle gives `D=5,C=31` under a one-excursion cut. |
| Known-cycle controls | The ordered `q=13` five-cycle refutes inheritance of circular order by height-zero first returns; `q=5` survives the exact cut; `d=7` `(5,11)` is outside `q<=L`. |
| Cheapest meaningful next test | Derive a new inequality coupling the **locations** of multiple excursions to the full sorted-rank order and test it on the `q=5,13,233` controls; stop if elimination yields only (3). |
| Genuinely intermediate milestone | Exclude every nontrivial ordered `q=1` cycle at all periods and heights. This remains open; it covers the ordered class and leaves unordered integer cycles unaddressed. |

**Decision:** the exact excursion-cut mechanism, by itself, reaches the
same `D|C` obstruction already visible before cutting. A route based
on first-return circular order is refuted by the `q=13` control.
No novel published-result claim, full cycle exclusion, or formal
verification is made.
