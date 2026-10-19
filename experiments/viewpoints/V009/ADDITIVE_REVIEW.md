# V009 — Independent audit of the additive-excess theorem

**Outcome: written-argument audit passed.** I reviewed the saved
[`binary_tail.md`](binary_tail.md), especially Sections 8–10, against the
V004 positive-section closure and V005/V007 infinitude results. The claim
audited is

> If a finite-valued Collatz invariant `h` is nonconstant, then
> `kappa_h(D)-(D+1) -> infinity`.

This is a partial universal gain. It does not prove that
`kappa_h(D)/(D+1)` is unbounded, and it does not prove Collatz. The
application inherits Cobham through V004/V005/V007; Sections 8–10 add no
external theorem. The audit is neither formal verification nor a novelty
assessment.

## 1. Upstream quantifiers and state convention

The argument counts **entire** binary sections, with `h(0)=h(1)`. For a
nonconstant invariant, the binary kernel is infinite, and a missing new
layer would make it finite. Thus the excess above `D+1` is a nonnegative,
nondecreasing integer. Under `kappa_h(D)=D+O(1)`, every sufficiently deep
layer has exactly one new state `q_n`, while all earlier states form one
finite set. A positive-depth state has a positive-offset representation:
a zero-offset section equals `h` by doubling invariance, including at
input zero. Hence each `q_n` belongs to the positive-section family
`S=K_2(b)`, which is closed under both bases. The cited V005/V007 results
give infinite pure kernels in both bases at every state of `S`.

The depth-four bound for a ternary image is measured from `h`, not along
four binary edges from the current state. Sections 2–7 preserve this
distinction. For `tau(n)=max_j rho(T_j q_n)` and
`delta_n=tau(n)-n`, choose any escaping binary child
`E_i q_n=q_(n+1)`. Each radix swap writes its ternary child as a binary
child of some `T_k q_n`, so `tau(n+1)<=tau(n)+1` and `delta_n` is
nonincreasing. If it ever reached zero or below, all later tail ternary
edges would be nonexpanding in minimum depth. Enlarging a finite binary
ball beyond the ternary images of its finite earlier set would make that
ball ternary-closed, contrary to pure ternary infinitude. Thus the
eventual integer increment is in `{1,2,3,4}`. At increment one the same
finite-ball construction has only the next binary state as a possible
exit; an actual binary edge reaches it. V007's exact single-exit theorem
excludes this case, leaving `{2,3,4}`.

For the maximal boundary, a nonescaping binary child has depth at most
`n`, so one ternary edge cannot reach `n+delta+1`; similarly a
nonmaximal ternary child cannot reach it by one binary edge. The finite
earlier-state images are excluded by choosing the stable depth above
their finitely many images. Consequently the polynomial identity
`X_n(z)Y_(n+1)(z^2)=Y_n(z)X_(n+delta)(z^3)` compares exactly the six
affine residues, not merely the number of paths. At a primitive eighth
root it excludes the ternary gap pair; at a primitive fourth root it
then excludes adjacent pairs. Primitive third and sixth roots match the
remaining ternary triple indicator to itself at the next index and to
the binary doubleton indicator. Thus eventually both maximal-digit sets
are full or both are singletons. In the full case both binary children
of each late `q_n` equal `q_(n+1)`; repeated binary reading and the
zero-output equality make `q_n` constant as an entire function. This
contradicts its growing minimum depth.

In the singleton case, the coefficient identity is
`c_n+2*d_(n+1)=d_n+3*c_(n+delta)`. Multiplying its rearrangement by
successive powers of two and reducing modulo `2^L` gives the saved
equation `(2^delta-3)R_(n,L)=2^delta*d_n-3*P_n (mod 2^L)`.
Because `2^delta-3` is odd, the finite pair `(P_n,d_n)` determines
*every* future binary prefix. Repetition of a pair gives a common
eventual period for `c`; bounded integer differences satisfying
`e_n=2*e_(n+1)` give the same period for `d`. For `delta=2` the
coefficient is one, so each binary tail is the 2-adic expansion of an
ordinary integer and is eventually all zeros or all ones. The same
bounded-difference identity forces `d=2c` on that tail.

I also checked the constant-tail bootstrap, which is needed both for
`delta=2` and for the endpoint phases at larger increments. With
`c` constant and `d=2c`, the radix swap gives exactly
`A_(n+delta)=T_1 A_n`. The second swap
`E_c(T_1q_n)=T_(2c)(A_n)` shows that, when both images are late ray
states, the depth of `T_1q_n` equals `rho(A_n)+delta-1`.
If either image lies in the finite earlier set, its bounded depth is
absorbed in a constant. Combining this with the first recurrence first
gives a slope below one and then a global strict contraction for `T_1`
on the positive-section family. Hence the `A` states lie eventually in
one finite set and are periodic. The zero outputs and then induction on
input make the `q` states periodic as **entire functions**, a
contradiction. No bound on the size of a backward return is inserted.

Finally, the phase classification is exact: the periodic center obeys
`v_(n+1)=(v_n+M*c_n)/2` with `c_n=v_n mod 2`, where
`M=2^delta-3`. The endpoints `0,M` are the just-excluded constant
patterns. For `M=5` and `M=13`, the displayed cycles exhaust all
interior residues. They give the two periodic nonconstant patterns with
`delta=3` or `4` used below.

## 2. Phase arithmetic and the half-odd obstruction

For either remaining pattern, `M=2^delta-3` is odd, and
`x_n=-v_n/M` with `v_n` in `1,...,M-1` and `c_n=v_n mod 2`. The radix
identity for the nonescaping binary child has residue equation

```
2*j_n+(1-c_n) = d_n+3*(1-c_(n+delta)),
```

so the displayed `j_n=(d_n+2+c_n-3*c_(n+delta))/2` is an integer ternary
digit and gives the exact whole-function identity
`A_(n+delta)=T_(j_n) A_n`. Substituting the two center recurrences gives
`y_n=j_n+3*y_(n+delta)` without an assumed section equality.

The numerator of
`y_n=-(v_n+M*(1-c_n))/(2*M)` is odd. Thus `y_n` has 2-adic
valuation minus one, whereas every `x_a=-v_a/M` has nonnegative
2-adic valuation. In particular, `y_n != x_a` for every pair of stable
phases. If all `p` transitions of the `j` word starting at an arbitrary
tail state `q_a` were maximal, both center recurrences would use the same
digits. Since both centers are `p`-periodic, iteration gives
`y_n-x_a=3^p*(y_n-x_a)`, a contradiction. This remains true when
`gcd(p,delta)>1`: `p*delta` is a multiple of the common period.

As a finite arithmetic sanity check, the two phase cycles produce `j`
words `2002` and `112202110020`, respectively. Exact integer substitution
checks `3*w_(n+delta)-w_n=2*M*j_n` for
`w_n=v_n+M*(1-c_n)`. No phase pair follows an all-maximal `p` block.
These checks illustrate the symbolic argument; they do not replace it.

## 3. Strict depth gain, including the finite core

For `U_n`, the `p`-step ternary word above, a path staying in the stable
tail has at least one nonmaximal edge. That edge raises minimum depth by
at most `delta-1`; each other edge raises it by at most `delta`. If the
path enters the finite earlier set, only finitely many states and suffix
words of length at most `p` remain. The same finite bound covers a path
starting there. Thus one constant `H`, independent of the starting state
and `n`, satisfies

```
rho(U_n(s)) <= max(H, rho(s)+p*delta-1).
```

Applying `A_(n+p*delta)=U_n(A_n)` along the finitely many index residue
classes yields `rho(A_n)<=lambda*n+B` with
`lambda=1-1/(p*delta)<1`. This is only a slope gain, not yet a finite
bound; the proof does not mistake it for one.

## 4. Every nonmaximal ternary return has the same slope gain

If `T_j(q_n)=q_m` is a tail state and `j!=d_n`, the proposed rational
center equality `x_n=j+3*x_m` would imply
`v_n=3*v_m-M*j`. Comparing it modulo `M` with the critical identity
`v_n=3*v_(n+delta)-M*d_n` gives
`v_m=v_(n+delta)`, since `3` is invertible modulo `M` and both values
lie strictly between `0` and `M`. The integer equality then gives
`j=d_n`, a contradiction.

The unequal rational centers have odd denominator, so a finite binary
prefix distinguishes them. The required length `k` may depend on the
two state phases; no uniform length is assumed. Write the critical
`k`-bit word of `q_m` as `R`, and divide `3R+j=2^k*t+u`. Then
`0<=t<=2` and the exact affine interchange is

```
q_(m+k)=E_R(T_j q_n)=T_t(E_u q_n).
```

At the first bit `ell<k` where `u` differs from the critical word of
`q_n`, the binary path reaches `A_(n+ell)`. Its remaining
`k-ell-1` binary edges raise minimum depth by at most that many. A
ternary edge raises depth by at most one fixed global constant, using
the stable bound and the finite earlier set. Therefore

```
m+k <= lambda*(n+ell)+B+(k-ell-1)+C_0,
m <= lambda*n+B+C_0-1+(lambda-1)*ell
  <= lambda*n+C_1.
```

The coefficient of `ell` is nonpositive. This is the decisive uniformity
check: an arbitrarily long distinguishing word does **not** degrade the
contraction. An image in the finite earlier set is covered by enlarging
`C_1`. Thus the bound is uniform over all nonmaximal digits, all tail
indices, and all returns, however far backward they jump.

## 5. Bounded returns and whole-function contradiction

In each `U_n` path, either the finite core is visited or some first
nonmaximal ternary transition occurs. Before that transition, depth can
grow by at most `delta` per step. The transition obeys the preceding
`lambda` bound, and only a fixed number of later edges remain. This gives
`rho(U_n(s))<=lambda*rho(s)+C_2` uniformly on `S`. Iterating on the
`p*delta` index classes makes all sufficiently late `A_n` members of one
finite set.

The word `U_n` depends only on `n mod p`, and `p*delta` is a multiple of
`p`. Each residue-class subsequence of `A_n` is therefore an orbit of
one deterministic map on a finite set. A common eventual period `P` may
be chosen to preserve both the `A` states and the escape digits.

Both remaining binary escape words contain a `1`. Following a bounded
initial run of zero escape digits reduces `q_n(0)` to some
`A_(n+t)(0)`, so the zero outputs have period `P`. Induction on each
positive input, simultaneously for all sufficiently large `n`, then
uses the nonescaping child equality or passes from the escaping child
to the smaller input `floor(z/2)`. It proves
`q_(n+P)=q_n` as entire functions, contradicting their distinct minimum
depths. No inference from matching finite prefixes is used.

## 6. Scope and next obstruction

The audited theorem excludes only an eventual single new binary state
per layer. Since the excess `kappa_h(D)-(D+1)` is nondecreasing,
excluding bounded excess does prove that it tends to infinity. Growth
such as `D+sqrt(D)` remains compatible with this conclusion; the active
unbounded-ratio goal is still open. The proof's new arithmetic gain is
control of **every** nonmaximal return without a bounded-backjump or
uniform distinguishing-prefix premise. Extending that control to
several new states at recurring layers is the unresolved step.

The d=5 and d=61 periodic generalized-map colorings have finite kernels
and fail the required two-base-infinitude premise. They therefore remain
known-cycle controls rather than counterexamples to this theorem.
