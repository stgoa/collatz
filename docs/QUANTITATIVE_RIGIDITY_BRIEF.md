# Goal — Quantify the complexity of a hypothetical Collatz obstruction

**Activated 2026-10-18; active and unresolved.** This records the accepted
objective below. V004's finite-state classification is complete. The new
goal has a stronger completion requirement.

Prove that any nonconstant finite-valued Collatz invariant requires binary-section complexity exceeding every linear bound.

The completed theorem excludes finite-state descriptions. Seek a quantitative strengthening that also excludes descriptions whose complexity grows only linearly with binary depth.

Compare a few bounded mechanisms before deepening. Preserve exact hypotheses, controls and failed approaches. Do not assume that the actual nonabsorbing set has any regularity.

Success requires a proved complexity bound beyond what follows merely from having an infinite kernel.

## Exact target and conventions

Let h take values in a finite set on the positive integers, with

```
h(2n)=h(n)       for n>=1,
h(3n+1)=h(n)     for positive odd n>1.
```

Retain absorber1 and set h(0)=h(1) for the section convention. Define

```
K_D(h)={n -> h(2^a*n+r):0<=a<=D,0<=r<2^a}, n>=0,
kappa_h(D)=|K_D(h)|.
```

The members counted are entire functions, not finite prefixes. The goal is

```
h nonconstant => sup_(D>=0) kappa_h(D)/(D+1)=infinity.
```

Equivalently, for every finite C there is a D with
`kappa_h(D)>C*(D+1)`. This does not silently strengthen the request to
convergence of the ratio to infinity at every sufficiently large depth.
The generic infinite-kernel bound `kappa_h(D)>=D+1` is already available
from V004 and a no-plateau argument; it does not complete this goal.

## First batch

[V005](../experiments/viewpoints/V005/REPORT.md) compares direct section
reconstruction, graph growth, and quantitative two-base mechanisms. Written
local consequences and rejected shortcuts are progress only. The goal
remains active until the full unbounded-ratio statement is proved and
verified at its actual quantifier scope.

## Second batch

[V006](../experiments/viewpoints/V006/REPORT.md) proves quadratic growth
if an invariant has one positive section of digit-count type. It also
shows that weaker binary graph assumptions do not supply that section.
The next overlap test retains all radix identities and the three root
relations. The full all-invariant target above is unchanged and unresolved.
