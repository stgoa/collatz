"""Exact closure and addend-aware controls for the terminal-intercept cone.

Universal implications are proved in README.md. No join census is used
as an absence proof. Finite power and local descent ranges are complete.
"""
from fractions import Fraction as F
from hashlib import sha256
import json
from math import gcd
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
HALF_LIMIT = 2**19
FINAL_HALF_LIMIT = 1714
LOCAL_LIMIT = 2**20


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def valuation(n):
    require(n != 0, "nonzero numerator")
    n = abs(n)
    return (n & -n).bit_length()-1


def intercept(word):
    c, total = 0, 0
    for letter in word:
        require(letter >= 1, "positive valuation")
        c = 3*c+2**total
        total += letter
    return c


def trace(start, additive, word):
    states = [start]
    for letter in word:
        require(states[-1] != 0 and states[-1] % 2, "nonzero odd cut")
        raw = 3*states[-1]+additive
        require(valuation(raw) == letter, "exact full valuation")
        states.append(raw >> letter)
    require(states[-1] != 0 and states[-1] % 2, "nonzero odd endpoint")
    return states


def actual_cycle(word):
    C, D = intercept(word),2**sum(word)-3**len(word)
    require(D > 0, "positive full denominator")
    common = gcd(C,D)
    additive,start = D//common,C//common
    states = trace(start,additive,word)
    require(states[-1] == start and min(states) > 0, "positive actual closure")
    return additive,states[:-1]


def change_last(word, shift):
    value = tuple(word[:-1])+(word[-1]+shift,)
    require(min(value) >= 1, "positive modified last valuation")
    return value


def join_control(J,r,h,A,B):
    A,B = tuple(A),tuple(B)
    M,N = 2**J,2**r
    require(J > r >= 1 and h > 0 and h % 2, "levels and endpoint")
    require(A and B and A[-1] > J-r and B[-1] > r, "boundary conditions")
    signed_A = trace(-h,M-1,A)
    z = signed_A[-1]
    signed_B = trace(z,N-1,B)
    require(signed_B[-1] == h, "signed join closes")
    a,b,P,T = len(A),len(B),sum(A),sum(B)
    m = a+b
    D = 2**(P+T)-3**m
    require(D > 0, "positive half gap")
    eta = F(D,2**(P+T))
    c = F(3**b,2**T)
    chi = 1-c*z/h
    CA,CB = intercept(A),intercept(B)
    require(chi == F((N-1)*CB,2**T*h) > 0, "terminal intercept fraction")
    require(F(CB,2**T) <= F(2,2**B[-1])*(F(3,2)**b-1), "terminal suffix bound")
    require(chi*h < F(3,2)**b, "terminal budget")
    u = change_last(A,-(J-r))+change_last(B,-r)
    v = A+change_last(B,J)
    d,states = actual_cycle(u+v)
    X,Y,Xprime,Z = states[0],states[a],states[m],states[m+a]
    require(Xprime == M*X+d*h and Z == N*Y-d*z, "paired actual endpoints")
    F0 = (N+1)*h*3**a-(M-N)*CA
    require(M*(N-1)*D*X == d*h*D+d*3**b*F0, "scaled divided identity")
    require((d*F0) % D == 0, "remaining-factor divisibility retains addend")
    difference = (N-1)*Y-d*z
    require(3**b*difference == 2**(T-r)*(M*(N-1)*X-d*h), "second exact boundary")
    require((F0 > 0) == (difference > 0), "residual sign matches paired order")
    Kactual = (M-1)*X+d*h
    require(3**a*Kactual == 2**(P-J+r)*((M-1)*Y-2**(J-r)*d*z), "first boundary")
    require(valuation(Kactual) == P-J+r >= a, "first exact binary order")
    require(eta*Kactual < 4*d*h, "uniform shifted state enclosure")
    require(eta*chi*2**a < 4*d*F(3,2)**b, "scaled binary-intercept budget")
    if F0 > 0:
        require(F0 < 2*N*h*3**a, "positive residual upper bound")
        require(eta*3**b < 2*N*d*h, "scaled ternary budget")
        require(eta*chi*2**b < 2*N*d, "scaled combined terminal budget")
    require(3*min(states)*D < m*d*2**(P+T), "half-clock minimum bound with addend")
    return {"J":J,"r":r,"h":h,"z":z,"A":list(A),"B":list(B),
            "u":list(u),"v":list(v),"chi":str(chi),"cone":chi >= F(1,2),
            "positive_second_difference":difference > 0,"addend":d,
            "canonical_normalized_state":str(F(X,d)),"actual_states":states,
            "signed_A":signed_A,"signed_B":signed_B,"arrows":len(states)}


def signed_controls():
    specifications = [
        (3,1,1,(2,1,1,3),(4,)),
        (3,2,3,(1,2,1,1,3),(1,1,4)),
        (4,3,1,(2,),(4,)),
        (5,2,15,(1,1,1,2,1,1,2,2,3,1,4),(1,1,1,2,3)),
        (6,5,1,(2,),(2,3,6)),
    ]
    rows = [join_control(*values) for values in specifications]
    # A genuine B-loop: after 5 -> 1 under +1, the word (2) fixes 1.
    base_c = F(9,64)
    loop_rows = []
    for repeats in (0,1,2,7):
        row = join_control(3,1,1,(2,1,1,3),(4,)+(2,)*(repeats+1))
        expected = 1-F(3,4)**repeats*base_c*5
        require(F(row["chi"]) == expected, "all-repeat affine chi identity")
        loop_rows.append(row)
    require(F(loop_rows[0]["chi"]) < F(1,2) <= F(loop_rows[2]["chi"]), "loop crosses cone")
    require({row["cone"] for row in rows} == {False,True}, "both cone sides")
    require({row["positive_second_difference"] for row in rows} == {False,True}, "both order signs")
    main = rows[-1]
    require(main["addend"] == 8111 and main["chi"] == "1643/2048", "displayed cone control")
    require(main["actual_states"] == [5,4063,5075,2917,8431,8351,8291,4123], "displayed actual cycle")
    return {"genuine_join_controls":rows,"B_loop_representatives":loop_rows,
            "loop_map":"(3*x+1)/4 fixes 1; slope 3/4",
            "scope":"These exact joins have positive interfaces. They test identities and both state-order signs, not absence of other joins."}


def symbolic_checks():
    # Integer polynomials in M,N,h,z,R,U,C, with R=3^a,U=2^P,C=C_A.
    zero = (0,)*7
    def const(n): return {zero:n} if n else {}
    def var(i):
        v = [0]*7; v[i] = 1
        return {tuple(v):1}
    def add(*values):
        out = {}
        for value in values:
            for k,c in value.items(): out[k] = out.get(k,0)+c
        return {k:c for k,c in out.items() if c}
    def scale(n,v): return {k:n*c for k,c in v.items() if n*c}
    def mul(*values):
        out = const(1)
        for v in values:
            nxt = {}
            for k,c in out.items():
                for j,d in v.items():
                    e = tuple(x+y for x,y in zip(k,j)); nxt[e] = nxt.get(e,0)+c*d
            out = {k:c for k,c in nxt.items() if c}
        return out
    M,N,h,z,R,U,C = [var(i) for i in range(7)]
    M1 = add(M,const(-1))
    diff = add(N,scale(-1,M))
    relation = add(mul(M1,C),scale(-1,mul(h,R)),scale(-1,mul(z,U)))
    Ffull = add(mul(add(mul(M,N),const(-1)),h,R),mul(diff,z,U))
    F0 = add(mul(add(N,const(1)),h,R),mul(diff,C))
    remainder = add(Ffull,scale(-1,mul(M1,F0)),mul(diff,relation))
    require(not remainder, "full identity factors before division")
    # Sign-free bounds, including negative interface, on exact affine data.
    cases = 0
    for J in range(2,9):
        for r in range(1,J):
            M,N = 2**J,2**r
            for lam in (F(1,8),F(1,2),F(7,8)):
                for t in (-lam/2,F(0),F(1,4),F(3,4)):
                    if not -lam < t < 1: continue
                    # t=c*z/h; h=1. This is abstract affine data only.
                    x = F((M-1)+M*lam*(N-1)+(N-M)*t,
                          M*(M-1)*(N-1)*(1-lam))
                    require(x > 0, "positive affine canonical point")
                    require(((M-1)*x+1)*(1-lam) < 4, "sign-free enclosure constant")
                    require(1-t > 0, "positive affine intercept fraction")
                    cases += 1
    return {"factorization_residual_terms":len(remainder),"abstract_affine_cases":cases,
            "abstract_scope":"Both signs of c*z/h; no exact signed word or cycle is asserted for abstract data."}


def gap_closure():
    power = 1
    depth = 0
    depth_indices = []
    for n in range(1,HALF_LIMIT):
        power *= 3
        exponent = power.bit_length()
        beta = 1 << exponent
        gap = beta-power
        require((gap << 24) > beta, "complete eta_min > 2^-24 range")
        d = exponent-gap.bit_length()+1
        if d > depth: depth,depth_indices = d,[n]
        elif d == depth: depth_indices.append(n)
    require(depth == 24 and depth_indices == [190537], "gap range diagnostic")
    power = 1
    worst,worst_n,worst_T = F(0),0,0
    for n in range(1,FINAL_HALF_LIMIT+1):
        power *= 3
        exponent = power.bit_length(); beta = 1 << exponent; gap = beta-power
        require(3*LOCAL_LIMIT*gap > n*beta, "complete half-clock minimum range")
        ratio = F(n*beta,3*gap)
        if ratio > worst: worst,worst_n,worst_T = ratio,n,exponent
    ceiling = (worst.numerator+worst.denominator-1)//worst.denominator
    require(ceiling == 583561 and worst_n == 1636, "minimum bound extremum")
    margin = HALF_LIMIT-(65*(172+341*20)+155)
    require(margin == 69653 and HALF_LIMIT > 65*341, "dyadic cutoff and persistent increments")
    require(65*24+155 == FINAL_HALF_LIMIT+1, "strict integer endpoint")
    require(106**5 < 2**8*35**5 and 3**5 < 2**8, "mean and logarithm comparisons")
    return {"half_lengths_checked":HALF_LIMIT-1,"eta_lower_bound":"2^-24 (strict)",
            "worst_binary_gap_depth":depth,"worst_depth_indices":depth_indices,
            "dyadic_first_margin":margin,"dyadic_increment_subtrahend":65*341,
            "final_half_lengths_checked":FINAL_HALF_LIMIT,"minimum_ceiling":ceiling,
            "minimum_extremizer_half_length":worst_n,"minimum_extremizer_half_total":worst_T,
            "local_limit":LOCAL_LIMIT}


def local_descent():
    steps = maximum = peak = 0
    maximum_seed = 0
    digest = sha256()
    for seed in range(3,LOCAL_LIMIT,2):
        x,count = seed,0
        while x >= seed:
            raw = 3*x+1
            x = raw >> valuation(raw)
            count += 1
            require(count <= 10000, "local seed must finish its exact descent")
            peak = max(peak,x)
        require(x > 0 and x % 2 and x < seed, "strict smaller odd seed")
        steps += count
        if count > maximum: maximum,maximum_seed = count,seed
        digest.update(f"{seed}:{x}:{count}\n".encode())
    return {"seeds":(LOCAL_LIMIT-2)//2,"odd_range":[3,LOCAL_LIMIT-1],
            "odd_steps":steps,"maximum_steps":maximum,"maximum_steps_seed":maximum_seed,
            "peak_odd_output":peak,"descent_sha256":digest.hexdigest(),
            "scope":"Every seed descends below itself; induction gives convergence to 1."}


def standard_fixtures():
    path = ROOT/'areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json'
    payload = json.loads(path.read_text())
    fixtures = payload['cycles']
    records = []
    for fixture in fixtures:
        d = fixture.get('d',fixture.get('q'))
        states = fixture.get('cycle',fixture.get('states'))
        require(d is not None and states, "shared fixture shape")
        letters = []
        for x,y in zip(states,states[1:]+states[:1]):
            raw = 3*x+d; a = valuation(raw)
            require(raw >> a == y and x > 0 and x % 2, "actual standard cycle")
            letters.append(a)
        require((2**sum(letters)-3**len(letters))*states[0] == d*intercept(letters), "fixture affine equation")
        records.append({"addend":d,"period":len(states),"minimum":min(states)})
    require(len(records) == 11, "all standard controls")
    return {"fixture_sha256":sha256(path.read_bytes()).hexdigest(),"cycles":records,
            "arrows":sum(v['period'] for v in records)}


def main():
    receipt = {"scope":"High-to-low terminal-intercept cone; no finite join-absence inference",
               "symbolic":symbolic_checks(),"signed_controls":signed_controls(),
               "gap_closure":gap_closure(),"local_descent":local_descent(),
               "standard_controls":standard_fixtures(),
               "checker_sha256":sha256(Path(__file__).read_bytes()).hexdigest()}
    path = HERE/'check_terminal_intercept.json'
    rendered = json.dumps(receipt,indent=2,sort_keys=True)+'\n'
    if sys.argv[1:] == ['--write-receipt']:
        path.write_text(rendered)
    else:
        require(not sys.argv[1:], "only --write-receipt is supported")
        require(path.read_text() == rendered, "generated receipt differs")
    print(json.dumps({"result":"PASS","half_gaps":HALF_LIMIT-1,
                      "minimum_comparisons":FINAL_HALF_LIMIT,
                      "local_seeds":receipt['local_descent']['seeds'],
                      "genuine_signed_joins":len(receipt['signed_controls']['genuine_join_controls']),
                      "loop_representatives":len(receipt['signed_controls']['B_loop_representatives']),
                      "standard_cycles":len(receipt['standard_controls']['cycles'])},sort_keys=True))


if __name__ == '__main__':
    main()
