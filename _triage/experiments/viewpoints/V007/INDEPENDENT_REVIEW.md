# V007 — Independent review of the singleton-exit theorem

**Result: PASS as a written elementary argument.** Reviewed the actual
source [separator.md](separator.md), Sections 1–5, including all returns
to the finite interior. This is a mathematical source audit, not formal
verification or a novelty assessment. The full quantitative target is
still open.

**Dependency clarification added in V008:** the generic separator proof
is elementary under its stated infinitude hypothesis. The Collatz
application establishes that hypothesis using V005/V004 and inherits
their published Cobham input. This source review did not formally replay it.

## Hypotheses and reverse closure

The vertices must be entire sequences with the five exact section
transitions. All six radix relations and the zero-output convention are
retained. The theorem explicitly requires infinite pure binary and pure
ternary kernels at every reachable vertex. This hypothesis is stronger
than infinitude of the joint graph.

The reverse-closure calculation in Section 1.1 agrees with the independent
parity table in [affine_growth.md](affine_growth.md#3-independent-audit-reverse-closure-gives-two-base-infinitude).
For m=3^a and v=mi+r, writing v=2w or 2w+1 gives 0<=w<m;
the four displayed offsets stay within their claimed ternary moduli.
The affine extraction and interleaving arguments supply the claimed
ternary-automatic-cylinder consequence. V004's positive-section closure
then supplies the theorem's infinitude hypothesis for a hypothetical
nonconstant Collatz invariant.

## Step-by-step separator audit

1. **Boundary polynomial — PASS.** Each exponent from 0 through 5 has
   exactly one representation 2j+i and one representation 3l+k in the
   stated digit ranges. An intermediate vertex in U cannot leave V on
   the next step. Thus the coefficient equality records precisely the
   common two-step vertex lying outside V, without lost multiplicities.
   The polynomials A and B are nonzero because closing either radix on
   V would contradict the infinitude hypothesis. X and Y are both
   nonzero by their product identity.

2. **Unique escaping binary digit — PASS.** If A=1+z, a monomial X
   contradicts parity. For X=1+z, comparison after cancellation gives
   y0=y1=y2=1 and B=1+z+z². The six actual vertex identities then
   identify all five children of q with one vertex p. The identity
   p(m)=p(floor(2m/3)) decreases every positive argument, so p and q
   are constant. This correctly rules out the two-escape case.
   With the remaining unique binary escape, each marked ternary escape
   is identified with the same actual target p by a radix identity.

3. **Propagation and tail digits — PASS.** Every newly produced vertex
   lies outside the preceding finite set, so all q_n are distinct.
   At q_(n−1), a two-step path outside V_n must first reach q_n;
   this justifies the residue-set equation exactly. Cardinality and
   parity force each D_n to be a singleton: the only competing common
   size is two with D_n={0,2}, whose widths disagree. For
   t_n=d_n−c_n, the recurrence is t_(n−1)=2t_n−c_n. Values −1 and
   2 force forbidden predecessor values −3 and 4. From n=2 onward
   the digits are uniformly (0,0) or uniformly (1,2).

4. **Finite T1 closure — PASS.** With N=2, every vertex already in
   V_(N−1) has all successors in V_N, and T1 at q_N is nonescaping.
   Thus V_N is T1-closed. The nonescaping binary child A_N lies in V_N.
   The respective residue-3 and residue-2 radix identities give
   A_(n+1)=T1(A_n), so these entire vertices are eventually periodic.
   This argument does not assume the other four transitions close V_N.

5. **Equality of entire sequences — PASS.** In the zero-escape case,
   m=2^v(2u+1)>0 gives q_n(m)=A_(n+v)(u); equality at m=0 follows
   separately from the common zero output along E0. In the maximal
   escape case, v=v2(m+1) gives
   m=2^(v+1)u+2^v−1 and the same evaluation formula. Its final zero
   digit is legitimate even for m=0 and for an all-one binary word,
   because E0 preserves output at zero. Eventual periodicity of A_n
   therefore gives q_(n+p)(m)=q_n(m) for every m>=0, with one fixed
   p and all n sufficiently large. This contradicts distinct whole
   vertices; it is not merely agreement on finite prefixes.

## Exact scope

The theorem excludes every singleton exit from a finite forward interior,
including singleton distance layers at arbitrary depth. Nonempty layers
therefore have at least two vertices and |J_D(b)|>=2D+1 follows.
After the known depth distortion this is still a linear bound and does
not improve the generic binary bound |K_D(h)|>=D+1. Its gain is the
excluded graph structure.

No step extends the Boolean one-exit identity to multiple boundary
states. Arbitrary fixed finite separator size, and hence the requested
unbounded ratio, remain open. Generalized-map colorings with finite
kernels fail the infinitude hypothesis and are not excluded by this
theorem. No additional experiment or external theorem was required for
this audit.
