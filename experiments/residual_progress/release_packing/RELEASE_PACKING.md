# Two disjoint cancellation families exposed by the release analysis

2026-10-17. **Written elementary proof and executable universal partial
constructor.** The source is the six-band annulus A_N, for every positive
multiple of8. These currents do not certify the whole annulus. No novelty
or universal termination claim is made. All states are positive odd integers,
and 1 is absorbing.

The release analysis suggested retaining negative intermediate source
coefficients when moving a positive source backwards. An intermediate
ancestor can be larger than the positive source and still cancel it at zero
positive current cost. The following two families give explicit additional
capacity, independently of the subsequent future of their states.

## 1. A zero-cost pair

For every q with

    36N < q < 54N,    q = 31 modulo54,

put u=(4q-1)/3. Then u is odd, 48N<u<72N, and u=5 modulo18.
The original source coefficients are A_N(q)=2 and A_N(u)=-2.
Since 3u+1=4q, its exact Syracuse valuation is2 and S(u)=q. Thus

    2 delta_q - 2 delta_u = (I-P)(-2 delta_u).

Each pair removes two positive units with a nonpositive current. The
negative source u exceeds q; restricting all backward moves to smaller
individual ancestors would miss this cancellation. The larger signed
path-collapse construction explains it as part of an entire path.

## 2. A three-source chain

For every q with

    64N < q < 72N,    q = 31 or103 modulo108,

put u=(4q-1)/3 and v=(3q+1)/2. The exact arrows are

    u --valuation2--> q --valuation1--> v.

Here q is13 modulo18 in band4, u is5 or11 modulo18 in band5,
and v is11 modulo18 in band5. Explicitly A_N(u)=-1, A_N(q)=2,
and A_N(v)=-1, so

    -delta_u + 2 delta_q - delta_v = (I-P)(-delta_u + delta_q).

The current has positive cost1. In units of N, u lies in (256/3,96)
and v in (96,108). Integer parity resolves every affine endpoint offset:
all interval boundaries in the q conditions are even, while q is odd.

## 3. Source capacity, including the previous catalogue

Within each family, all affine maps are injective. The positive q sources
cannot equal a negative source because their actual annular signs differ.
The two kinds of negative triple sources occupy disjoint intervals.
Pair negative sources lie below72N and triple negative sources above
256N/3. The positive q intervals of the two families are disjoint.
Consequently all new source blocks are mutually disjoint.

They are also disjoint from the five short families and the two-class
five-source packing in the previous combined constructor:

- Every new positive q has residue13 in band4. None of the old positive
  source columns has that band and residue.
- Pair negative sources have residue5 in band4. None of the old negative
  source columns has that band and residue.
- Triple negative v sources have residue11 in (96N,108N). The old short
  catalogue's only negative band5 sources are the A-family middle points
  in (72N,96N). The five-source packing has only residue5 negative sources
  in band5.
- A triple negative u with residue5 cannot be an old short source in
  band5. When u has residue11, write q=103+108t, so u=137+144t. If it were
  an old A-family middle point, its predecessor would be
  (2u-1)/3=91+96t. Modulo72 this is19,43,or67, whereas the old A-family
  requires7 or55. Hence that collision is impossible.
- The only remaining comparison is a residue5 triple u against the old
  five-source negative top atom. The new u is41 modulo144; the old atom
  is13775+1152t, always95 modulo144. They are disjoint.

This proves full coefficient capacity for every N, rather than only for
the finite audit cutoffs. Current rows may overlap: linearity permits that,
and only reuse of source coefficients would require additional accounting.

## 4. Exact floor counts and the extended constructor

For a strict progression let

    C(N;a,b;r,m) = floor((bN-1-r)/m) - floor((aN-r)/m).

The number of pairs and triples is respectively

    P(N) = C(N;36,54;31,54),
    T(N) = C(N;64,72;31,108) + C(N;64,72;103,108).

Therefore P(N)=N/3+O(1), T(N)=4N/27+O(1), and these two families remove
exactly 2P(N)+2T(N)=26N/27+O(1) positive mass. Their positive current cost
is exactly T(N). These are bounded floor corrections; no absorption
assumption enters the counts. Under N→N+216 the counts increase by72 and32.

Let D(N) be the old short-catalogue removed positive mass and C_old(N) the
old five-source copy count. The extended constructor returns full integer
tables satisfying

    A_N = (I-P) J_ext,N + Z_ext,N,
    ||Z_ext,N^+|| = 99N/4 - D(N) - 3C_old(N) - 2P(N) - 2T(N),
    ||J_ext,N^+|| <= 3C_old(N) + T(N).

The total removed positive mass is 1073N/432+O(1), versus the previous
73N/48+O(1). The positive cost bound is73N/432+O(1). The remaining positive
mass is retained explicitly. The new constructor uses finite arithmetic
loops and the stored old affine identities; it performs no absorption search.

## 5. Reproduction

Run:

```sh
python3 experiments/residual_progress/release_packing/release_packing.py
```

The reusable entry point is `build_extended_partial_current(N)`, returning
the full current, exact residual, and summary. The default audit checks
every multiple of8 through1024, plus6144; it reconstructs every source,
checks disjoint capacity against the old constructor, verifies the full
divergence, and checks all27 boundary phases of the new floor counts.
The adjacent receipt records the finite cases. `--write-receipt` explicitly
regenerates it. The universal statements rely on the arithmetic and capacity
proof above, not on the finite range of the audit.
