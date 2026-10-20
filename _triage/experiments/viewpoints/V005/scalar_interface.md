# V005 — Three scalar identities retain the complete Collatz guard

**Status: written equivalence, independently agent-reviewed.** This is a
precise interface for the next growth argument, not a new convergence
criterion or completion of the quantitative goal.

Let b be any finite-valued sequence on n>=0. Set h(0)=b(0) and, for n>0,

```
h(n)=b((oddpart(n)-1)/2).
```

Then h(0)=h(1), h(2n)=h(n), and h(2n+1)=b(n). The remaining invariant
equation `h(3n+1)=h(n)` at positive odd n>1 is equivalent to the following
three identities, all for n>=0:

```
b(3n)=b(4n),
b(3n+2)=b(2n+1),
b(4n+2)=b(n).                                      (1)
```

The forward implication is the V004 algebra. The omitted odd source1
equation is already the valid color equality h(4)=h(1).

For the converse prove E(n): `h(3n+2)=b(n)` by strong induction. E(0)
is h(2)=h(1)=b(0). If n=2m+1, then

```
h(3n+2)=h(6m+5)=b(3m+2)=b(2m+1).
```

If n=4m, use doubling and the first identity:

```
h(3n+2)=h(12m+2)=h(6m+1)=b(3m)=b(4m).
```

If n=4m+2, use E(m) and the third identity:

```
h(3n+2)=h(12m+8)=h(3m+2)=b(m)=b(4m+2).
```

Here m<n, so the induction is valid. Thus E holds everywhere, and

```
h(3(2n+1)+1)=h(6n+4)=h(3n+2)=b(n)=h(2n+1).
```

This gives the full invariant coloring. No orbit convergence or finite
kernel was used. The additional V004 relation
`b(3n+1)=b(16n+8)` now follows; it need not be an extra assumption.

## Exact complexity comparison

For D>=1 the positive-offset h-sections through depth D are exactly the
binary b-sections through depth D-1. In one direction strip the power of2
from the positive offset; in the other direction use

```
b(2^a*n+r)=h(2^(a+1)*n+2r+1).
```

The zero-offset sections of h all equal h. Therefore

```
K_D(h)={h} union K_(D-1)(b),
kappa_b(D-1) <= kappa_h(D) <= 1+kappa_b(D-1).           (2)
```

Combined with the depth comparison in [direct_sections.md](direct_sections.md),
this makes linear binary growth of h equivalent to linear joint2/3 section
growth of b under (1). The unresolved target is to prove that a nonconstant
finite-valued b satisfying (1) cannot have that growth. Stating this
equivalence does not prove the required exclusion.

The [graph control](section_graph.md) retains only the third relation of
(1), and fails the first at n=1. Its linear count is therefore a useful
test against discarding part of the interface, not a counterexample to it.
