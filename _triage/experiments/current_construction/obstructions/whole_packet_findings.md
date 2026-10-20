# Historical cancellation on whole right-packet measures

Finite certificate results, 17 October 2026. These experiments do not prove
universal existence, a uniform exposure depth, or Collatz convergence.

The constructor exposes at most `d` steps from **every nonzero source atom**
of `Pi_right_N`, joins historical intersections, and tests the total signed
source mass in each finite component. A component containing 1 is resolved;
all other components must have mass zero for an exact current, or mass at
most zero for a nonpositive-residual current. The method and its completeness
in the unbounded-depth limit are proved in `functional_graph_currents.md`.

The distinction between cancellation and compressed halting verification is
visible in the data. At all the sampled earlier 30-ray cutoffs, and at
65536 (also on the final five-ray grid), the exposed graph at exact success already links every
source to 1. Historical search discovers the shared paths earlier than equal
time iteration, but those particular successes still establish halting of
every supported source. They do not demonstrate cancellation of unresolved
futures.

At the deliberately chosen nongrid cutoff **2053**, the exact current is
found while **27 sources have no path to 1 in the exposed graph**. They occupy
two components of mass zero, containing 18 and 9 sources. Their futures cancel
without being followed to the absorber. The one-sided certificate stops even
earlier, with 32 sources unlinked to 1 across six components whose masses are
`0,0,-2,-1,-1,-1`. Thus the implementation really can use the signed-current
mechanism rather than merely requiring all supported seeds to halt.

| Cutoff N | Historical exact depth | Historical one-sided depth | Synchronous exact depth |
|---:|---:|---:|---:|
| 120 | 12 | 12 | 44 |
| 236 | 12 | 8 | 51 |
| 480 | 50 | 13 | 61 |
| 517 | 50 | 15 | 61 |
| 1984 | 31 | 28 | 78 |
| 2053 | 26 | 17 | 78 |
| 3008 | 43 | 30 | 86 |
| 8197 | 45 | 44 | 97 |
| 15104 | 44 | 37 | 101 |
| 65536 | 72 | 72 | 128 |

Depth means the maximum exposed prefix length from each original source;
it is not a current-row count, a wall-clock measure, or the length of paths
assembled by joining prefixes. The receipt separately records current size,
positive cost, residual mass, and every unresolved component's source states.
In all samples, synchronous extinction occurs at the largest individual
source hitting time, independently checked with a finite cap.

For example, at 2053 the exact current has 1,636 nonzero rows and positive
current cost 1,887. Its one-sided counterpart has 1,532 rows, positive cost
1,950, and four residual atoms with total mass -5. Earlier stopping and fewer
rows do not automatically mean smaller positive cost. The one-sided table and
residual are persisted as `one_sided_2053.csv` and
`one_sided_residual_2053.csv`.

At 65536, both searches first succeed at depth 72 and yield the same exact
current: 53,621 rows, positive cost 74,725, and zero residual. The stored table
is `exact_65536.csv`; `exact_residual_65536.csv` is an empty table with its
header. This is a certificate for the revised family at one cutoff, separate
from the inherited archive's other packet family.

Every sampled exact historical current agrees coefficient by coefficient with
the full synchronous current. This is expected after the separate finite
check that the sources terminate: finite currents on an absorbing functional
component are unique. For completeness, if a finite signed current has zero
divergence, each state with nonzero outgoing weight must have at least one
predecessor with nonzero weight. Following such predecessors inside the finite
support forces a cycle. A deterministic cycle cannot have a forward path
leaving it, so the original state itself must lie on that cycle. Thus all
nonzero support lies on directed cycles, and conservation makes the weight
constant around each cycle. The kernel consists of finite cycle circulations.
An absorbing component, with its
absorber's outgoing edge excluded, has no such cycles. Unknown disjoint
nonabsorbing cycles could supply irrelevant additional circulations in the
general graph; they play no role in these constructed tables.

## What remains worth testing or proving

A **uniform aggregate exposure depth D** could still be a candidate: expose
`D` steps from every source atom in the whole packet, then show each component
not linked to 1 has nonpositive source mass. The bounded-size obstruction for
individual triples does not rule this out, because the aggregate construction
uses many more atoms and allows cancellations between triples. A uniform
aggregate depth bound would be a strong theorem implying the universal current
criterion; none is established here. Depths at most 71 already fail at 65536
for this specific exposure rule, in both certificate modes. The sample is too
small to infer eventual boundedness or growth.

A more flexible next obligation is a recursive arithmetic proof controlling
the signed mass of exposed components, with depth depending on the cutoff.
The useful output to explain is why unresolved components always have
nonpositive mass, or why a positive component must eventually merge or reach
an already verified component. If the argument instead shows that all sources
enter a known halting interval, it should explicitly be described as a descent
proof; presenting it as current cancellation would hide the true obligation.

The final five-ray reduction narrows the cutoffs at which that obligation is needed.
`sparse_ray_independent_audit.md` independently checks its maximum-principle
argument and exact rational constants. Existence at infinitely many ray
cutoffs remains unproved.

## Actual verification and limits

Run `python3 experiments/current_construction/obstructions/whole_packet_demo.py`.
The script reconstructs each full packet, checks each divergence exactly,
compares exact currents with synchronous currents, reproduces the receipt,
and checks persisted tables. No inherited snapshot files are modified.
The finite caps are historical depth 96, synchronous depth 512, and 1,000
odd-only steps per source for the separate hitting-time comparison. Unresolved
searches are represented explicitly; all ten listed inputs succeeded within
these caps. The constructor is ordinary integer code, with no guessed tail
behavior, randomized sampling, or floating-point acceptance tests.
