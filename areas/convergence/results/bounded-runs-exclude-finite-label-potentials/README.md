---
id: bounded-runs-exclude-finite-label-potentials
kind: result
title: Repeating the eight-step word (1,2,1,1,1,1,2,2) gives arbitrarily many increasing run returns with two fixed labels, so no finite-label height potential decreases at every return
status: written
claim: >
  Odd-only 3x+1 map S; nu, T of elementary-bridge-quotient-normal-form and the normalised run return f_star of
  complementary-run-bridges. (Clock) For complementary x with run parameters (a, t, d, w), f_star(x) = T^k(x) with
  k = a + floor(d/2) - 1. (Repeated runs) For every r >= 1, every positive x = c_r mod 2^(11r+6), where
  c_r = -9221 4513^(-1) mod 2^(11r+6), has its first 8r odd steps in r repetitions of the valuation word
  (1,2,1,1,1,1,2,2); all states are canonical, every noninitial state stays above x, and its first 2r normalised
  run returns alternate labels (a, d) = (2,2), (5,4) and strictly increase (pair map Psi(x) = (6561x + 9221)/2048).
  For every r and every b >= 11r+6 there is an actual coefficient-1 complementary root x of R'_N, N = 12 2^b, with
  this behaviour, all 8r states above N, unresolved by the run bridges. (Obstruction) No potential
  V(x) = G(label(x), x) with a finite label set and G nondecreasing in x within each label strictly decreases at
  every f_star transition on all complementary states. Scoped: unbounded arithmetic state, nonmonotone potentials,
  progress arguments allowing increases or plateaus, and mergers into supplied paths are not excluded. The seed
  varies with the requested length; no positive integer is proved to grow forever, and no counterexample is claimed.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [elementary-bridge-quotient-normal-form, complementary-run-bridges]
certificates: [check_bounded_runs_recompute.py]
evidence:
  - "check_bounded_runs.py, bounded_runs.py, bounded_runs_audit.json: the legacy constructor and checker (the affine table, 57 parameter cylinders through 128 repetitions, 21 required-ray examples, six finite-modulus label repetitions, every valuation, canonical phase, return and finite-current divergence). Fails at its new path: bounded_runs.py loads ../bridge_normal_form/normal_form.py (now ../elementary-bridge-quotient-normal-form/) and ../complementary_bridge/run_bridge.py (now ../complementary-run-bridges/) by their pre-migration paths. Passed at be73a66 as experiments/residual_progress/bounded_run_cycles/check_bounded_runs.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran these steps before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a). The later odd-h-pair-interface-compiler loads bounded_runs.py by its old path"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-17
    link: ../shrinking-paired-return-recursion/batch_64fff1d_check.py
    scope: "Finite only (side-lane feed entry 2026-10-17 20:44, VERIFIED, main 64fff1d; the R31 part): 4513 27 + 9221 = 2^17; 4513 Psi(x) + 9221 = (6561/2048)(4513x + 9221); x = -9221/4513 mod 2^(11r+6) forces r complete words (1,2,1,1,1,1,2,2), checked by direct steps for r = 1..6. The written theorem and the potential obstruction were not re-derived; the status stays written"
aliases: [R31]
tags: [convergence, outer-residual, run-bridges, potentials, obstruction, valuation-words]
---

# Repeating the eight-step word (1,2,1,1,1,1,2,2) gives arbitrarily many increasing run returns with two fixed labels, so no finite-label height potential decreases at every return

## Statement

Odd-only clock; `ν`, `T` from [`elementary-bridge-quotient-normal-form`](../elementary-bridge-quotient-normal-form/README.md) and the normalised run return `f_★` from [`complementary-run-bridges`](../complementary-run-bridges/README.md).

1. **Exact clock.** For complementary `x` with run parameters `(a, t, d, w)`, `f_★(x) = T^k(x)`, `k = a + ⌊d/2⌋ − 1 ≥ 2`.
2. **One growing pair.** For every positive `x ≡ 27 (mod 2^17)` the first eight valuations are `(1, 2, 1, 1, 1, 1, 2, 2)`, all states are canonical and above `x`, and the two run returns (labels `(2,2)`, `(5,4)`) give `f_★(x) = (9x + 5)/8 > x` and `f_★²(x) = Ψ(x) = (6561x + 9221)/2048 > f_★(x)`.
3. **Repeated runs.** For `r ≥ 1`, `K_r = 11r + 6` and `c_r ≡ −9221·4513^(−1) (mod 2^(K_r))`, every positive `x ≡ c_r (mod 2^(K_r))` has `r` repetitions of the word in its first `8r` steps, all states canonical, every noninitial prefix above `x`, and `2r` strictly increasing returns with labels alternating `(2,2)`, `(5,4)`; all `a ≤ 5`, `d ≤ 4`, valuations 1 or 2. (The negative rational fixed point `−9221/4513` is modular notation only, not an orbit or a negative cycle.)
4. **Actual roots.** For every `r` and every `b ≥ K_r`, `N = 12·2^b` has a coefficient-1 complementary root `x ≡ 3 (mod 12)` in `(N, 5N/4]` with this behaviour; its `8r` ordinary states stay canonical and above `N`, so it never enters `{y : ν(y) ≤ N}` during that prefix and the run bridges leave it unresolved. Supplied-path saturation may still certify some of these roots.
5. **Obstruction.** No potential `V(x) = G(label(x), x)`, with labels in a fixed finite set and `G` nondecreasing in `x` within each label, strictly decreases at every `f_★` transition on all complementary states. This covers a label rank followed by height and residue-dependent multiples of height; it does not cover unbounded arithmetic state, nonmonotone potentials, arguments allowing increases or plateaus, or mergers into supplied paths.

The seed varies with the requested length: no positive integer is proved to grow forever, and no counterexample or novelty is claimed.

## Proof

The legacy note "Arbitrarily long growth with two fixed run labels" follows, lightly edited (headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

2026-10-17. **Written finite-cylinder theorem and scoped potential obstruction.**
The seed varies with the requested length. No positive integer is proved
to grow forever, and no Collatz counterexample or novelty is claimed.

Use the odd-only map S, canonical normalization nu and quotient T from
[R25](../elementary-bridge-quotient-normal-form/README.md), and normalized run return
f_star from [R26](../complementary-run-bridges/README.md).

### 1. An exact variable clock for the run map

For a complementary seed x with R26 parameters(a,t,d,w), put
`k(x)=a+floor(d/2)-1>=2`. Then **f_star(x)=T^k(x)**.
For even d, the raw return is S^k(x). For odd d, the last state before
the common-successor comparison is F(f(x)) at the same time k.
Applying nu gives the claim, since nu F=nu and T^k nu=nu S^k.
This exact positive clock accelerates the quotient; it does not prove
that iteration terminates.

### 2. One growing pair of run returns

Consider the eight valuations

```
v=(1,2,1,1,1,1,2,2).
```

At x=27 the actual states are

```
27,41,31,47,71,107,161,121,91.
```

All are canonical. The first run return has label(a,d)=(2,2) and ends
at31 after two steps; the second has label(5,4) and ends at91 after
six more steps. No normalization changes these endpoints.

For every positive x=27 modulo2^17 the same valuations and canonical
phases hold. Its affine prefixes are S^j(x)=(3^j*x+C_j)/2^A_j:

| j | total valuation A_j | numerator3^j | offset C_j |
|---:|---:|---:|---:|
|1|1|3|1|
|2|3|9|5|
|3|4|27|23|
|4|5|81|85|
|5|6|243|287|
|6|7|729|925|
|7|9|2187|2903|
|8|11|6561|9221|

The recurrence `C_(j+1)=3C_j+2^A_j` derives every row. Replacing27
by27+2^17h changes prefix j by `3^j*2^(17-A_j)h`. These congruences
preserve every displayed exact valuation and canonical class.
In particular the middle state is31 modulo2^14, fixing its a=5,d=4;
the last state is91 modulo64, a complementary class with a=2,d=2.

Every prefix has3^j>2^A_j and C_j>0, so every noninitial state stays
above the pair's starting seed. Both run returns strictly increase:

```
f_star(x)=(9x+5)/8 > x,
f_star^2(x)=Psi(x)=(6561x+9221)/2048 > f_star(x).
```

The second inequality also follows from the middle-class formula
`f_star(y)=(729y+697)/256`. Individual valuation2 steps may decrease
from their immediate predecessors; every state stays above the pair's start.

### 3. Arbitrarily many repetitions with bounded parameters

Write `x_*=-9221/4513`, where4513=6561-2048. Its odd denominator
defines a unique residue modulo every power of2. This is notation for
a modular inverse: the negative rational fixed point of the affine word
is neither a positive integer orbit nor a negative-integer Collatz cycle.

For each integer r>=1 set

```
K_r=11r+6,
c_r=-9221*4513^(-1) modulo2^K_r,       0<c_r<2^K_r.
```

**Repeated-run theorem.** Every positive x=c_r modulo2^K_r has its
first8r ordinary steps in r repetitions of v. All states are canonical.
Its first2r normalized run returns alternate labels(2,2),(5,4) and
strictly increase at each return. Every noninitial ordinary prefix
remains above x.

**Proof.** The exact identities

```
4513*27+9221=2^17,
4513*Psi(x)+9221=(6561/2048)*(4513x+9221)
```

give `v2(4513*Psi^i(x)+9221)>=K_r-11i`. For i<=r-1 this is at
least17, so the next pair begins at27 modulo2^17 and Section2 applies.
That section also proves the next iterate is integral; the induction
does not assume an undefined rational iterate. Each pair starts higher
than its predecessor, and every within-pair prefix exceeds its start.
The final state is27 modulo64 and is canonical. This proves the theorem.

Throughout these returns a<=5,d<=4, and every ordinary valuation is1
or2. Thus a bound on the number of returns before descent cannot depend
only on the maximum run labels. Adaptive depth depending on the full seed
and other arithmetic information remains possible. No single positive
integer is claimed to realize all lengths.

### 4. Actual unresolved roots on the required rays

Let P_r=3*2^K_r. Choose the CRT residue e_r modulo P_r with
`e_r=c_r modulo2^K_r` and `e_r=0 modulo3`.
For every b>=K_r put N=12*2^b and choose the first x=e_r modulo P_r
strictly above N. Then

```
N<x<=N+P_r<=5N/4<3N/2,       x=3 modulo12.
```

This is a coefficient1 root of R_N, complementary with label(2,2),
hence in R'_N. Its first normalized return exceeds x>N, so R26 leaves
it unresolved. Its next2r-1 returns and all8r ordinary prefixes remain
canonical and above N. None enters the cutoff-only elementary known set
`{y:nu(y)<=N}` during that prefix. For every r this gives infinitely
many cutoffs on the required ray, with b>=9. Larger supplied-path
saturation can still certify some of these roots; it is not excluded.

### 5. No finite-label height potential decreases at every return

Suppose each complementary state receives a label in a fixed finite set L.
It may include any fixed binary or ternary residues and the bounded run
parameters, or be any other finite classification. Consider a potential
`V(x)=G(label(x),x)` in an ordered set, where for each fixed label ell,
G(ell,x) is nondecreasing in x on its domain.

No such potential strictly decreases at every f_star transition on all
complementary states. Choose r with2r>|L| and take the theorem's2r
consecutive starting states. They strictly increase in height. Two have
the same label; monotonicity makes the later potential at least the earlier
one, while strict decrease along the intervening returns makes it smaller.
This is a contradiction.

This includes a finite label rank followed lexicographically by height,
and positive residue-dependent multiples of height. The obstruction is
scoped to stepwise decrease for this return map and monotonicity in height
within each label. It permits unbounded arithmetic state, nonmonotone
potentials, finite-progress arguments allowing increases or plateaus, and
additional mergers into supplied known paths.

### 6. Reproduction

```
python3 experiments/residual_progress/bounded_run_cycles/check_bounded_runs.py
```

The default compares with `bounded_runs_audit.json`; `--write-receipt`
regenerates it. The checker derives the affine table independently and
checks57 parameter cylinders through128 repetitions,21 required-ray
examples and six finite-modulus label repetitions. Every ordinary
valuation, canonical phase, exact return and finite-current divergence
is checked. There is no unbounded orbit search or absorption assumption.
The universal claims rest on the proofs above.

## Certificates

- [`check_bounded_runs_recompute.py`](check_bounded_runs_recompute.py) (written at the B10 migration, under 1 s, standard library). With its own Syracuse step, canonical test, `ν` and `f_★` it checks, against [`bounded_runs_audit.json`](bounded_runs_audit.json): the affine prefix table of the word, `3^j > 2^(A_j)` on every row, `4513·27 + 9221 = 2^17` and the `Ψ` identity as an exact rational identity; the 57 cylinder samples (`r = 1, …, 16, 32, 64, 128`; offsets 0, 1, 7), with the word, canonical states, alternating labels, increasing returns, `Ψ` endpoints and the receipt's bit lengths, row counts and SHA-256 hashes; the 21 required-ray witnesses; and the six finite-modulus label repetitions. It does not rerun the legacy constructor or its current bookkeeping (legacy checker, evidence only).
- The command in the legacy text names `experiments/residual_progress/bounded_run_cycles/`.

## Remarks

- **Area.** The legacy folder was called `bounded_run_cycles`, but the "cycles" are repeated valuation words along growing prefixes, not periodic orbits; the node belongs to convergence, not to the cycles area.
- It sharpens the two-transition label obstruction (`27 → 31 → 91`) of [`complementary-run-bridges`](../complementary-run-bridges/README.md) §6 to every finite label set. The odd-`h` interface of [`odd-h-pair-interface-compiler`](../odd-h-pair-interface-compiler/README.md) reuses the repeated word on `x ≡ 10 (mod 27)` to exclude a bounded test.
- Whether the normalised quotient terminates is [`normalised-quotient-termination`](../../questions/normalised-quotient-termination.md); this node shows what a terminating potential cannot look like.
- No novelty is claimed.

## History

- Migrated from `experiments/residual_progress/bounded_run_cycles/BOUNDED_RUN_GROWTH.md` (legacy ID R31) at commit `be73a66`, by the B10 migration (Claude, Opus 5.5). Note, scripts and receipt moved byte-identical; `check_bounded_runs_recompute.py` was added at the migration. Legacy status: "written finite-cylinder theorem and scoped obstruction; no divergent positive orbit is exhibited".
- Main lane (ChatGPT, Codex), 2026-10-17, from commit `64fff1d`. The batch report (archive/convergence-residual-progress/REPORT.md) records "independent model" proof and code audits for this batch; they were the main lane's own agents, so they do not count as an independent review. The side lane's finite check is recorded under `reviewed_by`.
