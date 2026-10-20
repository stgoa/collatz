---
id: rational-basin-precision-barrier
kind: result
title: "A finite rational basin bounds every inverse word at c0, so no smaller original source reaches the repeated target within 12r + 5 steps"
status: written
claim: >
  Computer-assisted. Odd-only 3x+1 map S, absorbing at 1, canonical quotient T = nu S, extended to the signed
  canonical quotient on rationals with reduced denominator D = 7153. At c0 = -899841/7153, every legal finite
  quotient inverse word of length d and affine slope lambda, with arbitrary ray indices, satisfies lambda
  (3^12/2^19)^max(0, ceil((d-5)/12)) >= 1, with equality for reversed complete twelve-step cycles. Proof: a first
  strict counterword must start at a primitive odd canonical -u/7153 with 7153 < u < 7277133 (written reduction),
  and two independent exact implementations (signed Python, positive-magnitude C++) classify all 1,732,883
  eligible origins, with no cap reached: only 19 reach c0, all with first-hit score >= 1, every other origin being
  resolved by a path to a classified state, another cycle or the invariant region x > -1. Written corollary: on
  the original coupled cell v0 = 67839005952677 + 2^18 3^18 ell, Q = 70506316836123 + 3 2^45 ell, if at least r
  guarded Phi returns are available and n_r = 3 Phi^r(v0), no positive canonical p <= Q reaches n_r in d <= 12r+5
  quotient steps (every inverse ray and word; also ordinary histories), via p >= n0 + 1 - (243/32) 2^(7r) > Q; Q
  itself reaches n_r at depth 18+12r. No all-depth positive exclusion, exclusion of longer histories, later
  targets or signed currents, and no terminal supply.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [elementary-bridge-quotient-normal-form, binary-return-exit-control, retained-history-w9-reduction]
certificates: [check_shadow_precision_recompute.py, check_legacy_replay.py]
evidence:
  - "check_shadow_precision.py, shadow_precision.py, shadow_precision_audit.json, independent_basin.cpp: the legacy Python classifier, checker, receipt and the independent C++ classifier (compiled and compared only with --cpp): the full 1,732,883-origin basin with its 19 hit records, the c0 cycle, the branch inequalities, 306 positive inverse words on 21 families through r = 128, and 14 invalid-domain rejections. Fails at its new path: the checker loads ../history_cell_scope/history_cell_scope.py (now ../four-target-history-classification/) by its pre-migration path, and its receipt pins the SHA-256 of this node's legacy note SHADOW_PRECISION.md and of ../phi_exit_control/PHI_EXIT_CONTROL.md, now edited READMEs. Not reached at be73a66: the scripts/verify_all.py gate stopped earlier, at residual_progress/history_frontier (archive/legacy-checker-run-be73a66.md); it passed in full at 9dbc71a; A replay at this migration, before the note was edited, passed (exit 0, receipt unchanged). Its Python audit is recomputed by check_shadow_precision_recompute.py; the C++ comparison needs a compiler and is not part of the certificate. Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
  - "c0_basin_classify.c, c0_basin_receipt.py, c0_basin_receipt.json: the side lane's independent C classification (Claude side lane, 2026-10-18 06:34) of the c0 basin on R91's universe and on the larger deeper-window universe 7153 < u < 741545113, with its wrapper and receipt; fourteen-step-window-original-source cites it. The wrapper compiles the C program with cc, so it is evidence, not a certificate. Passed at be73a66 as reviews/side_lane/c0_basin_receipt.py (archive/legacy-checker-run-be73a66.md, exit 0, 8.8 s)"
  - "side_lane_review_8ed32bc.md, side_lane_review_8ed32bc.json: the main lane's pinned review (2026-10-18) of side commit 8ed32bc: byte-identical reproduction of c0_basin_receipt in 5.71 s, source inspection of the signed-quotient convention and overflow range, and the scope note that the floating minimum-slope diagnostic is not an exact certificate and that the C program does not verify R92's suffix proof"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: c0_basin_classify.c
    scope: "Finite only (side-lane feed entry 2026-10-18 06:34, FINDING (exhaustive, independent C)): '**Validation on R91's universe** (`7153 < u < 7277133`). Every published figure matches exactly: 1,732,883 eligible origins; 19 in the c₀ basin; largest intermediate numerator 1,049,066,989,135; smallest weighted slope μ = 1.' and 'Neither the candidate's reduction (§§2–5) nor the R91 theorem is re-proved; this entry supplies only the exhaustive finite table the candidate requires.' Reproduced by the main lane in side_lane_review_8ed32bc.md, which notes that the minimum slope is a floating-point diagnostic. The status stays written"
aliases: [R91]
tags: [convergence, outer-residual, computer-assisted, rational-shadow, inverse-barrier, ternary-precision]
---

# A finite rational basin bounds every inverse word at c0, so no smaller original source reaches the repeated target within 12r + 5 steps

## Statement

**Computer-assisted.** Odd-only clock, 1 absorbing; canonical quotient `T = νS` with the complete inverse table of [`elementary-bridge-quotient-normal-form`](../elementary-bridge-quotient-normal-form/README.md) (R25), extended to a deterministic signed quotient on rationals `−u/D` with reduced denominator `D = 7153`. Put `A = 3^12`, `M = 2^19`, `γ = A/M`, `B = 299947`, `c0 = −3B/D = −899841/7153`, `k(d) = max(0, ⌈(d − 5)/12⌉)`.

1. **All-word slope theorem.** Every legal finite quotient inverse word at `c0`, of length `d` and slope `λ`, with arbitrary ray indices, satisfies `λ·γ^k(d) ≥ 1`. Reversing complete twelve-step cycles of `c0` gives equality.
2. **How it is proved.** A first word with score below 1 must start at a primitive odd canonical `−u/D` with `7153 < u < 7277133` (written reduction, independent of the word length). Two independent exact classifiers resolve all 1,732,883 eligible origins with no cap: 19 reach `c0`, each with first-hit score at least 1; every other origin reaches a classified state, a different cycle, or the invariant region `x > −1`. The largest visited numerator is 1,049,066,989,135. This finite classification is the computer-assisted step.
3. **Positive corollary (written).** On the original coupled cell of [`binary-return-exit-control`](../binary-return-exit-control/README.md) (R90), `v0 = 67839005952677 + 2^18·3^18·ℓ`, `Q = 70506316836123 + 3·2^45·ℓ`, suppose at least `r` guarded returns, and let `n_r = 3Φ^r(v0)`. No positive canonical `p ≤ Q` reaches `n_r` in `d ≤ 12r + 5` quotient steps, over every inverse ray and word, with no bound on intermediate heights; the same holds for ordinary histories. The bound is `p ≥ n0 + 1 − (243/32)·2^(7r) > Q`, using `n0 > 2Q` and `L(v0) ≥ 81·2^(19r+18)`, for every eligible source. The original `Q` reaches `n_r` at depth `18 + 12r`, thirteen steps beyond the window.

## Proof

The legacy note "Accumulated ternary precision cannot supply a smaller original history" follows, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**R91 — computer-assisted inverse-word theorem and written positive-source
corollary.** A finite, completely classified rational-shadow graph supplies
one step of the proof. The theorem includes every inverse ray and every
finite word in the stated slope test. Its positive-source consequence excludes
all smaller histories through the accumulated-precision horizon. It does not
exclude longer histories, different future targets, arbitrary signed currents,
or absorption of a fixed positive source. No novelty is asserted.

Use absorbed odd Syracuse S, the canonical normal form nu, and T=nu S from
[R25](../elementary-bridge-quotient-normal-form/README.md). The positive family and
its exact growing return are those of
[R90](../binary-return-exit-control/README.md), built from the retained cell in
[R89](../retained-history-w9-reduction/README.md). This result preserves that
original source cutoff rather than comparing only with the growing endpoint.

### 1. The complete rational inverse-word theorem

Set

    A=3^12=531441,       M=2^19=524288,
    D=A-M=7153,         B=299947,
    gamma=A/M>1,        c0=-3B/D=-899841/7153.

Consider the signed canonical quotient on rationals with reduced denominator
D, defined in Section2. For any legal quotient inverse word W starting at c0,
let d be its length and lambda its positive affine slope. Every inverse ray
index is allowed. Put

    k(d)=max(0,ceil((d-5)/12)),
    mu(W)=lambda*gamma^k(d).                              (1)

**Theorem.** Every such finite word satisfies

    mu(W)>=1.                                             (2)

The bound is sharp: reversing any number of complete twelve-step cycles of
c0 gives equality. No assertion that those are the only equality words is
needed. In particular, if d<=12k+5 for any k>=0, then

    lambda*gamma^k>=1.                                    (3)

Thus no word in this entire precision budget gains a factor below1/3, or
even below1, relative to reversing the available growing returns. This is a
slope theorem at one explicit rational centre, not a global rank theorem.

### 2. Exact signed quotient and unrestricted inverse branches

For x=N/D with N odd and gcd(N,D)=1, all residue statements use modular
inverses of D. Define

    S(x)=(3x+1)/2^v2(3x+1).

Normalize by repeatedly replacing x with(x-1)/4 while x=5 mod8, then applying
x->(x-1)/2 if x is selected. The selected condition is the usual condition:
x=3 mod4, a=v2(x+1), and the odd unit (x+1)/2^a is3^a mod4. All valuations
of signed nonzero integers use their absolute value.

These operations preserve reduced denominator D. Indeed their numerator
updates are congruent, modulo any divisor of D, to multiplication by a unit.
The exceptional values -1 and -1/3 therefore cannot occur. The valuation
arguments are nonzero; repeated F normalization terminates because each
F division decreases the finite value v2(3x+1) by2. This defines a genuine
deterministic signed quotient T. It is used only for the finite rational
comparison; no convergence property of this signed map is assumed.

The algebraic inverse classification of R25 extends to this domain. Its
base inverse branches (a*x+b)/3 are:

| x modulo3 | Point | First ray base | Second ray base |
|---|---|---|---|
|0|none|(8x+3)/3|(16x+3)/3|
|1|none|(4x-1)/3|(32x+19)/3|
|2|(2x-1)/3|(64x+19)/3|(128x+83)/3|

Each ray continues by p->64p+49. At arbitrary index L>=0 its state is

    p_L=64^L*p_0+7(64^L-1)/9.                            (4)

The proof of completeness uses exact valuation and residue conditions and
terminating normalization; positivity of the original integer is not needed.
The denominator D is coprime to3, so the same residue tests select integral
numerators. Every inverse branch x->alpha*x+beta satisfies

    alpha>=2/3,      alpha-beta>=1,      beta>=-1/3.        (5)

These inequalities hold for both full rays, not just their bases. They show
that every inverse state from c0 is strictly below-1. It has the form -u/D,
where u>D is an odd integer coprime to D and -u/D is canonical.

For independent finite checking, the forward map can use positive numerator
u. First put z=(3u-D)/2^v2(3u-D). Normalize -z/D by the same signed tests:
F division sends z to(z+D)/4, and selected halving sends it to(z+D)/2.
Since D=1 mod8, the signed residue tests reduce to tests on -z modulo8 and4.
The inverse slope of this forward quotient arrow is2^e/3, where e is its
ordinary valuation plus twice the number of F divisions plus the selected
halving indicator.

If a forward orbit crosses into x>-1, it cannot later reach c0. The interval
(-1,infinity) is invariant under S and both normalizing operations. Exact
x=-1 is excluded by the reduced denominator. A detected other cycle also
certifies nonmembership in the c0 basin. Neither test presumes general
termination of the signed map.

### 3. Why the arbitrary-word question has a finite origin universe

The following reduction makes the finite calculation exhaustive. It also
records how the bound depends on the proposed score threshold.

Fix 0<tau<=1. Suppose an inverse word with mu<tau exists, and choose one
with least length d. Write lambda_j for its prefix slope and k_j=k(j).
Every proper prefix satisfies lambda_j*gamma^k_j>=tau.
The empty word has score1, so this first strict counterword has d>=1.

At shadow -u_j/D put t_j=u_j-D>0. Initially t0=892688. By(5), an inverse
arrow gives

    t_j=alpha_j*t_(j-1)+D*delta_j,
    delta_j=alpha_j-beta_j-1,       0<=delta_j<alpha_j.

Consequently

    t_d=lambda_d*t0+D*sum_(j=1)^d(delta_j*lambda_d/lambda_j)
       <tau*t0+D*sum_(i=0)^(d-1) gamma^(k_i-k_d)
       <tau*892688+12D*gamma/(gamma-1)
       =tau*892688+12*531441.                             (6)

For the geometric estimate, k=0 occurs at the six prefix depths0..5; every
subsequent k occurs at twelve depths. Bounding every count by12 gives the
stated strict upper bound. The unknown inverse depth and all ray indices
have disappeared from(6).

For tau=1, every first counterword therefore begins at a canonical rational
-u/D with

    7153<u<7277133,       u odd,       gcd(u,7153)=1.        (7)

The largest possible odd numerator is7277131. Intermediate states need not
remain below this bound. The finite calculation follows their actual paths;
it does not impose(7) as an intermediate height cap.

### 4. Complete finite basin classification

The signed forward orbit of c0 has exactly twelve states. The table displays
positive numerators u, so the actual states are -u/D; e is the arrow's inverse
binary exponent.

|u|next u|e|
|---:|---:|---:|
|899841|1346185|1|
|1346185|2015701|1|
|2015701|3019975|1|
|3019975|1135173|3|
|1135173|1699183|1|
|1699183|1272599|2|
|1272599|952661|2|
|952661|1425415|1|
|1425415|1067273|2|
|1067273|1597333|1|
|1597333|2392423|1|
|2392423|899841|3|

The exponent sum is19. From a given origin, any subsequent visit to c0 adds
(12,19) to its first-hit depth and exponent sum. Since k(d+12)=k(d)+1, this
leaves mu unchanged. Hence only the first hit needs to be tested.

Two independent exact implementations, Python using signed numerators and
C++ using positive magnitudes, classify **all1,732,883** canonical origins in
(7). They agree on every c0 hit below. No time, state, path-length, or overflow
cap was reached. The largest numerator visited was1,049,066,989,135, well
above(7) and within the checked arithmetic range. The19 hit origins are:

|u|first-hit d|exponent sum E|mu=2^(E-19k)3^(12k-d)|
|---:|---:|---:|---:|
|899841|0|0|1|
|952661|5|8|256/243|
|1067273|3|5|32/27|
|1135173|8|13|81/64|
|1272599|6|10|729/512|
|1346185|11|18|3/2|
|1425415|4|7|128/81|
|1597333|2|4|16/9|
|1699183|7|12|243/128|
|2015701|10|17|9/4|
|2392423|1|3|8/3|
|3019975|9|16|27/8|
|3789185|5|10|1024/243|
|4791999|1|4|16/3|
|5054631|6|12|729/128|
|5622977|16|28|512/81|
|5680201|4|9|512/81|
|6047103|9|17|27/4|
|6746661|7|14|243/32|

All scores are at least1. Every other origin is classified by a complete
forward path to a previously classified state, a different detected cycle,
or the invariant interval x>-1. The finite reduction(6), this exhaustive
classification, and invariance under further c0 cycles prove(2). This is the
computer-assisted part of the theorem. A capped or incomplete classification
would not prove it.

### 5. Positive sources: all inverse words through the gained precision

Return to the original positive coupled cell. For ell>=0 put

    v0=67839005952677+2^18*3^18*ell,
    Q =70506316836123+3*2^45*ell,
    n0=3v0,                 L(v)=Dv+B.

Here n0>2Q, v3(L(v0))=4, and v2(L(v0))>=18. Suppose at least r>=0 guarded
returns are available, equivalently

    v2(L(v0))>=19r+18.

Define v_r=Phi^r(v0), n_r=3v_r. R90 gives the exact quotient and ordinary
comparisons

    T^(18+12r)(Q)=n_r,
    S^(23+12r)(Q)=S^5(n_r).                               (8)

The second equality is a two-clock merger, not an assertion that the ordinary
prefix of length18+12r ends at n_r. The algebraic centre identity is

    n_r-c0=gamma^r(n0-c0),
    v3(n_r-c0)=12r+5.                                    (9)

**Corollary.** No positive canonical p<=Q reaches n_r in d<=12r+5 quotient
steps. This includes every inverse ray and every inverse word in that
horizon, without a height bound on its intermediate states.

#### Shadow legality

Lift any such actual inverse word to a shadow starting at c0. Before its
j-th inverse step, the actual-shadow difference has ternary order at least
12r+5-(j-1)>=1. Their residues modulo3 therefore agree at every required
branch decision. The complete inverse formulas and(5) keep the shadow
canonical, with reduced denominator D, and strictly below-1. Thus the actual
word is one of those covered by(2). Its slope satisfies lambda>=gamma^(-r),
since k(d)<=r.

#### Intercept and original-cutoff bound

For the prefix slopes lambda_j, (5) gives lambda_j>=(2/3)^j. Summing the
possible negative affine offsets yields

    p=lambda*n_r+lambda*sum_(j=1)^d beta_j/lambda_j
      >=lambda*[n_r+1-(3/2)^d].                           (10)

The bracket is positive under the bounds below. Substituting lambda>=gamma^(-r),
using d<=12r+5 and(9), gives

    p >= n0+[-c0+gamma^(-r)(c0+1)]-(243/32)*2^(7r)
      >= n0+1-(243/32)*2^(7r).                            (11)

The last bracketed term is at least1 because c0<-1 and gamma^(-r)<=1.

The original binary order and exact ternary order imply

    L(v0)>=81*2^(19r+18),
    n0>=(243*2^(19r+18)-3B)/D.

For every r>=0 this gives

    n0/2>(243/32)*2^(7r).                                 (12)

At r0 the required exact inequality is243*(2^18-D/16)>3B. For larger r,
factoring2^(7r) and using2^(19r)>=2^(7r) makes its left-side advantage only
larger. Since n0>2Q, (11)-(12) prove p>Q. They also establish the positivity
needed in(10) before lambda is replaced by its lower bound.

The source comparison n0>2Q follows coefficientwise from the displayed
positive affine formulas; it is not an asymptotic estimate. Equality and
small-parameter cases are therefore covered.

An ordinary history from a positive odd p<=Q to n_r in at most12r+5 arrows
is also impossible: T^d(nu(p))=nu(S^d(p))=n_r and nu(p)<=p. Absorption at1
creates no exception because the positive target n_r is greater than1.

### 6. What this excludes, and what it leaves open

The accumulated ternary precision does not, by itself, supply a smaller
original partner at the repeated target. Every allowed word within that
precision has now been covered. In particular, arbitrarily large inverse
ray indices and combinations of multiple rays do not evade this bound.

The known original source still reaches n_r at quotient depth18+12r,
thirteen steps beyond the excluded horizon. Different terminal targets,
longer inverse histories, adaptive constructions using deeper digits,
multiple signed comparisons, and eventual absorption remain open. The
positive seed changes when arbitrary r is prescribed; a fixed positive
source has only finitely many guarded returns. No infinite positive orbit,
closed recurrence across all exits, or failure of all finite currents follows.

The shadow theorem(2) is stronger than a bounded-depth search: its finite
origin reduction covers all inverse-word lengths. Its positive consequence
still has the explicit clock bound12r+5 because that is the available
ternary precision linking an actual word to the shadow. These are distinct
quantifiers and should not be conflated.

### 7. Reproduction and evidence

Run `python3 experiments/residual_progress/shadow_precision/check_shadow_precision.py`.
Add `--cpp` to compile and compare the independent C++ classifier in temporary
storage. The explicit `--write` option regenerates the stored receipt.

The accompanying exact Python and C++ classifiers reconstruct the full finite
origin classification and compare the19 hit records and summary counts. The
checker also verifies the cycle, branch inequalities, source-cell identities,
positive transfer bounds, and negative/domain controls. Missing supply is not
converted to an absorption current; this theorem constructs no terminal
current. Default replay compares the stored audit receipt; regeneration is
explicit. Any cap or arithmetic-range failure is an unresolved computation,
not a nonmembership result.

## Certificates

[`check_shadow_precision_recompute.py`](check_shadow_precision_recompute.py) (written at the B13 migration; standard library). At the B13 migration no legacy check of this node passed: its legacy checker pins the SHA-256 of notes that are now edited READMEs. Since the replay restores those notes from git, the unmodified checker now passes too (see below). The certificate rebuilds the pre-migration layout in a temporary directory from `tools/legacy_paths.json`, replaces each pinned note by a placeholder, imports the unmodified legacy checker there and runs its audit, and requires the result to equal the committed receipt after removing only those note hashes; every other value, including the hashes of the pinned code and data, must agree. It writes nothing in the repository. It reruns the exact Python classification of all 1,732,883 origins and the other checks of the receipt (about 15 s). The independent C++ classifier `independent_basin.cpp` and the side lane's C classifier `c0_basin_classify.c` need a compiler and are evidence only. The commands in the legacy text name `experiments/residual_progress/shadow_precision/`.

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B18-replay-revival migration; standard library) replays the unmodified legacy check `check_shadow_precision.py` in a temporary copy of the legacy layout built by `tools/legacy_replay.py`, requiring exit 0 and every file unchanged (about 26 s). It checks finite steps only; the status is unchanged.

## Remarks

- The universal word quantifier rests on the first-counterword reduction plus the exhaustive finite basin, not on the 306 positive samples. The result is computer-assisted in that sense.
- It excludes the specific proposal that accumulated ternary precision supplies a smaller history at the repeated target; longer histories, later targets, deeper digits and signed comparisons remain open. The fourteen further steps are settled by [`fourteen-step-window-original-source`](../fourteen-step-window-original-source/README.md) (R92).
- The main lane's REPORT records two independent mathematical reviews and a source/C++ review, all by its own agents. The side lane reproduced the finite classification independently only later (feed 06:34, `8ed32bc`).
- No novelty is claimed.

## History

- Migrated from `experiments/residual_progress/shadow_precision/SHADOW_PRECISION.md` (legacy ID R91) at commit `be73a66`, by the B13 migration (Claude, Opus 5.5). Note, scripts and receipts moved byte-identical; the note became this README, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Legacy status: "computer-assisted inverse-word theorem with a written positive-source corollary".
- The side-lane C program and wrapper `reviews/side_lane/c0_basin_classify.c`, `c0_basin_receipt.*` and the main lane's review `side_lane_review_8ed32bc.*` (`experiments/residual_progress/`) moved here.
- Main lane (ChatGPT, Codex), 2026-10-18, first committed in `a94533a`. The batch's "independent" proof, source and default-replay reviews recorded in archive/convergence-residual-progress/REPORT.md were the main lane's own agents, not a different lane.
