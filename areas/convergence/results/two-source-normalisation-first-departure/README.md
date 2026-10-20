# The actual lower history and a complete two-source exit interface

**Status: written arithmetic proof, exact finite rational-orbit certificate,
and unfinished comparison currents. No terminal pair current or new accepted
domain is supplied.** Ordinary steps below use the odd-only Syracuse map S,
absorbed at1. The quotient clock is not used in this package.

The [retained-history family](../retained_history/RETAINED_HISTORY.md) and
[guarded upper return](../phi_exit_control/PHI_EXIT_CONTROL.md) leave a positive
high source. This note retains the actual lower-source path instead of
immediately replacing it by its formal absorption plan. It gives a common
coordinate for both sources and completely specifies the lower path's first
departure from its forced rational itinerary. The final positive source still
needs a comparison or supplied current.

## 1. Exact normalization of both sources

For every integer ell>=0 put

    Q=70506316836123+3*2^45*ell,  b=Q/3,
    v=67839005952677+2^18*3^18*ell,
    z=471104208005+2^14*3^16*ell.

Then

    v=144z-43,
    Q=(2^31*z-665034679)/3^15,
    Y(z)=864z-257=6v+1.

The following two complete ordinary valuation words hold on the entire cell:

    from Q: (1,2,1,1,1,1,1,2,2,1,1,2,2,1,1,3,1,2),
    from b: (2,1,1,2,2,1,1,2,2,1,3,2,1,5,2,3).

Their lengths/costs are respectively18/26 and16/31, and

    S^18(Q)=Y(z),   S^16(b)=z.                         (1)

These are identities for actual integer paths. Verification at ell0 and the
exact word-cylinder modulus2^(cost+1) prove them for the whole cell: both
source periods are divisible by2^45, exceeding both required precisions.
Alternatively one may compose each displayed affine branch directly.

Let I(x,t) be the current of the first t ordinary arrows from x, so its
divergence is [x]-[S^t(x)]. With P(b)=[3b]-[b], (1) gives

    P(b)=div(I(Q,18)-I(b,16)) + [Y(z)]-[z].           (2)

No helper pair is assumed in (2). Its two-atom residual is explicit and is
not claimed to have a supplied current.

## 2. A legal coordinate for every guarded upper return

Write

    A=3^12=531441, M=2^19=524288, D=A-M=7153,
    Psi(z)=(Az-53)/M,  C(z)=Dz-53.

The earlier map Phi(v)=(Av+299947)/M obeys

    Phi(144z-43)=144Psi(z)-43,
    7153v+299947=144C(z),
    C(Psi(z))=(A/M)C(z).                             (3)

The broad upper guard is n=v2(C(z))>=14. One complete return into that guard
is equivalent to n>=33. On it Psi(z) is a positive odd integer greater than z,
and the twelve-arrow word

    (1,1,1,1,3,1,4,1,2,1,1,2)

maps Y(z) to Y(Psi(z)). Its cost is19. The word itself already holds at n>=15;
the stronger condition n>=33 is what returns to the broad guard. This
distinction preserves the exact valuation bit and the exit boundary.

For the original cell, n is finite and at least14. The exact maximum number
of guarded upper re-entries and the last upper exit order h are

    r=floor((n-14)/19),  h=18+(n-14 modulo19),
    n=19r+h-4,  18<=h<=36.                           (4)

All z_i=Psi^i(z), 0<=i<=r, are integers; only z_0 is asserted to lie in the
original ternary progression. The original upper path reaches Y(z_i) in
18+12i ordinary arrows.

Coordinate integrality supplies no lower-source path to z_i. Indeed the
exact one-return decomposition is

    [Y(z)]-[z] = div I(Y(z),12)
                  + ([Y(Psi(z))]-[Psi(z)])
                  + ([Psi(z)]-[z]).                 (5)

The final defect in (5) is a missing comparison. A direct fixed ordinary
word z->Psi(z) on an infinite arithmetic progression is impossible: every
nonempty forward word has a positive affine intercept, whereas Psi's
intercept is -53/M. This statement does not exclude variable words,
unequal-time mergers, or signed comparisons using additional sources.

## 3. A finite certificate controls every forced lower prefix

Consider the positive odd-denominator rational Syracuse orbit starting at
53/D. Its numerator map is

    N -> (3N+D)/2^v2(3N+D).                          (6)

All numerators are positive and odd; the denominator remains D. The stored
finite certificate contains448 distinct states before the first repeat:

- preperiod71, total valuation cost146;
- cycle377, total valuation cost739;
- repeated entry numerator7817;
- maximum numerator819533, hence every rational state is strictly below115.

For every prefix among these448 states, if i is its ordinary length and E_i
its total valuation cost, exact integer comparison gives

    3^i <= 2^E_i.                                   (7)

The cycle multiplier3^377/2^739 is strictly below1. Thus (7) holds for every
prefix of the infinite eventually periodic itinerary: every further cycle
multiplies the already checked slopes by this smaller factor. This extension
is a proof from a finite exact certificate, not an inference from an arbitrary
bounded orbit scan. The certificate asserts a rational cycle, not a positive
integer Collatz cycle.

Write the original integer z as

    z=(53+2^n*t)/D,   n=v2(C(z)),  t positive odd.

Along any matching prefix i, with rational numerator N_i and cost E_i,

    x_i = (3^i*2^(n-E_i)*t+N_i)/D
        = (3^i/2^E_i)*(z-53/D)+N_i/D.               (8)

Whenever E_i<n the complete valuation word is forced: its last exact bit
has not exhausted the binary precision. From (7), (8), and N_i/D<115,

    0<x_i<z+115<Q.                                  (9)

This holds for arbitrarily many rational shadow cycles when n grows; each
actual positive integer has finite n and therefore eventually leaves the
forced itinerary. No claim is made about its entire subsequent trajectory.

## 4. Complete first-departure classification and cylinders

Let i be the unique index with

    E_i<n<=E_i+e,   e=v2(3N_i+D),
    N_next=(3N_i+D)/2^e,  a=n-E_i.

All earlier arrows have exactly the shadow valuations. At the next arrow:

1. **Short branch, a<e.** The actual valuation is exactly a, and

       S(x_i)=(3^(i+1)*t+2^(e-a)*N_next)/D.

2. **Long branch, a=e.** Put

       j=v2(3^(i+1)*t+N_next)>=1.

   The actual valuation is e+j and

       S(x_i)=(3^(i+1)*t+N_next)/(D*2^j).

Both assertions follow by factoring2^a or2^e from3x_i+1. In particular this
is the first differing valuation, including the case where the shadow cost
equals n. The parser does not silently accept a word at the missing extra bit.

Every exact order n>=14 is realized on the original ell progression. In a
short branch no further binary choice is necessary. In a long branch every
j>=1 is realized, with its full exact congruence

    t = (2^j-N_next)*3^(-(i+1)) modulo2^(j+1).        (10)

The residue in (10) is odd. Combining z=(53+2^n*t)/D with the original z
progression gives one complete ell cylinder modulo2^(n+j+1-14). For short
branches the complete exact-order ell modulus is2^(n+1-14). The odd cofactor
3^16 of the z period is invertible modulo these powers of2. The construction
therefore gives every claimed cylinder, including arbitrarily large n and j;
there is no unproved existence assumption or finite search in this step.

Together with (4), this classifies the lower first departure for every upper
return count and every upper exit row. There is a finite eventual phase
description: after shadow cost146, replacing n by n+739 adds377 lower arrows
with the same local departure type; the upper exit row advances by739 modulo19.
Since gcd(739,19)=1, replacing n by n+19*739 preserves both phase labels and
adds19 shadow cycles and739 upper returns. The free long-branch valuation j
is unbounded and remains explicit. Finite phase labels alone do not prove
termination after these departures.

## 5. The first departure and eleven further arrows remain below Q

For every positive odd x and integer t>=0,

    S^t(x)+1 <= (3/2)^t*(x+1).

It also holds at the absorbing state1. Applying it to the last matching state
x_i<z+115 shows that, for every t=0,...,12,

    S^t(x_i) < (3/2)^t*(z+116)-1 < Q.                (11)

The count12 begins at x_i: it includes the first departing arrow and at most
eleven further arrows. It does not mean twelve arrows after departure.

For the last strict inequality it is enough to test t12. After multiplying
by3^15*2^12, its slope in z is

    2^43-3^27=1170495537221>0.

At the least z=471104208005 the exact positive difference is
551425372148651686473501. This proves the inequality for every positive member
of the original progression, retaining its affine intercept. Nothing after
the twelfth arrow is covered by this estimate.

Thus, for any 0<=j<=r and any0<=t<=12, the actual paths give the full signed
comparison

    P(b)=div(I(Q,18+12j)-I(b,16+i+t))
           +[Y(Psi^j(z))]-[S^t(x_i)].               (12)

The negative residual source in (12) is below the original Q. The positive
one is above Q. The code stores both sources and every signed current row.
These are unfinished comparisons, not supplied pair currents. Assuming
absorption below Q could discharge the negative source, but would still leave
the positive source's continuation unresolved.

## 6. What this does and does not complete

This is an exact normalization and a complete first-departure interface for
the retained lower source across all upper guarded return counts. It does not
supply the missing defect in (5), show a common future for the residual pair,
or prove that a later continuation decreases the original rank. The lower
path remains below Q throughout its forced shadow prefix and the stated
departure window, so that path has not yet produced a high negative frontier
that could cancel the upper residual.

The next constructive question is a comparison after this complete departure
interface, with an explicit well-founded parameter or supplied lower inputs.
Any use of an absorption or pair current beyond the actual displayed paths
must state and supply it. The negative controls and the distinction between
changing sources and one fixed source remain in force.

## Reproduction

Run from the repository root:

    python3 experiments/residual_progress/two_source_history/check_two_source_history.py

The default checker compares a stored receipt. `--write-receipt` regenerates
only that receipt inside this directory. It independently verifies the finite
rational orbit, exact integer paths and divergences, all departure branches,
complete valuation bits, and rejected invalid or capped requests. The stored
path comparisons are explicitly unfinished. No dispatcher or frozen earlier
result is modified by this package.
