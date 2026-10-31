---
id: absorbed-fibre-uniform-counts
kind: result
title: A supplied current through N certifies the infinite elementary closure I_N, whose count in every band [X, 2X) is N/4 + O(log N) uniformly in X
status: reviewed
claim: >
  Odd-only 3x+1 map, absorbing at 1; nu and the canonical set B of elementary-bridge-quotient-normal-form. Let
  I_N = {x > 0 odd : nu(x) <= N} = union of the components {F^k(q), F^k(2q+1)} over canonical q <= N. (Certificates,
  conditional) Given a supplied finite integer current H with div H = U_N (either sign allowed), every requested
  x in I_N gets a finite exact current with divergence delta_x and an actual nonnegative absorption path on the
  supplied rows plus at most 2 floor(log2(2N+2)) + 2 explicit bridge rows, independently of how high x lies; this
  is a certificate for each requested member, not one finite current for the infinite set, and members of I_N have
  bounded hitting times once the input is supplied. (Count) For every pair of integers X >= N >= 8,
  B_N(X) = #{odd x in [X, 2X) : nu(x) <= N} satisfies |B_N(X) - N/4| <= 2 floor(log2 N) + 3, so its proportion
  among odd integers of the band is N/(2X) + O(log N / X). This is actual integer membership; it does not prove that
  any orbit enters I_N, gives no orbit-hitting probability, and does not imply Collatz convergence.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [elementary-bridge-quotient-normal-form]
certificates: [fibre_count_check.py, check_legacy_replay.py]
evidence:
  - "check_fibers.py, fibers.py, fiber_audit.json: the legacy constructor (band_count, telescope_count, conditional certificates) and checker (912 small bands, 42 boundary bands at odd cutoffs, 18 high bands with multipliers through 2^512, 56 conditional current conversions including F-exponents 128, supplied absorption through 96 discovered with a 1000-step cap per seed). Fails at its new path: fibers.py loads ../bridge_normal_form/normal_form.py (now ../elementary-bridge-quotient-normal-form/) by its pre-migration path. Passed at be73a66 as experiments/residual_progress/absorbed_fibers/check_fibers.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran these steps before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a). Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
  - "fibre_count_check.py is also the import hub of the side lane: run_bridge_check and quotient_iteration_probe (../complementary-run-bridges/), batch_r33_r36_check (../mixed-shrinking-pair-rules/), batch_436f51f_check (../critical-tripling-domain-equivalence/) and about 19 later probes import it from their own folder, so they fail at their new paths"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-17
    link: fibre_count_check.py
    scope: "Finite only (side-lane feed entry 2026-10-17 20:23, VERIFIED, main 541101a): the normal form rebuilt by descent from the two bridge moves without importing main's code; brute-force descent on every odd x in [X, 2X) agrees exactly with the count over the components {F^k(q), F^k(2q+1)}, q in B, q <= N, for N in {8, 13, 64, 100, 257, 1000} and X up to N 2^14; the component count stays within the stated bound for X = N 2^64, N 2^200 and N 2^512, the largest error used being 19% of the bound. The written telescoping proof was not re-derived; the status stays written"
  - by: Claude review lane (Fable 5.1; directed by Santiago Armstrong)
    date: 2026-10-31
    link: REVIEW-2026-10-31-claude-review-lane.md
    scope: "Full argument re-derived (the finite-component lemma and bridge row count of section 1, the level formula, the telescope (8)-(11), the K bound and (12), the hitting-time statement of section 4) and checked with the lane's own nu on 5936 brute-force bands, 120 bands at X up to N 2^1000 and 9000 hitting times; both certificates re-run (PASS, exit 0, 12 s and 6 s); the 3x+d controls fail the hypothesis, as the conditional statement requires. Verdict HOLDS; three imprecision notes, no correction"
aliases: [R27]
tags: [convergence, outer-residual, normal-form, known-set, counting, conditional]
---

# A supplied current through N certifies the infinite elementary closure I_N, whose count in every band [X, 2X) is N/4 + O(log N) uniformly in X

## Statement

Odd-only clock, absorbing at 1; `U_N` gives weight 1 to each odd `3 ≤ q ≤ N`. With `ν` and the canonical set `B` of [`elementary-bridge-quotient-normal-form`](../elementary-bridge-quotient-normal-form/README.md), put `I_N = {x odd : ν(x) ≤ N} = ⋃_(q ∈ B, q ≤ N) {F^k(q), F^k(2q + 1) : k ≥ 0}`, an infinite set containing every odd `x ≤ N`.

1. **Conditional certificates.** Given a supplied finite integer current `H` with `div H = U_N` (any signs), each requested `x ∈ I_N` has a finite current `J_x + H_ν(x)` of divergence `δ_x`, from which an actual nonnegative absorption path on supplied rows and explicit bridge edges is extracted; the bridge needs at most `2⌊log₂(2N + 2)⌋ + 2` rows, independently of `x`. This certifies each requested member; it is not one finite current for an infinite measure. Members of `I_N` have hitting times bounded by the maximum of 2 and the known canonical hitting times through `N`.
2. **Uniform count.** For all integers `X ≥ N ≥ 8`, `|#{odd x ∈ [X, 2X) : ν(x) ≤ N} − N/4| ≤ 2⌊log₂ N⌋ + 3`. Hence the proportion among odd integers of the band is `N/(2X) + O(log N / X)`, leading term `1/(2H)` at `X = HN`.

The count is actual integer membership, conditional on the supplied lower current for the certificates. It does not prove that any orbit enters `I_N`, is not an orbit-hitting probability, does not describe the finite forward union of known seeds, and does not imply Collatz. No novelty, formal verification or human review is claimed.

## Proof

The legacy note "An infinite known set from a finite supplied current" follows, lightly edited (headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**Status: written conditional construction and uniform arithmetic count.**
The input is a finite exact current for absorption through a specified cutoff
N. The construction certifies any requested member of an explicit infinite
set, including arbitrarily large members. It does not prove that an unknown
orbit enters this set, and it does not imply universal Collatz convergence.
No novelty, formal verification, or human review is claimed.

Use positive odd integers, the odd-only Syracuse clock, and absorption at1.
The measure delta1 and current row at1 are killed. Let U_N assign weight1 to
each odd integer3<=q<=N. The count theorem below holds for every pair of
integers X>=N>=8; divisibility of N by8 is unnecessary for this local result.

### 1. The known elementary closure is infinite

The [complete elementary-bridge normal form](../elementary-bridge-quotient-normal-form/README.md)
defines the canonical set B and the map nu. Its components are exactly

```
C_q={F^k(q),F^k(2q+1): k>=0},    q in B,
F(x)=4x+1,
B={q=1 mod8} union {q=2^a t-1: a>=2, t=-3^a mod4}.
```

All integers here are positive and odd. Every q in B is the unique smallest
element of its component. For every odd x the normal-form constructor returns
a finite integer current J_x with

```
div J_x=delta_x-delta_nu(x).                            (1)
```

Define

```
I_N={x>0 odd: nu(x)<=N}
   = union_(q in B, q<=N) C_q.                         (2)
```

The equality follows from the complete component classification, so the
display includes every member of this elementary closure. It contains all
positive odd integers at most N because nu(x)<=x. It is infinite because
even the component C_1 contains two infinite F-rays.

Suppose a finite integer current H satisfying `div H=U_N` is supplied.
H may have either sign. For any requested x in I_N, put q=nu(x). The
finite nonzero-row graph of H contains an absorbing path from q when q>1.
Indeed a finite weak component disjoint from1 has total divergence zero;
it cannot contain any of the positive U_N sources. A finite functional
component containing the absorbing vertex1 has a directed path to1 from
each of its vertices. This argument needs no global exclusion of cycles.

Let H_q be the nonnegative path current from q, or zero if q=1. Then

```
div(J_x+H_q)=delta_x.                                  (3)
```

Although this summed current can be signed, the same finite-component
argument extracts an actual nonnegative absorption path for x from its
nonzero-row graph. Its edges are a subset of the supplied graph together
with the explicitly constructed bridge edges. The constructor therefore
follows no unknown outer future. All boundary terms, including target1,
are handled exactly.

This gives a finite certificate for each requested member of an infinite
set; it is not one finite current whose divergence is an infinite measure.
Any finite nonnegative integer source supported on I_N can be certified
by summing its individual currents, with all source multiplicities retained.
Already supplied absorption paths can be reused as proof inputs.

The bridge size depends on N, not on how high x lies in its F-ray. Its
F-root is q or2q+1, at most2N+1. An F-sibling comparison uses at most two
current rows; the possible R23 bridge uses two explicit prefixes of length
`a<=floor(log2(2N+2))`. Thus at most

```
2*floor(log2(2N+2))+2                                  (4)
```

bridge rows suffice, before cancellations, independently of x. Integer
bit length and the size of the supplied current still affect computation.

### 2. A single affine sequence for each canonical base

Interleave the two F-rays by defining, for s>=0,

```
f_s(q)=2^s q+beta_s,
beta_s=(2^s-1)/3          when s is even,
beta_s=(2^(s+1)-1)/3      when s is odd.                (5)
```

The offsets are integers. For s=2k this is F^k(q), and for s=2k+1 it is
F^k(2q+1). The complete normal-form theorem ensures that every pair (q,s),
q canonical, represents a distinct integer. Consequently the desired band
count is

```
B_N(X)=#{odd x in [X,2X): nu(x)<=N}
      =sum_(s>=0) #{q in B: 1<=q<=N, X<=f_s(q)<2X}.    (6)
```

Only O(log N) levels can contribute, uniformly in X>=N. If a level has a
member, then beta_s/2^s is between0 and2/3, so

```
X/(N+2/3) <= 2^s < 2X.
```

Their exponent range has length O(log(N+1)). `band_count` evaluates (6)
by exact canonical progression counts, with inclusive and strict endpoints
implemented using `(X-1-beta_s)//2^s` and `(2X-1-beta_s)//2^s`.
It has O(log^2 N) arithmetic-count complexity independent of X; the bit
cost of those arithmetic operations does depend on X.

### 3. Exact telescoping improves the uniform error to O(log N)

Let K(Y) count canonical positive integers at most Y. For any real t, define

```
K_N(t)=#{q in B: 1<=q<=N, q<=t},
A_s(t)=K_N((t-1-beta_s)/2^s),                          (7)
```

where t will be an integer X or2X. Thus A_s(t) counts the level-s members
strictly below t. Every sum below is finite because A_s(t)=0 for all
sufficiently large s.

Reindexing (6), and using X>=N, gives the exact identity

```
B_N(X)=K(N)+sum_(s>=1) [A_s(2X)-A_(s-1)(X)].         (8)
```

Indeed the first unsummed term is `A_0(2X)=K_N(2X-1)=K(N)`.
Crucially, (8) telescopes the exact count before any replacement by a
leading density.

The two real arguments in the s-th correction differ by

```
d_s=(1+2 beta_(s-1)-beta_s)/2^s
   = 1/3+2/(3*2^s),        s even;
   =-1/3+2/(3*2^s),        s odd.                    (9)
```

For s>=1, `|d_s|<=1/2`; at s=1 the difference is zero. An interval of
length at most1/2 contains at most one integer, so every correction in
(8) has magnitude at most1.

It remains to bound the number of potentially nonzero corrections without
introducing a dependence on log X. Put

```
c_s=(1+beta_s)/2^s,      1/3<c_s<=1.
```

The two arguments in (8) are `2X/2^s-c_s` and
`2X/2^s-c_(s-1)`. If their counts differ, the interval between them contains
some canonical integer q with1<=q<=N, with the lower endpoint excluded.
Since both c's are positive and at most1, this forces

```
2X/(N+1) < 2^s < 2X.                                 (10)
```

Let L=floor(log2 N). The ratio between the endpoints in (10) is N+1,
which is at most2^(L+1). An open interval with this ratio contains at most
L+1 distinct powers of2. Therefore

```
|B_N(X)-K(N)| <= L+1.                                 (11)
```

The normal-form count theorem gives

```
|K(N)-N/4| <= floor(log2(N+1))+1/2 <= L+3/2.
```

Combining this with (11) proves the explicit, uniform bound

```
|B_N(X)-N/4| <= 2*floor(log2 N)+3,
for every integer X>=N>=8.                            (12)
```

The extra half unit in this displayed bound is harmless rounding. The
argument establishes O(log N), stronger than separately replacing each
level count by its density, which would only yield O(log^2 N).
`telescope_count` implements (8), checks the active range (10), and returns
all nonzero signed corrections for inspection.

### 4. Interpretation and limits

There are ceil(X/2) odd integers in the integer band [X,2X). Equations
(11)-(12) therefore imply the uniform counting proportion

```
B_N(X)/ceil(X/2)=N/(2X)+O(log N/X).                    (13)
```

At X=HN this has leading term1/(2H). This is the density of the explicitly
certified elementary closure in a band, conditional on the supplied lower
current. It describes actual integer membership. It is not an independent
trial probability for an orbit, a proof that every orbit hits I_N, or an
iteration rule for the complementary residual. It also does not describe
the different set obtained by taking a finite forward union of known seeds.

For each fixed N, the set I_N even has bounded absorption times once the
finite input is supplied. In a component C_q with q>1, the F identities
preserve hitting time, and the selected-partner R23 identity compares two
equal-length prefixes neither of which reaches1 early. All its members
therefore have the same hitting time as q. Every member of C_1 reaches1
within two steps. The bound is the maximum of2 and the finitely many known
canonical hitting times through N. This strengthens the individual
certificate interpretation; it supplies no information about a seed outside
I_N entering that set.

### 5. Reproduction and finite evidence

Run from the repository root:

```
python3 experiments/residual_progress/absorbed_fibers/check_fibers.py
```

The default run is read-only and compares against `fiber_audit.json`.
`--write-receipt` regenerates that receipt. The checks compare three exact
counts: direct band membership for small bands, the level formula, and the
telescope. A fourth independent calculation enumerates canonical bases and
locates the first F-power in the band, without scanning very high intervals.

The receipt covers912 small bands,42 additional boundary bands at odd
cutoffs,18 high bands with multipliers through2^512, and56 actual conditional
current conversions, including F-exponents
128. Supplied absorption through96 is discovered solely for these finite
tests, with a1000-step cap per seed; it is an input assumption in the theorem.
No universal absorption search, orbit-hitting heuristic, or convergence
claim is used.

## Certificates

- [`fibre_count_check.py`](fibre_count_check.py) (side-lane probe, about 10 s, standard library, fixed seed; it checks by `assert` and refuses to run under `-O`). It rebuilds `ν` by descent and checks the count bound (12) by brute force for `X` up to `N·2^14` and by the component count up to `X = N·2^512`, for `N ∈ {8, 13, 64, 100, 257, 1000}`. It rewrites [`fibre_count_check.json`](fibre_count_check.json) on every run; the run at the migration reproduced it byte for byte. Passed at `be73a66` as `reviews/side_lane/fibre_count_check.py` (archive/legacy-checker-run-be73a66.md, exit 0).
- The legacy main-lane checker was evidence only until the B18 replay revival (below) (see `evidence`). The command in the legacy text names `experiments/residual_progress/absorbed_fibers/`.

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B18-replay-revival migration; standard library) replays the unmodified legacy check `check_fibers.py` in a temporary copy of the legacy layout built by `tools/legacy_replay.py`, requiring exit 0 and every file unchanged (about 14 s). It checks finite steps only; the status is unchanged.

## Remarks

- **Relation to the side lane's merge heuristics.** The side lane's earlier claim that all merge-type certificates share one `c/H²` density law was withdrawn on 2026-10-17 20:22 because `I_N` has density about `1/(2H)` at height `HN` ([`cylinder-certificates-outer-residual`](../../attempts/cylinder-certificates-outer-residual/README.md)); the scope of finite forward-union experiments is discussed in [`prefix-rule-cylinder-rate-barrier`](../prefix-rule-cylinder-rate-barrier/README.md) §7.
- **Use.** [`supplied-path-saturation-core`](../supplied-path-saturation-core/README.md) closes `I_N` further under supplied forward arrows; [`merger-catalogue-scope`](../merger-catalogue-scope/README.md) compares it with the forward union `F_N`.
- No novelty is claimed.

## History

- Migrated from `experiments/residual_progress/absorbed_fibers/ABSORBED_FIBERS.md` (legacy ID R27) at commit `be73a66`, by the B10 migration (Claude, Opus 5.5). Note, scripts and receipt moved byte-identical, with the side-lane probe `reviews/side_lane/fibre_count_check.*`, which passes at its new path and is the certificate. Legacy status: "written counting theorem and conditional finite certificates".
- Main lane (ChatGPT, Codex), 2026-10-17, from commit `541101a`. The batch report (archive/convergence-residual-progress/REPORT.md) records "independent model" proof and code audits for this batch; they were the main lane's own agents, so they do not count as an independent review. The side lane first numbered the halving bridge R27 in its feed and corrected it to R23 on 2026-10-18; this node is main's R27.
- 2026-10-31: reviewed by the Claude review lane (Fable 5.1; directed by Santiago Armstrong); status raised to reviewed. No correction; the review notes that `fibre_count_check.py` checks by `assert` only and rewrites its receipt on every run, that the hypothesis `N >= 8` is not used by the proof, and supplies the missing short argument for "neither of which reaches 1 early" in section 4. See [`REVIEW-2026-10-31-claude-review-lane.md`](REVIEW-2026-10-31-claude-review-lane.md).
