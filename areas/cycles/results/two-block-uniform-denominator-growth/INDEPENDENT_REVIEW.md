# C003 independent mathematical review

**2026-10-19. Verdict: PASS for the written two-square theorem, with the
published Corvaja–Zannier results kept as explicit inputs.** I reviewed
the final saved [UNEQUAL_PROBE.md](UNEQUAL_PROBE.md) independently of its
author. This is a review of the argument and its stated scope, not a
formal proof, a novelty assessment, or a new finite census. The headline
exclusion of every nontrivial Collatz cycle remains open.

## 1. Unequal slopes: source and quantifiers

I checked the [Corvaja–Zannier author preprint](https://arxiv.org/pdf/math/0311030),
math/0311030v2. Its Corollary 1, Eq. (1.3), gives the required
finite-exception estimate for multiplicatively independent pairs in
one **fixed finitely generated group**. Proposition 1, Eq. (2.2), gives
the finite union of translated one-dimensional subtori, plus finite
points, used for the positive power-gap estimate. The application does
not treat a changing block pair as a changing group: all pairs lie in
`Gamma=(<2,3>)^2`.

For `X=2^(ak)/3^(rk)` and `Y=2^(b*ell)/3^(s*ell)`, a relation
`X^i Y^j=1` has 2- and 3-valuation determinant
`k*ell*(a*s-b*r)`. Thus unequal slopes make **every** relevant pair
independent. At primes other than 2 and 3, the local sum in the
corollary is `-log gcd(|2^(ak)-3^(rk)|,|2^(b*ell)-3^(s*ell)|)`;
the 2- and 3-terms vanish, and the archimedean term is nonpositive.
The resulting logarithmic gcd is `o(A)` uniformly in the changing
blocks. A finite exceptional rational pair cannot have infinitely
many word presentations: its four 2/3 exponents are fixed, each
repetition count divides fixed integers, and fixed length and total
admit finitely many positive valuation words.

The Proposition 1 exception handling also survives variable blocks.
For `2^A>3^M`, the grid point `(2^A,3^M)` on a translated subtorus
`X^pY^q=lambda` has at most one pair `(A,M)` if `p*q!=0`.
If `p=0`, M is fixed and `2^A/3^M-1` eventually exceeds 1.
If `q=0`, A is fixed and positivity bounds M. Each translate
therefore contains finitely many **bad positive-grid** points.
This proves `log(2^A-3^M)=A*log2-o(A)` uniformly, including near
the expansion/contraction boundary.

## 2. Uniform algebra and the unequal-slope rate

The prefix bound gives
`C_z< B_z=2^(A_z-m_z)3^m_z`. As `A_z>=m_z`, both
`2^A_z` and `3^m_z` are at most B_z, with the strict difference
bound `|D_z|<B_z`. Consequently

```
|K|<2*B_u*B_v,
log|K|<log2+gamma_q*A*log2,
gamma_q=(2-log_3 2)/q.
```

This calculation permits either block to expand. The exact dual
elimination gives
`gcd(C_w,D_w) | |K|*gcd(G_u(k),G_v(ell))`.
On the positive domain, `K=0` would force two contracting blocks
with the same positive fixed point; exact deterministic valuations
then force equal slopes. Thus `K!=0` in the unequal-slope branch.
Combining the three estimates yields

```
log den(w)/(A*log2) >= 1-gamma_q-o(1).
```

For `q=2`, `1-gamma_q=0.3154648768...>0`. The threshold is
uniform in the two words but ineffective because the imported
Subspace Theorem does not supply a bound for the finite exception set.

## 3. Proportional slopes at two repetitions

I checked the new integer lemma in §5.2. With coprime `R,S`,
`k,ell>=2`, `L=Rk+S*ell`, `H=gcd(Rk,S*ell)`, it proves

```
5*(L-H+1)>=7*(R+S).
```

The three cases for coprime `Rk/H` and `S*ell/H` are complete.
When their sum is at least 4, `R+S<=L/2` suffices. When both equal 1,
the common value is a multiple of `R*S` by coprimality; the `R=1`,
`R=2`, and `R>=3` checks cover every case. When their sum is 3,
the only potentially tight situation has both repetition counts 2;
coprimality then forces the small pair handled directly. The bound
is attained for `(R,S,k,ell)=(2,3,3,2)`.

The proportional proof correctly retains
`E=2^(a_0*e)-3^(b_0*e)` from the C002 strong-divisibility bound.
The global power-gap estimate gives
`log E=e*log U_0-o(A)` **uniformly**: for any epsilon, the finitely
many small binary exponents contribute one constant `C_epsilon`,
while the error for larger exponents is at most epsilon times their
binary exponent, which is no larger than A. This covers sequences
where `a_0*e` stays bounded while k or ell grows.

Writing `T=L-H+1`, `B=R+S`, and `c_0=2-log_3 2`, the commutator bound
and lemma give `B<=5T/7`, `T>=L/2`, and

```
T-c_0*B >= (7-5*c_0)*L/14
          = ((5*log_3 2-3)/14)*L.
```

The coefficient `eta_*=(5*log_3 2-3)/14=0.0110463406...` is
positive because `2^5>3^3`. The exact rate is therefore positive
uniformly over **varying** proportional words with `K!=0` and
`k,ell>=2`. The separate `q>=3` estimate is effective and does not
claim effectiveness for this two-square refinement.

## 4. Controls, correction and limits

The final saved worked example `(1)^3(2)^5` has
`C=10865`, `D=1631`, gcd 1 and denominator 1631. The author
explicitly corrected a draft-only arithmetic error in §8. The
`K=0` case keeps the actual raw denominator-1, 5, 7 and 13 cycle
controls; the theorem does not exclude them. All words use exact
odd-only valuations and raw arrows, with no absorber at 1.

The elementary [contracting-block proof](../contracting-two-block-effective-exclusion/PROPORTIONAL_UNIFORM.md) is
authored by this reviewer, so I do **not** label this document an
independent review of that proof. The root and the unequal-slope lane
separately reported independent checks of its trapping, lattice
divisibility, maximum-length bound and finite-layer consequence.
Section 7 of UNEQUAL_PROBE.md records a valid weaker minimum-length
version; PROPORTIONAL_UNIFORM.md gives the stronger maximum-length
bound. Neither version applies when a block expands.

**Conclusion.** The two-square conclusion is a written structural
theorem: among `u^k v^ell` with `k,ell>=2`, positive raw cycle
denominator and `K!=0`, every bounded denominator layer has finitely
many representations even as both words vary. Its common-cycle
exception, ineffective asymptotic threshold, expanding-block finite
range, and arbitrary-word gap remain explicit.
