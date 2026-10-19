# Phase 6 literature and transfer audit

**Status: setup reference, not a new mathematical result.** Read on 18 October
2026 against side proposal commit
`f244b7a5b77a51f8dd7e6bccf2c6d5f18932df88`. The route map is maintained under
the user's authorization for autonomous research. References are primary papers, publisher records, or
author-hosted copies. A cited published theorem has not thereby been
independently re-proved or formally verified here. No novelty claim is made.

## L1 — Terras and Everett: stopping-time calibration

The classical benchmark is that the set of positive integers having an iterate
strictly below their starting value has natural density one. Everett states
this for the shortcut map `C(2n)=n`, `C(2n+1)=3n+2` in his original
[1977 paper](https://www.sciencedirect.com/science/article/pii/0001870877900871).
Terras's [1976 paper](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/30/3/101028/a-stopping-time-problem-on-the-positive-integers)
develops the parity-vector method; its Theorem 1.2 and Corollary 1.3 identify
length-`k` parity vectors with residues modulo `2^k`. The publisher's direct
PDF was intermittently inaccessible during this audit; the primary search
index exposed these theorem statements, not a complete proof audit.

**Exact published match for S.1.**
[Korec (1994), Theorem 1, page 85](https://dml.cz/bitstream/handle/10338.dmlcz/133225/MathSlov_44-1994-1_8.pdf)
proves that, for every real `c>log_4(3)`, the set
`{n: C^j(n)<n^c for some j>=0}` has natural density one. Choose `c=4/5`:
`log_4(3)<4/5` follows from `3^5=243<256=4^4`, and
`n^(4/5)<=n/2` for `n>=32`. Restricting a density-zero exceptional set to
odd integers still gives relative density zero. If the shortcut endpoint
is even, continuing its divisions by 2 reaches an odd endpoint no larger.
Thus the fixed-half odd-only statement is a direct corollary of this
published theorem, with the explicit comparison threshold 32.

**Calibration obligation S.1.** Re-derive that corollary
`min_{j>=0} S^j(n) <= n/2` for density-one odd `n`, with an explicit finite
error bound and a stated odd-step horizon. The theorem's existence of a
density limit does not supply such a numerical error estimate by citation.
The literal value `n/2`, the exceptional finite range, and the conversion
from shortcut steps must be retained.

**Transfer status.** The finite parity encoding argument extends to each
fixed positive odd `d` for `C_d(n)=n/2` on even inputs and `(3n+d)/2` on odd
inputs: the multiplier 3 remains invertible modulo powers of 2. The affine
remainder changes with `d`. A completed quantitative transfer must control
that remainder, keep `d` fixed, and state its dependence on `d`. A parity
bijection alone is not an all-integer stopping theorem. Pulling a density
statement back through `w -> nu(3w)` is a separate obligation; many-to-one
normalization must not silently preserve density.

**Closer finite-horizon match for P6-001.** Borovkov–Pfeifer,
[Corollary 2, equation (11)](https://doi.org/10.1137/S0040585X97978245),
verified in the [author-uploaded text](https://www.researchgate.net/publication/251795632_Estimates_for_the_Syracuse_Problem_via_a_Probabilistic_Model),
give, for k>=2, the natural density of `{n:C^k(n)<n/2}` as
`2^(-k) sum_(0<=j<(k-1)/log_2(3)) binom(k,j)`. It tends to1 with k.
This matches the order of quantifiers in S.1 more closely than eventual
density alone. P6-001 proves a conservative finite-cutoff bound and the
separate odd-clock/W5 conversions; it does not reproduce every exact
fixed-k density in that paper.

**Additional current benchmark (not reproduced here).**
[Inselmann v3](https://arxiv.org/abs/2402.03276v3) states natural-density
power descent below n^epsilon for every fixed epsilon>0, at a specified
shortcut horizon. This is stronger than Korec's exponent range; neither
statement is a count of starts failing to reach the fixed target1.
P6-001's independently proved conservative calibration is unchanged.

## L1a — Published power counts for strict stopping exceptions

Lagarias's 1985 survey, [Theorem D](https://www.cecm.sfu.ca/organics/papers/lagarias/paper/html/theorem-D.html)
and [Theorem F](https://www.cecm.sfu.ca/organics/papers/lagarias/paper/html/theorem-F.html),
states the following for strict shortcut stopping time sigma. Set
`theta=1/log_2(3)` and `h=-theta log_2(theta)-(1-theta)log_2(1-theta)`,
approximately0.949955527188. The density of seeds with sigma>k is at most
`2^(-(1-h)k)`, and the count with infinite sigma through X is at most
`c1 X^h` for an unspecified constant c1. The linked primary TeX formulas
were checked because the HTML displays the equations as images.

These are published benchmarks, not newly reproduced explicit calibrations.
Strict stopping exceptions are not the nonabsorbing basin, and are not
identical to the first-half exception set. No bound for their full inverse
closure follows by changing the set's name. P6-002 examines one specific
endpoint transport premise; its failure is proved directly by exact
one-arrow sources, independently of these published estimates.

## L2 — Tao: almost bounded values, logarithmic density

[Tao's paper](https://arxiv.org/html/1909.03562v3), Theorem 1.3, proves that
for **every** function `f(n)` tending to positive infinity, the minimum of
the ordinary positive Collatz orbit is below `f(n)` for logarithmic-density-one
inputs. Theorem 1.6 supplies the odd-only Syracuse version. These are
statements about orbit minima, not arrival at 1 within a prescribed horizon.
Remark 1.4 gives a constant `C_delta` covering lower logarithmic density at
least `1-delta`, with size `C_delta << exp(delta^(-O(1)))`; the hidden
constants are not numerical constants supplied by this audit.

The paper explicitly explains why density-one descent statements cannot
simply be iterated: the resulting states may concentrate in the exceptional
set. Thus L2 does not discharge C.2's power-saving count of seeds still
unabsorbed at a finite time. A calibration claiming explicit numerical
constants must extract and verify them; citing the theorem is insufficient.

**Transfer status.** No verbatim `3x+d` version of this full theorem is
imported here. It requires a separate primary theorem or an audited adaptation
of the first-passage and mixing arguments. The parity-vector observation in
L1 does not verify that adaptation.

**P6-003 match.** Tao Lemma2.1 and Remark1.10 give the exact valuation-word
and geometric-cylinder context; Section1.1 explains concentration as a
problem with iterating descent estimates. Borovkov–Pfeifer Theorem3 gives
joint finite-horizon threshold densities in shortcut time. Neither is
claimed here to state the exact sparse growth-norm barrier. P6-003 proves
its finite inverse-residue averaging, thresholds and norm count directly,
and derives code mass from P6-001. Kontorovich–Sinai's structure theorem
has a bounded perturbation hypothesis and is not imported as an arbitrary-d
theorem. No novelty conclusion follows from the absence of an exact match
in this audit.

**Version update.** The [corrected Tao v7](https://arxiv.org/abs/1909.03562v7)
was posted July16,2026 and identifies a correction to Lemma7.9. The main
statement remains the growing-threshold logarithmic-density theorem. New
analytic imports must use the corrected version; P6-001/003 prove their
finite-cylinder arguments directly and do not rely on that corrected lemma.

## L3 — Krasikov–Lagarias: the predecessor lower bound

In [Krasikov–Lagarias, Theorem 6.1](https://arxiv.org/pdf/math/0205002), define
`pi_a(X)=#{1<=n<=X: C^j(n)=a for some j>=0}`, with the shortcut map `C`.
For **every fixed positive `a` not divisible by 3**, there is `X0(a)` such
that `pi_a(X)>=X^0.84` for every `X>=X0(a)`. No assumption that `a` reaches 1
is present. It therefore applies to a hypothetical nonabsorbing target as
well. This is the result published in *Acta Arithmetica* 109 (2003), 237–258;
the [author-hosted revised copy](https://websites.umich.edu/~lagarias/doc/krasikov.pdf)
confirms the same quantifiers.

Theorem 2.2 gives the explicit interface
`phi_k^m(y) >= c_k^m * lambda^y / (4 max_m c_k^m)` for `y>=0`, given a
feasible vector for its specified linear program. Table 2 reports `k=11`,
`lambda=1.7922310`, and exponent approximately `0.8417560`. Displayed decimal
values are not a replacement for a certified feasible vector. A calibration
must supply that vector, error bounds, and the target-dependent cutoff.

**Transfer status: unchecked.** The inverse-tree congruences and collisions
must be audited anew for `3x+d`; the theorem above is for `d=1`.

**Route C caution.** C.1 counts all positive starting integers. C.2 should
use the same domain, for example starting odd-only iteration at `oddpart(n)`
and counting only subsequent odd arrows. If a hypothetical nonconvergent
odd seed is divisible by 3, its odd successor is not; that supplies an eligible
target `a`. Every predecessor of this target is also nonconvergent. Hence
an eventual upper bound `C X^(0.84-epsilon)` for the unabsorbed count, with
fixed `C<infinity`, `epsilon>0`, would contradict C.1. Neither an unweighted
source-support count nor a signed annular mass is automatically this count.

## L3a — Linear predecessor density: audited formal input

[Mazur's predecessor manuscript](https://www.proofatlas.ai/papers/positive-lower-density-collatz-predecessors/paper-v1.pdf)
asserts positive lower natural density of distinct predecessors of every
fixed target a>0 with3 not dividing a, without assuming the target reaches1.
P6-004 independently rederived the weighted-history and terminal counting
chain conditional on Tao's corrected v7 mixing theorem. The written audit
retains residue endpoints, exact source multiplicities, endpoint-dependent
shifts, separate error terms and coverage of every sufficiently large scale.
It does not independently derive Tao's analytic mixing estimate.

[Lau, Hexagon2610.00249v1](https://hexagonmath.org/2610.00249v1), dated
October14, supplies an explicit formal refinement. The pinned
[challenge](https://github.com/AxiomMath/CollatzPositiveDensity/blob/3a38bfbb70379e051b51155def1423846fab3a90/Challenge/Basic.lean)
uses L=2^(2^(2^87640)), coefficient1/(t^4 L), and cutoff2^(t^3 L).
For every eligible cutoff it counts distinct odd sources reaching any
target t with3 not dividing t in the ordinary clock and its odd part in
the accelerated clock. The respective bounds are natural floors of
10.46log(n/t) and3.4881log(n/t), with real division. The strongest theorem
has no convergence or nonperiodicity premise on t.

P6-004 rebuilt the [solution](https://github.com/AxiomMath/CollatzPositiveDensity/tree/3a38bfbb70379e051b51155def1423846fab3a90)
independently inside the reviewed offline sandbox:4102 jobs completed.
An independent namespace copy of all four challenge statements and their
definitions compiled against the solution. All eight actual axiom reports
contain exactly propext, Classical.choice and Quot.sound. The challenge's
intentional placeholders were not imported. The [audit record](linear_density_audit/README.md)
separates this execution evidence from static inspection, cached dependency
trust and the additional fresh-kernel replay. Source and dependency pins,
logs, source checksums and statement output are retained.

This is an independent reproduction of the supplied formal derivation,
not our own numerical Fourier/renewal rederivation. Our separate written
argument imports Tao's unspecified mixing constants. Programme label:
**none** under the literal current calibration rule. The full Hexagon
article was unavailable: the adopted exact theorem is the accessible
formal challenge, not a claimed page-by-page match to the full article.
Hexagon's identifier must not be confused with an arXiv identifier.

**Transfer:** the qualitative written reconstruction extends to every fixed
positive d coprime to6 and positive target a not divisible by3. The affine
offset is multiplied by d, roots are chosen beyond d16^b0, and the reference
law is permuted by multiplication by d. All constructed pretarget paths
avoid the absorber. This does not transfer Lau's explicit constants or clocks.

**Consequence for the route:** if any bad odd seed m exists, a=S(m) is a
bad ternary-unit target. Every predecessor of a is bad, yielding a linear
lower bad count at every sufficiently large cutoff. C.2a's arbitrarily
small late fractions would contradict it. That upper estimate remains
open. Positive predecessor density is not a proof of Collatz, and the
historical exponent0.84 should not be described as the strongest audited
lower premise now available here.

## L4 — Simons–de Weger and Hercher: cycle minima

[Simons–de Weger (2005)](https://math.deweger.net/papers/%5B35%5DSidW-3n%2B1-ActaArith%5B2005%5D.pdf)
exclude nontrivial cycles with `1<=m<=68`, where `m` counts local minima
under the shortcut map. The authors' later updated version must be
distinguished from this published 2005 bound.

[Hercher (2023), Theorem 23](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf)
excludes nontrivial `m`-cycles for `m<=91`. Its proof uses a verified initial
range and explicit Diophantine estimates. The journal PDF uses
`X0=695*2^60` in that proof; versions should not be silently mixed. The
journal's [14 June 2026 corrigendum](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/corrigendum.pdf)
repairs an inequality argument in Theorem 21 and retains the bound used
afterward. Any proof-level calibration must read that repair as well as
the original paper and reproduce the required computational inputs.

**Transfer status.** The numerical no-cycle assertions do not hold verbatim
for all `3x+d`: the supplied controls contain small positive cycles. A
canonical-quotient analogue needs an explicit translation of cycle words,
local minima, and exceptional base states before these bounds can be used.
Y.2 must state a precise new class or bound. Excluding cycles leaves the
possibility of unbounded nonperiodic orbits unresolved.

## L5 — Berg–Meinardus, analytic encoding, and the repository quotient

[Berg–Meinardus (1994)](https://link.springer.com/article/10.1007/BF03323136)
give equivalent analytic formulations of Collatz using orbit generating
functions and a linear functional equation. The publisher abstract confirms
these equivalences; full text was not available through the checked
publisher page. Their [1995 author-institution record](https://www.math.uni-rostock.de/math/pub/romako/heft48/berg2.html)
identifies a follow-up discussion. Consequently this setup does **not**
import a precise Berg–Meinardus operator or analytic function-space theorem
without its hypotheses. Lagarias's [author-maintained bibliography](https://websites.umich.edu/~lagarias/3x%2B1.html)
provides historical orientation, not a missing proof premise.

**Closest match and missing bridge.** The repository's finite-current
component criterion is graph linear algebra. On the canonical quotient,
a proposed H.2 statement can specify a bounded sequence `a(q)` satisfying
`a(Tq)=a(q)` and ask whether it must be constant. Its generating series
`sum_{q canonical} a(q) z^q` is analytic for `|z|<1` by boundedness. That
encoding alone does not prove rigidity or identify the series with the
solution space of a particular published functional equation. A component
indicator already meets those boundedness and analyticity conditions.

**Transfer status.** Component duality is a general graph fact and transfers
once the graph and absorber are specified. Rigidity is a separate statement:
multiple components supply nonconstant invariant indicators. A `d`-dependent
quotient must be defined and validated before asserting literal transfer of
the repository's `nu` and `T`.

## R.1 and R.2 — local sufficient tests versus global equivalence

The reviewed repository [stopping-threshold argument](../residual_progress/side_lane_review_33c3829.md)
already proves that universal finite hitting of `9x+5<8q`, with
`q=nu(3w)`, `w=5 mod8`, supplies strict-`rho` induction. Conversely,
Collatz sends every such quotient orbit to 1, which passes that threshold.
Thus the **universally quantified** statement is equivalent to Collatz.
For one fixed input the inequality is only a sufficient endpoint test for
the specified construction. A different signed comparison can succeed
without using that endpoint test. No closest published theorem asserting
this exact quotient threshold or the exact `u` versus `18u+5` merger
reformulation was verified in this audit; L1 and L5 are method-level
comparisons, not evidence of novelty.

## Decision on blanket transfer claims

The wording “all almost-all statements transfer to `3x+d`” is rejected.
Every transfer label needs a specified assertion, density, domain, clock,
absorber, and treatment of fixed versus varying `d`. For example, for
fixed odd `d>1`, positive multiples of `d` stay divisible by `d` under the
raw `3x+d` dynamics. They cannot reach 1 and form a positive-density
exceptional set. This directly separates an almost-everywhere *arrival at
1* claim from almost-everywhere *relative descent*. Merely being a density
statement neither proves transfer nor establishes Phase 6 outcome (a).

These source checks establish the literature matches and scope of proposed
obligations. They do not earn a calibration label until the published
result has been re-derived with the constants required by the selected node.
