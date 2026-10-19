# C002 — Unequal slopes: subexponential cancellation and denominator escape

**Status: written argument with two published inputs; independent lane, 2026-10-19.**
This note reads the full primary source identified in C001, checks its exact
quantifiers, and applies it to two fixed nonempty positive valuation words.
It covers every exponent pair whose combined word has positive raw
denominator, including pairs with one expanding block. No novelty or formal
verification claim is made. The constants and eventual thresholds below may
depend on the two fixed words.

## 1. Precise conclusion and word convention

For a word z of length m and valuation sum A, write

```
P_z=2^A,  Q_z=3^m,
C_z=sum_(j=0)^(m-1) 3^(m-1-j) 2^(a_0+...+a_(j-1)),
D_z=P_z-Q_z.
```

The affine action is `(Q_z*x+C_z)/P_z`. For `D_z>0` its fixed
point is a positive odd rational cycle with exact displayed valuations,
and its common reduced denominator is `d_z=D_z/gcd(C_z,D_z)`.
This uses the raw odd-only Syracuse recurrence, without making 1 absorbing.
The elementary legality and cyclic-rotation argument are retained from
[R71](../../residual_progress/lattice_cycles/BALANCED_DENOMINATORS.md) and
[C001](../C001/REPETITION_SPECTRUM.md).

Fix nonempty words u,v. Put

```
a=sum(u), r=len(u), b=sum(v), s=len(v),
Delta=a*s-b*r,
G_u(k)=(P_u^k-Q_u^k)/D_u,
G_v(ell)=(P_v^ell-Q_v^ell)/D_v,
K=D_u*C_v-D_v*C_u.
```

Each G is a positive integer geometric sum, even when its D is negative.
Unique factorization makes both D_u and D_v nonzero.

**Unequal-slope theorem.** Suppose `Delta!=0`. Uniformly over positive
integers k,ell as `N=k+ell` tends to infinity,

```
log gcd(G_u(k),G_v(ell)) = o(N).                         (1)
```

Restricting only to pairs for which `D_(u^k v^ell)>0`, put
`A=a*k+b*ell` and `M=r*k+s*ell`. Then

```
0 <= A*log(2)-log d_(u^k v^ell) = o(N).                 (2)
```

Thus for every eta>0 there is a threshold N_0(u,v,eta) such that every
such positive pair with N>=N_0 satisfies

```
d_(u^k v^ell) >= 2^((1-eta)*A).                         (3)
```

In particular, every fixed denominator, and even every bounded set of
denominators, occurs for only finitely many exponent pairs in this fixed
two-block family. An empty or finite positive domain makes that assertion
vacuous. Neither block is individually required to have positive D.

## 2. Primary source and the exact inputs

P. Corvaja and U. Zannier, *A lower bound for the height of a rational
function at S-unit points*, Monatshefte für Mathematik 144 (2005), 203–224,
DOI [10.1007/s00605-004-0273-0](https://doi.org/10.1007/s00605-004-0273-0).
The inspected [full author preprint, math/0311030v2](https://arxiv.org/pdf/math/0311030)
is dated 22 April 2004. References below use its printed page numbers.

Take normalized rational absolute values, `|p|_p=1/p`,
`log^-(t)=min(0,log(t))`, and logarithmic height
`h(x/y)=log max(|x|,|y|)` for coprime integers x,y.

**Input A — Corollary 1, Eq. (1.3), p. 2; proof pp. 16–17.**
For fixed finitely generated `Gamma <= (Q^*)^2` and epsilon>0, all but
finitely many multiplicatively independent pairs `(U,V) in Gamma` satisfy

```
sum_(nu in M_Q) log^- max(|U-1|_nu,|V-1|_nu)
    >= -epsilon*max(h(U),h(V)).                         (CZ-A)
```

**Input B — Proposition 1, Eq. (2.2), p. 4; proof pp. 4–7.**
Let S contain the archimedean places, Gamma be as above, and f be a Laurent
polynomial with constant monomial 1 present. For epsilon>0, solutions of

```
sum_(nu in S) log^- |f(U,V)|_nu
    < -epsilon*max(h(U),h(V))                           (CZ-B)
```

lie in finitely many translates of one-dimensional subtori, plus a finite
set. We use this with `S={infinity,2,3}` and S-unit coordinates.

The full text, including Proposition 2 and the proof of Corollary 1, was
inspected: Input A removes every infinite exceptional family by requiring
multiplicative independence. Input B retains translates, which Section 5
handles explicitly. The paper gives effective descriptions of the relevant
one-dimensional exceptional groups; this application supplies no effective
height bound for the residual finite exceptional set and no computable
threshold in (1)–(3). It relies on the Subspace Theorem, not a finite test.

## 3. Rational S-units and all local contributions

Set

```
alpha=2^a/3^r, beta=2^b/3^s,
U=alpha^k, V=beta^ell,
Gamma=<(alpha,1),(1,beta)>.
```

For integers i,j, `U^i*V^j=1` implies

```
a*k*i+b*ell*j=0,
r*k*i+s*ell*j=0.
```

The determinant is `k*ell*Delta!=0`. Hence i=j=0: **every** pair under
consideration is multiplicatively independent. There is no omitted
subsequence of dependent pairs.

Write `L_u=2^(a*k)-3^(r*k)` and `L_v=2^(b*ell)-3^(s*ell)`.
These are nonzero odd integers prime to 3; signs are immaterial to gcds.
At each place the terms in (CZ-A) are as follows.

| Place | Calculation | Contribution |
| --- | --- | --- |
| 2 | U and V have positive 2-adic valuation, so both U−1 and V−1 are units. | 0 |
| 3 | `|U−1|_3=3^(r*k)`, `|V−1|_3=3^(s*ell)` are greater than 1. | 0 |
| p different from 2,3 | The denominators are p-adic units. | `-min(v_p(L_u),v_p(L_v))*log(p)` |
| infinity | `e_infty=log^- max(|U−1|,|V−1|)` | at most 0 |

Consequently the entire sum is exactly

```
-log gcd(|L_u|,|L_v|)+e_infty.                           (4)
```

One must not assert `e_infty=0` in general. Its nonpositive sign suffices:
(CZ-A) and (4) give, outside a finite set,

```
log gcd(|L_u|,|L_v|) <= epsilon*H+e_infty <= epsilon*H,
H=max(k*max(a*log2,r*log3), ell*max(b*log2,s*log3)).       (5)
```

For a fixed pair of words, `H<=c*(k+ell)` for a fixed positive c, and
H tends to infinity with k+ell. The map `(k,ell)->(U,V)` is injective,
so the exceptional set gives only finitely many index pairs. Taking
epsilon as small as required proves the **uniform** little-o statement,
including sequences along which one exponent stays fixed.

Since `G_u(k)` divides `|L_u|` and `G_v(ell)` divides `|L_v|`, their gcd
divides the gcd in (5). This proves (1). No primality or coprimality
assumption on D_u,D_v was used.

## 4. Passing from geometric sums to actual cancellation

Chronological composition, with u first and v second, gives

```
C_w=Q_v^ell*C_u*G_u(k)+P_u^k*C_v*G_v(ell),
D_w=P_u^k*P_v^ell-Q_u^k*Q_v^ell,
D_u*C_w-C_u*D_w=P_u^k*K*G_v(ell),
D_v*C_w-C_v*D_w=-Q_v^ell*K*G_u(k).                      (6)
```

For D_w>0, let `g=gcd(C_w,D_w)`. Since D_w is prime to 6, so is g.
The last two identities imply

```
g divides |K|*gcd(G_u(k),G_v(ell))                      (7)
```

provided K!=0. In the positive domain, unequal slopes ensure this.
Indeed, K=0 would force D_u,D_v to have the same sign because C_u,C_v>0.
They cannot both be negative when D_w>0. If both are positive, their
rational fixed points coincide. Exact valuations and determinism give
`u^infinity=v^infinity`. Both words are powers of a common primitive
word, so `a/r=b/s`, contrary to Delta!=0. This is the same common-fixed-point
argument as C001, with both repetitions retained.

Equations (1) and (7) now give `log g=o(N)`. This alone is not enough:
the positive integer D_w might conceivably be much smaller than its
two exponentially large summands. Section 5 supplies the needed bound.

## 5. Positive power differences: handling an expanding block

We prove the following auxiliary consequence of Input B, without importing
an additional theorem on linear forms in logarithms.

**Power-gap lemma.** Uniformly over A,M>=1 with `2^A>3^M`,

```
log(2^A-3^M)=A*log2-o(A) as A tends to infinity.         (8)
```

Apply (CZ-B) with

```
Gamma_0=<(2,1),(1,3)>,  (U,V)=(2^A,3^M),
f(X,Y)=X/Y-1, S={infinity,2,3}.
```

The Laurent monomials are 1 and X/Y, so the constant-monomial condition
is satisfied. At 2, f(U,V) is a unit; at 3 its absolute value is 3^M>1.
Thus the left side of (CZ-B) is exactly

```
log^- |2^A/3^M-1|.                                    (9)
```

For fixed epsilon, every exceptional translate has an equation
`U^p V^q=lambda`, where p,q are integers not both zero. Its intersection
with our positive power grid has the following exhaustive forms.

* If p and q are both nonzero, comparison of valuations at 2 and 3 fixes
  A and M. There is at most one point. If lambda is not rational, there
  are no rational grid points in the first place.
* If p=0, M is fixed. As A grows, `2^A/3^M-1` eventually exceeds 1, so
  (9) is zero and cannot violate the desired lower bound. Only finitely
  many bad points remain.
* If q=0, A is fixed. Positivity `3^M<2^A` permits only finitely many M.

Therefore the exceptional translates and the isolated exceptional points
together contain **only finitely many bad positive power pairs**. Since
`max(h(2^A),h(3^M))=A*log2` on this domain, for all sufficiently large A
and every allowed M,

```
|2^A/3^M-1| >= exp(-epsilon*A*log2).                   (10)
```

This step does not simply discard the exceptional translates; their
intersection with the exact grid and the positivity condition are used.

If `2^A>=2*3^M`, then `2^A-3^M>=2^(A-1)`. Otherwise (10) gives

```
2^A-3^M >= 3^M*exp(-epsilon*A*log2)
          > 2^(A-1)*exp(-epsilon*A*log2).              (11)
```

Together with `2^A-3^M<2^A`, these bounds prove (8), since epsilon was
arbitrary. No fixed separation of `2^A/3^M` from 1 has been assumed.

For the two fixed blocks, `A=a*k+b*ell` is comparable to N=k+ell.
Equation (8) therefore reads `log D_w=A*log2-o(N)` on the entire
positive domain. Combining this with `log g=o(N)` proves (2), and (3)
follows because `A>=min(a,b)*N`.

A polynomial relative-gap estimate is unnecessary for this argument:
(8) already suffices. Making only the power-gap bound effective would
not by itself provide an effective threshold for the gcd estimate.

## 6. Exact controls, interpretation and remaining task

**Expanding-block example.** Take `u=(1)`, `v=(2)`. Then
`(C_u,D_u)=(1,-1)`, `(C_v,D_v)=(1,1)`, and K=-2. At `(k,ell)=(2,3)`,

```
w=(1,1,2,2,2), A=8, M=5,
D_w=256-243=13, C_w=283, d_w=13,
G_u(2)=5, G_v(3)=37.
```

This checks the signs and the full positive domain in a case excluded by
the unnecessary requirement D_u,D_v>0. It is an exact illustration;
it does not verify the imported asymptotic theorem by computation.

**Necessary control for equal slopes.** The words `(1,1,3)` and `(1,2,2)`
have equal length and sum, but different C. At k=ell the common geometric
sum divides C_w and D_w and grows exponentially. Thus (1) is false
without the unequal-slope hypothesis. That case requires the separate
elementary analysis, not an application of (CZ-A) to dependent pairs.

**Known-cycle control.** Choosing u and v as powers of the same actual
rational cycle gives K=0 and equal slopes; its denominator is preserved.
For example powers of `(2)` retain denominator 1, and powers of `(1,2,2)`
retain denominator 5. The unequal-slope theorem excludes neither control.

| Required field | Outcome |
| --- | --- |
| Objects | Exact reduced denominators of positive rational cycles `u^k v^ell`, for each fixed pair of positive valuation words with unequal slopes. |
| Structural gain | Cancellation is subexponential; reduced denominators retain the full leading exponential size of `2^(a*k+b*ell)`, uniformly on the positive domain. |
| Translated unresolved gap | No effective threshold is supplied, and the block pair cannot vary with the exponents under this theorem. Arbitrary word families are still unclassified. |
| Worked example | `(1)^2(2)^3` has an expanding first block, positive D=13 and reduced denominator 13. |
| Known-cycle controls | Common-word powers have equal slopes and K=0; actual denominator-1 and denominator-5 cycles remain allowed. Equal-slope noncommuting blocks can have exponential cancellation. |
| Cheapest meaningful next test | Independently check the two local-place tables and the three cases disposing of exceptional translates; compare the result with the proportional-slope proof before stating a complete fixed-pair theorem. |
| Intermediate milestone | For every fixed unequal-slope block pair, a written finite-occurrence theorem for every bounded denominator layer. This is a strict word-family restriction, not a reformulation of Collatz. |

**Source and review boundary.** The exact statements and relevant proofs in
the primary preprint were read. The applications, local valuations, sign
checks, and exception removal above are this lane's derivation. No numerical
cutoff, exhaustive family enumeration, independent formal replay, or novelty
claim is asserted.
