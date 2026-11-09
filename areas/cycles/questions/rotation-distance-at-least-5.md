---
id: rotation-distance-at-least-5
kind: question
title: Can a rotation of a nontrivial 3x+1 cycle differ from it in exactly four positions?
status: open
claim: >
  Prove or refute: no nonidentity rotation of the valuation word of a hypothetical nontrivial primitive
  integer cycle of the raw odd-only 3x+1 map differs from it in exactly four positions, so that ρ(w) ≥ 5
  (given the same imports as ρ ≥ 4: the replayed gap EXT-1 and the period and minimum bounds).
created: 2026-10-19
tags: [cycles, rotation-distance, frontier]
---

# Can a rotation of a nontrivial 3x+1 cycle differ from it in exactly four positions?

## Question

Exclude rotations with exactly four mismatches for hypothetical nontrivial `q = 1` cycles of the raw odd-only `3x+1` map, giving `ρ(w) ≥ 5`, or exhibit a reason that the available methods cannot. This is a one-step improvement; the growing target is [`rotation-distance-growth`](rotation-distance-growth.md).

## Why it matters

It is the next constant after `ρ ≥ 4` ([`three-mismatch-exclusion`](../results/three-mismatch-exclusion/README.md), formal given EXT-1 for `m ≥ 2^19`, `L ≥ 2^20`). It was the legacy frontier's second target. The side lane paused it because the size method it was using cannot go beyond it.

## Known progress

- **2026-11-08: the minimum is close to the larger half defect.**
  The [minimum-window result](../results/half-defect-minimum-window/README.md)
  keeps the offset and the prefix/suffix valuation excesses in both
  remaining chronological orders. Under EXT-1, every minimum occurs
  fewer than `173N/1000` odd steps from the state immediately after
  the larger defect, with `N` the half-length. Its weighted inequality
  also restricts the remaining suffix; no half-period case is excluded
  by this additional necessary condition.

- **2026-11-08: the entire reduction to a half-period now needs only EXT-1.**
  The strengthened [non-half-period theorem](../results/non-half-period-four-mismatch-exclusion/README.md)
  excludes every four-mismatch shift of order at least three,
  using the coefficient `37/100` and margin `1/750` in both
  geometric order ranges. EXT-1 reduces the full odd period
  below `2^22`; exact gap bounds reduce it below `24000`.
  Complete local descent below `18000000` and five final geometric
  comparisons close every remaining period. No external convergence
  computation or period bound is imported. The half-period case
  remains open; the earlier two-input conclusions are retained below
  as research history.

- **2026-11-08: the minimum location and imbalance bounds now need only EXT-1.**
  The strengthened [imbalance result](../results/half-defect-imbalance-growth/README.md)
  replaces its original external period closure by a complete local
  computation. In canonical form `A B A[p] B[q]`, every minimum
  lies in first `A` when `p<q`, and in second `B[q]` when `p>q`.
  All cases require `|p-q|>N/8`; the latter order further requires
  `p-q>3N/4`. These statements include opposite-parity changes.
  When this refinement was first proved, the reduction from arbitrary
  shifts to the half-period still used Barina; the later strengthening
  above removes that separate input.

- **2026-11-08: a high-to-low terminal intercept must be small.**
  The [terminal-intercept exclusion](../results/half-defect-terminal-intercept-exclusion/README.md)
  uses EXT-1 alone to exclude every high-to-low Mersenne join with
  `chi=1-3^len(B)*z/(2^sum(B)*h)>=1/2`, at arbitrary levels and
  lengths. The remaining same-parity high-to-low branch has
  `0<chi<1/2`; the low-to-high order and opposite parity are separate.
- **2026-11-08: half-defect magnitudes must differ by more than one eighth of the half length.**
  The [imbalance law](../results/half-defect-imbalance-growth/README.md)
  proves `N<36 log_2(minimum)+7|p-q|` without external inputs,
  for half length `N` and defect magnitudes `p,q`. Under EXT-1,
  `|p-q|<=N/8` forces `N<2^22`; the separately declared Barina
  period input excludes that regime at every length. Both signs,
  both magnitude orders and opposite parity are covered, with no
  bound on the smaller magnitude. The larger-imbalance case remains open.
- **2026-11-08: equal half-defect magnitudes are excluded at every size.**
  The [equal-amplitude exclusion](../results/equal-amplitude-half-defect-exclusion/README.md)
  rules out denominator one for every pair of positive equal-length
  half-words differing at exactly two positions by the same absolute
  amount, with either sign pattern. It uses EXT-1 and a local exact
  descent replay, with no external convergence computation or bound
  on the amplitude. Combined with the non-half-period theorem, the
  remaining four-mismatch targets have unequal defect magnitudes.
  The [paired-state order theorem](../results/half-defect-positive-order-exclusion/README.md)
  independently excludes one ordering of those unequal defects
  without external inputs.
- **2026-11-08: only the half-period shift remains.**
  The [non-half-period exclusion](../results/non-half-period-four-mismatch-exclusion/README.md)
  uses the necessary one-track or two-track structure of the four
  mismatch positions to exclude every rotation order `3<=M<=18`.
  Together with the high-order theorem, EXT-1 forces `m<2^26`
  whenever a four-mismatch shift has order at least three.
  The separately declared Barina input leaves only `M=2`, hence
  `H=m/2` and even m. At most one four-mismatch shift can remain;
  unrestricted half-word changes keep the general question open.
- **2026-11-08: every remaining four-mismatch rotation has order at most eighteen.**
  The [high-order exclusion](../results/high-order-four-mismatch-exclusion/README.md)
  applies to every primitive cycle word, with no label, arc-placement
  or coprimality restriction. For a shift H of order
  `M=m/gcd(H,m)>18`, EXT-1 forces `m<2^26`; the separately declared
  Barina period bound excludes all lengths. Thus, under these inputs,
  all coprime shifts are settled and the remaining orders are
  `2<=M<=18`. The general question stays open.
- **2026-11-08: arbitrary mechanical edits have a uniform denominator law.**
  [`mechanical-edit-denominator-law`](../results/mechanical-edit-denominator-law/README.md)
  handles all mechanical totals and phases, with arbitrary signed
  replacements. It excludes at most two edits using only EXT-1,
  and at most ten with the separately declared convergence input.
  Under EXT-1, a hypothetical cycle of length `m>=2^32` also differs
  in more than `sqrt(m)` positions from every contracting mechanical
  word. Mechanical edit distance is not rotation distance; the
  general four-mismatch question remains open.
- **2026-11-08: common additive factors constrain signed endpoints.**
  [`odd-order-residue-signed-endpoint-divisibility`](../results/odd-order-residue-signed-endpoint-divisibility/README.md)
  proves that every prime-power component of a common addend whose
  residue orders of 2 and 3 are odd must divide the endpoint `h`
  of a signed `-h -> h` join. This applies to both Mersenne orders
  at arbitrary levels and lengths. In the endpoint-one,
  low-to-high `r=1` subclass, it excludes every level divisible
  by 11 or 25. Other endpoints and levels remain open here.
- **2026-11-08: one arbitrary change to a mechanical word is excluded.**
  [`one-edit-mechanical-denominator-growth`](../results/one-edit-mechanical-denominator-growth/README.md)
  proves an explicit denominator law for every primitive word differing
  in at most one position from a positive mechanical word, with arbitrary
  base total, phase and replacement. Under EXT-1, exact local finite
  checks exclude denominator 1 at every length. This includes the
  [prime four-mismatch family](../results/sparse-rotation-bounded-period-reduction-obstruction/README.md)
  whose bounded-period decomposition obstruction remains valid.
  General four-mismatch words need not have this form; the question
  remains open.
- **2026-11-08: a uniform endpoint-and-slope enclosure.**
  [`mersenne-join-state-enclosure`](../results/mersenne-join-state-enclosure/README.md)
  bounds the canonical normalized state for either interface sign
  in every unequal same-parity Mersenne normal form. A state lower
  bound gives an explicit necessary lower bound on the total
  segment slope; failure excludes denominator 1. Positive cycle
  insertions decrease the upper state bound. The result has no
  level or length restriction, but does not assert that every
  join lies in the excluded slope region.
- **2026-11-08: small signed endpoints are excluded at every amplitude.**
  [`small-mersenne-endpoint-exclusion`](../results/small-mersenne-endpoint-exclusion/README.md)
  proves the linked-segment affine test whenever `M>=7h+1`, where
  `M-1` is the first Mersenne addend and the signed endpoints are
  `-h,h`; a sharper quadratic condition is also proved. Both
  segment orders and arbitrary lengths and levels are covered,
  without external inputs. A denominator-one candidate must have
  `h>(M-1)/7`. This leaves the larger-endpoint region unresolved.
- **2026-11-08: bounded unequal half defects are excluded without external inputs.**
  [`bounded-unequal-half-defect-exclusion`](../results/bounded-unequal-half-defect-exclusion/README.md)
  excludes denominator 1 whenever the two half-defect magnitudes are
  unequal, have the same parity, and sum to at most 24, with arbitrary
  length, common letters, signs and positions. Complete signed state
  graphs reduce full plus-factor cancellation to 74 base joins;
  an affine convexity argument handles every cycle repetition.
  This gives an unconditional proof for this bounded-variation class,
  already excluded with the stronger imported mismatch bounds below.
  Larger amplitudes and the general four-mismatch question remain open.
- **2026-11-08: changes to any fixed expanding background must grow.**
  [`expanding-background-defect-growth`](../results/expanding-background-defect-growth/README.md)
  proves an explicit bound, under EXT-1, for arbitrary positive
  substitutions in repetitions of a fixed expanding word. It allows
  every phase and both increases and decreases, and gives effective
  finiteness at fixed substitution count. Its independently replayed
  four-increase `(2,1)` corollary subsumes the earlier lifted family;
  the node credits the stronger prior `(1,2)`-perturbation result.
  Sparse rotations need not admit a fixed background of this kind,
  so the general rotation-distance question remains open.
- **2026-11-08: a lifted four-arc class is excluded at every length.**
  [`lifted-four-arc-denominator-one-exclusion`](../results/lifted-four-arc-denominator-one-exclusion/README.md)
  excludes denominator 1 for the words obtained by replacing every
  letter `d` in `(1^(2r-4),a,1,c,1^(2r-2),c,1,b)` by `(2,d)`,
  for all `r>=2`, `a,b>=1`, `c>=2`. A nonzero resultant and the
  declared gap EXT-1 force at most 4,088 odd steps; a local exact
  descent and product certificate excludes those lengths. No
  near-critical or parity hypothesis is used. This specified track
  shape includes primitive near-critical four-mismatch words with
  unbounded shortcut local-minimum counts; arbitrary four-mismatch
  words remain outside the result.
- **2026-11-08: a general half-defect normal form.**
  [`two-half-defect-mersenne-normal-form`](../results/two-half-defect-mersenne-normal-form/README.md)
  parametrizes full plus-factor cancellation for every unequal same-parity
  pair of half-defect magnitudes by two linked signed odd-only segments
  with addends `2^J-1` and `2^r-1`. It includes both sign orders and gives
  an exact affine-state test sufficient to exclude denominator 1.
  That test is not proved uniformly; the general question remains open.
- **2026-11-08: amplitudes 2 and 4 are excluded at every length.**
  [`unequal-two-four-half-defect-classification`](../results/unequal-two-four-half-defect-classification/README.md)
  excludes positive integer `3x+1` cycles whose halves differ at
  exactly two positions with absolute changes 2 and 4, in any signs
  or order. Full plus-factor cancellation occurs in two explicit
  infinite families, but a uniform affine bound gives a rational
  state strictly between 0 and 1 in each. The exclusion uses no
  near-critical hypothesis or external bound. It covers only this
  half-period four-mismatch class; the general question remains open.
- **2026-11-08: an unconditional half-period subcase is excluded.**
  [`unequal-one-five-half-defect-classification`](../results/unequal-one-five-half-defect-classification/README.md)
  excludes positive integer `3x+1` cycles whose two halves differ at
  exactly two positions with absolute changes 1 and 5, in any signs
  or order, at every length. The proof classifies full plus-factor
  cancellation and shows that every exceptional word still has
  denominator greater than 1. It uses no near-critical assumption
  or external bound. This settles only that half-period four-mismatch
  class; the general question remains open.
- `ρ ≥ 4`: [`three-mismatch-exclusion`](../results/three-mismatch-exclusion/README.md).
- S8's claim that size arguments stop at three mismatches was withdrawn ([`four-mismatch-size-method-limit`](../attempts/four-mismatch-size-method-limit/README.md)): its words fail the rotation by `2h`.
- S10 ([`multi-rotation-four-mismatch-exclusion`](../attempts/multi-rotation-four-mismatch-exclusion/README.md)): in a continuous model of the aligned single-drop structure, both four-mismatch patterns are excluded by several rotations (`v₂ = v₄` by `h`, `2h`; `v₂ ≠ v₄` by `h, …, 12h`), but five and six mismatches survive; no exclusion is claimed, and exact certificates, finite `m`, the 2–2 case, the small-rotation branch and short arcs are missing.
- The sign structure of a four-mismatch rotation is formal: [`four-mismatch-sign-dichotomy`](../results/four-mismatch-sign-dichotomy.md).
- Conditional on EXT-1: a four-mismatch rotation needs `|h|_m ≥ 0.075m`, at most 156 such rotations exist at `m = 1.375·10^11` ([`short-rotation-mismatch-growth`](../results/short-rotation-mismatch-growth/README.md)), and it forces a letter `≥ 0.0220m`, so `ρ ≥ 5` holds for cycles with `m ≥ 1.375·10^11` whose letters are all below `0.022m` ([`largest-letter-rho-reduction`](../results/largest-letter-rho-reduction.md)).

## Suggested attacks

**2026-11-08: use the minimum window together with its suffix budget.**
The [weighted minimum-window inequality](../results/half-defect-minimum-window/README.md)
places the minimum near the start of the common arc after the larger
defect and charges twice for valuation excess after that minimum.
Retain those prefix/suffix quantities in the two exact block identities;
discarding them returns to the earlier coarse imbalance estimates.
A useful next result must exploit their integer structure or prove
that the weighted region still admits an exact obstruction. The
smaller defect, both chronological orders and opposite parity remain
unbounded targets.

**2026-11-08: combine the EXT-1-only reduction with the forced minimum arc.**
Every remaining four-mismatch shift is the half-period, under EXT-1
alone. In canonical form `A B A[p] B[q]`, retain the actual minimum
in first `A` for `p<q`, and in second `B[q]` for `p>q`.
The latter order requires `p-q>3N/4`; both require `|p-q|>N/8`.
The next target is a contradiction between that large terminal
division, the two retained affine block identities, and the positive
integer minimum. Keep opposite parity separate from signed Mersenne
joins. This is an open target, not a further exclusion.

**2026-11-08: retain the forced minimum arc and asymmetric imbalance.**
The [refined half-defect result](../results/half-defect-imbalance-growth/README.md)
leaves the minimum in the common arc immediately after the larger
defect. For `p>q` the imbalance exceeds `3N/4`; for `p<q` it
exceeds `N/8`, under EXT-1 alone. Use that placement together with
the full valuation budget, preserving the terminal division and
actual state order. The two chronological orders cannot be exchanged
by assuming a new double-increase normalization.

**2026-11-08: the remaining half defects have a large imbalance.**
Under the declared gap and period inputs, the
[new necessary bound](../results/half-defect-imbalance-growth/README.md)
leaves only `|p-q|>N/8`. Keep the state order from the
[paired-state result](../results/half-defect-positive-order-exclusion/README.md)
and the terminal division in the smaller copy of the second block.
The next target is to exploit the resulting large valuation jump,
without discarding the cancellation terms or assuming a preferred
ordering of the two positive defect magnitudes.

Within the same-parity high-to-low branch, retain the
[terminal intercept fraction](../results/half-defect-terminal-intercept-exclusion/README.md)
as well: `chi<1/2`, and the necessary length law is
`m<65*log2(1/(eta*chi))+90` for half length m and half-gap eta.
The next endpoint estimate must address this small-intercept region;
neither the low-to-high branch nor opposite parity follows from this law.

**2026-11-08: current target is unequal half-period defect magnitudes.**
The [all-amplitude theorem](../results/equal-amplitude-half-defect-exclusion/README.md)
settles equal magnitudes under EXT-1; the non-half-period reduction
uses EXT-1 plus Barina. For the remaining half-words, keep both
integer paired-difference equations. In the canonical double-increase
form, the [order constraint](../results/half-defect-positive-order-exclusion/README.md)
  forces the sign of the intermediate paired difference to follow
  the ordering of the two unequal magnitudes. The remaining cancellation
  cases need a new argument. The signed Mersenne normal form applies
to same-parity magnitudes; opposite-parity changes require a separate
integer analysis. Taking a quadratic norm alone adds no independent
congruence, as the order theorem explains. Earlier targets stay below
as research history.

**2026-11-08: current target is the unrestricted half-period case.**
The [non-half-period theorem](../results/non-half-period-four-mismatch-exclusion/README.md)
settles every other order under EXT-1 plus Barina. Write the
remaining word as `U V`, with equally long positive half-words
that differ at exactly two positions. Resolve the remaining
signed-endpoint and unequal-change arithmetic without adding
an unproved bound on the change sizes or normalizing away the
actual additive parameter. The geometric model genuinely admits
half-period controls, so the new certificate alone cannot close
this last case. Earlier dated directions are retained below.

**2026-11-08: current target is rotation orders two through eighteen.**
The [high-order theorem](../results/high-order-four-mismatch-exclusion/README.md)
supersedes the earlier coprime targets below under EXT-1 plus Barina.
For `g=gcd(H,m)`, examine the `g` tracks of length `M=m/g` with
`2<=M<=18`: four total mismatches allow only a small number of
nonconstant tracks, while `g` and the letters remain unbounded.
The balanced third-period branch is excluded by the existing
[denominator law](../results/balanced-third-period-denominator-law/README.md).
Unbalanced third-period changes, unrestricted half-period changes,
and the remaining small orders need additional arithmetic. At a
multiple of M the shift is the identity and the paired-state witness
vanishes, so simply testing more multiples does not close these cases.
Earlier dated directions below are retained as research history.

**2026-11-08: two singleton high arcs and a third-period subcase.**
The [two-singleton theorem](../results/two-singleton-high-arcs-exclusion/README.md)
excludes four-distinct-label coprime tracks whose two largest
labels each occur once, whether adjacent or opposite. Its
EXT-1-only core gives `m<=418657053<2^29`; the separately declared
Barina input closes every length. Binary words at every shift and
three-label coprime words were already covered by the results below.
The remaining coprime target therefore has a larger-label arc of
length at least two; noncoprime words with at least three labels
remain open.

Separately, the [balanced third-period denominator law](../results/balanced-third-period-denominator-law/README.md)
excludes denominator one unconditionally for every balanced
third-period change size. Unbalanced third-period defects remain
outside that subcase. These results do not settle the general question.

**2026-11-08: move to four distinct labels or noncoprime tracks.**
Under EXT-1 and the separately declared Barina convergence input,
the [three-label theorem](../results/three-label-four-mismatch-exclusion/README.md)
excludes every primitive three-label word with four mismatches at
a coprime shift and denominator one. Its EXT-1-only core gives
`m<=3501056435`, hence excludes `m>=2^32`. Together with the
[two-label theorem](../results/two-label-four-mismatch-exclusion/README.md),
this leaves only four distinct labels for a coprime four-mismatch
candidate: a coprime track with four mismatches has exactly four
constant arcs.

The new step closes the remaining separated-maximum geometries.
Single-arc oscillation bounds reduce them to four small
multiplicity pairs. Two pairs satisfy direct concentration bounds;
the other two contradict explicit end witnesses. Thus the earlier
overlap targets below are settled under the stated inputs, and
their original descriptions remain as history.

The next coprime target is a four-arc word with four distinct
labels, retaining both large-label contributions in its profile.
For noncoprime shifts, the two-label case is excluded, but words
with three or more labels still require coupling between tracks;
the inverse-complexity bound is only a necessary condition.
The general question remains open.

**2026-11-08: exclude clustered pairs of maximum arcs.**
The [clustered two-maximum-arcs theorem](../results/clustered-two-maximum-arcs-exclusion/README.md)
handles coprime-track shapes `V^a,A^b,V^c,B^d`, with positive
arc lengths, three distinct positive labels, and `V>max(A,B)`.
Write `r=a+c` and `u=min(h,m-h)/m`. When `ru<1`, its EXT-1-only
core excludes `m>=2^32`; the additional declared Barina input
closes every length. The proof aligns a minimum of the height
profile with an arc end and treats the three possible orders of
the four distinct boundaries. Its error must exceed `1/(104r)`.

When `r=2`, the condition `ru<1` is automatic for a coprime track
of this shape. The two-position argument gives the stronger
EXT-1-only cutoff `2^29` and a sharp relaxed threshold `1/208`.
The sharpness control is not an integer cycle.

Consequently, the separated-maximum target below can now require
`a+c>=3`, `u>=1/(a+c)`, and `b,d>=2` in `V^a,1^b,V^c,t^d`.
The next target is an obstruction for the remaining profile
orders, or an exact rational control showing that the current
end-witness inequalities are insufficient. Finite searches do
not settle that target. Four distinct labels and the remaining
noncoprime cases are still open.

**2026-11-08: retain two maximum arcs and the noncoprime block clock.**
The [two-label exclusion](../results/two-label-four-mismatch-exclusion/README.md)
settles every two-label case with at most four mismatches, at every
rotation and with EXT-1 as its sole external input. With EXT-1 and
the separately declared Barina input, the
[contiguous-maximum theorem](../results/contiguous-maximum-four-arc-exclusion/README.md)
also excludes all coprime-track shapes `V^d,A^a,B^b,A^c` with
positive arc lengths, three distinct positive labels, and
`V>max(A,B)`. Its large-period core
uses only EXT-1. These results narrow the previous targets below;
their original statements are retained as history.

For coprime four-mismatch tracks, the remaining shapes have four
distinct labels, or three labels with the maximum on the two
separate arcs of the repeated label. The earlier singleton theorem
already handles the latter shape when either nonrepeated-label
arc has length one. A concrete next target is therefore
`V^a,1^b,V^c,t^d`, with `V>t>=2`, `a,c>=1`, and `b,d>=2`.
The minimum's ones run bounds `t-1` logarithmically, and the
large-letter argument bounds `a+c` by 38 at the relevant periods.
Replacing the maximum letters by `t` leaves a binary track template
with discrepancy bounded by a quadratic in `log_2(m)`.
The missing step is an obstruction
for its maximum profile, now formed by two finite rotation segments.
The one-segment geometric proof does not supply that step.

For a noncoprime shift, put `g=gcd(h,m)`, `M=m/g`, and
`k=(h/g)^(-1) mod M`. The extended
[inverse-complexity theorem](../results/four-mismatch-inverse-continued-fraction-bound/README.md)
now gives `K(k/M)<27n+64log_2(L+1)/g` when `s(h)<=4`,
where `n<=2log_2(M)+1`. This is a necessary constraint, not an
exclusion; it can be automatic on short tracks. Beyond the
two-label case, the one-track four-boundary and two-track
two-boundary patterns still need arithmetic coupling between
tracks. Four distinct labels remain a separate coprime target.

**2026-11-08: move beyond singleton nonrepeated-label arcs.**
Under EXT-1 and the declared Barina convergence input, the
[general three-label theorem](../results/general-three-label-four-arc-exclusion/README.md)
excludes every coprime-track word `V,A^a,B^b,A^c` with positive
arc lengths and pairwise distinct positive labels, at every length.
This settles the `V>t>=3` target below; its earlier text is retained
as history. For coprime tracks, the remaining four-arc shapes have
four distinct labels, two alternating labels, or three labels with
both nonrepeated-label arcs of length at least two. Noncoprime
rotations also remain open. Every coprime four-mismatch candidate
now satisfies the
[logarithmic inverse-complexity bound](../results/four-mismatch-inverse-continued-fraction-bound/README.md),
`K(h^(-1)/m)<21942log_2(m)+11099` under EXT-1. The next task is
to combine that constraint with the arithmetic of these remaining
arc patterns; their exclusion is not supplied by the new theorem.

**2026-11-08: move beyond the two-level and background-maximum families.**
For the coprime track shape `V,A^a,B^b,A^c`, with
`a,b,c>=1` and pairwise distinct positive labels, the
[background-maximum theorem](../results/background-maximum-four-arc-exclusion/README.md)
excludes `max(A,B)>V`, and the
[rational-phase theorem](../results/two-level-four-arc-phase-exclusion/README.md)
excludes both arrangements with `{A,B}={1,2}` and `V>=3`.
These are all-length exclusions under EXT-1 plus the declared
Barina convergence input; their large-period cores use only EXT-1.
Within this shape, the product bound `E<8m/5` forces
`min(A,B)=1`: otherwise `E>=2m-1` contradicts that bound
at the imported minimum period. Thus the remaining target is
`V>t>=3` over background `{1,t}`, with either outer label.
Retain the full inverse rational phase and the exact integer
ones-run divisibility when treating its expanding and contracting
short blocks; no uniform contradiction for those blocks is proved
here. Other four-mismatch patterns and noncoprime tracks remain
open. This supersedes the finite-interval target immediately below,
whose earlier text is retained as history.

**2026-11-08: couple short multiples with the two-rotation geometry.**
For the specified coprime track pattern `V,1^a,2^b,1^c`,
with `a,b,c>=1` and `V>=3`, the
[inverse-complexity theorem and corollary](../results/four-mismatch-inverse-continued-fraction-bound/README.md)
leave only `m<2^1536` under EXT-1. If `m>=2^22`, the
[two-level four-arc theorem](../results/sparse-two-level-four-arc-exclusion/README.md)
also requires `b>m/128` and `K(h^(-1)/m)>m/512`.
For `m>=2^34`, the new arithmetic bridge supplies a multiple
`jh` with cyclic distance `Q` and `jQ<=512`. The next target
is a structural contradiction combining this short multiple
with the two-rotation geometry; no exhaustive search through
the enormous finite interval is proposed. Other track patterns
and the general four-mismatch question remain open.

**2026-11-08: focus on positive interfaces with `r>=257`.**
Under LMN, the [negative-interface theorem](../results/negative-interface-mersenne-exclusion/README.md)
excludes both orders at every level. Together with the
[positive-interface theorem](../results/positive-interface-mersenne-exclusion/README.md),
this excludes all normal-form candidates with `r<=256`.
Remaining candidates have positive interface, `r>=257`, and
`8r>5J` in low-to-high order or `32r>J` in high-to-low order.
Under the same LMN input, the
[first-segment exclusion](../results/one-defect-first-block-mersenne-exclusion/README.md)
also requires at least two letters greater than 1 in the first
signed segment `A` of every remaining low-to-high candidate.
These results supersede the narrower normal-form targets below;
the earlier text is retained as history. They do not settle
other defect classes or general four-mismatch rotations.

**2026-11-08: retain at least three exceptions in the low-to-high first segment.**
With the additional declared Chim estimate for two `3`-adic
logarithms and Barina convergence input, the
[two-exception theorem](../results/two-defect-first-block-mersenne-exclusion/README.md)
excludes denominator-one candidates arising from positive-interface
low-to-high Mersenne joins whose first segment `A` has at most
two letters greater than 1, with arbitrary positions, sizes,
endpoints, levels and second segment.
Remaining candidates under these three inputs therefore need
at least three such letters. The sole-LMN statement above still
requires only two; the stronger conclusion uses the additional
sources. An iteration must retain the exact congruences at each
exception, since controlling the final short state alone does
not bound all earlier intermediate states.

**2026-11-08: move to the other order or higher low levels.** The
[unit-low-level theorem](../results/unit-low-level-mersenne-exclusion/README.md)
settles all low-to-high `r=1` denominator-one candidates under
LMN, including `g>h` and contracting first prefixes. This
supersedes the remaining-case targets for that subclass below;
their earlier text is retained as history. The signed auxiliary
joins are not themselves ruled out. The next normal-form targets
are high-to-low order and low-to-high `r>=2`; arbitrary
four-mismatch rotations still need additional structure.

**2026-11-08: isolate the remaining negative interfaces.** Under LMN
alone, the
[expanding-prefix exclusion](../results/expanding-negative-prefix-mersenne-exclusion/README.md)
removes low-to-high `r=1` joins `-h -> -g -> h` with `g<=h`
and expanding first slope, including every closed negative prefix
at every endpoint. Remaining low-to-high `r=1` candidates must
have `g>h` or a contracting first slope; slope 1 is impossible.
The other segment order, other `r` and the full four-mismatch
question remain outside this result.

**2026-11-08: move beyond closed negative prefixes.** Under EXT-1,
the [closed-prefix denominator law](../results/closed-negative-prefix-mersenne-denominator-law/README.md)
excludes denominator one for low-to-high `r=1` joins whose first
segment closes at `-h` with `h<=91`, including the endpoint-one
case. Within this normal-form subclass, remaining denominator-one
work must use a nonclosed first segment or `h>91`. The theorem
does not settle existence of the auxiliary signed returns.

**2026-11-08: retain residue restrictions on the endpoint.** Apply
the [common-addend divisibility condition](../results/odd-order-residue-signed-endpoint-divisibility/README.md)
before estimating a Mersenne join. For endpoint-one low-to-high
`r=1`, the first segment fixes `-1`; the remaining return under
`3x+(2^J-1)` is still unresolved at odd levels not removed by
the odd-order residue obstruction. A finite return search does
not settle those unbounded levels.

**2026-11-08: retain both the endpoint and total slope.** The
[state enclosure](../results/mersenne-join-state-enclosure/README.md)
covers negative as well as positive interfaces. Combine its
necessary slope threshold with the small-endpoint exclusion;
the remaining normal-form candidates must satisfy both. Moving
the cut to the other defect produces a mixed-sign auxiliary
description, so a second positive-addend bound needs justification.

**2026-11-08: the remaining endpoint region.** The
[uniform endpoint bound](../results/small-mersenne-endpoint-exclusion/README.md)
settles every normal-form join with `M>=7h+1`, independently of
the Mersenne levels. Focus on larger signed endpoints, including
paths whose first negative-to-positive crossing is delayed; the
bound does not assert that these cases fail.

**2026-11-08: separate transients from repeatable cycles.** The
[bounded-amplitude theorem](../results/bounded-unequal-half-defect-exclusion/README.md)
settles the linked-segment affine test for `2<=J<=12`, all `1<=r<J`,
at every word length. Its loop convexity argument reduces arbitrary
positive cycle insertions to base values and fixed-point limits.
The remaining unbounded-amplitude target is to control crossing
graphs and transient paths uniformly, or find another integrality
obstruction. Equal magnitudes, opposite parities and other shifts
require their corresponding scoped arguments.

**2026-11-08: linked signed segments.** For unequal same-parity half
defects, use the [Mersenne normal form](../results/two-half-defect-mersenne-normal-form/README.md)
to seek a uniform bound `F_u(1)<2^s+h`, or an integrality obstruction
that does not require this bound. Both the high boundary valuations
and the common signed endpoints must be retained. This is a target,
not a consequence already supplied by the parametrization.

From the legacy S10 §6 and frontier, marked as proposals: exact Farkas certificates per linear cell (one rotation with a uniform margin per region), the finite-`m` threshold against `ℓ* ≈ 342·log₂ m + 172`, the `(1, 1, 2)` window theorem (queued in the Lean lane), the `(2, 2, 0)` case and the small-rotation branch, and the `v₂ ≠ v₄` pattern with the slope cost of its letters `≥ 3`. Alternatively, a letter bound below `0.022m` ([`largest-letter-sublinear`](largest-letter-sublinear.md)).

## History

- 2026-11-08: added the shared weighted minimum-window inequality
  and its `173N/1000` location consequence under EXT-1. Kept the
  already recoverable total-excess corollary subordinate to the new
  offset/suffix information. This is a further necessary condition;
  the half-period case and general question remain `open`
  (Codex root research lane, GPT-6; directed by Santiago Armstrong).

- 2026-11-08: strengthened the complete non-half-period exclusion
  to EXT-1 alone, with sharper exact geometry, a full-period gap
  bootstrap, and internally checked finite descent. Updated the
  current research target without deleting the earlier two-input
  conclusions. The general four-mismatch question remains `open`
  (Codex root research lane, GPT-6; directed by Santiago Armstrong).

- 2026-11-08: strengthened the half-defect imbalance result with
  the forced minimum arc and the `p>q` cone. Its all-length closure
  now uses EXT-1 and complete internal finite checks, without Barina.
  The original weaker two-input statement is retained below as
  dated history; the general question remains `open`.

- 2026-11-08: added the high-to-low terminal-intercept restriction under
  EXT-1, preserving the larger-imbalance target and separate low-to-high
  and opposite-parity branches. The general question remains `open`
  (Codex cycle research lane, GPT-6 Astra; directed by Santiago Armstrong).

- 2026-11-08: added the unconditional minimum-versus-imbalance law
  and its all-length `|p-q|<=N/8` exclusion under EXT-1 plus Barina.
  The remaining target has larger imbalance; earlier dated scope
  statements are retained and the general question remains `open`.
- 2026-11-08: excluded equal half-defect magnitudes at every amplitude
  under EXT-1 and added the unconditional paired-state order constraint
  for unequal changes. The current target is unequal half-period
  changes; the general question remains open (Codex root research
  lane, GPT-6; directed by Santiago Armstrong).
- 2026-11-08: recorded the complete exclusion of rotation orders
  at least three for four mismatches, conditional on EXT-1 plus
  Barina, and narrowed the current question to unrestricted
  half-word changes. The half-period case and the question stay
  open (Codex root research lane, GPT-6; directed by Santiago Armstrong).
- 2026-11-08: recorded the general high-order exclusion and replaced
  the current coprime target by the finite list of rotation orders
  two through eighteen, conditional on EXT-1 and Barina. Preserved
  all earlier claims and dated directions; the question stays open
  (Codex root research lane, GPT-6; directed by Santiago Armstrong).
- 2026-11-08: recorded the all-placement two-singleton-high
  exclusion with its EXT-1-only `2^29` cutoff and separate Barina
  all-length corollary, plus the unconditional exclusion of every
  balanced third-period change size. Retained the previous frontier as
  history; the general question remains open (Codex four-arc
  research lane, GPT-6 Astra; directed by Santiago Armstrong).

- 2026-11-08: recorded the full three-label coprime four-mismatch
  exclusion under EXT-1 plus Barina, with an EXT-1-only `2^32`
  cutoff. The next targets are four distinct labels on a coprime
  track and noncoprime words with at least three labels. Earlier
  overlap targets are retained as history; the general question
  remains open (Codex main research lane, GPT-6 Astra;
  directed by Santiago Armstrong).

- 2026-11-08: recorded the clustered two-maximum-arcs exclusion
  with its EXT-1-only `2^32` cutoff and the sharper `2^29`
  two-isolated-maxima corollary. The next separated-maximum target
  has at least three maximum letters and `u>=1/(a+c)`; earlier
  targets remain as history. The general question remains open
  (Codex main research lane, GPT-6 Astra; directed by Santiago Armstrong).

- 2026-11-08: recorded the two-label exclusion for every rotation
  under EXT-1, the contiguous-maximum three-label exclusion under
  EXT-1 plus Barina, and the inverse-complexity bound with the
  noncoprime block clock. Identified two separated maximum arcs,
  four distinct labels, and the remaining noncoprime patterns as
  the next targets. Earlier targets remain as history; the general
  question remains open (Codex main research lane, GPT-6 Astra;
  directed by Santiago Armstrong).

- 2026-11-08: recorded the three-label singleton nonrepeated-label arc exclusion
  under EXT-1 plus Barina and the logarithmic inverse-complexity
  theorem for every coprime four-mismatch rotation. The remaining
  arc patterns above replace the narrower `V>t>=3` target, whose
  original statement is preserved. The general question remains
  open (Codex main research lane, GPT-6 Astra; directed by Santiago
  Armstrong).

- 2026-11-08: recorded the all-length background-maximum and
  both-arrangement two-level exclusions under EXT-1 plus Barina,
  and the remaining `V>t>=3` target within that specific track
  shape. Also recorded the two-exception first-segment exclusion
  under LMN, Chim and Barina without strengthening the sole-LMN
  claim. Earlier targets are retained above; the general question
  remains open (Codex main research lane, GPT-6 Astra; directed
  by Santiago Armstrong).

- 2026-11-08: recorded the inverse-continued-fraction bridge
  and the specified two-level track family's cutoff `2^1536`
  under EXT-1, with the short-multiple geometry target above.
  The general question remains open (Codex signed-endpoint
  research lane, GPT-6 Astra; directed by Santiago Armstrong).

- 2026-11-08: combined the all-level negative-interface exclusion
  with the positive-interface low-level and level-ratio exclusions,
  leaving the stated larger positive-interface regions under LMN.
  The general question remains open (Codex signed-endpoint research
  lane, GPT-6 Astra; directed by Santiago Armstrong).

- 2026-11-08: added the all-length
  [`unit-low-level-mersenne-exclusion`](../results/unit-low-level-mersenne-exclusion/README.md)
  and clarified that the remaining low-to-high `r=1` targets
  are now covered under LMN. Other orders and levels remain
  open, as does the general question (Codex cycle research lane,
  GPT-6 Astra; directed by Santiago Armstrong).
- 2026-11-08: separated the remaining `r=1` interfaces after the
  all-endpoint expanding-prefix exclusion under LMN alone;
  retained the earlier `h<=91` result with its sole-EXT-1 input
  (Codex signed-endpoint research lane, GPT-6 Astra;
  directed by Santiago Armstrong).

- 2026-11-08: refined the low-to-high `r=1` target after the
  closed-negative-prefix exclusion for `h<=91` under EXT-1.
  Auxiliary signed-return existence and the general question
  remain open (Codex closed-prefix research lane, GPT-6 Astra;
  directed by Santiago Armstrong).

- 2026-11-08: added the uniform mechanical-edit denominator bounds,
  with distinct inputs for the two-edit and ten-edit exclusions and
  the contracting-background square-root restriction. The general
  question remains `open` (Codex four-arc research lane, GPT-6 Astra;
  directed by Santiago Armstrong).
- 2026-11-08: added the all-length residue constraint on signed
  endpoints and its infinite level exclusions for the endpoint-one
  subclass. The general question remains `open` (Codex cycle
  research lane, GPT-6 Astra; directed by Santiago Armstrong).
- 2026-11-08: added the one-edit mechanical denominator law and its
  arithmetic exclusion of the prime four-mismatch coverage family,
  conditional only on EXT-1. The general question remains `open`
  (Codex four-arc research lane, GPT-6 Astra; directed by Santiago Armstrong).
- 2026-11-08: added the uniform Mersenne state enclosure and the
  combined endpoint-and-slope target. The general question remains
  `open` (Codex cycle research lane, GPT-6 Astra; directed by
  Santiago Armstrong).
- 2026-11-08: added the uniform small-endpoint criterion and its
  remaining larger-endpoint target. The general question remains
  `open` (Codex cycle research lane, GPT-6 Astra; directed by
  Santiago Armstrong).
- 2026-11-08: added the unconditional bounded unequal half-defect
  exclusion and the transient-versus-loop research target. The
  general question remains `open` (Codex cycle research lane,
  GPT-6 Astra; directed by Santiago Armstrong).
- 2026-11-08: added the fixed expanding-background substitution
  bound and the independently checked weaker instance of the
  known `(1,2)` perturbation exclusion. The general question stays
  `open` (Codex four-arc research lane, GPT-6 Astra;
  directed by Santiago Armstrong).
- 2026-11-08: added the lifted four-arc denominator-one exclusion,
  conditional only on the declared gap EXT-1, with a locally replayed
  finite length exclusion. The general question remains `open`
  (Codex four-arc research lane, GPT-6 Astra; directed by Santiago Armstrong).
- 2026-11-08: added the general signed-Mersenne half-defect normal form
  and its unresolved affine-state target; the question remains `open`
  (Codex cycle research lane, GPT-6 Astra; directed by Santiago Armstrong).
- 2026-11-08: added the unconditional amplitudes-2-and-4 half-period
  exclusion from [`unequal-two-four-half-defect-classification`](../results/unequal-two-four-half-defect-classification/README.md).
  The arbitrary four-mismatch question remains `open`
  (Codex cycle research lane, GPT-6 Astra; directed by Santiago Armstrong).
- 2026-11-08: added the unconditional amplitudes-1-and-5 half-period
  exclusion from [`unequal-one-five-half-defect-classification`](../results/unequal-one-five-half-defect-classification/README.md).
  The arbitrary four-mismatch question remains `open`
  (Codex cycle research lane, GPT-6 Astra; directed by Santiago Armstrong).
- 2026-11-08: narrowed the remaining low-to-high positive-interface
  target under LMN to first segments with at least two non-one
  letters, using the first-segment exclusion above. The general
  four-mismatch question remains `open`.
