# C012 — What a uniform rotation bound must retain

**Status: written elementary obstructions, exact finite controls; the
proposed uniform denominator bound remains open.** No new integer cycle
class is excluded. The full cycle goal remains active; divergence is
separate. Use the raw positive odd-only clock without absorption at1.

## Recommendation in response to the user's question

Aim for a structural restriction on **every hypothetical nontrivial
integer cycle**, uniform in period and height. The concrete intermediate
target is a growing lower bound on its minimum distance from a
nonidentity rotation. If w has primitive period m, define

```
rho(w)=min_(1<=r<m) #{i : a_i != a_(i+r mod m)}.
```

Seek an explicit F(m) tending to infinity such that every hypothetical
nontrivial Collatz cycle has `rho(w)>=F(m)`. A bound of order
`m/log m` would be a stronger outcome. C011 currently gives only
`rho(w)>=3`, under its stated published inputs. A succession of fixed
counts does not complete this target. High-complexity cycles would still
remain possible after such a theorem, so it is genuinely intermediate.

The next attempt must exploit how the shared arcs overlap inside the
same word. C012 rules out two specific shortcuts. It does not establish
that the proposed estimate is true or that rotation distance is the
eventual successful language. If a bounded discrimination probe cannot
retain that information, compare another mechanism instead of expanding
a fixed-count catalogue. This recommendation does not replace the
user's active all-cycle headline.

Fable's reported Lean work can strengthen verification of established
interfaces. It has not supplied the new uniform estimate; see the
[pinned side review](SIDE_REVIEW.md).

## The mechanism tested

For a word with total A and period m, put `D=2^A-3^m>0`,
`g=gcd(C_w,D)` and `q=D/g`. The candidate extension of C011 is

```
g^s * 4^m < 2^(A*s) * 3^m,
q > (1-3^m/2^A) * (4/3)^(m/s),                  (candidate)
```

where s is the nonzero mismatch count for a selected rotation. These
two forms are equivalent. At s=2 this is the established bound. At
arbitrary s it remains unproved and unrefuted in this batch.

Conditional payoff: a nontrivial integer cycle has A<2m. With natural
logarithms, the logarithm input already audited in C011 would combine
with the candidate estimate at q1 to force

```
s > log(4/3)*m / (600000000*(1+log(2m))).
```

This consequence is conditional on the candidate. It is not an achieved
lower bound. The purpose of displaying it is to make the next research
target's all-period payoff explicit.

## All cuts retain only limited free-block information

Cut just after every mismatch. Paired blocks have the same interior,
different last valuations, and exactly the same intercept c_i. With
`alpha_i=3^ell_i`, `beta_i=2^B_i` and `beta'_i=2^B'_i`, the cyclic
block matrices B,B' give the complete difference matrix

```
M=D*(B'^(-1)-B^(-1)),
|det M|=D^(s-2)*product_i |beta'_i-beta_i|.
```

Every k-minor is divisible by `D^max(k-2,0)`. When all mismatch
amplitudes are one, its Smith form over `Z[1/6]` is
`diag(1,1,D,...,D)`. Thus adjugate elimination is already vacuous for
s>=3. For unit-amplitude mismatches and g>1, the exact matrix on free
block-intercept variables retains only two independent congruences
modulo g. Actual rotation overlap
still imposes additional restrictions on those variables.

The [complete proof](COUPLED_SYSTEM.md) also supplies primitive actual
cycles with arbitrary even s, unbounded period and any prescribed
coprime-to6 divisor of g. This establishes sharpness on genuine cycles;
it does not refute a relative bound on `g/2^A`.

## Three mismatches can conceal an arbitrary background

The primitive family `(1,U,3,U,4,U)`, for U over2 and5, has minimum
rotation distance exactly3 while U can carry arbitrary information.
The stronger counting family `(3,U,4,U,5,U)` uses U with t ones and
2t twos and has positive D and A<2m for t>=3. These are specified in
[the obstruction proof](COUPLED_OBSTRUCTIONS.md).

At fixed length and total, there are exponentially many distinct legal
shared-arc intercepts, whereas expressions with a fixed number of
signed terms, fixed coefficient choices and powers of2 and3 bounded
linearly in that length have only polynomially many possibilities.
This rules out that specific compression into a fixed number of
S-unit terms. Neither arbitrary S-unit methods nor the candidate
denominator bound are refuted.

## Checks and limits of finite evidence

The [coupled checker](check_coupled_system.py) reconstructs all2,459
stored raw instances at333 parameters, the C007 addition,1,185
normalized cycles and all11 fixtures. It tests the complete block-cut
identities for every one of27,646 nonidentity rotations. Selected
determinants and minors are independently evaluated with integer
arithmetic; the universal statements rest on written proofs.

Every stored rotation passes the candidate, but every pass already
follows from its observed q and m/s. In particular all nonfixed q are
at least5 and m/s is at most5, with `(3/4)^5>1/5`. This is
**nondiscriminating evidence**, not empirical support for the missing
bound. Generated long-arc examples are also finite diagnostics.

The [shared-arc checker](check_shared_arcs.py) tests350 original
fixed-total backgrounds,3,582 backgrounds in the A<2m range, and
seven prescribed-prime sets, totaling177,288 raw arrows and173,349
rotations. It checks primitive periods,
minimum mismatch count3, recovery of words from intercepts and the
correct shared-arc formula. The exponential-versus-polynomial argument
is not inferred from those finite counts.

The initially discussed formula for `C_(k,2^n)` had an off-by-one in
the leading power of3. Root review corrected it before persistence:
`C=3^n+2^k*(4^n-3^n)`. Its residue is1, not3, in the specified
prime-avoidance construction. The conclusion survives the correction.
No historical mathematical file was changed.

See [the source audit](LITERATURE.md), [root review](ROOT_REVIEW.md),
[theory review](INDEPENDENT_THEORY_REVIEW.md), [checker review](INDEPENDENT_CHECKER_REVIEW.md)
and [exact review](EXACT_REVIEW.md) for their separate scopes. Saved
receipts and the delivery check record verification and preservation.
No novelty, independent formal verification or improved published cycle
record is claimed.
