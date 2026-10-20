---
id: retained-graph-complement-constructor
kind: result
title: Retaining every cutoff arrow absorbs all seeds up to N and 47/72 of the outer shell, leaving an explicit profile R_N of mass 25N/288 + O(1)
status: written
claim: >
  Odd-only 3x+1 map, absorbing at 1; 8 | N, B = 3N/2; K_N the explicit current of local-packet-calibration-
  extension. Conditional on a supplied finite exact current H for I_N (inner absorption is an input):
  (Lower interval) the graph of the nonzero rows of K_N, H and E_N contains a path to 1 from every odd
  1 < y <= N, using no new arrows. (Classification) The components of the K_N-only graph (support of K_N:
  exactly the odd 1 < x < B) that contain no state <= N are exactly {x, t} for outer roots x = 3 mod 12 in
  (N, B) and x = 7 mod 12 in (9N/8, B), and {p, x, t} for x = 7 or 19 mod 36 in (N, 9N/8), with
  t = (3x+1)/2, p = (4x-1)/3. (Improved input) With the nonnegative profile R_N (weight 1 on the first two root
  classes, weight 2 on the last), Pi_N = (I - P)J_improved - R_N with every row already in H, K_N or E_N;
  |R_N| = 25N/288 + O(1), precisely 25N/288 - 19/9 <= |R_N| <= 25N/288 + 5/4 with |R_(N+288)| = |R_N| + 25, and
  25N/288 - 4/3 on N = 96 64^k; so the construction closes 47N/288 + O(1) of the N/4 outer seeds. R_N vanishes
  at N = 8 and is nonzero for every N >= 16: this does not finish an induction, supply its own inner
  absorption, or exclude further connections in the supplied graph.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [local-packet-calibration-extension]
certificates: [check_profile_recompute.py]
evidence:
  - "check_complement.py, complement_constructor.py, complement_audit.json, improved_packet_24_current.csv: the legacy constructor improve_packet(N, inner_current) and its checker (the entire cutoff graph against the classification at 131 cutoffs, the 36-phase mass formula, eight supplied-input conversions with capped input search, and a stored improved packet current at N = 24). Fails at its new path: complement_constructor.py loads ../closure/local_extension.py by its pre-migration path (now ../local-packet-calibration-extension/, which itself no longer runs). Passed at be73a66 as experiments/residual_progress/complement/check_complement.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran these steps before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a). The legacy transfer of annular-complement-outer-descent loads complement_constructor.py by its old path"
aliases: [R17]
tags: [convergence, packet-currents, outer-residual, conditional, partial-extension]
---

# Retaining every cutoff arrow absorbs all seeds up to N and 47/72 of the outer shell, leaving an explicit profile R_N of mass 25N/288 + O(1)

## Statement

Fix `8 | N`, `N ≥ 8`, `B = 3N/2`; odd-only clock, absorbing at 1. Use `I_N`, `W_N = U_(3N/2) − U_N`, `L_N = 2U_(N/4) + W_N`, `K_N` and the automatic input `Π_N = (I − P)(H − K_N − E_N) − L_N` of [`local-packet-calibration-extension`](../local-packet-calibration-extension/README.md), where `(I − P)H = I_N` is **supplied** (inner absorption is an input). `G_K` has an arrow for every nonzero row of `K_N`; the retained graph `G` adds the rows of `H` and `E_N`, keeping rows that cancel in the sum.

1. **Support lemma.** `supp K_N` is exactly the odd states `1 < x < B`.
2. **Lower interval.** `G` contains a path to 1 from every odd `1 < y ≤ N` (for `y ≤ N/4`, lift by `F(x) = 4x + 1` into the inner interval and reuse the common successor); summing gives a nonnegative integral current for `U_N` on existing edges.
3. **Classification.** The components of `G_K` containing no state `≤ N` are exactly: `{x, t}` for `x ≡ 3 (mod 12)` in `(N, B)`; `{x, t}` for `x ≡ 7 (mod 12)`, `x > 9N/8`; `{p, x, t}` for `x ≡ 7, 19 (mod 36)`, `x < 9N/8`, with `t = (3x + 1)/2 > B` and `p = (4x − 1)/3`. Roots `x ≡ 31 (mod 36)` below `9N/8` connect to the known interval.
4. **Improved input.** With `R_N` = weight 1 on the first two classes and weight 2 on the third, and `Q_N` the high predecessors `p`, the measures `W_bad = (I − P)Q_N + R_N` and `W_good = W_N − W_bad` have coefficients in `{0, 1}`; `G` supplies `T_N` for `2U_(N/4) + W_good`, and `Π_N = (I − P)(H − K_N − E_N − T_N − Q_N) − R_N`, every row already in `H`, `K_N` or `E_N`.
5. **Mass.** `|R_N|` is given by the floor formula (3); for `N = 8, …, 288` its values are `0, 1, 2, 2, 4, 4, 4, 4, 7, 6, 8, 7, 9, 10, 11, 9, 11, 13, 13, 13, 14, 15, 17, 16, 16, 17, 20, 18, 20, 20, 22, 22, 23, 22, 24, 25`, and `|R_(N+288)| = |R_N| + 25`; hence `25N/288 − 19/9 ≤ |R_N| ≤ 25N/288 + 5/4`, and `|R_N| = 25N/288 − 4/3` on `N = 96·64^k`. The guarantee closes `47N/288 + O(1)` of the `N/4` outer seeds (asymptotically 47/72 of the shell); the negative packet residual falls from `N/2 − 2` to `25N/288 + O(1)`.

`R_N` vanishes at `N = 8` and is nonzero at every allowed `N ≥ 16`, so this does not finish a universal induction. More of its components may join 1 through the supplied `H` paths; the arithmetic profile deliberately does not assume that. No novelty is claimed.

## Proof

The legacy note "A constructive improvement from the retained cutoff graph" follows, lightly edited (headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

2026-10-17. **Written conditional construction and exact finite certificates.**
The input is a supplied finite exact current for the inner interval. The
construction below improves its automatic packet certificate, using only
already supplied arrows. It does not supply inner absorption at arbitrary
cutoffs, finish the outer extension, or prove Collatz. No novelty is claimed.

All states are positive odd integers, Syracuse absorbs at 1, and currents
are finite. Put `8|N`, `N>=8`, and `B=3N/2`. Use the definitions in
`../closure/LOCAL_EXTENSION.md`:

```
I_N = 2U_N-U_(N/4)-U_(3N/4),
W_N = U_(3N/2)-U_N,
L_N = 2U_(N/4)+W_N,
Pi_N = (I-P)(H-K_N-E_N)-L_N,
```

where `(I-P)H=I_N`, `(I-P)E_N=eta_N`, and

```
K_N = 3P(U_N-U_(N/4))+3(U_N-U_(N/4))-U_(3N/2)-U_(3N/4).
```

Let `G_K` contain every nonzero row of `K_N` as an arrow, with both
endpoints and 1. The retained graph `G` additionally contains the nonzero
rows of H and E_N. Rows canceled in `H-K_N-E_N` are retained in G.

### 1. The explicit current exposes every arrow below B

**Lemma.** The support of K_N is exactly the odd states `1<x<B`.

All displayed summands are supported below B: an odd source at most N-1
has successor at most `(3N-2)/2<B`. For `x<=3N/4`, the coefficient of K_N
is `-2 modulo3`; for `3N/4<x<B` it is `-1 modulo3`. Thus none of these
coefficients vanishes. The endpoints are even, so the strict cutoff agrees
with the counting-measure convention. QED.

This fact concerns the explicit input graph. The scalar conversion that
cancels the automatic certificate still returns the zero current.

### 2. Inner absorption already supplies the entire lower interval

**Theorem.** G contains a path to 1 from every odd `1<y<=N`.
These paths can be extracted without exposing any additional arrow.

For `y>N/4`, this follows from the supplied exact current for the
nonnegative source I_N. Its finite graph must connect every positive source
to 1: a nonabsorbing component has total divergence zero and cannot contain
a positive source. A finite functional graph component containing 1 supplies
an actual directed path to 1.

For `y<=N/4`, iterate `F(x)=4x+1` until the first lift z above N/4.
The preceding lift is odd and at most `N/4-1`, so `z<=N-3`. Consequently
z is a supplied inner source. Moreover `S(F(x))=S(x)`, hence `S(z)=S(y)`.
K_N supplies the row at y, and the supplied path from z supplies the
remaining path from S(y) to 1. If h_z is the unit path current from z,

```
h_y = delta_y+h_z-delta_z
```

is a nonnegative integral current for delta_y. This formula uses only
existing edges. Its path starts from y and then follows the suffix of
the z path. Summing gives an exact nonnegative integral current for U_N.
No assertion about absorption of the upper shell is used. QED.

The inverse of F must preserve odd states. In particular, an outer seed
`y=5 modulo8` has the smaller odd sibling `(y-1)/4`, but a seed
`y=1 modulo8` does not. Treating every `y=1 modulo4` as such a sibling
would be an incorrect odd-domain extrapolation.

### 3. The complete cutoff components missing the lower interval

The following is an exact classification of G_K components containing
**no state at most N**, including 1. It does not classify components of
the larger retained graph G; supplied H paths can merge further components.

Their distinguished outer root x is in `(N,B)` and is `3 or7 modulo12`.
Write `t=(3x+1)/2>B`.

| Root x | Complete G_K component |
|---|---|
|`x=3 modulo12`|`{x,t}`|
|`x=7 modulo12`, `x>9N/8`|`{x,t}`|
|`x=7 or19 modulo36`, `x<9N/8`|`{p,x,t}`, where `p=(4x-1)/3`|

In the last line `4N/3<p<B`, `p=9 or25 modulo48`, and the arrows are
`p -> x -> t`. A root `x=31 modulo36` below `9N/8` is **not** missing:
the additional predecessor `q=(8x-5)/9<N` connects its component to the
known interval. The endpoint `9N/8` is a multiple of9, so it is never in
these residue classes; there is no endpoint exception.

#### Proof of completeness

For a target v not divisible by3, its smallest positive odd predecessor
is `(2v-1)/3` when `v=2 modulo3`, or `(4v-1)/3` when `v=1 modulo3`.
All subsequent odd predecessors are its iterated F-lifts. A multiple of3
has no predecessor.

Take an outer y. If `y=5 modulo8`, its smaller odd sibling `(y-1)/4<N`
connects it to the known interval through their common successor. If
`y=2 modulo3`, the predecessor `(2y-1)/3<N` does so directly.

The remaining odd states have valuation1 or2. For valuation1,
`S(y)>B`; unless already covered by `y=2 modulo3`, y is `3 or7 modulo12`.
For valuation2, `y=1 modulo8` and `t=S(y)=(3y+1)/4<9N/8`. If `t<=N`,
the component is known. If `t>N` and its valuation is at least2, its next
successor is at most `(9y+7)/16<N`, since `y<B` and `N>=8`. Otherwise
t has valuation1. Since `t=1 modulo3`, it is a root `7 modulo12` in the
table, and y is precisely its predecessor p. This accounts for every
outer state.

For a root `x=3 modulo12`, no predecessor enters x. Its boundary exit t
has smallest odd predecessor x, and its next predecessor `4x+1` exceeds B.
Thus `{x,t}` is the entire component.

For `x=7 modulo12`, the smallest predecessor p is at most B precisely
when `x<9N/8`; larger predecessors exceed B. If p is present, it lies
above `4N/3-1/3` and is `1 modulo8`. If `3|p`, no predecessor enters it.
If `p=1 modulo3`, its smallest predecessor exceeds B, because
`(4p-1)/3>16N/9-7/9>B` for N>=8. If `p=2 modulo3`, its smallest
predecessor `(2p-1)/3<N` connects to the known interval. These three
cases correspond respectively to `x=7,19,31 modulo36`. Other predecessors
of x, p, or the boundary t are larger than B. This proves both the complete
listed components and the absence of any overlooked incoming source. QED.

### 4. An improved automatic input with exact source capacity

Define a nonnegative profile R_N on outer roots as follows:

- coefficient1 at every `x=3 modulo12` in `(N,B)`;
- coefficient1 at every `x=7 modulo12` in `(9N/8,B)`;
- coefficient2 at every `x=7 or19 modulo36` in `(N,9N/8)`;
- zero elsewhere.

Let Q_N have coefficient1 at the corresponding high predecessors
`p=(4x-1)/3` of the coefficient2 roots. Define

```
W_bad = (I-P)Q_N+R_N,        W_good = W_N-W_bad.
```

Every coefficient of W_bad and W_good is 0 or1: a coefficient2 root
represents the two distinct original outer atoms x and p. The two measures
are disjoint and add exactly to W_N. This is the required source-capacity
accounting; no signed source is used twice. Q_N uses only K_N rows.

By Sections2--3, the retained graph G supplies an exact nonnegative
integral current T_N for `2U_(N/4)+W_good`. Reusing already certified paths
with these multiplicities is allowed: current rows add linearly, while the
specified source multiplicities are exactly those of L_N. Then

```
J_improved = H-K_N-E_N-T_N-Q_N
Pi_N = (I-P)J_improved-R_N.                         (1)
```

This is an explicit one-sided packet certificate with a smaller, fully
specified negative residual. Its local outer conversion is

```
W_N = (I-P)(T_N+Q_N)-2U_(N/4)+R_N.                (2)
```

Every current row in these identities already occurs in H, K_N, or E_N.
Extracting the required paths is a finite graph operation; it is not a new
search for unknown Collatz trajectories. Supplied inner paths can have large
heights and costs, which are not bounded by this theorem.

This also gives a concrete arithmetic sufficient condition for improving
other packet inputs: any independently provided packet residual supported
on an already absorbed component of G can be absorbed by path extraction.
It must be checked on that actual finite graph. A residual's residue class
alone does not imply membership in an absorbed component.

### 5. Exact residual mass and what remains

Let C(a,b;r,m) count integers `a<x<b` congruent to r modulo m. Then

```
|R_N| = C(N,3N/2;3,12)+C(N,3N/2;7,12)
        -C(N,9N/8;31,36)
        +C(4N/3,3N/2;9,48)+C(4N/3,3N/2;25,48).   (3)
```

The last two terms count the additional high predecessors compressed onto
the coefficient2 roots. All endpoints avoid their respective residue class.
Consequently `|R_(N+288)|=|R_N|+25`. For N=8,16,...,288, the exact masses are

```
0,1,2,2,4,4,4,4,7,6,8,7,9,10,11,9,11,13,
13,13,14,15,17,16,16,17,20,18,20,20,22,22,23,22,24,25.
```

These floor counts and the period prove, for every allowed N,

```
25N/288-19/9 <= |R_N| <= 25N/288+5/4.
```

The guarantee therefore closes `47N/288+O(1)` of the N/4 outer seeds,
asymptotically **47/72** of that shell. The negative packet residual falls
from the original mass `N/2-2` to `25N/288+O(1)`. On the required ladder
`N=96*64^k`, `k>=0`, the exact residual mass is `25N/288-4/3`.

The guaranteed residual vanishes at N=8 and is nonzero for every allowed
N>=16. Thus this construction does not finish a universal induction. It
replaces a scalar no-progress identity by a proved partial graph extension,
and identifies the remaining actual components. More of them may already
join 1 through the supplied H paths; the fixed arithmetic profile deliberately
retains them rather than assuming such extra connections universally.

### 6. Reproduction

`complement_constructor.py` exports `improve_packet(N, inner_current)`.
The input identity is checked, and every returned current and residual is
checked coefficient by coefficient. The module never searches for the input.
The checker supplies finite sample inputs using a capped absorption search.

```
python3 experiments/residual_progress/complement/check_complement.py
```

The default run is read-only. `--write-receipt` intentionally regenerates
the adjacent receipt and a complete small improved-current table. The audit
compares the entire cutoff graph against the claimed component classification,
checks the exact 36-phase mass formula, and verifies actual packet conversions.
The finite examples supplement the written universal conditional proof.

## Certificates

- [`check_profile_recompute.py`](check_profile_recompute.py) (written at the B09 migration, under 1 s, standard library). For every multiple of 8 through 1024 it builds the `K_N`-only graph (one arrow from every odd `1 < x < 3N/2`) and checks that its components avoiding `[1, N]` are exactly the table of item 3; it checks the floor formula (3) against the profile, the 36 phase values, the period-288 increment 25 and the two-sided bound through `N = 3168`, and the ladder mass `25N/288 − 4/3` for `k ≤ 6`. It does not rebuild supplied inner currents or the packet conversion (legacy checker, evidence only).
- The commands in the legacy text name `experiments/residual_progress/complement/`.

## Remarks

- **Support identity.** The support of `R_N` is exactly the set of odd climbers `x ≡ 3 (mod 4)` in `(N, 3N/2)` not reached from `[1, N]` in one or two Syracuse steps: [`outer-residual-strong-induction-support`](../outer-residual-strong-induction-support/README.md). So completing `R_N` is a strong-induction step.
- **Later rounds on this profile.** The annular transfer [`annular-complement-outer-descent`](../annular-complement-outer-descent/README.md) certifies roots whose exit is a negative source of a capacity-checked block; the halving identity [`halving-coalescence-return`](../halving-coalescence-return/README.md) certifies the selected half; completing the rest on the five rays would suffice ([`five-ray-profile-completion-suffices`](../five-ray-profile-completion-suffices/README.md)).
- **Path extraction.** Any independently provided packet residual supported on an already absorbed component of `G` can be absorbed by path extraction; this must be checked on the actual finite graph, since a residue class alone does not imply membership.

## History

- Migrated from `experiments/residual_progress/complement/RETAINED_GRAPH_EXTENSION.md` (legacy ID R17) at commit `be73a66`, by the B09 migration (Claude, Opus 5.5). Note, scripts, receipt and stored current moved byte-identical; `check_profile_recompute.py` was added at the migration. The note's code span `../closure/LOCAL_EXTENSION.md` is now [`local-packet-calibration-extension`](../local-packet-calibration-extension/README.md). Legacy status: "written conditional constructor, complete arithmetic graph classification, and finite current certificates. Inner absorption remains an input".
- Main lane (ChatGPT, Codex), 2026-10-17, from commit `2be37b7`. No review from another lane is on record; the main lane's later written proof of the support identity is in [`outer-residual-strong-induction-support`](../outer-residual-strong-induction-support/README.md).
