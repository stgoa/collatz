# Complete smaller-history classification within ternary precision

**R82 — written finite-anchor completeness theorem and exact finite audit.**
This reduces all inverse rays and all depths within a stated ternary horizon
to a finite list of supplied anchor histories. It gives a sharp uniqueness
result for the enlarged R80 family. It does not prove universal access to a
smaller history or exclude additional comparisons beyond that horizon.

Use absorbed odd Syracuse S, canonical minimum nu, and T=nu S from
[R25](../bridge_normal_form/BRIDGE_NORMAL_FORM.md). Its complete inverse
branches are `x -> alpha*x+beta`, including every nonnegative ray index,
with alpha>0 and alpha-beta>=1. The exact formulas and inequality are in
[R41](../critical_inverse/CRITICAL_INVERSE.md). The finite table below is
a supplied premise, checked by arithmetic; no unknown orbit is searched.

## 1. A finite anchor table controls every smaller inverse history

Let Q be a finite canonical edge table, closed under T, with every vertex
reaching1. It contains every canonical origin c<=N. Extra states are
permitted. Fix a canonical anchor target Y>1. Take integers q>=2 and y>=Y,
with y canonical and

    y=Y modulo3^K,       K>=0.

The threshold q need not be the anchor origin and need not belong to Q.
Define the exact strict shadow cutoff

    C=(q+1)(Y+1)/(y+1),       n=ceil(C)-2.                  (1)

Assume n<=N. If n<1 the candidate set is empty. Form a finite catalogue:
for every canonical c<=n follow only its supplied table edges to1;
retain it exactly if the path visits Y. There is at most one such path,
since Y>1 and Q is absorbing. Let d_c be its length and lambda_c the product
of the affine multipliers on its reversed inverse word. Include the empty
word at c=Y when it is eligible, with d_c=0 and lambda_c=1.

**Theorem.** The complete set of pairs `(a,d)` satisfying

    a canonical, a<q, 0<=d<=K, T^d(a)=y                 (2)

is precisely

    (a,d)=(c+lambda_c*(y-Y), d_c)

over the catalogue entries with d_c<=K and a<q. Every inverse ray index
and every word length through K is covered; there is no ray search cap.
If Y is outside Q, the set is empty.

**Proof.** Shadow an arbitrary actual inverse word starting at y by the
same word starting at Y. Congruence modulo3^K ensures legality of every
branch through K, because every branch has denominator3 and numerator
multiplier a power of2. Write actual and shadow states as

    a_i=lambda_i*(y-Y)+c_i.

Starting from G_0=0, the exact recurrence is

    G_i=lambda_i-(c_i+1)/(Y+1)
       =alpha_i*G_(i-1)+(alpha_i-beta_i-1)/(Y+1)>=0.       (3)

All ray indices satisfy this inequality. Since y-Y>=0,

    a_i+1 >= (c_i+1)*(y+1)/(Y+1).                        (4)

If a_i<q, then c_i+1<C, equivalently c_i<=ceil(C)-2=n.
That shadow is therefore among the supplied origins. Its unique forward
path must visit Y after exactly i steps, so its inverse word is in the
catalogue. Absorption excludes extra traversals of a nontrivial cycle.
Conversely every listed inverse word of length at most K is legal at y,
gives a positive canonical integer, and has the displayed affine value.
Testing a<q proves sufficiency. The zero-length case obeys the same
inequality and is included explicitly. If Y is outside Q, forward closure
excludes every candidate. This proves the theorem.

The catalogue is finite independently of K: its size is at most the number
of canonical origins through N and each path length is at most |Q|-1.
This does not extend the theorem past the supplied ternary precision.
At greater depths the shadow branch can cease to be integral or legal.
The condition Y>1 also matters: repeated visits to the absorbing1 would
produce arbitrarily long anchor words rather than one path per origin.

## 2. The cutoff for a fixed affine forward comparison

Suppose a canonical target prefix has affine endpoint y=gq+h, g>0,
on a stated domain q>=b, and Y=gb+h>1. Then

    C=(q+1)(Y+1)/(gq+h+1)
      <= max(b+1,(Y+1)/g).                              (5)

The rational function is monotone or constant, so its supremum is one of
the endpoint and limiting values. Thus one finite anchor table covering
canonical origins through `ceil(max(b+1,(Y+1)/g))-2` suffices for all q in
that domain, subject to the required ternary congruence. This is a bound
on anchor origins, not on actual partner height or unknown orbit work.

For a prefix of j canonical valuation-one arrows,

    y+1=(3/2)^j*(q+1),       Y+1=(3/2)^j*(b+1),

and (1) simplifies exactly to n=b-1. The same smaller-origin anchor table
then controls every lifted smaller history at that future target.

One must not use n=b-1 for an arbitrary contracting prefix. An exact
counterexample is the pair of anchor paths

    465 ->43 ->65 ->49 ->9 ->7 ->11,
    497 ->11,

in the quotient clock. Their inverse multipliers are32768/729 and128/3.
For D>=0,t>=1 the complete lifted paths give

    q=465+2^19*3^D*t,
    p=497+2^11*3^(D+5)*t,
    y=11+16*3^(D+6)*t,
    T^6(q)=T(p)=y,       p<q.                           (6)

The anchor origin497 is larger than465. Their slope ratio243/256 makes
the lifted partner smaller; p-q=32-26624*3^D*t<0. The full inverse words
are legal because y=11 modulo3^(D+6), and y=11 modulo16 is canonical.
The anchor bound in (5) is393216/729, giving the safe origin cutoff538.
This example refutes the unrestricted smaller-anchor shortcut. It is not
claimed as a new accepted W5 domain.

## 3. A unique smaller history on the enlarged R80 progression

Use the exact [R80 anchor table](../native_history/anchor_certificate.json),
verified to have4892 canonical states, to include every2887 canonical
origin below b=11547, to be absorbing and forward-closed, and to exclude b.
Set Y=(3b+1)/2=17321.

Following every lower origin through the supplied table proves an exact
finite classification: **only c=11391 reaches Y**, and its quotient path
has length13. Its path is

    11391,17087,25631,38447,57671,86507,129761,
    97321,72991,109487,164231,246347,369521,17321.

Its inverse slope is lambda=2^20/3^13. Each reverse edge is identified
without truncation: for a ray base a0, `9a+7=64^j*(9a0+7)` determines the
unique index j>=0 exactly. This is an exhaustive finite table certificate,
not a scan of selected inverse words or a conjecture about minimum origins.

For every D>=1,t>=0 set

    q=11547+16*3^D*t,       y=(3q+1)/2.                  (7)

Both q and y are canonical, and q/3 lies in W9. The exact cutoff (1) is
11546 and y-Y=8*3^(D+1)*t. Therefore, for t>0, the complete set of smaller
canonical origins reaching y in at most D+1 quotient steps is:

- empty when D<=11;
- the single origin
  `p=11391+2^23*3^(D-12)*t`, at exactly13 steps, when D>=12.

For t=0, the same horizon statement holds, and the supplied anchor table
also proves this single smaller origin is the only one at **any** depth.
In the lifted case no exclusion past D+1 is asserted. The slope relative
to q is2^19/3^12<1, so p<q throughout the D>=12 family.

The same table, with anchor target11547, is empty of lower histories.
Applying (1) to target q itself gives the earlier complete exclusion
through D. Thus the direct inverse barrier and the unique high future
history follow from one finite-anchor theorem. The enlarged progression
contains8192 times as many integers as R80's original fixed-D progression;
its exact ordinary-word lifting and local phase scope are proved in R81.
Being in this larger W9 family does not imply being in its blocked local
row. At the quotient clock,13 is the sharp smaller-history length to the
specified one-step future y; this is not an optimality claim over later
target steps, other sources, or arbitrary currents.

## 4. Current construction and evidence

Every canonical arrow x->T(x) has the ordinary current
`delta_x+N_(S(x))`. Summing it over a retained partner path gives a checked
ordinary current L with divergence[p]-[y]. Subtract it from the target's
ordinary q-to-y arrow to get K with divergence[q]-[p]. With the R75 formal
critical plans, `K+J_p-J_(q/3)` requests `A_p-A_(q/3)`, every rank below q.
Negative coefficients and all normalizer rows are retained. Unknown
terminal pair currents are still supplied premises.

The checker reuses the4892-state certificate, exhausts its complete
lower-origin paths, verifies the exact inverse branch codes, independently
enumerates bounded inverse trees as a cross-check, tests large ray indices,
and checks (6) as a cutoff control. It reconstructs two actual supplied
currents from R80's stored inputs and verifies row equality and divergence.
The written theorem supplies the all-ray and all-depth-within-K quantifiers.
The default performs no absorption search outside supplied finite tables.

Run `python3 experiments/residual_progress/history_frontier/check_history_frontier.py`.
The receipt pins the proof, checker, anchor and reachable local source files.
No universal current supply, Collatz proof or novelty claim is made.
