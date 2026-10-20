"""Exact finite counterexample to a displayed set identity, not to Collatz.

The definitions checked are transcribed in RECURSIVE_SIEVE_AUDIT.md.
No orbit discovery or third-party code is involved.
"""
from itertools import product


def sieve_residues(depth):
    return {3+4*sum(d*3**j for j, d in enumerate(digits))
            for digits in product((0, 1), repeat=depth)}


def primed_residues(n):
    return {3+4*(sum(d*3**j for j, d in enumerate(lower))
                 + a*3**(n-1)+b*3**n)
            for lower in product((0, 1), repeat=n-1)
            for a, b in product((0, 1, 2), repeat=2)}


def removed_residues(n):
    return {3+4*(sum(d*3**j for j, d in enumerate(lower))
                 + 2*3**(n-1)+2*3**n)
            for lower in product((0, 1), repeat=n-1)}


def main():
    assert sieve_residues(2) == {3, 7, 15, 19}
    assert primed_residues(1) == set(range(3, 36, 4))
    assert removed_residues(1) == {35}
    for n in range(1, 9):
        left = sieve_residues(n+1)
        right = primed_residues(n)-removed_residues(n)
        assert left < right
        assert len(left) == 4*2**(n-1)
        assert len(right) == 8*2**(n-1)
        assert min(right-left) == 8*3**(n-1)+3
    print('PASS: displayed sieve identity fails; first witness11 at n=1, exact counts through n=8')


if __name__ == '__main__':
    main()
