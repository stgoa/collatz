---
id: binary-return-exit-control
kind: result
title: "The guarded Phi return has an exact binary countdown and a complete nineteen-row exit table at the original rank"
status: reviewed
claim: >
  Odd-only 3x+1 map S, absorbing at 1; retained critical basis of R75. Put A = 3^12, M = 2^19, B = 299947, D =
  7153, Phi(v) = (Av+B)/M, L(v) = Dv+B. On the guard v = 133797 mod 2^18 (equivalently 2^18 | L(v)) the raw word
  from 6v+1 and the word from 3v both have twelve arrows and end at 6Phi(v)+1 on v = 133797 mod 2^19; L(Phi(v)) =
  (A/M) L(v), T^12(3v) = 3Phi(v) on the re-entry cylinder, and a fixed guarded positive v has exactly
  floor((v2(L(v)) - 18)/19) complete re-entries, each consuming 19 binary digits, gaining 12 ternary digits and
  increasing v; every prescribed count occurs in the original coupled R89 cell, which is not invariant under Phi.
  At the maximal exit h = v2(L(v)) in 18..36, all 19 rows have an exact fixed ordinary prefix followed by one
  arbitrary valuation a >= p, with complete cylinders and pullbacks to the original parameter, and the raw
  endpoint test against the ORIGINAL Q is an exact affine inequality whose fixed (h, a) template fails for large
  r. The existing comparison has quotient clock 18+12r, ordinary clocks (23+12r, 5) and a unique highest request
  P(v_r) with coefficient +1; a fresh forward continuation to an exit y gives prefix(Q, L) + J_y - J_(Q/3) with
  every high request positive, so extending this history creates no negative high cancellation. Each fixed exit
  cell's terminal image is a tail of one residue class mod a power of 3, so unconditional absorption of one whole
  cell would already imply Collatz; conditional strict-premise pair repair is a distinct target. No decreasing
  measure across exits and no terminal supply.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [retained-history-w9-reduction, common-critical-rank-basis]
certificates: [check_legacy_replay.py]
evidence:
  - "check_phi_exit_control.py, phi_exit_control.py, phi_exit_control_audit.json: the legacy module, checker and receipt: 10 full return comparisons, all 19 rows, 171 signed exit comparisons, 15 modular ancestor certificates, 29 rejections, three stored exit plans with 156/283/498 rows, 65 controls where the raw y >= Q but the native plan descends; 37 local sources pinned. Fails at its new path: phi_exit_control.py loads ../retained_history/ (now ../retained-history-w9-reduction/) by its pre-migration folder name, and is loaded in turn by the legacy deeper_window/ and later_target_probe/ code; and Its receipt pins the SHA-256 of this node's legacy note PHI_EXIT_CONTROL.md, now an edited README, so it fails at its new path and in a legacy replay at earlier migrations (before rewritten notes were restored from git). Not reached at be73a66: the scripts/verify_all.py gate stopped earlier, at residual_progress/history_frontier (archive/legacy-checker-run-be73a66.md); it passed in full at 9dbc71a; A replay at this migration, before the note was edited, passed (exit 0, receipt unchanged). Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
  - "r90_phi_return_check.py, r90_phi_return_check.json: side-lane probe (Claude side lane, 2026-10-18 06:27) of the return words, the quotient identity and the re-entry counts. Fails at its new path: it imports affine_controls from experiments/packet_currents/negative_controls/ by repository-relative path (now ../locally-collatz-like-control-barrier/). Passed at be73a66 as reviews/side_lane/r90_phi_return_check.py (archive/legacy-checker-run-be73a66.md, exit 0); its receipt is reproduced byte for byte by check_legacy_replay.py"
  - "side_lane_review_86ead16.md, side_lane_review_86ead16.json: the main lane's pinned review (2026-10-18) of side commit 86ead16: byte-identical reproductions of r90_phi_return_check, batch_r61_r67_check and r64_lifted_cycle_check, the full output of r88_anchor_exhaustive.c (cited from four-target-history-classification), a replay of the PR1 minimality and 3x+61 controls, and the strategic assessment at R90/R91; it records that the side lane had not reproduced R91 at that commit"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: r90_phi_return_check.py
    scope: "Finite only (side-lane feed entry 2026-10-18 06:27, VERIFIED, main a94533a), with the lane's own step and ν: '**Return words.** On 2,000 random `v ≡ 133797 (mod 2¹⁹)`, both words end at `6Φ(v) + 1`'; '**Quotient identity.** On 500 members of the re-entry cylinder `v ≡ 102642092709 (mod 2³⁷)` ... `T¹²(3v) = 3Φ(v)` and `L(Φ(v)) = (3¹²/2¹⁹)·L(v)`'; '**Re-entry count.** On 3,000 guarded seeds, half of them forced to have a deep `v2(L)`, the number of complete re-entries found by direct iteration equals `⌊(v2(L(v)) − 18)/19⌋`.' The exit table, the signed comparisons and the ancestor-cover argument were not rebuilt; reproduced by the main lane in side_lane_review_86ead16.md. The status stays written"
  - by: Claude review lane (Fable 5.1; directed by Santiago Armstrong)
    date: 2026-10-31
    link: REVIEW-2026-10-31-claude-review-lane.md
    scope: "Full argument re-derived with an independent implementation: guard and words by exhaustion and on random inputs, the re-entry identity on 300 inputs, the countdown on 500 seeds, the original cell, the signed comparison for r = 1, 2 and the 19-row exit table with 171 exit cells (stored return and exit plans identical row for row), the raw inequality, the point shadow, the ancestor cover; certificate re-run (PASS, exit 0, 4.97 s); 3x+5 and 3x+13 scaled analogues hold and the actual cycles lie outside every guard. Verdict HOLDS; three imprecision-level findings, no correction to the claim"
aliases: [R90]
tags: [convergence, outer-residual, retained-history, binary-countdown, original-rank, exit-classification]
---

# The guarded Phi return has an exact binary countdown and a complete nineteen-row exit table at the original rank

## Statement

Odd-only clock `S`, 1 absorbing, quotient `T = νS`; the retained critical basis of [`common-critical-rank-basis`](../common-critical-rank-basis/README.md) (R75). Put `A = 3^12`, `M = 2^19`, `B = 299947`, `D = A − M = 7153`, `Φ(v) = (Av + B)/M`, `L(v) = Dv + B`.

1. **Return.** The broad guard is `v ≡ 133797 (mod 2^18)`, i.e. `2^18 | L(v)`. On `v ≡ 133797 (mod 2^19)` the words `(1,1,1,1,3,1,4,1,2,1,1,2)` from `6v + 1` and `(1,1,1,2,1,1,4,1,2,1,1,2)` from `3v` both end at `6Φ(v) + 1`. `L(Φ(v)) = (A/M)L(v)`, and on the re-entry cylinder `T^12(3v) = 3Φ(v)`.
2. **Countdown.** A fixed guarded positive `v` makes exactly `⌊(v2(L(v)) − 18)/19⌋` consecutive re-entries; each consumes 19 binary digits, gains 12 ternary digits and increases `v`. Every prescribed count occurs on the original coupled cell of [`retained-history-w9-reduction`](../retained-history-w9-reduction/README.md) (R89), `v0 = 67839005952677 + 2^18·3^18·ℓ`, `Q = 70506316836123 + 3·2^45·ℓ`, but that cell is not invariant under `Φ`.
3. **Signed comparison.** `T^(18+12i)(Q) = 3v_i`, `S^(23+12i)(Q) = S^5(3v_i)`; the full pair plan keeps a unique highest request `P(v_i)`, coefficient `+1`, rank `3v_i > Q`.
4. **Exits.** At the maximal exit `h = v2(L(v)) ∈ {18, …, 36}` all 19 rows have an exact fixed prefix followed by one arbitrary valuation `a ≥ p`, with complete cylinders and exact pullbacks to `ℓ`. The raw endpoint test against the original `Q` is an exact affine inequality; for fixed `(h, a)` it fails for all large `r`. Native normalisation can still succeed above `Q`.
5. **No negative high cancellation.** A fresh forward continuation to an exit `y` gives `prefix(Q, L) + J_y − J_(Q/3)` with vector `A_y − A_(Q/3)`; every request of rank `≥ Q` is positive.
6. **Ancestor cover.** Each fixed exit cell's terminal image is a tail of one residue class modulo `3^(L+1)`, so unconditional absorption of one whole cell would already imply Collatz. This is not an equivalence for the pair currents, nor an obstruction to conditional repair.

## Proof

The legacy note "Complete control of the guarded Phi exits" follows, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**Status: written arithmetic classification and conditional finite-current
construction. No universal current supply or whole-type termination is proved.**

This package merges the exact binary return with every maximal exit row. It
keeps the original threshold fixed, every signed premise, and both ordinary
clocks. The raw endpoint test is a complete arithmetic test for that endpoint;
it is not a test for all possible current constructions. The ancestor-cover
statement concerns unconditional absorption, not pair currents alone.

The inputs come from the [retained-history cell](../retained-history-w9-reduction/README.md).
Use the odd-only Syracuse map S with absorption at1, elementary normal form nu,
and quotient T=nu composed with S on canonical states. Write P(w)=[3w]-[w].
The native critical-basis plan is [s]=div J_s+A_s.P, with nonnegative integral
coefficients A_s and every request rank rho(u)=nu(3u) at most nu(s). Both W5 and
W9 input types remain available. A finite formal current becomes an actual
pair current only after every remaining signed pair premise is supplied.

### Exact return and its guards

Put

    A = 3^12 = 531441, M = 2^19 = 524288,
    B = 299947, D = A-M = 7153,
    Phi(v) = (A v+B)/M, L(v)=D v+B.

The broader binary version of the coupled R89 input condition is

    v = 133797 (mod 2^18).

Equivalently, beta=(729v+35)/4096 is an integer congruent to 5 modulo 64.
This is exactly one progression with minimal modulus 2^18; it does not contain
the original retained-cell ternary condition.

The two exact ordinary Syracuse valuation words

    raw start 6v+1: (1,1,1,1,3,1,4,1,2,1,1,2),
    start 3v:      (1,1,1,2,1,1,4,1,2,1,1,2)

both end at 6Phi(v)+1. Both words have length12; their
valuation sums are respectively 19 and 18. Their common complete v-cylinder is
v=133797 modulo 2^19. To check completeness, a fixed odd valuation word of sum
E has exact starting cylinder modulo 2^(E+1). Substitution of 6v+1 removes one
binary bit for the raw word; substitution of 3v preserves all bits for the
second word. The representative 133797 has the displayed words, and the
opposite lift 395941 has last valuation 3 instead of 2. The affine endpoints
of both words are

    (1594323 v+1161985)/262144 = 6Phi(v)+1.

In particular, re-entry into the broader guard implies both words are valid.
Indeed, the guard is L(v)=0 modulo 2^18, and

    L(Phi(v)) = (3^12/2^19)L(v).

Thus the exact single re-entry cylinder is

    v = -B D^(-1) (mod 2^37),

whose least residue is 102642092709. It implies the complete word cylinder.
The quotient identity on this re-entry cylinder is T^12(3v)=3Phi(v).
For an explicit check, put C=(81v+11)/64, beta=(729v+35)/4096,
X=18beta+1 and Z=(81beta+7)/4. The elementary normalization formulas give
T^4(3v)=3C, T^7(3v)=X, T^9(3v)=Z and T^12(3v)=3Phi(v).
The guard fixes the required selection bits. In the first intermediate segment,
the selected sibling's negative three-row tail cancels the three-row upper
prefix, as in the retained-history construction. This verifies the quotient
clock separately from the ordinary words. The ordinary twelve-step endpoint
is 6Phi(v)+1.

### Maximal repetitions, growth, and original-cell intersection

For a positive guarded v, let h=v2(L(v)). Since L(v)>0, h is finite. The exact
maximum number of consecutive guarded re-entries is

    floor((h-18)/19).

Each such return reduces h by 19, increases v3(L) by 12, and increases v:
Phi(v)-v=L(v)/M>0. The prime-to-6 part of L is conserved. This is a genuine
finite countdown for this one subsystem. No bound on later exits or subsequent
return mechanisms follows from it.

For every r>=0, all starts with at least r re-entries form the complete cylinder

    v = -B D^(-1) (mod 2^(19r+18)).

These cylinders intersect the original coupled R89 cell for every r. Write

    V0=67839005952677, P0=2^18*3^18,
    v=V0+P0*l, m=2736+4096*l.

Let c_r be the least nonnegative residue -B D^(-1) modulo 2^(19r+18), and set

    l_r = ((c_r-V0)/2^18)*(3^18)^(-1) modulo 2^(19r).

Then precisely l=l_r+2^(19r)j, j>=0, gives the required original-cell starts.
All inverses are of odd integers, and c_r-V0 is divisible by 2^18.

Only the START is asserted to lie in the original retained ternary cell. On
that original cell v3(L(v))=4, so for its raw r0=6v+1 and first return g,

    v3(g-r0)=v3(6L(v)/2^19)=5.

The original raw cell has period 128*3^19, so it is not invariant under this
return. Arbitrarily long repetitions use different starting
integers and the broader binary guard, not invariance of the original cell.

### Full signed comparison at the fixed original threshold

For the original m and Q=133704987+3*2^33*m, set b=Q/3. Let v_i=Phi^i(v_0).
The original ordinary 18-prefix ends at 6v_0+1. Concatenating the exact raw words
therefore gives an actual ordinary prefix of length 18+12i ending at 6v_i+1.
Every v_i in the guard is 37 modulo 64. Its selected terminal sibling has the
same five-step tail as 3v_i. Consequently

    S^(23+12i)(Q) = S^5(3v_i),
    T^(18+12i)(Q) = 3v_i.

Keep both clocks. If K_i is the difference of these two finite ordinary path
currents, then div K_i=[Q]-[3v_i]. With native critical-basis absorption plans
[s]=div J_s + A_s.P, the complete conditional pair identity is

    P(b) = div(K_i+J_(v_i)-J_b)
           + ({v_i:+1}+A_(v_i)-A_b).P.

No coefficient is dropped. Its request v_i has coefficient +1 and is the
unique highest-rank request, with rho(v_i)=3v_i>Q. The other positive requests
have rank at most (3v_i+1)/16 because the first elementary reduction and free
arrow of v_i supply that bound. Negative A_b requests have rank below Q.
All remaining ranks are below 3v_i, but they are NOT claimed below the fixed
original Q for arbitrary i. This is why an increasing raw return does not by
itself establish a repeated admissible R89 original-Q plan or a supply theorem.

### Maximal-exit parameters and the fixed original threshold

Put V0=67839005952677, VP=2^18*3^18. The original coupled sources are

    v0=V0+VP*l,
    Q=70506316836123+3*2^45*l
     =(2^27*v0-213949807)/3^17, l>=0.

At the maximal return count r the exit v=Phi^r(v0) has
h=v2(Dv+B) in {18,...,36}. Its complete exit cylinder is

    v=c_h+2^(h+1)*t,
    c_h=(2^h-B)*D^(-1) modulo 2^(h+1).

Every prescribed r,h occurs in the original cell. The next section refines
this cylinder by the exact first variable valuation, including its extra bit.

### Nineteen complete prefixes, followed by one arbitrary valuation

Let W=(1,1,1,1,3,1,4,1,2,1,1,2), the twelve-arrow raw return word.
The table gives the maximal fixed ordinary prefix from 6v+1 on the entire
h-cylinder. At its end the next valuation a is any integer a>=p. E is the
sum of the fixed prefix valuations, and ell its length.

|h|fixed prefix|ell|E|p|
|--|--|--:|--:|--:|
|18|W without its final 2|11|17|3|
|19|W|12|19|2|
|20|W,1|13|20|2|
|21|W,1,1|14|21|2|
|22|W,1,1,1|15|22|2|
|23|W,1,1,1,1,1|17|24|1|
|24|W,1,1,1,1,2|17|25|1|
|25|W,1,1,1,1|16|23|4|
|26|W,1,1,1,1,3|17|26|2|
|27|W,1,1,1,1,3,1,1|19|28|1|
|28|W,1,1,1,1,3,1,2|19|29|1|
|29|W,1,1,1,1,3,1,3|19|30|1|
|30|W,1,1,1,1,3,1|18|27|5|
|31|W,1,1,1,1,3,1,4|19|31|2|
|32|W,1,1,1,1,3,1,4,1,1|21|33|1|
|33|W,1,1,1,1,3,1,4,1|20|32|3|
|34|W,1,1,1,1,3,1,4,1,2|21|34|2|
|35|W,1,1,1,1,3,1,4,1,2,1|22|35|2|
|36|W,1,1,1,1,3,1,4,1,2,1,1,1|24|37|1|

This is a finite affine verification, not a sampled classification. Start
x=alpha*t+beta with alpha=6*2^(h+1), beta=6*c_h+1. At each fixed step,
v2(3*beta+1)<v2(3*alpha), so that valuation is constant for all t. At the
listed stopping point, p=v2(3*alpha) and v2(3*beta+1)>=p. Define the odd
integer u=3*alpha/2^p and the integer z=(3*beta+1)/2^p. The exact next-a
cell, with j=a-p>=0, is

    t=(2^j-z)*u^(-1) modulo 2^(j+1).

Every such cell is nonempty and includes the required extra bit. In particular
p=h+2-E. The constructor computes all integer affine states; the checker independently
verifies each fixed valuation and the first variable one.

The resulting exact exit-v residue has modulus 2^(E+a). Writing
C_r=B*(A^r-M^r)/D, its pullback to v0 has modulus 2^(19r+E+a), with residue

    v0=(M^r*c_exit-C_r)*(A^r)^(-1) modulo 2^(19r+E+a).

Divide the difference from the original v0 base by 2^18, then invert 3^18,
to obtain the exact original l progression. This determines *exactly* r
re-entries, exit h, and next valuation a, not just lower bounds.

### Complete raw-target test, keeping original Q

For the listed fixed prefix, define its affine constant c by
x=(6*3^ell*v+c)/2^E. Initialize c=1,E=0; an arrow of valuation e changes
c to 3c+2^E and E to E+e. After the variable arrow let t0=ell+1 and
c_star=3c+2^E. Its actual endpoint is

    y=[6*3^t0*(A^r*v0+C_r)+M^r*c_star]/[M^r*2^(E+a)].

Exactly y<Q if and only if

    [2^27*M^r*2^(E+a)-6*3^(t0+17)*A^r]*v0
      > 3^17*[6*3^t0*C_r+M^r*c_star]
        +213949807*M^r*2^(E+a).

The right side is positive. Thus a nonpositive bracket excludes the raw-target
stop on the entire fixed (r,h,a) cell. A positive bracket gives an exact lower
bound on v0; intersecting it with the complete progression handles any finite
initial exceptions. This is only the raw-target test. Native normalization can
succeed above Q, so its failure is not a missing-current claim.

Any fixed h,a has a positive fixed terminal slope multiplied by (A/M)^r.
Therefore the raw-target stop cannot work on that fixed exit template for
arbitrarily large r. A variable exit valuation can compensate; no argument
here forces it to be large enough.

### Signed inputs: forward history creates no negative high cancellation

The concatenated ordinary path from the original Q to y has length

    L=18+12r+ell+1.

For b=Q/3, its complete native formal pair plan is

    P(b)=div(prefix(Q,L)+J_y-J_b)+(A_y-A_b).P.

All requests of A_b have rank<Q, while the native absorption coefficients in
A_y are nonnegative. Consequently every request with rank>=Q in this fresh
plan is positive. No high negative request can be cancelled merely by
retaining more of this one forward history. The original inherited D+E+F
relations stay below the original Q and likewise cannot cancel those high
requests. A new cancellation needs another comparison or a separate retained
history. This does not exclude progress by a potential on positive vectors.

### A scope fact: each fixed exit cell is an unconditional ancestor cover

For fixed r,h,a, let L be the total ordinary word length above, and E_total
its total valuation sum. The original Q step is 3*2^45. The exact word fixes
l modulo 2^(E_total+1-45), because its complete cylinder has modulus
2^(E_total+1). Here E_total=26+19r+E+a>=46. Therefore the complete cell's
terminal image is exactly

    y=y_min+2*3^(L+1)*j, j>=0.

It is a tail of all odd integers in one residue class modulo 3^(L+1), with
no remaining binary restriction. This supplies an explicit ancestor-cover
property. Given any positive odd z not divisible by3, choose e with

    2^e*z=3*y_min+1 modulo 3^(L+2).

Such e exists because 2 generates the units modulo powers of3. Adding the
period 2*3^(L+1) makes e arbitrarily large. Then p=(2^e*z-1)/3 is an odd
member of the terminal progression once large enough, and S(p)=z. Its unique
preimage Q in the fixed cell is positive and reaches z after L+1 arrows.
For a seed divisible by3, its next Syracuse state is not divisible by3.

Thus unconditional absorption of *one complete fixed exit cell* already
implies Collatz. This is NOT an equivalence for the pair currents P(Q/3)
alone, and NOT an obstruction to a useful conditional repair with strictly
smaller original-Q premises. Those must remain distinguished. The statement
also does not assume a uniform bound on the exponent e; it may be very large.

Elementary justification of the unit generator: v3(4^(3^j)-1)=j+1 by the
binomial induction. Hence 2 has order 2*3^(K-1) modulo3^K, the entire number
of units.

### Why the gained ternary order does not automatically make a long point chain

The rational centre of the raw word is -1792529/7153. Every finite ordinary
word applied to that centre remains a rational with reduced denominator
7153 times a power of2: multiplication by3 is invertible modulo7153.
It can never equal -1. Therefore, after any fixed exit word, the exact finite
value v3(y_shadow+1) stabilizes the maximal point-chain length once the gained
ternary precision exceeds it. The latter grows with r, but the former does
not. With variable a, high point depth is a separate congruence in 2^a; it is
not a consequence of r alone. Multi-ray inverse words are outside this claim.

### Consequences and unresolved obligation

The binary budget is a well-founded countdown for consecutive Phi re-entries.
It does not control how another branch changes the affine centre or replenishes
precision. The original ternary cell is not closed, the raw return grows, and
all high requests in a fresh forward comparison are positive. These statements
rule out treating the countdown or the endpoint table as terminal supply.

The exact whole-exit obligation remains: supply every remaining pair current
at the original rank, or prove a recurrence which terminates across all exits.
The interface permits parameter-dependent histories and additional signed
comparisons. It does not exclude multi-ray inverse words, later targets,
nonlocal histories, or richer progress measures. The separate first-ray/point
scratch obstruction is intentionally not part of this result.

### Executable interface and verification

`phi_exit_control.py` exports:

- `repeat_parameters(count,index)` and `repeat_comparison(...)`: complete
  at-least-count cylinders and full signed original-Q comparisons;
- `exit_row(h)`: the exact row and its maximal fixed affine prefix;
- `exit_parameters(count,h,a,index)`: complete exact-count/exit/valuation cells;
- `exit_comparison(...)`: actual forward current plus every native signed
  request, explicit high frontier and exact raw inequality;
- `ancestor_exponent(target,anchor,power)`: a modular exponent certificate for
  the ancestor-cover argument, without materializing enormous powers of2.

Both comparison constructors have an explicit ordinary-prefix cap, default
10000. They reject invalid integer domains and incomplete capped comparisons.
No absorption search or dispatcher extension is performed. A returned
`descending` status means every retained premise is strictly below the
original threshold; it does not mean those premises have been supplied.

Replay with:

    python3 experiments/residual_progress/phi_exit_control/check_phi_exit_control.py

The checker independently recomputes ordinary arrows and current boundaries,
replays complete cells and exact progression increments, and pins reachable
local source dependencies. The finite receipt is
[phi_exit_control_audit.json](phi_exit_control_audit.json). Its finite samples
support the written arguments; they do not establish their universal scope by
sampling. No terminal absorption current is assumed or searched for.


The frozen focused receipt covers10 full return comparisons (two indices for
r=1,2,4,8,16), all19 exact rows, and171 full signed exit comparisons
(r=0,1,4; every h; a=p,p+1,p+3). Every exit also checks the next progression
member and its exact image increment. All ten return plans and three exit
plans are stored in full; the latter have156/283/498 current rows. Fifteen
modular ancestor certificates and29 explicit invalid-premise/cap controls are
retained. Sixty-five tested cases have raw y>=Q while their native formal plan
is descending, preserving the non-necessity of the raw stop. Reachable source
pinning covers37 local files. Generation and default replay each took about
1.5 seconds. These are conditional comparisons; no terminal inputs were
supplied or silently discarded.

## Certificates

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B13 migration; standard library). The legacy scripts load sibling modules by their pre-migration paths, so they no longer run here. This certificate calls `tools/legacy_replay.py`, which rebuilds the pre-migration layout in a temporary directory from `tools/legacy_paths.json`, runs the unmodified legacy scripts there without `-O` (as `scripts/verify_all.py` did at `be73a66`), and requires exit 0 and every copied file unchanged. It writes nothing in the repository. It replays: the side-lane probe `r90_phi_return_check.py` (under 1 s, receipt reproduced byte for byte): the two return words on 2,000 guarded inputs, the quotient identity on 500 re-entry inputs, and the re-entry count on 3,000 seeds. The legacy checker `check_phi_exit_control.py` was not replayed at the B13 migration, which predated restoring hash-pinned notes from git; it is now (see below and `evidence`). The command in the legacy text names `experiments/residual_progress/phi_exit_control/`.

At the B18-replay-revival migration [`check_legacy_replay.py`](check_legacy_replay.py) was extended to replay also `check_phi_exit_control.py`, which now passes in the legacy layout because rewritten notes are restored from git at `be73a66` (about 15 s in all). It checks finite steps only; the status is unchanged.

## Remarks

- The countdown proves departure from one subsystem only; it gives no decreasing measure across subsequent exits. R67's count ([`mixed-rank-growing-blocks`](../mixed-rank-growing-blocks/README.md)) includes the last guarded step whose image may leave the guard; this one counts complete returns. The two conventions differ (side_lane_review_86ead16.md).
- The unpromoted first-ray/point scratch obstruction mentioned in the note is not part of this result.
- No novelty is claimed.

## History

- Migrated from `experiments/residual_progress/phi_exit_control/PHI_EXIT_CONTROL.md` (legacy ID R90) at commit `be73a66`, by the B13 migration (Claude, Opus 5.5). Note, scripts and receipts moved byte-identical; the note became this README, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Legacy status: "written arithmetic classification and conditional signed construction; terminal supply remains open".
- The main lane's review `side_lane_review_86ead16.md` and its record `.json` (`experiments/residual_progress/`, 2026-10-18) moved here with the side-lane probe they reproduce.
- Main lane (ChatGPT, Codex), 2026-10-18, first committed in `a94533a`. The batch's "independent" proof, source and default-replay reviews recorded in archive/convergence-residual-progress/REPORT.md were the main lane's own agents, not a different lane.
- 2026-10-31: reviewed by the Claude review lane (Fable 5.1; directed by Santiago Armstrong); status raised to reviewed. No correction to the claim or proof; the review records that for the minimal next valuation `a = p` the raw-target bracket is negative already at `r = 0` in all 19 rows, that the quotient identity `T^12(3v) = 3Φ(v)` does not extend from the re-entry cylinder to the broader word cylinder (so the stated restriction is necessary), and that the pair index `b = Q/3` is a `W9` index. See [`REVIEW-2026-10-31-claude-review-lane.md`](REVIEW-2026-10-31-claude-review-lane.md).
