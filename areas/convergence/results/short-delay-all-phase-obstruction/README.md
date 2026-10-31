---
id: short-delay-all-phase-obstruction
kind: result
title: The three-source chain stays isolated in 17/18 and 53/54 of the ternary phases, refuting completion at exposure 2h + 1 in every phase
status: written
claim: >
  Odd-only 3x+1 map, absorbing at 1; A_N the six-band annulus; G_D(N) the first D arrows exposed from every
  nonzero source; N = 3X/128, h = v_3(X-1), U = (X-1)/3^h, y_j = 3^j X/2^j - 1. (Classification) For h = 2,
  2^10 | X, X >= 497664, the component of y_3 in G_5(N) is exactly the path y_1 -> ... -> y_8 with only the
  sources (-2, +2, +2) iff U != 16 mod 27; for h = 3, 2^11 | X, X >= 8957952, the same holds in G_7(N) iff
  U != 31 mod 81 (isolated fractions 17/18 and 53/54 of the unit classes; in each excluded class a further
  annular source really attaches). The 70 isolated classes are proved by finite symbolic inverse-decision
  traces valid on whole arithmetic progressions. (Ladder) Every N = 96 64^(2 + 27t), X = 2^(24 + 162t),
  t >= 0, has h = 2 and an isolated mass-2 component at depth 5, so completing the block at exposure 2h + 1 in
  every phase is refuted even for h = 2 and with all valuation words. (Coverage) The two delayed-release
  families cover the fraction 1/3^(r+3) of the unit classes at their modulus. A finite scan of 1944
  representatives gives 21 exact zero-cost partial currents; no class coverage is inferred from them. Deeper
  or phase-sensitive constructions are not excluded.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [delayed-release-cancellation, depth-32-aggregate-exposure-obstruction, depth-32-obstruction-infinite-family]
certificates: [check_legacy_replay.py]
evidence:
  - "check_coverage.py, coverage_audit.json: the legacy checker (rederives the 70 symbolic traces with their translation checks, the exceptional-class attachments, the 135-comparison lift at N = 393216, and the finite representative scan with the 21 stored partial certificates; caps 2000 vertices and 30000 queries, all finished; about 0.6 s). Fails at its new path: it imports inverse_exposure_probe and the release checker from ../templates/ and ../release/ (now ../unbounded-exposure-depth-necessary/ and ../delayed-release-cancellation/). Passed at be73a66 as experiments/residual_progress/release_coverage/check_coverage.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran these steps before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a). Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
aliases: [R19]
tags: [convergence, packet-currents, annular, exposure-depth, delayed-release, obstruction, refutation]
---

# The three-source chain stays isolated in 17/18 and 53/54 of the ternary phases, refuting completion at exposure 2h + 1 in every phase

## Statement

Notation of [`delayed-release-cancellation`](../delayed-release-cancellation/README.md): odd-only clock, absorbing at 1; `N = 3X/128`, `h = v_3(X − 1)`, `U = (X − 1)/3^h`, `y_j = 3^j X/2^j − 1`; the block `μ_0 = −2δ_(y_1) + 2δ_(y_2) + 2δ_(y_3)`.

**Theorem (exact short-depth phase classification).** The component of `y_3` in `G_D(N)` is exactly the path `y_1 → ⋯ → y_(D+3)` with only the three sources `(−2, +2, +2)` in precisely these phases:

| Exact ternary depth | Exposure | Binary requirement | Sufficient size | Isolated phases |
|---|---:|---|---:|---|
| `h = 2` | `D = 5` | `2^10 ∣ X` | `X ≥ 497664` | `U ≢ 16 (mod 27)` |
| `h = 3` | `D = 7` | `2^11 ∣ X` | `X ≥ 8957952` | `U ≢ 31 (mod 81)` |

So 17/18 and 53/54 of the unit classes are isolated; in each excluded class an actual further source `v` attaches through the valuation word `(1^h, 2^h, 3)`. An isolated component has mass 2 and no current on `G_D(N)` (signed, rational, cross-packet) leaves a nonpositive residual. The 70 isolated classes are proved by finite symbolic inverse-decision traces (complete inverse decisions, affine inequalities valid for every real `q ≥ 1`, and a translation argument preserving integrality, inverse branches and source coefficients along `X = X_0 + jT`), not by numerical representatives.

**Refutation on the ladder.** `N = 96·64^(2+27t)`, `X = 2^(24+162t)`, `t ≥ 0`, has `h = 2` and an isolated depth-5 component (eight vertices; the lift at `N_0 = 393216` uses 28 queries and 135 comparisons). The proposed bound "exposure `2h + 1` suffices in every phase" fails.

**Coverage.** At fixed qualifying `h` the two delayed-release families cover exactly `2` of the `2·3^(r+3)` unit classes of `U` modulo `3^(r+4)`, a fraction `1/3^(r+3)` (for `h = r = 2`, `U ≡ 70, 313 (mod 729)`). A separate finite scan of one representative per class (486 at `h = 2`, 1458 at `h = 3`) gives 21 exact zero-cost partial certificates with capacity and attachment placement checked; this is finite representative data, not class coverage.

Not human peer-reviewed or formally verified; no novelty or Collatz convergence claim. A phase-sensitive growing-depth rule controlling every remaining component is open, and no phase is shown unfillable at all depths.

## Proof

The legacy note "Complete phase obstructions to the short delayed-release rule" follows, lightly edited (headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

Date: 2026-10-17. Status: written proof with finite symbolic certificates,
plus a separate finite scan and exact partial-current certificates.
The claims are not human peer-reviewed or formally verified. No novelty
or Collatz convergence claim is supplied.

### 1. The question and the answer

Use the odd-only Syracuse map `S`, absorbed at 1, the actual annular
measure `A_N`, and the historical graph `G_D(N)` exposing the first `D`
arrows from **every nonzero annular source**. Set

\[
N=3X/128,\qquad h=v_3(X-1),\qquad U=(X-1)/3^h,
\]

and write

\[
y_j=3^jX/2^j-1.
\]

The previous [delayed-release construction](../delayed-release-cancellation/README.md)
cancels the actual source block

\[
\mu_0=-2\delta_{y_1}+2\delta_{y_2}+2\delta_{y_3}
\]

in selected ternary phases at exposure at most `2h+1`. Its coverage does
**not** extend to every phase. In fact, the complete component remains
isolated for most phases already when `h=2` or `h=3`.

#### Theorem: exact short-depth phase classification

The component of `y_3` in `G_D(N)` is precisely the path

\[
y_1\longrightarrow y_2\longrightarrow\cdots\longrightarrow y_{D+3},
\tag{1}
\]

with only the three sources `(-2,+2,+2)`, exactly in the following
complementary phases:

| Exact ternary depth | Exposure | Binary requirement | Sufficient size | Isolated phases |
|---|---:|---|---:|---|
| `h=2` | `D=5` | `2^10 divides X` | `X>=497664` | `U != 16 modulo27` |
| `h=3` | `D=7` | `2^11 divides X` | `X>=8957952` | `U != 31 modulo81` |

Only unit classes of `U` are counted, since `h` is exact. Thus the
isolated fractions are **17/18** and **53/54**, respectively. In each
excluded class a further nonzero annular source really attaches, so the
classification is an equivalence. No assertion about cancellation in
that exceptional class follows merely from its attachment.

The proof of the 70 isolated classes is a finite exact inverse-decision
certificate valid on full infinite arithmetic progressions, explained
in Section 3. It exhausts all possible incoming historical paths. It
does not restrict valuation words to a selected pattern.

An isolated component has mass 2 and does not contain 1. Summing a
divergence over this entire exposed component gives zero. Consequently
neither `A_N` nor the original block with any source-capacity-safe
additions from this graph can have a current on `G_D(N)` leaving an
everywhere nonpositive residual. This conclusion permits signed or
rational currents and arbitrary cross-packet grouping inside `G_D`.
It concerns the specified exposure; it does not rule out a deeper
certificate, other arrows, or an eventual recursive construction.

### 2. A single required-ladder family refutes the all-phase conjecture

The fixed cutoff

\[
X_0=2^{24},\qquad N_0=393216=96\cdot64^2
\]

has a complete depth-5 component of eight vertices and seven arrows.
Its only source rows are

| Source | Actual coefficient |
|---:|---:|
| 25165823 | -2 |
| 37748735 | +2 |
| 56623103 | +2 |

The independent complete symbolic lift at this cutoff proves the same
component for `N=N_0 q`, `q>=1`, `q=1 modulo243`. It uses 28 reachability
queries and 135 affine comparisons. In particular, for every integer
`t>=0`, take

\[
\boxed{\quad N=96\cdot64^{2+27t},\qquad
X=2^{24+162t}.\quad}
\tag{2}
\]

Indeed, `2^162=1 modulo243`, so the lift applies. Also
`v_3(X-1)=1+v_3((24+162t)/2)=2`: the factor
`12+81t` has exactly one factor of 3. Thus (2) gives infinitely many
counterexamples, already on a single required ladder, to the proposed
assertion that exposure `2h+1` suffices in every phase of the obstructing
block. The elementary order and valuation argument used here is proved
in the earlier delayed-release note.

### 3. Why the 70 finite symbolic traces prove infinite classes

The checker imports the complete inverse oracle and the affine-decision
verifier from [the templates directory](../depth-32-aggregate-exposure-obstruction/README.md).
Their correctness arguments are retained in
[the fixed-depth lift note](../depth-32-obstruction-infinite-family.md).
Here we specify the additional phase argument rather than infer an
infinite conclusion from numerical representatives.

#### Complete inverse decisions

For an exposed source at height less than `144N`, its `r`th iterate is
at most

\[
B_r=3^r144N/2^r-1.
\]

The binary hypotheses make the relevant bounds integral. To decide
whether a state has an annular source ancestor at distance at most `r`,
the verifier first tests its exact annular coefficient. If that is zero,
it tests the height bound and recursively enumerates **every** odd
predecessor `(2^a y-1)/3` below `B_(r-1)`. Its congruence determines the
parity of `a`; successive candidates multiply `2^a` by 4. The first
excluded predecessor provides the finite stopping bound. A true query
may stop at its first witness; a false query exhausts every candidate.

The component proof checks the outgoing arrow at every vertex of (1),
the absence of a terminal outgoing arrow, and that its incoming exposed
predecessors are exactly the preceding path vertices. These tests prove
full component closure. They include all annular atoms, even those
outside the selected three-source block.

#### Affine decisions and the new additive parameter

For each starting cutoff the existing verifier represents every queried
state as `a q+b`, with positive `a` and rational coefficients whose
denominators are powers of 3. Every comparison with an exposure bound,
source-band endpoint, or 1 is certified by its slope and value at `q=1`.
It therefore holds for **every real `q>=1`**. The original verifier used
a sufficiently strong integer congruence on `q` to preserve residues.
The present checker independently replaces that residue condition.

For `(h,D,K)=(2,5,5)` or `(3,7,7)`, put

\[
B=2^{\max(D+4,10)},\quad M=3^K,\quad T=BM.
\]

For each unit `U` modulo `3^(K-h)`, except the class in the theorem, choose

\[
X_0=B\left(\bigl((1+3^hU)B^{-1}\bmod M\bigr)+M\right).
\tag{3}
\]

Then `T<=X_0<2T`. On the arithmetic progression `X=X_0+jT`, `j>=0`,
set the real parameter `q=X/X_0`. Each state becomes

\[
a+b+j\Delta,\qquad \Delta=aT/X_0.
\]

For every registered chain or queried state, the checker proves:

1. `a+b` is an odd integer greater than 1, and `Delta` is an integer
   divisible by 6. Thus every state stays an odd positive integer and
   its residue modulo 3, which selects inverse branches, stays fixed.
2. Every band or height comparison remains true by the already proved
   affine inequalities. For a state inside a source band, the coefficient
   at its three possible residues `a+b+j Delta modulo18`, `j=0,1,2`, is
   identical. Since `6|Delta`, these three residues exhaust the orbit.
   Outside the source support, the coefficient remains zero by the
   affine bounds. Preserving the full residue modulo 18 is unnecessary
   when the coefficient is the same at all three residues.

These checks exhaust registered states: they consist of the chain,
the queried states, and generated predecessors immediately passed to
a query. The first excluded predecessor requires only its affine
inequality, not a residue or source test. True early exits retain their
original witness, and false decisions still enumerate every predecessor.
Therefore the complete finite decision proof remains valid on the
entire additive progression. This is an exact proof by reuse of its
finite decision tree with all arithmetic branches preserved.

Finally, any `X>=2T` satisfying the theorem's binary and ternary
conditions is in exactly the corresponding progression (3), because
`B` and `M` are coprime. Its index `j` is nonnegative since `X_0<2T`.
This gives the common thresholds

\[
2\cdot2^{10}\cdot3^5=497664,\qquad
2\cdot2^{11}\cdot3^7=8957952.
\]

The receipt records all 70 starting traces, their original compact
receipts, and hashes of their full query, comparison, and translation
tables. These tables are deterministically regenerated and rechecked.
Three numerical representatives per trace provide an additional check;
the infinite conclusion comes from the affine and residue proof above.

#### The exceptional classes really attach

Here `r=h` and `D=2h+1`. For `h=2,U=16 modulo27`, or
`h=3,U=31 modulo81`, the defining congruence is

\[
4^{h+1}U+2\equiv0\pmod{3^{h+1}}.
\tag{4}
\]

Set

\[
v=\frac{2^h(4^{h+1}U+2)}{3^h}-1
  =\lambda X-c,\quad
\lambda=4(8/9)^h,\quad c=\lambda+1-2(2/3)^h.
\]

For `h=2,3`, `9/4<lambda<27/8`, `c>1`, and the theorem's thresholds
give `y_2<v<y_3`. Thus `v` is a distinct top-band state. Equation (4)
makes `v` odd and `v=2 modulo3`. Every odd residue equal to 2 modulo3
has a nonzero coefficient in the top band: residues `5,11,17` have
coefficients `-1,-1,+2`. Hence `v` is an actual additional source.

Reversing from `y_1`, valuation 3 gives `4X-3`; the next `h` inverse
valuations 2 give `4^(h+1)U+1`; the next `h` inverse valuations 1 give
`v`. The intermediate states are odd integers by (4) and `3^h|X-1`.
Their forward valuations are therefore exactly

\[
(\underbrace{1,\ldots,1}_{h},
 \underbrace{2,\ldots,2}_{h},3).
\]

This length-`D` path from the source `v` to `y_1` is exposed in `G_D`.
The component cannot be (1). This argument holds for every member of
the exceptional class above the stated threshold; the three exceptional
representatives in the receipt are checks of that argument, not its
quantifier justification.

### 4. Coverage of the earlier two-phase construction

At fixed qualifying `h`, let `r` be the canonical parameter of the
earlier construction. Its modulus for `U` is `3^(r+4)`, with
`2*3^(r+3)` unit classes. The choices `V=47,155` give exactly two such
classes. Their difference has ternary valuation `r+3`: the difference
`155-47=108` has valuation 3, while the formula multiplies it by `3^r`
and ternary units. The classes are distinct modulo `3^(r+4)`.
Thus the construction covers the fraction

\[
\boxed{\quad 1/3^{r+3}\quad}
\]

of all admissible unit-`U` classes at that modulus. This is a congruence
class fraction, not a density of resolved full annular components.
For `h=r=2`, the two classes are `U=70,313 modulo729`, giving `2/486`.

The side-lane suggestion of this coverage question was reviewed at
commit `e5f2b80726a9612576c7c7cda624f12ffbd86775`. The later independent
scan at `f12da944dc68cfaff0884d874e11bc6c2cb98d34` was also reviewed;
neither feed is treated as a proof or an instruction source.

### 5. Separate finite scan: actual capacities and partial certificates

The checker also tests one explicitly specified representative of
**every** old-construction unit phase, using `B=2^20`,
`M=3^(h+r+4)`, and

\[
X=B\left(\bigl((1+3^hU)B^{-1}\bmod M\bigr)+M\right).
\]

These are finite representative results, not universal assertions about
the classes at this finer modulus:

| `h`, exposure | Representatives | Only the original three sources | Exactly one eligible negative unit | At least two eligible negative units |
|---|---:|---:|---:|---:|
| `2`, `D=5` | 486 | 459 | 17 | 10 |
| `3`, `D=7` | 1458 | 1431 | 16 | 11 |

An eligible negative source is an additional actual source whose
exposed forward path first joins one of `y_1,y_2,y_3`. Its usable
capacity is the magnitude of its actual negative coefficient. A source
joining only later on the chain is not counted for the zero-cost rule.

When there are at least two eligible units, choose exactly two, using
a partial negative coefficient if necessary. Start with the current
`-2 delta_(y_1)` and send the two selected negative units along their
actual forward paths to `y_3`. Every added current row is nonpositive.
The initial divergence is `-2 delta_(y_1)+2 delta_(y_2)`; the two paths
supply their selected negative sources and `+2 delta_(y_3)`. Thus the
result is an exact current for the original block plus selected negative
capacity. All positive source coefficients equal the original block;
every selected negative coefficient lies between its actual annular
coefficient and zero.

The receipt stores the complete component source table and the full
source/current/path rows of each of the **21** successful partial
certificates. Every current arrow is checked against both the exact
Syracuse map and the complete exposed graph. A separate flag states
whether the selected submeasure equals the whole component's source
measure. Positive mass in the remainder is retained; two negative
arrivals do not by themselves certify the whole component or annulus.

This placement argument validates the later side-lane scan's zero-cost
inference when its two units actually reach one of the first three
chain states. However, failure to find two units by a finite search
depth does **not** imply that every later cancellation needs positive
cost. Nor does insufficient negative capacity imply that no source
has re-entered the annulus. Those stronger readings are unsupported.

### 6. Reproduction and the remaining obligation

```sh
python3 experiments/residual_progress/release_coverage/check_coverage.py
```

The default checker rederives the exact proofs, compares the persisted
receipt, and regenerates all finite certificates. The recorded run took
about 0.6 seconds. Every numerical component search has caps of 2,000
vertices and 30,000 reachability queries; all finish. The largest
representative graphs used 41 vertices/141 queries at `h=2` and
90 vertices/467 queries at `h=3`. A capped computation raises an error;
it never becomes a positive or negative mathematical conclusion.
The symbolic query cap is also 30,000. No optimized Python mode is used.

**Refuted:** a phase-independent completion of the original block at
exposure `2h+1`, even for the single fixed depth `h=2` and even with all
annular sources and all inverse valuation words available.

**Open:** a phase-sensitive growing-depth rule that controls every
remaining positive component, preserves actual source capacity under
recursion, and proves termination. The exceptional classes may require
finer ternary information even to determine their finite component's
mass. This work establishes exact obstructions and selected finite
certificates, not that any phase is unfillable at all depths.

## Certificates

No certificate ran at this path before the B18 replay revival; the legacy checker imports the inverse oracle and the release checker from folders that moved and was evidence only until the B18 replay revival (below). Its symbolic verifier is the one certified (for the depth-32 family) by [`check_symbolic_lift.py`](../unbounded-exposure-depth-necessary/check_symbolic_lift.py). The command in the legacy text names `experiments/residual_progress/release_coverage/`.

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B18-replay-revival migration; standard library) replays the unmodified legacy check `check_coverage.py` in a temporary copy of the legacy layout built by `tools/legacy_replay.py`, requiring exit 0 and every file unchanged (about 13 s). It checks finite steps only; the status is unchanged.

## Remarks

- The side lane suggested this coverage question (feed reviewed at `e5f2b807`) and later scanned depth-16 backward attachments (`chain_cancellation_scan.py`, attached to [`delayed-release-cancellation`](../delayed-release-cancellation/README.md)); the main lane treated neither feed as proof. The scan's zero-cost inference is valid when its two units reach `y_1, y_2` or `y_3`; failure to find two units within a finite depth does not imply that later cancellation needs positive cost.
- A stronger restriction, with the ternary order fixed at 2 and every depth, is [`fixed-ternary-order-unbounded-depth`](../fixed-ternary-order-unbounded-depth/README.md).
- Novelty undetermined.

## History

- Migrated from `experiments/residual_progress/release_coverage/PHASE_COVERAGE.md` (legacy ID R19) at commit `be73a66`, by the B09 migration (Claude, Opus 5.5). Note, checker and receipt moved byte-identical. Legacy status: "written arithmetic proof with exact finite symbolic verification; the all-phase completion candidate is refuted".
- Main lane (ChatGPT, Codex), 2026-10-17, from commit `65093c4`. Its "independent model reviews" of the phase proof were the main lane's own agents; no review from another lane is on record.
