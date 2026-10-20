# C006 independent mathematical review

**Status:** the stated sparse-forcing denominator law, its height-free
corollary, and the resulting fixed-parameter finiteness consequence pass
this independent proof review. This is a review
of the written argument and selected exact controls, not an independent
replay of the entire finite census or a novelty claim. The ordered
denominator-one exclusion and the unrestricted Collatz cycle question remain
open.

## Gap theorem, including the seam

In the setting of [ORDER_RIGIDITY.md](ORDER_RIGIDITY.md), the normalized
states are distinct. If `n_i/2^h_i=n_k/2^h_k` for odd numerators, then
`h_i=h_k` and `n_i=n_k`. Thus the sorted gaps
`Delta_j=z_[j+1]-z_[j]` for `0<=j<m`, using `z_[m]=2z_[0]`, are all
strictly positive and sum to `L=z_[0]`. For `m>1`, each gap is strictly
less than `L`.

The extension must include **both** `z_[j+m]=2z_[j]` and
`eps_[j+m]=2eps_[j]`. In particular, `eps_[m]=2q`, while
`eps_[m-1]<=q`, so the seam forcing is positive. On a rank shift
`+s mod m`, the ordered equations are `2z_[j+s]=3z_[j]+eps_[j]`.
Subtracting adjacent equations and clearing the height denominator
with `G_j=2^B Delta_j` and
`T_j=2^B(eps_[j+1]-eps_[j])` gives the exact integer recurrence

```
2^(1+floor((j+s)/m)) G_((j+s) mod m)=3G_j+T_j,
G_j in Z_(>0), T_j in Z, sum_j G_j=2^B L.
```

The seam `T_(m-1)>0`, so `1<=J=#{j:T_j!=0}<=m`. The rank shift is
transitive on the `m` states because the cycle is primitive; hence
`gcd(s,m)=1`, and the same shift is transitive on gap indices.

The `J` forced positions cut the shifted index cycle into `J`
zero-forcing runs. Their lengths total `m-J`, so some run has length
`t>=ceil(m/J)-1`. Along any such run, with exponent sum
`E=sum(1+floor((j+s)/m))>=t`, iteration yields

```
2^E G_end=3^t G_start.
```

As `G_start` and `G_end` are integers, `2^E` divides `G_start`, so
`G_start>=2^E`. Combined with the strict gap inequality this gives
`L>2^(E-B)>=2^(t-B)`. This includes the boundary `J=m`: all runs
have `t=E=0`, and the only divisibility assertion is `G_start>=1`.
The other endpoint `J=1` gives one run of length `m-1`. Neither case
requires a missing gap or an assumed nonzero run.

The positive Green comparison gives `L<=q C_c/D`; hence each run
also gives the exact rational bound

```
q>(D/C_c) 2^(E-B).
```

Finally, multiplication of the original odd-cycle arrows gives
`delta=A log 2-m log 3=sum_i log(1+q/(3n_i))<=mq/(3L)`.
Substituting the uniform lower bound for `L` proves all three claims
in (G1). The second is a direct intercept consequence; the third
uses the product identity.

## Effective consequence and its scope

[Bugeaud, *B′*, Theorem 1.1, equation (1.2)](https://arxiv.org/pdf/2209.00275)
states an effective lower bound of the form
`log|Lambda|>=-C h*(alpha_1)h*(alpha_2)log B_src` for two fixed
algebraic numbers of degree-one field. Take `alpha_1=2`,
`alpha_2=3`, coefficient pair `(A,-m)`, and
`B_src=max(3,A,m)=A<2m` for `m>1`. The linear form is nonzero by
multiplicative independence of 2 and 3. Thus an effective absolute
`K>0` exists with `delta>=(2m)^(-K)`, equivalently the note's
`delta>=c_0 m^(-K_0)` after changing absolute constants. No numerical
value for these constants was checked or is needed.

It follows that `q` grows at least exponentially in `m/J-B` divided
by a fixed power of `m`, as in (G2). At fixed upper bounds
`q<=Q`, `B<=B_0`, and `J<=J_0`, the right side eventually exceeds
`Q`, since `m/J_0` grows linearly while `log m` grows sublinearly.
Thus `m` is effectively bounded. Order gives `A=m+s<2m`; there are
finitely many positive valuation words of those bounded totals, and
each positive word has at most one rational cycle. This verifies the
finite-cycle consequence. With only `q,B` fixed, (G2) instead gives
`J=Omega(m/log m)`; it does not bound `m`.

### Height-free corollary

The added implication (H1) is valid in the same ordered domain. The
chronological height relation is
`h_(i+1)-h_i=c_i-a_i<=1`, since `c_i<=2` and exact raw valuations
`a_i>=1`. A path starting at `h_0=0` and attaining `B` must therefore
visit every level `0,...,B`. These `B+1` labels all occur in the sorted
height list, whose adjacent internal entries must change at least `B`
times. The seam is always forced, so `J>=B+1`.

Replacing `B` by its upper bound `J-1` in the exponents of (G1)
gives the first two inequalities in (G5). The corresponding substitution
in (G2) gives

```
m/J < J + log_2(q/(3c_0)) + (K_0+1)log_2 m.
```

For bounded `q<=Q` and `J<=J_0`, this inequality is impossible for
all sufficiently large `m`, since the left side is at least `m/J_0`
and the right side grows at most logarithmically plus a constant.
The positive valuation words then form a finite effectively bounded
set, so the fixed-`q,J` finite-cycle statement is sound.

For fixed `q`, put
`T_q(m)=log_2(q/(3c_0))+(K_0+1)log_2 m=O_q(log m)`.
Then `m<J^2+T_q(m)J`. For sufficiently large `m`, `T_q(m)>=0`;
solving the quadratic inequality gives
`J>(sqrt(T_q(m)^2+4m)-T_q(m))/2 >= sqrt(m)-T_q(m)/2`.
Thus `J>=sqrt(m)-O_q(log m)` and in particular
`J=Omega(sqrt(m))`, as stated. This remains only a necessary law
for hypothetical ordered cycles; no finite denominator-one case is
excluded. No new finite scan was used for this addendum.

## Exact controls and comparison

I separately recomputed the ordered one-height `q=233` cycle from its
eight raw arrows. Its sorted rank shift is `s=5`, `B=1`, and its
integer gaps and forcing terms are

```
G=(387,381,348,516,508,464,688,522),
T=(-233,233,0,0,0,0,0,466).
```

Here `sum G=3814=2L` and `J=3`. At `j=0`, the recurrence reads
`2*464=3*387-233`; at the seam `j=7`, it reads
`4*508=3*522+466`. The raw word has
`C_c=14501`, `C_h=13349`, `D=1631=7*233`; its reduced denominator
is indeed `q=233`, so even one legal height defect can change the
mechanical gcd. I also recomputed the ordered `q=13` control's ten
pairwise normalized gaps: their smallest odd numerator is 15, attained
at `347-227=120`. These checks cover the seam and two distinct
failed strengthening proposals; they do not certify the full census.

The generic extremal rotation argument and odd-lattice capacities in
Section 5 are algebraically valid without circular order, and the
text correctly labels them as baselines. [Brox's published
few-descents paper](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/en/publishing-house/journals-and-series/acta-arithmetica/all/92/2/111840/collatz-cycles-with-few-descents)
counts chronological descents. The present `J` counts transitions of
dyadic height after sorting normalized states, including the seam.
These are different parameters; this review does not assert novelty
against every published cycle result.

The sole textual slip found during review was the proof's reference to
the “second” inequality of (G1) after using the product identity; that
identity proves the **third** inequality. It was corrected in the
reviewed source before this note was saved. No remaining mathematical
error was found in the scoped claims above.
