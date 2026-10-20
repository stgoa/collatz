---
id: prescribed-ternary-child-unbounded-clocks
kind: result
title: "The prescribed ternary child of the coupled cell cannot be reached at uniformly bounded clocks"
status: written
claim: >
  Odd-only 3x+1 map S, absorbing at 1; Q(ell) = 70506316836123 + 3 2^45 ell, the original coupled source. For
  every digit c in {0,1,2}, every ordinary clock bound K >= 0 and every prescribed return lower bound R >= 0,
  there is an infinite positive binary progression of j such that ell = c + 3j > j, the source at ell has at least
  R guarded Phi returns, and S^a(Q(ell)) != S^b(Q(j)) for all a, b <= K. Hence the proposed child Q(floor(ell/3))
  cannot be supplied on its whole domain by a finite catalogue of word pairs, even with finite binary refinements;
  the witnesses may change with K and R. Proof: the three digits share the negative rational parent centre q* =
  -515908491727/11404192419 (ell* = -22852975802/34212577257), whose shadow follows an 18-prefix and a negative
  12-cycle; the child shadows for c = 0, 1 are positive, and for c = 2 an exact 112-word negative path disjoint
  from the upper orbit reaches 1663/7153 > 0, so the rational orbits never meet; binary precision fixes both
  finite words, each prospective merger is a nonzero affine equation whose finitely many nonnegative integer roots
  are removed by further refinement, and precision at least 19R gives the returns. Nothing is said against
  unbounded input-dependent clocks, other child families, several signed children or general currents; the
  conditional child identity remains valid if its merger and helpers are supplied.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [binary-return-exit-control]
certificates: [check_legacy_replay.py]
evidence:
  - "check_child_catalogue_scope.py, child_history_audit.json: the legacy cylinder constructor, checker and receipt: complete cylinders for caps 0, 1, 2, 4, ..., 128 in all three digits plus cap 16 with R = 1, 4, 16, 128 (39 cylinders), 156 replayed positive pairs, the 112-word certificate with all 113 child states, and 13 rejections. It imports nothing, but its receipt pins the SHA-256 of this node's legacy note CHILD_HISTORY_SCOPE.md by file name, now an edited README, so it fails at its new path and in a legacy replay. Not reached at be73a66: the scripts/verify_all.py gate stopped earlier, at residual_progress/history_frontier (archive/legacy-checker-run-be73a66.md); it passed in full at 9dbc71a; A replay at this migration, before the note was edited, passed (exit 0, receipt unchanged)"
  - "../two-source-normalisation-first-departure/r93_r94_check.py: side-lane probe of R93, R94 and the later-target probe, replayed by this node's check_legacy_replay.py (see reviewed_by)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: ../two-source-normalisation-first-departure/r93_r94_check.py
    scope: "Finite only (side-lane feed entry 2026-10-18 07:33, VERIFIED): the centres q* and ℓ* with v2(ℓ*) = 1 and v2(q* − Q₀) = 46; the 18-prefix and 12-word from q* ('All 31 states are negative'); 'The 112-arrow orbit of `p*_2` ends at `1663/7153`. All its earlier states are negative, none equals an upper state, and none exceeds 80 bits.'; and 'I built main's plan independently: c ∈ {0,1,2} and K ∈ {0,1,2,4,…,128}, plus K = 16 with R ∈ {1,4,16,128}. That gives 39 cylinders and 156 replayed positive pairs.' The progression guarantee rests on the written affine-root argument. The status stays written"
aliases: [R94]
tags: [convergence, outer-residual, clock-bound, rational-shadow, crt-construction, child-recursion]
---

# The prescribed ternary child of the coupled cell cannot be reached at uniformly bounded clocks

## Statement

Odd-only clock `S`, 1 absorbing; both clocks of a common-tail comparison are ordinary clocks. `Q(ℓ) = Q0 + QP·ℓ`, `Q0 = 70506316836123`, `QP = 3·2^45`, the original coupled source of [`binary-return-exit-control`](../binary-return-exit-control/README.md) (R90). The proposed child of [`common-tail-comparison-after-r92`](../../questions/common-tail-comparison-after-r92.md) is `Q(⌊ℓ/3⌋)`.

1. **Theorem.** For each digit `c ∈ {0, 1, 2}`, each clock cap `K ≥ 0` and each return count `R ≥ 0` there is an infinite positive binary progression of `j` with `ℓ = c + 3j > j`, the source at `ℓ` having at least `R` guarded `Φ` returns, and `S^a(Q(c + 3j)) ≠ S^b(Q(j))` for all `0 ≤ a, b ≤ K`.
2. **Consequence.** A comparison supplying this child for every input cannot have uniformly bounded ordinary clocks, even within one digit class and after prescribing many initial returns; a finite catalogue of fixed word pairs, with any finite binary refinement, is insufficient for this child rule.
3. **Certificate.** All three digits share the negative rational centre `q* = −515908491727/11404192419` (`11404192419 = 7153·3^13`), whose shadow follows the 18-prefix and the negative 12-cycle of the guarded return. The child centres for `c = 0, 1` are positive; for `c = 2` an exact 112-word negative path, disjoint from the upper orbit, reaches `1663/7153 > 0`. So the shadows never meet; sufficient binary precision fixes the finite words, each prospective merger is a nonzero affine equation, and its finitely many nonnegative integer roots are excluded by refinement. Precision at least `19R` gives the returns.

This does not exclude input-dependent unbounded clocks, other child families, several signed children or general currents.

## Proof

The legacy note "The prescribed ternary child requires unbounded clocks" follows, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**Status: written scoped proof with an exact finite rational-word certificate.**
This does not exclude a merger at input-dependent, unbounded clocks. It does
not exclude a different child family, several signed children, or a general
finite current. It supplies no missing Collatz current.

The proposed child in [the later-target template](../../questions/common-tail-comparison-after-r92.md)
is `Q(floor(ell/3))`, where

    Q(ell)=Q0+QP*ell,
    Q0=70506316836123, QP=3*2^45.

Throughout, S is the ordinary odd-only Syracuse map, absorbed at1. Both clocks
in a common-tail comparison are ordinary clocks. No quotient-clock conversion
is used here.

### 1. Complete quantifiers

For each digit `c in {0,1,2}`, each clock cap `K>=0`, and each prescribed return
count `R>=0`, there is a positive binary progression of integers j such that:

1. `ell=c+3j>j>0`, so `Q(j)<Q(ell)`;
2. the original coupled source at ell has at least R guarded Phi returns;
3. for every pair of clocks `0<=a,b<=K`,

       S^a(Q(c+3j)) != S^b(Q(j)).                       (1)

The progression is infinite. It is constructed from finite rational arithmetic
for any prescribed c,K,R. Thus a comparison supplying this particular child
for every input cannot have a uniform bound on its two ordinary clocks, even
within any one digit class and after restricting to arbitrarily many initial
Phi returns. A finite catalogue of fixed word pairs, with any finite binary
refinement or choice policy, is therefore insufficient for this child rule.

This conclusion concerns the prescribed merger. The conditional signed-current
identity in NEXT_TARGET.md remains correct if the merger is supplied. The result
does not obstruct input-dependent words of unbounded length or a terminating
recursion that generates such words.

### 2. One common binary center

Write

    D=7153, B=299947, v*=-B/D,
    q*=(2^27*v*-213949807)/3^17
       =-515908491727/11404192419,
    ell*=(q*-Q0)/QP=-22852975802/34212577257.

The denominators are odd. In particular ell* is a binary-integral rational,
`v2(ell*)=1`, and `v2(q*-Q0)=46`. For each digit put

    j*_c=(ell*-c)/3,
    p*_c=Q0+QP*j*_c.

All j*_c are negative, binary-integral rationals. Their parent center is always
`Q(c+3j*_c)=q*`. The child centers are

|c|p*_c|
|--|--|
|0|1608135207907736055411347 / 34212577257|
|1|404387159579536788517523 / 34212577257|
|2|−799360888748662478376301 / 34212577257|

The first two are positive. Their rational Syracuse orbits stay positive:
for a positive odd rational with odd denominator, `3x+1>0`, and division by
its exact positive power of2 preserves positivity and oddness.

Rational Syracuse is used only as exact arithmetic on these auxiliary centers.
It is not being substituted for the positive integer dynamics. For an odd
rational x with odd denominator and `3x+1!=0`, define

    S_hat(x)=(3x+1)/2^v2(3x+1).

Every auxiliary state used below satisfies these conditions. A finite word is
locally constant in the binary topology, which transfers it to actual positive
integer sources in Section4.

### 3. The upper shadow and the third child are disjoint

Starting from q*, an exact 18-arrow prefix reaches

    6v*+1=-1792529/7153.

The subsequent exact word

    (1,1,1,1,3,1,4,1,2,1,1,2)

returns to the same rational state. Its length is12 and its cost is19. Every
state of the initial prefix and this cycle is negative. These are precisely
the original prefix and guarded return formulas, evaluated at the fixed
center; they can also be checked directly using rational arithmetic.

For c=2, the exact112-arrow word stored in
`check_child_catalogue_scope.py` and the audit receipt takes p*_2 to

    S_hat^112(p*_2)=1663/7153>0.                         (2)

All112 earlier states of this path are negative. None is equal to any state of
the upper18-prefix and12-cycle. The checker verifies every exact valuation,
the endpoint, all signs, and every equality comparison. The receipt retains
all113 child states and the complete112-word; its largest numerator has only
80 bits. This is a finite certificate, not an orbit extrapolation. After (2),
positivity supplies the infinite continuation argument without requiring a
cycle classification or any convergence assertion.

Consequently, for every c and every pair of finite nonnegative clocks a,b,

    S_hat^a(q*) != S_hat^b(p*_c).                       (3)

For c=0,1 this is simply the sign difference. For c=2 the finite negative
prefix is checked against the complete upper prefix and cycle; every later
child state is positive. The extra repeated upper endpoint is checked as well.

### 4. From disjoint shadows to a whole positive progression

Fix c,K. Compute the first K exact rational valuations at q* and p*_c, and
let E_max be the larger of their two total costs. The finite words exist:
the upper shadow has the stated negative cycle; both positive child shadows
never have `3x+1=0`; the third child reaches positivity by the finite certificate.

A word of total cost E occupies exactly one source cylinder modulo `2^(E+1)`.
The extra bit is retained. If

    j=j*_c (mod 2^N),  N+45>=E_max+1,                  (4)

both actual positive sources have their respective first K shadow valuations,
because the source slopes are `3QP` and `QP`, each of exact binary order45.
Absorption at1 introduces no discrepancy: the odd-only formula also fixes1
with valuation2.

For each `a,b<=K`, the two endpoints on (4) are affine functions of j:

    f_a(j)=[3^a*(Q0+QP*c+3QP*j)+C_a]/2^A_a,
    g_b(j)=[3^b*(Q0+QP*j)+C'_b]/2^B_b.                (5)

They cannot be identical affine functions. Indeed, evaluating (5) at j*_c
would contradict (3). Their equality therefore has either no solution or
one rational solution. Retain just their finitely many nonnegative integer
roots, forming a set F.

No member t of F equals j*_c, since j*_c<0. Increase N, if necessary, so

    N>v2(t-j*_c) for every t in F.                    (6)

Every valuation in (6) is finite. Thus the complete binary cylinder (4)
contains none of the roots. All positive j in it satisfy (1). This excludes
all clock pairs simultaneously, rather than only a sampled set of j.

The implementation follows (4)--(6) literally. It checks that no affine
equation vanishes identically, solves every remaining equation exactly, and
rejects every nonnegative integer root from the returned cylinder.

### 5. Compatibility with any prescribed initial return count

The original source coordinate is

    v0=67839005952677+2^18*3^18*ell.

At ell*, its value is v* and `Dv*+B=0`. Hence on `ell=c+3j`,

    Dv0+B = D*2^18*3^19*(j-j*_c).                   (7)

Taking N at least19R in addition to (4)--(6) gives

    v2(Dv0+B)>=19R+18.

By the complete guarded-return criterion, every such positive source has at
least R Phi returns. Increasing the binary precision does not remove the
infinite positive tail of the progression. This proves all quantifiers in
Section1, including independent choices of K and R.

The conclusion does not say that any fixed positive source fails forever.
The obstructing positive sources may change when K or R increases. It also
does not say that all sources in one exact return-count cell fail: the
constructed cylinder has a lower bound on its return count.

### 6. An independent argument for the c=2 digit

Without the112-word certificate, a weaker version of the c=2 conclusion
(without independently prescribing many Phi returns) follows at j*=-1.
There both rational sources equal the same negative integer `Q0-QP`.
All finite ordinary words are well-defined there. On a sufficiently small
binary cylinder, both sources follow prefixes of this single infinite word.

If an affine endpoint equation were identical, its slopes would require

    3^(a+1)*2^B = 3^b*2^A,

so `b=a+1` and `A=B`. The child word of length a+1 extends the identical
length-a prefix by one positive valuation, which forces `B>A`, a contradiction.
The same finite-root exclusion then works. This provides an independent
structural check of the prescribed-child limitation. The main theorem uses
the stronger common Phi center for all three digits.

### 7. Reproduction and limits

Run

    python3 experiments/residual_progress/child_history_scope/check_child_catalogue_scope.py

The checker constructs complete cylinders for caps
`0,1,2,4,8,16,32,64,128` in all three digits, and separately combines cap16
with return lower bounds `1,4,16,128`. It independently replays four positive
integer pairs from every cylinder and checks all their bounded-clock endpoint
intersections. These positive samples check the implementation; the full
progression guarantee comes from the finite affine-root certificate, not from
the samples. The receipt also pins the proof and checker source hashes.

Regenerate the receipt only after an intended source change using `--write`.
No repository dispatcher is extended. No terminal pair inputs are supplied.
No general signed-current obstruction or Collatz nonconvergence is inferred.

## Certificates

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B13 migration; standard library). The legacy scripts load sibling modules by their pre-migration paths, so they no longer run here. This certificate calls `tools/legacy_replay.py`, which rebuilds the pre-migration layout in a temporary directory from `tools/legacy_paths.json`, runs the unmodified legacy scripts there without `-O` (as `scripts/verify_all.py` did at `be73a66`), and requires exit 0 and every copied file unchanged. It writes nothing in the repository. It replays: the side-lane probe `r93_r94_check.py` from [`two-source-normalisation-first-departure`](../two-source-normalisation-first-departure/README.md) (about 2 s, receipt reproduced byte for byte), which rebuilds the centres, the shadows, the 112-word certificate and all 39 cylinders with 156 positive pairs independently. The legacy checker `check_child_catalogue_scope.py` is not replayed: it pins the hash of this node's note, now an edited README (see `evidence`). The command in the legacy text names `experiments/residual_progress/child_history_scope/`.

## Remarks

- The obstructing sources may change when `K` or `R` grows; no fixed positive source fails forever, and not every source of one exact return-count cell fails.
- This is the last result of the residual-progress line, which was frozen at R94 (see [`packet-current-supply`](../../questions/packet-current-supply.md)).
- No novelty is claimed.

## History

- Migrated from `experiments/residual_progress/child_history_scope/CHILD_HISTORY_SCOPE.md` (legacy ID R94) at commit `be73a66`, by the B13 migration (Claude, Opus 5.5). Note, scripts and receipts moved byte-identical; the note became this README, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Legacy status: "written scoped theorem with an exact finite rational-word certificate and complete cylinder constructor".
- Main lane (ChatGPT, Codex), 2026-10-18, first committed in `9190ccf`. The batch's "independent" proof, source and default-replay reviews recorded in archive/convergence-residual-progress/REPORT.md were the main lane's own agents, not a different lane.
