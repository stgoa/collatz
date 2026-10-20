"""Exact finite audits of the parameterized halving construction."""

import argparse
import csv
import hashlib
import json
from fractions import Fraction
from pathlib import Path

import halving_return as H


HERE = Path(__file__).resolve().parent


def digest(table):
    text = "".join(f"{x},{c}\n" for x, c in sorted(table.items()))
    return hashlib.sha256(text.encode()).hexdigest()


def v2(x):
    return (x & -x).bit_length() - 1


def run():
    selected_count, complementary_count = 0, 0
    for x in range(3, 65536, 4):
        a, t = H.parameters(x)
        q = (x-1)//2
        if H.selected(x):
            data = H.coalescence(x)
            r, modulus = H.binary_residue(a)
            assert x % modulus == r
            assert 2*data["smaller"] < x
            selected_count += 1
        else:
            z = 3**(a-1)*t-1
            d = v2(z)
            assert d >= 2
            w = z//2**d
            left, right = x, q
            for _ in range(a):
                left = H.step(left)
            for _ in range(a-1):
                right = H.step(right)
            assert right == w
            assert left == (3**a*t-1)//2 == 3*2**(d-1)*w+1
            if a >= 3:
                assert H.selected(q)
            complementary_count += 1
    # Large a values test the parameterized prefix, not presumed convergence.
    large_branches = []
    for a in range(2, 129):
        for t in range(1, 33, 2):
            if t % 4 != pow(3, a, 4):
                continue
            x = 2**a*t-1
            data = H.coalescence(x)
            large_branches.append([a, t, digest(data["current"])])

    profile_cases, total_roots, removed_roots, doubled_roots = 0, 0, 0, 0
    maximum_error = Fraction(0)
    for N in range(8, 4097, 8):
        _, _, residual = H.COMPLEMENT.residual_profile(N)
        target = H.selected_profile(N)
        exact = H.selected_mass_formula(N)
        assert exact == sum(target.values())
        assert all(c == residual[x] for x, c in target.items())
        A = (3*N//2).bit_length()-1
        error = abs(Fraction(exact)-Fraction(25*N,576))
        assert error <= 6*(A-1)+Fraction(25,216)
        remaining_mass = sum(residual.values())-exact
        assert abs(Fraction(remaining_mass)-Fraction(25*N,576)) <= 6*A
        maximum_error = max(maximum_error, error)
        profile_cases += 1
        total_roots += len(residual)
        removed_roots += len(target)
        doubled_roots += sum(c == 2 for c in target.values())

    formula_cases = []
    for b in (3, 6, 12, 24, 48, 96, 192, 384, 768):
        for mantissa in (12, 14, 16, 18, 21):
            N = mantissa*2**b
            selected_mass = H.selected_mass_formula(N)
            old_mass = H.COMPLEMENT.residual_mass_formula(N)
            remaining_mass = old_mass-selected_mass
            A = (3*N//2).bit_length()-1
            assert abs(Fraction(selected_mass)-Fraction(25*N,576)) <= 6*(A-1)+Fraction(25,216)
            assert abs(Fraction(remaining_mass)-Fraction(25*N,576)) <= 6*A
            formula_cases.append(dict(N=N, selected_mass=selected_mass,
                                      remaining_mass=remaining_mass))

    conversions, stored_current = [], None
    for N in (8,16,24,72,96,384,768,6144):
        lower = H.LOCAL.FORCING.absorption_current(H.LOCAL.count(N), cap=1000)
        result = H.certify_selected(N, lower)
        assert H.divergence(result["current"]) == result["target"]
        conversions.append(dict(N=N, lower_input_rows=len(lower),
                                lower_input_sha256=digest(lower),
                                selected_mass=sum(result["target"].values()),
                                remaining_mass=sum(result["remaining"].values()),
                                selected_weight2_roots=sum(c == 2 for c in result["target"].values()),
                                output_rows=len(result["current"]),
                                output_sha256=digest(result["current"]),
                                signed_output_sha256=digest(result["signed_current"]),
                                new_prefix_rows=len(result["new_rows"]),
                                largest_prefix_length=result["largest_prefix_length"]))
        if N == 72:
            assert result["target"][79] == 2
            edges = {x:H.step(x) for x in result["current"]}
            stored_current = H.COMPLEMENT.extract_exact({79:2},edges)
        if N in (96,768):
            geo = H.LOCAL.geometry(N)
            inner = H.COMPLEMENT.extract_exact(geo["inner"], {x:H.step(x) for x in lower})
            old = H.COMPLEMENT.improve_packet(N,inner)
            upgraded = H.combine((1,old["packet_current"]),(-1,result["current"]))
            assert H.combine((1,H.divergence(upgraded)),(-1,result["remaining"])) == geo["packet"]
            conversions[-1]["full_packet_upgrade_verified"] = True

    required_ray_cases = []
    for a in (8,16,32,64,128,256,512):
        N = 12*2**(a-4)
        x = 2**a-1
        assert H.TRANSFER.residual_coefficient(N,x) == 1
        data = H.coalescence(x)
        assert data["smaller"] < N
        assert all(y >= x for y in data["left"][:-1])
        peak = 2*3**(a-1)-1
        assert data["left"][-2] == peak
        required_ray_cases.append(dict(a=a,N=N,root=x,smaller=data["smaller"],
                                       peak_before_coalescence=peak,
                                       common_state=data["left"][-1]))

    for j in range(1025):
        x = 9183+768*j
        assert H.parameters(x)[0] == 5 and H.selected(x)
    counterexample = dict(N=24,root=27,smaller=13,a=2,
                          root_two_steps=H.step(H.step(27)),
                          smaller_two_steps=H.step(H.step(13)))
    assert H.TRANSFER.residual_coefficient(24,27) == 1
    assert counterexample["root_two_steps"] == 31 != counterexample["smaller_two_steps"] == 1
    coefficient_two = H.coalescence(79)
    return dict(status="PASS",scope="Complete selected family; complementary residual remains open",
                seed_range=[3,65535,4],selected_seeds=selected_count,
                complementary_seeds=complementary_count,
                parameterized_prefix_cases=len(large_branches),
                parameterized_prefix_hash=hashlib.sha256(json.dumps(large_branches).encode()).hexdigest(),
                profile_cutoffs=dict(first=8,last=4096,step=8,count=profile_cases),
                profile_roots=total_roots,selected_roots=removed_roots,
                selected_weight2_roots=doubled_roots,
                largest_selected_mass_error=str(maximum_error),
                large_exact_formula_cases=formula_cases,
                finite_absorption_input_cap=1000,conversions=conversions,
                required_ray_excursions=required_ray_cases,
                old_packed_class_checks=1025,
                complementary_counterexample=counterexample,
                coefficient_two_example=dict(N=72,root=79,weight=2,
                    left=coefficient_two["left"],right=coefficient_two["right"],
                    current_rows=len(stored_current),current_sha256=digest(stored_current))), stored_current


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt",action="store_true")
    args = parser.parse_args()
    receipt,current = run()
    receipt_path = HERE/"halving_return_audit.json"
    table_path = HERE/"outer_79_double_current.csv"
    if args.write_receipt:
        receipt_path.write_text(json.dumps(receipt,indent=2)+"\n")
        with table_path.open("w",newline="") as output:
            writer=csv.writer(output,lineterminator="\n")
            writer.writerow(("state","current"))
            writer.writerows(sorted(current.items()))
    else:
        assert json.loads(receipt_path.read_text()) == receipt
        with table_path.open(newline="") as source:
            saved={int(row["state"]):int(row["current"]) for row in csv.DictReader(source)}
        assert saved == current
    print(f"PASS: {receipt['selected_seeds']} selected and {receipt['complementary_seeds']} "
          f"complementary seeds; {receipt['profile_cutoffs']['count']} full profiles; "
          f"{len(receipt['conversions'])} supplied-current conversions")


if __name__ == "__main__":
    main()
