---
id: fourteen-step-window-original-source
kind: result
title: "Fourteen more inverse-history steps admit only the original source at the repeated target"
status: written
claim: >
  Computer-assisted. Odd-only 3x+1 map S, absorbing at 1, canonical quotient T = nu S. On the original coupled
  cell of R90 (v0 = 67839005952677 + 2^18 3^18 ell, Q = 70506316836123 + 3 2^45 ell), for every source with at
  least r guarded Phi returns and n_r = 3 Phi^r(v0): among positive canonical p <= Q and depths 0 <= d <= 12r+19,
  T^d(p) = n_r holds exactly for p = Q at d = 12r+18, uniformly in ell and r, with all ray indices and
  intermediate heights allowed. Proof: written affine bounds (prefix score below 102 at h = 12r+5, whole-word
  score below 1/2) and the exact selective congruence 243u = 899841 2^m mod 7153, m = 8..14, reduce the boundary
  origins to 33,995 canonical candidates, all classified by an exact signed Python classifier with no cap (exactly
  16 relevant first-hit tails); an independent C++ classification of all 176,754,119 canonical origins with 7153 <
  u < 741545113 finds the same 16 tails; the boundary states are r-independent affine functions of ell, and a
  complete enumeration of suffixes of length <= 14 and cost <= 21 leaves only (9Q+5)/8 (always above Q) and Q
  itself. Extends R91 by fourteen steps; supplies no current and is not an all-depth exclusion; longer histories,
  later targets and signed comparisons stay open.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [rational-basin-precision-barrier, binary-return-exit-control, elementary-bridge-quotient-normal-form]
certificates: [check_legacy_replay.py]
evidence:
  - "check_deeper_window.py, deeper_window.py, sparse_basin.py, deeper_window_audit.json, full_basin_audit.json, independent_basin.cpp: the legacy selective classifier, suffix enumeration, checker, receipts and the independent C++ full-interval classifier (compiled only with --cpp): the 33,995-origin selective basin, 224 first-hit arrows, 21 positive guarded families through r = 128, 303 boundary lifts, 42 terminal histories, 24 affine interval cases, 24 rejections, three cap-abort checks. Fails at its new path: it loads ../phi_exit_control/ and ../shadow_precision/ (now ../binary-return-exit-control/, ../rational-basin-precision-barrier/) by their pre-migration folder names, and its receipt pins the hashes of this node's legacy note DEEPER_WINDOW.md and of SHADOW_PRECISION.md and PHI_EXIT_CONTROL.md, now edited READMEs. It also fails in a replay with the notes unedited: its receipt pins a hash of ../binary-return-exit-control/phi_exit_control_audit.json that predates the regeneration of that receipt at the be73a66 rename (as for history_frontier in archive/legacy-checker-run-be73a66.md). Not reached at be73a66: the scripts/verify_all.py gate stopped earlier, at residual_progress/history_frontier (archive/legacy-checker-run-be73a66.md); it passed in full at 9dbc71a. Fails under replay (B18-replay-revival): the stale pin of phi_exit_control_audit.json above, which predates the migration"
  - "CANDIDATE.md: the historical unpromoted draft (2026-10-18, commit b2731dd) of the finite-boundary reduction, resolved by this result; kept as evidence, with its three links repointed to nodes"
  - "r92_inverse_tree_check.py, r92_inverse_tree_check.json: side-lane probe (Claude side lane, 2026-10-18 07:02): independent inverse-tree search at two concrete sources and a brute-force check of the R25 inverse table (cited from elementary-bridge-quotient-normal-form). Fails at its new path: it imports affine_controls from experiments/packet_currents/negative_controls/ by repository-relative path (now ../locally-collatz-like-control-barrier/). Passed at be73a66 as reviews/side_lane/r92_inverse_tree_check.py (archive/legacy-checker-run-be73a66.md, exit 0); its receipt is reproduced byte for byte by check_legacy_replay.py"
  - "../rational-basin-precision-barrier/c0_basin_classify.c: the side lane's C classification of the larger universe 7153 < u < 741545113, whose 16 tails with m in 8..14 agree with the ones used here (see reviewed_by)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: r92_inverse_tree_check.py
    scope: "Finite only (side-lane feed entry 2026-10-18 07:02, VERIFIED, main 61fd041), with the lane's own step and ν: '**`ℓ = 0`, `r = 0`** (`Q = 70506316836123`, depth at most 19). The only canonical `p ≤ Q` reaching `n₀` is `p = Q`, at depth 18. The search tree has 63 nodes.' '**The least `ℓ` with `r = 1`** (`ℓ = 398166`, `Q ≈ 4.2·10¹⁹`, depth at most 31). The only such `p` is `p = Q`, at depth 30.' Two concrete sources only; the uniform statement rests on the written reduction. The status stays written"
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: ../rational-basin-precision-barrier/c0_basin_classify.c
    scope: "Finite only (side-lane feed entries 2026-10-18 06:34 and 07:02): the independent C classification of the candidate universe 7153 < u < 741545113: 'All 176,754,119 eligible origins are classified, with none left unknown' and '1,939 lie in the c₀ basin'; 'R92's sixteen boundary tails (the same `u`, `d₀`, `E₀` and `m` in each case), its full-interval counts (176,754,119 origins and 1,939 hits) and its largest numerator (`23,508,760,799,607,151`) coincide with this branch's independent classification'. 'The suffix step, with its affine inequalities `p ≤ Q` and the source guards, has **not** been run here.' The status stays written"
aliases: [R92]
tags: [convergence, outer-residual, computer-assisted, rational-shadow, inverse-barrier, ternary-precision]
---

# Fourteen more inverse-history steps admit only the original source at the repeated target

## Statement

**Computer-assisted.** Odd-only clock, 1 absorbing; canonical quotient `T = νS`, its complete inverse table ([`elementary-bridge-quotient-normal-form`](../elementary-bridge-quotient-normal-form/README.md), R25) and the signed rational quotient of [`rational-basin-precision-barrier`](../rational-basin-precision-barrier/README.md) (R91). Put `A = 3^12`, `M = 2^19`, `D = 7153`, `B = 299947`, `Φ(v) = (Av + B)/M`, `L(v) = Dv + B`, `c0 = −899841/7153`.

**Theorem.** For every `ℓ ≥ 0`, with `v0 = 67839005952677 + 2^18·3^18·ℓ`, `Q = 70506316836123 + 3·2^45·ℓ`, and every `r ≥ 0` with `v2(L(v0)) ≥ 19r + 18`, put `n_r = 3Φ^r(v0)`. For every positive canonical `p ≤ Q` and every `0 ≤ d ≤ 12r + 19`: `T^d(p) = n_r` iff `p = Q` and `d = 12r + 18`. All inverse ray indices and intermediate heights are allowed.

The proof extends R91 (which covers `d ≤ 12r + 5`) through fourteen more steps:

1. written affine bounds keep the intercepts and force the boundary score `μ_h < 102` and the whole-word score `< 1/2`;
2. the exact selective congruence `243u ≡ 899841·2^m (mod 7153)`, `m = 8..14`, with `7153 < u < 7153 + (2^m/243)(892688 + 12·3^12)`, leaves 67,992 odd and 33,995 canonical candidates;
3. an exact signed Python classifier resolves all of them with no cap: exactly 16 relevant first-hit tails. An independent C++ classification of all 176,754,119 canonical origins with `7153 < u < 741545113` (1,939 hits) recovers the same 16;
4. the boundary states are affine in `ℓ` with coefficient `2^(m+18)·3^14`, independent of `r` once `r ≥ k0`, which fixes every branch decision for the next fourteen steps;
5. a complete enumeration of suffixes of length at most 14 and exponent cost at most 21 (7,036 states) leaves exactly two endpoints with score below `1/2`: `(9Q + 5)/8`, always above `Q`, and `Q` itself, the known self-history.

It supplies no current and is not an all-depth exclusion at a fixed source.

## Proof

The legacy note "Only the original source survives fourteen more inverse-history steps" follows, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**R92 — written reduction with a complete finite rational-basin certificate.**
This result extends [R91](../rational-basin-precision-barrier/README.md) on the
same positive coupled family. It includes every quotient inverse word and
every inverse ray through the stated window, uniformly over the growing
return count. The only source no larger than the original Q is Q itself,
at its already known clock. No smaller history or new current is supplied.
Longer histories, later targets, and other signed comparisons remain open.
No novelty, human peer review, or formal verification is asserted.

The historical [candidate](CANDIDATE.md) is superseded by this proof and the
complete selective classification below. The proof uses the canonical
quotient T and normal form nu of
[R25](../elementary-bridge-quotient-normal-form/README.md), with the positive return
family and clocks of [R90](../binary-return-exit-control/README.md).

### 1. Statement at the original source

Set

    A=3^12=531441, M=2^19=524288, D=A-M=7153,
    B=299947, gamma=A/M,
    Phi(v)=(Av+B)/M, L(v)=Dv+B,
    c0=-3B/D=-899841/7153, t0=899841-D=892688.

For every ell>=0 define

    v0=67839005952677+2^18*3^18*ell,
    Q =70506316836123+3*2^45*ell,
    n0=3v0.

Let r>=0 satisfy v2(L(v0))>=19r+18, so at least r guarded Phi returns
are available. Put v_r=Phi^r(v0), n_r=3v_r, and h=12r+5.

**Theorem.** For every positive canonical integer p<=Q and every integer
0<=d<=12r+19,

    T^d(p)=n_r    if and only if    p=Q and d=12r+18.     (1)

The result includes all intermediate heights and all inverse ray indices.
Both r and ell are quantified; the same Q is retained throughout a chosen
history. Different members may have different available return counts.

R90 supplies the existence in (1), with the separate ordinary comparison

    T^(18+12r)(Q)=n_r,
    S^(23+12r)(Q)=S^5(n_r).                              (2)

The ordinary prefix of length18+12r ends at6v_r+1, not at n_r. In
particular, (1) is not an assertion about an ordinary merger with equal
clocks.

R91 already excludes p<=Q at d<=h. It remains to classify

    h<d<=h+14.                                           (3)

### 2. Actual-rank bounds before finite enumeration

The complete inverse table from R25, also valid at the signed rational
centre c0, has bases (a*x+b)/3:

|x modulo3|Point|First ray|Second ray|
|---|---|---|---|
|0|none|(8x+3)/3|(16x+3)/3|
|1|none|(4x-1)/3|(32x+19)/3|
|2|(2x-1)/3|(64x+19)/3|(128x+83)/3|

Each ray continues by p->64p+49. Every inverse branch x->alpha*x+beta
satisfies

    alpha>=2/3, beta>=-1/3, alpha-beta>=1.

Consequently a word of length j and slope lambda_j satisfies the full
affine estimate

    x_j>=lambda_j*[n_r+1-(3/2)^j].                       (4)

Write

    kappa=2^27/3^18, c=213949807/3^17>1,
    Q=kappa*n0-c, n0>2Q, Q+1<kappa*n0.                  (5)

These identities and inequalities hold coefficientwise on the original
positive cell. Its exact orders give

    n_r-c0=gamma^r(n0-c0), v3(n_r-c0)=h,
    L(v0)>=81*2^(19r+18),
    n0>=(243*2^(19r+18)-3B)/D>=C*2^(7r),
    C=(243*2^18-3B)/D=62801151/7153.                     (6)

Suppose (3) has a source p<=Q. At the boundary after h inverse steps put

    mu_h=lambda_h*gamma^r,
    E_r=(243/32)*2^(7r), K=(3/2)^14.

The remaining at most fourteen arrows give x_h+1<=K(Q+1), while (4)-(6)
give x_h>=mu_h*(n0+1-E_r). This bracket is positive, and therefore

    mu_h<K*(Q+1)/(n0+1-E_r)
        <(8192/81)*n0/(n0+1-E_r)<102.                    (7)

The equality K*kappa=8192/81 is exact. A sufficient exact check for the
last strict inequality, valid uniformly in r and ell, is

    (70/81)*C-102*(243/32)
       =21052290557/3090096>0.

The slope of the whole word has a stronger necessary bound. With
mu_total=lambda_d*gamma^r, (4) yields

    p>=mu_total*[n0+1-(3/2)^19*2^(7r)].

The bracket exceeds2Q, because

    (1-2*kappa)*C-(3/2)^19
      =232269104057100257855/484305580032786432>0.

Thus every actual p<=Q in this window must satisfy

    mu_total<1/2.                                       (8)

These bounds retain the affine intercept. Neither one is an inference from
an asymptotic slope or a finite sample of source sizes.

### 3. Finite boundary universe and exact selective congruence

The first h inverse steps share a legal shadow word from c0: before each
branch decision their actual-shadow difference is divisible by3. All
shadow states are canonical rationals -u_j/D<-1 with reduced denominator D.

R91 proves for every shadow prefix

    lambda_j*gamma^k(j)>=1,
    k(j)=max(0,ceil((j-5)/12)).

Put t_j=u_j-D. For an inverse edge,

    t_j=alpha_j*t_(j-1)+D*delta_j,
    delta_j=alpha_j-beta_j-1, 0<=delta_j<alpha_j.

Expanding this recurrence and using the R91 prefix bound gives

    t_h<mu_h*[t0+12D*gamma/(gamma-1)]
       =mu_h*(t0+12A).                                  (9)

The geometric sum counts at most twelve depths at each k; k=0 actually
occurs at only six depths. Equations (7) and (9) initially imply

    D<u<D+102*(t0+12A)=741545113.                         (10)

This is an origin bound only. Intermediate forward states may exceed it.

Let d0,E0 be the shadow origin's first forward hitting time of c0 and its
binary exponent sum. The signed deterministic c0 cycle has exact length12
and cost19. Since the boundary word has length h=12r+5, necessarily

    d0=12k0+5, E0=19k0+m, k0>=0,
    r>=k0, mu_h=2^m/243.

R91 and (7) force the seven possibilities m=8,...,14. They sharpen (10)
to the individual strict bounds

    D<u<D+(2^m/243)*(t0+12A).                            (11)

Every length-d inverse word has affine form (2^E*x+C)/3^d with integer C,
including all ray indices. At x=-899841/D this gives

    u=899841*2^E*3^(-d) modulo D.

Since2^19=3^12 modulo D, the first-hit phase forces

    u=899841*2^m*243^(-1) modulo D.                      (12)

Together with oddness, (11)-(12) give seven finite arithmetic progressions
of period2D. Primitivity is automatic, since899841,2,3 are coprime to D.
Their exact counts are:

|m|First odd u>D|Odd candidates|Canonical candidates|
|---:|---:|---:|---:|
|8|8465|536|267|
|9|9777|1071|536|
|10|12401|2142|1070|
|11|17649|4283|2142|
|12|13839|8566|4283|
|13|20525|17131|8566|
|14|19591|34263|17131|
|Total||67,992|33,995|

No assumption about the larger basin was used to select these candidates.

### 4. Complete rational-basin certificate

The signed quotient is the exact deterministic map in R91. A nonhit is
certified by its path to an already classified state, a detected other
cycle, or the invariant interval x>-1. It is never inferred from a failed
bounded search. The portable selective classifier treats every cap as an
error and records every candidate row in a fixed digest.

All33,995 canonical candidates are completely classified. The calculation
uses275,892 memoized states, with largest visited numerator
3,723,514,929,151 and longest newly explored path120. No cap is reached.
Exactly the following sixteen candidates hit c0; all have the required
first-hit depth and cost phase:

|u|d0|E0|m|Suffix states enumerated|
|---:|---:|---:|---:|---:|
|952661|5|8|8|396|
|3789185|5|10|10|363|
|7499687|17|30|11|514|
|15120975|5|12|12|472|
|29977289|17|32|13|513|
|30206185|5|13|13|355|
|30363551|5|13|13|522|
|57915973|53|90|14|442|
|59646999|29|52|14|461|
|59775753|17|33|14|463|
|59933119|17|33|14|429|
|60290769|17|33|14|438|
|60433829|17|33|14|379|
|60505359|5|14|14|463|
|60562583|5|14|14|370|
|60619807|5|14|14|456|
|Total||||7,036|

The certificate stores all sixteen first-hit paths and costs. The complete
row digest is
`b0f8ec3a422ede361d49cb06d79c74be7d01d05d18c58d61da972ee0f09f2d3e`.
The digest identifies the calculation; it does not replace replay of it.
An independent C++ implementation checks the same candidate classifications.
The proof needs no termination assertion for the signed quotient outside
this fully checked finite set.

The independent C++ calculation also classifies the entire larger interval
(10): all176,754,119 canonical primitive origins, with1,939 target hits,
largest visited numerator23,508,760,799,607,151, and no cap reached. Filtering
that complete table by (11)-(12) and the first-hit phase recovers the same
sixteen rows. Every selective candidate outcome is compared, including
nonhits. This broader calculation is an independent crosscheck; the smaller
complete33,995-origin certificate already suffices for the proof.

### 5. Compression to r-independent affine boundaries

The forward path of each shadow origin is deterministic. An inverse word
of length h consists of r-k0 complete inverse c0 cycles, followed by that
origin's one fixed first-hit tail. On the positive source this yields

    x(ell)=(2^m/243)*(n0(ell)-c0)-u/D
           =(2^m*L(v0)/81-u)/D
           =x(0)+2^(m+18)*3^14*ell.                     (13)

It is independent of r once r>=k0. Its intercept is integral: v3(L(v0))=4
makes L(v0)/81 integral, and (12) makes the displayed numerator divisible
by D. Legality and canonicality on each admitted source follow from the
actual inverse formulas and the shadow precision through h.

The period in (13) is divisible by3^14. Therefore every chosen inverse
suffix through fourteen arrows has the same ternary decisions at every
ell. The source's binary guard remains explicit. For r returns it is

    ell = -[(D*V0+B)/2^18]*(D*3^18)^(-1) modulo2^(19r),
    V0=67839005952677.                                   (14)

These source sets are nested as r increases. A suffix eligible at any
r>=k0 must therefore be eligible on the k0 guard; this does not authorize
discarding the stronger guard when constructing an actual history.

### 6. Complete finite suffix enumeration and the two outputs

Let a remaining suffix have length t<=14 and binary exponent sum E_s.
Its inverse slope is2^E_s/3^t. The boundary score is at least1, so (8)
forces

    2^E_s/3^t<1/2, and hence E_s<=21.                    (15)

Every quotient inverse arrow has positive integral cost. A ray at index L
has cost e_base+6L with e_base>=2, so all possible suffixes are covered by
enumerating length<=14 and cost<=21. The exponent cost is not an ordinary
Syracuse clock.

The default algorithm enumerates every such legal word at all sixteen
boundaries, without optimistic completion pruning. It generates rays by
the exact recurrence p->64p+49, preserves the full integer affine source
formula, and tests positivity and p<=Q at every generated state. Thus
finite small-parameter exceptions to a slope comparison would be retained.
The affine interval is intersected with (14). A separate implementation
using the closed ray formula and a proved optimistic slope bound returns
the identical terminal list.

Among all7,036 enumerated states, exactly two nonempty suffixes satisfy
the necessary whole-score bound (8). Both come from u=952661,d0=5,E0=8:

|Suffix length t|Cost E_s|Full origin p(ell)|Whole score|
|---:|---:|---|---|
|11|16|(9Q+5)/8|2^24/3^16|
|13|19|Q|2^27/3^18|

The first is strictly greater than Q for every positive Q. The second is
the known self-return and has no strict comparison interval. Explicitly,
their affine formulas are

    79319606440639+118747255799808*ell,
    70506316836123+105553116266496*ell.

For a compact independent check, define the inverse maps

    a(x)=(8x+3)/3, b(x)=(4x-1)/3, p(x)=(2x-1)/3.

The first suffix applies, in order,

    a,b,p,p,b,b,p,p,p,p,p.

The second appends b,p. The boundary is (13) with u=952661,m=8.
The receipt retains every branch name, index, cost, and affine numerator.

The self-return has d=h+13=12r+18. The fifteen other first-hit tails have
no suffix satisfying (8). R91 covers d<=h, and (8)-(15) exhaust every
possible p<=Q in the remaining window. This proves (1).

### 7. Reproduction and limits

Run

    python3 experiments/residual_progress/deeper_window/check_deeper_window.py

To compile and independently replay the entire C++ interval as well, run

    python3 experiments/residual_progress/deeper_window/check_deeper_window.py --cpp

The checker replays the complete selective basin, all first-hit paths,
the two suffix enumerations, full affine comparisons and source guards,
exact rational constants, positive histories, and rejection controls.
Source hashes and complete audit data are stored in `deeper_window_audit.json`.
The independent C++ replay is included when the checker is invoked with
its C++ option by the unified gate.

This certificate proves a uniform all-word statement over infinitely many
positive source parameters, because the mathematical reduction covers every
such parameter before enumeration. It is stronger than a scan of finitely
many positive seeds. Its window is nevertheless finite relative to r:
histories after12r+19, later common targets, and other signed-current
comparisons are not covered.

The original Q is retained as equality, not counted as a smaller supplied
premise. The result adds no accepted current rule and does not show that a
fixed positive source lacks a history at all depths. Collatz and universal
terminal current supply remain open here.

## Certificates

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B13 migration; standard library). The legacy scripts load sibling modules by their pre-migration paths, so they no longer run here. This certificate calls `tools/legacy_replay.py`, which rebuilds the pre-migration layout in a temporary directory from `tools/legacy_paths.json`, runs the unmodified legacy scripts there without `-O` (as `scripts/verify_all.py` did at `be73a66`), and requires exit 0 and every copied file unchanged. It writes nothing in the repository. It replays: the side-lane probe `r92_inverse_tree_check.py` (under 1 s, receipt reproduced byte for byte): complete inverse trees from `n_r` at the two concrete sources `ℓ = 0, r = 0` and the least `ℓ` with `r = 1`, and the brute-force check of the R25 inverse table. The legacy checker `check_deeper_window.py` cannot be replayed (see `evidence`); the computer-assisted classification itself is not re-run by any certificate of this node, and the C++ and C classifiers need a compiler. The commands in the legacy text name `experiments/residual_progress/deeper_window/`.

## Remarks

- The original `Q` is retained as equality, not counted as a smaller supplied premise.
- The [historical candidate](CANDIDATE.md) proposed this reduction before the classification existed; this result supersedes it.
- The research template written alongside this result is the question [`common-tail-comparison-after-r92`](../../questions/common-tail-comparison-after-r92.md); the R92 decision was to pivot to later meeting targets or different signed histories.
- The main lane's REPORT records independent proof and source reviews and a separate reproduction of the C++ receipt and the unpruned suffix enumeration, all by the main lane's own agents.
- No novelty, human peer review or formal verification is claimed.

## History

- Migrated from `experiments/residual_progress/deeper_window/DEEPER_WINDOW.md` (legacy ID R92) at commit `be73a66`, by the B13 migration (Claude, Opus 5.5). Note, scripts and receipts moved byte-identical; the note became this README, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Legacy status: "computer-assisted finite-window theorem, uniform in the source and return count (the note: written reduction with a complete finite rational-basin certificate)".
- The historical draft `CANDIDATE.md` (added at `b2731dd`) stays in this folder as evidence. The research template `NEXT_TARGET.md` of the same folder became the question [`common-tail-comparison-after-r92`](../../questions/common-tail-comparison-after-r92.md). The side-lane probe `reviews/side_lane/r92_inverse_tree_check.*` moved here.
- Main lane (ChatGPT, Codex), 2026-10-18, first committed in `61fd041`. The batch's "independent" proof, source and default-replay reviews recorded in archive/convergence-residual-progress/REPORT.md were the main lane's own agents, not a different lane.
