# C004 — Absolute spacing is unbounded in positive rational cycles

**Status:** written elementary obstruction, exact examples, and a bounded
primary-source scope check. No novelty or formal-verification claim. This
note uses the raw odd-only rational map; it does not replace the absorber
convention for integer convergence questions.

## 1. Question and outcome

Consider a primitive positive odd rational cycle of

\[
S_1(x)=\frac{3x+1}{2^{v_2(3x+1)}},
\]

with common reduced denominator coprime to 6. The proposed intrinsic
criterion was that any nontrivial such cycle contains distinct states
less than 2 apart. This would exclude reduced denominator 1 by the odd
integer lattice.

**That criterion is false.** The actual raw \(3x+5\) cycle

\[
19\xrightarrow{1}31\xrightarrow{1}49\xrightarrow{3}19
\]

normalizes to the primitive rational cycle

\[
19/5\longrightarrow31/5\longrightarrow49/5\longrightarrow19/5.
\]

Its smallest pair distance is \(12/5>2\). The arrows have the exact
displayed valuations: \(62=2\cdot31\), \(98=2\cdot49\), and
\(152=8\cdot19\). This is an existing C001 control, with valuation word
\((1,1,3)\), intercept 19 and denominator \(32-27=5\).

There is a stronger all-size obstruction:

> For every real \(G>0\), a primitive positive rational cycle exists with
> at least two odd states, every distinct pair of odd states more than
> \(G\) apart, and minimum greater than \(mG\), where \(m\) is its number
> of odd states. The construction imposes no fixed reduced denominator.

The proof below develops the existing R71 mechanical construction. It
does not posit an arbitrary dilation of a \(3x+1\) cycle: scaling a
normalized rational cycle by its denominator changes the map to
\(3x+d\), and every displayed scaled arrow is legal on that map.

## 2. What the lattice inequalities actually say

Write the distinct states in increasing order as
\(x_1<\cdots<x_m\), with \(m\ge2\), and their common reduced denominator
as \(d\). Every numerator \(p_i=dx_i\) is odd. Therefore

\[
x_{i+1}-x_i\ge\frac2d.
\]

Writing \(\sigma=\min_{i\ne j}|x_i-x_j|\) and
\(W=x_m-x_1\) gives

\[
\boxed{\quad d\ge\frac2\sigma,\qquad
 d\ge\frac{2(m-1)}W.\quad} \tag{1}
\]

Equivalently, the lattice supplies **lower** bounds on separation and
width. To exclude \(d=1\) through these inequalities requires an
additional **upper** bound \(\sigma<2\) or \(W<2(m-1)\).
The first example violates both proposed uniform upper bounds:
\(\sigma=12/5\), \(W=6>4\). Section 4 excludes any constant upper bound
on \(\sigma\), or on \(W/(m-1)\), over all primitive positive rational
cycles. These statements leave open bounds that use denominator-specific
arithmetic information or a genuinely narrower hypothesis.

## 3. Ordered mechanical states and exact adjacent increments

Take coprime integers \(A\ge m\ge2\) with \(2^A>3^m\). Define

\[
a_i(\ell)=\left\lfloor\frac{(i+1)A+\ell}{m}\right\rfloor
          -\left\lfloor\frac{iA+\ell}{m}\right\rfloor,
\qquad 0\le i,\ell<m,
\]

\[
B_\ell=\sum_{j=0}^{m-1}3^{m-1-j}
                  2^{\lfloor(jA+\ell)/m\rfloor},
\qquad D=2^A-3^m.
\tag{2}
\]

All valuations are positive. Shifting a word by \(s\) positions changes
its phase to \(\ell+sA\pmod m\), so coprimality makes all \(m\) phases
rotations of one cycle. The cyclic intercept identity gives exact
valuation legality, and R71 proves that every \(B_\ell/D\) has reduced
denominator exactly \(D\). See
R71, Sections 1–2 (`experiments/residual_progress/lattice_cycles/BALANCED_DENOMINATORS.md`, not yet migrated).

For each \(0\le\ell\le m-2\), there is exactly one
\(j=j(\ell)\in\{1,\ldots,m-1\}\) satisfying

\[
jA+\ell\equiv m-1\pmod m.
\]

Only that summand's floor increases from phase \(\ell\) to
\(\ell+1\). The unique index is not zero because \(\ell\le m-2\).
Consequently

\[
B_{\ell+1}-B_\ell
 =3^{m-1-j}2^{\lfloor(jA+\ell)/m\rfloor}>0.
\tag{3}
\]

Thus phase order is exactly size order, and these are \(m\) distinct
states of one primitive cycle. Moreover,

\[
\begin{aligned}
3^{m-1-j}2^{\lfloor(jA+\ell)/m\rfloor}
&>\frac{3^{m-1}}2
   \left(\frac{2^{A/m}}3\right)^j\\
&\ge\frac{3^{m-1}}2.
\end{aligned}
\tag{4}
\]

The first inequality follows from
\(\lfloor(jA+\ell)/m\rfloor>jA/m-1\); the second from \(2^A>3^m\).
The same lower bound holds for every summand of \(B_\ell\).

Put \(\theta=\log_2 3\) and \(\delta=A-m\theta>0\). Since
\(D=3^m(2^\delta-1)\), (3)–(4) imply

\[
\boxed{\quad
\sigma>\frac1{6(2^\delta-1)},\qquad
\min_\ell\frac{B_\ell}D>
          \frac m{6(2^\delta-1)}.
\quad}\tag{5}
\]

For nonadjacent phases the difference is a sum of positive adjacent
increments, so the first bound applies to every distinct pair. Also
\(W>(m-1)/[6(2^\delta-1)]\).

There is no conflict with a small **ratio** of largest to smallest state.
Indeed, termwise

\[
\left\lfloor\frac{jA+m-1}m\right\rfloor
 \le\left\lfloor\frac{jA}m\right\rfloor+1,
\]

and the corresponding inequality after exponentiation is strict at
\(j=0\). Therefore

\[
\max x/\min x=B_{m-1}/B_0<2. \tag{6}
\]

Hence arbitrarily large absolute separations occur even inside this
ratio interval. The [companion proof](../../results/narrow-cycles-are-mechanical/ROTATION_LATTICE.md) establishes
the converse to (6). That converse is not needed for this obstruction.

## 4. Arbitrarily small positive errors, without an imported rate

Here is an elementary existence argument for the needed coprime upper
approximations. No continued-fraction estimate is required.

The real number \(\theta=\log_2 3\) is irrational: a rational equality
would imply equality of a positive power of 2 and a positive power of 3.
For an integer \(Q\ge2\), the pigeonhole principle applied to the
\(Q+1\) fractional parts \(0,\theta,\ldots,Q\theta\) in \(Q\) equal
subintervals supplies integers \(m\ge1,A\) with

\[
0<|m\theta-A|<1/Q.
\]

If \(A-m\theta>0\), keep this pair. Otherwise put
\(\epsilon=m\theta-A\in(0,1/Q)\) and
\(t=\lfloor1/\epsilon\rfloor\). Then

\[
0<(tA+1)-tm\theta=1-t\epsilon<\epsilon<1/Q.
\tag{7}
\]

Both inequalities are strict because \(\epsilon\) is irrational. Thus
\((A',m')=(tA+1,tm)\) is an upper approximation. In either case divide
the two integer coordinates by their gcd. This preserves a strictly
positive error and can only decrease it.

Letting \(Q\) tend to infinity supplies coprime pairs with
\(\delta=A-m\theta\to0^+\). Their reduced \(m\)'s are unbounded:
bounded \(m\) and errors below 1 allow only finitely many \(A\), none
with zero error. We can therefore select a subsequence with \(m\ge2\)
and \(A\ge m\). Eventually \(\delta<1\), so
\(A=\lceil m\log_2 3\rceil\), and all valuations in (2) are 1 or 2.

For any prescribed \(G>0\), choose such a pair satisfying
\(\delta<\log_2(1+1/(6G))\). Equation (5) proves the theorem in
Section 1. For \(G\ge1\), every rational state exceeds 1, and the
corresponding integer \(3x+D\) cycle avoids the normalized absorber
state \(D\). There is no assertion of unbounded separations at one
fixed \(D\), nor of a new cycle at \(d=1\).

## 5. Exact example and check scope

The parameters \((A,m)=(8,5)\) give \(D=13\) and the word
\((1,2,1,2,2)\). Its ordered phase numerators are

\[
(B_0,\ldots,B_4)=(319,367,421,485,557),
\]

with adjacent differences \((48,54,64,72)\). Its chronological raw
\(3x+13\) cycle is

\[
319\xrightarrow{1}485\xrightarrow{2}367
\xrightarrow{1}557\xrightarrow{2}421\xrightarrow{2}319.
\]

Thus the rational cycle has \(\sigma=48/13\),
\(W=238/13\), and ratio \(557/319<2\). The lower gap bound in (5)
is \(81/26\), strictly below \(48/13\), as required.

An independent exact-integer calculation during this audit verified:

- Every arrow, oddness, and coprimality for the \(d=5\) and \(d=13\)
  examples above.
- The unique changing index, equality (3), and strict inequality (4)
  for all phases of \((A,m)=(5,3),(8,5),(27,17),(65,41),(485,306)\).

These finite checks are arithmetic checks of displayed examples, not
the proof of the quantified statement. The proof is Sections 3–4.
The C004 common replay is maintained separately by the data lane; this
note does not represent another agent's replay as an independent run.

## 6. Primary-source scope

The bounded pass inspected the following primary texts. It did not
establish a novelty claim for this consequence of mechanical formulas.

- **Halbeisen–Hungerbühler, _Optimal bounds for the length of rational
  Collatz cycles_ (1997).** Full author-hosted paper inspected.
  Lemma 2 records the affine formula; Lemma 5 identifies the mechanical
  parity pattern maximizing the cycle minimum at fixed shortcut length
  and number of odd steps. This concerns the extremal minimum, not a
  universal bound on the distance between two odd states. The source
  uses the shortcut clock; our \(A\) is its total shortcut length and
  our \(m\) is its number of odd states.
  [Author-hosted full text](https://people.math.ethz.ch/~halorenz/publications/pdf/collatz.pdf).
- **Fernández–Ibáñez, _Christoffel Words as Extremal Structures in
  Collatz Dynamics_, arXiv:2607.24844v1 (July 2026).** Full HTML source
  inspected. Theorem 7.3 identifies the Christoffel rotation class as
  the maximizer of the minimum rotation numerator. Section 8 gives
  minimum-versus-length/density bounds. These statements are not a
  closest-pair theorem or the converse of (6). This note imports none
  of its proofs or novelty assertions.
  [Primary preprint](https://arxiv.org/html/2607.24844v1).
- **Knight, _Collatz high cycles do not exist_ (2026).** C001 recorded
  the publisher-preview scope: “high” means extremal minimum for fixed
  shortcut counts, not an arbitrary lower bound on every state. The
  publisher endpoint failed during this follow-up; no fresh full-text
  audit is claimed here. It must not be cited as an already verified
  proof of the narrow-ratio converse.
  [Publisher entry](https://www.sciencedirect.com/science/article/pii/S0012365X25004200).

The searches for closest-state, ratio-two, circular-order and cycle
geometry statements did not locate an inspected primary theorem
identical to the proposed narrow-ratio converse. This is a bounded
search outcome, not evidence that the converse is new. The obstruction
in Sections 1–4 needs no external theorem beyond the elementary
construction already persisted as R71.

## 7. Seven-field assessment

1. **Objects.** All positive primitive odd rational cycles for the
   spacing question; mechanical cycles with coprime totals provide
   the exact obstruction.
2. **Structural gain.** Phase order is size order, with one explicit
   monomial for every adjacent increment. Positive approximation errors
   tending to zero make every pair gap unbounded, simultaneously with
   the minimum.
3. **Translated unresolved gap.** Lattice packing cannot supply its
   own missing upper bound. An integer-cycle obstruction must retain
   denominator-specific arithmetic or additional structural information.
4. **Worked example.** The exact \(d=5\) cycle disproves the threshold
   2; the \(d=13\) cycle exhibits both separation greater than 2 and
   largest-to-smallest ratio below 2.
5. **Known-cycle controls.** These are actual generalized cycles with
   verified valuations. They preserve R71's nonintegrality and do not
   turn a raw cycle containing an absorber into a nonconvergence witness.
6. **Cheapest meaningful next test.** Test an order/cancellation
   constraint valid across several dyadic ranges; an additive-gap
   catalogue cannot repair the refuted uniform assertion.
7. **Genuinely intermediate milestone.** The companion proof now shows
   that the intrinsic ratio condition forces a mechanical word, hence
   its exact denominator, without assuming a repeated-block
   decomposition. It leaves wider cycles and all divergence questions
   open.
