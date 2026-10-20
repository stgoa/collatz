# C009 independent excursion arithmetic and first-return review

**Status:** exact integer-compression lemma, exact loss of circular order
under a first-return cut, and scoped drift controls. No nontrivial
denominator-one cycle is excluded. The raw positive odd-only map is
used without an absorber at 1. This note independently audits
[EXCURSION_ARITHMETIC.md](EXCURSION_ARITHMETIC.md).

## 1. The true affine cut retains the integer lattice

Fix any positive valuation segment `a_0,...,a_(ell−1)` and positive odd
parameter `q`. Let `A_j=sum_(i<j) a_i`, `A=A_ell`, and

```text
C_j = sum_(i<j) 3^(j−1−i) 2^A_i.
```

**Lemma (written proof).** If positive odd integers `x,y` satisfy

```text
2^A y = 3^ell x + q C_ell,                         (1)
```

then the entire segment from `x` to `y` consists of positive odd
integers and has exactly the prescribed valuations. Thus the exact
endpoint congruence `3^ell x+q C_ell=0 (mod 2^A)`, together with an
odd endpoint, already includes every intermediate odd valuation
cylinder.

For a prefix of length `j`, the composition identity is

```text
C_ell = 3^(ell−j) C_j + 2^A_j C_tail.
```

Equation (1) modulo `2^A_j` then forces
`2^A_j | 3^(ell−j)(3^j x+q C_j)`. Since 3 is a 2-adic unit,
`u_j=(3^j x+q C_j)/2^A_j` is an integer. It is positive, and the
identities `3u_j+q=2^a_j u_(j+1)` hold. For every `j<ell`, the
right side is even and `q` is odd, so `u_j` is odd; `y` is odd by
hypothesis. Hence `v_2(3u_j+q)=a_j` exactly. QED.

For a height-zero first return, the true segment intercept written
in normalized coordinates is the weighted `C_h`, equal to this
ordinary `C_a` because the endpoint heights agree. Replacing it by
the unweighted mechanical `C_c` changes (1); that replacement, not
exact compression, loses the integer lattice. The compact ordered
`q=13` control makes this visible. In the cycle

```text
n=(283,431,653,493,373),
a=(1,1,2,2,2), h=(0,0,1,0,0), c=(1,2,1,2,2),
```

the sole positive-height excursion `431 -> 653 -> 493` has original
word `(1,2)`, normalized word `(2,1)`, and exact equation

```text
8*493 = 9*431 + 13*5.
```

The unweighted mechanical intercept would be `7` instead of `5`;
it sends the same start to `(9*431+13*7)/8=1985/4`, not an integer.

## 2. Closing exact cuts returns the original denominator test

Cut a full period at every height-zero state. For block `b`, let
`ell_b`, `A_b`, `C_b` be its length, valuation total, and **true**
intercept, and let `x_b,x_(b+1)` be its odd endpoints. The compressed
integer system is

```text
2^A_b x_(b+1) − 3^ell_b x_b = q C_b.             (2)
```

The lemma proves that (2) already implies all intermediate integer
arrows. The cyclic coefficient matrix of the `k` block equations has
determinant `(-1)^(k−1)(2^A−3^m)`, where
`A=sum A_b`, `m=sum ell_b`. Its Smith form is
`diag(1,...,1,D)` for `D=2^A−3^m`: any prime dividing `D` is neither
2 nor 3, and deleting the last row and column leaves a triangular
minor `±3^(ell_0+...+ell_(k−2))`, a unit at that prime. At all other
primes the determinant is already a unit. Composing (2) around the
cycle gives

```text
D x_0 = q C_a = q C_h.                            (3)
```

At `q=1`, (3) is exactly `D|C_h` when `x_0` is integral; it is not
a second denominator obstruction. The original rotation identities
`2^a_i C_(i+1)=3C_(i)+D` propagate `D|C_(0)` to every phase because
2 is invertible modulo odd `D`; the lemma then supplies all exact
odd-only arrows. Actual dyadic height inequalities and sorted
successor order still have to be checked. Compression preserves the
lattice when it retains `C_h`, but it does not simplify that global
shape-and-divisibility conjunction.

## 3. First return can destroy circular rank order

There is a general combinatorial reason. Consider a rotation
`j -> j+s (mod m)` on `m` ordered ranks. Delete one rank and induce
first return on the remaining `m−1` ranks. Rotate labels so the
deleted rank is zero; retained ranks `j=1,...,m−1` compress to
`j−1`. The predecessor `j=m−s` returns through the deleted point
to rank `s`, giving compressed shift `2s−1 (mod m−1)`. The other
arrows split into

```text
j=1,...,m−s−1:       m−s−1 arrows of shift s;
j=m−s+1,...,m−1:     s−1 arrows of shift s−1
                         (all shifts mod m−1).
```

For `2<=s<=m−2`, both regular types occur and their shifts differ,
so the first-return permutation is **not** a circular rank shift.
For `s=1` or `s=m−1`, it is respectively the nearest-neighbor
forward or backward rotation. This is a precise failure of recursive
circle order after a single deleted state; it does not assert that
every abstract deletion is realizable by an odd cycle.

The ordered `q=13` cycle above realizes the failure with only one
positive-height state. Its sorted normalized states are
`(283,653/2,373,431,493)` with strictly increasing scaled images
`(862,986,1132,1306,1492)`, so the full rank shift is `+3 mod 5`.
The height-zero core sorted by value is `(283,373,431,493)`. Its
first-return rank map is `(2,0,3,1)`, whose offsets modulo four are
not constant. The `q=233` one-defect ordered cycle offers a larger
check: the height-zero core sorted indices are `(0,2,7,4,1,6,3)`,
and its first-return rank map is `(4,6,0,5,1,2,3)`, with offsets
`{2,4,5}` modulo seven. These are actual ordered integer numerator
cycles, not just abstract permutations. Neither claims anything about
an unknown `q=1` cycle.

## 4. Drift signs do not supply a local q=1 exclusion

Two **open** `q=1` paths have exact positive odd arrows and locally
increasing sorted scaled images. They are not cycles:

```text
L=7:  7 -> 11 -> 17 -> 13,
      sorted z=(7,17/2,11,13), F=(22,26,34,40).
      The excursion 11 -> 17 -> 13 has 8*13=9*11+5 and rises by 2.

L=11: 19 -> 29 -> 11,
      sorted z=(11,29/2,19), F=(34,44,58).
      The excursion has 16*11=9*19+5 and falls by 8.
```

Thus oddness, positive-height excursion shape, and local sorted-F
order do not fix the sign of a return's drift. Even a contracting
homogeneous slope need not make an actual ordered excursion descend:
the ordered `q=83` cycle
`(157,277,457,727,283,233,391)` has excursion
`277 -> 457 -> 727 -> 283`, for which
`32*283=27*277+83*19`; slope `27/32<1`, but the return increases
by 6. Its full sorted scaled images are
`(554,566,628,727,782,914,932)`, strictly increasing.

## 5. Independent review and decision

I checked the proof in [EXCURSION_ARITHMETIC.md](EXCURSION_ARITHMETIC.md):
its prefix-divisibility lemma, block determinant and Smith argument,
the `q=5` cut arithmetic, and the `q=13` sorted values and first-return
map are correct under the stated hypotheses. The one-rank deletion
law above explains why the `q=13` counterexample is structural.

**Decision:** exact excursion compression is a faithful integer
re-expression, but closure recovers only the existing `D|C_h` test.
Removing positive-height states can destroy the circular order that
made the normalized word mechanical. A new all-period `q=1` theorem
would have to couple the full weighted divisibility with the complete
sorted-rank inequalities; neither excursion closure nor a local drift
rule provides it here. The broader Collatz cycle exclusion remains open.
