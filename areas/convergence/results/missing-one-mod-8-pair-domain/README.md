---
id: missing-one-mod-8-pair-domain
kind: result
title: Two complete branches enter the paired recursion from the missing domain w = 1 mod 8 and give smaller-seed mergers on the a = 3 mod 16 Mersenne family
status: written
claim: >
  Odd-only 3x+1 map S, absorbing at 1; P(w) = delta_(3w) - delta_w; F(y) = 4y+1. (Branch A) For w = 17 mod 128,
  w = 16u+1, v = 3u: S(3w) = F(18u+1), S(w) = F(3u), 18u+1 is the selected partner of the canonical 9u = 3v, so an
  explicit local current has divergence P(w) - P(v), with v = 3 mod 8, 0 < v < w; a child clock l >= 2 gives
  parent clock l+1. (Branch B) For w = 105 mod 256, v = (9w-1)/16 = 11 mod 16: S^2(3w) = 2(3v)+1 and
  S^2(w) = 2v+1 are selected partners of the canonical 3v and v, giving divergence P(w) - P(v), 0 < v < w, parent
  clock l+2. In both the child current is added, and the child enters the 3-mod-8 constructor of
  mixed-shrinking-pair-rules. (Cylinders and roots) Every accepted mixed word has a complete A parent cylinder (and
  B parents for words whose origin is 11 mod 16), realised by exponent classes a = 3 mod 16 of the family
  x = 2^a - 1, q = 2^(a-1) - 1 < N = 12 2^(a-4); e.g. S^(a+4)(2^a-1) = S^(a+4)(2^(a-1)-1) for a = 1699 mod 4096 and
  S^(a+5)(2^a-1) = S^(a+5)(2^(a-1)-1) for a = 659 mod 4096, although the old normalised return is unbounded relative
  to x. With a supplied current for q (absorption below N is an input) such x are certified. Partial: it does not
  cover all w (a = 147 is an explicit unresolved child example) or prove Collatz, and no residual density
  improvement is claimed.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [elementary-bridge-quotient-normal-form, mixed-shrinking-pair-rules, tripling-doubling-pair-decomposition]
certificates: [check_pair_one_recompute.py, check_legacy_replay.py]
evidence:
  - "check_pair_one.py, pair_one.py, pair_one_audit.json, pair_315_current.csv: the legacy constructor and checker (direct domains over 4096 inputs, mixed-word cylinders, modular exponent lifts, four actual Mersenne bridges, the a = 659 supplied-input conversion with a 10000-step input cap, and the small current for 315 from a supplied path of 105). Fails at its new path: pair_one.py loads ../paired_completion/mixed_pairs.py (now ../mixed-shrinking-pair-rules/, which itself no longer runs) by its pre-migration path. Passed at be73a66 as experiments/residual_progress/pair_one/check_pair_one.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran these steps before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a). The later coupled-even-pair-recursion loads pair_one.py by its old path. Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-17
    link: ../mixed-shrinking-pair-rules/batch_r33_r36_check.py
    scope: "Finite only (side-lane feed entry 2026-10-17 21:06, VERIFIED, main 1603bf3; the R36 part): S^t(2^a - 1) = S^t(2^(a-1) - 1) at a = 1699 with t = a+4 and at a = 659 with t = a+5. The written branch identities and cylinder constructions were not re-derived; the status stays written"
aliases: [R36]
tags: [convergence, outer-residual, pair-recursion, tripling-pairs, mersenne, conditional, constructive]
---

# Two complete branches enter the paired recursion from the missing domain w = 1 mod 8 and give smaller-seed mergers on the a = 3 mod 16 Mersenne family

## Statement

Odd-only clock, absorbing at 1, `div = I − P`; `P(w) = δ_(3w) − δ_w`, `F(y) = 4y + 1`; elementary identities from [`elementary-bridge-quotient-normal-form`](../elementary-bridge-quotient-normal-form/README.md).

1. **Why this branch.** For `a ≡ 3 (mod 16)`, `a ≥ 19`, the root `x = 2^a − 1` at `N = 12·2^(a−4)` has `S^(a−1)(q) = w = (3^(a−1) − 1)/8 ≡ 1 (mod 8)` and `S^a(x) = F(3w)`, so the remaining comparison is `P(w)` outside the `3 (mod 8)` domain; [`tripling-doubling-pair-decomposition`](../tripling-doubling-pair-decomposition/README.md) shows the static catalogue cannot close it.
2. **Branch A.** `w ≡ 17 (mod 128)`, `w = 16u + 1`, `v = 3u ≡ 3 (mod 8)`, `0 < v < w`: `S(3w) = F(18u + 1)`, `S(w) = F(3u)`, and `18u + 1` is the selected partner of the canonical `9u`. A local current `L_A` has `div L_A = P(w) − P(v)`; `L_A + J_v` certifies `P(w)`; child clock `l ≥ 2` gives parent clock `l + 1`.
3. **Branch B.** `w ≡ 105 (mod 256)`, `v = (9w − 1)/16 ≡ 11 (mod 16)`, `0 < v < w`: `S²(3w) = 2(3v) + 1`, `S²(w) = 2v + 1` (valuations `1,2` and `2,1`), selected partners of the canonical `3v` and `v`; `div L_B = P(w) − P(v)`, child added, parent clock `l + 2`.
4. **Cylinders and actual roots.** Each accepted child word of [`mixed-shrinking-pair-rules`](../mixed-shrinking-pair-rules/README.md) with modulus `M` has the exact A parent cylinder `3w ≡ 16r + 3 (mod 16M)`, and for `r ≡ 11 (mod 16)` the B parent `9w ≡ 16r + 1 (mod 16M)`; lifting gives exponent classes, e.g. A: `w ≡ 1681 (mod 2048)`, `a ≡ 1699 (mod 4096)`, `S^(a+4)(2^a − 1) = S^(a+4)(2^(a−1) − 1)`; B: `w ≡ 105 (mod 2048)`, `a ≡ 659 (mod 4096)`, merger at `a + 5`. The old normalised return is unbounded relative to `x` on both. With a supplied current for `q` (absorption below `N` is the input), `D_x + J_w − H_(q,w) + H_q` certifies `x` at any source multiplicity.

Universal coverage is open (`a = 147` is an explicit unresolved child example although it enters branch B); no uniform residual density improvement, novelty, human review or formal verification is claimed.

## Proof

The legacy note "Entering the paired recursion from the missing residue domain" follows, lightly edited (headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

2026-10-17. **Written partial construction and finite exact checks.**
Use odd-only Syracuse S, with1 absorbing, and killed divergence I-P.
For any positive odd w write P(w)=delta_(3w)-delta_w. This note supplies
two complete branches from w=1 modulo8 into the previously handled
w=3 modulo8 domain. It does not cover all w or prove Collatz.

The [mixed-pair constructor](../mixed-shrinking-pair-rules/README.md) supplies
finite currents for an explicit subset of the3-modulo8 domain, with a
prescribed merger clock l satisfying S^l(3w)=S^(l+1)(w). Its accepted
clocks are at least3. Its unresolved outcomes remain unresolved here.
We use the elementary F and selected-halving identities of
[R25](../elementary-bridge-quotient-normal-form/README.md), where F(y)=4y+1.

### 1. Why this is a different missing branch

For every a>=19, a=3 modulo16, put

```
x=2^a-1,  N=12*2^(a-4),  q=2^(a-1)-1,
w=(3^(a-1)-1)/8.
```

Then x is a full coefficient1 complementary R_N root, q<N, and w=1
modulo8. Exact prescribed prefixes give S^(a-1)(q)=w and
S^a(x)=F(3w). The needed remaining comparison is P(w), outside R30's
original domain. The [static catalogue audit](../tripling-doubling-pair-decomposition/README.md)
proves that elementary identities plus all hypothetical3-modulo8 pair
bridges still leave the endpoints of this comparison distinct after the
first R26 run. Additional dynamic comparisons are therefore necessary
for that particular mechanism. The rules below supply some of them.

### 2. Branch A: one ordinary step and two elementary bridges

Suppose

```
w=16u+1,       u=1 modulo8,       v=3u.
```

Equivalently w=17 modulo128. The child v is3 modulo8 and
0<v=3(w-1)/16<w. Direct arithmetic gives

```
S(3w)=72u+5=F(18u+1),
S(w)=12u+1=F(3u),
18u+1=2(9u)+1.
```

Since9u is1 modulo8 and canonical,18u+1 is its selected partner.
The left prefix followed by the F bridge and selected-halving bridge
ends at9u=3v. The right prefix followed by its F bridge ends at3u=v.
Subtracting gives an explicit local current L_A with

```
div L_A=P(w)-P(v).                                   (1)
```

If J_v certifies P(v), then L_A+J_v certifies P(w). The orientation is
positive; this is different from the even recursive branches of R30.

For the clock, the selected partner of9u has run length2. Consequently

```
S^j(3w)=S^(j-1)(3v)  for j>=3,
S^j(w)=S^(j-1)(v)    for j>=2.
```

Thus any child merger clock l>=2 gives parent clock l+1:
S^(l+1)(3w)=S^(l+2)(w). No absorption assertion is used in this identity.

### 3. Branch B: two ordinary steps and two selected partners

Suppose w=105 modulo256, and put

```
v=(9w-1)/16.
```

Then v=11 modulo16, so both v and3v are canonical, v=3 modulo8,
and0<v<w. The first two valuations on3w are1,2; on w they are2,1.
The exact endpoints are

```
S^2(3w)=(27w+5)/8=2(3v)+1,
S^2(w)=(9w+7)/8=2v+1.
```

These are selected partners of3v and v. Append their elementary bridges
and subtract to obtain another explicit local current

```
div L_B=P(w)-P(v).                                   (2)
```

The left partner has selected run length2; the right has length3.
Therefore S^j(3w)=S^(j-2)(3v) for j>=4 and
S^j(w)=S^(j-2)(v) for j>=5. A child clock l>=2 gives parent clock l+2.
As in branch A, the child current is added, not subtracted.

The A and B domains are disjoint, being1 and9 modulo16 respectively.
Every recognized parent enters the3-modulo8 constructor after one strict
parameter decrease. Failure of either parent recognition or child
recognition is reported explicitly, never interpreted as nonconvergence.

### 4. Complete mixed cylinders and actual Mersenne roots

Let a complete accepted child word from the mixed-pair theorem have
origin v=r modulo M, where M is its power-of-two modulus. Branch A has
the unique complete parent cylinder

```
3w=16r+3 modulo16M.                                  (3)
```

For branch B require r=11 modulo16; its parent cylinder is

```
9w=16r+1 modulo16M.                                  (4)
```

Odd3 and9 are invertible modulo16M, so both are executable exact
binary cylinders. All necessary branch bits are retained. Every A
parent is17 modulo128. Every B parent is105 modulo256. The child word
has its proved prescribed finite depth, so the parent is accepted.
There are A parents of every finite mixed word and hence arbitrarily
large recursive depths. B includes the terminal word and every word
whose origin is11 modulo16; no other words are claimed for it.

Nonempty positive integer witnesses follow by CRT: for A choose the
child in its binary cylinder and v=0 modulo3, then w=1+16v/3.
For B choose v=5 modulo9, then w=(16v+1)/9. These witnesses prove
actual integer integrality, rather than relying only on2-adic notation.

For each parent residue c=1 modulo8 modulo2^m, elementary lifting gives
a unique a=3 modulo16 modulo2^(m+1) such that

```
3^(a-1)=1+8c modulo2^(m+3).                          (5)
```

Start with exponent a-1=2 modulo16 and lift one bit at a time using
3^(2^j)=1+2^(j+2) modulo2^(j+3). Each lift has exactly one choice.
This realizes each complete parent word in the actual exponential w
from Section1. Two explicit terminal examples are

| Parent branch | Parent w cylinder | Exponent cylinder | Pair clock |
|---|---|---|---:|
| A |1681 modulo2048|1699 modulo4096|4|
| B |105 modulo2048|659 modulo4096|5|

For every exponent in the A class, respectively B class,

```
S^(a+4)(2^a-1)=S^(a+4)(2^(a-1)-1),
S^(a+5)(2^a-1)=S^(a+5)(2^(a-1)-1).                  (6)
```

The normalized old return is(3w-1)/2 on A and3w on B. Both have
unbounded ratio to x along their exponent progression. These are
therefore smaller-seed mergers through the old growing-return obstruction,
including portions of the separate a=3 modulo16 family. No claim of a
uniform residual density improvement follows from this construction.

### 5. Supplied-input conversion and checks

Let D_x be the raw R26 bridge from x to3w, J_w the accepted pair current,
and H_(q,w) the prescribed q prefix. Then

```
div(D_x+J_w-H_(q,w))=delta_x-delta_q.                 (7)
```

Add a supplied finite exact current for q and extract a nonnegative
absorption current from that finite graph. The construction uses only
supplied or explicitly prescribed edges. Scale the entire identity for
any positive source multiplicity. Separate root certificates may reuse
known inputs; this is not a joint annular capacity assertion.

The code keeps R30 unchanged and imports its extended domain3 constructor.
The default checker is read-only:

```
python3 experiments/residual_progress/pair_one/check_pair_one.py
```

The receipt records direct domains, mixed-word examples, modular exponent
lifts, actual Mersenne bridges and a capped supplied-input conversion.
The small current for315 uses only a supplied105 path and the branch B
certificate. The much larger a659 conversion is regenerated under a
10000-step input-discovery cap and recorded by exact current hashes.
Current arithmetic and merger clocks are checked independently with
ordinary prefixes. These finite checks support the implementation; the
infinite claims rest on the written identities above.

Universal coverage, external novelty and human/formal verification remain
unestablished. In particular a147 is an explicit unresolved child example
for the present rule, despite entering parent branch B.

## Certificates

- [`check_pair_one_recompute.py`](check_pair_one_recompute.py) (written at the B10 migration, under 1 s, standard library). With its own `S` and canonical test it checks: both branch identities, the child bounds and canonicity for every A and B input among the 4096 odd `w ≡ 1 (mod 8)` below 32768, and the domain counts 256, 128 and 3712 of [`pair_one_audit.json`](pair_one_audit.json); the two terminal exponent lifts `1699` and `659 (mod 4096)` by exhaustion; the four actual Mersenne mergers (`a = 659, 1699, 4755, 5795`) at the receipt's clocks by direct iteration; and that [`pair_315_current.csv`](pair_315_current.csv) is the actual path of 315 to 1. It does not rebuild the mixed-word acceptances, the current hashes or the supplied `a = 659` conversion (legacy checker, evidence only).
- The command in the legacy text names `experiments/residual_progress/pair_one/`.

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B18-replay-revival migration; standard library) replays the unmodified legacy check `check_pair_one.py` in a temporary copy of the legacy layout built by `tools/legacy_replay.py`, requiring exit 0 and every file unchanged (about 13 s). It checks finite steps only; the status is unchanged.

## Remarks

- **Consistent with the static scope.** The exponent classes `659` and `1699 (mod 4096)` lie inside the counterfamily of [`tripling-doubling-pair-decomposition`](../tripling-doubling-pair-decomposition/README.md); the branches succeed there by using additional ordinary forward arrows, beyond the static identity graph that node classifies.
- **Next step.** [`coupled-even-pair-recursion`](../coupled-even-pair-recursion/README.md) builds its first entry `A` on branch A here and finds the exact success set of the older split algorithm.
- No novelty is claimed.

## History

- Migrated from `experiments/residual_progress/pair_one/MISSING_PAIR_DOMAIN.md` (legacy ID R36) at commit `be73a66`, by the B10 migration (Claude, Opus 5.5). Note, scripts, receipt and stored current moved byte-identical; `check_pair_one_recompute.py` was added at the migration. Legacy status: "written partial bridges, complete mixed cylinders and actual smaller-seed mergers".
- Main lane (ChatGPT, Codex), 2026-10-17, from commit `1603bf3`. The batch report (archive/convergence-residual-progress/REPORT.md) records "independent model" proof and code audits for this batch; they were the main lane's own agents, so they do not count as an independent review. The side lane's finite check is recorded under `reviewed_by`.
