# Residual progress and finite forcing

Started 2026-10-17 from clean pushed commit `ce56699`.
The preceding goal turn made progress: universal partial currents, an exact
one-pass compression, scoped counterexamples, and their reproducible evidence
were committed and pushed. Collatz and the universal complete constructor
remain open.

## Objective and completion standard

Find a proved mechanism that resolves the remaining positive annular components.
Completion of the research goal requires a correct universal construction or
other valid proof of Collatz; a stronger reduction or finite experiment alone
does not meet that standard.

## Falsifiable directions

1. Combining root collapse with transport closes a residual class with a
   decreasing integer potential.
2. Affine tree templates extend to an actual aggregate cover, or a precise
   aggregate obstruction identifies why a fixed catalogue cannot do so.
3. The five-ray comparison admits an explicit finite forcing certificate
   with its boundary terms retained, isolating a finite constructive task.

## Checklist

- [x] Revalidate repository and previous progress.
- [x] Probe residual transport and derive its valid scope.
- [x] Test aggregate template coverage and persist a complete finite-depth obstruction.
- [x] Develop a finite constructive use of the scalar comparison.
- [x] Audit the transport and finite-cone claims independently; persist counterexamples.
- [x] Integrate verified results, run checks, and compile the current note.

## Findings

### 1. A finite compiler retains the boundary terms and uses integrality

The new [finite-cone theorem](duality/FINITE_CONE.md) converts finitely many
supplied packet certificates into an exact integer absorption current. On
grid ordinals k=5b+i the source comparison has shifts -10,+3,-2. The rational
weight `(35/27)^k` contracts strictly. A finite nonnegative inverse supplies
exact rational weights for a measure identity, retaining every source-scale
current, rounding shell, and upper/lower boundary term.

The key step is an integer-component gap: an integer source with an exact
rational current and total positive residual mass below 1 has no positive
integer component obstruction. The same finite graph therefore supplies an
integer current with nonpositive residual. For a nonnegative counting source,
all source vertices are already connected to 1.

For target m, an explicit sufficient block contains O(log m) packet cutoffs,
the largest O(m^2.14682). This bounds the inputs required by the compiler; it
does not bound their construction cost or prove that they exist universally.

The [actual demonstration](forcing/ACTUAL_COMPILER.md) supplied 30 checked
one-sided packet currents at the starting cutoffs through 5376. Twenty of
those input searches finished with sources still unlinked to 1 in their own
graphs. Exact combination produced a rational current with 6217 rows and
positive residual mass `29145292346068/46422343855805 < 1`. The compiler then
extracted a stored 95-row nonnegative integer current for U_112, using only
the already present nonzero current arrows.

**What changed:** there is now a finite constructive form of the five-ray
implication, with every boundary term retained and no global-invariance
assumption. **What remains:** the packet inputs may lie above the target
scale. Assuming them during a decreasing induction is circular. The compiler
does not supply its own universal input certificates.

### 2. Root collapse and transport have an exact normal form

The [transport note](transport/ROOT_TRANSPORT.md) proves `R^2=R` and `PR=P`,
so every word in these operators reduces to I, R, P^t, or RP^t. On roots,
RP is conjugate to ordinary killed Syracuse on odd states coprime to 3.
Interleaving the operators changes representatives and current tables; it
does not introduce a different synchronous residual dynamics.

Exactly `floor(4N/2^t)-floor(2N/2^t)` explicit top-band sources retain
coefficient +2 through t transports and collapses. This rules out a fixed
transport depth for all required annuli. At N=a*2^b the top source survives
b+2 steps at `324*a*3^b-1`, also excluding a uniform linear height bound for
this process. Historical cancellation and other arithmetic rewrites remain
possible.

**Pivot:** repeated 19/22 contraction is false, with exact N=96 norms
`3533 -> 3124`. A later reachable residual even has norm13 and positive
mass4 unchanged after one more step. A longer-block progress theorem could
still hold, but requires a new argument; a one-step claim does not.

### 3. A complete aggregate obstruction at depth 32

The [inverse exposure method](templates/AGGREGATE_EXPOSURE.md) reconstructs
an entire exposed component without enumerating the O(N) source support.
It uses exact inverse branches under proved height bounds to decide whether
an arrow is among the first D arrows from any actual source. Explicit caps
return unresolved; only a completed component supports an obstruction.

At the required cutoff `N=96*2^24=12*2^27`, the complete depth-32 component
of the top source has 35 vertices and exactly three annular sources:
`(64N-1,-2)`, `(96N-1,+2)`, `(144N-1,+2)`. Its mass is +2 and it does not
contain 1. The 9171 inverse reachability decisions exclude every extra
attachment in that entire graph. Consequently no current supported on the
depth-32 exposure graph can have a nonpositive residual for this annulus.
This also excludes an exact source cover by tree templates whose directed
source-to-anchor depths are all at most 32.

**Pivot:** a growing positive top orbit alone is not a valid aggregate
witness. At N=10368 and depth2 its complete component contains 27 sources
with total mass zero. Historical intersections attach negative coefficients
that a forward-only inspection misses. All vertices and arrows of both
examples are persisted. Independent full forward graphs match the inverse
algorithm on 48 smaller cases.

The depth-32 example is a fixed finite obstruction. No obstruction for
arbitrarily large aggregate depths is proved. A future extension would need
a parameter family with a proof excluding every additional incoming source;
the current inverse method supplies a tool to investigate that condition.

## Next obligation

Supply the finite compiler's packet inputs by a noncircular construction,
or find a different exact residual class with a proved decreasing parameter.
The current partial template families remain available. Any proposed cover
must account for the complete aggregate components, including sources that
attach at unequal times. The normal form above excludes obtaining a new
residual evolution merely by rearranging P and R.

## Verification status

Scoped checkers and the actual compiler pass. Independent model reviews
checked the root-1 absorption convention, surviving-atom count and height,
finite inverse positivity, every boundary sign, the integer gap, and the
main LaTeX transcription. Three transcription clarifications were applied:
lower grid indices, least admissible B for the cutoff bound, and explicit
general-graph scope of the fixed-point threshold counterexample.

`python3 scripts/verify_all.py --cpp` passed on 17 October 2026, including
all prior archive and certificate checks and the four new default checkers.
The existing LaTeX source compiled successfully. All 44 checked local
Markdown links resolved, and `git diff --check` passed. Commit history records
delivery of this batch; the universal research goal remains open.
