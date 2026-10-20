# A fixed positive survivor must have many different return factors

**Status: written conditional theorem and bounded exact replay.** In the
two-return subsystem of [the complete prefix theorem](../integer_prefix/INTEGER_PREFIXES.md),
any **one fixed positive integer** that makes infinitely many returns has
factor complexity

\[
 \liminf_{L\to\infty}\frac{p(L)}L
 \ge \frac{19}{\log_2(3^{24}/2^{37})}
 \approx18.2850540694.                                      \tag{1}
\]

Here p(L) counts all distinct length-L words occurring anywhere in that
one infinite itinerary. In particular, an itinerary satisfying
`p(L)<=18L+O(1)` is impossible. This strengthens exclusion of eventually
periodic words, but permits many aperiodic words. It neither constructs a
positive survivor nor excludes all of them. No accepted current rule is
added, and the higher leading pair remains unresolved.

This is a constraint across prefixes of the **same** integer. The seed in
the earlier finite-cylinder theorem may vary with the chosen word; that
theorem is fully consistent with this result. No external theorem or
novelty assertion is used here.

## 1. The precise subsystem and a real height bound

Retain the R74 constants and complete positive domains:

```
A=3^12=531441, M=2^19, B=311195, D=A-M=7153,
P=A^2, C=B(A+M), Q=2^37,
G={positive integers w : w=40529845 mod2^26},
V(w)=(Aw+B)/M, R(w)=(Pw+C)/Q=2V^2(w).
```

A V return has input `2218391138229 mod2^45`; an R return has input
`8515171531530858421 mod2^63`. Each output must again belong to G. The
domains are disjoint. Set

\[
 K=B/D>0,\qquad r=A/M>1,\qquad \Lambda=P/Q=2r^2>1.
\]

The shifted real coordinate X=w+K obeys exactly

\[
 X(Vw)=rX(w),\qquad X(Rw)=\Lambda X(w)-K.          \tag{2}
\]

Consequently every legal positive finite trajectory w_0,...,w_n satisfies

\[
 0<w_i<w_j\quad(i<j),\qquad
 X(w_j)\le\Lambda^jX(w_0).                       \tag{3}
\]

Strict increase follows directly from the positive offset and slope
greater than 1 in both unshifted maps. Equation (2) gives the upper bound
by induction. It is not an assumption about the statistical frequency
of the two symbols.

There are no equal-state or absorbing cases on this positive domain:
strict increase prohibits repeats, and 1 is not in G. Exiting this subsystem
is not being identified with absorption or even Syracuse descent.

## 2. Repeating a factor requires a large integer difference

For a finite word omega, write

\[
 F_\omega(w)=(a_\omega w+c_\omega)/2^{e_\omega},\quad
 e_\omega=19\#V+37\#R,
\]

with a_omega odd. The complete-prefix theorem gives a **single** starting
residue modulo `2^(26+e_omega)` for following omega and ending in G.

Suppose a finite legal itinerary has the same length-L factor omega
beginning at positions i<j. Both w_i and w_j are in that same cylinder.
They are distinct positive integers by (3), so

\[
 2^{26+e_\omega}\mid(w_j-w_i),\qquad
 2^{26+e_\omega}\le w_j-w_i
 <X(w_j)\le\Lambda^jX(w_0).                       \tag{4}
\]

Thus every actual repeat obeys the exact integer inequality

\[
 D\,2^{26+e_\omega}Q^j < (Dw_0+B)P^j.             \tag{5}
\]

This includes overlapping factors. No assumption that their occurrences
are disjoint, or that their intervening path is periodic, was used.
The word-specific precision e_omega can be retained; the uniform bound
`e_omega>=19L` is enough for the next conclusion.

## 3. The complexity bound for one hypothetical infinite survivor

Fix a positive integer w_0 in G and **assume** that its legal trajectory
has infinitely many V/R returns. Its unique itinerary is then defined at
every position, because the two return domains are disjoint.

For a given L>=1, every position j>=0 satisfying

\[
 (Dw_0+B)P^j\le D\,2^{26+19L}Q^j                  \tag{6}
\]

starts a different length-L factor. Indeed, two equal factors at i<j
would contradict (5). Since Lambda>1, the qualifying positions form an
initial interval. Hence

\[
 p(L)\ge \max\left(0,1+\left\lfloor
 \frac{26+19L-\log_2(w_0+K)}{\log_2\Lambda}
 \right\rfloor\right).                          \tag{7}
\]

When the interval is empty the displayed lower bound is simply 0;
the independent trivial bound p(L)>=1 remains valid. The executable
computes (6) by exact integer comparisons, without using floating logarithms.
Dividing (7) by L proves (1), because w_0 is fixed.

In particular, `3^432<2^685` proves exactly that `Lambda^18<2^19`.
Therefore `19/log2(Lambda)>18`, so `p(L)<=18L+O(1)` cannot hold, even
along an unbounded sequence of lengths. More generally, for any constant
`c<19/log2(Lambda)`, `p(L)<=cL+O(1)` is impossible along unbounded lengths.

This is an exclusion of a specified itinerary class. Computability of an
itinerary does not imply a linear factor-complexity bound; no such inference
is made. Aperiodicity alone also supplies no bound on p(L). High-complexity
aperiodic itineraries remain outside this obstruction.

### A finite return bound without enumerating the seeds

There are only 2^L binary factors of length L. A legal prefix of length
`2^L+L` has factors beginning at all positions `0,...,2^L`. If

\[
 (w_0+K)\Lambda^{2^L}\le2^{26+19L},                \tag{8}
\]

equation (6) makes all these 2^L+1 factors distinct, a contradiction.
Therefore such a seed has fewer than `2^L+L` consecutive returns.
For L=5 this gives the exact cutoff

\[
 0<w_0\le
 \left\lfloor\frac{2^{1305}}{3^{768}}-
                   \frac{311195}{7153}\right\rfloor
 =260028359941009900571662033:
 \quad\text{no legal prefix of 37 returns}.         \tag{9}
\]

Inputs outside G have no first return. For inputs in G the statement is a
uniform proof for the entire displayed interval, not an enumerated scan.
It guarantees an exit from this **specified V/R subsystem**, not absorption,
Syracuse descent, or termination of the larger research programme.
It still permits an infinite survivor above this finite cutoff.

## 4. Exact maximum repetition count for any fixed word

There is also an exact finite version of the periodic exclusion. Fix a
nonempty omega, put a=a_omega, c=c_omega, q=2^e_omega, and fix w in G.
All offsets are positive and a>q. Define the positive integer

\[
 Z=(a-q)w+c>0.
\]

For every k>=1,

\[
 F_\omega^k(w)-w
 =\frac{Z}{q^k}\sum_{t=0}^{k-1}a^{k-1-t}q^t.     \tag{10}
\]

The sum is odd: its first term is odd and all later terms are even.
Therefore `F_omega^k(w)` is an integer in G if and only if
`v2(Z)>=26+k*e_omega`. By completeness of the word cylinder, this is
equivalent to following all k copies with every intermediate state in G.
Positivity of the intermediates follows from the forward affine maps.

Also `v2(Z)>=26` for every w in G. To see this, choose one positive
cylinder member u for omega. Both u and F_omega(u) are in G, so
`(a-q)u+c=q(F_omega(u)-u)` is divisible by 2^26. Since u=w modulo 2^26,
the same is true of Z. Thus the exact number of complete consecutive copies is

\[
 k_{\max}(w,\omega)
 =\left\lfloor\frac{v_2((a-2^{e_\omega})w+c)-26}
 {e_\omega}\right\rfloor.                        \tag{11}
\]

This number is finite for positive w. Its finiteness does not limit the
total number of returns after changing the next word. Applying (11) to a
different word is another scoped repetition test, not a proof of universal
termination. In particular, a higher-complexity infinite word need not
repeat any one fixed word arbitrarily many consecutive times.

For omega=V, equation (11) is `floor((v2(Dw+B)-26)/19)`.
These are complete V returns **ending in G**. R67's count of guarded
growing blocks, whose final endpoint may leave G, is one greater.
The two clocks and the off-by-one distinction must be preserved.

## 5. Why real and 2-adic limits cannot be identified

Inverse-word expansions contract both in the real metric and the 2-adic
metric. This alone does **not** identify their two limits as the same
rational number. An explicit counterexample to that inference, using
the very same bases A and M, is

\[
 z_n=\frac{A^n\bmod M^n}{A^n},\qquad n\ge1.
\]

Its real value satisfies `0<z_n<(M/A)^n`, so its real limit is 0.
But `z_n-1` has 2-adic order at least 19n, because A is odd and
the numerator difference is divisible by M^n. Its 2-adic limit is 1.
All denominators are powers of 3. This is an arithmetic counterexample
to an inference about completions, not a return itinerary or a Collatz
counterexample.

The actual periodic word point `-c/(a-2^e)` is negative and rational.
For a repeated periodic block, corresponding states are equal, so the
strictly positive integer difference used in (4) is absent. These synthetic
negative rational periodic controls are tested separately. They show why
the positivity, integrality and distinct-state hypotheses cannot be dropped.
No rationality-implies-periodicity assertion is assumed or proved.

## 6. Verification and boundaries

Run `python3 experiments/residual_progress/itinerary_complexity/check_itinerary_complexity.py`.
The default replays the adjacent receipt; `--write-receipt` refreshes it.
The portable module has no dependency beyond the Python standard library.
The check independently composes affine words, compares complete cylinders,
checks exact repetition counts by actual guarded returns, verifies repeated
factor differences in finite positive traces, tests the integer complexity
threshold, and includes negative rational periodic and invalid-input controls.
The receipt records the precise counts and source hashes.

The infinite result depends on the written proof, not on these finite
examples. The fixed survivor is a hypothesis throughout. No current is
supplied for its higher leading pair, no accepted dispatcher is changed,
and no claim is made about all positive Collatz trajectories.
