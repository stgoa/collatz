# V002: does a relational summary simplify an actual merger obligation?

**Outcome: representation test; no new merger or accepted domain. Stop and
demote shortlist A as a separate research portfolio.** Keep guarded affine
relations as supporting notation. This bounded comparison found that the
successful example already contains the proposed abstraction, while the
unresolved example already preserves the relation that a sound abstraction
would need. No theorem imported from abstract interpretation is used.

## 1. Success and failure gates

Objects are two actual positive odd Syracuse histories, with absorption at1,
their separate arrow clocks, exact valuation guards, affine offsets, and the
signed difference of their path currents. A relation's concretization must
consist of actual integer histories satisfying all those data. Merely making
two endpoint coordinates integral is insufficient.

The success gate was a simpler compositional relation which **adds a useful
closure implication** on a frozen successful family and survives a nontrivial
part of R93 without assuming its missing comparison. A compact restatement
of affine composition, endpoint equality or current telescoping fails the
gate. The intermediate target is a summary for a proper parameterized
family, with other families allowed to remain unresolved; it is not universal
certificate supply.

## 2. Successful comparison: R80/R81 already has the exact relation

[R80](../../../convergence/results/high-smaller-origin-history/README.md) gives a smaller
origin despite inverse obstructions through every prescribed depth D, with
the seed changing with D. Its merger clocks are nevertheless fixed. The
complete fixed-word cell is proved in
[R81](../../../convergence/results/fixed-word-history-cells/README.md): for every
integer k>=0,

```
q=11547+16*3^12*k,   p=11391+2^23*k,
2^19*q-3^12*p=309105,
q-p=156+114448*k>0,
S^2(q)=S^14(p)=(9q+5)/8.
```

The target word is `(1,2)`; the smaller-origin word is
`(1^6,2,2,1^4,2,6)`. Their valuation totals are3 and22, so the exact source
cylinders require moduli16 and2^23, including the extra bit. The R80
arbitrary-depth subfamily has `k=8192*3^(D-12)*t`, D>=12, t>=0.
“Arbitrary depth” here concerns excluded inverse comparisons; it does not
mean that the displayed merger takes arbitrarily many arrows.

At k0 the two endpoints are12991, above q11547; the lower history's peak
is369521. The ordinary clocks are **(2,14)**. The separately proved quotient
clocks **(1,13)** meet at17321 and must not replace them in a path current.
Writing I(x,t) for the first t actual arrow rows gives

```
div(I(q,2)-I(p,14))=[q]-[p].
```

This is already a compositional relation: after the actual merger, appending
any common suffix cancels from the current difference. R81 also classifies
the maximal CRT cell for any two prescribed words and the exact slope and
intercept condition for p<q. An “affine relational domain” reproduces that
theorem rather than shortening its mathematical obligation.

**Information-loss check.** The bare linear relation also holds at
q1074429, p1059967, obtained by increasing q by2*3^12 and p by2^20.
But `v2(3q+1)=3`, not the first prescribed valuation1. Retaining the relation
and dropping the exact word cylinder does not certify the displayed merger.
Restoring the guard restores precisely the data already stored in R81.
The comparison still requires a supplied current for the smaller origin,
or the signed smaller-rank requests of the frozen compiler.

## 3. Unresolved comparison: R93 already carries a joint invariant

Use the complete family and notation of
[R93](../../../convergence/results/two-source-normalisation-first-departure/README.md):

```
z=471104208005+2^14*3^16*ell,   ell>=0,
Q=(2^31*z-665034679)/3^15,   b=Q/3,
D=7153,   C=D*z-53,   n=v2(C),
z_j=Psi^j(z),   Psi(z)=(3^12*z-53)/2^19,
U_j=864*z_j-257=S^(18+12j)(Q).
```

The upper re-entry counter allows `0<=j<=floor((n-14)/19)`. If N_i is the
rational-shadow numerator and E_i its cumulative valuation cost, the actual
matching lower state is `L_i=S^(16+i)(b)` and satisfies

```
D*z_j-53=(3^12/2^19)^j*C,
D*L_i-N_i=(3^i/2^E_i)*C,
2^E_i*3^(12j)*(D*L_i-N_i)
    =3^i*2^(19j)*(D*z_j-53).
```

The last equation is a compact asynchronous relational invariant, valid
for every legal upper re-entry and every matching lower prefix. Advancing
either path preserves it with the stated updates of j, i, E_i and N_i.
However, it is obtained merely by eliminating C from R93's two stored
formulas. It supplies no new closure after lower departure. In its proved
range, R93 gives **L_i<z+115<Q<U_j**: the actual endpoints cannot cancel
there. Its further twelve-arrow lower window still lies below Q.

A focused exact example has ell922454, n33 and one upper re-entry:

| Quantity | Value |
|---|---:|
| z |650586500747312261|
| Q |97367964818811137307|
| upper endpoint at ordinary clock30 |569775707683020881887|
| last matching lower endpoint at ordinary clock28 |80500808671037|
| lower shadow length i / cost E_i |12 / 32|
| next shadow valuation |1|
| z_1-z |8876123885813760|

The lower endpoint uses the original source b and clock16+i, not the
coordinate z_1. The integer z_1 supplies no path from z to z_1. Indeed one
upper return leaves the exact defect

```
[U_0]-[z]
  =div I(U_0,12)+([U_1]-[z_1])+([z_1]-[z]).
```

Deleting the last term is precisely the false closure that an independent
interval, phase or integrality summary might suggest. The frozen proof
already rules out a fixed forward word z→Psi(z) on an infinite progression:
such a word has positive affine intercept, while Psi has negative intercept.
Variable words, unequal-time mergers and other signed comparisons remain
open; this probe supplies none of them.

## 4. Controls, translated gap, and stop verdict

The relation-and-current bookkeeping works unchanged on the absorbed d=5
map. Its exact cycle19→31→49→19 has word `(1,1,3)` and return
`(27x+95)/32`. A contracting multiplier and a perfectly closed relational
summary coexist with nonabsorption. A sound progress inference therefore
needs the actual equality to a supplied smaller origin, or another proved
terminal condition. The d=61 cycle with minimum235 likewise supplies no
smaller absorbed origin; none of the relational identities would erase its
cycle boundary or certify its absorption. These controls reject a generic
“summary closure implies convergence” inference, not the exact R81 merger.

**Translated unresolved gap:** supply an actual comparison between R93's
two residual endpoints after its complete lower-departure interface, retaining
both clocks and every defect. Calling this an abstract-domain closure problem
does not reduce its arithmetic content.

**Verification:** direct integer replay checked the16 arrows of the R81
anchor, the30 upper and28 lower arrows of the R93 example, the displayed
joint invariant, and the three-arrow d=5 control. These bounded checks
illustrate the translation; the all-parameter claims are the cited frozen
proofs. No search, new exit catalogue, dispatcher change or current premise
was added.

**Decision:** the success gate failed. The cheapest meaningful test was this
two-family comparison, and it found no new closure or simpler proof
obligation. Demote A from the active research shortlist; retain its exact
relations when another viewpoint needs arithmetic bookkeeping. Reopen it
only with a specific relation that handles a currently unsupplied endpoint
comparison or proves a genuinely new compositional consequence. A richer
record of the same histories alone is insufficient.
