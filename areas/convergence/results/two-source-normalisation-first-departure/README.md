---
id: two-source-normalisation-first-departure
kind: result
title: "Both original histories normalise the coupled pair to [864z - 257] - [z], with a complete first-departure interface for the lower path"
status: written
claim: >
  Odd-only 3x+1 map S, absorbing at 1. On the entire original coupled family put z = 471104208005 + 2^14 3^16 ell;
  then v0 = 144z - 43, Q = (2^31 z - 665034679)/3^15, and the actual ordinary paths satisfy S^18(Q) = 864z - 257
  and S^16(Q/3) = z, so P(Q/3) = div(I(Q,18) - I(Q/3,16)) + [864z-257] - [z] exactly, with no helper current
  assumed. The upper return is conjugate to Psi(z) = (3^12 z - 53)/2^19; with n = v2(7153z - 53), one complete
  re-entry is legal exactly when n >= 33, the maximum count is floor((n-14)/19), and n = 19r + h - 4 at the upper
  exit h in 18..36; integrality of Psi(z) gives no lower-source path to it, leaving the explicit defect [Psi(z)] -
  [z]. The rational lower shadow from 53/7153 has a complete 448-state certificate (71-step/cost-146 preperiod,
  377-step/cost-739 cycle, every state below 115, every prefix slope at most 1, extended to all prefixes by the
  cycle contraction); hence the actual lower path follows it while the cumulative cost stays below n, and its
  first departure is classified exactly (short branch, or long branch with an arbitrary extra j >= 1), with
  complete extra-bit cylinders for every row and every upper repetition count. Every matching lower state is below
  z + 115, and the last matching state and its next 12 arrows stay below the ORIGINAL Q. The signed comparisons
  keep a residual upper source above Q and a lower source below Q; they supply neither the residual current nor a
  new accepted domain.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [retained-history-w9-reduction, binary-return-exit-control]
certificates: [r93_r94_check.py, check_legacy_replay.py]
evidence:
  - "check_two_source_history.py, two_source_history.py, two_source_history_audit.json: the legacy constructor, checker and receipt: the complete 448-state rational certificate, 64 initial identities, 3520 exact departures, 180 joint upper/lower cases through r = 128, 739 periodic phases, three full unfinished tables, 19 rejection controls. It imports only its sibling module, but its receipt pins the SHA-256 of this node's legacy note TWO_SOURCE_HISTORY.md by file name, which is now an edited README, so it fails at its new path and in a legacy replay at earlier migrations (before rewritten notes were restored from git). Not reached at be73a66: the scripts/verify_all.py gate stopped earlier, at residual_progress/history_frontier (archive/legacy-checker-run-be73a66.md); it passed in full at 9dbc71a; A replay at this migration, before the note was edited, passed (exit 0, receipt unchanged). Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
  - "r93_r94_check.py, r93_r94_check.json: side-lane probe (Claude side lane, 2026-10-18 07:33, with the 07:36 update) of R93, R94, the later-target probe and the scaling remark of the R92 template; prescribed-ternary-child-unbounded-clocks and the attempt two-ray-point-procedure-later-target replay it from this folder. It imports nothing from the repository and passes at its new path. Passed at be73a66 as reviews/side_lane/r93_r94_check.py (archive/legacy-checker-run-be73a66.md, exit 0)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: r93_r94_check.py
    scope: "Finite only (side-lane feed entry 2026-10-18 07:33, VERIFIED, main working copy on 61fd041, committed unchanged as 9190ccf), with the lane's own integer and rational Syracuse code: '**Cell identities.** `v = 144z − 43`, `Q = (2³¹z − 665034679)/3¹⁵` and `Y(z) = 864z − 257 = 6v + 1` hold as affine identities in `ℓ`'; the upper coordinate identities and the return criterion on exact orders n = 14..80; the lower shadow ('448 states: preperiod 71 (cost 146) and cycle 377 (cost 739)', largest numerator 819533 < 115·7153); the departures for every exact order n = 14..1000 and 1,584 long-branch cases; 209 joint cases. Finite instances; the all-n classification rests on the written argument. The status stays written"
aliases: [R93]
tags: [convergence, outer-residual, retained-history, two-source, rational-shadow, original-rank]
---

# Both original histories normalise the coupled pair to [864z - 257] - [z], with a complete first-departure interface for the lower path

## Statement

Odd-only clock `S`, 1 absorbing; only ordinary steps are used. `I(x, t)` is the current of the first `t` ordinary arrows from `x`.

1. **Two-source normalisation.** On the original coupled family of [`retained-history-w9-reduction`](../retained-history-w9-reduction/README.md) (R89) and [`binary-return-exit-control`](../binary-return-exit-control/README.md) (R90), put `z = 471104208005 + 2^14·3^16·ℓ`. Then `v = 144z − 43`, `Q = (2^31·z − 665034679)/3^15`, `S^18(Q) = 864z − 257` (word of length 18, cost 26) and `S^16(b) = z` for `b = Q/3` (length 16, cost 31), so `P(b) = div(I(Q, 18) − I(b, 16)) + [864z − 257] − [z]`, with no helper current.
2. **Upper coordinate.** `Φ(144z − 43) = 144Ψ(z) − 43` with `Ψ(z) = (3^12·z − 53)/2^19`. With `n = v2(7153z − 53)`, one complete guarded re-entry is legal iff `n ≥ 33`; the maximum count is `⌊(n − 14)/19⌋`, and `n = 19r + h − 4` with exit row `h ∈ 18..36`. Integrality of `Ψ(z)` gives no lower path to it: `[Y(z)] − [z] = div I(Y(z), 12) + ([Y(Ψz)] − [Ψz]) + ([Ψz] − [z])`, with the last defect a missing comparison.
3. **Lower shadow certificate.** The rational orbit of `53/7153` has 448 states: preperiod 71 (cost 146), cycle 377 (cost 739), every numerator below `115·7153`, every prefix with `3^i ≤ 2^(E_i)`; the cycle multiplier `3^377/2^739 < 1` extends the slope bound to all prefixes.
4. **First departure.** Along every matching prefix `x_i = (3^i/2^(E_i))(z − 53/D) + N_i/D < z + 115`. The first differing valuation is exactly `n − E_i` (short branch) or `e + j` with an arbitrary `j ≥ 1` (long branch), and every row has a complete extra-bit cylinder in `ℓ`, for every upper repetition count.
5. **Window below Q.** The last matching state and its next 12 actual arrows (the departing one and at most eleven more) stay below the original `Q`.

The full signed comparisons keep a positive residual source above `Q` and a negative one below `Q`; they are unfinished.

## Proof

The legacy note "The actual lower history and a complete two-source exit interface" follows, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**Status: written arithmetic proof, exact finite rational-orbit certificate,
and unfinished comparison currents. No terminal pair current or new accepted
domain is supplied.** Ordinary steps below use the odd-only Syracuse map S,
absorbed at1. The quotient clock is not used in this package.

The [retained-history family](../retained-history-w9-reduction/README.md) and
[guarded upper return](../binary-return-exit-control/README.md) leave a positive
high source. This note retains the actual lower-source path instead of
immediately replacing it by its formal absorption plan. It gives a common
coordinate for both sources and completely specifies the lower path's first
departure from its forced rational itinerary. The final positive source still
needs a comparison or supplied current.

### 1. Exact normalization of both sources

For every integer ell>=0 put

    Q=70506316836123+3*2^45*ell,  b=Q/3,
    v=67839005952677+2^18*3^18*ell,
    z=471104208005+2^14*3^16*ell.

Then

    v=144z-43,
    Q=(2^31*z-665034679)/3^15,
    Y(z)=864z-257=6v+1.

The following two complete ordinary valuation words hold on the entire cell:

    from Q: (1,2,1,1,1,1,1,2,2,1,1,2,2,1,1,3,1,2),
    from b: (2,1,1,2,2,1,1,2,2,1,3,2,1,5,2,3).

Their lengths/costs are respectively18/26 and16/31, and

    S^18(Q)=Y(z),   S^16(b)=z.                         (1)

These are identities for actual integer paths. Verification at ell0 and the
exact word-cylinder modulus2^(cost+1) prove them for the whole cell: both
source periods are divisible by2^45, exceeding both required precisions.
Alternatively one may compose each displayed affine branch directly.

Let I(x,t) be the current of the first t ordinary arrows from x, so its
divergence is [x]-[S^t(x)]. With P(b)=[3b]-[b], (1) gives

    P(b)=div(I(Q,18)-I(b,16)) + [Y(z)]-[z].           (2)

No helper pair is assumed in (2). Its two-atom residual is explicit and is
not claimed to have a supplied current.

### 2. A legal coordinate for every guarded upper return

Write

    A=3^12=531441, M=2^19=524288, D=A-M=7153,
    Psi(z)=(Az-53)/M,  C(z)=Dz-53.

The earlier map Phi(v)=(Av+299947)/M obeys

    Phi(144z-43)=144Psi(z)-43,
    7153v+299947=144C(z),
    C(Psi(z))=(A/M)C(z).                             (3)

The broad upper guard is n=v2(C(z))>=14. One complete return into that guard
is equivalent to n>=33. On it Psi(z) is a positive odd integer greater than z,
and the twelve-arrow word

    (1,1,1,1,3,1,4,1,2,1,1,2)

maps Y(z) to Y(Psi(z)). Its cost is19. The word itself already holds at n>=15;
the stronger condition n>=33 is what returns to the broad guard. This
distinction preserves the exact valuation bit and the exit boundary.

For the original cell, n is finite and at least14. The exact maximum number
of guarded upper re-entries and the last upper exit order h are

    r=floor((n-14)/19),  h=18+(n-14 modulo19),
    n=19r+h-4,  18<=h<=36.                           (4)

All z_i=Psi^i(z), 0<=i<=r, are integers; only z_0 is asserted to lie in the
original ternary progression. The original upper path reaches Y(z_i) in
18+12i ordinary arrows.

Coordinate integrality supplies no lower-source path to z_i. Indeed the
exact one-return decomposition is

    [Y(z)]-[z] = div I(Y(z),12)
                  + ([Y(Psi(z))]-[Psi(z)])
                  + ([Psi(z)]-[z]).                 (5)

The final defect in (5) is a missing comparison. A direct fixed ordinary
word z->Psi(z) on an infinite arithmetic progression is impossible: every
nonempty forward word has a positive affine intercept, whereas Psi's
intercept is -53/M. This statement does not exclude variable words,
unequal-time mergers, or signed comparisons using additional sources.

### 3. A finite certificate controls every forced lower prefix

Consider the positive odd-denominator rational Syracuse orbit starting at
53/D. Its numerator map is

    N -> (3N+D)/2^v2(3N+D).                          (6)

All numerators are positive and odd; the denominator remains D. The stored
finite certificate contains448 distinct states before the first repeat:

- preperiod71, total valuation cost146;
- cycle377, total valuation cost739;
- repeated entry numerator7817;
- maximum numerator819533, hence every rational state is strictly below115.

For every prefix among these448 states, if i is its ordinary length and E_i
its total valuation cost, exact integer comparison gives

    3^i <= 2^E_i.                                   (7)

The cycle multiplier3^377/2^739 is strictly below1. Thus (7) holds for every
prefix of the infinite eventually periodic itinerary: every further cycle
multiplies the already checked slopes by this smaller factor. This extension
is a proof from a finite exact certificate, not an inference from an arbitrary
bounded orbit scan. The certificate asserts a rational cycle, not a positive
integer Collatz cycle.

Write the original integer z as

    z=(53+2^n*t)/D,   n=v2(C(z)),  t positive odd.

Along any matching prefix i, with rational numerator N_i and cost E_i,

    x_i = (3^i*2^(n-E_i)*t+N_i)/D
        = (3^i/2^E_i)*(z-53/D)+N_i/D.               (8)

Whenever E_i<n the complete valuation word is forced: its last exact bit
has not exhausted the binary precision. From (7), (8), and N_i/D<115,

    0<x_i<z+115<Q.                                  (9)

This holds for arbitrarily many rational shadow cycles when n grows; each
actual positive integer has finite n and therefore eventually leaves the
forced itinerary. No claim is made about its entire subsequent trajectory.

### 4. Complete first-departure classification and cylinders

Let i be the unique index with

    E_i<n<=E_i+e,   e=v2(3N_i+D),
    N_next=(3N_i+D)/2^e,  a=n-E_i.

All earlier arrows have exactly the shadow valuations. At the next arrow:

1. **Short branch, a<e.** The actual valuation is exactly a, and

       S(x_i)=(3^(i+1)*t+2^(e-a)*N_next)/D.

2. **Long branch, a=e.** Put

       j=v2(3^(i+1)*t+N_next)>=1.

   The actual valuation is e+j and

       S(x_i)=(3^(i+1)*t+N_next)/(D*2^j).

Both assertions follow by factoring2^a or2^e from3x_i+1. In particular this
is the first differing valuation, including the case where the shadow cost
equals n. The parser does not silently accept a word at the missing extra bit.

Every exact order n>=14 is realized on the original ell progression. In a
short branch no further binary choice is necessary. In a long branch every
j>=1 is realized, with its full exact congruence

    t = (2^j-N_next)*3^(-(i+1)) modulo2^(j+1).        (10)

The residue in (10) is odd. Combining z=(53+2^n*t)/D with the original z
progression gives one complete ell cylinder modulo2^(n+j+1-14). For short
branches the complete exact-order ell modulus is2^(n+1-14). The odd cofactor
3^16 of the z period is invertible modulo these powers of2. The construction
therefore gives every claimed cylinder, including arbitrarily large n and j;
there is no unproved existence assumption or finite search in this step.

Together with (4), this classifies the lower first departure for every upper
return count and every upper exit row. There is a finite eventual phase
description: after shadow cost146, replacing n by n+739 adds377 lower arrows
with the same local departure type; the upper exit row advances by739 modulo19.
Since gcd(739,19)=1, replacing n by n+19*739 preserves both phase labels and
adds19 shadow cycles and739 upper returns. The free long-branch valuation j
is unbounded and remains explicit. Finite phase labels alone do not prove
termination after these departures.

### 5. The first departure and eleven further arrows remain below Q

For every positive odd x and integer t>=0,

    S^t(x)+1 <= (3/2)^t*(x+1).

It also holds at the absorbing state1. Applying it to the last matching state
x_i<z+115 shows that, for every t=0,...,12,

    S^t(x_i) < (3/2)^t*(z+116)-1 < Q.                (11)

The count12 begins at x_i: it includes the first departing arrow and at most
eleven further arrows. It does not mean twelve arrows after departure.

For the last strict inequality it is enough to test t12. After multiplying
by3^15*2^12, its slope in z is

    2^43-3^27=1170495537221>0.

At the least z=471104208005 the exact positive difference is
551425372148651686473501. This proves the inequality for every positive member
of the original progression, retaining its affine intercept. Nothing after
the twelfth arrow is covered by this estimate.

Thus, for any 0<=j<=r and any0<=t<=12, the actual paths give the full signed
comparison

    P(b)=div(I(Q,18+12j)-I(b,16+i+t))
           +[Y(Psi^j(z))]-[S^t(x_i)].               (12)

The negative residual source in (12) is below the original Q. The positive
one is above Q. The code stores both sources and every signed current row.
These are unfinished comparisons, not supplied pair currents. Assuming
absorption below Q could discharge the negative source, but would still leave
the positive source's continuation unresolved.

### 6. What this does and does not complete

This is an exact normalization and a complete first-departure interface for
the retained lower source across all upper guarded return counts. It does not
supply the missing defect in (5), show a common future for the residual pair,
or prove that a later continuation decreases the original rank. The lower
path remains below Q throughout its forced shadow prefix and the stated
departure window, so that path has not yet produced a high negative frontier
that could cancel the upper residual.

The next constructive question is a comparison after this complete departure
interface, with an explicit well-founded parameter or supplied lower inputs.
Any use of an absorption or pair current beyond the actual displayed paths
must state and supply it. The negative controls and the distinction between
changing sources and one fixed source remain in force.

### Reproduction

Run from the repository root:

    python3 experiments/residual_progress/two_source_history/check_two_source_history.py

The default checker compares a stored receipt. `--write-receipt` regenerates
only that receipt inside this directory. It independently verifies the finite
rational orbit, exact integer paths and divergences, all departure branches,
complete valuation bits, and rejected invalid or capped requests. The stored
path comparisons are explicitly unfinished. No dispatcher or frozen earlier
result is modified by this package.

## Certificates

[`r93_r94_check.py`](r93_r94_check.py) (the side-lane probe; it imports nothing from the repository and passes in place, about 2 s): the cell identities, the upper coordinate and return criterion, the 448-state lower shadow, the departures for every exact order `n = 14..1000`, the 209 joint cases, the R94 centres and cylinders, the later-target controls and the scaling remark, against `r93_r94_check.json`. The legacy checker `check_two_source_history.py` pins the hash of this node's note, now an edited README (see `evidence`). The command in the legacy text names `experiments/residual_progress/two_source_history/`.

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B18-replay-revival migration; standard library) replays the unmodified legacy check `check_two_source_history.py` in a temporary copy of the legacy layout built by `tools/legacy_replay.py`, requiring exit 0 and every file unchanged (about 17 s). It checks finite steps only; the status is unchanged.

## Remarks

- The next obligation, a comparison after this departure interface that supplies the positive residual with a proved original-rank decrease or another terminating construction, is the question [`residual-pair-864z-257-supply`](../../questions/residual-pair-864z-257-supply.md), the line's final open target.
- Assuming absorption below `Q` could discharge the negative source, but would still leave the positive source unresolved.
- No novelty is claimed.

## History

- Migrated from `experiments/residual_progress/two_source_history/TWO_SOURCE_HISTORY.md` (legacy ID R93) at commit `be73a66`, by the B13 migration (Claude, Opus 5.5). Note, scripts and receipts moved byte-identical; the note became this README, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Legacy status: "written arithmetic proof with a finite rational-orbit certificate; unfinished comparison currents".
- The side-lane probe `reviews/side_lane/r93_r94_check.*` moved here.
- Main lane (ChatGPT, Codex), 2026-10-18, first committed in `9190ccf`. The batch's "independent" proof, source and default-replay reviews recorded in archive/convergence-residual-progress/REPORT.md were the main lane's own agents, not a different lane.
