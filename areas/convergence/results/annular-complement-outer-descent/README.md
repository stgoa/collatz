---
id: annular-complement-outer-descent
kind: result
title: A capacity-checked annular block certifies its negative atoms and the outer roots whose exits they are, with explicit unbounded-excursion descents
status: written
claim: >
  Odd-only 3x+1 map, absorbing at 1; 8 | M, N = 64M; A_M the six-band annulus; R_N the residual profile of
  retained-graph-complement-constructor. Conditional on a supplied finite exact current H for U_N (known
  absorption through N is an input): (Lemma) every positive atom of A_M has an explicit odd ancestor <= N
  within two steps, so its path to 1 is already in the graph of H. (Transfer) For any supplied integer block
  P - Q = (I - Push)J with disjoint P, Q >= 0, P <= A_M+, Q <= A_M-, Q = (I - Push)(H_P - J) certifies every
  atom of Q; every root x of R_N has exit t = (3x+1)/2 in (3N/2, 9N/4), t = 5 or 11 mod 18, A_M(t) = -1, and
  whenever Q(t) > 0 the root's entire coefficient (1 or 2) is certified, giving Pi_N = (I - P)(J_0 - T) -
  R_remaining. (Coverage) The existing catalogue covers exactly the C_old(M) = N/9216 + O(1) roots
  9183 + 768j, far below |R_N| = 25N/288 + O(1). (Descents) For every delayed-release family the root
  t = (2v-1)/3 has R_N(t) = 1 and an exact first descent to N - 1 by the word (1^(r+1), 2^h, 3), of length
  h + r + 2 <= 2h + 2, all intermediate states above N and peak above (4/3)^h N; an example at h = r = 3,
  N = 36473856 certifies a coefficient-2 root 40480795 in ten arrows. Universal coverage of R_N, or a
  decreasing parameter for its unhandled roots, is not proved.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [retained-graph-complement-constructor, delayed-release-cancellation, universal-annular-partial-current, release-source-packing, affine-common-tail-tree-lifting]
certificates: [check_legacy_replay.py]
evidence:
  - "check_transfer.py, transfer.py, transfer_audit.json, outer_9183_current.csv: the legacy constructor and checker (positive-source ancestor formulas and exact catalogue coverage at M = 8, 16, ..., 512, 768, 6144: 353280 positive atoms, 164 matched roots; five actual transfers at M = 8, 96, 168, 384, 768 with capped supplied lower absorption; 170 symbolic descent branches for qualifying 2 <= h <= 32 and both congruences, including the coefficient-2 example; about 3 s) and the stored 61-row current for delta_9183 that upgrades the N = 6144 packet residual by one unit. Fails at its new path: transfer.py loads ../complement/complement_constructor.py, ../release_packing/release_packing.py and ../release/check_release.py by their pre-migration paths (now ../retained-graph-complement-constructor/, ../release-source-packing/, ../delayed-release-cancellation/). Passed at be73a66 as experiments/residual_progress/complement_recursion/check_transfer.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran these steps before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a). The legacy constructor of halving-coalescence-return loads transfer.py by its old path. Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
aliases: [R20]
tags: [convergence, packet-currents, outer-residual, transfer, conditional, constructive]
---

# A capacity-checked annular block certifies its negative atoms and the outer roots whose exits they are, with explicit unbounded-excursion descents

## Statement

Fix `8 | M`, `N = 64M` (odd-only clock, absorbing at 1). A finite exact current `H` for `U_N` is **supplied** (it can itself be extracted from the inner-interval current by [`retained-graph-complement-constructor`](../retained-graph-complement-constructor/README.md)); no absorption above `N` is assumed. `Push` is the killed Syracuse pushforward; `R_N` is the residual profile of that node.

1. **Lemma.** Every positive atom of `A_M` has an explicit odd ancestor `≤ N` at distance at most two (residues 11, 17 via `(2y − 1)/3`; residue 13 via `(8y − 5)/9 → (4y − 1)/3 → y`; band-5 residue 17 via `(4y − 5)/9 → (2y − 1)/3 → y`), so its whole path to 1 is already in the nonzero-row graph of `H`.
2. **Transfer.** For a supplied integer block `μ = P − Q = (I − Push)J` with `P, Q ≥ 0` on disjoint states, `P ≤ A_M⁺`, `Q ≤ A_M⁻`, the graph of `H` supplies `H_P` with `(I − Push)H_P = P`, so `Q = (I − Push)(H_P − J)` and the graph of `H_P − J` contains actual paths to 1 from every atom of `Q` (no cycle hypothesis is needed: a finite weak component without 1 carries zero divergence). Every root `x` of `R_N` has exit `t = (3x + 1)/2 ∈ (3N/2, 9N/4)`, `t ≡ 5` or `11 (mod 18)`, `A_M(t) = −1`; whenever `Q(t) > 0`, appending `x → t` certifies the **entire** coefficient `R_N(x)` (1 or 2; a certified path may be reused with multiplicity 2 without reusing annular capacity). Then `R_N = (I − Push)T + R_remaining`, `R_remaining ≥ 0`, and `Π_N = (I − P)(J_0 − T) − R_remaining`.
3. **Exact coverage of the existing catalogue.** The old five-source packing's negative top atoms `t = 13775 + 1152j` (`j = 9s` or `9s + 3`) give exactly the roots `x = 9183 + 768j`, `R_N(x) = 1`, so `C_old(M) = M/144 + O(1) = N/9216 + O(1)` roots; the other catalogue families, the release pairs and the release triples add none.
4. **Shrinking branches.** For every delayed-release family ([`delayed-release-cancellation`](../delayed-release-cancellation/README.md)) at annular cutoff `M = 3X/128`, `N = 3X/2`: the root `t = (2v − 1)/3` satisfies `9N/8 < t < 3N/2`, `t ≡ 31 (mod 36)`, `R_N(t) = 1`, and has the exact first descent `t → ⋯ → N − 1` with word `(1^(r+1), 2^h, 3)`, length `h + r + 2 ≤ 2h + 2`, all intermediate states above `N`, peak above `(4/3)^h N`. When `M` is on `96·64^k`, `N` is on the next rung. At `h = r = 3`, `V = 155`, `X = 24315904`, `N = 36473856`, the root `40480795` has `R_N = 2` and a ten-arrow first descent to `36473855`.

A constructive transfer and infinitely many nontrivial branches; it does not close the residual family or prove Collatz. No novelty is claimed.

## Proof

The legacy note "Turning annular cancellation into a recursive complement reduction" follows, lightly edited (headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

2026-10-17. **Written conditional transfer theorem and explicit shrinking
branches.** The known absorption input is only the odd seeds at most N.
These results do not close the whole residual family or prove Collatz.
No novelty is claimed. All clocks are odd-only Syracuse with absorption at1.

### 1. Every positive annular source is already certified at the inner scale

Fix `8|M`, and set `N=64M`. Let A_M be the actual six-band annulus.
Suppose a finite exact current H for U_N is supplied. This input can itself
be extracted from the inner-interval current by R17's retained-graph theorem.

**Lemma.** Every positive atom of A_M has an explicit odd ancestor at
most N, at distance at most two. Its entire path to1 is consequently
already present in the nonzero-row graph of H.

Atoms at most N need no ancestor construction. The remaining positive
atoms in band4 lie in `(N,9N/8)` and have residues11,13,17 modulo18.
For residues11 or17, the predecessor `(2y-1)/3<N` works. For residue13,
the two-arrow chain is

```
(8y-5)/9 -> (4y-1)/3 -> y,
```

with valuations1,2, and first state below N. In band5, the only positive
residue is17 modulo18, with coefficient2. For `9N/8<y<9N/4`, use

```
(4y-5)/9 -> (2y-1)/3 -> y,
```

with valuations1,1; again the first state is below N. All displayed states
are positive odd integers, and exact valuations follow from their odd
successors. In a finite functional graph, an exact current with nonnegative
source U_N forces actual directed paths from its sources to1. Those paths
must include the displayed descendants. QED.

This lemma is stronger than a bound on the raw positive-source height:
positive annular sources up to `9N/4` are certified from ancestors below N.
It imposes no absorption assumption on the negative sources.

### 2. Transfer any capacity-checked partial annular current

Suppose a finite integer block

```
mu = P-Q = (I-Push)J,          P,Q >= 0,
```

is supplied, where P and Q use disjoint states, `P<=A_M^+`, and
`Q<=A_M^-` coefficientwise. These are the exact source-capacity hypotheses.
The symbol Push is the killed Syracuse pushforward; P here denotes the
positive source measure only.

By Section1, the graph of H supplies an exact nonnegative integral current
H_P for P. Therefore

```
Q = (I-Push)(H_P-J).                                  (1)
```

The current H_P-J may have either sign. Since its source Q is nonnegative,
its nonzero-row graph supplies actual absorption paths for every atom of Q.
Those paths can be extracted by a finite graph algorithm without exposing
new arrows.

No hypothesis excluding Collatz cycles is needed here. In every finite weak
component that does not contain1, the divergence of any finite signed current
sums to zero, including when the component has a directed cycle. Such a
component cannot carry positive Q mass. A finite functional component that
does contain1 has1 as its unique terminal state, so its vertices follow
directed paths to1. Possible unrelated components with zero Q mass are
irrelevant. This is a finite graph consequence of (1), not an assumption
about globally invariant orbit classes.

Now let R_N be the exact R17 residual. Each root x in its support is3 or7
modulo12, so

```
t=(3x+1)/2 in (3N/2,9N/4),
t=5 or11 modulo18,           A_M(t)=-1.                 (2)
```

Whenever Q(t)>0, append the already explicit cutoff arrow `x->t` to the
path certified by (1). It gives an exact nonnegative current for
`R_N(x) delta_x`. Summing over all such roots gives

```
R_N = (I-Push)T + R_remaining,                         (3)
R_remaining >= 0,
```

where the removed coefficient at each covered root is its **entire**
R_N coefficient, either1 or2. Certifying absorption of a state once allows
its path current to be multiplied by2; this does not use an annular source
coefficient twice. The annular capacity was spent once in mu, while (1)
has supplied a reusable path certificate. Source multiplicities in (3)
are retained exactly.

Thus an improved packet identity `Pi_N=div J_0-R_N` becomes

```
Pi_N = div(J_0-T)-R_remaining.                         (4)
```

Only known absorption through N, a finite arithmetic annular block at the
smaller cutoff M=N/64, and the existing cutoff arrows are inputs. This is
a constructive transfer, not an assumption that all annular blocks or all
their negative atoms are certifiable. Full closure would follow if supplied
blocks covered every exit in (2); that coverage is presently unproved.

### 3. Exact coverage of the existing combined catalogue

This transfer identifies precisely which parts of the current catalogue
help R_N. It does not infer coverage from the amount of annular mass removed.

The old five-source packing has negative top atom

```
t=13775+1152j,     j=9s or9s+3,
```

for its admissible copy indices. Its corresponding complement root is

```
x=(2t-1)/3=9183+768j.                                 (5)
```

This root is3 modulo12 and lies in `(9N/8,3N/2)`, so R_N(x)=1.
For example, for j=9s, the maximum admissible M is `120+96s`, and
`t-108M>=815`; the other class has maximum `152+96s` and gives the same
bound. The upper inequality `t<144M` is part of the existing capacity
proof. Distinct copies give distinct roots. Thus all C_old(M) copies
provide C_old(M) new outer absorption certificates.

The other old negative sources are below96M, so their valuation-one
predecessors are below N. The new short release-packing pair is below72M
and likewise adds no root. A release triple's higher negative atom is
`t=(3q+1)/2`, with `64M<q<72M` and `q=31 or103 modulo108`. Its root q
is31 modulo36 in `(N,9N/8)`, where R_N is already zero. Its other negative
atom lies below96M. Consequently the extended catalogue's coverage of
R_N is **exactly** C_old(M), rather than a quantity proportional to all
the annular mass that catalogue removes.

The previous exact floor formulas give

```
C_old(M)=M/144+O(1)=N/9216+O(1).
```

This is positive reusable coverage, but far smaller than the remaining
mass `25N/288+O(1)`. It is not a complete recursive closure.

### 4. A genuinely shrinking branch with arbitrarily large intermediate height

The general delayed-release construction provides a second transfer with
unbounded path length. Use its parameters h,r,X at annular cutoff
`M=3X/128`, and put `N=64M=3X/2`. The notation in
`../release/DELAYED_RELEASE.md` gives

```
v -> ... -> y_1=N-1       with valuation word 1^r,2^h,3,
t=(2v-1)/3 -> v           with valuation1.
```

Its proved band inequalities give

```
9N/8 < t < 3N/2,        t=31 modulo36,        R_N(t)=1.
```

Therefore this is an actual unresolved R17 root, not a root already
absorbed by the earlier arithmetic profile. It has the explicit first
descent

```
t -> ... -> N-1,         word 1^(r+1),2^h,3.            (6)
```

All intermediate states after t are greater than N. This follows from
the delayed-release proof: v exceeds108M, all later intermediate states
exceed144M, and the endpoint is64M-1. Hence (6) reaches the known interval
for the first time after exactly `h+r+2<=2h+2` arrows. Appending the
supplied path from N-1 to1 gives an exact current for delta_t. Its unknown
seed has strictly decreased to the supplied range; no absorption above N
has been assumed.

The path reaches

```
w_h=4(4/3)^h(X-1)+1 > (4/3)^h N
```

for X>=2. Thus these shrinking branches have unbounded intermediate
height relative to N, despite their exact arithmetic construction. This
explains why a recursive scheme must permit such excursions rather than
impose a universal height ceiling. This is a statement about the specified
first-descent paths, not a universal cost bound for other current searches.

There are unbounded qualifying h, and infinitely many valid X for each.
When M is on the required ladder `96*64^k`, the complement cutoff N lies
on the next rung `96*64^(k+1)`. Thus (6) is a family of shrinking branches
on the programme's actual residual scales. The already proved parameter
congruences are reused; no claim is made for nonqualifying parameters or
for every root of R_N.

#### A coefficient2 branch, checked with its full multiplicity

The other negative source u may also have a remaining root
`x=(2u-1)/3`, followed by `x->u->t->v->...->N-1`. Its R_N coefficient
can be0,1,or2, so it must be evaluated rather than assumed. For the exact
parameters

```
h=r=3, V=155, X=24315904, N=36473856,
X=46765 modulo59049, 1024 divides X,
```

the root is `x=40480795`, and R_N(x)=2. Its ten-arrow first descent is

```
40480795 -> 60721193 -> 45540895 -> 68311343 -> 102467015
 -> 153700523 -> 230550785 -> 172913089 -> 129684817
 -> 97263613 -> 36473855.
```

Putting current2 on each of the ten arrow origins gives divergence
`2delta_40480795-2delta_36473855`, exactly. The endpoint is N-1 and every
earlier state exceeds N. The receipt stores the full current. This removes
two actual residual units using a certified path; it does not duplicate
the single annular coefficient at u.

### 5. What a complete recursion must still supply

The transfer separates three tasks that were previously easy to conflate:

1. Prove a current identity for an actual annular submeasure, with capacity.
2. Determine whether its negative atoms cover the **exits of remaining
   complement roots**, rather than already absorbed states.
3. Supply enough such identities to cover every remaining root, or give
   another explicit shrinking branch for it.

The first two now have an executable exact interface, and Section4 supplies
an infinite collection of nontrivial branches for the third. Universal
coverage, or a proved decreasing parameter for the unhandled roots, remains
open. Ordinary finite successful searches are not a termination proof.

### 6. Reproduction

```
python3 experiments/residual_progress/complement_recursion/check_transfer.py
```

The default checker is read-only. It checks the positive-source ancestor
formulas and exact catalogue coverage at finite M, constructs actual currents
using capped supplied lower-range absorption, and verifies symbolic delayed
branches without enumerating their enormous cutoff intervals. The adjacent
receipt records the ranges and hashes. `--write-receipt` intentionally
regenerates it.

The persisted audit checks all M=8,16,...,512, plus768 and6144: 353280
positive annular atoms, including125663 above the supplied lower cutoff,
and164 exactly matched catalogue roots. Five actual transfers use
M=8,96,168,384,768; the M=96 example stores a61-row current for delta9183
and checks the full packet update at N=6144. There are170 symbolic shrinking
branches for qualifying2<=h<=32 and both congruence choices, including
the full coefficient2 example above. The default checker takes about3 seconds
in the development environment; no runtime bound is part of the theorem.

## Certificates

No certificate ran at this path before the B18 replay revival; the legacy constructor loads three modules from folders that moved and was evidence only until the B18 replay revival (below). The stored current [`outer_9183_current.csv`](outer_9183_current.csv) (61 rows, `M = 96`) can be checked by hand against the Syracuse map. The command in the legacy text names `experiments/residual_progress/complement_recursion/`.

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B18-replay-revival migration; standard library) replays the unmodified legacy check `check_transfer.py` in a temporary copy of the legacy layout built by `tools/legacy_replay.py`, requiring exit 0 and every file unchanged (about 11 s). It checks finite steps only; the status is unchanged.

## Remarks

- **Three tasks separated.** (1) a current identity for an actual annular submeasure with capacity; (2) whether its negative atoms cover the **exits of remaining roots**, not already absorbed states; (3) enough such identities, or another shrinking branch, for every remaining root. The first two now have an exact interface; universal coverage is open.
- The branches need unbounded excursions, so a recursive scheme must allow them rather than a universal height ceiling.
- The halving identity [`halving-coalescence-return`](../halving-coalescence-return/README.md) certifies a larger, complete binary class of roots; the remaining complementary profile on the five rays is the conditional target of [`five-ray-profile-completion-suffices`](../five-ray-profile-completion-suffices/README.md).

## History

- Migrated from `experiments/residual_progress/complement_recursion/ANNULAR_COMPLEMENT_TRANSFER.md` (legacy ID R20) at commit `be73a66`, by the B09 migration (Claude, Opus 5.5). Note, scripts, receipt and stored current moved byte-identical; the note's code span `../release/DELAYED_RELEASE.md` is now [`delayed-release-cancellation`](../delayed-release-cancellation/README.md). Legacy status: "written conditional transfer theorem, explicit infinite descent families, and finite current certificates. Full residual coverage remains open".
- Main lane (ChatGPT, Codex), 2026-10-17, from commit `65093c4`. Its "independent model review" of the transfer was the main lane's own agents; no review from another lane is on record.
