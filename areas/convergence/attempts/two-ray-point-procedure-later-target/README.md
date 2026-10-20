---
id: two-ray-point-procedure-later-target
kind: attempt
title: "The two-ray/point inverse procedure also fails at later Phi-exit targets"
status: written
claim: >
  Tried: at a later exit target y of the original coupled source Q (odd-only 3x+1 map, absorbing at 1; quotient T
  = nu S; native formal absorption), replace the native plan by either complete quotient inverse ray of y followed
  by its maximal point chain, or by the direct point chain, with native absorption at the origin, deciding all ray
  indices by the finite cutoff of R83. Verdict: at r = 4 (exit row 18, next valuation 3, S^78(Q) = y) all 23 ray
  candidates and the direct-point plan fail the original-rank test and the native W5 leader is not recognised by
  the fixed seventeen rules; at r = 8 (S^126(Q) = y) all 37 ray candidates fail, but the existing R44 forward rule
  repairs the native leader at the original rank. So the one-ray/point procedure is incomplete at later targets
  too; a failed inverse method is not a missing-current theorem. Words with several ray choices, further forward
  moves, later targets and supplied histories are not covered; no new accepted family.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [history-beyond-prescribed-growth, binary-return-exit-control, returning-forward-interface, seventeen-family-rho-dispatcher, common-critical-rank-basis]
certificates: [check_legacy_replay.py]
evidence:
  - "check_later_target_probe.py, later_target_probe_audit.json: the legacy probe and receipt: the complete r = 4 and r = 8 controls, both ray cutoffs, every shorter point stop against its maximal completion, the full signed vectors, and the verified R44 repair at r = 8. Fails at its new path: it loads ../phi_exit_control/ and ../resolved_rules/ (now ../../results/binary-return-exit-control/, ../../results/seventeen-family-rho-dispatcher/) by their pre-migration folder names, and its receipt pins the hashes of this note and of ../native_growth_escape/NATIVE_GROWTH_ESCAPE.md (now ../../results/history-beyond-prescribed-growth/README.md), both edited. Not reached at be73a66: the scripts/verify_all.py gate stopped earlier, at residual_progress/history_frontier (archive/legacy-checker-run-be73a66.md); it passed in full at 9dbc71a; A replay at this migration, before the note was edited, passed (exit 0, receipt unchanged). Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
  - "../../results/two-source-normalisation-first-departure/r93_r94_check.py: side-lane probe of R93, R94 and this probe, replayed by this node's check_legacy_replay.py (see reviewed_by)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: ../../results/two-source-normalisation-first-departure/r93_r94_check.py
    scope: "Finite only (side-lane feed entry 2026-10-18 07:33, VERIFIED): '**Paths.** `S⁷⁸(Q) = y` (cost 122) at `r = 4`, and `S¹²⁶(Q) = y` (cost 198) at `r = 8`.'; the r = 4 witness z = ν(y) > Q and its high native request; the ray cutoffs J = 122 and 196 with allowed indices L ≤ (11, 10) and L ≤ (18, 17); 'All 23 and 37 maximal endpoints, respectively, exceed `Q`.' 'The seventeen-family dispatcher result and the R44 repair are not checked here.'"
aliases: [R94-b]
tags: [convergence, outer-residual, inverse-ray, later-target, original-rank, procedure-limit]
---

# The two-ray/point inverse procedure also fails at later Phi-exit targets

## Idea

[`history-beyond-prescribed-growth`](../../results/history-beyond-prescribed-growth/README.md) (R83) decides the two complete quotient inverse rays, followed by point inverses and native absorption, over every ray index by a finite cutoff, and finds the procedure failing at a fixed H17 input. Its algebra does not depend on the target, so the same decision can be run at a genuinely later target: the maximal exits of the guarded return of [`binary-return-exit-control`](../../results/binary-return-exit-control/README.md) (R90). Perhaps the ternary precision gained by the returns lets one of these rays reach a smaller origin there. This is the third hypothesis of the R93/R94 batch.

## What happened

The legacy note "A later Phi-exit target still defeats the two-ray/point procedure" follows, lightly edited (title dropped, headings demoted one level, links pointed to nodes).

**Status: exact finite witness and a reusable probe for an existing method.**
The r4 witness retains a native W5 request unhandled by the fixed seventeen
rules. The existing R44 rule repairs the separate r8 control at the original
rank. This probe excludes native
absorption at one specified later target and the two complete quotient inverse
rays followed by any number of point inverses, with native absorption at their
origins. Multiple ray choices in one word, later targets, other comparisons,
and supplied histories remain available. No new theorem number, universal
terminal supply, or novelty claim is proposed.

The cutoff argument is the one already proved in
[R83](../../results/history-beyond-prescribed-growth/README.md), sections1–2. Its algebra
does not depend on the H17 target. This probe applies it to an arbitrary
positive canonical target y and odd threshold Q>=3. It does not repeat the
R92 same-target finite-window search.

### 1. What is decided, without a ray cap

Let T be the canonical quotient, and let H_x,A_x be the native formal
absorption identity

    [x]=div H_x+A_x.P.

All coefficients of A_x are nonnegative and have rank at most nu(x). Suppose
an actual finite comparison K has div K=[Q]-[y], and b=Q/3 is a critical
pair input. Then native absorption gives the complete conditional identity

    P(b)=div(K+H_y-H_b)+(A_y-A_b).P.                 (1)

Every negative request in A_b is below Q. No request is supplied by this
identity. The checker retains the full signed vectors in (1) and below.

For any canonical y>1, the complete quotient inverse table has two rays,
with bases

|y modulo3|a0|a1|
|---:|---|---|
|0|(8y+3)/3|(16y+3)/3|
|1|(4y-1)/3|(32y+19)/3|
|2|(64y+19)/3|(128y+83)/3|

Each base is canonical and1 modulo8. Each ray satisfies

    a_L=(64^L*(9a0+7)-7)/9,  L>=0.

After taking this inverse arrow, allow any number of consecutive point
inverses. Their maximal length and endpoint are

    h=v3(a_L+1),   p=2^h*(a_L+1)/3^h-1.             (2)

For h>=1, p is positive complementary canonical,3 modulo4, and not2
modulo3. Consequently H_p has a highest request of rank p with coefficient
+1. Its other requests are lower. The resulting comparison is admissible
at original Q exactly when p<Q: subtracting A_b cannot cancel that highest
request if p>=Q. No inference from the raw ray height replaces this test.

Let I be the sum of the h ordinary valuation-one arrows p to a_L and the
exact quotient bridge a_L to y. Thus div I=[p]-[y]. The full source identity is

    P(b)=div(K-I+H_p-H_b)+(A_p-A_b).P.               (3)

If h=0, H_(a_L) follows its free quotient arrow back to y, and (3) is
exactly (1). If 1<=j<h points are taken, the resulting canonical state is
2 modulo3; its native inverse descent completes the remaining points.
The full rows and coefficients therefore equal (3) for the maximal h.
If y=2 modulo3, also consider the maximal direct point-only chain from y.
It has the same formula (2) with a_L replaced by y. This can differ from
native H_y: at y=1 modulo8 native priority takes a free forward arrow first.
Every nonempty shorter point stop has the same completion as its maximal
chain. The baseline, direct point-only comparison, and maximal ray endpoints
therefore exhaust this chosen method.

For h>=1 and p<Q, both p and Q are odd, and

    2^(h+1) divides p+1,  p+1<=Q-1.

Define, using exact integer arithmetic,

    J=floor(log2(Q-1))-1,
    Pmax=floor(3^J*(Q-1)/2^J).

There is no successful ray endpoint when J<1. Otherwise h<=J and
a_L+1=(3/2)^h*(p+1)<=Pmax. Hence every successful index satisfies

    64^L <= floor((9*Pmax-2)/(9*a0+7)).              (4)

The two right sides are finite explicit integers. The probe enumerates
exactly those possible ray indices, without an arbitrary search cap. All
larger indices fail (4). The argument is inherited from R83; the executable
reuse for a general canonical target is the change here.

### 2. An r4 native leader unhandled by the fixed seventeen rules

Take r=4, exit guard order18, next valuation3, and index0 in R90's exact
exit progression. The ordinary source and later target are

    Q=10700808724915244204246595675625106715,
    y=33053313160223488220607297455181106259,
    S^78(Q)=y, with valuation sum122.

The canonical target is

    z=nu(y)=16526656580111744110303648727590553129>Q.

The checker retains the exact elementary normalizer from y to z, including
its negative rows. Thus its comparison current has divergence [Q]-[z];
no equality of ordinary clocks at z is assumed.

The native comparison retains exactly the high request

    +P(8263328290055872055151824363795276565),

of rank12394992435083808082727736545692914847>Q. The fixed seventeen-family
dispatcher returns no rule for this W5 input. Its direct point-only origin is

    p=(2z-1)/3=11017771053407829406869099151727035419>Q.

Here z=1 modulo8, so this point comparison differs from native H_z; both
full signed plans are retained. Its high request is
`+P(3672590351135943135623033050575678473)`, a W9 input with rank p.
The two complete rays from z satisfy cutoff
L<=11 and L<=10 respectively. All23 maximal-point endpoints exceed Q, and
all shorter positive point stops give the same current as their maximal
completion. The complete high vectors appear in the receipt.

This is a specific failure of native and one-ray/point comparisons. Only the
native W5 leader is tested against the fixed seventeen rules. Further
expansion of other high pairs, W9 repair, multi-ray words and later targets
are outside this probe; their possibilities are not ruled out.

### 3. The r8 control and its existing repair

Use the complete original coupled family and exit parameters of
[R90](../../results/binary-return-exit-control/README.md). Take r=8, exit guard order18,
next valuation3, and index0 in that complete exit progression. Then

    Q=210065029006409577911756714191833302426696026205209908227355,
    y=685003375529270486518611195608212623248313116517585840060299.

There are exactly eight guarded Phi re-entries. The subsequent exit is the
entire h18 row with its next exact valuation3. Its actual ordinary path is

    S^126(Q)=y,

with valuation sum198. The target y is canonical and y>Q. The same r8 source
is used for every comparison below. Its complete original-source parameters,
valuation word, native comparison, and all signed request vectors are stored
in the receipt.

Both the native plan at y and its direct point predecessor retain the high
request

    +P(304445944679675771786049420270316721443694718452260373360133),

whose rank is

    (2y-1)/3
      =456668917019513657679074130405475082165542077678390560040199>Q.

The two complete inverse rays start at (64y+19)/3 and (128y+83)/3. Here
J=196, and (4) allows respectively L=0,...,18 and L=0,...,17. All37 possible
ray indices were tested. Every maximal-point endpoint with h>=1 is above Q.
The smallest p-Q among all37 endpoints, including h0 controls, is

    12779628610659756684959685217341680145837611961091232688471660>0.

The positive point depths occur exactly at

|Ray|L and h|
|---|---|
|0|(1,1),(4,3),(7,1),(10,1),(13,2),(16,1)|
|1|(0,2),(3,1),(6,1),(9,2),(12,1),(15,1)|

The other25 rays return the native baseline. Every shorter positive point
stop is checked against its maximal completion, with exact current rows and
signed vectors. Each high coefficient is retained; the receipt does not
silently discard negative lower inputs or count a conditional leaf as supplied.

This is a complete failure witness for the specified one-ray/point/native
procedure at a genuinely later target. It does not cover words with two or
more ray choices or further forward movement.

**Existing repair control.** The seventeen-family dispatcher accepts its
sole native high input by `R44_returning_forward`. That rule's26 signed
requests are all below this original Q. Substituting its full current into
(1) therefore gives a descending conditional plan for this same witness.
The checker verifies the complete boundary and retains all resulting signed
premises. This is an already available repair, not a new accepted family or
supplied terminal current. It also provides a concrete control against
misreading a two-ray/point failure as absence of a valid current comparison.

### 4. Why the proposed tuned subfamily was not promoted

For this exit row, a prescribed ordinary predecessor exponent can be tuned
to the fixed ternary digits of y, and the remaining source digits can force
an arbitrarily long point prefix. Sufficiently many points make that tuned
origin smaller than Q. This reproduces R83's source-tuning mechanism and
does not give coverage for an arbitrary fixed source. The witness above
shows why an existence statement for such subprogressions cannot be promoted
to a whole-row repair.

The whole-row constructive obligation still requires a closed domain, a
decreasing quantity, and every terminal signed premise supplied or below the
original Q. The existing R44 repair handles this witness, and the two-ray
probe alone does not establish coverage of the remaining row inputs.

### Reproduction

Run `python3 experiments/residual_progress/later_target_probe/check_later_target_probe.py`.
Default replay verifies the stored receipt; `--write` refreshes it. The
checker independently evaluates ordinary arrows and all current divergences,
derives the two ray cutoffs, checks every shorter stop, and pins its reachable
local source files. It searches for no absorption current and modifies no
dispatcher. Resource exhaustion is an error, never a negative mathematical
conclusion.

Certificate: [`check_legacy_replay.py`](check_legacy_replay.py) (written at the B13 migration; standard library) replays, in a temporary copy of the legacy layout built by `tools/legacy_replay.py`, the side-lane probe `r93_r94_check.py` from [`two-source-normalisation-first-departure`](../../results/two-source-normalisation-first-departure/README.md) (about 2 s, receipt reproduced byte for byte), which checks both paths, the ray cutoffs and all 23 and 37 maximal endpoints independently. The legacy probe `check_later_target_probe.py` pins the hashes of edited notes and is evidence only. The command in the legacy text names `experiments/residual_progress/later_target_probe/`.

## Why it fails

At the r = 4 control every one of the 23 admissible ray candidates and the direct point-only plan keeps a high request above the original `Q`, and the native W5 leader is outside the fixed seventeen rules of [`seventeen-family-rho-dispatcher`](../../results/seventeen-family-rho-dispatcher/README.md). At r = 8 all 37 ray candidates fail as well. The procedure (one ray choice, then points, then native absorption) is therefore incomplete at later targets too. This is a limit of that procedure, not a theorem that no current exists: at r = 8 the existing rule of [`returning-forward-interface`](../../results/returning-forward-interface/README.md) (R44) already repairs the native leader at the original rank.

## What survives

- The finite ray cutoff of R83 applies to an arbitrary canonical target `y` and odd threshold `Q ≥ 3`; the executable reuse is the change here.
- The distinction between the direct point-only comparison and native priority at `y ≡ 1 (mod 8)`; both full signed plans are kept.
- A tuned ordinary predecessor exponent can force arbitrarily long point prefixes on subfamilies (R83's source-tuning mechanism), but this gives no coverage of a fixed source and was not promoted to a whole-row repair.
- The whole-row obligation is unchanged: a closed domain, a decreasing quantity and every terminal signed premise supplied or below the original `Q`; see [`residual-pair-864z-257-supply`](../../questions/residual-pair-864z-257-supply.md).

## History

- Migrated from `experiments/residual_progress/later_target_probe/LATER_TARGET_PROBE.md` (the ledger reports it inside R94; alias R94-b here) at commit `be73a66`, by the B13 migration (Claude, Opus 5.5). Note, probe and receipt moved byte-identical; the note became this README. Legacy status: "exact finite witness and a reusable probe for an existing method".
- Main lane (ChatGPT, Codex), 2026-10-18, first committed in `9190ccf`. The REPORT records independent proof, source and default-replay review by the main lane's own agents.
