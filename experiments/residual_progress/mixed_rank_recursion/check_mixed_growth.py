"""Bounded exact replay for the growing mixed-rank block and its guard."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import mixed_growth as M

HERE=Path(__file__).resolve().parent


def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),
                                    default=lambda x: {'numerator':x.numerator,'denominator':x.denominator}).encode()).hexdigest()


def audit():
    assert M.A==3**12 and M.DEN==2**19 and M.DIFFERENCE==M.A-M.DEN
    assert M.RESIDUE == -M.B*pow(M.DIFFERENCE,-1,2**26)%2**26
    # Uniform exact lower-request comparison, including the integer offset.
    assert 24*M.DEN-9*M.A > 9*M.B+5*M.DEN > 0
    first_macro=M.macro(M.RESIDUE)
    macros=[]
    for index in range(16):
        w=M.RESIDUE+2**26*index
        data=M.macro(w)
        macros.append([w,data['leading'],len(data['current']),
                       digest(data['current']),digest(data['coefficients'])])

    repetitions=[];stored=[]
    for count in (1,2,3,4,8,16):
        for index in (0,1):
            f=M.family(count,index)
            direct=M.repeated_plan(f['seed'],count)
            if count<=4:
                expanded=M.macro(f['seed'])
                for w in f['states'][1:-1]:
                    expanded=M.substitute_leading(expanded,M.macro(w))
                assert expanded['current']==direct['current']
                assert expanded['coefficients']==direct['coefficients']
                assert expanded['leading']==direct['leading']
            q,n=3*f['seed'],3*direct['leading']
            x=q
            for _ in range(12*count+1):x=M.NORMAL.step(x)
            assert x==M.NORMAL.step(n)
            x=q
            for _ in range(12*count):x=M.NORMAL.normal_form(M.NORMAL.step(x))
            assert x==n
            repetitions.append(dict(count=count,index=index,seed=f['seed'],
                                    leading=direct['leading'],rows=len(direct['current']),
                                    explicit_macro_substitution=count<=4,
                                    requests=len(direct['coefficients']),
                                    current_hash=digest(direct['current']),
                                    coefficient_hash=digest(direct['coefficients'])))
            if index==0 and count in (1,2):stored.append(direct)

    arithmetic=[]
    for count in (1,2,4,8,16,32,64,128,256):
        for index in (0,1,2**128):
            f=M.family(count,index);maximum=M.maximum(f['seed'])
            assert maximum['count']>=count
            start=f['seed']
            for j,w in enumerate(f['states']):
                assert (M.DIFFERENCE*w+M.B)*M.DEN**j == M.A**j*(M.DIFFERENCE*start+M.B)
                if j<count:
                    p=M.parameters(w)
                    assert p['guard_valuation']>=26
            arithmetic.append(dict(count=count,index=index,seed=start,
                                   bit_length=start.bit_length(),maximum=maximum['count'],
                                   exit_valuation=maximum['exit_valuation'],
                                   states_hash=digest(f['states'])))

    exits=[]
    for order in range(26,26+19*4):
        # Exact v2(D*w+B)=order, including the next binary bit.
        modulus=2**(order+1)
        w=(2**order-M.B)*pow(M.DIFFERENCE,-1,modulus)%modulus
        actual=M.maximum(w)
        assert actual['valuation']==order and actual['count']==1+(order-26)//19
        assert actual['exit_valuation']==order-19*actual['count']
        exits.append([order,w,actual['count'],actual['exit_valuation']])
    assert set(x[3] for x in exits)==set(range(7,26))

    # The convenient H_n forward transport is restricted, not every defect.
    n,q=1371,1543
    endpoint,path,_=M.path_current(n,2);assert endpoint==q
    before,after=M.RANK.absorption_plan(n),M.RANK.absorption_plan(q)
    assert before['coefficients']!=after['coefficients']
    difference=M.combine((1,before['coefficients']),(-1,after['coefficients']))
    assert difference=={29:1}
    transport_counter=dict(seed=n,endpoint=q,request_difference=difference,
                           current_difference=M.combine((1,before['current']),(-1,path),(-1,after['current'])))

    rejected=0
    for action in (lambda:M.macro(2781109),lambda:M.family(0),
                   lambda:M.family(2,-1),lambda:M.maximum(21),
                   lambda:M.repeated_plan(M.RESIDUE,2),
                   lambda:M.compile_plan(first_macro,{}),
                   lambda:M.compile_plan(first_macro,{v:{} for v in first_macro['coefficients']})):
        try:action()
        except (ValueError,AssertionError):rejected+=1
        else:raise AssertionError('Invalid or unsupplied request accepted')

    return dict(status='PASS',scope='Two specified valid plans, exact guarded growing blocks and finite-label height-monotone obstruction; no priority-dispatch or universal nontermination claim',
                complete_macros=len(macros),macro_hash=digest(macros),
                repetitions=repetitions,arithmetic_families=arithmetic,
                exact_exit_cases=len(exits),exit_hash=digest(exits),
                transport_counterexample=transport_counter,
                stored_macro=first_macro,stored_repetitions=stored,
                rejection_checks=rejected,
                caps=dict(full_macro_progressions=16,full_repeat_count=16,
                          explicit_macro_substitution_count=4,
                          arithmetic_repeat_count=256,index_bits=129,
                          ordinary_prefix_length=12*16+1),
                source_hashes={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                               for name in ('mixed_growth.py','check_mixed_growth.py')})


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--write-receipt',action='store_true')
    args=parser.parse_args()
    data=json.loads(json.dumps(audit(),sort_keys=True,
                    default=lambda x: {'numerator':x.numerator,'denominator':x.denominator}))
    path=HERE/'mixed_growth_audit.json'
    if args.write_receipt:path.write_text(json.dumps(data,sort_keys=True,indent=2)+'\n')
    else:assert json.loads(path.read_text())==data,'Receipt differs; inspect before regenerating'
    print('PASS: 16 complete macros, 12 full repetitions, 27 long families and 76 exact exits')


if __name__=='__main__':main()
