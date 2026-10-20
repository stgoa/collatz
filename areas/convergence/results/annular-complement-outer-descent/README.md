# Turning annular cancellation into a recursive complement reduction

2026-10-17. **Written conditional transfer theorem and explicit shrinking
branches.** The known absorption input is only the odd seeds at most N.
These results do not close the whole residual family or prove Collatz.
No novelty is claimed. All clocks are odd-only Syracuse with absorption at1.

## 1. Every positive annular source is already certified at the inner scale

Fix `8|M`, and set `N=64M`. Let A_M be the actual six-band annulus.
Suppose a finite exact current H for U_N is supplied. This input can itself
be extracted from the inner-interval current by R17's retained-graph theorem.

**Lemma.** Every positive atom of A_M has an explicit odd ancestor at
most N, at distance at most two. Its entire path to1 is consequently
already present in the nonzero-row graph of H.

Atoms at most N need no ancestor construction. The remaining positive
atoms in band4 lie in `(N,9N/8)` and have residues11,13,17 modulo18.
For residues11 or17, the predecessor `(2y-1)/3<N` works. For residue13,
the two-arrow chain is

```
(8y-5)/9 -> (4y-1)/3 -> y,
```

with valuations1,2, and first state below N. In band5, the only positive
residue is17 modulo18, with coefficient2. For `9N/8<y<9N/4`, use

```
(4y-5)/9 -> (2y-1)/3 -> y,
```

with valuations1,1; again the first state is below N. All displayed states
are positive odd integers, and exact valuations follow from their odd
successors. In a finite functional graph, an exact current with nonnegative
source U_N forces actual directed paths from its sources to1. Those paths
must include the displayed descendants. QED.

This lemma is stronger than a bound on the raw positive-source height:
positive annular sources up to `9N/4` are certified from ancestors below N.
It imposes no absorption assumption on the negative sources.

## 2. Transfer any capacity-checked partial annular current

Suppose a finite integer block

```
mu = P-Q = (I-Push)J,          P,Q >= 0,
```

is supplied, where P and Q use disjoint states, `P<=A_M^+`, and
`Q<=A_M^-` coefficientwise. These are the exact source-capacity hypotheses.
The symbol Push is the killed Syracuse pushforward; P here denotes the
positive source measure only.

By Section1, the graph of H supplies an exact nonnegative integral current
H_P for P. Therefore

```
Q = (I-Push)(H_P-J).                                  (1)
```

The current H_P-J may have either sign. Since its source Q is nonnegative,
its nonzero-row graph supplies actual absorption paths for every atom of Q.
Those paths can be extracted by a finite graph algorithm without exposing
new arrows.

No hypothesis excluding Collatz cycles is needed here. In every finite weak
component that does not contain1, the divergence of any finite signed current
sums to zero, including when the component has a directed cycle. Such a
component cannot carry positive Q mass. A finite functional component that
does contain1 has1 as its unique terminal state, so its vertices follow
directed paths to1. Possible unrelated components with zero Q mass are
irrelevant. This is a finite graph consequence of (1), not an assumption
about globally invariant orbit classes.

Now let R_N be the exact R17 residual. Each root x in its support is3 or7
modulo12, so

```
t=(3x+1)/2 in (3N/2,9N/4),
t=5 or11 modulo18,           A_M(t)=-1.                 (2)
```

Whenever Q(t)>0, append the already explicit cutoff arrow `x->t` to the
path certified by (1). It gives an exact nonnegative current for
`R_N(x) delta_x`. Summing over all such roots gives

```
R_N = (I-Push)T + R_remaining,                         (3)
R_remaining >= 0,
```

where the removed coefficient at each covered root is its **entire**
R_N coefficient, either1 or2. Certifying absorption of a state once allows
its path current to be multiplied by2; this does not use an annular source
coefficient twice. The annular capacity was spent once in mu, while (1)
has supplied a reusable path certificate. Source multiplicities in (3)
are retained exactly.

Thus an improved packet identity `Pi_N=div J_0-R_N` becomes

```
Pi_N = div(J_0-T)-R_remaining.                         (4)
```

Only known absorption through N, a finite arithmetic annular block at the
smaller cutoff M=N/64, and the existing cutoff arrows are inputs. This is
a constructive transfer, not an assumption that all annular blocks or all
their negative atoms are certifiable. Full closure would follow if supplied
blocks covered every exit in (2); that coverage is presently unproved.

## 3. Exact coverage of the existing combined catalogue

This transfer identifies precisely which parts of the current catalogue
help R_N. It does not infer coverage from the amount of annular mass removed.

The old five-source packing has negative top atom

```
t=13775+1152j,     j=9s or9s+3,
```

for its admissible copy indices. Its corresponding complement root is

```
x=(2t-1)/3=9183+768j.                                 (5)
```

This root is3 modulo12 and lies in `(9N/8,3N/2)`, so R_N(x)=1.
For example, for j=9s, the maximum admissible M is `120+96s`, and
`t-108M>=815`; the other class has maximum `152+96s` and gives the same
bound. The upper inequality `t<144M` is part of the existing capacity
proof. Distinct copies give distinct roots. Thus all C_old(M) copies
provide C_old(M) new outer absorption certificates.

The other old negative sources are below96M, so their valuation-one
predecessors are below N. The new short release-packing pair is below72M
and likewise adds no root. A release triple's higher negative atom is
`t=(3q+1)/2`, with `64M<q<72M` and `q=31 or103 modulo108`. Its root q
is31 modulo36 in `(N,9N/8)`, where R_N is already zero. Its other negative
atom lies below96M. Consequently the extended catalogue's coverage of
R_N is **exactly** C_old(M), rather than a quantity proportional to all
the annular mass that catalogue removes.

The previous exact floor formulas give

```
C_old(M)=M/144+O(1)=N/9216+O(1).
```

This is positive reusable coverage, but far smaller than the remaining
mass `25N/288+O(1)`. It is not a complete recursive closure.

## 4. A genuinely shrinking branch with arbitrarily large intermediate height

The general delayed-release construction provides a second transfer with
unbounded path length. Use its parameters h,r,X at annular cutoff
`M=3X/128`, and put `N=64M=3X/2`. The notation in
`../release/DELAYED_RELEASE.md` gives

```
v -> ... -> y_1=N-1       with valuation word 1^r,2^h,3,
t=(2v-1)/3 -> v           with valuation1.
```

Its proved band inequalities give

```
9N/8 < t < 3N/2,        t=31 modulo36,        R_N(t)=1.
```

Therefore this is an actual unresolved R17 root, not a root already
absorbed by the earlier arithmetic profile. It has the explicit first
descent

```
t -> ... -> N-1,         word 1^(r+1),2^h,3.            (6)
```

All intermediate states after t are greater than N. This follows from
the delayed-release proof: v exceeds108M, all later intermediate states
exceed144M, and the endpoint is64M-1. Hence (6) reaches the known interval
for the first time after exactly `h+r+2<=2h+2` arrows. Appending the
supplied path from N-1 to1 gives an exact current for delta_t. Its unknown
seed has strictly decreased to the supplied range; no absorption above N
has been assumed.

The path reaches

```
w_h=4(4/3)^h(X-1)+1 > (4/3)^h N
```

for X>=2. Thus these shrinking branches have unbounded intermediate
height relative to N, despite their exact arithmetic construction. This
explains why a recursive scheme must permit such excursions rather than
impose a universal height ceiling. This is a statement about the specified
first-descent paths, not a universal cost bound for other current searches.

There are unbounded qualifying h, and infinitely many valid X for each.
When M is on the required ladder `96*64^k`, the complement cutoff N lies
on the next rung `96*64^(k+1)`. Thus (6) is a family of shrinking branches
on the programme's actual residual scales. The already proved parameter
congruences are reused; no claim is made for nonqualifying parameters or
for every root of R_N.

### A coefficient2 branch, checked with its full multiplicity

The other negative source u may also have a remaining root
`x=(2u-1)/3`, followed by `x->u->t->v->...->N-1`. Its R_N coefficient
can be0,1,or2, so it must be evaluated rather than assumed. For the exact
parameters

```
h=r=3, V=155, X=24315904, N=36473856,
X=46765 modulo59049, 1024 divides X,
```

the root is `x=40480795`, and R_N(x)=2. Its ten-arrow first descent is

```
40480795 -> 60721193 -> 45540895 -> 68311343 -> 102467015
 -> 153700523 -> 230550785 -> 172913089 -> 129684817
 -> 97263613 -> 36473855.
```

Putting current2 on each of the ten arrow origins gives divergence
`2delta_40480795-2delta_36473855`, exactly. The endpoint is N-1 and every
earlier state exceeds N. The receipt stores the full current. This removes
two actual residual units using a certified path; it does not duplicate
the single annular coefficient at u.

## 5. What a complete recursion must still supply

The transfer separates three tasks that were previously easy to conflate:

1. Prove a current identity for an actual annular submeasure, with capacity.
2. Determine whether its negative atoms cover the **exits of remaining
   complement roots**, rather than already absorbed states.
3. Supply enough such identities to cover every remaining root, or give
   another explicit shrinking branch for it.

The first two now have an executable exact interface, and Section4 supplies
an infinite collection of nontrivial branches for the third. Universal
coverage, or a proved decreasing parameter for the unhandled roots, remains
open. Ordinary finite successful searches are not a termination proof.

## 6. Reproduction

```
python3 experiments/residual_progress/complement_recursion/check_transfer.py
```

The default checker is read-only. It checks the positive-source ancestor
formulas and exact catalogue coverage at finite M, constructs actual currents
using capped supplied lower-range absorption, and verifies symbolic delayed
branches without enumerating their enormous cutoff intervals. The adjacent
receipt records the ranges and hashes. `--write-receipt` intentionally
regenerates it.

The persisted audit checks all M=8,16,...,512, plus768 and6144: 353280
positive annular atoms, including125663 above the supplied lower cutoff,
and164 exactly matched catalogue roots. Five actual transfers use
M=8,96,168,384,768; the M=96 example stores a61-row current for delta9183
and checks the full packet update at N=6144. There are170 symbolic shrinking
branches for qualifying2<=h<=32 and both congruence choices, including
the full coefficient2 example above. The default checker takes about3 seconds
in the development environment; no runtime bound is part of the theorem.
