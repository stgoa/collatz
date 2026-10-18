# V001 — Tiny Dirichlet-domain discrimination probe

**Status: elementary worked comparison, not a new convergence result.**
2026-10-18. This is the single bounded follow-up to candidate C in
[operators_geometry.md](operators_geometry.md). No large truncation,
orbit search, or numerical extrapolation was used.

## 1. Exact model and boundary convention

The vertices are all positive odd integers. For each \(n>1\), join
\(n\) to \(S_d(n)\) with conductance \(1/n\). Parallel edges add;
self-loops may be omitted for hitting probabilities. There is no outgoing
arrow from the designated absorber 1. Every inverse neighbor is an actual
positive odd integer of exact valuation; no symbolic branch is added.

The conductance incident to a fixed vertex is finite: possible inverse
sources have the form \((2^a y-d)/3\) and eventually grow geometrically.
Normalize incident conductances to obtain an **auxiliary undirected walk**.
It has its own time clock. It is not the deterministic Syracuse process.

For finite \(F\ni1\), set

\[
u_F(n)=\Pr_n(T_1<T_{F^c}),\qquad u_F(1)=1,
\qquad u_F(n)=0\quad(n\notin F).
\]

Every edge leaving \(F\) leads to an escape boundary held at zero.
Its conductance stays in the harmonic equations. The outside vertices may
be collapsed into one zero-boundary vertex for this calculation; they must
not be identified with 1. If an interior component meets neither boundary,
the hitting probability selects zero there; an arbitrary harmonic constant
is not a permissible substitute.

The standard voltage/hitting-probability correspondence and energy
principle are described in [Doyle–Snell, Sections 1.3–1.4](https://math.dartmouth.edu/~doyle/docs/walkspdf/walks.pdf)
and [Lyons–Peres, Chapter 2](https://rdlyons.pages.iu.edu/prbtree/).
The examples and deterministic comparison below are direct derivations.

## 2. Ordinary map: the path 3 → 5 → 1

Take \(d=1\) and \(F=\{1,3,5\}\). Its internal conductances are
\(c_{3,5}=1/3\) and \(c_{5,1}=1/5\). Vertex 3 has no inverse
neighbors because \(3n+1=3\cdot2^a\) is impossible modulo 3.

Every inverse neighbor of 5 is exactly

\[
x_j=\frac{10\cdot4^j-1}{3},\qquad j\ge0.
\]

Here \(x_0=3\) is internal; \(13,53,213,\ldots\) are escape
neighbors. The exact total escape conductance is the convergent series

\[
T=\sum_{j\ge1}\frac{3}{10\cdot4^j-1}.
\]

This is an exact specification, not a truncated rational value. The two
harmonic equations reduce to

\[
u_F(3)=u_F(5),\qquad
\left(\frac15+\frac13+T\right)u_F(5)
=\frac15+\frac13u_F(3).
\]

Consequently

\[
u_F(3)=u_F(5)=\frac1{1+5T}.
\]

Since \(x_j\ge3\cdot4^j\), and the first escape source is 13,

\[
\frac1{13}\le T\le\sum_{j\ge1}\frac1{3\cdot4^j}=\frac19,
\qquad
\frac9{14}\le u_F(3)=u_F(5)\le\frac{13}{18}.
\]

Thus a fully rational finite comparison network uses the same two internal
edges and one edge from 5 to escape of conductance \(1/9\), obtaining
the rigorous lower voltage \(9/14\). Using only the actual escape edge
of conductance \(1/13\) instead gives the upper comparison \(13/18\).
Deleting the entire escape boundary gives 1, an incorrect value for this
Dirichlet problem. Both deterministic seeds nevertheless absorb: their
absorption indicators are exactly 1. The auxiliary voltage loses useful
mass even in this smallest known example.

For comparison, the smaller domain \(\{1,5\}\) also treats 3 as
escape and has voltage
\((1/5)/(1/5+1/3+T)\). Adding 3 strictly improves the bound. This is
a valid domain-monotonicity observation, not evidence of a uniform
large-domain rate.

## 3. Cycle control: d = 5

Take \(F=\{1,19,31,49\}\). The exact internal arrows and valuations
are

\[
19\xrightarrow{1}31\xrightarrow{1}49\xrightarrow{3}19,
\]

with undirected conductances \(1/19,1/31,1/49\), respectively.
There is no internal edge to 1. Positive escape conductances are already
witnessed by

\[
11\xrightarrow{1}19,\qquad81\xrightarrow{3}31,
\qquad129\xrightarrow{3}49.
\]

Their conductances are exactly \(1/11,1/81,1/129\). All additional
inverse edges also end at the zero escape boundary. Let their full totals
at the cycle vertices be \(T_{19},T_{31},T_{49}>0\). Summing the three
harmonic equations cancels every internal edge and gives

\[
T_{19}u_F(19)+T_{31}u_F(31)+T_{49}u_F(49)=0.
\]

Nonnegativity forces all three voltages to zero. The same conclusion holds
in the finite rational comparison retaining just the three displayed
escape edges. Omitting the escapes would leave an isolated harmonic cycle
with arbitrary constant solutions; interpreting a positive such constant
as absorption would be a boundary-condition error.

## 4. What the language adds, and what it does not

For this positive-conductance graph,

\[
u_F(n)>0
\quad\Longleftrightarrow\quad
\text{an undirected path inside }F\text{ joins }n\text{ to }1.
\]

In a functional graph with absorber 1, its component has a unique forward
path from each vertex to 1. Therefore the displayed condition is exactly
that this actual forward path is contained in \(F\). This is the finite
component certificate already present in R7; potential theory has not
supplied new membership information.

There is also a clock-safe inequality. If the auxiliary walk reaches 1
within \(h\) walk steps, loop erasure leaves a simple path of length at
most \(h\). That is the deterministic forward path. Thus

\[
\Pr_n(T_1\le h,\ T_1<T_{F^c})
\le1_{\{\tau_1(n)\le h\}}.
\]

The two clocks have not been equated; the inequality follows from path
length. Conversely, a short deterministic path need not have large
auxiliary probability, as Section 2 illustrates.

For a **fixed** finite \(F\),
\(\sum_{n\le X}u_F(n)/n\) stays bounded, so its relative logarithmic
average tends to zero. A density milestone needs growing domains \(F_X\)
and an all-cutoff estimate, with every escape term retained. That estimate
is currently absent. Trial functions of low energy alone do not give a
pointwise lower voltage: a lower comparison needs a valid subharmonic
inequality with the correct boundary values, or an explicit error bound.

## 5. Discrimination decision

**Keep as a secondary analytical possibility; no advantage established.**
The reversible setting offers energy methods that a directed trajectory
does not directly possess. The present probe, however, only repackages
known component membership and penalizes it through escape probabilities.
Choosing domains using presumed absorbing membership would be circular;
proving that membership by enumerating all paths first would remove the
claimed analytical benefit.

Compared with a guarded-cocycle or sound-abstraction programme, this probe
does not justify preferring potential theory. The latter would need a
uniform arithmetic boundary/energy inequality giving a new quantitative
average. The former would need a proved refinement or composition rule
that genuinely reduces unresolved integer states. Each earns priority
only by such an estimate, not by the sophistication of its vocabulary.
