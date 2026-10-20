# C010 literature and claim scope

The rational-cycle affine formula, legality and common denominator are
established background. The primary author copy of
[Halbeisen–Hungerbühler, Optimal bounds for the length of rational Collatz cycles](https://people.math.ethz.ch/~halorenz/publications/pdf/collatz.pdf)
was read at Lemmas1–2 and equation4. It uses shortcut parity words;
C010 uses positive odd-only valuation words. The C004 mechanical
spacing construction and R71 denominator theorem are already persisted
inputs. C010 adds the complete-seam identity to that construction.

[Aliyev, On integer linear combinations of terms of rational cycles for the generalized 3x+1 problem](https://arxiv.org/html/2307.11990v5)
was inspected at Sections2–3. Theorem3.1 obtains integer linear
combinations under an explicit denominator divisibility premise;
Corollaries3.4–3.5 propagate a common denominator and integrality
around the cycle. These statements are relevant background for
distinguishing integrality of selected combinations from integrality
of the whole vector. They supply no missing positivity or q1 exclusion
here. The paper's q denotes the affine divisor, unlike our reduced
denominator q. No theorem from it is a new premise of C010.

[Knight's publisher preview](https://www.sciencedirect.com/science/article/abs/pii/S0012365X25004200)
was accessible in this pass. Its high-cycle nonintegrality result
concerns the cycle maximizing the minimum at fixed shortcut totals,
represented by a Christoffel word. That supports retaining the existing
scope comparison: a high cycle is not any cycle with a large minimum.
Only the preview was inspected; no full-paper or Lean replay is claimed.

The inverse `I+E+...+E^(m-1)` is proved directly from `E^m=2I`.
No integer-programming impossibility theorem is imported. The rational
controls rule out only the explicitly stated relaxation using local
spacing lower bounds, including its nonnegative linear combinations.
Exact integer cutting planes can exclude individual fractional profiles;
a uniform argument over all profiles remains missing.

No novelty or improvement over published cycle records is claimed.
The [C001 primary audit](../../results/repeated-block-cancellation-bound/LITERATURE.md) retains the precise
Simons–de Weger and Hercher scopes and clock conventions. C010's gap
count is not their shortcut local-minimum count, and this batch excludes
no new universal integer-cycle class.
