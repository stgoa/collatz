"""Read-only exact audit of the two missing-domain branches."""
import argparse
import csv
import hashlib
import itertools
import json
from pathlib import Path
import pair_one as P

HERE=Path(__file__).resolve().parent


def digest(rows):
    payload='\n'.join(f'{x:x}:{c}' for x,c in sorted(rows.items()))
    return hashlib.sha256(payload.encode()).hexdigest()


def check_clock(w, clock):
    left,_=P.prefix(3*w,clock)
    right,_=P.prefix(w,clock+1)
    assert left[-1]==right[-1]


def audit():
    counts=dict(inputs=4096, A=0, B=0, parent_unresolved=0,
                accepted=0, child_unresolved=0)
    for w in range(1,32768,8):
        red=P.reduction(w)
        kind=red['kind']
        if kind=='unresolved':
            counts['parent_unresolved']+=1
            continue
        counts[kind]+=1
        local=P.local_current(w)
        child=P.MIXED.plan(red['child'])
        if child['accepted']:
            out=P.current(w)
            assert P.divergence(out['current'])=={3*w:1,w:-1}
            check_clock(w,out['clock'])
            counts['accepted']+=1
        else:counts['child_unresolved']+=1
    symbols=(('O',0),('E1',1),('E2',1))
    words=[word for depth in range(4)
           for word in itertools.product(symbols,repeat=depth)]
    words += [tuple(symbols[i%3] for i in range(depth)) for depth in (8,16,32,64)]
    cylinders=[]
    exponent_lifts=[]
    for kind in ('A','B'):
        for word in words:
            child_r,child_m=P.MIXED.word_cylinder(word)
            if kind=='B' and child_r%16!=11:continue
            r,m=P.cylinder(kind,word)
            a,period=P.exponent_cylinder(kind,word)
            assert a%16==3 and period==2*m
            assert pow(3,a-1,8*m)==(1+8*r)%(8*m)
            exponent_lifts.append(dict(kind=kind,word=[list(symbol) for symbol in word],a=a,period=period))
            for offset in (0,1,7):
                w=P.synthetic(kind,word,offset=offset)
                assert w%m==r
                out=P.current(w)
                assert [tuple((z['kind'],z['k'])) for z in out['child_plan']['layers'][:-1]]==list(word)
                check_clock(w,out['clock'])
                cylinders.append(dict(kind=kind,depth=len(word),offset=offset,
                                      bits=w.bit_length(),clock=out['clock'],
                                      rows=len(out['current']),sha256=digest(out['current'])))
    actual=[]
    for a in (659,1699,4755,5795):
        data=P.mersenne_bridge(a)
        assert data['old_normalized_return']>data['root']>data['N']>data['lower']
        left,_=P.prefix(data['root'],data['clock'])
        right,_=P.prefix(data['lower'],data['clock'])
        assert left[-1]==right[-1]
        # The actual source is weight1 in the upper part of R_N.
        assert data['root']%12==7
        assert 9*data['N']<8*data['root']<12*data['N']
        actual.append(dict(a=a,clock=data['clock'],rows=len(data['current']),
                           sha256=digest(data['current'])))
    unresolved=P.reduction((3**146-1)//8)
    assert unresolved['kind']=='B' and not P.MIXED.plan(unresolved['child'])['accepted']
    cap=10000
    large=P.mersenne_bridge(659)
    supplied=P.RUN.H.LOCAL.FORCING.absorption_current({large['lower']:1},cap=cap)
    converted=P.from_supplied_lower(659,supplied)
    doubled=P.from_supplied_lower(659,supplied,weight=2)
    assert doubled['current']=={x:2*c for x,c in converted['current'].items()}
    w=105
    pair=P.current(w)
    lower=P.RUN.H.LOCAL.FORCING.absorption_current({w:1},cap=cap)
    signed=P.combine((1,pair['current']),(1,lower))
    assert P.divergence(signed)=={3*w:1}
    small=P.RUN.H.COMPLEMENT.extract_exact({3*w:1},{x:P.step(x) for x in signed})
    result=dict(status='PASS',scope='Two partial 1-mod-8 pair branches; universal coverage open',
                direct_domains=counts,mixed_cylinders=cylinders,exponent_lifts=exponent_lifts,
                actual_mersenne_bridges=actual,unresolved_exponent=147,
                supplied_conversion=dict(a=659,input_cap=cap,input_rows=len(supplied),
                    input_sha256=digest(supplied),output_rows=len(converted['current']),
                    output_sha256=digest(converted['current']),weight2_checked=True),
                small_current=dict(root=315,lower=105,rows=len(small),sha256=digest(small)))
    return result,small


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--write-receipt',action='store_true')
    args=parser.parse_args()
    result,small=audit()
    receipt=HERE/'pair_one_audit.json'
    table=HERE/'pair_315_current.csv'
    if args.write_receipt:
        receipt.write_text(json.dumps(result,indent=2)+'\n')
        with table.open('w',newline='') as out:
            writer=csv.writer(out,lineterminator='\n')
            writer.writerow(('state','current'))
            writer.writerows(sorted(small.items()))
    else:
        assert json.loads(receipt.read_text())==result
        with table.open() as source:
            stored={int(r['state']):int(r['current']) for r in csv.DictReader(source)}
        assert stored==small and P.divergence(stored)=={315:1}
    print(f"PASS: 4096 inputs; {len(result['mixed_cylinders'])} cylinders; "
          f"{len(result['exponent_lifts'])} lifts; four Mersenne bridges; two supplied conversions")


if __name__=='__main__':main()
