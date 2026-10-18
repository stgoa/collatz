#!/usr/bin/env python3
"""Exact focused checks for the C.1a arithmetic audit and scoped C.2a attempt."""
import argparse
from collections import Counter
from fractions import Fraction
from functools import lru_cache
import hashlib
import json
from math import factorial
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "audit_checks.json"


def need(condition, message):
    if not condition:
        raise ValueError(message)


def raw(n):
    need(type(n) is int and n > 0 and n % 2 == 1, "invalid odd state")
    value = 3*n+1
    divisor = value & -value
    return value//divisor, divisor.bit_length()-1


def inverse_data(word):
    """Inverse-order word: 2^A*root = 3^D*source + c."""
    A, c = 0, 0
    for i, a in enumerate(word):
        need(type(a) is int and a >= 1, "invalid valuation")
        c = 2**a*c+3**i
        A += a
    return len(word), A, c


def inverse_path(root, word):
    x, backward = root, [root]
    for a in word:
        numerator = 2**a*x-1
        need(numerator > 0 and numerator % 3 == 0, "inadmissible inverse word")
        x = numerator//3
        need(x % 2 == 1, "even inverse state")
        backward.append(x)
    y = x
    for a in reversed(word):
        y, actual = raw(y)
        need(actual == a, "inverse valuation was not exact")
    need(y == root, "inverse path has wrong root")
    D, A, c = inverse_data(word)
    need(2**A*root == 3**D*x+c, "affine word identity failed")
    return x, backward


def ceil_log_three(t):
    need(type(t) is int and t >= 0, "invalid logarithm exponent")
    return (3**t-1).bit_length()


def barrier(b, s):
    return 2*b+ceil_log_three(max(0, s-b))-ceil_log_three(max(0, b-s))


def block_end(b, word):
    lower, upper = b-3*b//5, b+3*b//5
    need(len(word) >= lower, "word ends before lower endpoint")
    total = sum(word[:lower])
    need(total < barrier(b, lower), "lower endpoint did not miss")
    for s in range(lower+1, min(upper, len(word))+1):
        total += word[s-1]
        if total >= barrier(b, s):
            return s, total-barrier(b, s)
    raise ValueError("supplied word has no admitted block crossing")


def constants():
    pairs = [
        (2013**5*100**3, 2000**5*101**3, ">"),
        (2013*200**6, 2000*201**6, "<"),
        (2013**100, 2*2000**100, "<"),
        (3**8, 2**13, "<"),
        (4**5, 4*3**5, ">"),
        (32*16807**40, 18432**40, "<"),
        (3**200, 2**395, "<"),
    ]
    rows = []
    for left, right, sign in pairs:
        need(left < right if sign == "<" else left > right, "constant comparison failed")
        rows.append(dict(left=left, right=right, relation=sign))
    return dict(comparisons=rows, central_loss_constant=8*factorial(35)*576**35)


def central_histories():
    rows = []
    for b0, n in ((325, 1), (325, 3), (500, 2)):
        scales, blocks = [b0], []
        for j in range(n):
            b = scales[-1]
            word = [1]+[2]*(b-2)+[3]
            if j % 2:
                word[b//2] -= 1
                word[b//2+1] += 1
            end, overshoot = block_end(b, word)
            need(end == b and overshoot == 0, "central reference block failed")
            blocks.append(tuple(word))
            scales.append(b+b//100)
        word = tuple(a for block in blocks for a in block)
        D, A, c = inverse_data(word)
        modulus = 3**D
        root = c*pow(2**A, -1, modulus) % modulus
        if root % 2 == 0:
            root += modulus
        root += 2*modulus*max(0, (16**b0-root+2*modulus-1)//(2*modulus))
        need(root >= 16**b0, "root height condition failed")
        source, path = inverse_path(root, word)
        position, parent = 0, root
        composed_weight, composed_offset = Fraction(1), Fraction(0)
        for j, block in enumerate(blocks):
            b = scales[j]
            end, overshoot = block_end(b, word[position:])
            need(end == len(block), "full word did not determine block division")
            position += end
            child = path[position]
            d, a, offset = inverse_data(block)
            weight, beta = Fraction(3**d, 2**a), Fraction(offset, 2**a)
            need(parent == weight*child+beta, "block composition failed")
            need(0 <= beta < 2**b, "block offset bound failed")
            need(child >= 16**(b//100)*parent, "block growth bound failed")
            need(child >= 16**scales[j+1], "next block height not maintained")
            need(weight <= Fraction(1, 16**(b//100)), "block weight bound failed")
            composed_offset += composed_weight*beta
            composed_weight *= weight
            parent = child
        need(all(x > 1 for x in path), "histogram path encountered absorber")
        need(composed_offset == Fraction(c, 2**A) and
             composed_weight == Fraction(3**D, 2**A), "complete offset identity failed")
        need(composed_offset < 2**(b0+1), "root-uniform complete offset bound failed")
        need(composed_weight <= Fraction(1, 16**(scales[-1]-b0)),
             "telescoped weight bound failed")
        rows.append(dict(initial_scale=b0, generations=n, scales=scales,
                         depth=D, valuation_sum=A, root_bits=root.bit_length(),
                         source_bits=source.bit_length(), all_states_above_one=True,
                         path_sha256=hashlib.sha256(
                             json.dumps(path, separators=(",", ":")).encode()).hexdigest()))
    return rows


def fixed_group_checks():
    words = [(20-a, a) for a in (1, 7, 13, 19)]
    rows, fiber_checks = [], 0
    for root in (17, 35, 197, 180017):
        sources, offsets = [], []
        for word in words:
            source, _ = inverse_path(root, word)
            D, A, c = inverse_data(word)
            need((D, A) == (2, 20), "histories left their fixed group")
            sources.append(source)
            offsets.append(Fraction(c, 2**A))
        need(len(set(sources)) == len(words), "fixed-depth deterministic injectivity failed")
        W = Fraction(9, 2**20)
        width = max(offsets)-min(offsets)
        need((max(sources)-min(sources))*W == width, "source interval width depends on root")
        endpoint_needed = False
        for q in (0, 1, 2, 5, 12):
            counts = Counter(x % 3**q for x in sources)
            for count in counts.values():
                mass = 3**q*W*count
                need(mass <= width+3**q*W, "residue histogram endpoint bound failed")
                endpoint_needed |= mass > width
                fiber_checks += 1
        need(endpoint_needed, "test did not exercise required endpoint term")
        rows.append(dict(root=root, sources=sources, depth=2, valuation_sum=20,
                         weighted_interval_width=str(width), endpoint_term_necessary=True))
    a, _ = inverse_path(1, (4,))
    b, _ = inverse_path(1, (2, 4))
    need(a == b == 5, "different-depth collision control failed")
    return dict(rows=rows, residue_fibers=fiber_checks,
                different_depth_control=dict(root=1, source=5, inverse_words=[[4], [2, 4]],
                    scope="raw control outside histogram root-height domain; not globally injective"))


@lru_cache(None)
def reference_probability(q):
    """Exact finite Syracuse offset law; geometric valuations grouped by period."""
    if q == 0:
        return (Fraction(1),)
    modulus, period = 3**q, 2*3**(q-1)
    out = [Fraction(0) for _ in range(modulus)]
    for a in range(1, period+1):
        probability = Fraction(2**(period-a), 2**period-1)
        for z, mass in enumerate(reference_probability(q-1)):
            y = (3*z+1)*pow(2, -a, modulus) % modulus
            out[y] += probability*mass
    need(sum(out) == 1, "reference probability lost mass")
    return tuple(out)


def rho(q):
    return [Fraction(2, 3)*3**q*p for p in reference_probability(q)]


def average_abs(values):
    return sum(abs(x) for x in values)/len(values)


def transfer(word, values, t):
    D, A, c = inverse_data(word)
    need(len(values) == 3**t, "transfer domain length mismatch")
    modulus = 3**(t+D)
    out, seen = [Fraction(0) for _ in range(modulus)], set()
    for z, value in enumerate(values):
        y = (3**D*z+c)*pow(2**A, -1, modulus) % modulus
        need(y not in seen, "affine residue map is not injective")
        seen.add(y)
        out[y] = Fraction(3**D, 2**A)*value
    need(average_abs(out) == Fraction(1, 2**A)*average_abs(values),
         "transfer absolute-average factor failed")
    return out


def reference_checks():
    marginal_checks = 0
    for q in range(1, 5):
        values = rho(q)
        need(sum(values)/len(values) == Fraction(2, 3), "rho mean failed")
        need(all(values[y] == 0 for y in range(0, 3**q, 3)), "rho unit support failed")
        for m in range(1, q+1):
            coarse = [sum(values[y] for y in range(r, 3**q, 3**m))/3**(q-m)
                      for r in range(3**m)]
            need(coarse == rho(m), "finite reference marginal compatibility failed")
            marginal_checks += 1
    signed_checks = 0
    for word in ((1,), (2,), (1, 2), (3, 1)):
        for t in (1, 2):
            transfer(word, [Fraction((-1)**z*(z+1), z+2) for z in range(3**t)], t)
            signed_checks += 1
    V, Q, k, ell = ((1, 1), (1, 2), (2,)), 4, 1, 2
    p = sum(Fraction(1, 2**sum(w)) for w in V)
    exact_sum = [Fraction(0) for _ in range(3**Q)]
    lifted_sum = exact_sum.copy()
    replacement = Fraction(0)
    for word in V:
        t = Q-len(word)
        fine = rho(t)
        coarse = [rho(k)[z % 3**k] for z in range(3**t)]
        exact_sum = [a+b for a, b in zip(exact_sum, transfer(word, fine, t))]
        lifted_sum = [a+b for a, b in zip(lifted_sum, transfer(word, coarse, t))]
        replacement += Fraction(1, 2**sum(word))*average_abs([a-b for a, b in zip(fine, coarse)])
    complement = [a-b for a, b in zip(rho(Q), exact_sum)]
    need(min(complement) >= 0, "prefix code omitted complement has negative mass")
    need(average_abs(complement) == Fraction(2, 3)*(1-p), "omitted prefix mass failed")
    final_coarse = [rho(ell)[z % 3**ell] for z in range(3**Q)]
    lhs = average_abs([a-b for a, b in zip(lifted_sum, final_coarse)])
    final_error = average_abs([a-b for a, b in zip(rho(Q), final_coarse)])
    rhs = replacement+Fraction(2, 3)*(1-p)+final_error
    need(lhs <= rhs, "prefix replacement triangle inequality failed")
    return dict(reference_depths=[1, 2, 3, 4], marginal_checks=marginal_checks,
                signed_transfer_checks=signed_checks, prefix_code=[list(w) for w in V],
                prefix_mass=str(p), omitted_average=str(average_abs(complement)),
                variation_lhs=str(lhs), variation_rhs=str(rhs),
                scope="exact finite laws and transfer identities; no Tao mixing-rate verification")


def odd_residue_count(X, modulus, residue):
    return sum(n % modulus == residue for n in range(1, X+1, 2))


def c2_checks():
    level_rows, identities = [], 0
    for j in (1, 2):
        source_modulus, target_modulus = 3**j, 3**(j+1)
        period = 2*3**j
        table = [[(3*u+1)*pow(2, -a, target_modulus) % target_modulus
                  for a in range(1, period+1)] for u in range(source_modulus)]
        need(all((3*u+1)*pow(2, -(a+period), target_modulus) % target_modulus == table[u][a-1]
                 for u in range(source_modulus) for a in range(1, period+1)), "residue period failed")
        for A in (2, 4, 6):
            for X in (13, 64, 255):
                for u in range(source_modulus):
                    branches = sum(odd_residue_count((3*X+1)//2**a, target_modulus,
                        (3*u+1)*pow(2, -a, target_modulus) % target_modulus)
                        for a in range(1, A+1))
                    tail = sum(n % source_modulus == u and (3*n+1) % 2**(A+1) == 0
                               for n in range(1, X+1, 2))
                    need(branches+tail == odd_residue_count(X, source_modulus, u),
                         "complete inverse-branch/tail identity failed")
                    need(Fraction(tail) <= Fraction(X, source_modulus*2**(A+1))+1,
                         "CRT tail capacity failed")
                    identities += 1
        for A in (2, 6, 18):
            branches = sum(Fraction(3, 2*target_modulus*2**a) for a in range(1, A+1))
            tail = Fraction(1, source_modulus*2**(A+1))
            need(branches+tail == Fraction(1, 2*source_modulus), "positive density mode lost mass")
        level_rows.append(dict(level=j, residue_period=period, table=table))
    controls = []
    for d in (5, 7, 13, 61):
        for m in (1, 3, 5, 17):
            x = d*m
            value = 3*x+d
            nxt = value//(value & -value)
            baseline, _ = raw(m)
            need(nxt == d*baseline and nxt % d == 0 and nxt != 1,
                 "multiples-of-d control failed")
        need((4*d)//((4*d) & -(4*d)) == d, "d fixed point failed")
        controls.append(dict(d=d, fixed_point=d, sampled_odd_multipliers=[1, 3, 5, 17]))
    return dict(levels=level_rows, exact_branch_tail_checks=identities,
                density_mode_checks=6, multiples_controls=controls,
                scope="arithmetic bijection checked on all raw odd states; not an actual-B counterexample")


def rejection_checks():
    cases = {
        "zero valuation": lambda: inverse_data((0,)),
        "boolean valuation": lambda: inverse_data((True,)),
        "inadmissible inverse": lambda: inverse_path(3, (1,)),
        "missing lower endpoint": lambda: block_end(325, (1,)),
        "no block crossing": lambda: block_end(325, (1,)*520),
        "wrong transfer domain": lambda: transfer((1,), [Fraction(1)], 1),
    }
    for label, action in cases.items():
        try:
            action()
        except ValueError:
            continue
        raise ValueError(f"invalid case accepted: {label}")
    return list(cases)


def audit():
    return dict(schema="phase6-linear-density-ingredient-audit-v1", status="PASS",
                constants=constants(), central_histories=central_histories(),
                fixed_group_histogram=fixed_group_checks(), reference_transfer=reference_checks(),
                c2a_residue_attempt=c2_checks(), rejections=rejection_checks(),
                scope=("Finite exact arithmetic checks of written histogram and transfer identities. "
                       "No independent Tao theorem proof, full density-theorem audit, Lean replay, "
                       "or actual-B upper transport estimate is certified by this receipt."))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", type=Path)
    args = parser.parse_args()
    need(not sys.flags.optimize, "run without -O")
    result = audit()
    output = json.dumps(result, indent=2)+"\n"
    if args.write_receipt:
        args.write_receipt.write_text(output)
    else:
        need(result == json.loads(RECEIPT.read_text()), "audit receipt mismatch")
    print(output, end="")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, OSError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        sys.exit(1)
