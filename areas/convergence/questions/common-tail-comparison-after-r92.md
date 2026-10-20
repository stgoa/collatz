# A possible common-tail comparison after R92

**Research template only, 2026-10-18. Outside the verified R92 certificate.**
This note records a possible next target and its missing obligations. No new
search, closed recursion, current construction or accepted result is claimed.
See [R92](DEEPER_WINDOW.md) for the completed theorem and
[R90](../phi_exit_control/PHI_EXIT_CONTROL.md) for the exit interface.

**Subsequent scope result:** the [prescribed-child theorem](../child_history_scope/CHILD_HISTORY_SCOPE.md)
now excludes a uniform bound on both ordinary clocks for this exact child,
in every ternary digit and with any prescribed initial growth count. It
also excludes finite word catalogues with finite binary refinements. The
conditional identity below remains valid; unbounded histories and different
children remain available. The [two-source interface](../two_source_history/TWO_SOURCE_HISTORY.md)
separately retains both actual original paths and classifies the lower
path's first departure. Neither result supplies the missing merger.

## Verified starting constraints

Write the original coupled cell as

    Q(ell)=Q0+QP*ell,
    Q0=70506316836123, QP=3*2^45,
    b(ell)=Q(ell)/3, ell>=0.

R90 supplies complete maximal Phi exit words. On a fresh ordinary prefix
from Q to y, the exact native pair plan is

    P(b)=div(prefix(Q,L)+J_y-J_b)+(A_y-A_b).P.

Every request in A_b is below the original Q, whereas A_y is nonnegative.
Therefore all high requests in this displayed fresh plan are positive.
Retaining another native lower expression by itself does not produce an
opposite high coefficient. This scopes that representation, not arbitrary
actual histories or arbitrary signed currents.

R92 proves that at the repeated target n_r, all canonical origins p<=Q
through12r+19 quotient steps reduce to the known self-history Q at12r+18.
A longer history or a genuinely later common target is therefore necessary
for this family if a new smaller-origin history is to be used.

## The first new ternary decision is explicit

At the R92 precision boundary each candidate affine target is

    x(ell)=x0+2^(m+18)*3^14*ell, m in8..14.

After fourteen inverse suffix arrows of total cost E, write the resulting
affine state as

    z(ell)=z0+K*ell, K=2^(m+18+E).

Here z0 is the new intercept after those fourteen arrows, not x0.

All first fourteen inverse branch decisions are independent of ell. At the
**fifteenth** decision the source parameter modulo3 matters for the first
time. Write ell=c+3j, c in{0,1,2}. Any legal inverse branch
(2^e*z+d)/3 then gives exactly

    y(j)=[2^e*(z0+K*c)+d]/3+2^e*K*j,
    Q(c+3j)=Q0+QP*c+3*QP*j.                             (1)

The branch's residue condition makes the displayed intercept integral.
Equation(1) preserves the full intercept and original source threshold.
It is a useful arithmetic interface for an adaptive search; it does not
assert that y(j) is below Q, or belongs to any already closed family.
The binary guard does not remove any of the three possible ternary digits,
because its modulus is a power of two.

## A concrete missing common-tail lemma

A potential complete mechanism would choose a later common target of the
original source and a **smaller original-cell source**, rather than require
the intermediate target itself to become small.

For ell>0 let j=floor(ell/3). Then j<ell and Q(j)<Q(ell). Suppose one could
construct finite ordinary clocks a(ell),c(ell) satisfying

    S^a(ell)(Q(ell))=S^c(ell)(Q(j)).                     (2)

The clocks may grow with the binary return count and the parameter. They
must describe actual finite arrows, including every valuation bit. R92
neither supplies nor rules out this later-target relation.

Let K be the difference of the two path currents in (2). Then

    div K=[Q(ell)]-[Q(j)],

and the exact pair identity is

    P(b(ell))
      =div(K+J_b(j)-J_b(ell))
        +P(b(j))+(A_b(j)-A_b(ell)).P.                   (3)

The recursive child has coefficient+1. All helper ranks are at most
b(j) or b(ell), hence strictly below the ORIGINAL Q(ell). The child rank is
Q(j), also strictly smaller. This would be a legitimate whole-cell strict
comparison if (2) were established for every ell>0.

Equation(3) is only a conditional comparison. It becomes an actual finite
current after the child and every signed helper input are supplied. The
ell=0 pair is a separate base obligation; no stored actual current for it
has been identified or assumed in this scratch work. Iterating j=floor(ell/3)
terminates on the cell parameter, but does not automatically supply the
helper pairs outside this cell.

Several smaller-cell children could replace the single child in (3), with
all coefficients retained. That more general version would still need a
complete identity, strict original-rank checks, and supplied terminal inputs.

## Why one fixed pair of words cannot implement the ternary subdivision

The following written observation was checked separately during the full
verification run. It scopes the proposed next search; it is outside the
frozen R92 certificate and does not supply the missing comparison.

Fix s>=1 and 0<=c<3^s. There cannot be one fixed pair of ordinary exact
valuation words that gives a common target for

    q(j)=Q(c+3^s*j), p(j)=Q(j), for every j>=0.

Indeed, let the two lengths be a,b and their valuation sums be A,B.
Equality of affine slopes requires

    3^(a+s)*2^B = 3^b*2^A,

so A=B and b=a+s. A complete exact word of total valuation A occupies one
residue class modulo2^(A+1), including the extra bit; see the
[fixed-word cylinder theorem](../history_lifting/HISTORY_LIFTING.md).
Both source progressions have steps of exact binary order45. Legality for
every j therefore forces A=B<=44.

The two sources q(0),p(0) are congruent modulo2^45. Consequently the
child's first a valuations equal the parent's, and already sum to A.
Its additional s positive valuations then force B>A, a contradiction.
The same argument includes a=0.

Thus a pure ternary subdivision cannot be closed by assigning one fixed
pair of valuation words to each entire branch. The subsequent R94 theorem
also excludes whole-domain completion by uniformly bounded clocks,
including finite binary refinements. Input-dependent unbounded clocks,
different child families and general signed identities remain available.

## An inverse upper cycle does not give an integer original-source child

The subsequent two-source work suggests another tempting candidate: shrink
the original source by reversing its upper cycle around the same rational
center. This particular proposal fails an exact integrality test, before
any current or termination question. The following algebraic observation
is outside the frozen R92 certificate.

Write

    q*=-515908491727/(7153*3^13), gamma=3^12/2^19,
    p=q*+gamma^s*(q-q*),   s a nonzero integer.

For EVERY integer q, p is nonintegral. Indeed v3(q*)=-13. If s>0,
v3((1-gamma^s)q*)=-13 while v3(gamma^s*q)>=12s. If s<0, the
two orders are respectively12s-13 and at least12s. The smaller order
cannot cancel in either case, so p has a negative ternary order. The
case q=0 is immediate from the nonzero constant term.

Thus integer integrality of the v- or z-coordinate return must not be
transferred to a child in the original Q-coordinate. Reversing its growth
factor does not automatically define a smaller integer source. Different
affine centers and genuine word-pair comparisons remain available; their
complete divisibility and exact binary cylinders must be checked using
the [merger-cell formulas](../history_lifting/HISTORY_LIFTING.md).

## Honest status and the next useful test

No identity (2) has been found for all three ternary branches. Equation(1)
does not map its output back into the original coupled family, so there is
currently no closed recursion. Introducing a smaller parameter without that
arithmetic closure would merely rename the missing proof.

The next useful task is to seek a variable-word merger that closes one
complete parameter partition under (3), or prove that a proposed partition
cannot close. A bounded success catalogue without closure would not settle
the task. Any state machine must keep the original Q, the signed helpers,
binary guards and affine intercepts; a countdown for one Phi run cannot
serve as progress across all exits.

This note proposes an exact target lemma and records where fresh ternary
information becomes available. It asserts no new theorem of coverage,
absorption, actual terminal supply, or Collatz convergence.
