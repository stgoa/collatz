"""Check complete mixed shrinking-pair words and their signed currents."""
import argparse
import csv
import hashlib
import itertools
import json
from fractions import Fraction as F
from pathlib import Path
import mixed_pairs as M

HERE=Path(__file__).resolve().parent


def digest(current):
    return hashlib.sha256(''.join(f'{x},{c}\n' for x,c in sorted(current.items())).encode()).hexdigest()


def check_clock(w,data):
    length=M.merge_clock(data)
    assert M.prefix(3*w,length)[0][-1]==M.prefix(w,length+1)[0][-1]
    return length


def run():
    counts=dict(accepted=0,old_accepted=0,new_accepted=0,unresolved=0)
    kinds=dict(O=0,E1=0,E2=0)
    for w in range(3,32768,8):
        row=M.reduction(w)
        h,k,z=row['h'],row['k'],row['z']
        assert M.prefix(3*w,k)[0][-1]==(8*z+1 if h%2 else 4*z+1)
        assert M.prefix(w,k+1)[0][-1]==(4*z+1 if h%2 else 2*z+1)
        old=M.OLD.pair_plan(w)['accepted']
        data=M.plan(w)
        assert not old or data['accepted']
        counts['old_accepted']+=old
        if not data['accepted']:
            counts['unresolved']+=1
            continue
        certified=M.current(w)
        assert M.divergence(certified['current'])=={w:-1,3*w:1}
        check_clock(w,data)
        counts['accepted']+=1
        counts['new_accepted']+=not old
        for layer in data['layers'][:-1]:kinds[layer['kind']]+=1

    alphabet=(('O',0),('O',1),('E1',1),('E2',1))
    words=[word for size in range(4) for word in itertools.product(alphabet,repeat=size)]
    cylinder_cases=0
    for word in words:
        for terminal in (1,2):
            residue,modulus=M.word_cylinder(word,terminal)
            a,period=M.mersenne_cylinder(word,terminal)
            assert a%16==7 and period==2*modulus
            assert pow(3,a-1,8*modulus)==1+8*residue
            for offset in (0,1,7):
                w=residue+offset*modulus
                data=M.current(w)
                layers=data['plan']['layers']
                assert [(r['kind'],r['k']) for r in layers[:-1]]==list(word)
                assert layers[-1]['kind']=='terminal' and layers[-1]['k']==terminal
                assert layers[-1]['z']%8==1
                length=terminal+2+sum(k+(1 if kind=='O' else 2) for kind,k in word)
                assert check_clock(w,data['plan'])==length
                cylinder_cases+=1

    long_words=[]
    for depth in (1,2,4,8,16,32,64):
        for pattern in ((('O',0),),(('E1',1),),(('E2',1),),alphabet):
            word=tuple(pattern[i%len(pattern)] for i in range(depth))
            residue,modulus=M.word_cylinder(word)
            data=M.current(residue)
            assert len(data['plan']['layers'])==depth+1
            check_clock(residue,data['plan'])
            a,period=M.mersenne_cylinder(word)
            assert pow(3,a-1,8*modulus)==1+8*residue
            long_words.append(dict(depth=depth,pattern=pattern,seed_bits=residue.bit_length(),
                                   current_rows=len(data['current']),sha256=digest(data['current'])))

    t=F(1,6)
    branch_masses=dict(O=F(1,6),E1=F(1,96),E2=F(1,192))
    r=sum(branch_masses.values())
    assert r==F(35,192) and t/(1-r)==F(32,157)
    for K in (1,2,4,8,16):
        o=sum(F(1,2**M.affine('O',k)[2]) for k in range(K))
        e1=sum(F(1,2**M.affine('E1',k)[2]) for k in range(1,K+1))
        e2=sum(F(1,2**M.affine('E2',k)[2]) for k in range(1,K+1))
        assert o==branch_masses['O']*(1-F(1,4**K))
        assert e1==branch_masses['E1']*(1-F(1,4**K))
        assert e2==branch_masses['E2']*(1-F(1,4**K))

    exponent_examples=[]
    for word in ((('O',0),),(('O',1),),(('E1',1),),(('E2',1),),
                 (('O',0),('E1',1)),(('E2',1),('O',0))):
        a,period=M.mersenne_cylinder(word)
        exponent_examples.append(dict(word=word,a=a,period=period,
                                      additional_clock=3+sum(k+(1 if kind=='O' else 2)
                                                            for kind,k in word)))
    assert M.mersenne_cylinder((('O',0),))==(631,2048)
    assert M.mersenne_cylinder((('E1',1),))==(3655,32768)

    actual=[]
    for a in (39,631,2679,3655):
        data=M.mersenne_bridge(a)
        assert M.prefix(data['root'],data['merge_clock'])[0][-1]==M.prefix(data['lower_seed'],data['merge_clock'])[0][-1]
        assert M.OLD.RUN.H.TRANSFER.residual_coefficient(data['N'],data['root'])==1
        actual.append(dict(a=a,clock=data['merge_clock'],word=[(r['kind'],r['k'])
                           for r in data['plan']['layers']],current_rows=len(data['current']),
                           sha256=digest(data['current'])))

    # A genuine new Mersenne bridge: the supplied path does not already
    # contain x or f in its complete elementary-plus-forward closure.
    demo_a=631
    lower_seed=2**(demo_a-1)-1
    cap=5000
    lower=M.OLD.RUN.H.LOCAL.FORCING.absorption_current({lower_seed:1},cap=cap)
    converted=M.from_supplied_lower(demo_a,lower)
    known={1}|{M.NORMAL.normal_form(v) for v in lower}
    assert converted['data']['root'] not in known
    assert converted['data']['old_return'] not in known
    scaled=M.from_supplied_lower(demo_a,lower,weight=2)
    assert scaled['current']=={x:2*c for x,c in converted['current'].items()}

    # The unrestricted candidate would require an elementary bridge
    # 6z+1 -> 3z. At w19, z7 these are in different elementary components.
    failed=M.reduction(19)
    assert failed['h']==3 and failed['z']==7 and failed['kind']=='unresolved'
    assert M.NORMAL.normal_form(43)==43 and M.NORMAL.normal_form(21)==1
    for a in (7,23):assert not M.plan((3**(a-1)-1)//8)['accepted']
    stored=M.current(499)['current']
    receipt=dict(status='PASS',scope='Three complete shrinking branch domains; universal pair coverage open',
        w_domain=dict(first=3,last=32767,step=8,cases=4096,**counts),branch_uses=kinds,
        short_word_cylinders=dict(alphabet=alphabet,max_length=3,words=len(words),
                                 terminal_k=[1,2],offsets=[0,1,7],cases=cylinder_cases),
        long_word_cases=long_words,
        exact_relative_binary_measures=dict(terminal=str(t),recursive={k:str(v) for k,v in branch_masses.items()},
                                           accepted=str(t/(1-r)),unresolved=str(1-t/(1-r))),
        exponent_examples=exponent_examples,actual_mersenne_bridges=actual,
        supplied_conversion=dict(a=demo_a,lower_cap=cap,input_rows=len(lower),input_sha256=digest(lower),
            bridge_rows=len(converted['data']['current']),summed_rows=len(converted['signed_current']),
            output_rows=len(converted['current']),output_sha256=digest(converted['current']),
            root_and_old_return_absent_from_supplied_elementary_saturation=True,
            weight_two_scaling_checked=True,output_uses_only_summed_rows=True),
        rejected_unrestricted_odd_rule=dict(w=19,z=7,left_normal=43,right_normal=1),
        unresolved_exponents=[7,23],small_current=dict(w=499,rows=len(stored),sha256=digest(stored)))
    return receipt,stored


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-receipt',action='store_true')
    args=parser.parse_args()
    receipt,current=run()
    audit=HERE/'mixed_pairs_audit.json';table=HERE/'pair_499_current.csv'
    if args.write_receipt:
        audit.write_text(json.dumps(receipt,indent=2)+'\n')
        with table.open('w',newline='') as out:
            writer=csv.writer(out,lineterminator='\n');writer.writerow(('state','current'))
            writer.writerows(sorted(current.items()))
    else:
        assert json.loads(audit.read_text())==json.loads(json.dumps(receipt))
        with table.open(newline='') as source:
            saved={int(r['state']):int(r['current']) for r in csv.DictReader(source)}
        assert saved==current
    print(f"PASS: 4096 pairs; {receipt['short_word_cylinders']['cases']} mixed cylinders; "
          f"{len(receipt['long_word_cases'])} long words; four Mersenne bridges; "
          "one supplied-current conversion; exact cylinder measure32/157")


if __name__=='__main__':main()
