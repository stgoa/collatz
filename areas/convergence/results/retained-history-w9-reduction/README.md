---
id: retained-history-w9-reduction
kind: result
title: "Retaining the strict lower history gives a sharp three-node critical-nine reduction on a larger window"
status: written
claim: >
  Odd-only 3x+1 map S, absorbing at 1; retained critical basis of R75. For odd Q >= 11547 and C in W9 with Q <= 3C
  and 3C+1 < 4Q, keep the original lower history H_C and only the actual upper prefix U from 3C to F (F = 4(3z)+1
  for odd d, 6z+1 for even d): the plan U + J_F - J_C has request vector A_F - A_C, every lower request strict at
  Q and at most one request of rank >= Q, with coefficient +1; a high W9 index z obeys 16z < 9C and 4z < 3Q, so
  the R87 window applies, and at most three W9 nodes leave only lower premises and possibly one higher W5 input.
  The family C = 585 + 4096j, Q = 441 + 3072j, j >= 4 needs all three nodes for this procedure (j = 4: 16969 ->
  9545 -> 5369 at Q = 12729); sharpness among all constructions is not asserted, and the boundary C = 15401, Q =
  11551 is rejected. On R88's retained cell the first H4 block has second depth d = 2 + v2(E), E = 162818633 +
  3^22 m; on the subcell m = 2736 + 4096l the high vector +P(a) - P(b) has an exact strict plan for P(b) from the
  retained lower history, whose substitution with its negative coefficient cancels to the upper-only plan, an
  actual 25-arrow path Q -> X; the inherited lower zero-source relations D + E0 + Fv remain explicit. The finite
  continuation on that subcell ends in zero or one high W5 request (l = 4, l = 13 remain unresolved), and the
  proposed recurrent contraction fails (slope 3^12/2^19 > 1; the named point inverse returns to Z). Conditional on
  every signed terminal input; no supply.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [common-critical-rank-basis, critical-nine-elimination, failed-w9-leader-reduction, complementary-run-bridges, returning-forward-interface, later-target-twenty-step-descent, four-target-history-classification, signed-pair-frontier-normalisation]
certificates: [r89_retained_cell_check.py, check_legacy_replay.py]
evidence:
  - "check_retained_history.py, retained_history.py, retained_history_audit.json: the legacy constructor, checker and receipt: 656 enlarged-window cases, nine threshold controls, 66 first-run plans, 60 exact-depth cells through 128, four inherited origins, 68 coupled decisions, nine signed-history cancellations, 35 rejections, three supplied outputs with 43/154/232 rows, the 22-row nonzero inherited lower relation; 37 local sources pinned. Fails at its new path: retained_history.py loads ../complementary_bridge/run_bridge.py and ../frontier_progress/ (now ../complementary-run-bridges/, ../signed-pair-frontier-normalisation/) by their pre-migration paths, and is loaded in turn by the legacy phi_exit_control/ code (now ../binary-return-exit-control/); and Its receipt pins the SHA-256 of this node's legacy note RETAINED_HISTORY.md, now an edited README, so it fails at its new path and in a legacy replay at earlier migrations (before rewritten notes were restored from git). Not reached at be73a66: the scripts/verify_all.py gate stopped earlier, at residual_progress/history_frontier (archive/legacy-checker-run-be73a66.md); it passed in full at 9dbc71a; A replay at this migration, before the note was edited, passed (exit 0, receipt unchanged). Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: r89_retained_cell_check.py
    scope: "Finite only (side-lane feed entry 2026-10-18 09:07, VERIFIED, main 9190ccf): 'This uses this branch's own `S` and `ν`. The planner (`J_s`, `A_s`, the dispatcher) is not rebuilt, so statements about which plans pass are not checked here.' Checked: the window on 4,000 random W9 pairs, the three-node family for j = 4..399 (j = 4 chain 16969 → 9545 → 5369 at Q = 12729), the retained cell and its depth progressions, and on the subcell m = 2736 + 4096l (46 values of l) the 25-arrow path S²⁵(Q) = X and S²⁷(Q) = Z. The status stays written"
aliases: [R89]
tags: [convergence, outer-residual, critical-nine, retained-history, original-rank, bounded-reduction]
---

# Retaining the strict lower history gives a sharp three-node critical-nine reduction on a larger window

## Statement

Odd-only clock, 1 absorbing, `T = νS`; the retained critical basis of [`common-critical-rank-basis`](../common-critical-rank-basis/README.md) (R75), `[s] = div J_s + A_s·P`; `d = v2(9C − 1)`, `h = ⌊(d − 4)/2⌋`, `z = 3^h(9C − 1)/2^d`.

1. **Larger window.** For odd `Q ≥ 11547` and `C ∈ W9` with `Q ≤ 3C` and `3C + 1 < 4Q`, let `U` be the actual upper prefix of length `h + 2` from `3C` to `F` (`F = 4(3z) + 1` for odd `d`, `6z + 1` for even `d`). Then `P(C) = div(U + J_F − J_C) + (A_F − A_C)·P`, every request of `A_C` is strict at `Q`, and at most one request has rank `≥ Q`, coefficient `+1`. A high W9 request is `z`, with `16z < 9C` and `4z < 3Q`, so the R87 window ([`failed-w9-leader-reduction`](../failed-w9-leader-reduction/README.md)) applies: at most three W9 nodes in all leave only lower premises and possibly one higher W5 input. This bounds W9 nodes, not ordinary clocks.
2. **Three nodes are needed for this procedure.** `C = 585 + 4096j`, `Q = 441 + 3072j`, `j ≥ 4`; at `j = 4` the chain is `16969 → 9545 → 5369` at `Q = 12729`. The strict boundary matters: `C = 15401`, `Q = 11551` has `S(C) = Q` and is rejected.
3. **The retained cell.** On the cell of [`four-target-history-classification`](../four-target-history-classification/README.md) (R88), `Q = 133704987 + 3·2^33·m`, `v = 128646821 + 64·3^18·m`, the full old R87-plus-R44 plan keeps exactly `+P(v)` above `Q`; the first H4 block at `3v` has second depth `d = 2 + v2(E)`, `E = 162818633 + 3^22·m`, every depth is realised, and odd `d ≥ 9` and even `d ≥ 16` pass outright.
4. **Negative-history repair.** On `m = 2736 + 4096l`, the usual composition has high vector `+P(a) − P(b)` (`β = (9E − 1)/64`, `a = 12β + 1`, `b = 4β + 1`); the retained lower history gives an exact strict plan for `P(b)`, and its substitution with coefficient `−1` cancels exactly to the upper-only plan `K + U + J_X − J_v`, leaving `+P(a)`. The fresh comparison is the actual 25-arrow path `Q → X`, then two arrows to `Z = (81β + 7)/4`. The inherited lower zero-source relations `D + E0 + Fv` stay explicit (they need not vanish).
5. **Continuation.** Both parities of the subcell end in a strict plan or one high W5 request, `+1`; `l = 4` and `l = 13` keep explicit failed leaves. A recurrent contraction fails: on the canonical-`Z` depth-2 branch the return has slope `3^12/2^19 > 1` relative to `6v + 1`, and the named maximal point inverse returns exactly to `Z`.

## Proof

The legacy note "A larger original-rank W9 window from retained lower histories" follows, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**Status: written conditional construction and complete bounded reduction.**
The main theorem enlarges the R87 window by using the already strict lower
history of the W9 source. At most three W9 substitutions leave at most one
higher W5 request, with coefficient +1. Three substitutions can be necessary.
This does not supply that final pair, or any smaller signed premise. It
changes no dispatcher. The later sections apply the theorem to a complete
retained history cell and preserve a concrete unresolved continuation.

Use absorbed odd Syracuse S, the elementary normal form nu and quotient
T=nu S. The killed atom [1] is zero. Write P(w)=[3w]-[w], with critical
indices W5={w>0:w=5 mod8} and W9={w>0:w=9 mod16}, rank rho(w)=nu(3w).
Native formal absorption is

    [s] = div J_s + A_s.P,

where every integer request, including a negative coefficient after
composition, remains a premise. Its individual ranks are at most nu(s).
Dependencies are the [retained critical basis](../common-critical-rank-basis/README.md),
[complete W9 local identity](../critical-nine-elimination/README.md),
[R87 bounded repair](../failed-w9-leader-reduction/README.md),
[R26 full run](../complementary-run-bridges/README.md),
[R44 returning interface](../returning-forward-interface/README.md),
and [R84 native decision](../later-target-twenty-step-descent/README.md).
The executable construction is [retained_history.py](retained_history.py).
No external theorem or novelty claim is imported.

### 1. Main theorem: the larger complete W9 window

Let Q>=11547 be odd and C in W9 satisfy

    Q <= 3C,                 3C+1 < 4Q.                  (1)

The second inequality is strict. Put

    d=v2(9C-1)>=4,
    h=(d-5)/2 if d is odd, or (d-4)/2 if d is even,
    z=3^h(9C-1)/2^d.

Let U be the actual ordinary prefix of length h+2 from 3C, and let F be
its endpoint. The complete local calculation gives

    F=4(3z)+1 if d is odd,     F=6z+1 if d is even.     (2)

Use only that upper prefix, and retain the original lower history:

    P(C) = div(U+J_F-J_C) + (A_F-A_C).P.                (3)

Every request in A_C is strictly below Q. At most one request in (3) has
rank at least Q, and its coefficient is +1. If that request is W9, its
index is exactly z and

    16z < 9C,                  4z < 3Q.                (4)

It therefore satisfies the old R87 window Q<=3z and32z<33Q. Apply R87
only to that high W9 request, retaining every other signed request. At
most two further W9 substitutions remove it. Thus (3), followed by those
substitutions, uses **at most three W9 nodes**. Its terminal high vector
is either zero or one W5 request with coefficient +1.

This is a complete finite reduction for all inputs (1), with the decision
made at the same original Q throughout. It is not a supply theorem for
the remaining W5 input. In particular, a positive self-request cannot be
dropped merely because other coefficients are negative.

#### Proof of the full rank bound

C=1 mod8, and its first ordinary step is (3C+1)/4<Q. Hence every formal
request in J_C,A_C is strict. This is precisely the history that the
usual local subtraction at a later lower endpoint can lose.

For odd d, z<9C/32 and3z<9Q/8. Native absorption of the actual endpoint
F=4(3z)+1 first supplies the sibling current to3z. If3z is noncanonical,
its elementary minimum is at most(3z-1)/2<Q. If it is1 mod8, its first
ordinary step is (9z+1)/4<27Q/32+1/4<Q. Otherwise it is critical0 mod3;
its first missing pair is P(z), and every subsequent request has rank
at most nu(z)<=z<Q. Thus this branch has at most that one high+1.

For even d,

    z <= (9C-1)/16 < (3Q-1)/4 < Q.                    (5)

The elementary complementarity between3z and6z+1 is exhaustive:

* If3z is noncanonical, F=6z+1 is critical1 mod3. Its first missing
  pair is P(4z+1), followed by H_(4z+1), whose minimum is nu(z)<Q.
* If3z is canonical and complementary, F is its selected partner.
  Native normalization reaches3z, whose sole possible high request is
  P(z), followed by H_z with all ranks<Q.
* If3z is canonical1 mod8, normalize F to3z and take one free arrow to
  f=(9z+1)/4. By(5),

      f < (27Q-5)/16 < 2Q.

  Any nontrivial elementary normalization of f is already below Q.
  An above-Q canonical raw state is1 mod3. It is either a critical W5
  endpoint, or a1-modulo8 state taking A(x)=(3x+1)/4. At most two such
  A arrows suffice, since

      A^2(f) < (243Q+67)/256 < Q.

  If a critical state n>=Q appears first, its pair index (2n+1)/3 is
  F((n-1)/6), so the following absorption minimum is at most(n-1)/6<Q.
  There is exactly one high W5 request with coefficient+1 in that case.

These cases also prove that a high W9 can arise only at z. Equations(4)
then prove the domain of the old repair. Its strict side requests cannot
cancel or create another high request; all signs are nevertheless kept.
This proves(3) and the claimed total node bound.

The bound concerns W9 substitutions, not an ordinary clock bound: h is
unbounded. The raw upper path has length h+2. Odd d normalized to3z has
common-tail clocks(h+3,1); even d to its raw endpoint has clocks(h+2,0).
The supplied absorption currents have their own rows and are not assigned
one artificial orbit clock.

#### Three nodes are necessary for this chosen interface

For every j>=4 set

    C=585+4096j, Q=441+3072j.

Both first nodes have d4, and their high W9 indices are

    z1=329+2304j, z2=185+1296j.

All three indices are9 mod16, and3z2-Q=114+816j>0. Thus two nodes still
leave a high W9 request. At j4 the chain is16969→9545→5369 withQ12729;
the third node has d6 and closes. This is sharpness for the stated
procedure, not minimality among every possible current construction.

The strict boundary in(1) matters. C15401,Q11551 satisfy C<4Q/3 but
S(C)=Q, and H_C contains a request of rank Q. The constructor rejects
that boundary rather than assuming the lower history is strict.

### 2. A complete retained cell and its first H4 block

The originating R84 index k=85 mod256 is the whole R44 a4 subtype after
the initial R87 d4/noncanonical-upper replacement. Write k=85+256j.
Its variables are

    Q=133704987+3*2^27*j,
    w=135529161+256*3^13*j,
    z0=76235153+16*3^15*j,
    u0=4z0+1,  r=(81z0+23)/8.

The exact ordinary word from Q to r has length18: append(1,1,3,1,2) to
R84's thirteen-arrow word. Its valuation sum is26, so the exact binary
cylinder includes modulus2^27. It has r-1<6(Q-1).

Within it, put j=64m for arbitrary m>=0. Then

    k=85+16384m,
    v=128646821+64*3^18*m,
    Q=133704987+3*2^33*m,
    r=6v+1,  nu(r)=3v,
    E=(81v+11)/64=162818633+3^22*m.                     (6)

Here v=37 mod64 and v<Q<3v. The full old R87-plus-R44 substitution
retains exactly +P(v) above the ORIGINAL Q. All other requests are<Q.
This statement concerns the complete signed plan, not merely its leading
endpoint. Its retained lower identities are displayed in section4.

At3v the complementary run has exact first exponent H4, and second depth

    d=2+v2(E)>=2.                                      (7)

Every depth has the complete nonnegative m progression

    m=(2^(d-2)-162818633)*(3^22)^(-1) mod2^(d-1),        (8)

including the extra exact-valuation bit. Write b=floor(d/2). The full run
has target

    f=2*(3/4)^b E             if d=2b+1,
    f=8*(3/4)^b E+1           if d=2b.                 (9)

These are integers on(8). Its quotient length is3+floor(d/2); ordinary
common-tail clocks are(4+floor(d/2),1) for odd d and(3+d/2,0) for even d.
Adding J_f-J_v gives an exact finite conditional P(v) plan at threshold Q.
The executable first_run keeps all of its high requests and performs the
larger W9 repair when applicable. It makes no claim that every d passes.

Every request in H_v is strict: v=F((v-1)/4), the latter is9 mod16 and
its first successor is(3v+1)/16<Q. Moreover

    32E < 39(Q-1).                                    (10)

Thus every odd d>=9 and even d>=16 has f<Q and passes outright. For d2,
E is odd and2 mod3 and satisfies3E+1<4Q. Native H_E is strict: either a
noncanonical normalization halves it, a1-modulo8 canonical state takes
(3E+1)/4, or a complementary2-modulo3 state uses inverse(2E-1)/3. These
are all below Q. The particular first d2 leader E belongs to W9 exactly when m=0 mod16;
then the larger-window theorem applies to the ENTIRE progression.

Do not replace this classification by an unconditional two-label list:
when3E is canonical1 mod8, H_(6E+1) takes a forward arrow before its first
critical request. For example m10 has a different high index117740030521.
The implementation retains the exact full formal coefficients.

### 3. The coupled high requests have a strict negative-history repair

A more explicit subcell is

    m=2736+4096l, l>=0,
    C=E, beta=(9C-1)/64, s=(beta-5)/64,
    a=12beta+1, b=4beta+1,
    X=18beta+1, Y=6beta+1, Z=(81beta+7)/4.              (11)

Here C=121 mod128, beta=5 mod64 and8 mod9, s=3 mod9. All quantities are
positive integers. The first d2 run from3v reaches f=6C+1 in four ordinary
arrows(1,1,1,2). Its selected normalization reaches3C.

The ordinary upper/lower W9 prefixes of length3 have endpoints X/Y and
words(1,2,2)/(2,1,2). Call those prefixes U,V. Let K be the first four
arrows followed by the exact selected current N_f from f to3C. The full
usual substitution is

    K+U-V+J_X-J_Y+J_C-J_v,
    A_X-A_Y+A_C-A_v.                                  (12)

Its high vector is exactly +P(a)-P(b). Both high ranks exceed Q. Neither
is reducible by the two R73 normalizer guards: a=61 mod128,b=21 mod128.
That statement excludes those two identities only.

The lower history H_C is already strict. Also H_b is strict since b=F(beta)
and beta<Q. Since Y is critical with index b,

    H_Y = -N_(3b)+P(b)+H_b.

Therefore the following is an exact STRICT original-Q plan for the
negative high pair itself:

    P(b) = div(J_C-V+N_(3b)-J_b) + (A_C-A_b).P.         (13)

Substitute(13) with its coefficient -1 in(12). Every row and signed input
cancels exactly to

    K+U+J_X-J_v,                A_X-A_v.               (14)

This is not deletion of a negative coefficient: all premises in(13) were
retained and proved strictly below Q. The sole high request in(14) is
+P(a); its other requests are from H_(3beta) and H_v and are strict.
The positive pair remains unsupplied.

More strongly, the negative three-arrow prefix in N_f is exactly U.
Consequently K+U is the actual seven-arrow prefix3v→X. The retained
original comparison Q→3v has ordinary clocks(23,5); its five negative
rows cancel against that seven-arrow path. The fresh original source
comparison is therefore the **actual25-arrow path Q→X**, and two more
arrows(1,2) reach Z. These are ordinary clocks, not quotient counts.

At l0, the exact high pair is

    Q=70506316836123, v=67839005952677,
    beta=12073885580933,
    a=144886626971197, rho(a)=217329940456795,
    b=48295542323733,  rho(b)=72443313485599.

### 4. The inherited lower relations do not disappear

Use superscript5 for the older fully expanded W5 absorption. In section2
let Y0=2z0+1, and define

    D=J_w-path(w→Y0)-J_Y0,       d=A_w-A_Y0,
    E0=J_z0-J_z0^5,              e=A_z0-A_z0^5,
    Fv=J_v^5-J_v,                f=A_v^5-A_v.

Each pair is a zero-source identity div(current)+coefficients.P=0; this
does NOT mean its rows vanish. The full old source after the repaired
negative pair equals the fresh25-arrow plan plus D+E0+Fv, with request
vector plus d+e+f. All these requests are<Q. In particular the old H_z0^5
bound is(27z0+29)/32<Q, and the old H_v^5 bound is(27v+89)/128<Q.
The constructor compares these expressions row for row and preserves the
nonzero combined relation in its evidence. A fresh direct comparison can
be chosen independently; it must not be described as silently deleting
unknown signed inputs from the inherited plan.

### 5. Complete finite continuation on the coupled cell

After the fresh27-arrow path reaches Z, parity of s in(11) is exhaustive.

If s is odd, Z is selected and its minimum is3c, where

    c=(27beta+1)/8 in W9,       23Q/40<c<7Q/12.

H_Z has exactly one high request,+P(c), with every helper strict. One
R87 local substitution suffices to remove any high W9. It fails exactly
when its local depth is4,6,or8 and its3z is noncanonical; in these cases
the remaining high input is W5. All other local cases pass. Indeed every
canonical3z is below27c/16<63Q/64. In a noncanonical even case,6z+1 is
above Q at depths4/6/8 and below Q at all even depths>=10. These strict
bounds follow from the displayed c interval and Q>=11547.

If s is even, Z is canonical with first exponent3 and complete second
parameter

    d'=2+v2(729(s/2)+29).

Take its ENTIRE R26 block. For even d' its raw endpoint g is1 mod3 and
satisfies g-1<6(Q-1). The fourteen-template R84 A/B/C procedure then
terminates in at most seven transitions at a strict or critical endpoint.
For odd d', g is0 mod3 with g<3Q/2. Nontrivial normalization is strict;
a critical endpoint is retained; otherwise g is1 mod8 and one ordinary
arrow reaches a raw1-modulo3 state below9Q/8, to which the same procedure
applies. All these prescribed currents and normalizers remain explicit.

At a high critical1-modulo3 endpoint n, the following pair's absorption
minimum is at most(n-1)/6<Q. At a high critical0-modulo3 endpoint, either
the odd-g bound gives its index<Q/2, or the even raw1-modulo3 state has
undergone nontrivial normalization, giving index<Q. Thus every high W9
satisfies R87 and is removed in at most two replacements. The final high
vector in this entire coupled cell is zero or one W5 request,+1.

This finite decision is not a terminating recursion for all its W5 exits.
For example l4 retains a high input540615167619701, and l13 retains
1407056910087877. The first is a canonical-Z continuation and the second
is a selected-Z failure. Their complete currents are checked.

A proposed contraction back to the starting raw cell is false. On the
canonical-Z d'2 branch,

    g=(2187beta+265)/64=(3^13*v+1161985)/2^18.

Relative to the original raw r=6v+1 its slope is3^12/2^19>1. The fact
that g<6Q therefore provides a bounded decision envelope, not a decreasing
recurrent parameter. Also v3(2g+1)=3 and the named maximal point inverse
returns8(2g+1)/27-1=Z exactly; that inverse undoes this full run. Alternative
histories, unbounded adaptive comparisons, and further signed identities
remain open.

### 6. Reproduction and evidence scope

Run

    python3 experiments/residual_progress/retained_history/check_retained_history.py

The default reads every stored supplied pair current and checks all rows;
it performs no absorption search. Receipt generation uses capped ordinary
absorption only for three designated finite demonstrations. It pins all
reachable local module files, this proof and the checker. All actual
outputs require every terminal signed input, including negative ones.
Missing, malformed, high-rank and cap-limited inputs are rejected. The receipt checks656 enlarged-window cases, nine threshold controls,66
first-run plans,60 exact-depth cells through128, four full inherited
origins,68 coupled decisions and nine signed-history cancellations. Three
fully supplied outputs have43,154 and232 rows. It records35 explicit
rejections and37 local source hashes. The nonzero inherited lower relation
has22 rows and two requests in each of three retained controls. Finite
ranges and output sizes are recorded in
[retained_history_audit.json](retained_history_audit.json). These checks
support the stated algebra; neither the finite checks nor the conditional
compiler establish universal current supply.

## Certificates

[`r89_retained_cell_check.py`](r89_retained_cell_check.py) (the side-lane probe; it imports nothing from the repository and passes in place, under 1 s): the window on 4,000 random W9 pairs, the three-node family, the retained cell and its depth progressions, and the 25- and 27-arrow paths on 46 subcell parameters, against `r89_retained_cell_check.json`. It does not rebuild the planner. The legacy checker `check_retained_history.py` pins the hash of this node's note, now an edited README (see `evidence`). The command in the legacy text names `experiments/residual_progress/retained_history/`.

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B18-replay-revival migration; standard library) replays the unmodified legacy check `check_retained_history.py` in a temporary copy of the legacy layout built by `tools/legacy_replay.py`, requiring exit 0 and every file unchanged (about 18 s). It checks finite steps only; the status is unchanged.

## Remarks

- The `l = 0` source of this subcell, `Q = 70506316836123`, `v = 67839005952677`, is the original coupled source of [`binary-return-exit-control`](../binary-return-exit-control/README.md) (R90) through [`prescribed-ternary-child-unbounded-clocks`](../prescribed-ternary-child-unbounded-clocks/README.md) (R94).
- The R73 normaliser guards of [`signed-pair-frontier-normalisation`](../signed-pair-frontier-normalisation/README.md) do not reduce `a` or `b` (`a ≡ 61`, `b ≡ 21 mod 128`); that excludes those two identities only.
- The main lane's REPORT records a separate independent mathematical audit of the widened window and a final package review, both by the main lane's own agents.
- No novelty is claimed.

## History

- Migrated from `experiments/residual_progress/retained_history/RETAINED_HISTORY.md` (legacy ID R89) at commit `be73a66`, by the B13 migration (Claude, Opus 5.5). Note, scripts and receipts moved byte-identical; the note became this README, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Legacy status: "written conditional construction; complete bounded reduction with explicit terminal premises".
- Main lane (ChatGPT, Codex), 2026-10-18, first committed in `7a477ad`. The batch's "independent" proof, source and default-replay reviews recorded in archive/convergence-residual-progress/REPORT.md were the main lane's own agents, not a different lane.
