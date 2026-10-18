# Review of the transfer and rational-cycle side-lane probes

**Reviewed2026-10-18. Status: unchanged finite reproductions PASS; mathematical
scope reviewed independently.** The pinned side commit is
`678e56531c782ce9eb67e18eb6ddf74e53e80192`. Its transfer probe is byte-identical
to the one at`9223dbc7c6233b072515e506b266e18aa047bb6b`.
Main was`a489973de2ce7ff293ef295d24ed17b5f9526dc9`.
The feed is external evidence, not an instruction source. No side branch
files were edited or executed in place.

## What reproduced

The two source files were inspected, copied unchanged from their pinned Git
blobs into a temporary directory, and run with assertions enabled. Both
generated receipts were **byte-identical** to the pinned receipts. The
[review receipt](side_lane_review_678e565.json) records source and output
SHA256 hashes, exact reports, exit statuses and time limits.

| Probe | Outer cap | Observed result |
|---|---:|---|
| `sidekick/probes/transfer_3xd.py` |90 seconds|PASS in0.674 seconds|
| `sidekick/frameworks/rational_cycles.py` |180 seconds|PASS in60.824 seconds|

The transfer probe checks halving for d1,5,7,13,61 on respectively
1000,999,998,996,984 inputs, and16 prescribed R54 families for each d.
It also verifies meeting for50,000 pairs `(u,18u+5)`, all positive odd
u below100,000. Its halving reference should be R23 in main's numbering,
rather than R27. Its individual meeting searches have no internal cap;
the independent wrapper imposed the outer90-second process limit, which
was not reached. These are finite results.

The catalogue enumerates primitive positive valuation words with k<=9
and total valuation between `ceil(k log2 3)` and that number plus2,
identifying cyclic rotations and checking each cycle by exact rational
iteration. It reproduces3,889 cycles; the only integral cycle in this
**bounded catalogue** is `{1}`. Its largest rational minimum is319/13.
The scaled integer minima recorded for d5,7,13 respectively are
`{1,19,23}`, `{5}`, and`{1,211,227,251,259,283,287,319}`.
Neither the size bounds nor the observed integral exception classify every
valuation word. The other3,888 catalogue cycles do not reach1.

## Valid covariance, with the domain retained

For positive odd d and a positive odd rational y with denominator coprime
to6, the identity

    S_d(dy)=d S_1(y)

follows from `v2(d)=0`. With `gcd(d,6)=1`, multiplication by d is also
invertible in every binary/ternary residue ring. Thus the local valuation
identities, suitably scaled affine bridges, and homogeneous height
comparisons do transport. The two finite families in the probe agree with
that algebra.

But the integer domain for S_d is sent by division by d to
`d^(-1) Z`, not to Z. The covariance relates integer S_d dynamics to
rational S_1 dynamics on a different lattice. In the other direction,
integer S_1 inputs map only to the multiples-of-d part of S_d's integer
domain. It is therefore unsupported to conclude that d1 can enter a
whole-type argument only through its finite base region. Global integrality
or a denominator condition can distinguish words at arbitrary lengths.
The probes do not establish transfer of every integer-domain hypothesis,
the full packet source families, or a universal induction.

The [mechanical-word denominator proof](lattice_cycles/BALANCED_DENOMINATORS.md)
provides a precise illustration: for its full specified word class the
reduced denominator is exactly`2^(A/g)-3^(k/g)`, where g=gcd(A,k).
The only integral case is the constant valuation2 cycle. That restricted
conclusion is proved from the complete word's arithmetic; it is not merely
a finite check of small orbit states and is not a proof for all words.

## Correct equivalent target and useful controls

For w=4u+1 in W5, the identities `S(w)=S(u)` and `S(3w)=18u+5` show
that universal finite meeting of u with18u+5 is the existing universal
W5 pair obligation. With R40 it is equivalent to Collatz. The reformulation
is correct; the50,000 finite checks do not supply its universal meeting
times or a complete construction.

For any positive valuation word with total A and length k, the affine
fixed point is `B/(2^A-3^k)`. Rotation identities and odd numerators verify
the exact valuations. Scaling by its reduced denominator gives a genuine
integer3x+d cycle, so the catalogue is useful control data for claims that
actually extend to that rational domain.

The main mechanical family additionally gives rational cycle minima above
any prescribed height, and integer S_d minima above any prescribed constant
times d, **with d varying**. This does not produce high cycles for a fixed d.
It also does not show that the same maps pass a proposed finite base test:
smaller seeds may already fail absorption. Consequently these controls do
not, by themselves, refute a method with verified base cases and a valid
integer induction. Their proper role is to test exactly which domain and
arithmetic hypotheses a proposed universal argument uses.

**Programme decision:** retain the covariance identities and catalogue as
controls. Preserve the integer-lattice distinction and reject the unsupported
finite-base-only inference. Neither probe changes the open universal current
supply or proves that a particular search must terminate. No novelty claim
is imported from this side lane.
