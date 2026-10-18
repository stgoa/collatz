# Linear predecessor density: P6-004

**Nodes: C.1a and C.2a. Programme label: none. Collatz remains open.**

This batch separates an external theorem audit, a written mathematical
reconstruction conditional on Tao's mixing theorem, and an unsuccessful
upper-bound attempt. The isolated source build, exact statement/axiom audit,
and fresh replay into an empty instance of the same Lean kernel all passed.
The [completed replay record](formal_replay.json) pins the actual evidence
and its trust boundary. This is not a second kernel implementation or a
fresh source rebuild of every cached dependency.

## What the audited lower bound supplies

The exact formal statement under audit, at the pinned source in
[lau_scope.md](lau_scope.md), includes the following consequence. Put

\[
 L=2^{2^{2^{87640}}},\qquad
 c(a)=\frac{1}{a^4L},\qquad X_0(a)=2^{a^3L}.
\]

For each positive odd target \(a\) with \(3\nmid a\), and **every**
integer \(X\ge X_0(a)\), at least \(c(a)X\) distinct odd integers
\(n<X\) reach \(a\). The source also supplies two explicit logarithmic
clocks. Neither target convergence nor target nonperiodicity is a premise.

Here is the complete implication to our remaining node. Let \(B\) be the
positive odd nonabsorbing set and let
\(\widetilde B=\{n\ge1:\operatorname{oddpart}(n)\in B\}\). If
\(m\in B\), then \(a=S(m)>1\) is odd, not divisible by 3, and also
belongs to \(B\). Every odd predecessor of \(a\) is bad: the raw odd
map fixes 1, so such a path cannot pass through 1 before reaching \(a\).
Consequently, conditional on the displayed lower theorem,

\[
 \#(\widetilde B\cap[1,X))\ge c(a)X
 \quad\text{for every integer }X\ge X_0(a).
\]

For every finite odd-arrow horizon \(H\), these seeds are contained in
\(\{1\le n<X:\tau_1(\operatorname{oddpart}(n))>H\}\). Taking
\(\epsilon=c(a)/2\) and \(M=X_0(a)\) contradicts C.2a, which requires
some finite \(X\ge M,H\ge0\) with late count at most \(\epsilon X\).
Conversely, Collatz gives a finite maximum hitting time at each finite
cutoff and therefore implies C.2a. The lower theorem thus makes C.2a
an exact remaining convergence obligation. It does not establish that upper
condition.

## Written results and unsuccessful attempt

| Artifact | Status and scope |
|---|---|
| [audit_notes.md](audit_notes.md) | Arithmetic proof of a seed-uniform residue histogram, retaining multiplicities and residue endpoint errors; summable variation conditional on Tao's mixing estimate. |
| [terminal_audit.md](terminal_audit.md) | Conditional qualitative lower-density reconstruction: endpoint-dependent terminal shifts, separate transport and removal errors, every sufficiently large scale, and distinct integer sources. |
| [transfer_scope.md](transfer_scope.md) | Corrected Tao v7 normalization and qualitative extension to each fixed positive d coprime to 6, for targets not divisible by 3. This is not a transfer of Lau's numerical constants. |
| [c2a_attempt.md](c2a_attempt.md) | Exact inverse invariance through two ternary source levels. Its stated leading-coefficient relaxation admits a positive-density mode and does not prove the proposed actual-B contraction. Outcome none. |
| [next_upper_attempt.md](next_upper_attempt.md) | Preparation for a matched density-gap test. The required inequality is missing; a countermodel scopes what the aggregate inputs alone can imply. |
| [lau_scope.md](lau_scope.md) | Public-statement, source and dependency audit of the pinned formal development. It distinguishes the accessible formal challenge from the inaccessible full article. |
| [replay_notes.md](replay_notes.md) | Replay preparation and trust boundaries; author reports and cached dependencies are distinguished from actual checks. |

The handwritten derivation has explicit bounds in terms of Tao's
unspecified mixing constants. It does not independently derive Lau's
numerical Fourier/renewal estimates or enormous tower recipe. Independently
replaying that supplied formal derivation is useful verification, but we do
not relabel it as our own explicit-constant mathematical rederivation.
Under the programme's current wording, the batch label is **none**. Side
confirmation remains separate.

## Reproduce the arithmetic checks

```sh
python3 experiments/phase6/linear_density_audit/check_audit.py
python3 scripts/verify_all.py --cpp --transfer-controls
```

The arithmetic receipt [audit_checks.json](audit_checks.json) records finite
tests of the written ingredients. It neither checks an infinite orbit nor
runs Lean. The separate [formal runner](run_formal_replay.py) operates only
on prepared, pinned sources and a reviewed execution environment; see its
help and replay notes. The [statement generator](generate_statement_audit.py)
copies the pinned challenge definitions and types into a distinct namespace
without importing its proof placeholders.

No frozen result, dispatcher or open LaTeX source is changed by this batch.
