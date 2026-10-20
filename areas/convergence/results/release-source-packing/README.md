---
id: release-source-packing
kind: result
title: Two further disjoint cancellation families raise the universal partial current's removed mass to 1073N/432 + O(1)
status: written
claim: >
  Odd-only 3x+1 map, absorbing at 1; A_N the six-band annulus, for every positive N divisible by 8. (Pair) For
  every q = 31 mod 54 with 36N < q < 54N and u = (4q-1)/3: S(u) = q with valuation 2, A_N(q) = 2, A_N(u) = -2,
  and 2 delta_q - 2 delta_u = (I - P)(-2 delta_u). (Triple) For every q = 31 or 103 mod 108 with
  64N < q < 72N, u = (4q-1)/3, v = (3q+1)/2: u -> q -> v with valuations 2, 1, coefficients -1, 2, -1, and
  -delta_u + 2 delta_q - delta_v = (I - P)(-delta_u + delta_q). All these blocks are pairwise disjoint and
  disjoint from the short-chain catalogue and the five-source packing of universal-annular-partial-current;
  with P(N) = N/3 + O(1) pairs and T(N) = 4N/27 + O(1) triples (exact floor counts) the extended constructor
  gives A_N = (I - P)J_ext + Z_ext with removed positive mass 1073N/432 + O(1) (previously 73N/48 + O(1)) and
  ||J_ext+||_1 <= 3C_old(N) + T(N) = 73N/432 + O(1). The remaining positive mass is returned, not handled; no
  simultaneous packing with delayed-release-cancellation is assumed.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [universal-annular-partial-current, affine-common-tail-tree-lifting, disjoint-annular-recursion]
evidence:
  - "release_packing.py, release_packing_audit.json: the legacy extended constructor build_extended_partial_current(N) and its audit (every multiple of 8 through 1024 and 6144: every source, disjoint capacity against the old constructor, full divergence, and all 27 boundary phases of the floor counts). Fails at its new path: it loads experiments/annular_construction/arithmetic/combined_partial_current.py by its pre-migration path (now ../universal-annular-partial-current/, which itself no longer runs). Passed at be73a66 as experiments/residual_progress/release_packing/release_packing.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran these steps before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a). The legacy transfer of annular-complement-outer-descent loads it by its old path"
  - "release_families_check.py, release_families_check.json: side-lane probe (Claude side lane, 2026-10-17): rebuilds both families from their statements with its own A_N. Fails at its new path: it imports affine_controls and progress_measures_audit from experiments/packet_currents/negative_controls/ by repository-relative path (now ../locally-collatz-like-control-barrier/). Passed at be73a66 as reviews/side_lane/release_families_check.py (archive/legacy-checker-run-be73a66.md, exit 0)"
  - "side_lane_review.json: the main lane's reproduction (at side-lane commit f2af9452) of release_families_check and depth_probe, with source hashes and outputs; a review of those side-lane probes, not of this result"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-17
    link: release_families_check.py
    scope: "Finite only (side-lane feed entry 2026-10-17 19:05, VERIFIED, main 65093c4): both families rebuilt from the statement; arrows, valuations and coefficients, the floor counts P(N), T(N) (increments 72 and 32 under N -> N + 216) and removed mass 2P + 2T, and no reuse within or across the two families, for every multiple of 8 up to 1024 and at 40 random cutoffs up to about 8 10^9. 'Disjointness from the older catalogue was not checked here. Main's written disjointness argument was not re-derived.' The status stays written"
aliases: [R16-b]
tags: [convergence, packet-currents, annular, partial-current, packing, constructive]
---

# Two further disjoint cancellation families raise the universal partial current's removed mass to 1073N/432 + O(1)

## Statement

For every positive `N` divisible by 8 (odd-only clock, absorbing at 1; `A_N` the six-band annulus of [`disjoint-annular-recursion`](../disjoint-annular-recursion/README.md)):

1. **Zero-cost pairs.** For every `q ≡ 31 (mod 54)` with `36N < q < 54N`, `u = (4q − 1)/3` is odd, `48N < u < 72N`, `u ≡ 5 (mod 18)`, `S(u) = q` with valuation 2, `A_N(q) = 2`, `A_N(u) = −2`, and `2δ_q − 2δ_u = (I − P)(−2δ_u)`.
2. **Triples.** For every `q ≡ 31` or `103 (mod 108)` with `64N < q < 72N`, `u = (4q − 1)/3`, `v = (3q + 1)/2`: `u → q → v` with valuations 2, 1; `A_N(u) = −1`, `A_N(q) = 2`, `A_N(v) = −1`; `−δ_u + 2δ_q − δ_v = (I − P)(−δ_u + δ_q)` (positive cost 1).
3. **Capacity.** All new blocks are mutually disjoint and disjoint from the short-chain catalogue and the two-class five-source packing of [`universal-annular-partial-current`](../universal-annular-partial-current/README.md) (proof in §3 below), for every `N`.
4. **Counts and the extended constructor.** `P(N) = C(N; 36, 54; 31, 54) = N/3 + O(1)`, `T(N) = C(N; 64, 72; 31, 108) + C(N; 64, 72; 103, 108) = 4N/27 + O(1)`; with `D(N)`, `C_old(N)` of the old constructor,

```
A_N = (I − P)J_ext,N + Z_ext,N,
‖Z_ext,N⁺‖₁ = 99N/4 − D(N) − 3C_old(N) − 2P(N) − 2T(N),
‖J_ext,N⁺‖₁ ≤ 3C_old(N) + T(N),
```

so the removed positive mass is `1073N/432 + O(1)` (previously `73N/48 + O(1)`) and the positive cost is at most `73N/432 + O(1)`. The remaining positive mass is retained explicitly.

A partial constructor: these currents do not certify the whole annulus, and no universal termination or novelty is claimed.

## Proof

The legacy note "Two disjoint cancellation families exposed by the release analysis" follows, lightly edited (headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

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

### 1. A zero-cost pair

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

### 2. A three-source chain

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

### 3. Source capacity, including the previous catalogue

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

### 4. Exact floor counts and the extended constructor

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

### 5. Reproduction

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

## Certificates

No certificate runs at this path; the legacy constructor and the side-lane probe load modules from folders that moved and are evidence only. The command in the legacy text names `experiments/residual_progress/release_packing/`. The new floor counts can be recomputed by hand from item 4; the base constructor's counts are certified in [`universal-annular-partial-current`](../universal-annular-partial-current/README.md) (`check_partial_current_recompute.py`).

## Remarks

- The pair is the actual annular instance of the intermediate-capacity normalizer of [`signed-path-collapse-capacity`](../signed-path-collapse-capacity/README.md): the negative source `u` exceeds `q`, so a rule restricted to smaller ancestors misses it.
- Of all this cancelled annular mass, only the old five-source copies cover remaining outer roots in the transfer of [`annular-complement-outer-descent`](../annular-complement-outer-descent/README.md); the pairs and triples add no root.
- The open target is unchanged: [`five-ray-annular-current-supply`](../../questions/five-ray-annular-current-supply.md).
- Novelty undetermined (none claimed).

## History

- Migrated from `experiments/residual_progress/release_packing/RELEASE_PACKING.md` (part of legacy R16; alias R16-b here) at commit `be73a66`, by the B09 migration (Claude, Opus 5.5). Note, constructor and receipt moved byte-identical, with the side-lane probe `reviews/side_lane/release_families_check.*` and the main lane's reproduction receipt `experiments/residual_progress/side_lane_review.json`. Legacy status: as R16, "written universal partial-current families".
- Main lane (ChatGPT, Codex), 2026-10-17. Its "independent model review" of the packing capacity was the main lane's own agents. The side lane's finite check is recorded under `reviewed_by`.
