---
id: history-beyond-prescribed-growth
kind: result
title: "For every prescribed number of native returns, explicit cells have a smaller-origin history meeting above the root"
status: written
claim: >
  Odd-only 3x+1 map S, absorbing at 1; retained critical basis of R75; the H17 exit of R79 with U(b) =
  (729b+223)/512. For each r >= 0 put s = r+1 and choose the unique 0 < L < 3^(6s+2) with 64^L = 217/8272 mod
  3^(6s+4), h = 11L + 8s. Two exact positive CRT cells have v2(217b+223) = 9r+17 (exactly r returns), c = U^s(b) =
  137 mod 1024 and exact point order h on the second quotient inverse ray of q = 3(9c-1)/16; their endpoint p
  satisfies p < b for every positive member (slope 9 (131072/177147)^L / 18^s <= 1/2 with a strictly negative
  omitted intercept term). The ordinary words (1,2,1),(1,1,2,1,1,3)^s,(1,1,3) from 3b and 1^h,2,6L+3,1,2,1 from p
  meet at M = (2187c+925)/512 > 3b, clocks (6r+12, h+5), and the prefix difference plus H_p - H_b requests A_p -
  A_b, all ranks below 3b, with every smaller input a supplied premise. First values (r,L,h) = (0,740,8148),
  (1,2028089,22308995). For r >= 1 the two-ray/point procedure with deterministic H succeeds exactly when h >= 1
  and p < 3b, decided over all ray indices by a proved finite cutoff; at b = 96797577 all six admissible rays
  fail, while a supplied absorption witness exists there, so this limits the procedure, not the current. Not
  coverage of the whole H17 exit type.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [native-growth-original-rank-exit-obstruction, common-critical-rank-basis]
certificates: [check_legacy_replay.py]
evidence:
  - "check_growth_escape.py, growth_escape.py, growth_escape_audit.json: the legacy constructor, checker and receipt: 20 symbolic depths through 64, 160 modular phases, four exact terminal-unit/index cells, six exhaustive failure cases, 21 rejections, a capped-decision check, and the fully materialised r = 0 comparison (8165 rows) with its supplied 31041/39181-arrow absorption paths compiled to a 129-row pair current, stored losslessly. Fails at its new path: growth_escape.py loads ../native_nine_growth/ (now ../native-growth-original-rank-exit-obstruction/) by its pre-migration folder name; and Its receipt pins the SHA-256 of this node's legacy note NATIVE_GROWTH_ESCAPE.md, now an edited README, so it fails at its new path and in a legacy replay at earlier migrations (before rewritten notes were restored from git). Not reached at be73a66: the scripts/verify_all.py gate stopped earlier, at residual_progress/history_frontier (archive/legacy-checker-run-be73a66.md); it passed in full at 9dbc71a; A replay at this migration, before the note was edited, passed (exit 0, receipt unchanged). Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
  - "../fixed-word-history-cells/batch_r81_r83_check.py: side-lane probe of R81 and R83, replayed by this node's check_legacy_replay.py (see reviewed_by)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: ../fixed-word-history-cells/batch_r81_r83_check.py
    scope: "Finite only (side-lane feed entry 2026-10-18 04:08, VERIFIED, main 1d58f50): '**R83.** For `s = 1`, an exhaustive search over `0 < L < 3⁸` finds `L = 740` as the unique solution of `64^L ≡ 217/8272 (mod 3¹⁰)`. For `s = 2`, `L = 2028089` solves the congruence mod `3¹⁶`. It is unique below `3¹⁴` because 64 has order exactly `3¹⁴` there. Both give `h = 11L + 8s`: 8148 and 22308995. The CRT cells, the two words and the 8165-row comparison were not rebuilt.' The status stays written"
aliases: [R83]
tags: [convergence, outer-residual, smaller-origin-history, native-history, crt-construction, inverse-ray]
---

# For every prescribed number of native returns, explicit cells have a smaller-origin history meeting above the root

## Statement

Odd-only clock, 1 absorbing; `F(x) = 4x + 1`; retained critical basis of [`common-critical-rank-basis`](../common-critical-rank-basis/README.md) (R75), `[x] = div H_x + Σ A_x(v)P(v)`; the H17 exit of [`native-growth-original-rank-exit-obstruction`](../native-growth-original-rank-exit-obstruction/README.md) (R79): `U(b) = (729b + 223)/512`, `v2(217b + 223) = 9r + 17`, `s = r + 1`, `c = U^s(b)`, `z = (9c − 1)/16`, `q = 3z`, `Q = 3b`.

1. **All-ray decision for one procedure.** Follow either complete quotient inverse ray of `q` at index `L` by its maximal point chain, of length `h = v3(a + 1)`, ending at `p = 2^h(a + 1)/3^h − 1`, then deterministic `H`. For `r ≥ 1` the plan `E + I + H_p − H_b` (requests `A_p − A_b`) has all ranks below `Q` iff `h ≥ 1` and `p < Q`. All indices `L` are decided by the finite cutoff `64^L ≤ ⌊(9P_0 − 2)/(9a_0 + 7)⌋`, `J_0 = ⌊log₂(Q − 1)⌋ − 1`, `P_0 = ⌊3^J_0(Q − 1)/2^J_0⌋`. At `b = 96797577` only `L = 0, 1, 2` on each ray qualify and all six fail; a supplied absorption witness for the same `b` shows this limits the procedure, not the existence of the current.
2. **Escape after any growth depth.** For every `r ≥ 0` let `L` be the unique solution in `0 < L < 3^(6s+2)` of `64^L ≡ 217/8272 (mod 3^(6s+4))` and `h = 11L + 8s`. Two complete positive CRT cells have exactly `r` returns, `c ≡ 137 (mod 1024)`, and exact point order `h` on the second ray. On them `p < b` for every positive member: the slope is `9·(131072/177147)^L/18^s ≤ 1/2` and the omitted intercept term is negative.
3. **High meeting.** The ordinary words `(1,2,1), (1,1,2,1,1,3)^s, (1,1,3)` from `3b` and `1^h, 2, 6L + 3, 1, 2, 1` from `p` meet at `M = (2187c + 925)/512 > 3b`, clocks `(6r + 12, h + 5)`; so `p < b < 3b < M`. Their exact prefix difference plus `H_p − H_b` requests only ranks below `3b`; every smaller input, including negative coefficients, remains a supplied premise.

First values: `(r, L, h) = (0, 740, 8148)` and `(1, 2028089, 22308995)`.

## Proof

The legacy note "A smaller-origin history beyond every native H17 growth depth" follows, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**Status: written conditional construction and exact finite replay.** For every
prescribed number of R79 growing returns, an explicit infinite arithmetic
subfamily has an original-rank-valid comparison. Its smaller seed meets the
original root's future while both are above the original root. The ray index
and comparison length grow very quickly with the prescribed depth. This is
not coverage of the entire H17 exit family: a complete all-ray failure witness
for the precise point-inverse procedure is included below. No dispatcher is
changed, no universal terminal supply is proved, and no novelty is asserted.

Use the absorbed odd map S, `F(x)=4x+1`, elementary minimum nu, and retained
critical basis `W5 union W9` from [R75](../common-critical-rank-basis/README.md).
Write the exact formal absorption identity as

    [x] = div H_x + sum A_x(v) P(v),   P(v)=[3v]−[v],
    A_x(v) nonzero implies rho(v)<=nu(x).

These H identities retain missing pair inputs. An actual absorption current
must be supplied when a constructor requests one.

### 1. The full H17 exit and its exact two inverse rays

Recall [R79](../native-growth-original-rank-exit-obstruction/README.md). Put

    U(b)=(729b+223)/512,       Y(b)=217b+223.

Fix r>=0, a positive b with `v2(Y(b))=9r+17`, and set

    s=r+1,   c=U^s(b),   z=(9c−1)/16,   q=3z,   Q=3b.       (1)

There are exactly r complete guarded returns. The full exit has current
`E+H_z−H_b`, requests `{z:+1}+A_z−A_b`, and `div E=[Q]−[q]`.
Its ordinary clocks are `(6r+12,4)`. For r>=1, q>Q and its leading request
has coefficient+1. The two standard base inverse choices do not repair it.

The **complete** quotient inverse rays of q are

    a_(0,L)=(64^L(9(8z+1)+7)−7)/9,
    a_(1,L)=(64^L(9(16z+1)+7)−7)/9,        L>=0.            (2)

Every a is canonical and1 modulo8. Put

    h=v3(a+1),       p=2^h(a+1)/3^h−1.                      (3)

The h point-inverse arrows are all legal valuation1 arrows from p to a.
The endpoint p is positive and canonical. For h>=1 it is3 modulo4 and
not2 modulo3, hence a critical root with one highest request of rank p.
For h>=2 its critical pair index is W5; the possible h1 W9 case is retained,
not silently eliminated.

**Proof of these endpoint facts.** Since a=1 mod8, the exact binary order
of a+1 is1. Dividing a+1 by its exact power3 and multiplying by2^h gives
`v2(p+1)=h+1`. Its odd unit is3^h modulo4, opposite to the selected phase
3^(h+1). Thus p is complementary canonical; exact maximality gives p not2
modulo3. Positivity follows from a+1 being a positive even multiple of3^h.
Every intermediate point has the same complementary property and an exact
valuation1 forward arrow.

The ray arrows have fixed ordinary descriptions:

- For ray0, `S(a)=F^(3L)(6z+1)`. Its path merges with q after ordinary
  clocks `(5,4)` from a,q respectively.
- For ray1, `S(a)=F^(3L+1)(q)`, and `S²(a)=S(q)`, with exact valuations
  `(2,6L+3)` from a.

Prepending the h point arrows gives an inverse current I with
`div I=[q]−[p]`. Adding it to the entire exit and replacing the leading
P(z) by its exact inverse plan cancels both H_z terms. The result is

    J=E+I+H_p−H_b,
    requests=A_p−A_b.                                      (4)

All signs and multiplicities are retained. The displayed root-comparison
current `E+I` is exactly the difference of ordinary prefixes from Q and p
with clocks `(6r+12,h+5)`. In ray1, extend the equality at S(q) by three
arrows; these are precisely the three remaining rows of q's old four-arrow
prefix. In ray0 the merger already has q-clock4. This proves equality of
current rows, not only of their divergences.

### 2. A complete decision for this all-ray procedure

Suppose r>=1. For each ray and L, (4) has all remaining critical ranks below
Q **if and only if h>=1 and p<Q**.

If h>=1, H_p starts with its unique critical request of rank p and coefficient
+1. Later requests have smaller rank. Every negative H_b request has rank at
most b<Q, so a p>=Q request cannot cancel. Conversely p<Q and b<Q bound
every request in (4) below Q.

If h=0, the canonical a=1 mod8 takes its compulsory forward arrow and
normalizer to q. Its formal H therefore cancels I exactly and restores the
old H17 exit current, including its higher request. In particular a large
raw p=a is not being used as a bound in place of this exact cancellation.
For a nonempty shorter point prefix, the remaining endpoint is canonical,
3 modulo4 and2 modulo3, so formal H continues its inverse descent to (3).
Consequently stopping any positive point prefix early adds no successes.
The zero-point stop is the restored baseline. This exhausts the two rays
with this point continuation and deterministic H; it does not exhaust all
inverse words, cycle continuations, forward moves or supplied histories.

The decision over **every L** is finite. Set

    J0=floor(log2(Q−1))−1,
    P0=floor(3^J0*(Q−1)/2^J0).                              (5)

A passing p is odd and p<Q, so p+1<=Q−1. Since2^(h+1) divides p+1,
`h<=J0`. Therefore `a+1=(3/2)^h(p+1)<=P0`. At either base a0 this gives

    64^L <= floor((9P0−2)/(9a0+7)).                         (6)

The right side is explicit. Testing those finitely many L is exhaustive;
an implementation cap reports `capped`, never an exhausted failure.

**Complete failure witness.** Take b96797577, the first stored R79 r1
fixture. Then Q290392731, J0=27 and P0=16498700317341. The cutoff ratios
in (6) are18683 and9341, so each ray admits only L0,1,2. Their exact
`(h,p)` pairs are

| Ray | L0 | L1 | L2 |
|---|---|---|---|
|0|(1,588709275)|(0,56516090481)|(0,3617029790833)|
|1|(0,1766127825)|(0,113032180849)|(2,3215137588615)|

All fail the decision above. Thus every ray in this procedure fails at this
fixed positive input. The checker also stores a finite absorption witness
for this same b, so this is an obstruction to the named inference procedure,
not to existence of the pair current.

### 3. Exact ternary freedom after any prescribed growth depth

We now construct an accepted infinite subfamily for **every r>=0** using
ray1. Let s=r+1 and

    C_s=223(729^s−512^s)/217,        d=6s+4.

Then `c=(729^s b+C_s)/512^s`, and the second ray satisfies

    a+1 = (64^L(81c+7)+2)/9.                                (7)

Choose the unique L in `0<=L<3^(d−2)` such that

    64^L=217/8272 mod3^d.                                   (8)

The target is1 modulo9. The elementary identity
`v3(64^n−1)=2+v3(n)` proves that64 generates exactly the subgroup1 modulo9
at every precision, so (8) has one solution. It is nonzero, since
`v3(8272−217)=2<d`. This argument uses finite integer arithmetic, not an
assumption about a positive infinite 3-adic trajectory.

Write

    B0=64^L(81C_s+7*512^s)+2*512^s.

The constant B0 is divisible by3^d. Indeed

    217 B0 = 64^L*18063*729^s
             +2*512^s*(217−8272*64^L),                     (9)

and both terms have the required divisibility. Put beta=B0/3^d. Equation
(7) becomes

    a+1=3^(6s+2)*(2^(6L)b+beta)/2^(9s).                     (10)

This identity exhibits the **remaining free ternary digits of b**.
For any h>=6s+2, put m=h−6s−2 and choose either unit e=1 or2. The exact
point order h is imposed by the single residue

    b=(e*3^m−beta)*2^(−6L) mod3^(m+1).                     (11)

The coefficient is a ternary unit, so this cell is nonempty.

Independently impose the slightly sharper binary exit condition

    b=(512^s*137−C_s)*729^(−s) mod2^(9s+10).                (12)

It says exactly `c=137 mod1024`. Therefore `v2(Y(c))=8` and
`v2(Y(b))=9s+8=9r+17`: the original number of returns is still exactly r.
The coprime CRT of (11),(12) is a complete infinite positive progression.
Every integer in it has exact h, not merely a lower bound. Its modulus is
`2^(9s+10)*3^(h−6s−1)`. There are two terminal-unit cells. No sample search
is used to establish their existence.

### 4. A uniform parameter choice makes the endpoint smaller than b

Choose in (11)

    h=11L+8s.                                               (13)

This satisfies h>=6s+2. The coefficient of b in p is

    lambda=9*64^L*(729/512)^s*(2/3)^h
          =9*(131072/177147)^L/18^s <= 1/2.                (14)

The affine intercept is controlled exactly, rather than dropped. Since

    c=(729/512)^s*(b+223/217)−223/217,

(7) gives

    a+1 < 9*64^L*(729/512)^s*(b+223/217).

The omitted term is
`64^L*(7/9−2007/217)+2/9<0`. Hence

    p+1 < lambda*(b+223/217) <= (b+223/217)/2,
    0 < p < b.                                             (15)

The last strict inequality holds for every positive integer b. It does not
rely on an asymptotic threshold or a numerically observed slope.

Substituting (15) into (4) proves an original-rank-valid conditional pair
comparison on **all** of the two CRT cells, for every prescribed r. Every
request of H_p has rank at most p<b, and every request of H_b at most b<3b.
The negative term is retained with its actual multiplicities. A supplied
absorption current at p and at b therefore yields an actual P(b) current.
Equivalently one may expand both formal H plans into smaller critical pair
premises. Neither input is assumed automatically available.

The first values of `(r,L,h)` are `(0,740,8148)` and
`(1,2028089,22308995)`. Later cells quickly become enormous. The module
returns exact symbolic descriptors and enforces a separate materialization
cap; finite arithmetic tests at larger r do not expand those huge paths.

### 5. The meeting occurs above the original rank

Condition (12) supplies a stronger exact history statement. The original
root Q=3b has valuation word

    (1,2,1), (1,1,2,1,1,3)^s, (1,1,3),                      (16)

of length6r+12 and total valuation9r+18. To check the repeated part, after
the first three arrows the state is `x=(81b+23)/16`. The six-arrow block
sends x to `(729x+817)/512`, which is precisely `(81U(b)+23)/16`.
The guarded binary residues give every exact valuation, including the final
bit. At c137mod1024 the final three-arrow tail is `(1,1,3)`.

The smaller p has valuation word

    1^h, 2, 6L+3, 1,2,1                                  (17)

of length h+5. Its first h arrows reach a, the next two reach S(q), and
`q=3z=231 mod1728` gives the final three exact valuations `(1,2,1)`.
Thus both ordinary paths reach exactly

    S^(6r+12)(3b)=S^(h+5)(p)=M=(2187c+925)/512.              (18)

Since c>(729/512)^s b, we have M>3b. Together with (15),

    p < b < 3b < M.

The current E+I in (4) is precisely the difference of the prefixes (16),(17).
This is a smaller-origin **future-history** comparison. The endpoint M is
not itself assumed absorbed, and a high meeting does not violate the
original-rank test on the supplied inputs.

### 6. Reproduction and finite evidence

Run `python3 experiments/residual_progress/native_growth_escape/check_growth_escape.py`.
Default replay compares the stored receipt; `--write-receipt` refreshes it.
The checker independently reconstructs Syracuse edges, exact valuation
words, complete signed divergences, both all-ray cutoffs and failure
vectors. It tests modular descriptors for larger r without materializing
their exponentially large exponents. The r0 family is fully materialized;
its exact root-comparison current and supplied absorption currents are
encoded compactly by source values in hexadecimal and valuation words.
Their complete tables are reconstructed and checked during replay.

The designated absorption demonstration uses hard limits of50,000 odd
arrows and25,000 bits for each input. A cap is unresolved evidence, not an
infinite conclusion. Missing or malformed supplies and invalid or oversized
materializations are rejected. These finite inputs supply only the stored
example; the all-r theorem remains conditional on the explicitly smaller
inputs. Other members of the full H17 exit type remain open, as the
all-ray failure witness makes concrete.

## Certificates

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B13 migration; standard library). The legacy scripts load sibling modules by their pre-migration paths, so they no longer run here. This certificate calls `tools/legacy_replay.py`, which rebuilds the pre-migration layout in a temporary directory from `tools/legacy_paths.json`, runs the unmodified legacy scripts there without `-O` (as `scripts/verify_all.py` did at `be73a66`), and requires exit 0 and every copied file unchanged. It writes nothing in the repository. It replays: the side-lane probe `batch_r81_r83_check.py` from [`fixed-word-history-cells`](../fixed-word-history-cells/README.md) (under 1 s, receipt reproduced byte for byte), which recomputes the parameters `(L, h)` for `s = 1, 2`. The legacy checker `check_growth_escape.py` was not replayed at the B13 migration, which predated restoring hash-pinned notes from git; it is now (see below and `evidence`). The command in the legacy text names `experiments/residual_progress/native_growth_escape/`.

At the B18-replay-revival migration [`check_legacy_replay.py`](check_legacy_replay.py) was extended to replay also `check_growth_escape.py`, which now passes in the legacy layout because rewritten notes are restored from git at `be73a66` (about 17 s in all). It checks finite steps only; the status is unchanged.

## Remarks

- The same cutoff argument is reused at later exit targets in the attempt [`two-ray-point-procedure-later-target`](../../attempts/two-ray-point-procedure-later-target/README.md).
- The fixed-clock barrier [`bounded-history-clock-exclusion`](../bounded-history-clock-exclusion/README.md) (R85) does not contradict this construction, which uses later future targets and very long partner words.
- No novelty is claimed.

## History

- Migrated from `experiments/residual_progress/native_growth_escape/NATIVE_GROWTH_ESCAPE.md` (legacy ID R83) at commit `be73a66`, by the B13 migration (Claude, Opus 5.5). Note, scripts and receipts moved byte-identical; the note became this README, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Legacy status: "written conditional all-return-count CRT construction, complete scoped failure and full supplied finite demonstration".
- Main lane (ChatGPT, Codex), 2026-10-18, first committed in `1d58f50`. The batch's "independent" proof, source and default-replay reviews recorded in archive/convergence-residual-progress/REPORT.md were the main lane's own agents, not a different lane.
