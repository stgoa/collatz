# V001 discrimination probe: what an exact loop summary buys

**Outcome: representation clarified; no new absorption result.** This
bounded probe treats one R31 guard, not a new exit catalogue or dispatcher.
Its all-repetition arithmetic is a direct consequence of persisted R31,
and its general mechanism already appears in R77.

## 1. One concrete block, with its exact domain

Use positive odd Syracuse S, absorbed at 1. R31's word is

```
v=(1,2,1,1,1,1,2,2),   length=8 odd arrows,   total valuation=11,
G={positive x:x=27 mod2^17},
Psi(x)=(6561x+9221)/2048,
z(x)=4513x+9221.
```

On G, this is an actual eight-arrow path, all its states are canonical,
and it implements the two prescribed normalized returns (2,2),(5,4).
Every noninitial state in the block is above the block's starting height.
R31 proves

```
z(Psi(x))=(3^8/2^11)z(x).                         (1)
```

For any fixed x0 in G put b=v2(z(x0))>=17 and z(x0)=2^b u, with u
positive odd. Then, for every integer j in the complete guarded prefix,

```
x_j=S^(8j)(x0),
4513x_j+9221=3^(8j)2^(b-11j)u,
b_j=v2(z(x_j))=b-11j.                            (2)
```

The next guarded copy is legal exactly when b_j>=17. Consequently

```
r=floor((b-6)/11),
6<=b_r<=16,
tau_G(x0)=8r.                                   (3)
```

Here tau_G counts arrows to the first *macro-boundary* outside G; it is
not the first ordinary departure from G, since intermediate states leave
G inside each block. Integrality of every x_j follows inductively from
the exact guarded word. Finiteness follows from z(x0)>0 and finite b;
the negative rational fixed point has z=0 and is outside the domain.

Equations (2)–(3) certify exit for **every positive input in G**, with an
input-dependent finite clock. They certify no height descent: r>=1 and
x_r>x0. They do not prevent a later, different word from re-entering G
with a newly large counter.

There is a further necessary distinction. The raw word v itself has the
complete exact cylinder x=27 mod2^12, because its valuation sum is11.
Thus the guarded phase can end at b_r in {12,...,16} while one further
raw copy of v remains legal. Formula (3) counts complete copies of the
**chosen guarded phase**, not the maximum number of raw word copies.
An exact prescribed value b also retains its extra bit: v2(z)=b means
z=2^b mod2^(b+1).

A focused 16-arrow check illustrates the distinction: x0=12451867 has
b=23. Its first copy ends at39890971 with b=12, outside G; another raw
copy still ends at127795249. These integers are an example, not the proof
of the all-input formulas.

## 2. Three representations, three different guarantees

| Representation | What it preserves | What it proves here | What it loses |
|---|---|---|---|
| Finite labels for run type and bounded residues | A finite transition graph | The repeated labels are legal for arbitrarily long finite prefixes | Which fixed integer must eventually leave; height-monotone ranking is excluded by R31 |
| Unbounded counter b plus affine data (2) | Exact guard consumption, height, and clock | All-input finite exit from this guarded subsystem | Behavior after exit, re-entry, and any supplied smaller-seed connection |
| Relation between two actual histories | Joint affine/counter constraints and signed boundary | Can retain cancellation or separation which two independent summaries discard | A useful relation and its closure must still be proved |

A finite graph may overapproximate arbitrarily long prefixes by an
infinite loop without asserting a concrete divergent orbit. Adding b
removes that spurious *single-guard* infinite run. It does not create a
global ranking function.

For a simple relational diagnostic, let x0 and y0 be distinct inputs in
G and run both through j legal copies. Then

```
2^(11j)(x_j-y_j)=3^(8j)(x0-y0).                  (4)
```

Their separation increases and they cannot merge at equal macro times.
This is a useful rejection of an unsuitable synchronous comparison.
It says nothing about unequal-time mergers or paths which choose different
subsequent words. It is again the existing affine identity, not new coverage.

## 3. Where the naive conclusions fail

* **Counter descent implies absorption:** false inference. The counter
  ranks membership in one guard. Its zero region contains positive states
  above the original input, with further transitions unaccounted for.
* **Finite exit of every fixed word implies every trajectory terminates:**
  false inference. A trajectory can change words indefinitely. R77 already
  treats this distinction: its fixed-word counts and factor-complexity
  bounds leave sufficiently complex aperiodic survivors open.
* **A contracting affine multiplier is sufficient:** the d=5 cycle has
  exact word (1,1,3), and on its complete cylinder
  `S_5^3(x)=(27x+95)/32`. Its slope27/32 is below1, but19 is its positive
  fixed point and follows19→31→49→19. Ignoring the intercept falsely
  predicts progress. Absorbing only at1 leaves this cycle intact.
* **Two separate source bounds settle a signed comparison:** R93 already
  retains an upper source above original rank and a lower source below it;
  the unresolved two-atom boundary remains. Ordering alone cannot erase it.

## 4. One proposed relational invariant, without asserting it closes

For example, restrict to the proper progression x0=27 mod(3*2^17), which
still admits unbounded guarded repetition counts by CRT. Fix the actual smaller
seed y0=(x0-1)/2. Keep x_j=S^(8j)(x0), a separately timed actual state
y_t=S^t(y0), the original x0, counter b-11j, and both finite histories.
The exact invariant to preserve is

```
div(J_(8j,x0)-J_(t,y0))
    = [x0]-[y0]-[x_j]+[y_t].                     (5)
```

Here J_(k,n) is the sum of the first k actual odd-arrow rows from n,
with the row at1 killed. Formula (5) retains unequal clocks and every
signed coefficient. A relational abstract state must additionally couple
x_j and y_t; independent interval bounds would throw that information
away. Advancing either history preserves (5), but does not reduce its
two unresolved endpoint atoms automatically.

**Concrete intermediate milestone:** on this progression or an explicit
subprogression still admitting unbounded repetition counts, find a
counter-parameterized relation on these tuples
that is closed under its stated asynchronous advances and proves an
actual endpoint equality x_j=y_t for all its admitted repetition counts.
Allow the two clocks to grow. An exact symbolic certificate should verify
the relation and its terminal equality; other progressions remain open.
With a supplied current for y0 this would yield the corresponding current
for x0. This is not universal supply, and no such relation has been found
in this probe. Simply adding (5) to a state record is not the milestone.

## 5. Novelty and portfolio decision

* [R31](../../../convergence/results/bounded-runs-exclude-finite-label-potentials/README.md)
  already supplies the affine identity, exact cylinders, and arbitrarily
  long guarded growth. Formula (3) is its immediate exact-counter reading.
* [R77](../../../convergence/results/same-seed-factor-complexity-bound/README.md)
  already gives the general fixed-word repetition formula and distinguishes
  single-word exit from multiword survival.
* R53 and R57 already combine valuation counters with complete exit
  interfaces on other phases. Repeating that pattern is not a new language
  breakthrough.
* [R93](../../../convergence/results/two-source-normalisation-first-departure/README.md)
  already carries two actual histories and a complete lower-departure
  interface. Its unresolved signed residual is the standard this proposal
  must improve upon.

**Recommendation:** no separate research slot for unary inducing or the
counter formula. At most retain one conditional relational pilot, with
the explicit equality/closure milestone above and a stop rule if it only
reproduces existing path identities or exit classifications. The present
probe demonstrates a useful representation distinction, not evidence of a
new arithmetic mechanism. No scan, new dispatcher rule, expanded exit
catalogue, or universal termination claim was made.
