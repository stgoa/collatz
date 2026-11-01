---
id: native-height-inverse-obstruction
kind: result
title: "Adjacent currents: an all-ray inverse barrier at the native height, with a fixed forward certificate on the same family"
status: reviewed
claim: >
  Odd-only 3x+1 map S, absorbing at 1; T = nu S; D(q) = [q+2] - [q] and native height n(q) = (8q-5)/9 on the R65
  adjacent domain (canonical q = 31 mod 108). For every D >= 3, t >= 1 put q = 31 + 2^57 3^D t, n = 27 + 2^60
  3^(D-2) t. Every canonical predecessor p with T^d(p) = q, 1 <= d <= D, over every inverse ray index, is either n
  itself (d = 2, base ray then point inverse) or exceeds q; so no ordinary odd source below n reaches q in at most
  D ordinary arrows. The same family keeps the fixed 35-arrow word from 31 to 23 (total valuation 56), ending at y =
  23 + 2 3^(D+35) t with 8n - (9y+5) = 4 + 2 3^(D-2) t (2^62 - 3^39) > 0, and q+2 has one arrow to (3q+7)/4 < n;
  together these give an exact conditional D(q) current whose signed helper requests all have rho < n (at q = 31 no
  request remains). Transporting R44 through R65 is row for row the original endpoint comparison. The seed varies
  with D; the whole adjacent domain stays open and no dispatcher coverage is claimed.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [adjacent-source-defect-equivalence, inverse-only-exclusions-short-forward, returning-forward-interface, rank-excess-absorption-classification, elementary-bridge-quotient-normal-form, decreasing-w5-phase-inverse-barrier]
certificates: [check_legacy_replay.py, batch_r68_r70_check.py]
evidence:
  - "check_native_height.py, native_height.py, native_height_audit.json: the legacy constructor and checker: 2496 complete sampled inverse words through depth 5 (ray indices 0/1), three eight-branch words at ray indices 8/32/128, 120 paired binary runs, 120 transported-current identities, 48 family instances through D = 128, nine rejections, and two stored current demonstrations (q = 31: 45 rows, no supplied pair; q = 3891110078048108575: 345 rows from 15 supplied pairs). Fails at its new path: native_height.py loads ../defect_normal_form/ (now adjacent-source-defect-equivalence/) by its pre-migration folder name. Passed at be73a66 as experiments/residual_progress/adjacent_recursion/check_native_height.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran every residual-progress step before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a); replayed unchanged, with its receipt, by check_legacy_replay.py"
  - "batch_r68_r70_check.py, batch_r68_r70_check.json: side-lane probe (Claude side lane, 2026-10-18 08:37) of R68 and R70 with the lane's own S, nu and T; self-contained, it runs in place and rewrites its receipt byte for byte (checked at migration); passed at be73a66 as reviews/side_lane/batch_r68_r70_check.py (archive/legacy-checker-run-be73a66.md, exit 0). mixed-exit-growing-reentry cites it from this folder"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: batch_r68_r70_check.py
    scope: "Finite only (side-lane feed entry 2026-10-18 08:37, VERIFIED, main 9190ccf), with the lane's own S, nu and T, nothing imported from main: the six-state anchor {1, 7, 9, 11, 17, 25} with its T-edges and T^2(27) = 31 through 41; the 35-arrow word from 31 to 23 with cost 56 and nu(23) = 11; for D = 3..12 and six values of t (60 cases) q and n = (8q-5)/9 canonical, q = 31 (mod 108), an inverse-tree search over every branch and ray index (at most 28 nodes) finding n at d = 2 as the only canonical a < q with T^d(a) = q, 1 <= d <= D; the same word from q ending at y, and 8n - (9y+5) > 0. Finite D only; the all-ray proof and the conditional current were not rebuilt; the status stays written"
  - by: Claude review lane (Fable 5.1; directed by Santiago Armstrong)
    date: 2026-10-31
    link: REVIEW-2026-10-31-claude-review-lane.md
    scope: "Full re-derivation of the six-state anchor, the all-ray shadow and gap argument, the semiconjugacy step and the forward certificate (5)-(6); independent pruned exhaustive inverse search (validated against brute force) on 63 family instances through D = 20, request-level check of (6) and of the anchor q = 31 with this lane's own W5-only planner, 9,260 adjacent-domain binary runs; both certificates re-run (PASS, exit 0, 9.3 s in all); verdict HOLDS"
aliases: [R68]
tags: [convergence, outer-residual, tripling-pairs, adjacent-source, native-height, inverse-barrier]
---

# Adjacent currents: an all-ray inverse barrier at the native height, with a fixed forward certificate on the same family

## Statement

Odd-only clock, 1 absorbing; `ν`, `T = νS`; the complete canonical inverse branches of R25/R41. On the adjacent domain of [`adjacent-source-defect-equivalence`](../adjacent-source-defect-equivalence/README.md) (canonical `q ≡ 31 mod 108`), `D(q) = [q+2] − [q]` and its native height `n(q) = (8q − 5)/9`; missing pair currents must have rank strictly below `n`, not merely below `q`.

1. **Inverse barrier.** For every `D ≥ 3`, `t ≥ 1` put `q = 31 + 2^57·3^D·t`, `n = 27 + 2^60·3^(D−2)·t`. Every canonical predecessor `p` with `T^d(p) = q`, `1 ≤ d ≤ D`, over every inverse ray index, is either `n` itself (`d = 2`: base ray then point inverse) or exceeds `q`. Hence no ordinary odd source below `n` reaches `q` in at most `D` ordinary arrows.
2. **Forward certificate.** The same family keeps the fixed 35-arrow word from 31 to 23 (total valuation 56), ending at `y = 23 + 2·3^(D+35)·t`, with `8n − (9y + 5) = 4 + 2·3^(D−2)·t·(2^62 − 3^39) > 0`; and `q + 2` has one ordinary arrow to `(3q + 7)/4 < n`. Together they give an exact conditional `D(q)` current whose signed helper requests all have `ρ < n`; at `q = 31` no request remains.
3. **Transport.** Transporting the R44 rule ([`returning-forward-interface`](../returning-forward-interface/README.md)) through R65 is row for row the original endpoint comparison.

The seed varies with `D`, so this is not a permanent obstruction at one input. The whole adjacent domain stays open; no new dispatcher coverage is claimed.

## Proof

The legacy note "Adjacent currents: a native-height inverse barrier and forward separation" follows, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**Status: written scoped separation theorem and finite exact certificates.**
This does not close the whole adjacent-source domain or add a dispatcher
rule. It identifies a complete family on which arbitrary bounded inverse
depth fails at the required height, even though a smaller ancestor exists,
while a fixed ordinary forward word gives a conditional current below that
height. The seed varies with the depth. No infinite divergent orbit, global
search limitation, novel-result claim, or universal current supply follows.

Use absorbed odd Syracuse `S`, the elementary minimum `nu`, quotient
`T=nu S`, killed atoms `[1]=0`, and the complete canonical inverse branches
of R25/R41. For canonical `q=31 mod108`, let

    D(q)=[q+2]-[q],           n(q)=(8q-5)/9.

Here n is the native height from
[R65](../adjacent-source-defect-equivalence/README.md). Missing pair
currents must have their original critical-image rank strictly below n,
not merely below q. The all-ray affine argument extends the scoped
[R49 inverse barrier](../inverse-only-exclusions-short-forward/README.md).

### 1. Why two tempting adjacent rewrites give no new recursion

The ordinary word `(1,2)` takes n to q. Pulling the negative source q
back along this word leaves `[q+2]-[n]`. Since q+2 has an ordinary
successor at most `(3q+7)/4<n`, its positive source already belongs to
the supplied absorbing component under the intended lower-input
induction. The remaining absorption at n has not been supplied.

More precisely, let u=(2q+1)/3 and a=nu(u). R65's pair-to-adjacent
conversion has local current

    K=N_(3u)-N_u+J_(q+2)-J_a.

If G is the full returning prefix from q to r, the R44 plan has current

    L=N_(3u)+G-N_u+J_r-J_a.

Their exact subtraction is

    K-L=J_(q+2)-G-J_r,
    requests=A_(q+2)-A_r.                             (1)

Thus transporting that returning rule through the adjacent equivalence
is exactly the direct forward comparison, including every signed row.
It does not acquire a new endpoint or a better rank by changing notation.

The complete initial paired binary run has the same unresolved upper
endpoint. Write

    q=2^a t-1, a>=2, t odd,
    t=-3^a mod4,       2^a t=5 mod27.

The q-side has word `1^(a-1),2`, length a, ending at
`r=(3^a t-1)/2`. If a=2m, the positive source q+2 has m-1 valuation2
arrows to `F(z)`, z=3^(m-1)t, and the elementary sibling current changes
F(z) to z. Its residual is `[z]-[r]`. If a=2m+1, it has m valuation2
arrows to `2z+1`, z=3^m t, with residual `[2z+1]-[r]`.
The even branch's positive common-tail clocks are `(m,1)` from
`(q+2,z)`; the odd branch has an actual m-arrow prefix. The negative
prefix always has a ordinary arrows. These are not a single ordinary
clock for the signed source. Absorbing the known positive endpoint
alone leaves exactly the R44 endpoint r. No recursive closure is proved.

### 2. A six-state certificate at the native anchor

The canonical origins below27 and their entire T-forward closure are

    Q={1,7,9,11,17,25},
    T: 1->1, 7->11, 9->7, 11->17, 17->1, 25->9.      (2)

Every listed edge is direct arithmetic. Forward closure and omission of31
prove that no canonical origin below27 reaches31 at any depth. The only
canonical integer in `[27,31)` is27, and `T^2(27)=31` through41.
Consequently31 has exactly one canonical ancestor below31, namely27.

The fixed ordinary prefix from31 to23 has length35, total valuation56,
and exact valuation word

    W=(1,1,1,1,2,2,1,2,1,1,2,1,1,1,2,3,1,1,
       2,1,2,1,1,1,1,1,3,1,1,1,4,2,2,4,3).         (3)

Since nu(23)=11 belongs to Q, this also verifies absorption of31.
In particular27 reaches31 only at its second quotient step: a later
occurrence would force a return cycle through31. These finite data are
stored and verified without an uncapped trajectory search.

### 3. The complete all-ray native-height obstruction

**Theorem.** Fix D>=3 and t>=1, and set

    q=31+2^57*3^D*t,
    n=27+2^60*3^(D-2)*t=(8q-5)/9.                    (4)

Both states are canonical and q is in the entire R65 adjacent domain.
For every canonical predecessor p with `T^d(p)=q`, 1<=d<=D, exactly
one of the following occurs:

* d=2 and p=n, from the base ray0 followed by the point inverse;
* p>q.

The statement includes every inverse ray index. In particular no ordinary
odd source below n reaches q in at most D ordinary arrows.

**Proof.** Shadow any complete inverse word at31. Congruence modulo3^D
keeps each branch legal at the actual and shadow states throughout d<=D.
Write the affine result as

    p_i=lambda_i*(q-31)+c_i,    lambda_i=2^(A_i)/3^i.

Every c_i is a positive canonical ancestor of31. By (2), either c_i=27
or c_i>=31. The complete inverse affine branches `y->alpha*y+beta`
satisfy `alpha-beta>=1`, strictly on every ray, including all ray indices.
The first inverse at31 is a ray, since31=1 mod3. Therefore the exact gap

    G_i=lambda_i-(c_i+1)/32,
    G_i=alpha_i*G_(i-1)+(alpha_i-beta_i-1)/32

is strictly positive for i>=1. If c_i>=31, this gives lambda_i>1 and
p_i>q. If c_i=27, the finite anchor path proves that this word has length2
and is precisely ray0 at index0 followed by point. Its slope is8/9,
so p_i=8(q-31)/9+27=n. This exhausts every branch, without a ray-index
cutoff. For an ordinary predecessor x<n, semiconjugacy gives the canonical
predecessor nu(x)<=x<n, contradicting this classification. ∎

The presence of the explicit smaller ancestor n is the point of this
variant: a test which asks only for descent below q reports progress,
although the actual adjacent obligation requires strict descent below n.
The theorem concerns the prescribed depth and varies q with D. It does
not assert that every lifted q permanently misses smaller supplied history.

### 4. The same family has a fixed forward conditional certificate

Every q in (4) preserves word W because the exact cylinder modulus is
`2^(56+1)`. Its endpoint is

    y=23+2*3^(D+35)*t.

The complete original-rho formal absorption bound gives all H_y requests
below n, since

    8n-(9y+5)
      =4+2*3^(D-2)*t*(2^62-3^39)>0.                 (5)

The strict integer inequality `2^62>3^39` is checked exactly. For the
positive source, q+2 has one valuation2 arrow to
`s=(3q+7)/4<n`. Here s=1 mod3, so R58 gives every H_s request at most s:
its sole possible above-minimum exception is divisible by3.

Let G_q be the ordinary 35-arrow current along W and let E be the
one-row current at q+2. Then

    J=E+J_s-G_q-J_y,
    c=A_s-A_y,
    div J=D(q)-sum_v c(v)P(v),     rho(v)<n.          (6)

Every signed coefficient and both sources are retained. Exact supplied
currents for the remaining pairs yield an exact D(q) current; missing or
incorrect supply is rejected. The same formula is valid at the anchor
q31, with n27. The inverse obstruction and the fixed forward certificate
therefore hold on the same full parameter family. This is a structural
separation, not a new universal rule or a claim that these examples were
outside every previous accepted domain.

### 5. Reproduction and limits

`native_height.py` implements the finite anchor verification, arbitrary
all-ray shadow-word audit, the family (4), complete paired binary prefixes,
and the conditional current (6). `check_native_height.py` records bounded
word and family checks and finite supplied-current demonstrations. The
infinite inverse quantifiers follow from the proof, not from sampling ray
indices. Fixture discovery has explicit step/bit caps and cycle detection.

Run `python3 experiments/residual_progress/adjacent_recursion/check_native_height.py`.
The receipt checks 2496 complete sampled inverse words through depth 5 with
ray indices 0/1, three eight-branch words at ray indices 8/32/128, 120 full
paired binary runs, 120 exact transported-current identities, and 48 family
instances through D128. These samples do not replace the unbounded-ray
proof. Two complete current demonstrations are stored: q31 has 45 rows
and no supplied pair, while q3891110078048108575 has 345 rows after 15
distinct pair currents are supplied. All fifteen input tables are retained.
Nine negative checks reject invalid domains, insufficient precision,
an illegal inverse, an incorrect native height, missing or malformed
supply, and a zero fixture cap. The fixture limits are 10000 steps and 512
bits. Default execution compares the complete receipt and local source
hashes; `--write-receipt` regenerates it after inspection.

Universal closure of D(q) is still open. Retained lower history and new
forward comparisons remain available; another inverse search or a renamed
returning pair does not by itself establish the required native descent.

## Certificates

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B12 migration; standard library). The legacy scripts of this folder load sibling modules by their pre-migration paths, so they no longer run here. This certificate calls `tools/legacy_replay.py`, which rebuilds the pre-migration layout in a temporary directory from `tools/legacy_paths.json`, runs the unmodified legacy scripts there without `-O` (as `scripts/verify_all.py` did at `be73a66`), and requires exit 0 and every copied file unchanged. It writes nothing in the repository. It replays: the legacy checker `check_native_height.py` (about 6 s; the counts of section 5 of the note and the two stored current demonstrations, compared with `native_height_audit.json`). The commands in the legacy text name `experiments/residual_progress/adjacent_recursion/`.

[`batch_r68_r70_check.py`](batch_r68_r70_check.py) (under 1 s; side lane, independent code with its own `S`, `ν` and `T`): the R68 anchor, word and family checks listed under `reviewed_by`, and the R70 exit table and re-entries of [`mixed-exit-growing-reentry`](../mixed-exit-growing-reentry/README.md). Self-contained; it runs at this path and rewrites its receipt byte for byte.

## Remarks

- The inverse barrier extends the scoped R49 barrier of [`inverse-only-exclusions-short-forward`](../inverse-only-exclusions-short-forward/README.md) to every ray index. The explicit smaller ancestor `n` is the point: a test asking only for descent below `q` would report progress, while the adjacent obligation needs descent below `n`.
- The failed joint binary-run rewrite (section 1) and the related history audit are recorded in [`retained-lower-currents-adjacent-source`](../../attempts/retained-lower-currents-adjacent-source.md).
- Novelty undetermined (none claimed).

## History

- Migrated from `experiments/residual_progress/adjacent_recursion/NATIVE_HEIGHT_SEPARATION.md` (legacy ID R68) at commit `be73a66`, by the B12 migration (Claude, Opus 5.5). Note, scripts and receipt moved byte-identical; `check_legacy_replay.py` was added at the migration. The side-lane probe `reviews/side_lane/batch_r68_r70_check.*` (R68 and R70) moved here. Legacy status: "written all-ray separation and conditional adjacent-current construction".
- Main lane (ChatGPT, Codex), 2026-10-18, from commit `a489973`. The batch's "independent model" proof and code reviews (archive/convergence-residual-progress/REPORT.md) were the main lane's own agents, not a different lane.
- 2026-10-31: reviewed by the Claude review lane (Fable 5.1; directed by Santiago Armstrong); status raised to reviewed. No corrections; three imprecisions (the R58 step in section 4 needs `s` canonical, which holds since `s ≡ 25 (mod 2^55)`; the factor `2^57` serves only the forward cylinder; the legality of the shadow word at every depth) are recorded in [`REVIEW-2026-10-31-claude-review-lane.md`](REVIEW-2026-10-31-claude-review-lane.md).
