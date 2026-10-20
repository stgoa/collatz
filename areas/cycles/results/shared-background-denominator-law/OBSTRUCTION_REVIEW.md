# C013 — Independent review of the paired-run height obstruction

**Reviewer:** the overlap-controls sub-agent, independently of the author
of OVERLAP_THEORY.md. **Outcome:** no mathematical error found in the
reviewed proof. This is an independent written review and exact finite
reconstruction, not formal verification or a novelty assessment.

Reviewed source:

```text
experiments/cycle_spectrum/C013/OVERLAP_THEORY.md
SHA-256 43c44f9ef6a2d9f42b1ce956a70d69db5f7c5b9582baf81b87c554aadb0605f9
```

## Proof checks

1. In a primitive raw odd cycle, every nonidentity phase difference is
   nonzero and even. The agreeing-run identity therefore forces the
   exact multipliers `2^(E+1)k` and `2*3^t*k`, including the empty-run
   convention. The diameter bound and the strict conversion through
   `H/L<2^(B+1)` are correct. No order or q<=L assumption is used.
2. In the near-critical family, `u+v=b-1` and `u+2v=a-4`. Thus the
   displayed totals are exactly m=3b, A=3a, and the U slope is
   `lambda=3^(b-1)/2^(a-4)=(16/3)r`. The intercept is exactly
   `beta=lambda+1-2*(3/4)^v`. Composing marker 3,4,5 and the three U
   blocks yields the stated affine equations and
   `T=(r^2/2)b_3+(r/2)b_4+b_5` without approximation.
3. Unique markers establish primitivity and minimum nonzero rotation
   distance three. Positive D supplies actual odd integer cycles at
   the reduced denominator q. None of this makes their fractional
   additive-one states an integer Collatz cycle.
4. For r>=1/2 and u,v>=1, `beta>=13/6`, `b_5>=9/4`, and
   `X0>9/[4(1-r^3)]`. The bounds X1>=X0 and X2>=X0/2 follow directly
   from the affine equations. A one-run increases; a two-run moves
   monotonically toward 1, possibly in either direction. Since the
   entire U block increases its positive input, the minimum of each
   marker-plus-U block is its state immediately after the marker.
   This justifies the minimum formula and both strict finite bounds.
5. The limits `delta_0 X0->40/9` and
   `(X1/X0,X2/X0)->(2,2)` give the three post-marker leading
   constants `(5/3,5/3,5/6)`. Thus the third is eventually smallest,
   `delta_0 L/q->5/6`, and the largest one-run peak gives
   `(H/L)/(3/2)^u->2`. The asserted positive linear height rate
   follows with the raw period m=3b.
6. For an upper convergent let x=b0*delta00, with 0<x<log 2, and
   k=ceil(x^(-1/2)). Then `1<=k^2*x<(1+sqrt(log 2))^2<4`.
   Also `k*delta00 < (sqrt(log 2)+log 2)/b0`, so the rescaled drift
   tends to zero. This proves the stated linear normalized minimum
   without assuming bounded continued-fraction coefficients or
   coprimality of the rescaled totals.
7. The matching U run has b-1 agreeing positions. Applying the run
   law to it and using the rational diameter from the preceding
   asymptotics gives
   `liminf log(q)/b >= log 3-(2-log_2 3)*log(3/2)>0`.
   Hence these are growing-denominator controls. They refute the
   specified height conversions but leave fixed-q height bounds and
   the unrestricted denominator-complexity goal open.

## Separate exact reconstruction

The reviewer reconstructed the full rotated-intercept cycle with
integer arithmetic and evaluated the three affine states with exact
rational arithmetic. All arrows, oddness, distinct states, closure,
the post-marker minimum formula and both finite inequalities passed.

| (a,b) | (u,v) | Raw period | Bits in q | Dyadic height B | L>q |
| --- | --- | ---: | ---: | ---: | --- |
| (27,17) | (9,7) | 51 | 78 | 6 | yes |
| (65,41) | (19,21) | 123 | 191 | 12 | yes |
| (485,306) | (129,176) | 918 | 1447 | 76 | yes |

Here q was computed as `D/gcd(C,D)`, states as the exact raw arrows
from `C/gcd(C,D)`, and B as `floor(log_2(H/L))` using integer
comparisons. The finite reconstruction confirms those declared cases;
the infinite and asymptotic assertions depend on the written proof.

No proof correction was required during this review. In particular,
the possibility of an increasing finite two-run does not invalidate
the minimum argument, which uses the whole U endpoint as well.
