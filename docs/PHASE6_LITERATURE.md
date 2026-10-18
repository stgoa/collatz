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

The reviewed repository [stopping-threshold argument](../experiments/residual_progress/side_lane_review_33c3829.md)
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
