#!/usr/bin/env python3
"""Exact rational checks for C011's explicit constants, not imported theorems."""
import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from math import factorial
from pathlib import Path

HERE = Path(__file__).resolve().parent


def require(test, message):
    if not test:
        raise ValueError(message)


def pair(x):
    return [x.numerator, x.denominator]


def exp_lower(x, count):
    return sum((x**j / factorial(j) for j in range(count+1)), F(0))


def report():
    # Positive Taylor terms prove exp(x) exceeds each finite sum.
    e07 = exp_lower(F(7, 10), 5)
    e11 = exp_lower(F(11, 10), 5)
    e27 = exp_lower(F(27), 32)
    require(e07 > 2 and e11 > 3, 'upper log bounds failed')
    M = 137_500_000_000
    require(e27 > 2*M, 'boundary logarithm bound failed')
    require(3*2**69 < 2**71, 'published verification endpoint failed')
    # log(2)=2*atanh(1/3); retain its first two positive terms.
    log2_lower = 2*(F(1, 3)+F(1, 81))
    require(log2_lower > F(69, 100), 'lower log bound failed')
    require(F(10, 7)**2 > 2, 'sqrt upper bound failed')
    K_upper = F(7, 5)*30**5*16*F(10, 7)*F(7, 10)*F(11, 10)
    require(K_upper == 598_752_000 and K_upper < 600_000_000,
            'Matveev coefficient bound failed')
    log_ratio_lower = F(1, 7)
    require(log_ratio_lower > F(7, 50), "exponential rate lower bound failed")
    boundary = F(M)*F(7, 50)-600_000_000*28
    derivative = F(7, 50)-F(600_000_000, M)
    require(boundary == 2_450_000_000 and derivative == F(373, 2750),
            'global monotonicity certificate failed')
    return dict(status='PASS', schema='C011-exclusion-constants-v2',
        scope='Rational constant and monotonicity checks only; no replay of Matveev or the published cycle lower bound.',
        published_inputs=dict(
            matveev='https://link.springer.com/article/10.1007/s12188-025-00293-9',
            odd_period='https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf',
            correction='https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/corrigendum.pdf',
            convergence_verification='https://link.springer.com/article/10.1007/s11227-025-07337-0'),
        certificate=dict(exp_07_lower=pair(e07), exp_11_lower=pair(e11),
            exp_27_lower=pair(e27), log2_lower=pair(log2_lower),
            log_2_over_sqrt3_lower=pair(log_ratio_lower),
            required_seed_endpoint=3*2**69, published_seed_limit_exclusive=2**71,
            sqrt2_upper=pair(F(10, 7)), matveev_coefficient_upper=pair(K_upper),
            coefficient_used=600_000_000, period_boundary=M,
            boundary_margin=pair(boundary), derivative_lower=pair(derivative)),
        source_sha256={Path(__file__).name: sha256(Path(__file__).read_bytes()).hexdigest()})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    result = report()
    path = HERE/'exclusion_constants.json'
    if args.write:
        path.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    else:
        require(json.loads(path.read_text()) == result, 'receipt mismatch')
    print(json.dumps(dict(status=result['status'], mode='write' if args.write else 'replay',
        coefficient_upper=result['certificate']['matveev_coefficient_upper'],
        boundary_margin=result['certificate']['boundary_margin'],
        derivative_lower=result['certificate']['derivative_lower'])))


if __name__ == '__main__':
    main()
