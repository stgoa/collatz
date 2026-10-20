---
id: same-seed-factor-complexity-bound
kind: result
title: "A fixed positive survivor of the exit-18 return system has factor complexity above 18.28 L, and small seeds exit within 37 returns"
status: written
claim: >
  Odd-only 3x+1 map S, absorbing at 1; the V/R return subsystem of R74 on G = {w = 40529845 mod 2^26}, K =
  311195/7153, Lambda = 3^24/2^37. Along any legal positive trajectory the states strictly increase and w_j + K <=
  Lambda^j (w_0 + K); if a length-L factor repeats at positions i < j, then 2^(26+e) <= w_j - w_i < Lambda^j (w_0 +
  K) with e >= 19L, overlapping factors included. Hence one fixed positive integer making infinitely many returns
  has liminf p(L)/L >= 19/log2(Lambda) = 18.2850540694..., where p(L) counts the distinct length-L factors of its
  itinerary; p(L) <= 18L + O(1) is impossible even along unbounded lengths (3^432 < 2^685). Every positive start
  at most 260028359941009900571662033 makes fewer than 37 consecutive returns (exit from this subsystem only, not
  absorption or descent). For a fixed nonempty word F(w) = (a w + c)/2^e the exact number of consecutive complete
  copies from w in G is floor((v2((a - 2^e) w + c) - 26)/e). The survivor is a hypothesis: high-complexity
  aperiodic survivors are not excluded, none is constructed, and no current or rule is added.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [exit18-return-integer-cylinders, mixed-rank-growing-blocks]
certificates: [check_legacy_replay.py]
evidence:
  - "check_itinerary_complexity.py, itinerary_complexity.py, itinerary_complexity_audit.json: the legacy implementation, checker and receipt: 62 affine words, 186 lifts, 630 copy cases including 90 zero-copy cases, 12 R67/R74 boundary cases, 32 finite positive traces, 11242 factor repeats including 524 overlapping ones, 45 exact threshold cases, 62 negative rational periodic words, 80 distinct-completion controls and 12 rejections. Fails at its new path and in a legacy replay: it loads ../integer_prefix/ (now ../exit18-return-integer-cylinders/) by its pre-migration folder name and its receipt pins the SHA-256 of this note and of ../integer_prefix/ (now ../exit18-return-integer-cylinders/)INTEGER_PREFIXES.md under their legacy names, both now edited READMEs. Passed at be73a66 as experiments/residual_progress/itinerary_complexity/check_itinerary_complexity.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran every residual-progress step before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a); a replay with the two notes still byte-identical passed at this migration, before they were edited"
  - "../common-critical-rank-basis/batch_r75_r77_check.py: side-lane probe of R75 and R77, replayed by this node's check_legacy_replay.py (see reviewed_by)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: ../common-critical-rank-basis/batch_r75_r77_check.py
    scope: "Finite only (side-lane feed entry 2026-10-18 02:53, VERIFIED, main e9effe1), with the lane's own step and selected: V(w) + K = (3^12/2^19)(w + K) and R(w) + K <= Lambda(w + K) for w > 0; in exact arithmetic floor(2^1305/3^768 - K) = 260028359941009900571662033; on 150 random legal V/R trajectories every repeated factor of length 1-3 (2,188 repeats) has w_j = w_i (mod 2^(26+e)) with e >= 19L and satisfies the growth bound; the fixed-word copy count matches direct iteration in all 200 cases for V, R, VR, RV, VVR. Reproduced by the main lane in side_lane_review_fcc7e88.md. The complexity bound itself follows from the written argument; the status stays written"
aliases: [R77]
tags: [convergence, outer-residual, mixed-rank, factor-complexity, two-adic-coding, same-seed]
---

# A fixed positive survivor of the exit-18 return system has factor complexity above 18.28 L, and small seeds exit within 37 returns

## Statement

Odd-only clock, 1 absorbing. The two-return subsystem of [`exit18-return-integer-cylinders`](../exit18-return-integer-cylinders/README.md): `G = {w > 0 : w ≡ 40529845 mod 2^26}`, `V(w) = (3^12 w + 311195)/2^19`, `R(w) = (3^24 w + 328537586155)/2^37`; `K = 311195/7153`, `Λ = 3^24/2^37`.

1. **Spacing.** Along any legal positive trajectory the states strictly increase and `w_j + K ≤ Λ^j (w_0 + K)`. If a length-`L` factor `ω` repeats at positions `i < j`, both starts lie in its one complete cylinder, so `2^(26+e_ω) ≤ w_j − w_i < Λ^j (w_0 + K)`, with `e_ω ≥ 19L`; overlapping factors are included.
2. **Complexity.** Hence one **fixed** positive integer making infinitely many returns has `liminf p(L)/L ≥ 19/log₂Λ = 18.2850540694…`, where `p(L)` counts the distinct length-`L` factors of its itinerary. Since `3^432 < 2^685`, `p(L) ≤ 18L + O(1)` is impossible, even along unbounded lengths.
3. **Finite return bound.** Every positive start at most `⌊2^1305/3^768 − 311195/7153⌋ = 260028359941009900571662033` makes fewer than 37 consecutive returns. This is an exit from this subsystem, not absorption, Syracuse descent or termination of other comparisons.
4. **Fixed-word repetition.** For a fixed nonempty word `F(w) = (aw + c)/2^e`, the exact number of consecutive complete copies from `w ∈ G` is `⌊(v2((a − 2^e)w + c) − 26)/e⌋`. For `V` this is one less than R67's guarded block count ([`mixed-rank-growing-blocks`](../mixed-rank-growing-blocks/README.md)).

The infinite survivor is a hypothesis throughout: high-complexity aperiodic survivors are not excluded, none is constructed, and no current or dispatcher rule is added. A powers-of-three sequence with real limit 0 and 2-adic limit 1 shows that the two completions' limits cannot be identified.

## Proof

The legacy note "A fixed positive survivor must have many different return factors" follows, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**Status: written conditional theorem and bounded exact replay.** In the
two-return subsystem of [the complete prefix theorem](../exit18-return-integer-cylinders/README.md),
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

### 1. The precise subsystem and a real height bound

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

### 2. Repeating a factor requires a large integer difference

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

### 3. The complexity bound for one hypothetical infinite survivor

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

#### A finite return bound without enumerating the seeds

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

### 4. Exact maximum repetition count for any fixed word

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

### 5. Why real and 2-adic limits cannot be identified

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

### 6. Verification and boundaries

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

## Certificates

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B12 migration; standard library). The legacy scripts of this folder load sibling modules by their pre-migration paths, so they no longer run here. This certificate calls `tools/legacy_replay.py`, which rebuilds the pre-migration layout in a temporary directory from `tools/legacy_paths.json`, runs the unmodified legacy scripts there without `-O` (as `scripts/verify_all.py` did at `be73a66`), and requires exit 0 and every copied file unchanged. It writes nothing in the repository. It replays: the side-lane probe `batch_r75_r77_check.py` from [`common-critical-rank-basis`](../common-critical-rank-basis/README.md) (under 1 s, receipt reproduced byte for byte), which checks the growth bound, the exact 37-return threshold, the spacing lemma on 2,188 repeated factors and the fixed-word copy count. The legacy checker `check_itinerary_complexity.py` cannot be replayed: its receipt pins the hashes of two notes that are now edited READMEs (see `evidence`). The commands in the legacy text name `experiments/residual_progress/itinerary_complexity/`.

## Remarks

- **General form.** The same exact-cylinder and growth mechanism for every odd-only orbit, with the weaker constant `1/log₂(3/2) = 1.7095…`, is the side lane's [`divergent-orbit-itinerary-complexity`](../divergent-orbit-itinerary-complexity/README.md) (R77-b), reviewed by the main lane.
- This is the first constraint in the programme tying one integer seed across unboundedly many prefixes (side-lane feed 02:53); it narrows, but does not settle, [`aperiodic-exit18-return-survivors`](../../questions/aperiodic-exit18-return-survivors.md).
- No external theorem or novelty is claimed.

## History

- Migrated from `experiments/residual_progress/itinerary_complexity/ITINERARY_COMPLEXITY.md` (legacy ID R77) at commit `be73a66`, by the B12 migration (Claude, Opus 5.5). Note, scripts and receipt moved byte-identical; `check_legacy_replay.py` was added at the migration. Editing this note and `INTEGER_PREFIXES.md` (now [`exit18-return-integer-cylinders`](../exit18-return-integer-cylinders/README.md)) breaks the legacy checker's pinned hashes; it passed a replay at this migration before the edits. Legacy status: "written conditional complexity theorem, exact fixed-word repetition formula, and finite all-seed bound for the specified R74 subsystem".
- Main lane (ChatGPT, Codex), 2026-10-18, from commit `e9effe1`. The batch's "independent model" proof and code reviews (archive/convergence-residual-progress/REPORT.md) were the main lane's own agents, not a different lane.
