"""Exact finite closure and additive-parameter controls for equal half defects.

The all-amplitude implication is proved in README.md. This certificate
checks its complete finite power/descent ranges and exact actual-cycle
identities; it never infers an unbounded exclusion from a word census.
"""
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations, product
import json
from math import gcd
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
HALF_LIMIT = 2**19
FINAL_HALF_LIMIT = 959
LOCAL_LIMIT = 2**17


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def intercept(word):
    c, total = 0, 0
    for letter in word:
        require(letter >= 1, "positive valuation")
        c = 3*c+2**total
        total += letter
    return c


def raised(word, amount):
    require(word and amount >= 1, "nonempty block and positive increase")
    return tuple(word[:-1])+(word[-1]+amount,)


def actual_cycle(word):
    c = intercept(word)
    D = 2**sum(word)-3**len(word)
    require(D > 0, "positive complete discriminant")
    common = gcd(c,D)
    additive, value = D//common,c//common
    states = []
    for letter in word:
        require(value > 0 and value % 2, "actual positive odd state")
        states.append(value)
        raw = 3*value+additive
        require((raw & -raw).bit_length()-1 == letter, "exact actual valuation")
        value = raw >> letter
    require(value == states[0], "actual cycle closure")
    return additive,states


def canonical_control(A,B,p):
    a,b = len(A),len(B)
    require(a >= 1 and b >= 1 and p >= 1, "nonempty blocks and positive amplitude")
    n = a+b
    P,R,Q,S,k = 3**a,3**b,2**sum(A),2**sum(B),2**p
    alpha,beta = P*R,k*Q*S
    require(beta > alpha, "positive half gap")
    word = tuple(A)+tuple(B)+raised(A,p)+raised(B,p)
    additive,states = actual_cycle(word)
    x,z,y,t = states[0],states[a],states[n],states[n+a]
    require(y > x, "ordered half starts")
    require((y-x) % Q == 0 and (z-t) % S == 0, "both exact quotients")
    H,J = (y-x)//Q,(z-t)//S
    require(H > 0 and J > 0 and H % 2 and J % 2, "positive odd difference quotients")
    ca,cb = intercept(A),intercept(B)
    require(Q*z == P*x+additive*ca and S*y == R*z+additive*cb, "first two block equations")
    require(k*Q*t == P*y+additive*ca and k*S*x == R*t+additive*cb, "raised block equations")
    require((beta+alpha)*J == additive*(k-1)*ca, "exact plus equation")
    require((beta-alpha)*H == additive*(k-1)*cb+(k+1)*R*S*J, "exact minus equation")
    require(2**a*ca < P*Q and 2**b*cb < R*S, "strict positive-word intercept bounds")
    require(additive*P > 2**a*S, "first consequence with actual addend retained")
    eta = F(beta-alpha,beta)
    first = F(additive*(k-1)*cb,beta)
    second = F((k+1)*R*S*J,beta)
    require(eta*H == first+second, "half-gap decomposition")
    require(first < F(additive*(k-1)*R,k*Q*2**b), "first intercept estimate")
    require(second < F(additive*k,2**(a+1)), "second intercept estimate")
    # The manuscript specializes to additive=1. This weaker scaled
    # inequality remains valid for the true additive controls.
    require(eta*H < F(additive**2*k,2**a), "scaled remaining-factor bound")
    L = min(states)
    require(3*L*(beta-alpha) < n*additive*beta, "half-clock minimum bound")
    return {"A":list(A),"B":list(B),"amplitude":p,"addend":additive,
            "boundary_states":[x,z,y,t],"H":H,"J":J,"minimum":L,
            "half_length":n,"half_total":sum(A)+sum(B)+p,
            "arrows":len(word),"states_sha256":sha256(str(states).encode()).hexdigest()}


def normalize(u,v):
    n = len(u)
    require(n == len(v) and n >= 2 and min(u+v) >= 1, "positive equal halves")
    changed = [i for i in range(n) if u[i] != v[i]]
    require(len(changed) == 2, "two changed positions")
    p = abs(v[changed[0]]-u[changed[0]])
    require(p >= 1 and all(abs(v[i]-u[i]) == p for i in changed), "equal absolute changes")
    word = tuple(u)+tuple(v)
    D = 2**sum(word)-3**len(word)
    require(D > 0, "positive normalization input")
    original_q = D//gcd(intercept(word),D)
    for cut in range(2*n):
        rotated = word[cut:]+word[:cut]
        U,V = rotated[:n],rotated[n:]
        sites = [i for i in range(n) if U[i] != V[i]]
        if sites[-1] != n-1 or any(V[i]-U[i] != p for i in sites):
            continue
        split = sites[0]+1
        A,B = U[:split],U[split:]
        require(rotated == A+B+raised(A,p)+raised(B,p), "canonical double increase")
        row = canonical_control(A,B,p)
        require(row["addend"] == original_q, "rotation preserves reduced denominator")
        return row,cut,tuple(1 if v[i] > u[i] else -1 for i in changed)
    raise RuntimeError("cyclic normalization failed")


def word_controls():
    counts,patterns = Counter(),Counter()
    digest = sha256()
    examples = {}
    words = [tuple(w) for length in range(1,4)
             for w in product(range(1,4),repeat=length)]
    for A,B,p in product(words,words,range(1,17)):
        n = len(A)+len(B)
        if 2**(sum(A)+sum(B)+p) <= 3**n:
            counts["nonpositive_gap_canonical_words"] += 1
            continue
        row = canonical_control(A,B,p)
        counts["canonical_actual_cycles"] += 1
        counts["actual_arrows"] += row["arrows"]
        examples.setdefault("canonical",row)
        digest.update((json.dumps(row,sort_keys=True)+"\n").encode())
    for n in range(2,5):
        for u in product(range(1,4),repeat=n):
            for i,j in combinations(range(n),2):
                for p in (1,2,3,5,14,20):
                    for signs in product((-1,1),repeat=2):
                        v = list(u)
                        v[i] += p*signs[0]
                        v[j] += p*signs[1]
                        if min(v) < 1:
                            continue
                        v = tuple(v)
                        if 2**(sum(u)+sum(v)) <= 3**(2*n):
                            counts["nonpositive_gap_signed_words"] += 1
                            continue
                        row,cut,pattern = normalize(u,v)
                        patterns[str(pattern)] += 1
                        counts["normalized_actual_cycles"] += 1
                        counts["actual_arrows"] += row["arrows"]
                        digest.update((str((u,v,cut))+json.dumps(row,sort_keys=True)+"\n").encode())
    for p,signs in product((13,14,31,64),product((-1,1),repeat=2)):
        u = (p+1,p+2,1,p+3)
        v = list(u)
        v[0] += p*signs[0]
        v[3] += p*signs[1]
        row,cut,pattern = normalize(u,tuple(v))
        patterns[str(pattern)] += 1
        counts["large_signed_actual_cycles"] += 1
        counts["actual_arrows"] += row["arrows"]
        examples.setdefault("large_amplitude",row)
        digest.update((str((u,v,cut))+json.dumps(row,sort_keys=True)+"\n").encode())
    require(len(patterns) == 4, "all four sign patterns checked")
    return {"counts":dict(sorted(counts.items())),"sign_patterns":dict(sorted(patterns.items())),
            "examples":examples,"cases_sha256":digest.hexdigest(),
            "ranges":{"canonical_block_lengths":[1,3],"canonical_letters":[1,3],
                      "canonical_amplitudes":[1,16],"signed_half_lengths":[2,4],
                      "signed_base_letters":[1,3],"signed_amplitudes":[1,2,3,5,14,20],
                      "large_signed_amplitudes":[13,14,31,64]},
            "scope":"Genuine reduced 3x+d cycles with d retained; no finite absence inference."}


def gap_fourteen():
    parameter = 2**14-1
    value = -63
    middle = []
    path = [value]
    for _ in range(187):
        raw = 3*value+parameter
        require(raw != 0, "signed numerator is nonzero")
        valuation = (abs(raw) & -abs(raw)).bit_length()-1
        require(valuation >= 1, "positive signed valuation")
        value = raw//2**valuation
        require(value % 2, "signed odd state")
        middle.append(valuation)
        path.append(value)
    require(value == 453291 and sum(middle) == 320, "exact signed crossing endpoint")
    require(3*value+parameter == 2**16*21, "final high-valuation crossing arrow")
    u = (1,)+tuple(middle)+(15,)
    v = (15,)+tuple(middle)+(1,)
    row,cut,signs = normalize(u,v)
    original = u+v
    plus,minus = 2**336+3**189,2**336-3**189
    C,D = intercept(original),2**672-3**378
    require(gcd(C,D) == plus and D == plus*minus, "complete plus cancellation, intact minus")
    require(row["addend"] == minus, "actual positive additive parameter retained")
    require(row["A"] == middle+[1] and row["B"] == [1], "expected canonical blocks")
    require(row["J"] == 21*minus and row["H"] == 2080893, "retained difference scale")
    return {"half_length":189,"half_total":336,"amplitude":14,
            "actual_addend":minus,"full_plus_factor":plus,"canonical_cut":cut,
            "canonical":row,"signed_parameter":parameter,"signed_start":-63,
            "signed_preterminal":453291,"signed_terminal":21,
            "signed_path_sha256":sha256(str(path).encode()).hexdigest(),
            "word_sha256":sha256(str(original).encode()).hexdigest(),
            "scope":"Actual large-crossing control; no normalization to an integer 3x+1 cycle."}


def constants():
    require(3**5 < 2**8, "alpha less than eight fifths")
    mean_margin = 2**8*129**5-388**5
    require(mean_margin > 0, "minimum-129 product estimate")
    require(F(5,8)-F(3,5) == F(1,40), "half-length coefficient")
    base = 2**19-40*(172+341*20)
    increment = 2**19-40*341
    require(base == 244608 and increment == 510648, "dyadic cutoff and monotone increments")
    require(40*24-1 == FINAL_HALF_LIMIT, "strict final half-length cutoff")
    require(99935 < LOCAL_LIMIT, "local minimum contradiction")
    return {"alpha_bound":"8/5","minimum_for_mean":129,"mean_power_margin":mean_margin,
            "length_bound_coefficient":40,"dyadic_start":19,"dyadic_base_margin":base,
            "dyadic_first_increment":increment,"half_length_strict_upper":HALF_LIMIT,
            "eta_exponent":24,"final_half_length_upper":FINAL_HALF_LIMIT,
            "local_minimum":LOCAL_LIMIT,
            "external_input":"Only EXT-1 is imported; all finite ranges below are replayed."}


def power_gaps():
    power = 1
    digest = sha256()
    worst_depth = 0
    worst_at = []
    for n in range(1,HALF_LIMIT):
        power *= 3
        total = power.bit_length()
        binary = 1 << total
        gap = binary-power
        require(gap > 0 and (gap << 24) > binary, "complete positive half-gap comparison")
        depth = total-gap.bit_length()+1
        if depth > worst_depth:
            worst_depth,worst_at = depth,[n]
        elif depth == worst_depth:
            worst_at.append(n)
        digest.update(f"{n}:{total}:{depth}\n".encode())
    require(worst_depth == 24 and worst_at == [190537], "worst gap bit depth")
    return {"range":[1,HALF_LIMIT-1],"comparisons":HALF_LIMIT-1,
            "exact_test":"(2^bit_length(3^n)-3^n)*2^24 > 2^bit_length(3^n)",
            "strict_eta_lower":"1/16777216","worst_bit_depth":worst_depth,
            "worst_bit_depth_at":worst_at,"comparison_summary_sha256":digest.hexdigest(),
            "scope":"Every comparison uses the complete integers, not truncated logarithms."}


def finite_minimum():
    power = 1
    maximum,location,total_at = F(0),0,0
    digest = sha256()
    for n in range(1,FINAL_HALF_LIMIT+1):
        power *= 3
        total = power.bit_length()
        binary = 1 << total
        gap = binary-power
        require(3*LOCAL_LIMIT*gap > n*binary, "complete half-gap minimum comparison")
        upper = F(n*binary,3*gap)
        if upper > maximum:
            maximum,location,total_at = upper,n,total
        digest.update(f"{n}:{total}:{gap:x}\n".encode())
    ceiling = -(-maximum.numerator//maximum.denominator)
    require(ceiling == 99935 and location == 918 and total_at == 1455, "exact finite maximum")
    return {"range":[1,FINAL_HALF_LIMIT],"comparisons":FINAL_HALF_LIMIT,
            "maximum_bound":str(maximum),"maximum_ceiling":ceiling,
            "maximum_at":location,"maximum_total":total_at,
            "cases_sha256":digest.hexdigest(),"local_limit":LOCAL_LIMIT}


def local_descent():
    count = total_steps = maximum = 0
    digest = sha256()
    for seed in range(3,LOCAL_LIMIT,2):
        value,steps = seed,0
        while value >= seed:
            raw = 3*value+1
            value = raw >> ((raw & -raw).bit_length()-1)
            steps += 1
            require(steps < 10000, "local seed failed to descend")
        require(value > 0 and value % 2, "positive odd descent endpoint")
        count += 1
        total_steps += steps
        maximum = max(maximum,steps)
        digest.update(f"{seed}:{steps}:{value}\n".encode())
    require(count == 65535, "complete odd local range")
    return {"range":[3,LOCAL_LIMIT-1],"odd_seeds":count,"odd_steps":total_steps,
            "maximum_steps":maximum,"cases_sha256":digest.hexdigest(),
            "scope":"Every nontrivial odd seed below the limit reaches a smaller positive odd value."}


def standard_controls():
    path = ROOT/"areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json"
    raw = path.read_bytes()
    rows = json.loads(raw)["cycles"]
    arrows = 0
    for row in rows:
        states,word,d = row["states"],row["valuations"],row["d"]
        require(d in (5,7,13,61), "shared actual addend")
        for i,letter in enumerate(word):
            value = 3*states[i]+d
            require(value == 2**letter*states[(i+1) % len(states)], "fixture arrow")
            require((value & -value).bit_length()-1 == letter, "fixture exact valuation")
            arrows += 1
    require(len(rows) == 11 and arrows == 106, "all shared fixtures")
    return {"cycles":11,"arrows":106,"fixture_sha256":sha256(raw).hexdigest()}


def main():
    require(sys.argv[1:] in ([],["--write-receipt"]), "usage: checker [--write-receipt]")
    result = {"schema":"equal-amplitude-half-defect-exclusion-v1","constants":constants(),
              "power_gaps":power_gaps(),"finite_minimum":finite_minimum(),
              "local_descent":local_descent(),"word_controls":word_controls(),
              "gap_fourteen":gap_fourteen(),"standard_controls":standard_controls(),
              "checker_sha256":sha256(Path(__file__).read_bytes()).hexdigest()}
    encoded = json.dumps(result,sort_keys=True,indent=2)+"\n"
    path = HERE/"check_equal_halves.json"
    if sys.argv[1:]:
        path.write_text(encoded)
    else:
        require(path.read_text() == encoded,"receipt mismatch; inspect before regenerating")
    print(json.dumps({"status":"passed","power_gaps":result["power_gaps"]["comparisons"],
                      "minimum_comparisons":FINAL_HALF_LIMIT,"local_seeds":65535,
                      **result["word_controls"]["counts"],"standard_cycles":11},sort_keys=True))


if __name__ == "__main__":
    main()
