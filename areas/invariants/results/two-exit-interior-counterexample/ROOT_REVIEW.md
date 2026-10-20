# V008 — Independent audit of the first-shell theorem

**Status: PASS for the corrected theorem and case table below.** This
independent audit checks the root-specific argument proposed by the main
agent. One inconsistent row in its unpublished draft was identified,
reported, and corrected during review. No historical mathematical claim
or stored finite evidence was changed.

## 1. Reviewed claim and exact hypotheses

Let b be any sequence on the nonnegative integers, with values in an
arbitrary set, satisfying all three scalar identities for every n>=0:

```
b(3n)=b(4n),
b(3n+2)=b(2n+1),
b(4n+2)=b(n).
```

Let `J_1(b)` be the distinct entire sequences among

```
b, E_0b, E_1b, T_0b, T_1b, T_2b.
```

**Theorem.** If `|J_1(b)|<=3`, then b is constant.

The proof first closes a binary family of at most four states. Its outputs
are then all equal, giving constancy directly. Cobham and V004 are not
needed for this particular small-shell claim. The arbitrary output-set
scope is valid because the argument does not count output colors.

For a genuine nonconstant Collatz invariant the theorem implies
`|J_1(b)|>=4`. This concerns only the first joint shell. It does not
exclude two-exit interiors at arbitrary depths, repeated bounded layers,
or a linear bound with any larger coefficient, and it does not complete
the active growth goal.

## 2. Six identities and the exhaustive setup

Use the six whole-sequence radix identities, in this order:

```
R0: T_0 E_0 = E_0 T_0,
R1: T_0 E_1 = E_0 T_1,
R2: T_1 E_0 = E_0 T_2,
R3: T_1 E_1 = E_1 T_0,
R4: T_2 E_0 = E_1 T_1,
R5: T_2 E_1 = E_1 T_2.
```

Composition here applies the rightmost transition first. Put `u=E_0b`.
If u=b, the root identity `E_1(E_0b)=b` gives E_1b=b too, so b is
constant by binary reading.

Otherwise u and b are distinct. If a third root state occurs, call it v;
it is distinct from both. Write

```
p=E_1b=T_2b,
q=E_0u=T_0b,
t=T_1b,
E_1u=b.
```

Thus p,q,t belong to {b,u,v}. If p,q are both in {b,u}, that two-state
set is binary-closed, regardless of t. This also covers the case when
there is no third root state. In all remaining cases p=v or q=v.

Write `A=E_0v`, `B=E_1v`. The six identities at b give the universal
relations

```
(T_0u,T_1u,T_2u)=(E_0q,E_0p,E_1t),
(T_0p,T_1p,T_2p)=(E_0t,E_1q,E_1p).                   (1)
```

When p is b or u, its already specified ternary values must also agree
with (1). This consistency is retained in the audit below.

## 3. Corrected surviving table

An ordered pair in a binary column lists the zero and one children.
All rows additionally have `E(b)=(u,p)` and `E(u)=(q,b)`.
An added state w need not be distinct from the existing ones.

| p | q | t | E(v) | Additional binary children |
|---|---|---|---|---|
| v | b | b | (b,v) | none |
| v | u | b | (w,v) | E(w)=(u,v) |
| v | v | u | (w,u) | E(w)=(v,u) |
| v | v | v | (v,v) | none |
| b | v | u | (v,u) | none |
| b | v | v | (v,v) | none |
| u | v | u | (v,v) | none |

Here w=A=E_0v wherever it is used. Together with the already closed
case p,q in {b,u}, these rows exhaust the possibilities. The following
derivations check both the table and the excluded choices of t.

### 3.1. p=v, q=b

The binary children of u are (b,b), and (1) gives
`T(u)=(u,A,E_1t)`. Identity R3 at u gives
`t=T_1b=E_1(T_0u)=E_1u=b`.
Now R2 at u gives `b=E_0v=A`, while R5 at u gives
`v=E_1v=B`. Thus `E(v)=(b,v)`.

### 3.2. p=v, q=u

Here `E(u)=(u,b)` and `T(u)=(u,A,E_1t)`. Again R3 at u forces t=b.
Identity R5 at u then gives B=v. Identity R1 at u gives E_0A=u,
and R4 at u gives E_1A=v. Therefore, with w=A,
`E(v)=(w,v)` and `E(w)=(u,v)`.

### 3.3. p=v, q=v

Here `E(u)=(v,b)` and

```
T(u)=(A,A,E_1t),
T(v)=(E_0t,B,B).
```

R0 and R1 at u give respectively
`T_0v=E_0A` and `T_0b=E_0A`. Since T_0b=v, this proves

```
E_0A=v,      E_0t=v.                                (2)
```

R3 and R4 at u give

```
E_1A=t,      B=t.                                   (3)
```

If t=b, (2) says u=v, impossible. If t=u, (2)-(3) give
`E(v)=(A,u)` and `E(A)=(v,u)`, which is the displayed w row.
If t=v, (2) gives A=v, and (3) gives B=v, yielding `E(v)=(v,v)`.

**Draft correction.** The initial proposed table retained a row
`p=q=v,t=b` with an additional state w. It used an incomplete subset of
the swaps. Applying R1 at u as above makes that row inconsistent.
Removing it preserves, and simplifies, the theorem's conclusion. The
main agent acknowledged this correction before this audit was finalized.

### 3.4. p=b, q=v

From (1), matching the ternary values of p=b gives

```
E_0t=v,      B=t,
T(u)=(A,u,E_1t).
```

Thus t=b is impossible because E_0b=u is distinct from v.
For t=v, E_0t=v gives A=v and B=t gives B=v.

For t=u, one has B=u and `T(u)=(A,u,b)`. R2 and R4 at u give
`T_1v=u` and `T_2v=b`. The one additional swap needed at v is R1:

```
T_0(E_1v)=E_0(T_1v).
```

Its left side is T_0u=A, and its right side is E_0u=v.
Hence A=v and `E(v)=(v,u)`, as claimed.

### 3.5. p=u, q=v

Equation (1), including consistency with p=u, gives

```
B=v,      E_0t=A,      E_1t=b.
```

The choice t=b is impossible because E_1b=p=u differs from b.
The choice t=v is impossible because E_1v=B=v differs from b.
Thus t=u, and E_0t=E_0u=v gives A=v. Hence `E(v)=(v,v)`.

## 4. Direct constant-output finish

The scalar identities at n=0 already give

```
b(2)=b(0),      b(2)=b(1).
```

Therefore `b(0)=b(1)=b(2)`. The outputs at zero of b and all five of
its first children are equal to this common value: their values at zero
are respectively b(0), b(0), b(1), b(0), b(1), b(2).

The binary-closed set in each table row is a subset of {b,u,v,w}, with
w=E_0v when needed. Its added state's output also equals v(0), hence
the same common value. Reading any finite binary expansion from b
remains inside this set and ends at that output. Thus b(n)=b(0) for all
n>=0. The two-state closed case has the same conclusion immediately.

For the invariant h reconstructed from b by its odd part, constant b
means constant h. No condition on a hypothetical actual bad set, finite
prefix test, or imported finite-state classification is used in this
last step.

## 5. Scope and checks

- The case split is exhaustive: after p,q in {b,u}, the only pairs are
  (v,b), (v,u), (v,v), (b,v), (u,v); all three possible t values were
  either forced, closed, or explicitly ruled out in each case.
- All equations are equations of entire sequences, with the correct
  composition order. Finite binary closure is actually exhibited.
- The generic two-exit example in [two_exit.md](two_exit.md) has three
  first-shell states and fails `b(4n+2)=b(n)` at n=1, so it is consistent
  with this root-specific theorem.
- The d=5/d=61 periodic controls fail the named d=1 root relations;
  the theorem does not purport to classify those different maps.
- The result supplies a finite-depth separation, not an asymptotic
  complexity bound. The active unbounded-ratio goal remains open.
- No historical code, finite certificate, or full Phase 6 gate changed.
  Formal verification and novelty are unclaimed.
