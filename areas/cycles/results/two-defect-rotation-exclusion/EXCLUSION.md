# C011 — No two-defect rotation in a nontrivial integer cycle

**Status: written proof using explicitly identified published inputs.**
Independent review is recorded separately. This is an all-size exclusion
of a structural class; arbitrary cycles and divergence remain open.
No novelty or formal-verification claim is made. Use the raw positive
odd-only clock, with no absorber.

## 1. Statement

Let w be a positive valuation word of length m, with total A and
`D=2^A-3^m>0`. If any nonidentity cyclic rotation of w differs from
w in exactly two positions, then its reduced denominator

```
q = D/gcd(C_w,D)
```

is greater than one. There is **no bound on the period, state height,
valuation alphabet, mismatch amplitude, arc lengths or shift gcd**.

Equivalently, every hypothetical nontrivial integer Collatz cycle must
have at least three mismatches with every nonidentity rotation of its
primitive valuation word. This constant lower bound is not the proposed
growing-complexity milestone. Rotations cannot have just one mismatch,
and a primitive word cannot have zero. Three is not ruled out here:
for alphabets with more than two letters a rotation distance can be odd.

Exactly two mismatches force primitivity: an e-fold repeated word would
repeat the mismatch set e times, and a nonzero mismatch count in a
shorter word is at least two. Repetitions of the trivial word `(2)`
therefore lie outside the hypothesis and retain denominator one.

## 2. Published inputs and their scope

**Explicit logarithm estimate.** Apply the positive rational version of
Matveev stated in Languasco–Luca–Moree–Togbe,
[Theorem 2.1](https://link.springer.com/article/10.1007/s12188-025-00293-9),
to the bases 2,3 and exponents -A,m. For `B>=max(A,m)`,

```
log(1-3^m/2^A) > -K_0(1+log B),
K_0=1.4*30^5*2^(9/2)*log(2)*log(3) < 600,000,000.       (1)
```

Logs are natural, the field degree is one, and `D>0` makes the form
nonzero. This is an imported theorem, not a reconstructed proof.

**Integer-cycle period input.** Hercher's
[Corollary 29 and Remark 30, pp.20–21](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf)
give an odd-member count greater than `137,500,000,000` once convergence
is verified through `3*2^69`. Barina's
[2025 paper, section 6](https://link.springer.com/article/10.1007/s11227-025-07337-0)
reports verification for every positive integer below `2^71`.
The required endpoint is strictly inside that interval because
`3*2^69<2^71`. Hercher's K counts odd members and equals our m;
his variable m counts local minima and is a different quantity.
Both published computations are imported, not independently rerun here.
The [corrigendum](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/corrigendum.pdf)
repairs Theorem 21; Corollary 29 uses the separate Lemma 26 method.

Thus a nontrivial integer cycle satisfies

```
m > M = 137,500,000,000.                               (2)
```

Without this published period input, the argument below gives the
conditional exclusion for `m>=M` and leaves smaller periods unresolved.
No universal numerical cycle record is improved.

## 3. The elementary cancellation bound has no amplitude cap

Let `g=gcd(C_w,D)`. The two different entries are exchanged by the
rotation. Write them as `a,a+k`, with `a,k>=1`.
The two complementary arc identities in
[ROTATION_DEFECTS.md](ROTATION_DEFECTS.md), including their unused
terminal valuations, give

```
g^2 < (2^k-1)^2 2^(A-m-k) 3^m.                         (3)
```

Since one entry is at least `k+1` and every other entry is positive,
`k<=A-m`. Therefore

```
g^2 < 2^(A-m+k)3^m <= 2^(2A-2m)3^m,
q > (1-3^m/2^A)(2/sqrt(3))^m.                          (4)
```

These bounds apply across the generalized family at the true reduced
q. They do not assume q=1, a height bound, or a pure-block contraction.

## 4. Denominator one contradicts the explicit estimates

Suppose q=1. Primitivity makes the resulting integer cycle nontrivial.
Every odd state n_i is at least 3; multiplying its exact arrows yields

```
2^A = product_i (3+1/n_i) < 4^m,
```

so `A<2m`. Apply (1) with `B=2m`, then (4):

```
log q > F(m),
F(m) = m log(2/sqrt(3)) - 600,000,000(1+log(2m)).        (5)
```

The following estimates have elementary rational certificates:

```
sqrt(2)<10/7,   log(2)<7/10,   log(3)<11/10,
K_0 < (7/5)*30^5*16*(10/7)*(7/10)*(11/10)
    = 598,752,000 < 600,000,000.
```

Also `log(4/3)=2*atanh(1/7)>2/7`, hence
`log(2/sqrt(3))>1/7>7/50`. Positive Taylor terms give
`exp(27)>2M`, hence `log(2M)<27`. At the boundary,

```
F(M) > (7/50)M - 600,000,000*28
     = 2,450,000,000 > 0.                              (6)
```

For all real `m>=M`,

```
F'(m) = log(2/sqrt(3)) - 600,000,000/m
      > 7/50 - 6/1375 = 373/2750 > 0.                  (7)
```

Thus (2) implies `log q>0`, contradicting q=1. This proves the full
statement, including arbitrarily large mismatch amplitudes. QED.

[check_exclusion_constants.py](check_exclusion_constants.py) checks the
rational estimates, endpoint containment and monotonicity constants.
Its receipt does not replay the imported theorem or computations.

## 5. Scope, controls, and the next obligation

The actual cycles at d5, d7 and d13 include two-defect valuation words.
They are allowed: (3)–(4) constrain their actual reduced denominators,
while the period input (2) is only for nontrivial integer cycles at
additive parameter one. Scaling a generalized cycle does not turn its
normalized rational cycle into a denominator-one cycle.

The explicit marker family in ROTATION_DEFECTS has unbounded minimum
and unbounded shortcut local-minimum count, and a direct elementary
q>1 bound without (1) or (2). It separates the stated earlier block
classes. This establishes scope beyond fixed numerical record
hypotheses; it does not establish novelty against all literature.

For general rotations, the intercept difference is a signed sum over
several prefix-discrepancy plateaus. Divisibility of that sum does not
imply divisibility of its terms. A theorem forcing the mismatch count
to grow with period would require control of those coupled sums.
Nothing here establishes that growth, covers all primitive words, or
excludes divergent trajectories.

## Draft history

The first draft used a weaker arc bound and proved only `k<=m/6`
exclusion from an older published period lower bound. Retaining the
terminal valuations first improved that range, then the observation
`k<=A-m` removed amplitude from the denominator estimate altogether.
The explicit all-amplitude application uses the newer period input
specified above. The earlier valid weaker draft is superseded; no
historical C001–C010 theorem was changed.
