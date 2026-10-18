# No uniform fixed-word affine pair descent on the complete mixed-growth guard

**Status:** written exhaustive-search theorem with a finite exact certificate and
an independent enumeration. This is a scoped exclusion of one comparison model,
not a convergence theorem, a formal proof-assistant result, or a novelty claim.

## 1. Exact statement and scope

Use the ordinary odd Syracuse map

    S(x)=(3x+1)/2^v2(3x+1),  S(1)=1.

Let

    R=40529845, P=2^26, w(n)=R+Pn, for every integer n>=0.

This is the complete positive guard of the
[mixed-growth comparison](../mixed_rank_recursion/MIXED_GROWING_BLOCK.md).
There is no affine function `u(n)=alpha*n+beta` satisfying, simultaneously:

1. For **every** integer `n>=0`, `u(n)` is an integer, `0<u(n)<w(n)`, and
   `u(n)=5 mod8`.
2. There are nonnegative integers `j,ell,k,m` such that, for every `n>=0`,

       S^j(w(n))=S^ell(u(n)),
       S^k(3w(n))=S^m(3u(n)).

3. Each of these **four complete ordinary valuation words is fixed independently
   of n**. Empty words and unequal clocks are allowed.

The quantifiers are essential. In particular, this does **not** exclude fixed
clocks whose intermediate valuations vary with `n`. It also does not exclude
input-dependent clocks or words, binary or ternary subprogressions, non-affine
partners, partners outside `5 mod8`, multiple retained pairs, or general signed
currents. No universal current is supplied or ruled out.

The conclusion is that every candidate satisfying the lower common-tail
requirement fails the upper fixed-word requirement. The proof exhausts all
possible clocks and valuations within this model; it does not impose a guessed
search horizon or valuation cap.

## 2. Affine domain and complete fixed paths

Integrality at `n=0,1` forces `alpha,beta` to be integers. The inequalities for all
`n>=0` are equivalent to

    0<=alpha<=P, 0<beta<R.

The constant case `alpha=0` cannot share a fixed-word lower tail with `w`: every
finite fixed-word image of `w` has strictly positive affine slope, while an
image of a constant has slope zero. Thus only `alpha>0` remains. The W5 condition
is exactly `alpha=0 mod8, beta=5 mod8`. Equality `alpha=P` is allowed.

Represent a nonconstant positive odd progression by `(a,b)`, meaning `an+b`,
where `a` is positive even and `b` is positive odd. Put

    e=v2(a)=v2(3a), d=v2(3b+1).

Its next valuation is fixed for every `n>=0` if and only if `d<e`. If this holds,
the numerator divided by `2^d` has odd constant and even slope, so its valuation
is exactly `d` throughout. If `d>e`, the valuations at `n=0,1` differ; if `d=e`,
the divided numerator is odd at `n=0` and even at `n=1`. Therefore a fixed word
cannot continue through either case. A successful step gives

    (a,b) -> (3a/2^d,(3b+1)/2^d).

Each successful step lowers the binary order of the positive slope by at least
one. Consequently the maximal fixed word is finite and exhausts every possible
fixed prefix, including length zero.

Exact evaluation gives these complete parent paths:

| Source | Maximal ordinary valuation word | Length | Terminal `(a,b)` |
|---|---|---:|---|
| `w` | `(5,2,1,2,1,1,4,2,1,1,3)` | 11 | `(1417176,855893)` |
| `3w` | `(1,1,1,1,2,3,2,1,1,1,1,2,3,1,1,1,2)` | 17 | `(774840978,467958829)` |

Their total valuations are respectively23 and25. At each displayed terminal the
next valuation splits; no longer whole-domain fixed word is possible.

Absorption at1 creates no exception. The ordinary formula already has `S(1)=1`
with valuation2. An isolated member such as `n=0` may be at1 while the affine
family remains nonconstant; it must still have the same valuation as every other
member at each claimed fixed step. For example `(8,1)` has the single fixed
step `(8,1)->(6,1)`, after which the next valuations split. Padding an absorbed
member alone cannot create an additional whole-domain fixed word.

## 3. Ternary order bounds every possible lower inverse depth

After `j` lower-parent steps with total valuation `A`, its slope is

    P*3^j/2^A,

whose ternary order is exactly `j`. After `ell` child steps with total valuation
`B`, the slope is `alpha*3^ell/2^B`. Equality of the affine tails therefore forces

    ell+v3(alpha)=j.

Because `alpha` is a positive integer, every possible lower merger has

    0<=ell<=j<=11.                                      (1)

This is an all-length consequence, not a bounded-search assumption. Restricting
integrality to a ternary subprogression could admit rational `alpha` in the
original `n` coordinate and invalidate (1), which is why that broader problem
is outside this theorem.

## 4. Complete inverse enumeration and valuation bound

An ordinary inverse arrow of exact valuation `h>=1` from `(a,b)` is

    (a,b) -> (2^h*a/3,(2^h*b-1)/3).                      (2)

Keep it exactly when both coefficients are integers and the new intercept is
positive. The inherited even slope and odd intercept make the predecessor slope
even and its intercept odd. Its forward numerator is `2^h(an+b)`, whose final
factor is odd for every `n`; hence (2) has exact valuation `h` on the whole
domain. These conditions are necessary and sufficient.

For each parent endpoint `j=0,...,11`, enumerate inverse depths through `j`.
Intermediate slopes or intercepts may exceed the final bounds; they are not
discarded for that reason. At each visited depth, keep exactly the states with

    a=0 mod8, b=5 mod8, 0<a<=P, 0<b<R.                  (3)

There is a finite, proved cap on the next `h`. Let `t` be the number of further
inverse steps still allowed **after** this next step. Every such further inverse
multiplier is at least `2/3`. A final slope at most `P` requires

    a*2^(h+t)<=P*3^(t+1).                              (4)

Indeed, if the word actually takes only `s<=t` further steps, its final slope
is at least `(a*2^h/3)*(2/3)^s`, which is at least the corresponding expression
with `t`. Thus (4) remains necessary for a word stopping early. Its right side is
fixed at each node, so it bounds all `h` without an arbitrary cutoff.

Deduplicating the same affine state at the same depth loses no future branch:
the remaining depth is unchanged and future inverse choices depend only on the
state. Keeping one lower witness for a candidate reached at different endpoints
is also safe: the upper path depends only on the candidate itself.

The constructor visits **1,110 inverse nodes** and finds **43 distinct** states
satisfying (3) and a lower merger. It replays their exact forward lower words.
For each candidate it then computes the complete maximal fixed path from `3u`
and compares every state with all18 states of the parent's complete17-step upper
path, including clock zero. **There are no affine intersections.** Equality of
two affine states is equivalent to equality at every `n>=0`. This proves the
theorem.

## 5. Independent exhaustive verification

The checker reconstructs the candidate set using a different search bound.
For each exact pair of clocks `0<=ell<=j<=11`, it enumerates all inverse words
of length **exactly** `ell`. If their total valuation is `B`, their final slope is

    alpha=2^(26-A+B)*3^(j-ell).

The necessary and sufficient slope bound `alpha<=P` is therefore

    2^B*3^(j-ell)<=2^A.                                (5)

This gives a single total-valuation budget for that exact length. All words of
that length within the budget are considered, subject only to exact inverse
integrality and positivity; the constructor's local bound (4) is not reused.

The independent path routine also differs: it compares the next valuations at
`n=0` and `n=1`. Section2 proves that equality at those two points is equivalent
to whole-domain fixedness. It reconstructs the next affine coefficients from
the two resulting integer values.

This second enumeration visits **3,401 nodes** and **450 complete inverse words**.
It obtains exactly the same43 candidates, checks every stored lower witness,
and independently excludes every upper intersection. The receipt stores all43
candidate coefficients, lower witnesses, complete maximal upper words and
terminal states. It also stores a hash of the complete independent enumeration.

Additional implementation checks include215 direct integer instances of the
stored comparisons,256 small affine paths,12 partner-domain boundaries,
20 rejected invalid inputs/words, clock-zero handling, and the absorbed-member
and valuation-split cases. These finite checks supplement the completeness
proof; they do not replace its all-`n` argument.

## 6. Files, replay, and practical consequence

All mathematical code is standalone Python using only the standard library.
No repository resolver, supplied Collatz path, remote source, or external
mathematical theorem is a premise.

- [uniform_pair.py](uniform_pair.py): portable constructor, with no file writes.
- [check_uniform_pair.py](check_uniform_pair.py): independent enumeration,
  domain checks, exact certificate comparison, and source hashes.
- [uniform_pair_audit.json](uniform_pair_audit.json): full candidate receipt.

From the repository root:

```sh
python3 experiments/residual_progress/uniform_pair_scope/check_uniform_pair.py
```

The default command recomputes everything and compares the entire result with
the saved receipt. To intentionally regenerate the receipt:

```sh
python3 experiments/residual_progress/uniform_pair_scope/check_uniform_pair.py --write-receipt
```

That option writes only the receipt in this directory; replay prints its result
without writing files. The receipt pins this note and both source files.

Repeating this exact whole-guard, uniform affine W5, four-fixed-word search cannot
supply a descent. A different attempt must add a resource outside the model,
such as a valuation-dependent word, a refined domain, another partner class,
or a joint signed comparison. This conclusion does not justify abandoning those
alternatives or all single-partner reasoning. No dispatcher has been changed.
