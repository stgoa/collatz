---
id: delayed-release-cancellation
kind: result
title: After an arbitrarily long isolation, two further negative sources cancel the three-source chain at zero positive cost
status: reviewed
claim: >
  Odd-only 3x+1 map, absorbing at 1; A_N the six-band annulus; G_D(N) the first D arrows exposed from every
  nonzero source. For every h >= 2 with lambda = 4(4/3)^h(2/3)^r in (81/32, 27/8] (r the least such that
  lambda <= 27/8; qualifying h are unbounded, and of any two consecutive h at least one qualifies), each choice
  V in {47, 155} gives an arithmetic progression of X (with v_3(X-1) = h, 2^max(h+5,10) | X, and an explicit
  size bound) such that, with N = 3X/128, the five actual sources u, v (coefficient -1 each, in the top band),
  y_1 = 64N-1 (-2), y_2 = 96N-1 (+2), y_3 = 144N-1 (+2) satisfy mu = (I - P)J for an explicit current J <= 0
  with L + 4 rows, L = h + r + 1 <= 2h + 1, ||J||_1 <= 4h + 10, all arrows in G_L(N), along the valuation word
  (1^r, 2^h, 3) from v to y_1; the three-source chain is still a complete mass-2 component of G_D(N) for every
  1 <= D <= h + 1. Each qualifying h has infinitely many realizations on N = 96 64^k. This sharpens the
  ladder bound to d*(96 64^k) >= v_3(k+2) + 4. It certifies a five-source submeasure only: the rest of A_N,
  and other sources that join the full component, are not accounted for. Two complete finite components
  show a neutral first release (N = 60555264, mass 2 -> 2) and a resolving one (N = 340131840, mass 2 -> 0).
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [unbounded-exposure-depth-necessary, disjoint-annular-recursion]
certificates: [check_legacy_replay.py]
evidence:
  - "check_release.py, release_audit.json: the legacy checker (both complete first-release components; divergence and actual source capacity for 22 parameter families with three representatives each and two required-ray representatives; the canonical-parameter dichotomy for 2 <= h <= 64; the precision refinement against the inverse oracle at D = h + 1 for 2 <= h <= 16 and six ladder cutoffs). Fails at its new path: it imports inverse_exposure_probe from ../templates/ (now ../unbounded-exposure-depth-necessary/). Passed at be73a66 as experiments/residual_progress/release/check_release.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran these steps before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a). The legacy transfer of annular-complement-outer-descent loads it by its old path. Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
  - "delayed_release_check.py, delayed_release_check.json: side-lane probe (Claude side lane, 2026-10-17): rebuilds the construction from its statement with its own A_N. Fails at its new path: it imports affine_controls and progress_measures_audit from experiments/packet_currents/negative_controls/ by repository-relative path (now ../locally-collatz-like-control-barrier/), and it imports depth_probe from its own folder (now ../unbounded-exposure-depth-necessary/). Passed at be73a66 as reviews/side_lane/delayed_release_check.py (archive/legacy-checker-run-be73a66.md, exit 0). Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
  - "chain_cancellation_scan.py, chain_cancellation_scan.json: side-lane probe for the side lane's question Q3 (2026-10-17): a bounded depth-16 backward search for zero-cost cancellations of the chain block over all admissible classes at h = 2, 3. Finite data. Fails at its new path: it imports affine_controls and progress_measures_audit from experiments/packet_currents/negative_controls/ by repository-relative path (now ../locally-collatz-like-control-barrier/), and it imports delayed_release_check from its own folder. Passed at be73a66 as reviews/side_lane/chain_cancellation_scan.py (archive/legacy-checker-run-be73a66.md, exit 0)"
  - "side_lane_review_20261017_2005.json: the main lane's reproduction (at side-lane commit f12da944) of delayed_release_check, chain_cancellation_scan and depth_probe, with source hashes and outputs; a review of those side-lane probes, not of this result"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-17
    link: delayed_release_check.py
    scope: "Finite only (side-lane feed entry 2026-10-17 19:13, VERIFIED, main 65093c4): for every qualifying h <= 12, both V and three members of each progression (16 families), the parameters, the six coefficients, the arrows u -> t -> v, the word (1^r, 2^h, 3) and (I - P)J = mu with J <= 0 and at most 2h + 5 rows; the ladder cutoff N = 96 64^89; the qualifying h <= 64; and, by full brute force, the sharpened isolation at depth h + 1 at six cutoffs. The written arguments were not re-derived, so the status stays written"
  - by: Claude review lane (Fable 5.1; directed by Santiago Armstrong)
    date: 2026-10-31
    link: REVIEW-2026-10-31-claude-review-lane.md
    scope: "Re-derived sections 2-5 (congruences, inequalities (7)-(8), the path word, (I - P)J = mu, the refinement to D <= h + 1 and the ladder bound); 66 family members, both witnesses and brute-force exposure graphs from every source at the smallest cutoffs checked with independent code; certificate passed; verdict HOLDS WITH CORRECTIONS (a typo in the claim field)"
aliases: [R16]
tags: [convergence, packet-currents, annular, exposure-depth, delayed-release, partial-current, constructive]
---

# After an arbitrarily long isolation, two further negative sources cancel the three-source chain at zero positive cost

## Statement

Odd-only clock, absorbing at 1; `A_N` the six-band annulus, `G_D(N)` as in [`unbounded-exposure-depth-necessary`](../unbounded-exposure-depth-necessary/README.md), whose three-source chain `y_1 = 64N − 1` (−2), `y_2 = 96N − 1` (+2), `y_3 = 144N − 1` (+2) is the object here.

**Parameters (§2).** For `h ≥ 2` let `r` be least with `λ = 4(4/3)^h(2/3)^r ≤ 27/8`, and keep `h` when `81/32 < λ ≤ 27/8` (two consecutive `h` cannot both fail, so qualifying `h` are unbounded). For `V ∈ {47, 155}`, the congruences (2)–(3) and the size condition (4) define an unbounded progression of `X` with `v_3(X − 1) = h` exactly and `2^max(h+5,10) | X`; put `N = 3X/128`, `v = 2^r(4^(h+1)U + 2)/3^r − 1` with `U = (X − 1)/3^h`, `t = (2v − 1)/3`, `u = (4t − 1)/3`.

**Theorem (§§3–4).** `u, t, v` lie in the top band with `A_N(u) = A_N(v) = −1`, `A_N(t) = 0`; `u → t → v` has valuations 2, 1; `v` reaches `y_1` by the valuation word `(1^r, 2^h, 3)` without meeting the annulus elsewhere. With `L = h + r + 1` and `p_0 = v, …, p_L = y_1`,

```
μ = −δ_u − δ_v − 2δ_(y_1) + 2δ_(y_2) + 2δ_(y_3),
J = −δ_u − δ_t − 2 Σ_(j<L) δ_(p_j) − 4δ_(y_1) − 2δ_(y_2),     (I − P)J = μ,
```

`J ≤ 0`, `L ≤ 2h + 1`, `|supp J| ≤ 2h + 5`, `‖J‖₁ ≤ 4h + 10`, all arrows in `G_L(N)`. Subtracting `μ` uses valid annular capacity and removes 4 units of positive mass at zero positive cost.

**Delay and ladder (§5).** For `1 ≤ D ≤ h + 1` the chain is still the complete mass-2 component of `G_D(N)`. Each qualifying `h` has infinitely many cutoffs on `N = 96·64^k`; and `d*(96·64^k) ≥ v_3(k + 2) + 4` for every `k ≥ 0`. For `h = r = 2` the ladder indices are `k ≡ 575` or `89 (mod 729)`.

**Witnesses (§6).** At `N = 60555264` (`h = 4`) the first release adds three sources of total 0 (mass stays 2 through depths 8 and 9); at `N = 340131840` (`h = 2`) the complete depth-5 component has exactly the five sources of `μ`, mass 0, and the nine-row current certifies that whole component.

The construction certifies a five-source **submeasure**; other annular sources that join the exposed component later are not accounted for, no simultaneous packing with other catalogues is claimed, and it does not prove that every positive plateau ends.

## Proof

The legacy note "Exact cancellation after an arbitrarily long initial isolation" follows, lightly edited (headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

Date: 2026-10-17. Status: written elementary partial-current construction,
with exact checks and two complete finite component witnesses. This does
not construct a current for the whole annulus. No Collatz or novelty claim
is supplied; the argument is not human peer-reviewed or formally verified.

The clock is odd-only Syracuse, absorbed at 1. We use the actual six-band
annular measure `A_N`, with `8|N`, and write `G_D(N)` for the first `D`
arrows exposed from **every** nonzero source. Historical intersections
are retained. All coefficients below are actual annular coefficients.

### 1. What changes at release

The previous [unbounded-depth theorem](../unbounded-exposure-depth-necessary/README.md)
isolates three sources, of coefficients `-2,+2,+2`, on a rising chain.
Its positive component mass is 2. A newly attached negative source need
not reduce that mass: other sources can join through the same exposed
edges. The two exact examples in Section 6 distinguish these outcomes.

Here we construct infinitely many arithmetic families in which **two
specified negative annular sources cancel that entire three-source
block**. The resulting finite current is everywhere nonpositive, hence
has zero positive cost. The families have unbounded initial isolation
depth, and each has infinitely many realizations on the required ladder
`N=96*64^k`.

This is a universal identity for a five-source **submeasure**. Extra
sources of the full exposed component are not omitted from a claimed
component certificate: a complete component claim is made only for the
finite examples in Section 6. The construction does not account for the
rest of `A_N` or prove that every positive plateau ends.

### 2. Parameters and congruences

Choose an integer `h>=2`. Let `r` be the least nonnegative integer such
that

\[
\lambda=4\left(\frac43\right)^h\left(\frac23\right)^r
\le\frac{27}{8}.
\]

Then `r>=1` and `9/4<lambda<=27/8`. Retain the values of `h` for which

\[
\boxed{\quad\frac{81}{32}<\lambda\le\frac{27}{8}.\quad}
\tag{1}
\]

There are arbitrarily large such `h`. Indeed, if a value fails (1), then
`9/4<lambda<=81/32`; at `h+1`, the same `r` gives
`3<(4/3)lambda<=27/8`, and is still the least admissible `r`.
Thus two consecutive values of `h` cannot both fail (1). This conclusion
is an exact inequality argument, not an inference from the finite list.

Choose either `V=47` or `V=155`. All modular inverses in the following
formula are taken modulo `3^(r+4)`. Set

\[
U_0\equiv
4^{-h-1}\left(3^r2^{-r}(V+1)-2\right)
\pmod{3^{r+4}},
\tag{2}
\]

and require

\[
X\equiv1+3^hU_0\pmod{3^{h+r+4}},\qquad
2^{\max(h+5,10)}\mid X.
\tag{3}
\]

The two moduli are coprime, so (3) has an unbounded positive arithmetic
progression of solutions. Since `r>=1`, (2) gives `U_0=1 modulo3`.
Consequently **every** solution has `v_3(X-1)=h` exactly.

Write

\[
c=\lambda+1-2\left(\frac23\right)^r,
\]

and impose the explicit size condition

\[
X\ge1024,\qquad
X>\frac{c+1/2}{\lambda-81/32}.
\tag{4}
\]

This excludes only finitely many members of the progression. Define

\[
N=\frac{3X}{128},\qquad U=\frac{X-1}{3^h},\qquad
v=\frac{2^r\bigl(4^{h+1}U+2\bigr)}{3^r}-1,
\tag{5}
\]

\[
t=\frac{2v-1}{3},\qquad
u=\frac{4t-1}{3}=\frac{8v-7}{9}.
\tag{6}
\]

The congruence (2) says exactly that (5) is integral and
`v=V modulo81`. Its numerator shows that `v` is odd: `U` is odd and
`4^(h+1)U+2` has 2-adic valuation 1. Thus `v=V modulo162`.
In particular, (6) consists of odd integers. More explicitly,

| `v modulo162` | `v modulo18` | `t modulo18` | `u modulo18` |
|---|---:|---:|---:|
| 47 | 11 | 13 | 5 |
| 155 | 11 | 13 | 11 |

### 3. The actual source coefficients and the exact paths

Define the three original chain sources

\[
y_1=\frac32X-1=64N-1,\quad
y_2=\frac94X-1=96N-1,\quad
y_3=\frac{27}{8}X-1=144N-1.
\]

Their coefficients are `-2,+2,+2`, because `X=1 modulo9` and their
residues are `5,17,17` modulo18. Also `S(y_1)=y_2` and `S(y_2)=y_3`,
both with exact valuation 1.

Formula (5) is equivalently `v=lambda X-c`. Conditions (1) and (4) give

\[
\frac{81}{32}X+\frac12<v<\frac{27}{8}X-1=y_3.
\tag{7}
\]

For the upper inequality, use `c=lambda+1-2(2/3)^r>1`: indeed
`lambda/[2(2/3)^r]=2(4/3)^h>1`.
From (6) and (7),

\[
y_1<72N<t<y_2<u<v<y_3.
\tag{8}
\]

Thus `u,v,t` all lie in the **top band** `(72N,144N)`. Its coefficient
row, at residues `(1,5,7,11,13,17)`, is `(0,-1,0,-1,0,2)`.
Consequently

\[
A_N(u)=A_N(v)=-1,\qquad A_N(t)=0.
\]

The two identities in (6) give exact Syracuse arrows

\[
u\mathrel{\mathop{\longrightarrow}^{2}}t
\mathrel{\mathop{\longrightarrow}^{1}}v,
\tag{9}
\]

where the labels are valuations. Exactness follows because their
successors are odd.

The path from `v` to `y_1` has the explicit forward valuation word

\[
\boxed{\quad(\underbrace{1,\ldots,1}_{r},
\underbrace{2,\ldots,2}_{h},3).\quad}
\tag{10}
\]

To check the whole word without an orbit assumption, reverse it from
`y_1`. The first inverse valuation 3 gives `4X-3=4(X-1)+1`. After `j`
inverse valuations 2, for `0<=j<=h`, the state is

\[
w_j=4\left(\frac43\right)^j(X-1)+1.
\]

It is an odd integer, since `3^h` divides `X-1`. At `j=h` this equals
`w_h=4^(h+1)U+1`. After `l` subsequent inverse valuations 1 the state is

\[
z_l=\frac{2^l(w_h+1)}{3^l}-1,\qquad0\le l\le r.
\]

Equation (2) makes all these states integral; they are odd, and `z_r=v`.
Each inverse identity therefore has the claimed exact forward valuation.
The `w_j` increase and exceed `y_3`. Each `z_l` before `v` is at least
`z_(r-1)=(3v+1)/2>y_3`, by (7). Hence the path in (10) meets the annulus
only at its two endpoints `v,y_1`, and has no collision with `u,t,y_2,y_3`.
Repeated states in this path would give a cycle followed by `y_1`, which
is impossible for a deterministic map with these endpoint heights.

### 4. A finite current of zero positive cost

Let `L=h+r+1`, and let `p_0=v,...,p_L=y_1` be the path (10). Define

\[
\mu=-\delta_u-\delta_v-2\delta_{y_1}
             +2\delta_{y_2}+2\delta_{y_3},
\]

\[
\boxed{\quad
J=-\delta_u-\delta_t-2\sum_{j=0}^{L-1}\delta_{p_j}
                 -4\delta_{y_1}-2\delta_{y_2}.
\quad}
\tag{11}
\]

Telescoping along (9), (10), and the last two chain arrows gives

\[
(I-P)J
=(-\delta_u+\delta_v)+(-2\delta_v+2\delta_{y_1})
  +(-4\delta_{y_1}+4\delta_{y_2})
  +(-2\delta_{y_2}+2\delta_{y_3})
=\mu.
\]

All five coefficients of `mu` equal the corresponding actual coefficients
of `A_N`; the five points are distinct by (8). Thus subtracting `mu`
uses valid annular source capacity and removes exactly **4 units of
positive mass**. All current coefficients are nonpositive, so
`||J^+||_1=0`. The current has `L+4` rows and `||J||_1=2L+8`.
In addition, `r<=h`: taking `r=h` gives
`4(8/9)^h<=256/81<27/8` for `h>=2`. Hence

\[
L\le2h+1,\qquad |\operatorname{supp}J|\le2h+5,
\qquad \|J\|_1\le4h+10.
\]

Every current arrow belongs to `G_L(N)`: the long path starts at the
actual source `v`, the two-arrow path starts at the actual source `u`,
and the final two origins `y_1,y_2` are sources themselves. This statement
does not require that `G_L` has only these five sources in its component.
It is a finite exact certificate for `mu`, leaving `A_N-mu` unclaimed.

No simultaneous packing with the earlier catalogues is claimed here.
Those catalogues may reuse `u` or `v`; combined source capacity would need
a separate proof. This family removes a constant amount per chosen `X`,
not a positive fraction of the whole annulus by itself.

### 5. Unbounded initial delay and required-ray realizations

#### A sharper form of the existing isolation argument

If `h>=2`, `v_3(X-1)>=h`, and
`2^max(D+4,10)` divides `X`, the existing complete-chain proof remains
valid for **every `1<=D<=h+1`**. Its sources and whole component are the
same three-source chain, of mass 2.

Here is the precision check required for this refinement. In that proof,
an extra inverse history ending at `y_k` has, after `l` steps,

\[
x-z=u(X-1),\qquad u=3^{k-l}2^{A-k}.
\]

Before the first integral auxiliary value, the old argument is unchanged.
After that arrival, the only possible denominator of `u` is a power of3.
To make the **next** auxiliary value integral at step `l`, it is enough
that the difference at step `l-1` is divisible by3. Its ternary valuation
is at least

\[
h+k-(l-1)\ge h+1-(D-1)\ge1
\]

for `k>=1` and `l<=D<=h+1`. Thus every admitted inverse remains governed
by the same positive integral auxiliary values. The proved invariant
`u>=4`, `z>0`, with its special condition at `z=5`, still excludes every
extra source. No extra divisibility of the **final** difference is needed.
The bottom and terminal closure arguments are unchanged. This checks all
incoming histories, rather than just the visible chain.

Our conditions (3) supply the binary requirement with `D=h+1`. Therefore
each family in Sections 2–4 has a complete mass-2 top component through
depth `h+1`, followed by an explicit cancellation of its three designated
sources inside exposure `L=h+r+1`. Since qualifying `h` are unbounded,
these are actual partial cancellations after arbitrarily long isolation.
The theorem does not say that the **whole** component at depth `L` has
nonpositive mass, because other annular sources may have joined by then.

This refinement also improves the previously recorded lower bound on
the whole-annulus sufficient exposure depth. With infinity allowed,

\[
\boxed{\quad d_*(96\cdot64^k)\ge v_3(k+2)+4,\qquad k\ge0.\quad}
\tag{12}
\]

Indeed, `X=2^e`, where `e=6(k+2)`, has
`h=v_3(X-1)=2+v_3(k+2)`. The exact valuation follows from the cubing
calculation below and the factorization
`(a^q-1)/(a-1)=1+a+...+a^(q-1)=q modulo3` when `a=1 modulo3`
and `3` does not divide `q`. Also `e>=max(h+5,10)` for all `k>=0`.
Thus `G_(h+1)` has the complete mass-2 component, forcing
`d_*>=h+2`. This is a lower bound on exposure required for the **whole
annulus**, and does not assert that this depth is sufficient.

#### Each congruence family occurs on the required ladder

Put `M=h+r+4`. The residue for `X` in (3) is a unit modulo `3^M`.
The integer 2 generates all units modulo `3^M`; an elementary proof is
included to avoid relying on an unstated number-theoretic input.

Write `4^(3^n)=1+3^(n+1)b_n`. At `n=0`, `b_0=1`. Cubing gives

\[
b_{n+1}=b_n+3^{n+1}b_n^2+3^{2n+1}b_n^3\equiv b_n\pmod3.
\]

Hence `v_3(4^(3^n)-1)=n+1`, so the order of4 modulo `3^M` is exactly
`3^(M-1)`. The order of2 is even, because its residue modulo3 is -1;
therefore it is `2*3^(M-1)`. This equals the number of units modulo `3^M`,
so every unit is a power of2.

Consequently there is an exponent `e_0`, unique modulo `2*3^(M-1)`,
with `2^e_0` equal to the required residue. Taking
`X=2^(e_0+j*2*3^(M-1))` for sufficiently large integers `j` satisfies
both the binary and size conditions. Since `X=1 modulo9`, its exponent
`e` is divisible by6. For `e>=12`,

\[
N=\frac{3\cdot2^e}{128}=96\cdot64^{e/6-2}.
\]

Thus every qualifying `h` has infinitely many examples on the single
required ladder. Finding a small representative exponent is not needed
for the existence proof or current identity.

For the smallest case `h=r=2`, the two residues for `X` modulo6561 are
631 and 2818. Exact exponent representatives are respectively 3462 and
546 modulo4374. The ladder indices are therefore

\[
k=575\pmod{729}\quad\hbox{or}\quad k=89\pmod{729}.
\]

In this case `v=(256X-265)/81` and `u=(2048X-2687)/729`.

### 6. Two complete first-release witnesses

The bounded inverse oracle checks **every incoming historical source**.
The receipt stores all vertices, arrows, source coefficients, caps, and
query counts. Neither example reaches 1 in its exposed component.

| Parameter | Before release | First release | Effect |
|---|---|---|---|
| `X=2583691264`, `N=60555264`, `h=4` | `G_8`: 11 vertices, 3 sources, mass2 | `G_9`: 23 vertices, 6 sources, mass2 | Three new sources have total0. |
| `X=14512291840`, `N=340131840`, `h=2` | `G_4`: 7 vertices, 3 sources, mass2 | `G_5`: 15 vertices, 5 sources, mass0 | Two new sources have total-2. |

For the neutral release, the extra sources are

\[
(4301295295,+2),\quad(5735060393,-1),\quad(6451942943,-1).
\]

The last source has forward word `(1,1,1,1,2,2,2,2,3)` to `y_1`.
The first source is its valuation-one predecessor, and the middle source
is the valuation-two predecessor of the first. A selected negative
attachment would therefore misreport the complete mass change.

For the resolving release, the complete five-source table is

| Source | Coefficient |
|---:|---:|
| 21768437759 | -2 |
| 32652656639 | +2 |
| 40769785577 | -1 |
| 45866008775 | -1 |
| 48978984959 | +2 |

Here (11) certifies **the entire exposed top component at depth5**,
because the complete oracle source list equals `mu`. The current has
nine rows, norm18, and positive cost0. This is not a certificate for the
other components of the annulus.

The new source `u` reaches `y_1` in seven arrows, even though the entire
current is already in `G_5`: `v` is itself a source, so its outgoing
history is exposed independently. This is why an ordinary single-path
length must not be substituted for the historical graph's exposure clock.

### 7. Reproduction and remaining question

```sh
python3 experiments/residual_progress/release/check_release.py
```

The checker regenerates both complete component witnesses, verifies the
exact divergence and actual source capacities for 22 parameter families
and three representatives per family, and checks two actual required-ray
representatives. Its receipt stores compact hashes for the regenerable
family currents and full rows for the resolving component certificate.
It also checks the canonical-parameter dichotomy for `2<=h<=64`; the
unbounded conclusion follows from the inequality proof, not that scan.
The precision refinement is checked against the complete inverse oracle
at `D=h+1`, for every `2<=h<=16` and both possible next nonzero ternary
digits, as well as six explicit required-ladder cutoffs.

The first-release examples use caps of 2,000 vertices and 100,000 inverse
reachability queries. A cap is unresolved and cannot produce a completed
component claim. The default verification asserts both searches finish.

**Open:** extend this mechanism to control every remaining positive
component, or prove that its recursive use closes a specified residual
family with a decreasing parameter. The isolated block can be canceled
after arbitrarily long delay in these explicit families; a universal
annular completion or termination theorem does not follow.

## Certificates

No certificate ran at this path before the B18 replay revival; the legacy checker and both side-lane probes import modules from folders that moved, so all were evidence only until the B18 replay revival (below). The commands in the legacy text name `experiments/residual_progress/release/`.

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B18-replay-revival migration; standard library) replays the unmodified legacy checks `check_release.py`, `delayed_release_check.py` in a temporary copy of the legacy layout built by `tools/legacy_replay.py`, requiring exit 0 and every file unchanged (about 41 s). It checks finite steps only; the status is unchanged.

## Remarks

- **Side-lane finite data.** Coverage: the two families cover `2` of the `2·3^(r+3)` admissible unit classes of `U` modulo `3^(r+4)`, a fraction `1/3^(r+3)` (feed 2026-10-17 19:13, also proved in [`short-delay-all-phase-obstruction`](../short-delay-all-phase-obstruction/README.md)). Q3 (`chain_cancellation_scan.py`, feed 19:22): a depth-16 backward search finds sources of total coefficient `≤ −2` entering the chain in every representative of 11 of 486 classes at `h = 2` (20 of 1458 at `h = 3`), in some representatives of 34 (24), and in none of 441 (1414), and three further depth-7 classes at `h = 2` (`U ≡ 124, 610, 691`). The main lane reproduced these receipts and scoped them: absence within depth 16 does not exclude a deeper zero-cost attachment, and does not mean the inverse tree never re-enters the annulus.
- The extra negative sources may lie **above** the positive source; a backward rule restricted to smaller ancestors misses them. Related packing identities are [`release-source-packing`](../release-source-packing/README.md).
- The transfer of these families to exact outer-seed descents is in [`annular-complement-outer-descent`](../annular-complement-outer-descent/README.md); the all-phase extension of the short delay fails ([`short-delay-all-phase-obstruction`](../short-delay-all-phase-obstruction/README.md)).
- Novelty undetermined (none claimed).

## History

- Migrated from `experiments/residual_progress/release/DELAYED_RELEASE.md` (legacy ID R16; the ledger's R16 also covers [`release-source-packing`](../release-source-packing/README.md), alias R16-b) at commit `be73a66`, by the B09 migration (Claude, Opus 5.5). Note, checker and receipt moved byte-identical, with the side-lane probes `reviews/side_lane/delayed_release_check.*`, `chain_cancellation_scan.*` and the main lane's reproduction receipt `experiments/residual_progress/side_lane_review_20261017_2005.json`. Legacy status: "written universal partial-current families, with complete finite component examples. Full component resolution at every parameter and complete annular certificates remain open".
- Main lane (ChatGPT, Codex), 2026-10-17, from commit `2be37b7`. Its "independent model reviews" of the release theorem and precision refinement were the main lane's own agents. The side lane's finite check is recorded under `reviewed_by`.
- 2026-10-31: reviewed by the Claude review lane (Fable 5.1; directed by Santiago Armstrong); status raised to reviewed. Correction: in the `claim` field, "V in (47, 155)" (which reads as an interval) became "V in {47, 155}", the two values used by the Statement and the proof. Review: [`REVIEW-2026-10-31-claude-review-lane.md`](REVIEW-2026-10-31-claude-review-lane.md).
