# C013 — Independent review of the common-background theorem

**Status: independent written-proof review; one scope correction applied.**
This review covers every section of [OVERLAP_CONTROLS.md](OVERLAP_CONTROLS.md),
including the empty-background extension. It is not formal verification or
a novelty review. The reviewer is the author of the separate paired-state
note, not of the proof reviewed here.

## Reviewed version and correction

Reviewed SHA-256 of `OVERLAP_CONTROLS.md`:

```text
66d6b4eee55410ceee5b8da2e3b509f6ac29f37f8e0993aa0534e2ef17688ec8
```

The initial section 4 did not repeat the **nonconstant marker word**
assumption in its local statement. A nontrivial primitive integer cycle
does not by itself imply that its marker word is nonconstant: constant
markers can repeat a hypothetical nontrivial base block. Hence that
premise is necessary before using `e>=2` and dividing by `e-1`.
The author added it to section 4 and the candidate ledger. No formula
changed. No further error was found in the final version.

## Exact algebra and empty background

Composition of `(U,a_j)` gives the common numerator
`alpha*x+E`, with `alpha=3^(n+1)` and `E=3 C_U+u`.
Expanding the r-block composition verifies equation (1) with the stated
cut and prefix orientation. Homogenizing the monic gcd and quotients
then gives (2) exactly, including signs and repeated words.

For `h=gcd(Qbar_h,Pbar_h)`, the integral resultant identity gives
`h | R u^N`. Since `Qbar_h | D` and `gcd(D,6)=1`, division of the
power of u is valid. Dividing both numerical evaluations by h leaves
coprime integers, proving the retained factor
`h*gcd(Qbar_h/h,E)` in (3). No independence of cancellation factors
is assumed.

For empty U, `n=A_U=C_U=0`, `u=E=1` and `alpha=3`.
All extraction and numerical-gcd formulas remain valid. The bound
`C_U <= (u/2^n)(3^n-2^n)` becomes `0<=0`; (8) becomes
`1<=1<3`, so the subsequent strict inequalities remain valid too.

## Fourier and quantitative estimates

At each simple root `theta*zeta^k` of Q, direct evaluation of P gives
the displayed discrete Fourier transform. Thus the residual degree e
is exactly its nonzero Fourier-support size. Positivity ensures the
zero frequency is present, and `e=1` is equivalent to constant markers.

The displayed y has ordinary support exactly the marker mismatch set.
Combining the two terms for each unordered pair of distinct Fourier
frequencies gives the stated coefficient; diagonal terms cancel.
Therefore its Fourier support has size at most `binom(e,2)`. Parseval
and Cauchy--Schwarz yield `s*binom(e,2)>=r`, including nonprimitive
words and excluding only zero-distance rotations. No stronger linear
bound in e is inferred.

The root-modulus bound for `G_h` gives (6). Distinct roots of Q are
separated by at least `4 theta/r`; dividing P by the corresponding
factors of G and applying the monic resultant product gives (7).
The prefix bound on U proves (8). Combining these inequalities yields
both strict lines of (9), then (10) for nonconstant markers. The factors
eta, E, and R have not been omitted.

## Finiteness and the integer-cycle consequence

The constants `R_0=r^(r^2)2^(2Tr)` and `C_0=2^(3-r)/R_0` are valid
uniform weakenings of (7) and (9). For fixed r,T and denominator ceiling,
the two cases `A>=2m` and `A<2m` bound n. The stated derivative makes
the second case effective. Once n is bounded, the first line of (9)
bounds `u=2^A_U` in the large-A branch; the other branch bounds A_U
directly. This proves finiteness of the entire represented words, with
arbitrary U, rather than finiteness only at fixed U.

The logarithm estimate was checked against the imported estimate in
[C011/EXCLUSION.md, equation (1)](../two-defect-rotation-exclusion/EXCLUSION.md): here D>0 and
`A<2m` justify `B=2m` and `K=600,000,000`. This review does not reprove
Matveev or independently recheck its publication. No published numerical
integer-cycle period bound is needed by the C013 argument.

At q=1, nontriviality gives odd states at least 3, hence `A<2m`,
also for a displayed repetition. With nonconstant markers, division by
`e-1` proves (12)--(13). At `T<=Hr`, using `m=r(n+1)` and `r<=m`
gives the stated effective asymptotic
`r=Omega_H(sqrt(m/log m))`. This r is the number of copies of the
identical background; it is **not** the rotation mismatch count.
The empty-U representation makes the block-count conclusion weak,
not invalid. Neither finiteness nor this asymptotic excludes all
denominator-one exceptions.

## Concrete controls and verification scope

An independent exact calculation checked the six-marker coefficient
list, primitivity and shift-three distance two. The displayed polynomial
factorization expands correctly; its common factor with Q is `X+4`.
The irreducibility argument for coprime totals is valid by the absolute
value of a monic factor's constant term.

The actual d5 fixture was located in the cited C005 receipt. A separate
exact calculation reconstructed its 17 arrows and its values

```text
C=352383011, D=5077565, gcd(C,D)=1015513, q=5.
```

Thus the numerical-cancellation control is an actual raw odd cycle,
and its empty-U interpretation does not change its reduced denominator.
This review did not rerun the full C013 checker or all d5/7/13 fixtures;
those finite checks and their receipts remain separate evidence.
The algebra, finite controls, effective class theorem and unresolved
unrestricted mismatch-growth target are distinguished in the reviewed
note. No universal cycle record or novelty claim is made.
