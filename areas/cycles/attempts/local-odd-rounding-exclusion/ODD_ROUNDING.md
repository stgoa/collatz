# C010 — Exact odd-spacing rounds on the complete dyadic circle

**Status: written necessary inequality and exact obstruction to its proposed
exclusion use.** This note proves an all-height lower bound from ordered
adjacent pairs. It does **not** exclude every ordered denominator-one cycle.
Its rational controls satisfy the full closed cycle equations and every
rounded gap inequality while lacking integer states at additive parameter 1.
They are not integer Collatz counterexamples. No novelty or formal verification
is claimed.

Use primitive raw positive odd-only cycles, with no absorber, written
`3n_i+q=2^a_i n_(i+1)`, `a_i>=1`, where the reduced denominator `q` is
positive and coprime to 6. Assume `q<=L=min n_i` and strictly increasing
`F=3z+q2^-h` in increasing `z=n/2^h`, with
`h=floor(log_2(n/L))`. The full rank shift and true weighted intercept are
those of [C006](../../results/ordered-cycle-sparse-forcing/ORDER_RIGIDITY.md). Here `m>1`.

## 1. The seam in the existing gap recurrence is correct

In sorted order, write `z_[0]=L`, with height labels `H_j`. Extend
`z_[j+m]=2z_[j]` and `eps_[j+m]=2eps_[j]`, where
`eps_[j]=q2^-H_j`. With rank shift `+s mod m`, the full equations are

```text
2 z_[j+s] = 3 z_[j] + eps_[j],
2 Delta_(j+s) = 3 Delta_j + eps_[j+1] - eps_[j],
Delta_j = z_[j+1] - z_[j].
```

In particular `Delta_(m-1)=2L-z_[m-1]` is the ordinary retained seam
gap and `Delta_(j+m)=2Delta_j`. At the potentially confusing boundary
`j+s=m-1`, the target is precisely this seam gap; its next endpoint is
`z_[m]=2L`. Therefore, with `B=max H_j` and `G_j=2^B Delta_j`, the
existing modular formula is correct:

```text
2^(1+1_{j>=m-s}) G_((j+s) mod m)
    = 3G_j + 2^B(eps_[j+1]-eps_[j]).
```

The extra factor appears exactly when `j+s>=m`, not one index earlier.
No correction to C006's recurrence is required.

## 2. Sharp local lower bounds from oddness and order

For the following pair calculation, set `H_m=-1` and `n_[m]=L`, so
`z_[m]=n_[m]/2^-1=2L` and `eps_[m]=2q`. Consider adjacent sorted
ranks with heights `a=H_j`, `b=H_(j+1)`. The source height `a` is
nonnegative; the destination height may be `-1` only at the seam.
Their normalized difference `Delta_j` satisfies

```text
b_q(a,b) = 2/2^a,                                      if b=a;
b_q(a,b) = 1/2^a,                                      if b<a;
b_q(a,b) = [q(2^k-1)+eta(q,k)]/(3*2^b), k=b-a>0,        if b>a;

Delta_j >= b_q(a,b),                                   (1)
```

where, for supported `q`,

```text
eta(q,k) = 6,                       if k is even;
eta(q,k) = 2,                       if k is odd and q=1 mod 6;
eta(q,k) = 4,                       if k is odd and q=5 mod 6.
```

**Proof.** Equal heights give a positive difference of two odd integers,
so its numerator is at least 2. If `b<a`, the numerator
`2^(a-b)n_[j+1]-n_[j]` is positive and odd, hence at least 1.
This includes the seam, whose numerator is
`2^(a+1)L-n_[m-1]`.

If `b>a`, put `k=b-a` and
`r=n_[j+1]-2^k n_[j]`. It is positive and odd. Strict increase of
`F` says `3r>q(2^k-1)`. Since `3r=3 mod 6`, the smallest permitted
`3r` is the first number congruent to 3 modulo 6 strictly above
`q(2^k-1)`. For even `k`, the latter is itself 3 modulo 6, requiring
an increment 6; for odd `k` it is `q mod 6`, requiring increment
2 or 4. Dividing by `3*2^b` gives (1). QED.

These bounds are sharp for an isolated ordered pair with odd numerators.
For an upward height step choose the minimal allowed odd `r` and take
`n_[j]` sufficiently large and odd; put `n_[j+1]=2^k n_[j]+r`.
The downward and equal-height minima follow similarly. This sharpness
statement asserts neither simultaneous attainment around a cycle nor
compatibility with all successor arrows.

## 3. A global rounded denominator bound

Let the sums below run over all `m` adjacent gaps, including the seam,
and define

```text
R_q(H) = sum_j b_q(H_j,H_(j+1)),
V(H)   = sum_(H_(j+1)>H_j) (2^-H_j - 2^-H_(j+1)).
```

The seam is a downward height step, so it contributes no term to `V`.
The exact formulas in Section 2 give

```text
R_q(H) = q V(H)/3 + Gamma_(q mod 6)(H),           (2)
```

where `Gamma_1` and `Gamma_5` are positive rational quantities with denominators dividing a power of 2
times 3
obtained from the non-`q` parts of (1). They depend only on the full
sorted height list and the indicated residue class of `q`.

**Global rounding theorem (written proof).** Every cycle in the declared
domain satisfies

```text
L >= R_q(H),
q [C_h/D - V(H)/3] >= Gamma_(q mod 6)(H).         (3)
```

Here `D=2^A-3^m>0` and `C_h` is the **true weighted** intercept at the
minimum, so `L=q C_h/D`. In particular, its coefficient is positive and

```text
q >= Gamma_(q mod 6)(H) / [C_h/D - V(H)/3].       (4)
```

For a proposed ordered profile with nonpositive denominator on the
right, the profile cannot be realized in this domain. Replacing `C_h`
by the larger mechanical intercept `C_c` gives a weaker necessary bound
whenever the resulting denominator is positive.

**Proof.** Sum (1); the complete dyadic gaps telescope to
`z_[m]-z_[0]=L`. Substitute the exact cycle identity
`L=q C_h/D` and (2). Positivity of `Gamma` proves the final assertion.
QED.

This retains arbitrary heights, all adjacent transitions, strict image
order, odd spacing, and the seam. It is stronger than the corresponding
spacing estimate that drops image order, but it remains a necessary
inequality; satisfying it does not supply an integer cycle.

## 4. Exact obstruction: rounding inequalities do not recover integrality

The actual ordered `q=5` cycle

```text
n=(19,31,49),             a=(1,1,3),
chronological h=(0,0,1),  sorted H=(0,1,0),
D=2^5-3^3=5,             C_h=19,
```

becomes a positive rational cycle at additive parameter 1 after dividing
all states by 5. Its sorted normalized coordinates, images and complete
gaps are

```text
z = (19/5, 49/10, 31/5),
F = (62/5, 76/5, 98/5),
Delta = (11/10, 13/10, 7/5).
```

The parameter-one sharp bounds in (1) are
`(1/2,1/2,1)`. **Every gap exceeds its required bound**, and

```text
R_1(H)=2,       L/q=19/5>2,
V(H)=1/2,      Gamma_1(H)=11/6.
The bound (4) at residue class q=1 mod 6 is q>=55/109.
```

Thus the complete closed rational cycle satisfies every adjacent
parameter-one rounded lower inequality, their global sum, and the exact
gap recurrence. It fails precisely the missing exact integral lattice:
its states and scaled gaps still have reduced denominator 5. Applying a
ceiling to the aggregate minimum does not repair this example: the least
odd integer at least `R_1(H)` is 3, still below `19/5`.

The same control also passes all nonadjacent pairwise versions of (1)
inside one normalized annulus: its only remaining pair has equal height
and difference `12/5>=2`. This is a counterexample to using the full set
of these **lower inequalities** as an exclusion certificate; it does not
refute an argument retaining every exact congruence simultaneously.

A larger independent control is the ordered `q=13` five-cycle
`(283,431,653,493,373)`. Its sorted heights are `(0,1,0,0,0)`.
At additive parameter 1 the gaps are
`(87/26,93/26,58/13,62/13,73/13)`, which individually exceed
`(1/2,1/2,2,2,1)`. Hence `R_1=6<283/13`; even the odd-rounded
aggregate lower bound 7 is below `283/13`.

The inequality is not vacuous: the ordered `q=83` cycle
`(157,277,457,727,283,233,391)` has sorted heights
`(0,2,1,1,0,0,0)`, giving `R_1=15/2>157/83`. Here the
rounded denominator lower bound is `2407/545>4`. Its additive-one
rational shape therefore fails this rounded relaxation. The bounds
separate some profiles while retaining other exact nonintegral cycles.

The raw `d=7` cycle `(5,11)` has `q=7>L=5`, outside the declared
`q<=L` domain. The actual `d=5`, `d=13` cycles above remain allowed at
their actual parameters. No exclusion of a legitimate control is used.

## 5. Decision in seven fields

| Field | C010 rounding assessment |
| --- | --- |
| Objects | Complete sorted dyadic gaps of primitive ordered rational cycles, exact odd numerator spacing, and the true height profile. |
| Structural gain | The all-height inequality (3), with explicit dependence on upward height transitions, parameter residue modulo 6 and the dyadic seam. |
| Translated unresolved gap | Exact integral compatibility around the entire cycle remains necessary; lower rounding inequalities do not imply or contradict it universally. |
| Worked example | The `q=5` three-cycle rescaled to additive 1 passes every adjacent and within-annulus pairwise sharp lower bound, but retains denominator 5. |
| Known-cycle controls | Actual `q=5,13,83` examples satisfy their own parameter bounds; `d=7,L=5` lies outside `q<=L`. |
| Cheapest meaningful next test | Use the exact global lattice together with a structure absent from this monotone lower-bound relaxation; reject any proposal whose only output is (3) or the original `D|C_h`. |
| Genuinely intermediate milestone | Exclude nontrivial ordered denominator-one cycles at arbitrary heights and periods, leaving unordered integer cycles open. This remains unproved. |

**Decision:** preserve the rounded bound as a valid necessary diagnostic.
Reject its proposed universal exclusion use: exact known rational cycles
survive all of its parameter-one inequalities. This does not rule out a
stronger inequality using genuinely global information or the full exact
lattice. No published cycle record is improved by this batch's rounding
result; it excludes no new universal class of integer cycles.
