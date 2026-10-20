# C010 — The complete dyadic gap lattice

**Status: elementary written argument, independently agent-reviewed.**
This identifies exactly what taking all sorted gaps preserves. It gives
no new exclusion of denominator1. Cycles use the raw positive odd-only
map, with no absorbing state; q denotes the reduced odd denominator,
not a shortcut step count or an arbitrary scale multiple.

## 1. An integer change of coordinates with a positive inverse

For m>=1 and a vector Z=(Z_0,...,Z_(m-1)), define the dyadic shift

```
(E Z)_j = Z_(j+1) for j<m-1,     (E Z)_(m-1)=2Z_0.
```

Thus E^m=2I. Put U=E-I and G=UZ. These are the complete gaps,
including the seam G_(m-1)=2Z_0-Z_(m-1). The identity

```
(E-I)(I+E+...+E^(m-1))=E^m-I=I
```

shows that U is an integer unimodular matrix, with integer inverse
I+E+...+E^(m-1). Explicitly,

```
Z_0 = sum_j G_j,
Z_j = sum_i G_i + sum_(i<j) G_i.                 (1)
```

Consequently G has all entries positive if and only if
0<Z_0<Z_1<...<Z_(m-1)<2Z_0. For m1 this means just Z_0>0.
The gap cone is exactly the normalized order cone under this map.
No inequality or boundary condition is discarded.

Because both U and its inverse have integer entries:

- Z is integral if and only if G is integral;
- for integer vectors, gcd of all entries of Z equals gcd of all entries
  of G (use the nonnegative gcd, allowing signed entries);
- for rational vectors, the least positive common denominator of the
  coordinates is identical for Z and G.

The last statement follows by applying the first to kZ and kG for
every positive integer k. Individual coordinates may cancel different
factors; the claim concerns the whole vector, not each gap separately.

## 2. Application to actual cycles

For a reduced numerator cycle 3n_i+q=2^a_i n_(i+1), let L=min n_i,
h_i=floor(log_2(n_i/L)), B=max h_i. Sort

```
Z_j = 2^(B-H_j) n_[j],
p_j = 2^(B-H_j),
```

where H is the sorted height list. These Z lie in [2^B L,2^(B+1)L).
They are distinct because the original n_i are odd. Their gcd is1:
any odd common divisor would divide all reduced numerators; a cycle
arrow then makes it divide q, contradicting numerator reduction.
A state at height B makes one Z odd. Therefore their complete gap vector
also has gcd1. After normalizing the parameter to1 by dividing all
states by q, the scaled gap vector G/q has common reduced denominator
exactly q. Changing from states to gaps has not made the lattice easier.

This gcd statement and (1) hold for unordered cycles as well. Circular
successor order enters only in the next section.

## 3. The complete ordered operator is unchanged

Assume m>1, q<=L and circular normalized successor order. C005 gives
a coprime rank shift s, 1<=s<m, and A=m+s. In dyadic extension the
state equations are

```
K Z = q p,           K = 2E^s-3I.                (2)
```

Both U and K are polynomials in E, so UK=KU. Applying U gives

```
K G = q U p.                                    (3)
```

Conversely, U is invertible, so (3) and G=UZ imply (2). The last
coordinate of Up is 2p_0-p_(m-1); the factor2 at the seam is essential.
In modular indices (3) is exactly C006's recurrence

```
2^(1+1_(j>=m-s)) G_((j+s) mod m)
    = 3G_j + q(p_(j+1)-p_j),                    (4)
```

with p_m=2p_0. The cases j+s=m-1 and j+s=m are distinct; (4)
handles both. Independent audits found no seam error in C006.

Thus this is stronger than a determinant comparison: the state and gap
systems use the same linear operator K in different coordinates. Its
determinant has absolute value D=2^(m+s)-3^m, since the rank permutation
is one m-cycle and the product of the successor coefficients is
2^(m+s). The already-recorded full integrality obstruction remains.
No new independent congruence follows from taking more linear
combinations of these complete equations.

Summing (4) gives the exact scalar relation

```
2 sum_(j<s) G_j - sum_j G_j = q 2^B.             (5)
```

Since sum G=Z_0=2^B L and sum_(j<s)G_j=Z_s-Z_0,
equation (5) is precisely 2Z_s=3Z_0+q2^B, the original minimum
arrow. It is not a second global constraint.

## 4. What integrality itself still accomplishes

Suppose positive rational Z and prescribed nonnegative heights H, H_0=0,
with B=max H_j, satisfy
the full ordered equations, the dyadic range conditions, and legal
chronological valuations a_i=c_i+h_i-h_(i+1)>=1. Let the additive
parameter q be positive odd. The resulting cyclic odd-word solutions
have the form n_i=q C_i/D, with C_i and D odd. If every G_j is integral,
then every Z_j is integral by (1). Because n_i=Z_j/2^(B-H_j), its
reduced denominator is a power of2; its cycle formula has odd denominator,
so n_i is an integer. It is then odd, as an integer quotient of odd
integers. Hence lowbit(Z_j)=p_j automatically.

Accordingly, for legal profiles, retaining **all exact gap integrality**
retains the original integer-cycle problem, including oddness. Replacing
integrality by necessary spacing inequalities is a relaxation. The
[rounding note](ODD_ROUNDING.md) tests that relaxation and supplies
an exact rational witness it fails to eliminate. Neither statement
rules out a future nonlocal arithmetic proof.

In particular, these equivalences are not an impossibility theorem for
integer cutting planes. Eliminating a single fixed profile to its exact
fractional solution can certify its failure of integrality. The unresolved
step is an argument uniform over unrestricted legal profiles, not whether
a supplied finite rational solution can be checked.

## 5. Arbitrarily large slack survives every displayed spacing cut

The finite rational controls are not an accident of short periods.
The persisted [C004 spacing construction](../close-pair-lattice-criterion/SIZE_PROBE.md)
already supplies primitive mechanical rational cycles with arbitrarily
large distances between distinct states. Its seam has a particularly
simple exact value, which extends that obstruction to the complete
gap system tested here.

Take coprime A,m with m>=2, 2^A>3^m and positive mechanical valuations.
Use the phase intercepts from C004:

```
B_l = sum_(j=0)^(m-1) 3^(m-1-j) 2^floor((jA+l)/m),
D = 2^A-3^m,                  0<=l<m.
```

Their increasing rational cycle states are x_l=B_l/D, and the complete
normalized height profile is zero because B_(m-1)<2B_0. These phases
are rotations of a primitive cycle. R71 supplies their exact reduced
denominator D. C004 proves each interior increment is a single monomial
strictly greater than 3^(m-1)/2 before dividing by D.

For every j=1,...,m-1, coprimality makes jA mod m nonzero. Changing
l from0 to m-1 therefore raises each such floor by1, while the j0
summand stays 3^(m-1). Hence

```
B_(m-1) = 2B_0 - 3^(m-1),
2x_0-x_(m-1) = 3^(m-1)/D.                       (6)
```

Put epsilon=A-m log_2(3)>0. Every complete circular gap, including
the seam, consequently satisfies

```
Delta_j > 3^(m-1)/(2D)
        = 1/[6(2^epsilon-1)].                    (7)
```

C004 gives an elementary construction of coprime upper approximations
with epsilon tending to0 and m unbounded. Thus for every prescribed
K>2 there is such a rational additive-one cycle with **every complete
gap greater than K**. Its minimum is the sum of its gaps, greater
than mK. At the corresponding raw parameter q=D, q<=min B_l.
The denominator is greater than1: eventually A>=3, and
D=2^A-3^m is5 or7 modulo8, never1.

Every proper circular pair difference is a sum of one or more complete
gaps (with the dyadic factor on wrapped gaps), so it too exceeds K.
Since all heights are0, the sharp additive-one bound is2 for a pair
in the same annulus and1 for a pair crossing the seam. All such
bounds therefore hold with arbitrarily large slack. Their adjacent
sum is2m-1, already an odd integer; the minimum exceeds mK>2m.
Odd-rounding this summed bound also fails to exclude the family.

This proves an all-size obstruction to the proposed relaxation: exact
cycle equations, actual dyadic heights, image order, all the sharp
pairwise lower spacing inequalities and their nonnegative linear
combinations still admit noninteger rational cycles at additive1.
It does not refute the inequalities themselves, which are necessary,
nor arbitrary integer cutting planes or the desired q1 theorem.
These mechanical cycles are already known to be nonintegral; the
point is that this particular rounding method cannot recover even
their exclusion. No new excluded word class is claimed.

For these all-zero height profiles, V=0 and Gamma_1=2m-1. The
rounded denominator lower bound is therefore (2m-1)D/B_0<2/K.
It can tend to zero while the actual reduced denominator remains
greater than1. This quantifies the weakness of this particular bound.
