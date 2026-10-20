---
id: maximal-inverse-cycle-continuation
kind: result
title: "Maximal inverse-cycle continuation on a failed selected row, with a complete descent table"
status: written
claim: >
  Odd-only 3x+1 map S, absorbing at 1; original rank rho(w) = nu(3w), no sigma rule. On selected w = 3445 mod
  3456 put v = (16w-13)/27, assume 3 | v, and set b = 8v+1, q = rho(w), k = floor(v3(b+17)/7), p = (2048/2187)^k
  (b+17) - 17, j = v3(p+1), eta = 2^j (p+1)/3^j - 1. For k >= 1 the exact ordinary inverse comparison eta -> q
  has word 1^j, (1,1,1,2,1,1,4)^k, 2,1,1,4 and length j+7k+4 (maximal repetitions of that cycle word and maximal
  valuation-1 continuation, not maximality among all inverse choices). The full signed plan descends exactly for
  k = 1..5 with j >= 3, k = 6..11 with j >= 2, k = 12..17 with j >= 1, and every k >= 18 (intercepts included);
  failed k >= 1 rows retain a unique higher request of rank eta, and k = 0 retains the R56 original
  self-request. Complete CRT families realise every permitted remainder; a fixed 14-arrow comparison at k = 1, j
  = 3 has whole old-twelve-excluded families through every prescribed guarded forward depth L (some overlap R59,
  so this is not an exclusion from the enlarged dispatcher). Supplied currents remain necessary for the
  surviving smaller inputs; universal coverage is open.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [two-selected-inverse-choices, critical-image-rank-composition, guarded-cycle-exit-phases, twelve-family-rho-dispatcher]
certificates: [check_legacy_replay.py]
evidence:
  - "check_cycle_inverse.py, cycle_inverse.py, cycle_inverse_audit.json: the legacy constructor and checker: 512 affine checks, seven exact threshold boundaries, 99 complete plans (57 descending, 30 higher-leading failures, 12 original self-requests), nine full old-twelve-exclusion families through L = 64, four long words, three actual substitutions with full first-two tables and eight rejections. Fails at its new path: cycle_inverse.py loads ../selected_inverse/selected_inverse.py and the checker ../selected_cycle_exit/ and ../selected_rules/ by their pre-migration folder names. Passed at be73a66 as experiments/residual_progress/cycle_inverse/check_cycle_inverse.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran every residual-progress step before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a); replayed unchanged, with its receipt, by check_legacy_replay.py"
  - "r60_cycle_inverse_check.py, r60_cycle_inverse_check.json: side-lane probe (Claude side lane, 2026-10-18) of the maximal cycle inverse and its acceptance table. Fails at its new path: it imports affine_controls from experiments/packet_currents/negative_controls/ by repository-relative path (now ../locally-collatz-like-control-barrier/) and fibre_count_check from its own folder (now ../absorbed-fibre-uniform-counts/). Passed at be73a66 as reviews/side_lane/r60_cycle_inverse_check.py (archive/legacy-checker-run-be73a66.md, exit 0); its receipt is reproduced byte for byte by check_legacy_replay.py"
  - "side_lane_review_64a5981.md, side_lane_review_64a5981.json: the main lane's pinned review (2026-10-18) of side-lane commit 64a5981: byte-identical replays of three side-lane probes, r60_cycle_inverse_check (this node), r86_even_exit_check (legacy R86) and batch_r81_r83_check (legacy R81/R83, with its coverage correction), each within its stated finite scope and listed limits. A review of side-lane probes, not of this node; the R81, R83 and R86 nodes cite it here"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: r60_cycle_inverse_check.py
    scope: "Finite only (side-lane feed entry 2026-10-18 04:59, VERIFIED), with the lane's own step and nu: 400 inputs built by CRT with prescribed k = 1..20 (h = 7k) and j = 0..4, four per cell: the ordinary word from eta to q = (81v+23)/32 is exactly 1^j, (1,1,1,2,1,1,4)^k, 2,1,1,4; the height formula eta = lambda q + beta holds exactly; eta < q holds in exactly the cells of the table, including the boundary cells at k = 5/6, 11/12, 17/18. Per the main lane's replay (side_lane_review_64a5981.md), not checked: k = 0, nonzero h - 7k remainders, j >= 5 or k >= 21, complete signed plans and current supply. The status stays written"
aliases: [R60]
tags: [convergence, outer-residual, tripling-pairs, critical-rank, selected-phase, inverse-rays, negative-cycle-shadow]
---

# Maximal inverse-cycle continuation on a failed selected row, with a complete descent table

## Statement

Odd-only clock, 1 absorbing; `ν`; `P(w) = [3w] − [w]`; the original rank `ρ(w) = ν(3w)`; `H_s` keeps its signed `W5` requests. No `σ` rule is used. Domain: `w ≡ 3445 (mod 3456)` (the entry phase of [`growing-prefix-unhandled-leading-input`](../growing-prefix-unhandled-leading-input/README.md)), `v = (16w − 13)/27 ≡ 0 (mod 3)`, a row left by both choices of [`two-selected-inverse-choices`](../two-selected-inverse-choices/README.md).

1. **Procedure.** Set `b = 8v + 1`, `q = ρ(w)`, `k = ⌊v3(b + 17)/7⌋`, `p = (2048/2187)^k·(b + 17) − 17`, `j = v3(p + 1)`, `η = 2^j(p + 1)/3^j − 1`. For `k ≥ 1` the exact ordinary inverse comparison `η → q` has word `1^j, (1,1,1,2,1,1,4)^k, 2,1,1,4` and length `j + 7k + 4`: maximal repetitions of the specified cycle word and maximal valuation-1 continuation, not maximality among all inverse choices.
2. **Exact table.** The full signed plan descends exactly for `k = 1–5` with `j ≥ 3`, `k = 6–11` with `j ≥ 2`, `k = 12–17` with `j ≥ 1`, and every `k ≥ 18`, intercepts included. Failed `k ≥ 1` rows retain a unique higher request of rank `η`; `k = 0` retains the R56 original self-request.
3. **Families.** Complete CRT families realise every permitted remainder. A fixed 14-arrow comparison at `k = 1`, `j = 3` has whole old-twelve-excluded families ([`twelve-family-rho-dispatcher`](../twelve-family-rho-dispatcher/README.md)) through every prescribed guarded forward depth `L` of [`guarded-cycle-exit-phases`](../guarded-cycle-exit-phases/README.md). Some overlap R59, so this is not an exclusion from the enlarged dispatcher; 11432437 is an actual R60 priority winner there.

Supplied currents remain necessary for the surviving smaller inputs; universal coverage and current supply are open.

## Proof

The legacy note "A maximal cycle inverse and its complete point continuation" follows, lightly edited (headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**Status: written conditional theorem and exact constructor.** This classifies
one specified inverse procedure on an entire previously failed R56 row. It
retains every failed signed plan. A fixed fourteen-arrow instance intersects
every prescribed growing-prefix length and misses all twelve previous direct
rules. Universal coverage, universal current supply, and novelty remain open.

Use the absorbed odd Syracuse map `S`, elementary minimum `nu`,
`P(w)=[3w]-[w]`, and the original rank `rho(w)=nu(3w)`. The formal absorption
plan `H_s` retains its signed W5 requests. No sigma rule is used.

Dependencies are the [R56 inverse interface](../two-selected-inverse-choices/README.md),
the [R43 rank/current compiler](../critical-image-rank-composition/README.md), and
the [R57 exit interface](../guarded-cycle-exit-phases/README.md).
The old-twelve exclusions refer to the fixed
[selected dispatcher](../twelve-family-rho-dispatcher/README.md) at commit7206f9c;
they do not silently extend to a later enlarged dispatcher.

### 1. Whole domain and prescribed inverse procedure

Assume w is positive and

    w=3445 mod3456,  v=(16w-13)/27=0 mod3.

Then `v=-7 mod2048`, `v>=2041`, and

    q=rho(w)=(3w-1)/2=(81v+23)/32,   b=8v+1.

Both R56 choices have point-depth zero. Its exact four-arrow tail is

    b --(2,1,1,4)--> q.                              (1)

Put `h=v3(b+17)`, `k=floor(h/7)`, and `a=2048/2187`. If `k=0`, retain
the original R56 k4 zero-depth plan. If `k>=1`, define

    p=a^k(b+17)-17,
    j=v3(p+1),
    eta=2^j(p+1)/3^j-1.                              (2)

The complete ordinary path from eta to q has valuation word

    1^j, (1,1,1,2,1,1,4)^k, 2,1,1,4,               (3)

of length `j+7k+4`. This is an ordinary path, with common-tail clocks
`(j+7k+4,0)` from `(eta,q)`. The elementary pair normalizers below retain
their own currents; they are not zero ordinary elapsed time. No assertion
identifying all ordinary and quotient intermediate states is needed.

**Proof of existence, exactness, and maximality.** The seven-arrow word
has affine map `Psi(x)+17=(2187/2048)(x+17)`. If an odd positive target
x satisfies `3^7|(x+17)`, its inverse is
`y=2048(x+17)/2187-17`. Since `(x+17)/2187` is positive even, y is positive
and `y=-17 mod4096`, including the exact extra valuation bit. Substitution
checks all seven arrows. Its ternary order drops by exactly7. Thus precisely
k consecutive inverse copies of this same word are legal; the next is not.
This is maximality for this word, not for every possible inverse itinerary.

Here `v2(b+17)=1`. Hence `v2(p+17)=11k+1` and `v2(p+1)=4`.
The latter has unit `-1 mod4`, so p is complementary canonical. Each point
inverse is `(2x-1)/3`, legal exactly when x is2 mod3; all j such steps
give eta. Its binary exponent is exactly `4+j`, and its odd unit modulo4
is `-3^(4+j)`. Thus eta is again complementary canonical. Maximality of j
gives `eta!=2 mod3`. Positivity also follows from the integral expression
`eta+1`, divisible by `2^(4+j)`; eta>=15. This proves (3). When the
remainder `h-7k` is positive, j is automatically zero. ∎

### 2. Exact, exhaustive acceptance table

For k>=1 the entire formal comparison strictly decreases rho **if and only
if** the row below holds:

| Maximal cycle count k | Complete accepted point-depth domain |
|---|---|
| 1 through5 | j>=3 |
| 6 through11 | j>=2 |
| 12 through17 | j>=1 |
| 18 and higher | every j>=0 |

The statement covers every input in the domain, including all seven possible
remainders of h. For k=0 the plan retains the original request with coefficient
+1. For every other failure, its unique highest-rank request has coefficient
+1 and rank `eta>q`. It is never silently discarded.

**Height proof.** With `t=(2/3)^j`, formula (2) is

    eta = lambda*q + beta,
    lambda=(256/81)*a^k*t,
    beta=t*((1274/81)*a^k-16)-1 < -1.                (4)

The strict last inequality uses `1274<1296` and a<1. Therefore lambda<1
always implies eta<q. Exact integer comparison of
`256*2^(11k+j)` with `81*3^(7k+j)` gives the three transition pairs

    (k,j)=(5,2) fail, (6,2) pass;
           (11,1) fail, (12,1) pass;
           (17,0) fail, (18,0) pass,

and `(1,3)` passes. The three failing pairs still have eta>q at the
smallest q=5167; these are exact rational inequalities in (4), checked
as integers in the companion checker. Their slopes exceed1, so the
inequalities persist for all q>=5167. Decreasing k or j increases eta
at this positive range. Increasing k decreases lambda, and increasing j
decreases lambda; the negative beta already proves the passing side.
This proves the complete table, including all intercepts. Equivalently,

    32*3^(7k+j)*(eta-q)
      = (256*2^(11k+j)-81*3^(7k+j))*v
        +576*2^(11k+j)-512*2^j*3^(7k)-55*3^(7k+j).  (5)

No limiting slope approximation is used to decide a finite input.

### 3. Full signed plan and failure vectors

Let I be the negative current of (3), so `div I=[q]-[eta]`. Write
`z=nu(w)` and `div N_x=[x]-[nu(x)]`. The returned plan is

    J=N_(3w)+I-N_w+H_eta-H_z.                       (6)

If `A_s` denotes the full signed request vector of `H_s`, then

    div J=P(w)-A_eta+A_z.

Every coefficient is combined before the plan is returned. The lower
requests have rank at most `(9z+5)/8<q`, since `z<w/4`.

For k>=1, eta is canonical, `eta=-1 mod16`, and eta is0 or1 mod3.
Its first critical index u is respectively `eta/3` or `(2eta+1)/3`.
In either case u belongs to W5, `rho(u)=eta`, and has coefficient+1.
The remaining formal absorption requests have rank less than eta: they
come from `H_u`, whose bound is at most `(3eta+5)/8` or `(3eta+4)/4`.
Thus if eta<q every remaining request in (6) has smaller rank. If eta>q,
this unique leading request cannot cancel against any lower request or
any request from H_z. This proves necessity as well as sufficiency of
the table for this complete signed plan. It does not assert necessity for
some other representation of P(w).

For k=0, (6) is exactly the original R56 k4,h0 plan, with eta=b. Its
full vector identity is preserved:

    A_b=A_(3v)=A_q-A_ell+A_v,   ell=(q+2)/3,
    A_q={w:1}+A_w.

The complete W9 elimination at v has depth6; all auxiliary ranks after
subtracting A_z are below q. Hence the surviving original coefficient is
+1, rather than a new certificate. This includes every h<7.

`compile_plan` accepts only a descending plan and exact supplied currents
for every nonzero remaining request. It validates their boundaries and
substitutes them with their signed multiplicities. Missing or malformed
inputs are rejected. None of these inputs is assumed to exist universally.

### 4. Complete CRT phases and genuinely new direct domains

For k>=1 write

    b+17=2*3^(7k)*U,
    v=(3^(7k)*U-9)/4.

The binary congruence

    U=-19*3^(-7k) mod8192                            (7)

puts w in the required entry phase and makes U odd. For j>=1, either
e in{1,2} and

    U=2^(3-11k)*(1+3^j*e) mod3^(j+1)                (8)

give exact h=7k and exact point-depth j. These coprime congruences describe
whole infinite progressions. For j=0, one can choose the unique nonzero
unit U modulo3 with `2^(11k-3)*U=2 mod3`, giving h=7k; or choose
`U=3^r*e mod3^(r+1)` for any r=1..6, giving h=7k+r. Thus the constructor
includes every maximal-cycle remainder, not just exact multiples of7.

There are whole accepted progressions outside **all twelve previous direct
predicates**, for every prescribed old growing depth L>=0. Fix any passing
k,j with j>=1; in particular choose k=1,j=3. Impose (8) together with

    U=(2^(11L+20)*c-19)*3^(-7k) mod2^(11L+22),
    c=1 if L is even, and c=3 if L is odd.            (9)

Then for a positive odd s with `s=c mod4`,

    v=2^(11L+18)*s-7,
    q=81*2^(11L+13)*s-17.                            (10)

All sufficiently positive progression members (and the positive representatives
used by the constructor) give positive w. The congruences already force
`v=0 mod3`. Therefore:

- The old nine predicates fail on the R54 entry phase.
- R55 has first `(A,d)=(4,2)` and a canonical normalized endpoint class
  that fails its table; its second-block option applies only to `(2,2)`.
- R56 has both ray depths zero, since v=0 mod3.
- R57 takes exactly L guarded cycles and exits at e=13. Its exit odd
  parameter is `81*3^(7L)*s=1 mod4`. The complete raw exit is canonical
  and equals `a^(-(L+1))*(q+17)-17>q`. Its endpoint bound is that endpoint,
  so this direct test also fails.

This proves failure of the fixed twelve predicates throughout the entire
CRT progression. It does not prove failure of their arbitrary conditional
compositions or supplied-history closure. The new k=1,j=3 plan nevertheless
has a fourteen-arrow ancestor below the original q for every L. The seed
varies with L; no infinite positive growing orbit is asserted.

### 5. Relation to the known negative-cycle words

The ordinary negative cycles are used only to identify affine words, not
as actual positive sources. The full backward -5 word gives
`p=(8q-5)/9` on q4 mod9, already the earlier R41 inverse phase, including
its returning W9 row. For the -17 cycle, the only rotated endpoints with
ternary residue1 are -17 and -41. On selected critical images the former
is exactly R56's k4 domain; the latter has q4 mod9 and is already in R41's
strict phase. The other rotations are2 mod3 and cannot directly equal a
selected critical image (1 mod3) or a nonselected one (0 mod3).

The new operation is the **composition** of an initially expanding
four-arrow inverse tail, maximal cycle inverses, and the complete point
continuation, tested against the original q. It does not merely relabel
one bare rotated cycle. R49's permanent inverse-only exclusions remain
valid; this procedure supplies no universal inverse completion.

### 6. Reproduction and scope

Run `python3 experiments/residual_progress/cycle_inverse/check_cycle_inverse.py`.
The checker verifies the threshold constants, actual valuation words, full
failed vectors, all seven maximal remainders, CRT intersections, old-twelve
rejections, and exact supplied-current substitutions. Its receipt records
the finite ranges and retains complete designated current tables. Input
discovery has explicit caps and cycle detection; an exhausted cap is not
a negative theorem. The written proofs, rather than the finite scans,
provide the universal quantifiers above. This is model-assisted research,
not human peer review or formal verification.

The stored audit has512 exact affine checks and seven boundary comparisons;
99 complete signed plans (57 descending,30 higher-leading failures,12 original
self-requests); nine all-twelve-excluded progressions through L=64; and four
long-word checks through64 cycles or64 point arrows. Three actual supplied
conversions at215505781,827725813 and284897820661 have63,35 and91 output rows,
using5,5 and10 supplied pairs respectively. The first two complete plans,
input currents and outputs are stored. Eight designated invalid/missing-supply
checks are retained. These are finite evidence counts, not coverage estimates.

## Certificates

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B11 migration; standard library). The legacy scripts in this folder load their sibling modules by pre-migration folder names, so they no longer run here. This certificate rebuilds the legacy directory layout in a temporary directory from the node folders that now hold those files, runs the unmodified legacy checks there without `-O` (as `scripts/verify_all.py` did at `be73a66`), and requires exit 0 and every copied receipt unchanged. It writes nothing in the repository. It replays: the legacy checker `check_cycle_inverse.py` (about 11 s; the counts of section 6 and the stored tables, compared with `cycle_inverse_audit.json`) and the side-lane probe `r60_cycle_inverse_check.py` (under 1 s, receipt reproduced byte for byte). The command in the legacy text names `experiments/residual_progress/cycle_inverse/`.

## Remarks

- **Relation to the negative-cycle words** (section 5 of the note): the backward `−5` word is the R41 phase, the `−17` word with endpoint `−17` is exactly R56's `k = 4` domain ([`negative-cycle-backward-word`](../negative-cycle-backward-word/README.md)); the new operation is the composition of an expanding four-arrow inverse tail, maximal cycle inverses and the point continuation, tested against the original `q`. The permanent inverse-only exclusions of [`inverse-only-exclusions-short-forward`](../inverse-only-exclusions-short-forward/README.md) remain valid.
- Appended to the later fifteen-family dispatcher [`fifteen-family-rho-dispatcher`](../fifteen-family-rho-dispatcher/README.md) (R61-b). Novelty undetermined (none claimed).

## History

- Migrated from `experiments/residual_progress/cycle_inverse/CYCLE_INVERSE.md` (legacy ID R60) at commit `be73a66`, by the B11 migration (Claude, Opus 5.5). Note, scripts and receipts moved byte-identical; `check_legacy_replay.py` was added at the migration. The side-lane probe `reviews/side_lane/r60_cycle_inverse_check.*` and the main lane's review `experiments/residual_progress/side_lane_review_64a5981.md` and `.json` moved here. Legacy status: "written word-domain, maximality and complete conditional-plan classification".
- Main lane (ChatGPT, Codex), 2026-10-18, from commit `d265d94`. The batch's "independent model" proof and code reviews (archive/convergence-residual-progress/REPORT.md) were the main lane's own agents, not a different lane.
