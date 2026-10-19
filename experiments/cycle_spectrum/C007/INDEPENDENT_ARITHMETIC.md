# C007 independent arithmetic probe — height versus reduced denominator

**Status:** the proposed all-period bound `B<=q-1` for primitive positive
ordered numerator cycles remains **open**. This probe gives two exact
obstructions to shortcuts. It neither proves nor refutes the bound on its
declared integer domain. The raw odd-only clock and reduced denominator
conventions are those of [C006](../C006/ORDER_RIGIDITY.md).

## A height comparison that does not close

Let `n_0=L`, `h_0=0`, and let `n_i` be any cycle state at positive
height `h`. Under circular normalized order, `z_i=n_i/2^h>L` and
strictly increasing scaled images require `F_i>F_0`. Clearing the
height denominator gives the exact necessary inequality

```
3(n_i-2^h L)>q(2^h-1),
z_i>L+(q/3)(1-2^(-h)).                         (A1)
```

The integer gap `n_i-2^h L` is positive and odd. For `h=B`, (A1)
places the maximum-band point above `L+q(1-2^(-B))/3`. It does **not**
bound `B`: when `q<=L`, that lower threshold is below `4L/3`, while
the allowed normalized interval continues to `2L`. Thus the direct
minimum-to-height-`B` order comparison has room at every `B`.
The known ordered `q=13` cycle with numerators
`(227,347,527,797,601)` additionally shows that replacing (A1) by
“some pair has primitive odd normalized gap at most `q`” is false:
its least such gap is 15, exceeding 13.

## Geometry alone loses the integer obstruction

Take the actual primitive ordered `q=5` numerator cycle from
[C005](../C005/ORDER_THEORY.md), with numerators

```
(347,523,787,1183,1777,667,1003,1507,2263,3397,
 2549,1913,359,541,407,613,461).
```

It has positive exact raw valuations, strictly increasing sorted
scaled images, `q<=L=347`, and maximum dyadic height `B=3`.
Divide every state by 5. The rational states `x_i=n_i/5` satisfy
`3x_i+1=2^a_i x_(i+1)` with the **same** positive valuation word,
dyadic heights, successor rank order, and `B=3`. Their minimum is
`347/5>1`. Thus all real circle inequalities, correct geometric
height labels, and positive exponents coexist with additive term 1
and `B>0`.

This is **not** a counterexample to `B<=q-1`: the rational cycle's
reduced denominator is 5. The rescaled points are not odd integers,
and their cleared circular gaps need not be integers (the first is
`96/5`). In C006's notation the exact missing conditions are
`G_j=2^B Delta_j in Z_(>0)` for reduced numerator coordinates and
the full weighted denominator test

```
D L=q C_h,     q=D/gcd(C_h,D)
```

Any proof using only normalized order, the height coboundary and real
positivity would also apply to this rational rescaling and therefore
cannot establish the proposed bound. It must use integer lattice or
full-divisibility information that distinguishes reduced `q=1`
from reduced `q=5`.

## Why the current arithmetic does not settle the proposal

The [C006 sparse-forcing law](../C006/ORDER_RIGIDITY.md) gives
`q>(D/C_c)2^(ceil(m/J)-1-B)` and, after an imported two-logarithm
bound, effective finiteness when `q,J` are fixed. As `J` is allowed
to grow with the period, these statements do not put an upper bound
on `B` at fixed `q`. The target `B<=q-1` needs a new link between
height growth and the *full* cancellation in `D/gcd(C_h,D)`.

Even the one-defect case retains that link. With one chronological
height `h_t=1` and all others zero, legality requires
`c_(t-1)=2`, and the exact intercept is
`C_h=C_c-M_t/2`. Reduced denominator 1 would require
`D | C_c-M_t/2`. The actual ordered `q=233` one-defect cycle has
`C_c=14501`, `M_t/2=1152`, `C_h=13349`, and
`gcd(C_h,D)=7` for `D=1631`; hence a legal defect can create genuine
cancellation, though it does not cancel all of `D`. No all-period
exclusion follows from mechanical `gcd(C_c,D)=1` alone.

The `q=5` ordered period-17 control has `B=3<=q-1`, and the
`q=233` ordered defect has `B=1<=q-1`. The `q=1909` mechanical-word
cycle is not ordered, so it cannot validate a bound whose premise is
order. The `q=13` gap control above rules out a proposed small-gap
shortcut. All controls retain their actual denominators and domains.

**Decision:** retain `B<=q-1` as a candidate, not a theorem. The
meaningful all-period milestone is still exclusion of nontrivial
ordered cycles at reduced denominator 1. A useful next proof must
couple legal odd numerator heights and adjacent-rank inequalities to
the exact congruence `D | C_h`; another bound on real normalized
positions or on `J` at fixed height does not supply that bridge.

## Independent review of the C007 main note

I reviewed [HEIGHT_DENOMINATOR.md](HEIGHT_DENOMINATOR.md) after its
modular lemma was added. The lemma is correct on its stated `q>1`
domain: odd numerators and `q` coprime to 3 make each numerator a
unit modulo 6; a prime dividing both `q` and any numerator propagates
around the whole cycle, contradicting the separately stated
`gcd(n_0,...,n_(m-1))=1`. Reducing the normalized arrow modulo `q`
then gives `z_i≡L3^i2^(-P_i)`, with powers of 2 invertible. I
independently replayed the listed ordered `q=5` period-17 raw arrows,
its `B=3`, rank shift 10, and all four height-residue sets; they
match the note. Equation (3) matches (A1) above.

The scope of “normalization erases heights modulo `q`” is important:
it concerns residues for a **fixed normalized word** `c`. It does
not erase heights from integer order inequalities or from `C_h` and
does not rule out a proof combining those conditions. The note makes
that distinction and does not claim the candidate is false. Its
period-primitivity and reduced-numerator conditions are also logically
separate: the denominator equality `q=D/gcd(C_h,D)` uses the latter,
not primitive period alone. The opening display supplies the needed
numerator gcd condition, so no mathematical correction is required;
the phrase “primitive numerator realization” in Section 1 could be
read more clearly as “reduced numerator realization.”
