"""Check shrinking paired currents, their complete cylinders, and one input conversion."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import paired_return as P

HERE=Path(__file__).resolve().parent


def digest(current):
    return hashlib.sha256(''.join(f'{x},{c}\n' for x,c in sorted(current.items())).encode()).hexdigest()


def run():
    counts=dict(accepted=0,terminal=0,recursive=0,unresolved=0)
    for w in range(3,32768,8):
        plan=P.pair_plan(w)
        if not plan['accepted']:
            counts['unresolved']+=1
            continue
        data=P.pair_current(w)
        assert P.divergence(data['current'])=={w:-1,3*w:1}
        length=P.merge_clock(plan)
        assert P.prefix(3*w,length)[0][-1]==P.prefix(w,length+1)[0][-1]
        counts['accepted']+=1
        counts['recursive' if len(plan['layers'])>1 else 'terminal']+=1

    terminal_cases=0
    for k in range(1,25):
        residue,modulus=P.terminal_cylinder(k)
        for offset in (0,1,7):
            w=residue+modulus*offset
            data=P.pair_current(w)
            assert len(data['plan']['layers'])==1
            layer=data['plan']['layers'][0]
            assert layer['k']==k and layer['z']%8==1
            terminal_cases+=1

    recursive=[]
    for depth in [*range(25),32,48,64]:
        residue,modulus=P.recursive_cylinder(depth)
        for offset in (0,1):
            w=P.synthetic_pair(depth,offset)
            assert w%modulus==residue
            data=P.pair_current(w)
            layers=data['plan']['layers']
            assert len(layers)==depth+1 and all(row['k']==1 for row in layers)
            assert all(row['kind']=='recursive' for row in layers[:-1])
            assert layers[-1]['kind']=='terminal' and layers[-1]['w']%128==59
            assert P.divergence(data['current'])=={w:-1,3*w:1}
            length=P.merge_clock(data['plan'])
            assert length==3*depth+3
            assert P.prefix(3*w,length)[0][-1]==P.prefix(w,length+1)[0][-1]
            recursive.append(dict(depth=depth,offset=offset,seed_bits=w.bit_length(),
                                  current_rows=len(data['current']),sha256=digest(data['current'])))

    exponent_cylinders=[]
    for depth in range(65):
        residue,modulus=P.recursive_cylinder(depth)
        a,period=P.recursive_mersenne_cylinder(depth)
        assert a%16==7 and period==2*modulus
        assert pow(3,a-1,8*modulus)==1+8*residue
        assert pow(3,period,8*modulus)==1
        if depth<5:
            exponent_cylinders.append(dict(depth=depth,w_residue=residue,
                                          w_period=modulus,a_residue=a,a_period=period))
    assert P.recursive_mersenne_cylinder(0)==(199,256)
    assert P.recursive_mersenne_cylinder(1)==(2887,65536)

    # A different first branch, k=3, followed by the same terminal cylinder.
    modulus=2**19
    residue=((59*4096-175)*pow(243,-1,modulus))%modulus
    assert P.mersenne_exponent_cylinder(residue,modulus)==(39,2**20)
    assert P.pair_plan(residue)['accepted']

    mersenne=[]
    for a in (39,135,199,263,423,455,711,2887):
        data=P.mersenne_bridge(a)
        assert P.RUN.H.TRANSFER.residual_coefficient(data['N'],data['root'])==1
        assert data['old_return']>data['root'] and data['lower_seed']<data['N']
        f=data['old_return']
        assert P.NORMAL.valuation2(3*f+1)==2
        assert P.step(f)==(3**(a+1)-1)//32
        length=a+P.merge_clock(data['pair_plan'])
        assert P.prefix(data['root'],length)[0][-1]==P.prefix(data['lower_seed'],length)[0][-1]
        mersenne.append(dict(a=a,root_bits=data['root'].bit_length(),
                             old_return_bits=f.bit_length(),
                             pair_k_word=[row['k'] for row in data['pair_plan']['layers']],
                             equal_prefix_clock=length,
                             current_rows=len(data['current']),sha256=digest(data['current'])))
    for a in (7,23):
        assert not P.pair_plan((3**(a-1)-1)//8)['accepted']

    # Only this finite demonstration discovers an absorption path. The new
    # constructor receives that path as its input and never searches its future.
    a=39
    lower_seed=2**(a-1)-1
    cap=5000
    lower=P.RUN.H.LOCAL.FORCING.absorption_current({lower_seed:1},cap=cap)
    conversion=P.from_supplied_lower(a,lower)
    twice=P.from_supplied_lower(a,lower,weight=2)
    assert twice['current']=={x:2*c for x,c in conversion['current'].items()}
    data=conversion['data']
    receipt=dict(status='PASS',scope='Partial, terminating signed-pair recognizer; universal coverage open',
                 seed_domain=dict(first=3,last=32767,step=8,cases=4096,**counts),
                 terminal_cylinders=dict(k_first=1,k_last=24,offsets=[0,1,7],cases=terminal_cases),
                 recursive_integer_cases=recursive,
                 modular_exponent_lifts_checked=[0,64],
                 first_exponent_cylinders=exponent_cylinders,
                 secondary_exponent_cylinder=dict(a_residue=39,a_period=2**20,k_word=[3,1]),
                 actual_mersenne_bridges=mersenne,
                 unresolved_mersenne_examples=[7,23],
                 actual_conversion=dict(a=a,N=data['N'],root=data['root'],lower_seed=lower_seed,
                     old_canonical_return=data['old_return'],known_later_state=data['w'],
                     lower_input_cap=cap,lower_input_rows=len(lower),lower_input_sha256=digest(lower),
                     bridge_rows=len(data['current']),bridge_sha256=digest(data['current']),
                     summed_signed_rows=len(conversion['signed_current']),
                     output_rows=len(conversion['current']),output_sha256=digest(conversion['current']),
                     weight_two_scaling_checked=True,
                     output_edges_subset_of_summed_supplied_and_explicit_rows=True))
    return receipt,conversion['current']


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-receipt',action='store_true')
    args=parser.parse_args()
    receipt,current=run()
    receipt_path=HERE/'paired_return_audit.json'
    current_path=HERE/'mersenne_39_current.csv'
    if args.write_receipt:
        receipt_path.write_text(json.dumps(receipt,indent=2)+'\n')
        with current_path.open('w',newline='') as out:
            writer=csv.writer(out,lineterminator='\n')
            writer.writerow(('state','current'))
            writer.writerows(sorted(current.items()))
    else:
        assert json.loads(receipt_path.read_text())==receipt
        with current_path.open(newline='') as source:
            stored={int(row['state']):int(row['current']) for row in csv.DictReader(source)}
        assert stored==current
    print(f"PASS: 4096 pairs; {receipt['terminal_cylinders']['cases']} terminal cylinders; "
          f"{len(receipt['recursive_integer_cases'])} recursive pairs; 65 exact exponent lifts; "
          f"{len(receipt['actual_mersenne_bridges'])} Mersenne bridges; one supplied-current conversion")


if __name__=='__main__':
    main()
