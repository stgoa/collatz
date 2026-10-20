---
id: ray-index-decision-count-obstruction
kind: result
title: "Every inverse-ray index of a two-rotation cycle/point procedure is decidable, and it accepts under 1/500 of its entry row"
status: written
claim: >
  Odd-only 3x+1 map S, absorbing at 1; rho(w) = nu(3w). On the entry row v = 4089 + 6144n, w = 6901 + 10368n, q =
  10351 + 15552n, take the inverse ray b_L = 64^L (8v+1) + 49(64^L - 1)/63 (ordinary tail (2, 6L+1, 1, 4) to q), the
  named centre-17 or centre-25 seven-arrow rotation applied maximally, then all point inverses, ending at eta. The
  full signed plan passes exactly when its canonical endpoint eta is below q, except the classified baseline
  self-returns, which never pass; every failure retains a nondecreasing request +1. Explicit integer bounds on j,
  k and b_L give a finite exhaustive decision over all L at each fixed entry (w = 6901 fails at every L). Also
  v3(b_L - b_M) = v3(L - M). For L >= 1 success needs k >= 10L or j >= 8L, and for every N >= 1 the number of
  accepted entries among n = 0..N-1 is at most S N + 5T^2 + 6T + 1 with T = floor(log2(15552 N)) and S < 1/500;
  so the limsup accepted fraction is below 1/500 (no density is asserted). This bounds only this specified
  procedure, not all inverse words, premature cycle stops, the existing rule union or other constructions.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [maximal-inverse-cycle-continuation, lifted-inverse-ray-cycle, two-selected-inverse-choices, critical-image-rank-composition]
certificates: [check_legacy_replay.py]
evidence:
  - "check_all_rays.py, all_rays.py, all_rays_audit.json: the legacy constructor and checker: 900 isometry comparisons, 15 finite permutations, 28 digit lifts, 576 affine checks, 66 full signed plans (12 descending, 22 nondecreasing failures, 32 baseline returns), all 1024 first entries exhaustively rejected, 16 rejections, and two supplied conversions stored in full (L = 1, w = 36641534965: 9 pair inputs, 102 rows; L = 3, w = 302362550859146911249525: 16 pair inputs, 443 rows). Fails at its new path: all_rays.py loads ../refined_obstruction/ (now ../exponent-eleven-fifteen-rule-classification/), ../critical_rank/ (now ../critical-image-rank-composition/), ../cycle_inverse/ (now ../maximal-inverse-cycle-continuation/) and ../selected_inverse/ (now ../two-selected-inverse-choices/) by their pre-migration folder names. Passed at be73a66 as experiments/residual_progress/all_ray_continuation/check_all_rays.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran every residual-progress step before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a); replayed unchanged, with its receipt, by check_legacy_replay.py"
  - "../exponent-eleven-exit-continuation/batch_r61_r67_check.py: side-lane probe of R61, R65, R66 and R67 (see reviewed_by)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: ../exponent-eleven-exit-continuation/batch_r61_r67_check.py
    scope: "Finite only (side-lane feed entry 2026-10-18 06:14, VERIFIED), with the lane's own step, nu and selected: the identity v3(b_L - b_M) = v3(L - M) on 2,990 random pairs. The acceptance criterion, the ray cutoff and the counting theorem were not rebuilt; the status stays written"
aliases: [R66]
tags: [convergence, outer-residual, tripling-pairs, critical-rank, inverse-rays, counting-bound]
---

# Every inverse-ray index of a two-rotation cycle/point procedure is decidable, and it accepts under 1/500 of its entry row

## Statement

Odd-only clock, 1 absorbing; `ρ(w) = ν(3w)`; formal plans with signed requests. Entry row: `v = 4089 + 6144n`, `w = 6901 + 10368n`, `q = ρ(w) = 10351 + 15552n` (`n ≥ 0`), the whole `3 | v` part of the R60 domain.

1. **Procedure.** For every ray index `L ≥ 0`, `b_L = 64^L(8v+1) + 49(64^L − 1)/63` has ordinary path `(2, 6L+1, 1, 4)` to `q`. Apply the named centre-17 (`L ≡ 0 mod 3`) or centre-25 (`L ≡ 1 mod 3`) seven-arrow rotation maximally, then all point inverses, ending at `η` (at `L ≡ 2 mod 3`, `k = j = 0`). The full signed plan passes iff `η < q`, except the classified baseline self-returns, which never pass; every failure keeps a nondecreasing request `+1`.
2. **Finite decision.** Explicit integer bounds on `j`, `k` and `b_L` (formula (9) of the note) make the search over all `L` exhaustive at each fixed entry; the entry `w = 6901` fails at every `L`. Independently `v3(b_L − b_M) = v3(L − M)`, so every ternary precision is attainable, but `b_L` grows like `64^L`.
3. **Counting.** For `L ≥ 1`, success needs `k ≥ 10L` or `j ≥ 8L`. For every `N ≥ 1`, at most `S·N + 5T² + 6T + 1` of the entries `n = 0, …, N−1` are accepted, with `T = ⌊log₂(15552N)⌋` and an explicit `S < 1/500`. So the limsup accepted fraction is below `1/500`; no natural density is asserted.

This bounds only the specified two-rotation maximal-cycle/point procedure: not other inverse words, premature cycle stops, forward or supplied-history methods, or the existing larger rule union. It extends [`maximal-inverse-cycle-continuation`](../maximal-inverse-cycle-continuation/README.md) (R60) and [`lifted-inverse-ray-cycle`](../lifted-inverse-ray-cycle/README.md) (R64).

## Proof

The legacy note "A complete all-ray decision and its integer-density obstruction" follows, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**Status: written proof and exact conditional constructor.** On the complete
entry progression below, every choice of ray index in a specified two-rotation,
maximal-cycle/point procedure can be decided by a finite, explicit search. The
limsup fraction of entries it accepts is less than **1/500**. This is an actual
integer-counting statement, not a probability assigned to an orbit. It leaves
other inverse words, premature cycle stops, forward excursions, supplied-history
methods and the existing larger rule union unrestricted. Collatz remains open.

The procedure extends [R60](../maximal-inverse-cycle-continuation/README.md) and
[R64](../lifted-inverse-ray-cycle/README.md). Use their ordinary odd-only clock,
absorbed at1, signed pair P(w)=[3w]-[w], elementary normal form nu and
rho(w)=nu(3w). In the formal absorption plan write

    [x] = div J_x + A_x,

where A_x is a signed sum of missing W5 pairs, not an available current.
All constructors below retain those coefficients. No external theorem or
novelty claim is used.

### 1. The entire ray and the exact procedure

Assume w>0, w=3445 mod3456 and v=(16w-13)/27 divisible by3. Equivalently,
for a unique integer n>=0,

    v=4089+6144n,  w=6901+10368n,  q=rho(w)=10351+15552n.       (1)

In particular v=-7 mod2048. For every integer L>=0 set

    b_L=64^L(8v+1)+49(64^L-1)/63.
    9b_L+7=8*64^L(9v+2).                                      (2)

These are complete quotient inverse-ray lifts of the same node3v. Their exact
ordinary paths to q have valuation word

    (2,6L+1,1,4).                                              (3)

Indeed S(b_L)=F^(3L)(6v+1), where F(x)=4x+1; its next successor is9v+2.
The last two valuations follow from v=-7 mod2048, including the extra binary
bit. Also b_L=1 mod8 and b_L=L+1 mod3.

The two named rotated seven-arrow words are

    C17=(1,1,1,2,1,1,4),   C25=(1,1,2,1,1,4,1).

Each has total valuation11 and affine action
Psi_c(x)+c=(2187/2048)(x+c). A positive odd target y has a legal inverse
copy precisely when3^7 divides y+c; the output plus c is then a positive
multiple of4096, giving both positivity and the extra valuation bit. Direct
substitution supplies all seven intermediate valuations.

Use c=17 when L=0 mod3 and c=25 when L=1 mod3. At L=2 mod3 neither
rotation nor a point inverse is legal, so use k=j=0. Otherwise set

    h=v3(b_L+c),  k=floor(h/7),  a=2048/2187,
    p=a^k(b_L+c)-c,
    j=v3(p+1),  eta=(2/3)^j(p+1)-1.                            (4)

Thus the cycle copies are maximal, followed by the maximal point-inverse run.
The full exact ordinary path eta to q is

    1^j, C_c^k, 2,6L+1,1,4.                                  (5)

Its length is j+7k+4 and its total valuation is j+11k+6L+8. Pair normalizers
have their own signed rows and do not alter this stated path clock.

For k>=1, v2(b_L+c)=1, so v2(p+c)=11k+1. Then v2(p+1) is4 for c17
and3 for c25; the corresponding odd parts are3 and1 modulo4 respectively.
The point endpoint is positive canonical,
eta=7 mod8, eta not2 mod3, and

    v2(eta+1)=4+j (c17), or3+j (c25).                          (6)

For k=0 the point endpoint has v2(eta+1)=j+1 and remains canonical.
At L=0 or2 mod3 it has j=0. At L=1 mod3 it has j>=1; for j>=2 it is7
mod8. The only remaining j1 cases have eta=3 mod8 and eta=0 or1 mod3.

Allowing the other named rotation at a given ray does not add successes:
its cycle count is zero. At L=0 or2 it returns the baseline. At L=1, if the
chosen center25 has positive cycles, b_L+1 has exact ternary order1, and the
alternative point-only endpoint(2b_L-1)/3 exceeds q. If its cycle count is
zero, both choices give the same point continuation. This observation does
not permit arbitrary early stops in a positive cycle run.

### 2. Complete current and failure vector

Let I be the negative current along(5), so div I=[q]-[eta]. Put z=nu(w), and
return

    J=N_(3w)+I-N_w+J_eta-J_z,
    coefficients=A_eta-A_z.                                  (7)

Then div J=P(w)-sum_u coefficients(u)P(u), with integer signs and
multiplicities combined exactly. The full failure classification is:

1. k0,j0 gives exactly the old R56 ray4,depth0 current and vector.
2. k0,j1,eta0mod3 gives that same exact current and vector.
3. In every other case H_eta has one highest request+1 of rank eta, at a
   W5 index. All its other requests are below eta, and all H_z requests are
   below q. Therefore the entire plan strictly decreases the original rho
   **if and only if eta<q**. A failure retains that nondecreasing request+1.

The first two cases retain the original P(w)+1 and never pass. Here is the
all-L justification of the less immediate second case. Write y=b_(L-1), so
b_L=64y+49. Put u=eta/3=(128y+97)/9. Then u=9 mod16,
v2(9u-1)=5, and z1=(9u-1)/32=4y+3. The complete W9 rule gives

    A_eta=A_(3z1)-A_z1+A_u.

The actual absorption recursion gives A_u=A_z1: S(u)=(32y+25)/3 is selected;
its elementary half m=(16y+11)/3 is1 mod8 and S(m)=z1. Moreover
3z1=F^2(S(y)), while nu(S(y))=3v. Thus A_eta=A_(3v). The same elementary
prefix identities, with their exact signed rows, give equality of the full
current in(7) to the old baseline. Case1 uses b_L's elementary equivalence to
3v directly. The executable checker compares the complete current tables,
not merely the displayed leading coefficient.

For case3, the critical index is eta/3 if eta0mod3 and(2eta+1)/3 if
eta1mod3. It is W5 and has rank eta. Its lower absorption terms lie below
eta by the R43 bound. Since w5mod8, z<w/4, so the same bound puts H_z
strictly below q. Consequently the leading coefficient cannot cancel when
eta>=q. Equality is allowed in this failure statement; no claim about the
nonexistence of positive cycles is being assumed.

An accepted plan is conditional on exact supplied currents for every nonzero
pair request. The compiler rejects missing or malformed supplies. This is
individual-pair composition, not annular source-capacity reuse.

### 3. Exact all-L ternary structure

For fixed v and distinct nonnegative L,M,

    v3(b_L-b_M)=v3(L-M).                                      (8)

Indeed C=9b_0+7=8(9v+2) is a ternary unit and(2) gives the difference
C(64^L-64^M)/9. The elementary identity
v3(64^d-1)=2+v3(d) follows by first checking d not0mod3 and then iterating
x^3-1=(x-1)(x^2+x+1); when x=1mod9 the second factor has exact ternary
order1. This proves(8), without a Diophantine estimate.

Thus L to b_L permutes every ring modulo3^H, with period3^H. For any integer
target and H>=1 there is exactly one L modulo3^H attaining it. The provided
digit-lifting routine uses modular powers only, even for enormous L.
For the point-only run,

    b_L+1=2*(4*64^L*(9v+2)+1)/9.

Therefore arbitrarily high ternary precision can be forced by choosing L.
It does **not** imply descent: b_L grows as64^L, and that growth must be
paid for in the actual endpoint comparison.

### 4. An explicit finite cutoff for all rays

Fix one entry w and its q. Define exact integers

    J=floor(log2(q-1))-1,
    P=floor(3^J*(q-1)/2^J),
    K=floor((floor(log2(P+24))-1)/11),
    B=floor(2187^K*(P+24)/2048^K)-17.                           (9)

Every accepted ray satisfies

    j<=J,  k<=K,  b_L<=B,
    64^L <= floor((9B+7)/(9b_0+7)).                            (10)

All floors are computed with integer arithmetic. Thus enumerate L from0
through the base64 logarithm of the last ratio, inclusive; if the ratio is
zero there is nothing to test. This is an exhaustive finite decision for
this procedure. An optional resource cap yields `capped`, never `exhausted`.

**Proof.** Acceptance requires eta<q, and both numbers are odd, hence
eta+1<=q-1. Every nonspecial endpoint has eta+1 divisible by2^(j+1), giving
j<=J. Therefore p+1=(3/2)^j(eta+1)<=P and p+c<=P+24. At k>=1,
2^(11k+1) divides p+c, proving k<=K; k0 causes no difficulty. Finally
b_L+c=(2187/2048)^k(p+c), which gives b_L<=B and then(10).

A convenient loose bound is L<=floor(log2 q). To see it, for q>=10351,
P+24<=q^2: use(3/2)^J<=2^J<=(q-1)/2. Also
(2187/2048)^K<2^K<=P+24, so B+17<=q^4. Since b_0>q and
b_L>=64^L b_0, this even gives L<(log2 q)/2 whenever a ray passes.
The looser bound is enough for the integer counting argument below.

**Complete finite failure witness.** At w6901, v4089 and q10351,

    J12, P1342874, K1, B1434024,
    floor((9B+7)/(9b_0+7))=43<64.

Only L0 can pass. There b_0=32713 and v3(b_0+17)=1, so k=j=0 and the
full vector retains P6901+1. Hence **every ray index fails** at this fixed
entry under the defined procedure. This does not assert that P6901 lacks a
current or that another arithmetic rule fails.

### 5. A uniform barrier and an actual integer counting theorem

For L>=1, acceptance requires

    k>=10L or j>=8L.                                          (11)

This includes all intercepts. From(2) and(4), with t=(2/3)^j,

    eta=lambda*(q-5/32)+t*(a^k*(c-7/9)-(c-1))-1,
    lambda=(256/81)*64^L*a^k*t.                               (12)

If k<10L and j<8L then

    lambda >= (256/81)*(2^124/3^78)^L >3,

where2^124>3^78 is a strict integer inequality. The bracket in(12) is
at least-(c-1), so eta>=lambda*(q-5/32)-25>q for q>=10351.
This contradicts acceptance. Special baseline endpoints already fail by
Section2 and do not evade(11).

Now count entries n=0,...,N-1 in(1), with N>=1. At each fixed L, b_L is
affine in n with coefficient8*64^L*6144, of exact ternary order1.
Consequently a condition b_L+c=0mod3^d is empty or one residue class of n
modulo3^(d-1). More generally the same holds after multiplication by a power
of2. Each such class has at most N/3^(d-1)+1 entries.

At L0, a success needs at least one cycle: this is one class of relative
frequency3^(-6). For each L>=1, use(11). The k>=10L branch requires

    3^(70L) divides b_L+c.

For each of the10L choices0<=k<10L, the j>=8L branch requires

    2^(11k)*(b_L+c)-(c-1)*3^(7k)=0 mod3^(7k+8L).               (13)

These necessary congruences also cover k0 points. We may ignore maximality
and impossible rows when obtaining an upper bound. Their total geometric
frequency is at most

    S=1/729 + 3/((3^8-1)*(1-3^(-7))) + 3/(3^70-1)
     =5474401375691434500242938334713773823
       /2992672595549719928868845243684796434880
     <1/500.                                                 (14)

To pass from residue frequencies to actual growing integer intervals, use
Section4. Every tested input in this interval has q<15552N, so any successful
ray has L<=T=floor(log2(15552N)). The number of congruence classes used is
at most1+T+sum_(L=1)^T10L=5T^2+6T+1. Thus, for **every N>=1**,

    number of accepted entries among n0,...,N-1
       <= S*N + 5T^2+6T+1.                                  (15)

In particular the limsup accepted fraction is at most S, and the liminf
failure fraction is at least1-S>499/500. We do not assert the existence of
a natural density. The search cutoff is what makes the discrepancy
O(log^2 N); summing infinitely many modular densities alone would not prove
this integer result.

This is a precise obstruction to making the specified all-ray cycle/point
procedure universal on this entry row. It is not an upper bound on the
accepted domain of the larger existing rule union, an obstruction to all
inverse paths, an orbit-hitting claim, or a proof of divergence.

### 6. Verification and next obligation

Run `python3 experiments/residual_progress/all_ray_continuation/check_all_rays.py`.
The replay checks modular isometry, digit lifts, exact affine/intercept
identities, full paths and signed vectors, complete finite decisions, source
multiplicities and supplied-current substitutions. Its receipt is finite
implementation evidence; Sections1–5 give the infinite quantifiers.

The conditional API `one_step(w)` exhausts the proved finite ray interval.
Accepted plans can be combined with other strict-rho rules. The present result
does not alter the frozen existing dispatcher. To enlarge coverage substantially,
a new operation must go beyond this named maximal-cycle/point procedure;
merely increasing the ray-index search cap cannot complete it.

The stored replay contains900 isometry comparisons,15 finite permutations,
28 modular digit lifts,576 exact affine checks and66 full signed plans:
12 descending,22 retaining a nondecreasing leading request and32 exact
baseline returns. All1024 first entry inputs are exhaustively rejected by
this scoped procedure; that finite fact is separate from(15). Two supplied
conversions are stored in full: w36641534965 at L1 uses9 pair inputs and
102 output rows; w302362550859146911249525 at L3 uses16 pair inputs and
443 output rows. Supply searches are capped at10000 ordinary arrows and4096
bits with cycle detection; those designated fixtures completed. The replay
also checks16 invalid/missing-input rejections and preserves the distinction
between a resource cap and mathematical exhaustion. Generation and default
receipt replay passed. Source hashes cover the constructor, checker and
named frozen dependencies; no previous receipt or dispatcher is modified.

## Certificates

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B12 migration; standard library). The legacy scripts of this folder load sibling modules by their pre-migration paths, so they no longer run here. This certificate calls `tools/legacy_replay.py`, which rebuilds the pre-migration layout in a temporary directory from `tools/legacy_paths.json`, runs the unmodified legacy scripts there without `-O` (as `scripts/verify_all.py` did at `be73a66`), and requires exit 0 and every copied file unchanged. It writes nothing in the repository. It replays: the legacy checker `check_all_rays.py` (about 4 s; the counts of section 6 of the note and both stored supplied conversions, compared with `all_rays_audit.json`). The commands in the legacy text name `experiments/residual_progress/all_ray_continuation/`.

## Remarks

- The counting bound is an integer statement about entries of one arithmetic row, not a probability for an orbit. The search bound is proved, not an experimental cap; an optional resource cap reports `capped`, never `exhausted`.
- No rule is added to [`seventeen-family-rho-dispatcher`](../seventeen-family-rho-dispatcher/README.md). Main-lane decision of the round: pivot away from enlarging the named inverse-ray search (archive/convergence-residual-progress/REPORT.md).
- Novelty undetermined (none claimed).

## History

- Migrated from `experiments/residual_progress/all_ray_continuation/ALL_RAY_CONTINUATION.md` (legacy ID R66) at commit `be73a66`, by the B12 migration (Claude, Opus 5.5). Note, scripts and receipt moved byte-identical; `check_legacy_replay.py` was added at the migration. Legacy status: "written theorem, conditional constructor and finite replay".
- Main lane (ChatGPT, Codex), 2026-10-18, from commit `a489973`. The batch's "independent model" proof and code reviews (archive/convergence-residual-progress/REPORT.md) were the main lane's own agents, not a different lane.
