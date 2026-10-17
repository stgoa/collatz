# Independent audit of the sparse-ray maximum principle

Written argument checked independently on 17 October 2026. The infinite
certificate hypothesis remains open. This audit imports the established
right-packet identity and exceptional-count recurrence from the main proof
note, not an external theorem.

## Current five-ray criterion

Use mantissas `(12,14,16,18,21)` with index `i=0,1,2,3,4` and exponents
`b>=3`. The smallest grid point is 96. Set

`F(m_i*2^b)=2^((5b+i)/3)`.

The largest mantissa is below twice the smallest, so representations are
unique and this order followed by the next dyadic scale is the sorted grid.
For the five mantissas, upward grid bounds on `3N/2` have mantissas
`18,21,24,28,32` at the original scale. The first three are equalities;
the last two round `27` to `28` and `31.5` to `32`. The target index is
`i+3`, with one dyadic carry when this is at least five. Consequently its
weight is exactly `2F(N)`. Its half has weight `2*2^(-5/3)F(N)`, and
`N/4` has weight `2^(-10/3)F(N)`.

Every target just used is a grid point when it is at least 96; otherwise it
lies in the verified finite base. All source cutoffs are divisible by eight,
so their recurrence cutoffs are exactly `N/4-1`, `3N/2`, and `3N/4`.
If a positive maximum `M=max_(N in G) B(N)/F(N)` occurs at `N`, monotonicity
and the packet hypothesis give

`B(N)<=M F(N)[2^(-10/3)+(2/3)(1+2^(-5/3))]`.

The strict rational estimates follow from integer comparisons:
`2^10=1024>1000` gives `2^(-10/3)<1/10`, and `2^5=32>27` gives
`2^(-5/3)<1/3`. The bracket is therefore less than
`1/10+8/9=89/90<1`, contradicting maximality.

Such a positive attained maximum exists if any seed is nonterminating:
the grid is unbounded, `B` is nondecreasing, and its finite-base values are
zero, while `F(N)` is bounded above and below by positive constant multiples
of `N^(5/3)` on these five rays. Hence `B(N)/F(N)` tends to zero. The
maximum is taken **only on the grid**, so this proof requires neither a
subsolution inequality at nongrid cutoffs nor rounding of a nongrid maximizer.

This proves the five-ray conditional reduction provided all odd seeds below
96 are verified and the packet hypothesis holds at every point of the five
infinite rays. The script `check_five_rays_independent.py` checks that finite
base, all five transitions, the low-target cases, and the exact integer bounds.
The universal packet/current hypothesis remains open.

## Earlier power-weight grid criteria

Let `B(n)` count nonterminating odd seeds at most `n`, let `p>1`, and let
`G` be an unbounded increasing grid of multiples of four starting at `n0`.
Suppose its consecutive ratios are at most `alpha`, all odd seeds below
`n0` terminate, and the packet at each `N in G` satisfies
`<e,Pi_right_N><=0`. The latter follows from a finite current with nonpositive
residual at that cutoff, or merely from packet work bounded above there.

The exact recurrence yields, at every grid point,

`B(N)<=B(N/4-1)+(B(3N/2)+B(3N/4))/3`.

Set `lambda(p)=4^(-p)+((3/2)^p+(3/4)^p)/3`. If
`alpha^p lambda(p)<1`, then all seeds terminate. Indeed, if `B` is nonzero,
`B(n)/n^p` tends to zero and attains a positive maximum `M` at some
`n>=n0`. Choose the next grid point `N`, so `n<=N<=alpha n`. Monotonicity
and the recurrence give

`M n^p=B(n)<=B(N)<=M lambda(p) N^p<=M alpha^p lambda(p)n^p<Mn^p`,

a contradiction. The last inequality is strict even after replacing the
first cutoff `N/4-1` by `N/4`. No inequality at nongrid cutoffs is assumed.

For the 21-ray grid, take all `N=m*2^b`, `b>=3`, for

```
m = 8192, 8467, 8751, 9045, 9348, 9662, 9986,
    10321, 10668, 11026, 11396, 11778, 12173, 12582,
    13004, 13440, 13891, 14358, 14839, 15337, 15852.
```

The grid starts at 65536. Check all adjacent ratios, including the wrap from
15852 to 16384. Their maximum is `10668/10321`, strictly less than
`alpha=10337/10000`. Every grid point is divisible by eight.

For `p=7/5`, put `t=(alpha/4,3alpha/2,3alpha/4)`. The three rational upper
bounds for `(t_i^2)^(1/5)` are, respectively,

`5821/10000`, `11918/10000`, `9032/10000`.

Their validity is checked by raising each positive rational to its fifth
power. Multiplying by `t_i` and weighting by `1,1/3,1/3` gives the strict
bound

`alpha^(7/5)lambda(7/5)<399928193/400000000<1`.

Thus the 21-ray claim is correct conditional on its infinite packet hypothesis
and an actual finite verification of odd seeds below 65536. The independent
exact-rational checks here cover every gap and all three root bounds, not
decimal estimates. This older choice has been superseded by the five-ray
argument above, whose finite base is much smaller.

The earlier 30-ray choice `m=30..59`, `b>=2`, is also valid: its base is
120, mesh ratio is `31/30`, and `p=4/3` gives the strict upper bound
`1199731/1200000`. The same argument applies. The 21-ray choice uses a larger
finite base and fewer infinite ray obligations.

No optimality of 21 rays is claimed. These are conditional reductions, not
certificates for the infinitely many required cutoffs.
