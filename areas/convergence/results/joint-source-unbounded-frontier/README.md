---
id: joint-source-unbounded-frontier
kind: result
title: The complete joint-source interface of the R39 pair keeps an unbounded positive frontier on explicit families
status: written
claim: >
  Odd-only 3x+1 map S, absorbing at 1, killed atom; C(v) = [18v+3] - [v] for positive v = 3 mod 4 (the joint
  source of coupled-even-pair-recursion). (Interface) A two-row table gives both exact two-arrow endpoints for
  every such v (v = 3 mod 8: z = (9v+5)/2^(a+1), upper 9*2^(a-1) z - 7; v = 7 mod 8: z = (9v+5)/4, upper
  oddpart(9z-7)), with C(v) = div J + [y] - [z]; it is not a closed shrinking C family. (Block) On the whole
  class v = 3 mod 32 an exact prescribed block gives C(v) = div L + [q] - [u] with u <= (9v+5)/32 <= v/3 and q =
  2^s 3^(2j+3) u - 5 = 22 mod 27 (clocks 3+2j and 2); the residual pair is retained. (Expansion) For v_r =
  (2^(6r+5)-5)/9 the lower seed absorbs in two arrows while the canonical frontier q_r = 2*3^(4r+3) - 5 has
  q_r/v_r -> infinity; for every positive multiple r of 27 this embeds in an actual weight-1 residual root x_r =
  (2^(6r+15)-3365)/81 at cutoff N_r = 12*2^(6r+5), N_r < x_r < 9N_r/8, whose prescribed 4r+7-arrow prefix ends
  at q_r with q_r/x_r unbounded. This is a scoped failure of that proposed closure (it excludes only a linear
  height bound for the prescribed block), not a nontermination, an obstruction to other constructions, or a
  positive cycle.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [coupled-even-pair-recursion, elementary-bridge-quotient-normal-form]
certificates: [r42_joint_frontier_check.py, check_legacy_replay.py]
evidence:
  - "check_joint_frontier.py, joint_frontier.py, joint_frontier_audit.json, actual_r27_frontier_current.csv, actual_r27_lower_current.csv: the legacy constructors (interface, shadow_frontier, expanding_family, embedded_family, required_ray_family) and checker: 8192 whole-interface cases, 2048 full subdomain cases, 45 exact parameter pairs, 11 expansion examples, five d4 embeddings and four required-ray sources; the stored r = 27 comparison current is explicitly unfinished, its four-row lower absorption input is stored separately. Fails at its new path: joint_frontier.py loads ../even_pair_closure/even_pairs.py (now ../coupled-even-pair-recursion/) by its pre-migration folder name. Passed at be73a66 as experiments/residual_progress/joint_frontier/check_joint_frontier.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran every residual-progress step before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a); replayed unchanged, with its receipt, by check_legacy_replay.py"
  - "r42_joint_frontier_check.py, r42_joint_frontier_check.json: side-lane probe (Claude side lane, 2026-10-18) with its own S and nu; it imports nothing and passes at its new path, rewriting its receipt identically (listed under certificates). Passed at be73a66 as reviews/side_lane/r42_joint_frontier_check.py (archive/legacy-checker-run-be73a66.md)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: r42_joint_frontier_check.py
    scope: "Finite only (side-lane feed entry 2026-10-18 09:40, VERIFIED, main 9190ccf), with the lane's own S and nu, nothing imported from main: the two-case interface on all v = 3 (mod 4) below 2*10^5 plus 5,000 random 122-bit v (55,000 cases); the 3 (mod 32) block on 15,500 cases, the parametrization (4) conversely for 8,443 pairs (h, u) with h <= 39, the two arrows (5) on 3,000 random cases; the expanding family for r = 0..12; the embedding for r in {9, 18, 27, 36, 54, 81, 108}, including the four-arrow certificate (9), (10) and the identity for 81(q_r - x), and for 27 | r the bounds N_r < x_r < 9N_r/8 and p < N_r. The entry says: The retained-graph residual weight R_N(x_r) = 1 in (12) uses the annular residual machinery and is not checked. The status stays written"
aliases: [R42]
tags: [convergence, outer-residual, joint-source, even-pairs, scoped-obstruction, negative-cycle-shadow]
---

# The complete joint-source interface of the R39 pair keeps an unbounded positive frontier on explicit families

## Statement

Odd-only clock, 1 absorbing, `δ_1 = 0`; `C(v) = δ_(18v+3) − δ_v` for positive `v ≡ 3 (mod 4)`, the joint source retained by [`coupled-even-pair-recursion`](../coupled-even-pair-recursion/README.md).

1. **Interface.** For every such `v` a two-row table gives both two-arrow endpoints exactly (`v ≡ 3 (mod 8)`: `z = (9v+5)/2^(a+1)`, `a = v2((9v+5)/2) ≥ 2`, upper endpoint `9·2^(a−1)z − 7`; `v ≡ 7 (mod 8)`: `z = (9v+5)/4`, upper endpoint `(9z−7)/2^e`), and `C(v) = div J + δ_y − δ_z`. It is not a closed shrinking family of `C` states.
2. **The class `v ≡ 3 (mod 32)`.** With `t = (3v−1)/8`, `h = v2(3t+1)`, `u = S(t) ≤ (9v+5)/32 ≤ v/3`, `j = ⌊(h−2)/3⌋`, `s = h − 1 − 3j`, an exact prescribed block gives `C(v) = div L_v + δ_q − δ_u` with `q = 2^s·3^(2j+3)·u − 5 ≡ 22 (mod 27)`, clocks `3+2j` and `2`. The residual pair is retained; when `q` is critical it lies in the phase omitted by [`odd-h-pair-interface-compiler`](../odd-h-pair-interface-compiler/README.md).
3. **Expansion.** For `v_r = (2^(6r+5) − 5)/9` the lower seed absorbs in two arrows while the canonical frontier `q_r = 2·3^(4r+3) − 5` has `q_r/v_r → ∞`. For every positive multiple `r` of 27 the family embeds in an actual weight-1 residual root `x_r = (2^(6r+15) − 3365)/81` at the required cutoff `N_r = 12·2^(6r+5)`, `N_r < x_r < 9N_r/8`; its smaller half absorbs in four arrows and its prescribed `(4r+7)`-arrow prefix ends at `q_r`, with `q_r/x_r` unbounded.

This is a scoped failure of the proposed joint closure: it excludes only a linear frontier-height bound for that prescribed block. It exhibits no permanent nontermination, excludes no other bridge or current, and the negative-cycle shadow constants (`−5`, `−7`) are not a positive cycle. Full `C(v)` closure stays open.

## Proof

The legacy note "Complete joint-source interface and an expanding unfinished frontier" follows, lightly edited (headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**Status: written proof and bounded executable checks.** This gives a complete
arithmetic interface for the R39 source, then exhausts one previously unresolved
residue class. The resulting positive frontier need not decrease. This is a
scoped failure of that proposed closure, not a universal current construction,
an obstruction to other constructions, or a convergence/divergence claim.

Use the odd-only Syracuse map S, absorbed at1. Write delta1=0 and
div J=(I-P)J. A prefix current of length k from x has divergence
delta_x-delta_(S^k x). We retain signed currents and all positive residuals.
The relevant prior construction is [R39](../coupled-even-pair-recursion/README.md).

### 1. Complete two-arrow interface

For every positive v=3 modulo4 set

    C(v) = delta_(18v+3) - delta_v.

The following table covers every such v. Here a and e are exact valuations.

| Domain | Lower endpoint z=S²(v) | Upper endpoint y=S²(18v+3) | Upper/lower valuation words |
| --- | --- | --- | --- |
| v=3 mod8 | a=v2((9v+5)/2)>=2; z=(9v+5)/2^(a+1) | 9*2^(a-1)*z-7 | (2,1)/(1,a) |
| v=7 mod8 | z=(9v+5)/4; e=v2(9z-7)>=1 | (9z-7)/2^e | (2,e+1)/(1,1) |

Subtracting the two prefix currents gives exactly

    C(v) = div J + delta_y - delta_z.                         (1)

**Proof.** The upper first arrow always has valuation2 and endpoint
(27v+5)/2. In the first row its next arrow has valuation1 and endpoint
(81v+17)/4. Substitution of9v+5=2^(a+1)z gives the stated y.
In the second row, 9z-7=(81v+17)/4, so the upper second valuation is e+1.
The two lower arrows follow by direct substitution. All displayed endpoints
are positive odd integers. Telescoping gives (1).

In the first row a=2 exactly when v=11 mod16, and then z>v; for v=3 mod16
we have a>=3 and z<v. In the second row z>v. Thus even this complete local
classification does not supply a height-decreasing closed family of C states.

### 2. Exhausting the entire v=3 modulo32 class

For every positive v=3 mod32 define

    t=(3v-1)/8,   h=v2(3t+1)>=2,   u=S(t).

Then t=1 mod4 and the exact prefixes are

    S³(18v+3)=27*2^(h-1)*u-5,     upper word (2,1,2),
    S²(v)=u,                     lower word (1,h+2).         (2)

The lower closing valuation is h+2: S(v)=F(t)=4t+1. Moreover

    u <= (9v+5)/32 <= v/3,                                (3)

with equality in the second inequality only at v=3. The full parameterization
is

    v=(2^(h+3)*u-5)/9,
    h>=2, u positive odd, 2^h*u=4 mod9.                    (4)

Every pair (h,u) in (4) gives a positive v=3 mod32 and its exact valuation h.
Indeed division by9 is integral, and modulo32 gives v=-5/9=3; also
3t+1=2^h*u. Conversely (2) gives (4). Formula (3) follows from h>=2 and
u=(9v+5)/2^(h+3). The upper three arrows give (2) directly.

For any positive odd A,u and m>=4, the following two arrows are exact:

    A*2^m*u-5 --1--> 3*A*2^(m-1)*u-7
               --2--> 9*A*2^(m-3)*u-5.                   (5)

The first numerator has exactly one factor2 and the second exactly two,
since m>=4. The constants -5 and -7 shadow the negative3x+1 cycle; all actual
states in (5) are positive. This does not assert a positive cycle.

Put

    j=floor((h-2)/3),    s=h-1-3j in {1,2,3},
    q=2^s*3^(2j+3)*u-5.

Apply (5) j times after (2). This gives the complete finite block

    S^(3+2j)(18v+3)=q,      S²(v)=u,
    C(v)=div L_v + delta_q-delta_u.                        (6)

Here L_v is the upper prefix current minus the lower two-row prefix current.
Equation (6) keeps the unresolved pair. Exhausting the binary exponent
increases its ternary coefficient; the new pair is generally not C(u).
The lower parameter u alone cannot certify progress of the full signed state.

Every q in (6) satisfies q=22 mod27. When q is a critical canonical state,
it lies in R38's omitted phase: q=1 mod3, v3(q-1)=1, and the ternary unit
of q-1 is1. This identifies an unresolved interface, not a new impossibility
theorem for those targets.

### 3. Explicit expansion with an already absorbed lower source

For each integer r>=0 set

    h=6r+2,   v_r=(2^(6r+5)-5)/9,   u=1.

These are valid parameters in (4). Thus

    S²(v_r)=1,
    18v_r+3=2^(6r+6)-7,
    S^(4r+3)(18v_r+3)=q_r=2*3^(4r+3)-5.                   (7)

The upper word is (2,1,2)(1,2)^(2r), and the lower word is (1,6r+4).
The positive frontier is canonical: q_r=1 mod8. Since q_r=1 mod3, both the
R25 elementary normal form and the R34 decreasing inverse-chain normalizer
leave it unchanged. Its ordinary valuation2 arrow does decrease it to
`S(q_r)=(3^(4r+4)-7)/2`, but that endpoint still has unbounded ratio to
v_r. Further information is needed to absorb it; this note does not
exclude those subsequent ordinary steps.

In particular,

    q_r/v_r ~ (243/16)*(81/64)^r -> infinity.              (8)

Thus the prescribed complete block has no universal linear frontier-height
bound in v, even with its lower source absorbed. This does not exclude another
bridge, a richer rank with intermediate growth, or an unrelated decreasing
ancestor. Each r describes a different finite prefix.

### 4. Genuine complementary d4 roots and a required-ray family

For r>=0 divisible by9, v=v_r satisfies v=3 mod9. Define

    w=16v/3+1,     t0=(16w+1)/3,     x=4t0-1,
    p=(x-1)/2=(32w-1)/3.

Here w=17 mod128 and w=2 mod3. The seed x has a=2, odd t0=3 mod4 and exact
complementary run parameter d=v2(3t0-1)=4. It is the R39 A-entry with child v.
For the modular assertion, 2^54=1 mod81 gives v=3 mod9 when9 divides r.

The smaller half has the complete four-arrow absorption certificate

    p --5--> w --2--> F(v) --3--> S(v) --(h+2)--> 1.       (9)

The upper prefix is

    S³(x)=18w+1,
    S⁴(x)=F(2(18v+3)+1),
    S⁵(x)=F(S(18v+3)),
    S⁶(x)=S²(18v+3).

Combining with (7) gives

    S^(4r+7)(x)=q_r.                                     (10)

Its exact word is (1,2,2,1,3,3,2)(1,2)^(2r).
Subtracting the current in (9) from the prefix in (10) returns an explicit
**unfinished** comparison:

    delta_x-delta_p = div J_r + delta_(q_r).              (11)

Adding the supplied four-row absorption current of p merely leaves the upper
prefix and its positive frontier; it does not complete x's absorption.

There are actual residual sources on a required ray. For every positive
multiple r of27 set

    N_r=12*2^(6r+5),
    x_r=(2^(6r+15)-3365)/81.

These are the same x as above, and

    x_r=3 mod12,       N_r<x_r<9N_r/8,
    p<N_r,            R_(N_r)(x_r)=1.                    (12)

Indeed 2^162=1 mod243 and 2^15-3365=243*121 show3 divides x_r;
x_r=3 mod4 was already established. Also

    x_r/N_r=256/243 - 3365/(81N_r),

which is between1 and9/8 for r>=27. On this interval the retained-graph
residual has weight1 on3 mod12. Thus (12) uses its full actual coefficient.
No claim about the total mass of this sparse family is made.

Finally

    q_r/x_r ~ (2187/16384)*(81/64)^r -> infinity.          (13)

In fact q_r>x_r for r>=9: verify4374*81^9>32768*64^9 and use the increasing
ratio (81/64)^r in81(q_r-x_r)=4374*81^r-32768*64^r+2960.
The required-ray subfamily therefore has a smaller half with a four-arrow
certificate and an unresolved canonical frontier above the original root.
This is a concrete dependency failure for the prescribed joint block, not a
counterexample to Collatz or to the existence of another current.

### 5. Executable interface and evidence

[joint_frontier.py](joint_frontier.py) exports `interface`, `shadow_frontier`,
`expanding_family`, `embedded_family`, and `required_ray_family`. Every
constructor returns its full current and exact residual. It exposes only a
prescribed number of arrows; no absorption search is used.

Run the bounded checker:

```sh
python3 experiments/residual_progress/joint_frontier/check_joint_frontier.py
```

The checker compares the table with8192 exact two-arrow cases, the complete
block with2048 parameters,45 parameterized(h,u) cases, and11 expanding-family
instances. It checks five d4 embeddings and four actual required-ray roots.
The r=27 comparison current and its lower absorption input are stored as
[actual_r27_frontier_current.csv](actual_r27_frontier_current.csv) and
[actual_r27_lower_current.csv](actual_r27_lower_current.csv). Their replay
checks (11), including the positive residual; neither table is labeled as an
absorption certificate for x. The deterministic
[receipt](joint_frontier_audit.json) records clocks, sizes and hashes.

The proof establishes the infinite families. The finite checker only audits
their implementation and selected instances. Full C(v) closure and universal
completion of the remaining complementary roots stay open.

## Certificates

- [`r42_joint_frontier_check.py`](r42_joint_frontier_check.py): the side-lane probe, unchanged; it passes at its new path (under 1 s) and rewrites `r42_joint_frontier_check.json` identically. Its scope is under `reviewed_by`.
- [`check_legacy_replay.py`](check_legacy_replay.py) (written at the B11 migration; standard library). The legacy scripts in this folder load their sibling modules by pre-migration folder names, so they no longer run here. This certificate rebuilds the legacy directory layout in a temporary directory from the node folders that now hold those files, runs the unmodified legacy checks there without `-O` (as `scripts/verify_all.py` did at `be73a66`), and requires exit 0 and every copied receipt unchanged. It writes nothing in the repository. It replays: the legacy checker `check_joint_frontier.py` (under 1 s; the counts of section 5 of the note, the stored `r = 27` currents and their replay of (11), compared with `joint_frontier_audit.json`). The command in the legacy text names `experiments/residual_progress/joint_frontier/`.

## Remarks

- The R25 normal form and the R34 decreasing inverse-chain normaliser ([`decreasing-inverse-ancestry`](../decreasing-inverse-ancestry/README.md)) both leave `q_r` unchanged (section 3 of the note); the retained-graph residual weight in (12) is that of the B09 residual machinery ([`retained-graph-complement-constructor`](../retained-graph-complement-constructor/README.md)).
- The two arrows (5) are the 2-adic shadow of the negative cycle `{−5, −7}`; compare [`low-block-continuation-prescribed-growth`](../low-block-continuation-prescribed-growth/README.md) and [`negative-cycle-backward-word`](../negative-cycle-backward-word/README.md).
- Novelty undetermined (none claimed).

## History

- Migrated from `experiments/residual_progress/joint_frontier/JOINT_FRONTIER.md` (legacy ID R42) at commit `be73a66`, by the B11 migration (Claude, Opus 5.5). Note, scripts and receipts moved byte-identical; `check_legacy_replay.py` was added at the migration. The side-lane probe `reviews/side_lane/r42_joint_frontier_check.*` moved here. Legacy status: "written full arithmetic interfaces, explicit growing prefixes and actual required-ray examples; scoped failure of a proposed closure".
- Main lane (ChatGPT, Codex), 2026-10-17, from commit `4a45eb0`. The batch's "independent model" proof and code reviews (archive/convergence-residual-progress/REPORT.md) were the main lane's own agents, not a different lane.
