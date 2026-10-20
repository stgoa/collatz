# Integer realization of every mixed exit18 return word

**Status: written whole-class prefix theorem, exact conditional-current
constructor, and bounded replay.** Every finite sequence of the existing
exit18 re-entries has infinitely many positive integer realizations. Every
eventually periodic infinite return itinerary has a negative rational
starting point, so a hypothetical positive integer that survives forever
must have an aperiodic itinerary. This does **not** exclude such an integer,
prove termination of the return system, or supply its larger requested pair.

The inputs are the proved [R67 growing comparison](../mixed_rank_recursion/MIXED_GROWING_BLOCK.md)
and [R70 exit and re-entry interface](../mixed_exit/MIXED_EXIT_REENTRY.md).
No external theorem or empirical feed assertion is used. The optional feed
was read at `7150f312e0b9bd1099fb617ee680acb22cf1187e`; its corrected transfer
scope agrees with the distinction here. The [R71 denominator result](../lattice_cycles/BALANCED_DENOMINATORS.md)
concerns periodic cycle closure. Its integrality obstruction cannot simply
be applied to a finite prefix without the closure equation.

**Literature context, not a proof premise.** Bernstein and Lagarias,
[*The 3x+1 Conjugacy Map*, Canadian Journal of Mathematics 48(6), 1996](https://doi.org/10.4153/CJM-1996-060-x),
describe a full 2-adic shift conjugacy for the shortcut clock. The coding
argument below is an explicit scoped instance for these two returns, with
their guards, signed currents and separate odd/quotient clocks. No novelty
is claimed for 2-adic itinerary coding or finite-prefix realization.

## 1. Two disjoint returns to the same guard

Use the positive pair indices and constants

```
A=531441=3^12, M=2^19, B=311195, D=A−M=7153,
G={w>0 : w=40529845 mod2^26}, b=40529845,
V(w)=(Aw+B)/M,
P=A^2, C=B(A+M), L=M^2/2=2^37,
R(w)=(Pw+C)/L=2V^2(w).
```

Here `R` denotes this re-entry map, not the older root-collapse operator.
Every `w` in `G` is in W5, has canonical `3w`, and has `rho(w)=3w`.
The ordinary and quotient clocks retain the meanings in R67 and R70.

Consider **returns to G**, rather than the unconditioned affine maps.
Their complete positive domains are

| Symbol | Domain | Target | Consumed precision | Quotient steps | Ordinary common-tail clocks |
|---|---|---|---:|---:|---|
| V | `w=2218391138229 mod2^45` | `V(w) in G` | 19 | 12 | (13,1) |
| R | `w=8515171531530858421 mod2^63` | `R(w) in G` | 37 | 24 | (30,6) |

For either row, solving `a w+c=2^e b mod2^(e+26)` gives the displayed
single residue, since `a` is odd. That residue reduces to `b mod2^26`.
Thus these are necessary and sufficient return domains, including every
intermediate integrality and valuation condition already proved in R67/R70.

They are disjoint for a structural reason. Put `Y(w)=Dw+B`. Then

```
Y(V(w))=(A/M)Y(w),
Y(R(w))+B=(P/L)Y(w).                                  (1)
```

A V return requires `v2(Y(w))>=45`. An R return has
`v2(Y(w))=37` exactly, because its target has `2^26|Y(R(w))` and `B` is odd.
Both return maps strictly increase every positive input in their domains.
Their real affine slopes are greater than1 and their offsets are positive.

### This exhausts the existing exit18 re-entries

The R70 return with maximal old-guard count `m>=1` is precisely

```
V^(m−1) followed by R.                                (2)
```

Indeed the first `m−1` V arrows remain in G. At the next parent the exact
Y-order is37, so there is exactly one old R67 block left; its exit order
is18. The additional R70 continuation returns to G. Conversely every R70
exit18 re-entry has this decomposition. Its affine map is `2V^(m+1)`,
exactly R70's general formula. This covers every maximal depth m, but does
not claim that other exit valuations return or that this subsystem exhausts
all available Collatz comparisons.

## 2. Every finite mixed word has a complete integer cylinder

Let `omega` be any nonempty finite word over `{V,R}`. Set

```
e=19 #V +37 #R, ell=12 #V +24 #R, a=3^ell,
F_omega(w)=(a w+c)/2^e.
```

The positive odd offset c is computed in chronological order, starting
with `(a,c,e)=(1,0,0)` and appending a row `(alpha,beta,f)` by

```
(a,c,e) -> (alpha a, alpha c+beta 2^e, e+f).            (3)
```

**Complete-cylinder theorem.** An integer `w>0` follows all symbols in
omega, with every listed intermediate state and its terminal state in G,
if and only if

```
w = r_omega mod2^(26+e),
r_omega=(2^e b−c)a^(-1) mod2^(26+e).                  (4)
```

The least residue is positive and odd. Every member
`r_omega+j2^(26+e)`, `j>=0`, is a positive integer realization. All its
successive states strictly increase.

**Proof.** Following a legal word gives the terminal congruence in(4), so
necessity is immediate. Conversely the terminal congruence makes the full
affine output an integer in G. For every earlier prefix, its numerator
multiplied by the odd suffix multiplier differs from the full numerator by
a multiple of that prefix's denominator. Thus the full divisibility implies
every intermediate denominator divides its numerator. All intermediate
states are integers. Starting at the terminal G state and working backwards,
the single-return calculation in §1 puts each predecessor in the appropriate
complete return domain, hence in G. Positivity follows instead in the forward
direction from the positive initial value and both positive affine maps.
The start is in G and therefore odd and nonzero. ∎

Equivalently, pulling a cylinder of precision p back through V or R produces
one cylinder of precision `p+19` or `p+37`, respectively. The extra precision
already contains every exact valuation bit; this theorem does not replace
an exact valuation cylinder by the insufficient modulus `2^sum(a_i)`.

For any positive odd integer h and any residue t, CRT appends `w=t mod h`
to(4), giving a complete positive progression of period `h2^(26+e)`.
No condition on an initial odd modulus, by itself, eliminates any finite
word. Conditions on later states are induced by the same formulas and must
not be assumed independent.

In particular every prescribed finite list `m1,...,mk` of positive maximal
old counts occurs: apply(4) to
`V^(m1−1) R ... V^(mk−1) R`.

## 3. Full signed currents and both clocks

Write the fixed formal absorption plan as

```
[x]=div J_x + sum_v A_x(v) P(v),  P(v)=[3v]−[v].
```

These are identities with supplied pair-current premises; they do not
assert that `x` has been absorbed. Let `w0,...,wk` be the state sequence of
a legal word. Summing the existing complete R67/R70 comparisons gives

```
K_omega = D_(3w0,3wk)+J_wk−J_w0,
c_omega = {wk:+1}+A_wk−A_w0,
div K_omega = P(w0)−sum_v c_omega(v)P(v).              (5)
```

Every source multiplicity and sign is retained. All intermediate J terms
and their request vectors cancel exactly. This identity comes from actual
comparison rows, not just the affine endpoint equation.

The leading coefficient is+1. Every other nonzero request has
`rho(v)<3w_(k−1)<3wk`, using the existing single-return helper bound on the
last edge and the monotone heights. For k=1 the first strict bound reads
`rho(v)<3w0`; for longer words those helpers can exceed the **original**
rank `3w0`. In every case the leading request has `3wk>3w0` and remains
unresolved. Expanding only nonleading requests by strict-rho plans cannot
cancel it. Another representation or comparison at wk is not excluded.

The quotient clock is exactly ell. The ordinary common-tail clocks are

```
(ell+1,1) if omega ends in V,
(ell+6,6) if omega ends in R.                         (6)
```

To check composition, each local comparison is the ordinary path of length
`ell_i+c_i` from `3w_i` minus the length-`c_i` path from `3w_(i+1)`, with
`c_i` equal to1 or6. Every subsequent macro has at least12 quotient steps.
Those common tails therefore compose: its remaining ordinary prefix is long
enough to pass each preceding bridge. Equivalently, cancel the negative
length-`c_i` prefix against the next local path, then continue from their
equal states. The result is exactly the path of length `ell+c_last` from
`3w0` minus the path of length `c_last` from `3wk`. This proves both the
current identity and the clocks. No clock is assigned to the extra formal
absorption terms in(5).

## 4. Periodic closure and the remaining aperiodic question

Every infinite symbolic word has nested cylinders(4), with precision tending
to infinity. Consequently it determines exactly one odd 2-adic integer.
Every finite prefix still has arbitrarily large positive integer lifts.
The disjoint return domains make this coding injective.

For a nonempty finite cycle word, `a>2^e` and `c>0`. Its unique fixed point is

```
x_cycle=−c/(a−2^e)<0.                                (7)
```

Its denominator after reduction is odd. Nested cylinders for repeated
copies show that it is exactly the 2-adic point of that periodic itinerary.
For an eventually periodic word with preceding affine prefix
`(a0 w+c0)/2^e0`, its unique starting point is

```
x_start=(2^e0 x_cycle−c0)/a0 <0.                      (8)
```

Thus **no positive integer can have an eventually periodic infinite
itinerary in this return system**. This is a sign obstruction after imposing
cycle closure; it is not a proof that every itinerary is eventually periodic.
Any positive infinite survivor would have a genuinely aperiodic word and
strictly growing states. No such survivor is constructed here, and no claim
that none exists is proved.

The distinction is exact: for each finite word there is a different complete
positive progression, whereas one positive integer satisfying all prefixes
would have to equal the single 2-adic limit. Inferring the latter from the
former, or excluding it merely by testing periodic words, is invalid.

## 5. Exact prefix density, with a uniform counting error

Distinct words of the same symbol length m have disjoint cylinders: at
their first differing symbol the return domains are disjoint, and each
preceding affine map is injective. Let E_m be the positive integers making
at least m returns in this subsystem, define E_0=G, and put

```
s=2^(-19)+2^(-37)=262145/137438953472.
```

There are `2^m` cylinders, each with density `2^(-26-e)`. Therefore

```
density(E_m)=2^(-26) s^m,
| #(E_m intersect[1,X]) − X 2^(-26) s^m | < 2^m.       (9)
```

The first identity is an exact natural density for each **fixed** m. The
second is a uniform real-X counting bound from one interval-floor error
per cylinder. This is not an independence hypothesis.

The possible infinite-positive-survivor set is contained in every E_m, so
it has natural density zero. More quantitatively, for `X>=2^26`, write
`alpha=log(2)/log(2/s)`. Choosing
`m=ceil(log_(2/s)(X/2^26))` in(9) gives

```
#(possible infinite survivors intersect[1,X])
    <= 3 (X/2^26)^alpha.                              (10)
```

Indeed the two terms on the right of the counting bound are at most
`(X/2^26)^alpha` and `2(X/2^26)^alpha`. This sparsity bound permits a
nonempty exceptional set. It does not prove termination on any untested
integer and does not justify a probabilistic assertion about a fixed orbit.

## 6. What the theorem changes

The entire existing exit18 re-entry class supports arbitrary finite mixed
return words on the ordinary positive integer lattice. Exact finite-word
integrality, even with an additional starting congruence at any odd modulus,
cannot exclude those words. Periodic closure does exclude their positive
periodic points, but leaves a precise aperiodic survivor question.

A termination argument for this class must add a constraint on the **same
integer across unbounded prefixes**, a well-founded state that survives both
return branches, or a different signed-current construction. Neither this
statement nor R71 implies that such a constraint is unavailable. No new
accepted family is added to the seventeen-rule dispatcher.

## 7. Executable interface and bounded verification

`integer_prefix.py` supplies `cylinder`, `family`, `odd_lift`,
`maximal_counts`, `rational_point`, the complete signed `plan`, and a capped
trace. `compile_plan` requires every pair current, including the larger
leading one; an empty supply is rejected. A trace cap is unresolved, and
leaving this return system is not asserted to be Syracuse descent.

Run `python3 experiments/residual_progress/integer_prefix/check_integer_prefix.py`.
The adjacent receipt records exact ranges, source hashes, full signed
examples, and checks of the ordinary and quotient clocks. The default test
replays the saved receipt; `--write-receipt` refreshes it. Mathematical
quantifiers rest on the proofs above, not the bounded examples.
